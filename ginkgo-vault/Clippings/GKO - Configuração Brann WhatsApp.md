---
title: "GKO - Configuração Brann WhatsApp"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/699d5fce-8e44-832d-98f5-55dcaef2a579"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
ter., 24 de fev. às 5:22

Sim. Vou te mandar uma **versão correta (arquitetura + blueprint de nós + configs copy/cola)** do fluxo do Brann com:

1. **roteamento certo por tipo de mensagem**
2. **intenção (intent router) antes do LLM**
3. **transcrição de documentos via bots Telegram (Nyra/Alfred/Manus)**
4. **persistência de dados na Supabase via “bot Manus”** (pipeline padrão)

> Observação direta: eu não consigo “adivinhar” 100% os campos do seu payload do Evolution sem ver o JSON completo do webhook, então abaixo eu te entrego um fluxo **robusto** que funciona com qualquer shape, porque ele **detecta tipo por presença de campos** e normaliza.

---

## 1) FLUXO “BRANN v2” (CORRETO) — VISÃO GERAL

**Entrada (Evolution → n8n)**  
→ **Normalização** (descobre tipo + extrai texto/base64/link)  
→ **Dedup / Ignore fromMe**  
→ **Handoff (Supabase state)**  
→ **Media pipeline**

- Texto: segue
- Áudio: transcreve
- Imagem: descreve
- Documento: manda pro Telegram “Transcriber Bot” (Manus) e aguarda callback  
	→ **Intent Classifier** (OpenAI pequeno)  
	→ **Router por intenção**  
	→ **RAG (Pinecone/Supabase Vector)**  
	→ **LLM Brann Persona**  
	→ **Ações** (criar/atualizar lead, tags, status, agendamento)  
	→ **Responder no WhatsApp (Evolution)**  
	→ **Persistir conversa/telemetria (Supabase)**

---

## 2) SUPABASE (BASE) — TABELAS MÍNIMAS

Crie estas tabelas (mínimo pra Leaf SaaS):

### leads

- `id` uuid pk
- `client_id` text
- `phone` text unique (por client\_id)
- `name` text null
- `stage` text default 'new'
- `tags` text\[\] default '{}'
- `last_intent` text null
- `last_message_at` timestamptz
- `created_at` timestamptz default now()

### conversations

- `id` uuid pk
- `client_id` text
- `phone` text
- `channel` text default 'whatsapp'
- `last_summary` text null
- `updated_at` timestamptz default now()

### messages

- `id` uuid pk
- `client_id` text
- `phone` text
- `direction` text ('in'/'out')
- `message_type` text
- `content` text
- `raw` jsonb
- `created_at` timestamptz default now()

### handoff\_state

- `client_id` text
- `phone` text
- `mode` text ('BOT'/'HUMAN')
- `until` timestamptz null
- `updated_at` timestamptz default now()
- pk (`client_id`,`phone`)

### jobs (para transcrição via Telegram)

- `id` uuid pk
- `client_id` text
- `phone` text
- `job_type` text ('doc\_transcribe')
- `status` text ('queued','processing','done','error')
- `input_meta` jsonb
- `result_text` text null
- `created_at` timestamptz default now()
- `updated_at` timestamptz default now()

---

## 3) N8N — NÓS (SEQUÊNCIA) COM CONFIG

Abaixo está o “blueprint” do fluxo em ordem. Você replica e substitui credenciais.

## A) Entrada e Normalização

### 1) Webhook (Evolution)

- path: `brann-webhook`
- method: POST

### 2) Code: NormalizePayload

Objetivo: criar um payload padrão:

- `client_id`
- `phone`
- `fromMe`
- `message_type` (conversation / audio / image / video / document)
- `text` (quando existir)
- `base64` (quando existir)
- `doc_meta` (quando existir)

**Código (cole no Code node):**

