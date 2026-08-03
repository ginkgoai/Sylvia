---
title: "GKO - Configurar áudios recebidos"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/69068179-d0b0-8325-845e-bcfa9ef9eec9"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sáb., 1 de nov. às 18:53

Para fazer o fluxo entender **áudios recebidos**, siga a arquitetura descrita no PDF:

---

### 🧩 1. Extração da mídia

Crie o nó **Function** chamado `EXTRAIR MÍDIA` com este código:

```markdown
const payload = items[0]?.json ?? {};
const body_ = payload.body ?? payload;
const data_ = body_.data ?? body_;
const key_ = data_.key ?? {};
const msg_ = data_.message ?? body_.message ?? {};

const text = msg_.conversation || msg_.extendedTextMessage?.text || msg_.imageMessage?.caption || msg_.videoMessage?.caption || "";

const chatId = key_.remoteJid || data_.chatId || body_.chatId || payload.chatId || "";
const phone = (chatId || "").replace(/@c.us|@s.whatsapp.net/g, "");
const messageId = key_.id || data_.messageId || body_.messageId || "";

let mediaType = "text";
if (msg_.audioMessage) mediaType = "audio";
else if (msg_.videoMessage) mediaType = "video";
else if (msg_.imageMessage) mediaType = "image";

const audioUrl = msg_.audioMessage?.url ?? null;
const videoUrl = msg_.videoMessage?.url ?? null;
const imageUrl = msg_.imageMessage?.url ?? null;

return [{ json: { ...payload, text, chatId, phone, messageId, mediaType, audioUrl, videoUrl, imageUrl } }];
```

---

### 🔀 2. Switch de roteamento

Use um **Switch Node** com 4 saídas:

| Index | Tipo de mídia | Expressão |
| --- | --- | --- |
| 0 | Áudio | `$json.mediaType === 'audio'` |
| 1 | Vídeo | `$json.mediaType === 'video'` |
| 2 | Imagem | `$json.mediaType === 'image'` |
| 3 | Texto | else |

---

### 🔊 3. Download de áudio

**Preferencial:** GET direto.

**GET (quando há URL):**

```markdown
URL: ={{$json.audioUrl}}
Response Format: File
Binary Property: audio
```

**POST (fallback Evolution):**

```markdown
URL: ={{$env.EVOLUTION_BASE_URL}}/message/downloadMedia/{{$env.EVOLUTION_INSTANCE}}
Method: POST
Headers:
  Authorization: Bearer {{$env.EVOLUTION_TOKEN}}
  Content-Type: application/json
Body:
  { "messageId": "={{$json.messageId}}" }
Response Format: File
Binary Property: audio
```

---

### 🧠 4. Transcrição com IA

Use **OpenAI Chat Model** (gpt-4o-mini) com input binário `audio`.

```markdown
System prompt:
"Transcreva o áudio recebido (PT-BR). Retorne somente o texto puro da fala."
Temperature: 0.3
Max tokens: 1000
Binary property: audio
```

---

### 🧩 5. Normalização

Após o nó de IA, adicione um **Set Node**:

```markdown
text = {{$json.text || $json.output_text || $json.transcript || $json.candidates?.[0]?.content?.parts?.[0]?.text}}
```

---

### 🗣️ 6. Integração com o Brann

Depois da transcrição, envie `text` para o fluxo do **Brann (modelo principal)** com:

- `phone`
- `text`
- `mediaType = 'audio'`

---

### ✅ 7. Teste rápido

Envie um áudio via WhatsApp.  
O log deve mostrar sequência:

```markdown
Webhook → EXTRAIR MÍDIA → Switch(audio) → Download → OpenAI TTS → Set(text) → BRANN
```

O Brann responderá com o texto transcrito ou ação correspondente.

---

Deseja que eu te gere o **subfluxo de transcrição de áudio** pronto para importação no n8n (`.json`)?

