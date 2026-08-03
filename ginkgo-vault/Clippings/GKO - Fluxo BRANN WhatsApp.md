---
title: "GKO - Fluxo BRANN WhatsApp"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/68c694fc-397c-8328-892b-154b8af5efb1"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
tudo certo?

os switchs

Perfeito. Bora fechar o resto do circuito — vou te passar **campo a campo** o que preencher em cada nó que aparece no teu print.

---

## Downloads de mídia (para cada ramo)

## IF “tem URL?”

- **Expression (fx):**  
	`{{$json.audioUrl && $json.audioUrl.startsWith('http')}}`  
	(troque `audioUrl` por `videoUrl` ou `imageUrl` nos outros ramos)

### GET (quando TRUE)

- **URL:** `={{$json.audioUrl}}`
- **Response Format:** `File`
- **Binary Property:** `audio`

> Vídeo/imagem: mude para `={{$json.videoUrl}}` / `={{$json.imageUrl}}` e `binaryPropertyName` = `video` / `image`.

### POST (quando FALSE) – Evolution

- **URL:** `={{$env.EVOLUTION_BASE_URL}}/message/downloadMedia/{{$env.EVOLUTION_INSTANCE}}`
- **Method:** `POST`
- **Send Headers:** ON  
	**Headers JSON:**
	```markdown
	{"Authorization":"={{'Bearer ' + $env.EVOLUTION_TOKEN}}","Content-Type":"application/json"}
	```
- **Body (JSON):**
	```markdown
	{"messageId":"={{$json.messageId}}"}
	```
- **Response Format:** `File`
- **Binary Property:** `audio` (ou `video` / `image` conforme o ramo)

---

## Nós de IA (por tipo de mídia)

## Áudio → OpenAI Chat Model

- **Model:** `gpt-4o-mini`
- **System:** `Transcreva áudio PT-BR. Retorne somente o texto.`
- **Message:** **binário** (não texto)
- **Options:** temperature `0.3`, maxTokens `1000`

## Vídeo → OpenAI Chat Model

- **Model:** `gpt-4o-mini`
- **System:** `Resuma/transcreva a fala do vídeo em PT-BR. Retorne só texto.`
- **Message:** **binário** `video`
- **Options:** temperature `0.3`, maxTokens `1000`

## Imagem → OpenAI (visão)

- **Model:** `gpt-4o-mini`
- **Image Binary Property:** `image`
- **System:**  
	`Descreva a imagem em 1–3 frases úteis para atendimento comercial; se houver texto legível, inclua. Responda em JSON: { "text": "..." }.`
- **Options:** temperature `0.3`, maxTokens `400`

---

## Normalização para text

Nos teus “Format Response” / “Get User’s Message” (nós Set/Function), garanta que **sempre** exista `json.text`.

- **Set (áudio/vídeo):**  
	`text = {{$json.text || $json.output_text || $json.transcript}}`
- **Set (imagem):**  
	`text = {{$json.text || $json.caption || $json.description || $json.result}}`
- **Texto puro (Summarizer opcional):**  
	Se usar Summarizer, no final faça `text = {{$json.summary || $json.text}}`.

---

## Wait (meio do fluxo)

- **Amount:** `1`
- **Unit:** `seconds`

---

## BRANN (modelo + memória + ferramentas)

**OpenAI Chat Model**

- **Model:** `gpt-4o-mini`
- **Temperature:** `0.4`
- **Max tokens:** `1400`
- **Message:** `={{$json.text}}`
- **System (cole igual):**
```markdown
Você é o assistente corporativo da Ginkgo AI Systems.
Objetivos: compreender intenção, orientar claramente e encaminhar para solução com o menor atrito possível.
Prioridades: precisão, concisão, cordialidade profissional.
Sempre que fizer sentido, ofereça:
- Assinaturas Ginkgo (produtos/planos);
- Projeto Personalizado (escopo sob medida);
- Contato com humano (vendas/suporte).

Formato OBRIGATÓRIO (JSON em out) — escolha apenas 1:
{ "out": { "type": "text", "text": "..." } }
{ "out": { "type": "buttons", "text": "...", "buttons": [ {"id":"planos","text":"Ver Planos"}, {"id":"projeto","text":"Projeto Personalizado"}, {"id":"humano","text":"Falar com Humano"} ] } }
{ "out": { "type": "list", "text": "...", "sections": [ { "title":"Assinaturas", "rows":[ {"id":"plano_basico","title":"Plano Básico","description":"Essencial"}, {"id":"plano_futurista","title":"Plano Futurista","description":"IA avançada"} ] }, { "title":"Outros", "rows":[ {"id":"projeto","title":"Projeto Personalizado"}, {"id":"humano","title":"Falar com Humano"} ] } ] } }
{ "out": { "type": "image", "imageUrl": "https://...", "caption": "..." } }
{ "out": { "type": "audio", "audioUrl": "https://..." } }
{ "out": { "type": "audio_key", "key": "automacao|proposta|cases|onboarding|precos" } }
```