```markdown
const j = $json;

// Ajuste conforme seu multi-tenant: pode vir de instance, header, token etc.
const client_id = j.client_id || j.CLIENTE || j.instance || 'GINKGO';

// phone normalizado
const phone = j.NUMERO_LEAD || j.remoteJid || j.data?.key?.remoteJid || j.key?.remoteJid || '';

// fromMe
const fromMe = j.fromMe ?? j.data?.key?.fromMe ?? false;

// detectar tipo por presença de campos (mais robusto que confiar num campo “MENSAGEM_TIPO”)
const hasDoc = !!(j.documentMessage || j.message?.documentMessage || j.data?.message?.documentMessage || j.document);
const hasAudio = !!(j.audioMessage || j.message?.audioMessage || j.data?.message?.audioMessage || j.audio);
const hasImage = !!(j.imageMessage || j.message?.imageMessage || j.data?.message?.imageMessage || j.image);
const hasVideo = !!(j.videoMessage || j.message?.videoMessage || j.data?.message?.videoMessage || j.video);

let message_type = 'conversation';
if (hasDoc) message_type = 'document';
else if (hasAudio) message_type = 'audio';
else if (hasImage) message_type = 'image';
else if (hasVideo) message_type = 'video';

const text =
  j.text ||
  j.message?.conversation ||
  j.data?.message?.conversation ||
  j.MENSAGEM ||
  j.body ||
  '';

const base64 =
  j.base64 ||
  j.Base64 ||
  j.data?.message?.base64 ||
  null;

// meta do doc
const doc_meta = j.documentMessage || j.message?.documentMessage || j.data?.message?.documentMessage || null;

return [{
  json: {
    client_id,
    phone,
    fromMe,
    message_type,
    text,
    base64,
    doc_meta,
    raw: j
  }
}];
```

### 3) IF: IgnoreFromMe

- condição: `{{$json.fromMe}} is true`
- true → termina
- false → segue

### 4) Supabase: GetHandoffState

- select em `handoff_state` por `client_id` + `phone`

### 5) IF: HandoffHuman

- se `mode == HUMAN` e (until nulo ou > now) → termina (não responde)
- senão segue

### 6) Supabase: UpsertLead (sempre)

- upsert `leads` com `last_message_at=now()`

### 7) Supabase: InsertInboundMessage

- inserir em `messages` (direction='in', message\_type, content=text, raw)

---

## B) Media Pipeline (Texto/Áudio/Imagem/Documento)

### 8) Switch: RouteByMessageType

- value: `{{$json.message_type}}`
- cases: conversation / audio / image / video / document

#### Branch 1: conversation

→ `Set: FinalText = {{$json.text}}`

#### Branch 2: audio

1. `Convert Base64 to File` (se base64 existir)
2. `OpenAI Transcribe` (pt)
3. `Set: FinalText = {{$json.text}}` (output da transcrição)

#### Branch 3: image

1. `OpenAI Vision Analyze` (base64 ou URL)
2. `Set: FinalText = {{$json.content}}` (descrição da imagem)

#### Branch 4: document (aqui entra Telegram + Manus)

Esse é o upgrade que você pediu.

**Ideia:** documento entra → vira um JOB → você envia pro “Telegram Transcriber Bot (Manus)” → ele processa → chama **um webhook de callback** no n8n com o `job_id` → você retoma e responde.

**Fluxo document:**

1. `Supabase Insert Job` em `jobs`:
	- `job_type='doc_transcribe'`
		- `status='queued'`
		- `input_meta` com nome/size/mimetype (do doc\_meta)
2. `HTTP Request: SendToTelegramManus`
	- manda `job_id`, `client_id`, `phone`
		- e o arquivo (ou link) do documento
3. `Respond to WhatsApp` imediatamente:
	- “Recebido. Estou a extrair o conteúdo do documento. Já te devolvo um resumo e próximos passos.”
4. **STOP** (não entra no LLM agora)

---

## 4) CALLBACK DO TELEGRAM (MANUS) — RETOMA O FLUXO

Crie um **segundo workflow** no n8n:

### Workflow: manus-doc-callback

