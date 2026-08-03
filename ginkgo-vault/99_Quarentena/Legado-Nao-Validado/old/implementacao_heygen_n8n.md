# Guia de Implementação: Automação de Vídeos HeyGen + n8n + Ginkgo

## 1. Setup Inicial

### 1.1 Credenciais Necessárias

| Serviço | Credencial | Onde Obter |
| :--- | :--- | :--- |
| HeyGen | API Key | Dashboard → Settings → API |
| HeyGen | Avatar ID (Nyra) | Dashboard → Create Avatar → Photo Avatar |
| HeyGen | Voice ID | API `/v2/voices` ou Dashboard |
| OpenAI | API Key | platform.openai.com → API Keys |
| Supabase | URL + Anon Key | Project Settings → API |
| Evolution API | URL + Token | Seu servidor Evolution |

### 1.2 Configurar Credenciais no n8n

1. Acesse **Credentials** no n8n.
2. Crie uma nova credencial do tipo **HTTP Header Auth** para HeyGen:
   - Nome: `HeyGen API`
   - Header: `X-API-KEY`
   - Value: `<sua_api_key_heygen>`

3. Crie uma credencial do tipo **API Key** para OpenAI.
4. Crie uma credencial do tipo **Supabase** com URL e chave.

## 2. Workflow 1: Solicitação de Vídeo (Geração)

Este workflow é acionado quando um novo cliente/ideia chega (via formulário, webhook ou schedule).

### 2.1 Estrutura do Workflow

```
[Trigger] → [Gerar Script] → [Chamar HeyGen] → [Salvar no Supabase]
```

### 2.2 Nós Detalhados

#### Nó 1: Webhook Trigger (ou Schedule)
- **Tipo**: Webhook / Schedule
- **Descrição**: Recebe dados do cliente ou é acionado em horários específicos.
- **Saída esperada**:
  ```json
  {
    "cliente_nome": "João Silva",
    "dor_principal": "Demora em responder cliente",
    "tempo_resposta": "2 horas"
  }
  ```

#### Nó 2: OpenAI - Gerar Script
- **Tipo**: HTTP Request (ou usar nó OpenAI se disponível)
- **Endpoint**: `POST https://api.openai.com/v1/chat/completions`
- **Headers**: 
  - `Authorization: Bearer {{ $credentials.openai_api_key }}`
  - `Content-Type: application/json`
- **Body**:
  ```json
  {
    "model": "gpt-4o-mini",
    "messages": [
      {
        "role": "system",
        "content": "Você é a Nyra, uma IA que faz entrevistas virais na rua. Seu estilo é direto, provocativo e educativo. Sempre questione a dor do cliente e apresente a solução Ginkgo."
      },
      {
        "role": "user",
        "content": "Crie um script curto (máximo 30 segundos) para um vídeo onde você questiona um {{ $json.cliente_nome }} sobre '{{ $json.dor_principal }}' e depois apresenta como a Ginkgo resolve isso. O tempo atual de resposta dele é {{ $json.tempo_resposta }}."
      }
    ],
    "max_tokens": 200
  }
  ```
- **Saída**: `script` (texto do vídeo)

#### Nó 3: HeyGen - Criar Vídeo
- **Tipo**: HTTP Request
- **Endpoint**: `POST https://api.heygen.com/v2/video/generate`
- **Headers**: 
  - `X-API-KEY: {{ $credentials.heygen_api_key }}`
  - `Content-Type: application/json`
- **Body**:
  ```json
  {
    "title": "Nyra na Rua - {{ $json.cliente_nome }}",
    "caption": true,
    "dimension": {
      "width": 1080,
      "height": 1920
    },
    "callback_id": "{{ $json.cliente_nome }}_{{ Date.now() }}",
    "video_inputs": [
      {
        "character": {
          "type": "avatar",
          "avatar_id": "{{ $env.HEYGEN_AVATAR_ID }}",
          "avatar_style": "normal"
        },
        "voice": {
          "type": "text",
          "input_text": "{{ $json.script }}",
          "voice_id": "{{ $env.HEYGEN_VOICE_ID }}",
          "speed": 1.0
        },
        "background": {
          "type": "color",
          "value": "#000000"
        }
      }
    ]
  }
  ```