**Postgres Chat Memory (seu nó de memória)**

- **Session ID:** `={{$json.phone || $json.chatId}}`
- Janela: **10–20** últimas; **TTL** 30–60 dias (a gosto).

---

## Parser Chain (Function) — garante out.type sempre

Cole **exatamente** no teu “Parser”:

```markdown
const it = items[0].json;
let out = it.out;

if (!out) {
  try { out = JSON.parse(it)?.out; } catch(e) {}
}

if (!out) {
  if (typeof it === 'string') {
    out = { type: 'text', text: it };
  } else {
    out = { type: 'text', text: it.text || 'Certo! Vamos em frente.' };
  }
}

const ok = new Set(['text','buttons','list','image','audio','audio_key']);
if (!ok.has(out.type)) {
  out = { type: 'text', text: '[Parser] Formato inválido. Seguindo no texto.' };
}

return [{ json: { ...it, out } }];
```

---

## Segmentos (Switch por out.type)

- **Property Name (fx):** `{{$json.out.type}}`
- **Rules (equal):** `text`, `buttons`, `list`, `image`, `audio`, `audio_key`
- Saídas nessas **6** ordens para os nós de envio correspondentes (e o subfluxo no caso do `audio_key`).

---

## Envio (Evolution)

Todos os nós HTTP com:

- **URL base:** `={{$env.EVOLUTION_BASE_URL}}`
- **Headers JSON:**
	```markdown
	{"Authorization":"={{'Bearer ' + $env.EVOLUTION_TOKEN}}","Content-Type":"application/json"}
	```
- **Instance:** `{{$env.EVOLUTION_INSTANCE}}`

### Text

- **Endpoint:** `/message/sendText/{{$env.EVOLUTION_INSTANCE}}`
- **Body (JSON):**
```markdown
{
  "number": "={{$json.phone || $json.chatId}}",
  "options": { "delay": 800, "presence": "composing" },
  "textMessage": { "text": "={{$json.out.text}}" }
}
```

### Buttons

- **Endpoint:** `/message/sendButtons/{{$env.EVOLUTION_INSTANCE}}`
- **Body:**
```markdown
{
  "number": "={{$json.phone || $json.chatId}}",
  "buttonMessage": { "text": "={{$json.out.text}}", "buttons": "={{$json.out.buttons}}" }
}
```

### List

- **Endpoint:** `/message/sendList/{{$env.EVOLUTION_INSTANCE}}`
- **Body:**
```markdown
{
  "number": "={{$json.phone || $json.chatId}}",
  "listMessage": {
    "title": "Ginkgo AI Systems",
    "text": "={{$json.out.text}}",
    "buttonText": "Abrir opções",
    "sections": "={{$json.out.sections}}"
  }
}
```

### Image (URL)

- **Endpoint:** `/message/sendMedia/{{$env.EVOLUTION_INSTANCE}}`
- **Body:**
```markdown
{
  "number": "={{$json.phone || $json.chatId}}",
  "mediaData": { "url": "={{$json.out.imageUrl}}", "caption": "={{$json.out.caption || ''}}" }
}
```

### Audio (URL / PTT)

- **Endpoint:** `/message/sendAudio/{{$env.EVOLUTION_INSTANCE}}`
- **Body:**
```markdown
{
  "number": "={{$json.phone || $json.chatId}}",
  "mediaData": { "url": "={{$json.out.audioUrl}}", "ptt": true }
}
```