1. Webhook: `/manus-callback`
2. Supabase: `Update Job` (status='done', result\_text = texto extraído)
3. Supabase: `Get Lead + Conversation`
4. Chamar o **mesmo bloco** de Intent → RAG → Brann → Evolution
	- passando `FinalText = result_text`
		- `message_type = 'document_transcribed'`

> Isso separa “processamento pesado” do WhatsApp realtime. Leaf fica rápido e estável.

---

## 5) INTENT CLASSIFIER (ANTES DO BRANN)

Depois que você tiver `FinalText`, faz:

### Node: OpenAI (modelo pequeno) IntentClassifier

**System:**

- “Classifique intenção. Responda apenas JSON.”

**User:**

```markdown
Mensagem:
{{ $json.FinalText }}

Retorne JSON:
{
 "intent": "SUPORTE|VENDAS|DEMO|ORCAMENTO|INTEGRACOES|ONBOARDING|HUMANO|OUTROS",
 "confidence": 0-1,
 "entities": {"nome": "...", "empresa": "...", "produto": "..."}
}
```

### Node: Switch Intent

- value: `{{$json.intent}}`

Rotas mínimas:

- VENDAS/ORCAMENTO → script comercial
- SUPORTE/INTEGRACOES → FAQ/guia técnico
- DEMO → enviar links e CTA
- HUMANO → set `handoff_state=HUMAN` + confirmar
- OUTROS → Brann normal

---

## 6) “BOT MANUS” SALVANDO NA SUPABASE (PADRÃO)

Você pediu “interação com os bots Telegram para eles salvarem dados na supabase bot manus”.

Padrão certo:

- Telegram bot **NÃO** escreve direto no banco em produção, ele chama **um endpoint interno (n8n webhook)**.
- O n8n valida `client_id` + `signature` + `job_id`.
- O n8n executa Supabase com service role e registra logs.

Então você cria um endpoint:

### Webhook: /manus-write

Payload esperado:

```markdown
{
  "signature": "HMAC",
  "client_id": "GINKGO",
  "phone": "55...",
  "action": "upsert_lead|add_tag|set_stage|insert_doc_summary",
  "data": {...}
}
```

Ações que valem ouro:

- `insert_doc_summary` → grava o resumo do doc na `conversations.last_summary`
- `add_tag` → adiciona tag no lead
- `set_stage` → muda stage (ex: qualified)

---

## 7) BRANN (LLM) — PERSONA + FORMATO FIXO

No seu node principal do OpenAI (Brann):

**System (fixo):**

- Persona Brann (PT-PT), estrutura 1) confirmação 2) 2–3 bullets 3) CTA único
- “Nunca terminar conversa”
- “Se intent = HUMANO, não responda (ou responda confirmando handoff)”
- “Se doc\_transcribed, gere: resumo + pontos acionáveis + perguntas faltantes”

**Inputs:**

- `FinalText`
- contexto Redis Memory
- RAG tool (Pinecone)
- dados do lead (stage/tags)

---

## 8) SAÍDA + LOGS

Após gerar resposta:

1. Supabase: `InsertOutboundMessage`
2. Evolution: send message
3. Supabase: atualizar `leads.last_intent` + tags se aplicável

---

## 9) O QUE VOCÊ PRECISA CRIAR AGORA (SEM DISCUSSÃO)

1. **NormalizePayload (Code)** (corrige roteamento de vez)
2. **RouteByMessageType** baseado em `message_type`
3. **Document pipeline com Job + Telegram + Callback**
4. **IntentClassifier + Switch**
5. **Supabase tables** (leads/messages/jobs/handoff)

---

## 10) ENTREGA “PRONTA PRA COPIAR” (O QUE EU PRECISO DE VOCÊ)

Pra eu te devolver o **JSON importável do n8n 100% fiel ao seu ambiente** (com paths exatos do Evolution), manda **1 print ou cola aqui** do:

- **INPUT → JSON** do webhook (um evento de texto e um de documento).

Sem isso, eu entrego “universal”, mas com isso eu te entrego “cirúrgico” (sem erro de path).

---