qua., 5 de nov. às 13:01

A falha está no **Code in JavaScript** porque o payload real do Evolution não bate com os campos que o script espera. Em áudio curto isso é comum: vem `messages[0]` ou `data.message`, sem `message.url`. O seu código acessa caminhos que ficam `undefined` e quebra.

Corrija assim:

1. Substitua o conteúdo do **Code in JavaScript** por um parser resiliente.
```markdown
// Resiliente p/ Evolution (Baileys) vários formatos
function safeParse(x){ if(typeof x === 'string'){ try{ return JSON.parse(x); }catch(e){ return {}; } } return x||{}; }

const root   = safeParse(items[0]?.json);
const body   = safeParse(root.body) || root;
const data   = safeParse(body.data) || body;

// Evolution pode enviar: data.message  OU  data.messages[0]  OU  body.message
const msg    = data.message || (Array.isArray(data.messages) ? data.messages[0] : null) || body.message || {};
const key    = msg.key || data.key || {};
const chatId = key.remoteJid || data.chatId || body.chatId || root.chatId || "";
const phone  = (chatId || "").replace(/@c\.us|@s\.whatsapp\.net/g, "");
const messageId = key.id || data.messageId || body.messageId || "";

// Detecta tipo
let mediaType = "text";
if (msg.audioMessage) mediaType = "audio";
else if (msg.videoMessage) mediaType = "video";
else if (msg.imageMessage) mediaType = "image";

// URLs diretas quando existirem (nem sempre vêm em PTT)
const audioUrl = msg.audioMessage?.url || data.audioUrl || null;
const videoUrl = msg.videoMessage?.url || data.videoUrl || null;
const imageUrl = msg.imageMessage?.url || data.imageUrl || null;

// Texto de apoio (legenda/caption)
const text =
  msg.conversation ||
  msg.extendedTextMessage?.text ||
  msg.imageMessage?.caption ||
  msg.videoMessage?.caption ||
  data.text || "";

// Se for mídia e NÃO houver url, precisamos do messageId p/ /downloadMedia
if ((mediaType === "audio" || mediaType === "video" || mediaType === "image") && !audioUrl && !videoUrl && !imageUrl && !messageId) {
  throw new Error("Mensagem de mídia sem URL e sem messageId. Verifique se o webhook do Evolution está enviando key.id.");
}

return [{
  json: {
    ...root,
    chatId, phone, messageId,
    mediaType, audioUrl, videoUrl, imageUrl,
    text,
    isPtt: Boolean(msg.audioMessage?.ptt)
  }
}];
```
2. No **HTTP Request de download** use fallback por `messageId` quando não houver URL:
- `POST {{$env.EVOLUTION_BASE_URL}}/message/downloadMedia/{{$env.EVOLUTION_INSTANCE}}`
- Headers: `Authorization: Bearer {{$env.EVOLUTION_TOKEN}}`
- Body JSON: `{ "messageId": "={{$json.messageId}}" }`
- Response: `File`, `Binary Property: audio`
3. Garanta as ENVs no n8n:
- `EVOLUTION_BASE_URL`
- `EVOLUTION_TOKEN`
- `EVOLUTION_INSTANCE`
4. Se ainda parar no código, adicione um **IF debug** logo depois do Webhook:
- Condição: `{{$json?.data?.message || ($json?.data?.messages && $json.data.messages[0])}}`
- Em “false”, mande um **Set** com `debug_payload = {{$json}}` para inspecionar o formato que está chegando.
5. Fluxo correto do áudio:  
	`Webhook → Code in JavaScript → (Switch=audio) → GET url OU POST /downloadMedia → OpenAI Transcribe (binary=audio) → Set(text) → Brann`

Quer que eu gere um **subworkflow.json** pronto só para “Áudio recebido → transcrever → devolver texto” para você importar?

qua., 5 de nov. às 14:56