- **Saída**: `video_id`, `status`

#### Nó 4: Supabase - Inserir Registro
- **Tipo**: Supabase (Insert)
- **Tabela**: `heygen_videos`
- **Dados**:
  ```json
  {
    "video_id": "{{ $json.video_id }}",
    "status": "pending",
    "script": "{{ $json.script }}",
    "lead_id": "{{ $json.lead_id }}",
    "callback_id": "{{ $json.callback_id }}"
  }
  ```

### 2.3 Tratamento de Erros

Adicione um nó **Error Handler** após o nó HeyGen:
- Se falhar, registre o erro no Supabase com `status: "failed"` e `error_message`.

## 3. Workflow 2: Webhook de Conclusão (Distribuição)

Este workflow é acionado quando o HeyGen notifica que o vídeo está pronto.

### 3.1 Estrutura do Workflow

```
[Webhook HeyGen] → [Atualizar Supabase] → [Baixar Vídeo] → [Enviar WhatsApp/Drive]
```

### 3.2 Nós Detalhados

#### Nó 1: Webhook Trigger (HeyGen Callback)
- **Tipo**: Webhook
- **URL**: Configure no HeyGen Dashboard ou passe na requisição anterior.
- **Payload esperado do HeyGen**:
  ```json
  {
    "event_type": "video_completed",
    "video_id": "abc123",
    "status": "completed",
    "video_url": "https://...",
    "callback_id": "João Silva_1234567890"
  }
  ```

#### Nó 2: Supabase - Buscar Registro
- **Tipo**: Supabase (Select)
- **Tabela**: `heygen_videos`
- **Filtro**: `video_id = {{ $json.video_id }}`
- **Saída**: Registro completo com `lead_id`, `cliente_nome`, etc.

#### Nó 3: Supabase - Atualizar Status
- **Tipo**: Supabase (Update)
- **Tabela**: `heygen_videos`
- **Filtro**: `video_id = {{ $json.video_id }}`
- **Dados**:
  ```json
  {
    "status": "completed",
    "video_url": "{{ $json.video_url }}"
  }
  ```

#### Nó 4: HTTP Request - Baixar Vídeo
- **Tipo**: HTTP Request
- **Método**: GET
- **URL**: `{{ $json.video_url }}`
- **Salvar como arquivo**: Ativar
- **Caminho**: `/tmp/{{ $json.video_id }}.mp4`

#### Nó 5: Evolution API - Enviar WhatsApp
- **Tipo**: HTTP Request (ou nó customizado Evolution)
- **Endpoint**: `POST https://<seu_evolution_url>/message/sendMedia`
- **Body**:
  ```json
  {
    "number": "{{ $json.lead_phone }}",
    "mediaType": "video",
    "media": "{{ $json.video_url }}",
    "caption": "Confira este vídeo especial sobre como a Ginkgo pode transformar seu negócio! 🚀"
  }
  ```

#### Nó 6 (Alternativa): Google Drive - Salvar Vídeo
- **Tipo**: Google Drive (Upload)
- **Pasta**: Criar pasta dinâmica `/Ginkgo/Vídeos/{{ $json.mes }}/`
- **Arquivo**: `{{ $json.cliente_nome }}_{{ $json.video_id }}.mp4`

## 4. Prompt da Nyra (Para OpenAI)

Use este prompt no Nó 2 do Workflow 1 para manter consistência:

```
Você é a Nyra, uma IA especialista em criar conteúdo viral sobre automação e IA.

ESTILO:
- Direto e provocativo
- Faz perguntas que desafiam o status quo
- Apresenta a solução Ginkgo como a resposta óbvia
- Usa linguagem coloquial, como se estivesse na rua
- Cria urgência e consciência da dor

ESTRUTURA DO VÍDEO (máximo 30 segundos):
1. Hook: Pergunta provocativa sobre a dor do cliente
2. Validação: Reconhecer que é um problema comum
3. Demonstração: Mostrar como a Ginkgo resolve
4. CTA: Chamar para ação

EXEMPLO:
"Tu responde cliente em quanto tempo? Ah, depende? Então já perdeu. Enquanto você tá pensando, o cliente já foi pra concorrência. A Ginkgo não depende. Ela responde na hora, qualifica e marca reunião. Tudo automático. Quer ver como?"

DADOS DO CLIENTE:
- Nome: {{ cliente_nome }}
- Dor: {{ dor_principal }}
- Contexto: {{ contexto_adicional }}

Crie um script similar, adaptado para este cliente específico. Máximo 100 palavras.
```

## 5. Configuração de Webhook no HeyGen

Existem duas formas:

### Opção A: Webhook Global (Dashboard)
1. Acesse HeyGen Dashboard → Settings → Webhooks.
2. Adicione a URL do seu webhook n8n: `https://seu-n8n.com/webhook/heygen-callback`
3. Selecione os eventos: `video_completed`, `video_failed`.

### Opção B: Webhook por Vídeo (Recomendado)
Passe o `callback_url` na requisição de criação do vídeo (Nó 3, Workflow 1):

```json
"callback_url": "https://seu-n8n.com/webhook/heygen-callback"
```

## 6. Estrutura de Dados (Supabase SQL)

```sql
CREATE TABLE heygen_videos (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  video_id TEXT UNIQUE NOT NULL,
  status TEXT NOT NULL DEFAULT 'pending', -- pending, processing, completed, failed
  script TEXT NOT NULL,
  video_url TEXT,
  lead_id UUID REFERENCES leads(id),
  callback_id TEXT,
  error_message TEXT,
  
  CONSTRAINT status_check CHECK (status IN ('pending', 'processing', 'completed', 'failed'))
);

CREATE INDEX idx_video_id ON heygen_videos(video_id);
CREATE INDEX idx_status ON heygen_videos(status);
CREATE INDEX idx_lead_id ON heygen_videos(lead_id);
```

## 7. Escalabilidade e Otimizações

### 7.1 Fila de Processamento
Para evitar limites de taxa (rate limiting) do HeyGen:
- Configure o n8n para processar máximo 5 vídeos por hora.
- Use o nó **Wait** entre requisições.

### 7.2 Retry Logic
Se a criação falhar:
- Retentar automaticamente após 5 minutos.
- Máximo de 3 tentativas.

### 7.3 Monitoramento
- Crie um dashboard no n8n que mostre:
  - Total de vídeos gerados hoje.
  - Taxa de sucesso/falha.
  - Custo estimado (vídeos × custo unitário).

## 8. Custos Estimados (Mensal)

Assumindo 100 vídeos/mês:

| Item | Custo |
| :--- | :--- |
| HeyGen (100 vídeos × $0.15) | $15 |
| OpenAI (100 scripts × $0.01) | $1 |
| n8n (2 workflows) | $10 (plano starter) |
| Supabase | $5 (incluído no plano starter) |
| **Total** | **~$31/mês** |

Para 1000 vídeos/mês: ~$200/mês (com descontos em volume).

## 9. Próximos Passos

1. **Implementação**: Criar os workflows no n8n conforme descrito.
2. **Testes**: Rodar com 5 vídeos teste para validar o fluxo completo.
3. **Integração Brann**: Conectar o webhook de conclusão ao Brann para qualificação automática.
4. **Distribuição**: Plugar a saída nos canais (WhatsApp, Reels, TikTok).
5. **Análise**: Medir taxa de clique, conversão e ROI dos vídeos.

---

**Nota**: Este guia assume que você já tem acesso ao n8n self-hosted ou cloud. Se precisar de ajustes específicos ou tiver dúvidas sobre algum nó, entre em contato.