Se você quer que eu avance sem esperar, eu avanço no modo universal e te digo exatamente onde plugar os seus nodes existentes (Transcribe/Vision/Pinecone/Redis/Evolution).

Brann (18).json

Arquivo

olha o código atualmente e corrija melhore. importavel n8n

Aqui está a versão **corrigida e melhorada (importável no n8n)** do seu workflow **Brann**:  
Brann\_CORRIGIDO\_v2.json

Brann (18)

## O que foi corrigido (mudanças que destravam o roteamento e o fluxo)

1. **Bug raiz do roteamento**
- Seu `MENSAGEM_TIPO` estava recebendo o **texto** (`conversation: "Oi"`) em vez do **tipo**.
- Agora `MENSAGEM_TIPO = body.data.messageType` (ex.: `conversation`, `audioMessage`, `imageMessage`, etc).
2. **Referências quebradas**
- O workflow inteiro referenciava um node que **não existe**: `Tratamento de Dados`.
- Eu substituí **todas** as referências por `Dados` (node real). Isso sozinho já evita metade dos “não funciona”.
3. **IF `fromMe` errado**
- Estava comparando `fromMe` como **string** (`"=true"`).
- Corrigido para **boolean** (`isTrue`). Assim não responde a mensagens enviadas pelo próprio bot.
4. **Campos essenciais adicionados no `Dados`**
- `message_id` (era usado depois e não existia)
- `MENSAGEM` (texto normalizado)
- `Base64` (padronizado para bater com os nós Convert/Audio)
- `mediaKey` (mantido como referência)
5. **Instância default errada**
- Um node estava defaultando `PRV_Alimentos`.
- Corrigido para `BRANN`.

---

## Importante (sobre DOCUMENTOS)

Seu fluxo original tenta baixar documento usando `url = server_url`, o que **não é o link do arquivo**.  
Eu **não inventei endpoint** de download porque isso depende do seu Evolution (rota e params exatos). O fluxo agora está “arrumado”, mas **para transcrição de documento funcionar**, você precisa de **um passo real de download de mídia** (via Evolution API/endpoint correto) antes de enviar pro Telegram/Extract.

Se você me mandar **1 exemplo real** de evento `documentMessage` (o JSON do webhook), eu ajusto o branch de documento e te devolvo uma **v3** com:

- download correto do arquivo (binário)
- envio pro Telegram “Manus”
- callback/retorno e salvamento na Supabase

Sem isso, qualquer “download” vira chute.

---

## Como importar

n8n → **Workflows** → **Import from File** → selecione `Brann_CORRIGIDO_v2.json`.

Se quiser, eu também te devolvo uma versão “Leaf-ready” já com:

- Intent Router
- Supabase upsert lead/messages/jobs
- Telegram transcriber (Manus) com callback

Mas pra isso eu preciso do **payload real de documentMessage**.

qua., 25 de fev. às 22:13