Causa: o nó **OpenAI → Transcribe a Recording** não recebeu binário. Mensagem do n8n: “expects … binary file `file`, but none was found”. Na sua execução o item tem `mediaType: "text"` e `audioUrl: null`, então você roteou para o OpenAI sem antes baixar a mídia.

Faça assim.

## 1) Corrija o detector de tipo no “Code in JavaScript”

Inclua fallback para o campo `mensagem_tipo` que já chega no seu payload.

```markdown
function safe(x){ if(typeof x==='string'){ try{return JSON.parse(x)}catch(e){return {}} } return x||{} }

const root = safe(items[0]?.json);
const body = safe(root.body) || root;
const data = safe(body.data) || body;
const msg  = data.message || (Array.isArray(data.messages)? data.messages[0] : null) || body.message || {};
const key  = msg.key || data.key || {};

const chatId = key.remoteJid || data.chatId || body.chatId || root.chatId || "";
const phone  = (chatId||"").replace(/@c\.us|@s\.whatsapp\.net/g,"");
const messageId = key.id || data.messageId || body.messageId || "";

let mediaType = "text";
if (msg.audioMessage || data.mensagem_tipo === "audioMessage") mediaType = "audio";
else if (msg.videoMessage || data.mensagem_tipo === "videoMessage") mediaType = "video";
else if (msg.imageMessage || data.mensagem_tipo === "imageMessage") mediaType = "image";

const audioUrl = msg.audioMessage?.url || data.audioUrl || null;

const text =
  msg.conversation ||
  msg.extendedTextMessage?.text ||
  msg.imageMessage?.caption ||
  msg.videoMessage?.caption ||
  data.text || "";

return [{
  json: { ...root, chatId, phone, messageId, mediaType, audioUrl, text }
}];
```

## 2) Garanta o Switch correto

No “Route Types” use esta expressão única:

```markdown
{{$json.mediaType === 'audio' ? 0 : $json.mediaType === 'video' ? 1 : $json.mediaType === 'image' ? 2 : 3}}
```

Saídas: 0=Áudio, 1=Vídeo, 2=Imagem, 3=Texto.  
Conecte o **OpenAI Audio** somente à saída 0.

## 3) Baixe a mídia antes do OpenAI

Insira um **HTTP Request** entre o Switch(áudio) e o OpenAI:

- Se tiver URL:
	- Method: GET
		- URL: `={{$json.audioUrl}}`
		- Response: **File**
		- Binary Property: **file**
- Fallback Evolution quando não houver URL:
	- Method: POST
		- URL: `={{$env.EVOLUTION_BASE_URL}}/message/downloadMedia/{{$env.EVOLUTION_INSTANCE}}`
		- Headers:
		- `Authorization: ={{'Bearer ' + $env.EVOLUTION_TOKEN}}`
				- `Content-Type: application/json`
		- Body (JSON): `{"messageId":"={{$json.messageId}}"}`
		- Response: **File**
		- Binary Property: **file**

Opcional: coloque um **IF** antes para decidir GET vs POST:

```markdown
Condition: {{$json.audioUrl && $json.audioUrl.startsWith('http')}}
TRUE → GET, FALSE → POST
```

## 4) Configure o nó OpenAI

- Resource: **Audio**
- Operation: **Transcribe a Recording**
- **Input Data Field Name**: `file` ← deve bater com o Binary Property do passo anterior
- Language: `pt`
- Temperature: `0.2`

## 5) Normalize a saída

Após o OpenAI, um **Set**:

```markdown
text = {{$json.text || $json.output_text || $json.transcript || $json.candidates?.[0]?.content?.parts?.[0]?.text}}
```

## 6) Verificação rápida

Execute e confirme que no painel esquerdo do OpenAI aparece:

- `binary → file` presente
- `mediaType: "audio"`
- `messageId` preenchido

Se ainda falhar, envie o print do **HTTP Request (download) → OUTPUT**. O problema estará aí.