### audio\_key → Subfluxo

- **Execute Workflow** → `waitForCompletion: ON`
- **Input:**  
	`{ "phone":"={{$json.phone || $json.chatId}}", "key":"={{$json.out.key}}", "text":"={{$json.text}}" }`

---

## Loop Over Items

- Se o Parser devolver **um** objeto, você pode remover o loop.
- Se preferir manter, garanta que a entrada esteja como **array** (marque “Always output array” no Parser ou faça um pequeno Set para embrulhar).

---

## Wait final

- **Amount:** `1`
- **Unit:** `seconds`  
	(se quiser “1.2s” e o nó só aceita segundos inteiros, deixa 1s mesmo)

---

## Smoke test (agora)

1. **Texto** “oi” → deve ir pro Summarizer (se ativo) → BRANN → `sendText`.
2. **Imagem com legenda** → “Image Explainer” → `text` → BRANN → `sendText`.
3. **PTT** → transcreve → BRANN → `sendText`.
4. Palavra-chave **“automação”** → BRANN **`audio_key`** → **Execute Subfluxo AUDIO** → envia PTT.

Se algum ponto não disparar, me diga **qual nó ficou vermelho** e **o tipo de mídia** — te mando o patch da configuração daquele nó na hora.

Show! Esse é o ponto certo do fluxo. Aqui vai **o que selecionar e o que colar** no nó **BRANN** para casar com o parser/segmentos que já fizemos.

## O que escolher no dropdown “Agente”

- **Escolha:** **Agente Conversacional**  
	Motivo: nosso Parser espera **sempre** um JSON em `out` (sem “tool calls”). O *Agente de Ferramentas* pode responder com chamadas de ferramenta no formato interno do agente, e aí você teria que mudar o Parser. Então, para ficar plug-and-play com o fluxo atual, use **Agente Conversacional**.

## Parâmetros (preencha exatamente assim)

**Modelo de bate-papo:** `gpt-4o-mini`  
**Temperatura:** `0.4`  
**Máx tokens de saída:** `1400`  
**Idioma:** `pt-BR` (se existir esse campo)

**Instrução do sistema (cole tudo):**

```markdown
Você é o assistente corporativo da Ginkgo AI Systems.
Objetivos: compreender intenção, orientar claramente e encaminhar para solução com o menor atrito possível.
Prioridades: precisão, concisão, cordialidade profissional.

Formato OBRIGATÓRIO (retorne SEMPRE JSON válido):
{ "out": { "type": "text", "text": "..." } }
{ "out": { "type": "buttons", "text": "...", "buttons": [ {"id":"planos","text":"Ver Planos"}, {"id":"projeto","text":"Projeto Personalizado"}, {"id":"humano","text":"Falar com Humano"} ] } }
{ "out": { "type": "list", "text": "...", "sections": [ { "title":"Assinaturas", "rows":[ {"id":"plano_basico","title":"Plano Básico","description":"Essencial"}, {"id":"plano_futurista","title":"Plano Futurista","description":"IA avançada"} ] }, { "title":"Outros", "rows":[ {"id":"projeto","title":"Projeto Personalizado"}, {"id":"humano","title":"Falar com Humano"} ] } ] } }
{ "out": { "type": "image", "imageUrl": "https://...", "caption": "..." } }
{ "out": { "type": "audio", "audioUrl": "https://..." } }
{ "out": { "type": "audio_key", "key": "automacao|proposta|cases|onboarding|precos" } }

REGRAS:
- Nunca responda fora do JSON acima.
- Se tiver dúvida, devolva { "out": { "type": "text", "text": "Poderia detalhar?" } }.
- Para áudio pronto, use "audio_key" (NÃO gere URL); quem envia o PTT é outro subfluxo.
- Seja breve e direto.
```

## Aba “Memória”

Conecte o **Postgres Chat Memory** (o nó que você já tem com os pontilhados para o BRANN):

- **Session ID (expr):** `={{$json.phone || $json.chatId}}`
- **Mensagens por sessão:** 10–20
- **TTL:** 30–60 dias

## Aba “Ferramentas”