![4e404b61-b438-4127-8d6a-bd40132b582d.png](https://chatgpt.com/backend-api/estuary/content?id=file_000000001c14720ea1bdd884f2aa8ccc&ts=495692&p=fs&cid=1&sig=1abe72eb1a90f70fa56448eb1ba1d5a787e9013bbd890a73ca533dac4f591250&v=0) ![5dbc3571-40e8-4bab-8000-9c7b88f32392.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000a5bc720eba2dec6071688b5d&ts=495692&p=fs&cid=1&sig=93bd7e6c4e6985495acfae5718d7c6c4ed2b5239233fb22823fbb63fa0a030fc&v=0)

queria usar o bot manus no telegram para fazer a transcrição de arquivos docs para o agent n8n, como fazemos isso?

Perfeito. Vamos fazer isso da forma **profissional e escalável**, não gambiarra.

Hoje seu erro no Telegram é:

> **Bad Request: chat not found**

Você colocou `Chat ID = alfred`.

Telegram **não aceita username como chat\_id**.  
Ele aceita:

- ID numérico do usuário (ex: `123456789`)
- ID numérico do grupo (ex: `-100XXXXXXXX`)
- ou `@username` se for canal público

---

## ARQUITETURA CORRETA — MANUS TELEGRAM → n8n

Você quer:

WhatsApp envia documento  
→ n8n recebe  
→ envia para Manus no Telegram  
→ Manus transcreve  
→ Manus devolve texto  
→ n8n continua fluxo

Isso exige **CALLBACK**, não polling manual.

---

## MODELO PROFISSIONAL (2 WORKFLOWS)

## WORKFLOW 1 — BRANN (envia documento para Manus)

### 1️⃣ Quando for documentMessage:

- Download real do arquivo (binário)
- Criar `job_id`
- Salvar job na Supabase
- Enviar arquivo pro Telegram Manus
- Responder WhatsApp: “Estou processando”

---

## WORKFLOW 2 — TELEGRAM CALLBACK

Telegram bot recebe resposta do Manus  
→ webhook no n8n  
→ atualiza job  
→ continua fluxo Brann

---

## PASSO A PASSO REAL

---

## ETAPA 1 — PEGAR CHAT ID CORRETO

No Telegram:

1. Fale com seu bot Manus
2. Envie qualquer mensagem
3. No n8n crie workflow simples:

Webhook Telegram → Log JSON

Você verá algo como:

```markdown
{
  "message": {
    "chat": {
      "id": 123456789,
      "username": "gabriel..."
    }
  }
}
```

Use:

```markdown
123456789
```

Não use “alfred”.

---

## ETAPA 2 — ENVIAR DOCUMENTO CORRETAMENTE

Node Telegram:

- Resource: Message
- Operation: Send Document
- Chat ID: 123456789
- Binary: ON
- Input Binary Field: data

⚠ IMPORTANTE  
O node anterior precisa ter o binário com o nome `data`.

Se o seu Download Document não estiver retornando `binary.data`, não funciona.

---

## ETAPA 3 — MANUS TRANSCRIBIR

Você tem duas opções:

---

## OPÇÃO A — Manus responde no mesmo chat

Ele manda texto transcrito.

Você cria workflow:

Telegram Trigger → IF message.document → processa  
Telegram Trigger → IF message.text → é resposta do Manus

---

## OPÇÃO B — Manus chama webhook (melhor)

Manus após transcrever faz:

POST → n8n webhook:

```markdown
{
  "job_id": "...",
  "text": "texto transcrito",
  "client_id": "...",
  "phone": "..."
}
```

Esse é o modelo enterprise.

---

## ETAPA 4 — N8N CONTINUA FLUXO

No webhook callback:

1. Atualiza Supabase job
2. Recupera dados do lead
3. Chama IntentClassifier
4. Chama Brann
5. Envia WhatsApp

---

## COMO FAZER TRANSCRIÇÃO REAL DE DOC

Telegram não transcreve DOC sozinho.

Manus precisa:

- Extrair texto do PDF/DOCX
- Se imagem → OCR
- Se PDF escaneado → OCR
- Se DOCX → converter

Se Manus não tiver OCR:

Use OpenAI + PDF Extract:

Pipeline dentro do Manus:

1. Recebe arquivo
2. Extrai texto (pdf-parse / docx extractor)
3. Se imagem → Vision
4. Retorna texto puro

---

## ESTRUTURA IDEAL

```markdown
WhatsApp → n8n → Telegram Manus → OCR/Extract → n8n callback → Brann → WhatsApp
```

---

## SOBRE SEU ERRO ATUAL

O erro é só:

```markdown
Chat ID inválido
```

Use ID numérico.

---

## QUER QUE EU TE ENTREGUE?

Posso gerar:

- Workflow 1 (Brann document job)
- Workflow 2 (Telegram Manus callback)
- SQL Supabase jobs
- JSON importável pronto

Mas preciso saber:

1. Manus é seu bot próprio?
2. Ele já tem webhook?
3. Ele consegue fazer OCR?

Me confirma isso que eu te entrego arquitetura fechada pronta pra produção.