- **Nenhuma ferramenta obrigatória** neste modo (Conversacional).
- Se mais tarde você quiser buscas factuais, aí sim trocamos para **Agente de Ferramentas** e eu te passo o schema do `web.search` (SerpAPI) + throttling. Por ora, mantenha limpo para preservar o formato de saída.

## Teste rápido do nó BRANN

1. Clique **Executar passo** e envie como *input* um JSON com `text: "quero conhecer os planos"` (ou deixe vir do nó anterior).
2. Saída esperada: um objeto com `out.type = "text"` ou `"buttons"`.
3. Verifique se o **Parser** recebe `out` direitinho e o **Switch/Segmentos** manda ao **Enviar mensagem**.

Se nessas condições o BRANN devolver algo que não seja JSON, me avise a saída bruta (copie o texto do painel) que eu ajusto a instrução do sistema para “forçar” melhor o formato. Próximo passo depois disso é ativar o **subfluxo de áudio** (para o `audio_key`) e rodar os quatro smoke tests de ponta a ponta.

esta certo?

Quase certo — faltam **3 ajustes** para ficar redondo e futuro-proof:

## 1) A fonte da mensagem do usuário

No BRANN, em **“Fonte para Prompt (Mensagem do Usuário)”**:

- troque **“Define below”** por **“Expressão”**
- no campo fx cole:  
	`={{$json.text}}`

> Hoje você está colocando instruções no campo do **usuário**; com isso o modelo não lê `{{$json.text}}` que veio do fluxo.

## 2) Sistema vs Usuário

- Deixe o campo **“Prompt (Mensagem do Usuário)”** **vazio** (ou um placeholder simples).
- Cole TODAS as instruções (regras/formato obrigatório) no campo **de sistema** (“Você é o assistente corporativo…”).  
	(O bloco que você já tem está ótimo — só mova para o **System**.)

## 3) (Recomendado) Travar o formato de saída

Ative **“Exigir formato de saída específico”** e escolha **JSON Schema**. Cole este schema para garantir `out.type`:

```markdown
{
  "type": "object",
  "properties": {
    "out": {
      "type": "object",
      "oneOf": [
        { "properties": { "type": { "const": "text" }, "text": { "type": "string" } }, "required": ["type","text"] },
        { "properties": { "type": { "const": "buttons" }, "text": { "type":"string" }, "buttons": { "type":"array", "items": { "type":"object", "properties":{"id":{"type":"string"},"text":{"type":"string"}}, "required":["id","text"] } } }, "required":["type","text","buttons"] },
        { "properties": { "type": { "const": "list" }, "text": { "type":"string" }, "sections": { "type":"array", "items": { "type":"object", "properties": { "title":{"type":"string"}, "rows": { "type":"array", "items": { "type":"object", "properties":{"id":{"type":"string"},"title":{"type":"string"},"description":{"type":"string"}}, "required":["id","title"] } } } } } }, "required":["type","text","sections"] },
        { "properties": { "type": { "const": "image" }, "imageUrl": { "type":"string" }, "caption": { "type":"string" } }, "required":["type","imageUrl"] },
        { "properties": { "type": { "const": "audio" }, "audioUrl": { "type":"string" } }, "required":["type","audioUrl"] },
        { "properties": { "type": { "const": "audio_key" }, "key": { "type":"string" } }, "required":["type","key"] }
      ]
    }
  },
  "required": ["out"]
}
```

## Sobre o aviso “Agente descontinuado”

Funciona, mas como está marcado como **descontinuado**, é melhor migrar quando puder:

- troque **Agente** para **“Agente de Ferramentas (Tools Agent)”**;
- mantenha a **mesma** fonte do prompt (`{{$json.text}}`) e **o mesmo System**;
- não registre ferramentas por enquanto (vai operar como chat “puro”);
- mantenha Temp `0.4` e Máx Tokens `1400`.

### Teste de fumaça

No BRANN → **Executar passo** passando `{"text":"quero conhecer os planos"}` na entrada do nó anterior.  
Saída esperada: `out.type = "buttons"` (ou `"text"`). Se vier fora do schema, o n8n acusa e você vê onde ajustamos.

Feitos esses 3, teu parser e os segmentos ficam sempre coerentes e o envio no Evolution não quebra.