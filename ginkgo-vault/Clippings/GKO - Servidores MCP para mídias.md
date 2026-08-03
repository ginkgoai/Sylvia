---
title: "GKO - Servidores MCP para mídias"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/68f8040a-c660-832b-b7d0-37b3d914ca63"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
ter., 21 de out. às 19:07

Sim — e o seu próprio documento *Visão Geral do Fluxo* já indica o caminho: os servidores MCP (Model Context Protocol) **capazes de entender mídias** são aqueles que suportam **entrada binária** (binary input) e têm modelos multimodais integrados.

Para o seu caso no ecossistema *Ginkgo Leaf / BRANN*, os principais candidatos MCP são:

1. **OpenAI GPT-4o mini / GPT-4o (via MCP Server)**  
	Esses modelos entendem **áudio, vídeo, imagem e texto** diretamente.
	- *Áudio*: transcrição PT-BR natural (Speech-to-Text).
		- *Vídeo*: resumo + transcrição da fala.
		- *Imagem*: OCR e descrição contextual.
		- No n8n, você envia o binário (`binaryProperty`) diretamente; o MCP trata e devolve o texto.
2. **Whisper MCP (da OpenAI ou Microsoft)**  
	Especializado só em áudio/vídeo, mas muito mais leve. Ideal para pipelines dedicados de **transcrição pura**.
3. **Vision MCP (Google Gemini / Anthropic Claude 3V)**  
	Interpretam imagens, screenshots, diagramas e PDFs com OCR, útil para **documentos e imagens complexas**.  
	Pode ser montado no seu stack via proxy local (Docker ou EasyPanel) com autenticação por token.
4. **Firecrawl MCP (nativo da Ginkgo)**  
	Consegue “ler” PDFs e páginas da web, extraindo texto e metadados — ótimo para *documentos longos*, não para áudio ou vídeo.

Em resumo prático:

- **Áudio e vídeo** → GPT-4o mini (modo binário) ou Whisper MCP.
- **Imagem e PDF** → GPT-4o mini (modo visão) ou Vision MCP.
- **Texto puro** → qualquer modelo LLM via MCP padrão.

Posso te mandar o *manifest MCP JSON* (para usar direto no VS Code ou no n8n MCP Server) de cada um desses módulos — quer que eu monte agora os quatro (áudio, vídeo, imagem e documento)?

Então conseguimos fazer o fluxo no n8n dessa forma, chega a mensagem webhook etc e a gente manda pro mcp certo entender e trazer a resposta para enviar pro agente gerar uma resposta e responder?

Sim — essa é exatamente a arquitetura certa. A linha do tempo é:

1. Webhook recebe a mensagem (texto, áudio, vídeo, imagem).
2. Função “EXTRAIR\_MÍDIA” identifica o tipo e extrai URLs/IDs.
3. Baixa o binário (GET direto da URL ou POST /downloadMedia na Evolution).
4. Envia o binário para **um servidor MCP multimodal** (ou para MCPs especializados).
5. MCP devolve **texto normalizado** (transcrição/descrição/resumo).
6. Passa esse texto para o **agente BRANN** (LLM com memória/ferramentas).
7. BRANN decide o formato (texto/botões/lista/áudio\_key) e você **envia a resposta** via Evolution API.

Abaixo vai o “como fazer”, versão copy/cola, já organizado para o n8n e com duas topologias de MCP: “tudo-em-um” (multimodal) ou “especializados”.

---

## Fluxo n8n (passo a passo)

## 0) Variáveis de ambiente (n8n › Settings › Environment variables)

```markdown
EVOLUTION_BASE_URL=https://SEU-HOST:PORTA
EVOLUTION_TOKEN=SEU_TOKEN
EVOLUTION_INSTANCE=BRANN

MCP_OPENAI_BASE_URL=https://api.openai.com/v1
MCP_OPENAI_API_KEY=sk-...
MCP_SERVER_URL=http://mcp-openai:3333

# (opcional) Whisper
MCP_WHISPER_URL=http://mcp-whisper:4000/transcribe

# (opcional) Vision (Gemini/Claude)
MCP_VISION_URL=http://mcp-vision:5000/vision
MCP_VISION_API_KEY=...
```

## 1) Webhook (Trigger)

- Method: POST
- Path: `/brann/webhook`

## 2) Function “EXTRAIR\_MIDIA” (cole exatamente)

```markdown
const payload = items[0]?.json ?? {};
const body_ = payload.body ?? payload;
const data_ = body_.data ?? body_;
const key_ = data_.key ?? {};
const msg_ = data_.message ?? body_.message ?? {};

const text = msg_.conversation || msg_.extendedTextMessage?.text || 
             msg_.imageMessage?.caption || msg_.videoMessage?.caption || "";

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

## 3) Switch “Roteia por mediaType”

- Number of outputs: **4**
- Expression (zero-based):
```markdown
{{$json.mediaType === 'audio' ? 0 : $json.mediaType === 'video' ? 1 : $json.mediaType === 'image' ? 2 : 3}}
```
- Saídas: 0=Áudio, 1=Vídeo, 2=Imagem, 3=Texto

## 4) Download da mídia (para cada ramo áudio/vídeo/imagem)

### 4.1 IF “tem URL direta?”

- Condição: `{{$json.audioUrl && $json.audioUrl.startsWith('http')}}`  
	(troque `audioUrl` por `videoUrl` / `imageUrl` em cada ramo)

### 4.2 HTTP Request GET (se TRUE)

- Authentication: None
- URL: `={{$json.audioUrl}}` (ou `videoUrl` / `imageUrl`)
- Response: **File**
- Binary Property: `audio` / `video` / `image`

### 4.3 HTTP Request POST Evolution (se FALSE)

- URL: `={{$env.EVOLUTION_BASE_URL}}/message/downloadMedia/{{$env.EVOLUTION_INSTANCE}}`
- Method: POST
- Headers:
```markdown
Authorization: ={{'Bearer ' + $env.EVOLUTION_TOKEN}}
Content-Type: application/json
```
- Body (JSON):
```markdown
{ "messageId": "={{$json.messageId}}" }
```
- Response: **File**
- Binary Property: `audio` / `video` / `image`

---

## Chamada ao MCP (duas abordagens)

## Modo A — Único MCP Multimodal (recomendado para começar)

Você expõe um **MCP “openai-multimodal”** aceitando binário e retornando texto. No n8n, use **HTTP Request**:

### Áudio → MCP

- Method: POST
- URL: `={{$env.MCP_SERVER_URL}}/multimodal/transcribe`
- Headers:
```markdown
Authorization: ={{'Bearer ' + $env.MCP_OPENAI_API_KEY}}
Content-Type: multipart/form-data
```
- Body (form-data):
	- `file` → **Binary** = `audio`
		- `task` → `transcribe`
		- `lang` → `pt-BR`
- Response: JSON com `{ "text": "..." }`

### Vídeo → MCP

- POST `.../multimodal/transcribe`
- `file` (binary) = `video`
- `task` = `transcribe+summarize`

### Imagem → MCP

- POST `.../multimodal/vision`
- `file` (binary) = `image`
- `prompt`:
```markdown
Descreva a imagem em 1-2 frases úteis para atendimento comercial; se houver texto legível (OCR), inclua. Responda:
{"text":"..."} em PT-BR.
```

> Vantagem: um ponto só. Menos peças para cuidar.  
> Desvantagem: tudo na mesma conta/modelo.

## Modo B — MCPs Especializados (mais fino/custo-efetivo)

- **Áudio/Vídeo (voz)** → Whisper MCP (`{{$env.MCP_WHISPER_URL}}`)
- **Imagem/PDF** → Vision MCP (`{{$env.MCP_VISION_URL}}`)
- **Texto** → LLM padrão (OpenAI/Anthropic) via MCP comum

No n8n muda só a **URL** e os **campos**:

- Whisper:
	- POST `{{$env.MCP_WHISPER_URL}}`
		- file=binary (`audio` ou `video`)
		- retorna `{ "text": "..." }`
- Vision:
	- POST `{{$env.MCP_VISION_URL}}`
		- file=binary (`image`)
		- `mode=ocr+caption`
		- retorna `{ "text": "..." }`

---

## 5) Normalização para text (Set)

Crie um **Set** após cada chamada MCP para garantir `text`:

```markdown
text = {{$json.text || $json.output_text || $json.transcript || $json.caption || $json.description}}
```

## 6) BRANN (Chat Model) — geração da resposta

Use “OpenAI Chat Model” (ou “LLM via MCP”) com **System** corporativo do BRANN e **JSON mode ON**.  
**Input**: `={{$json.text}}` + memória (Session ID = `{{$json.phone || $json.chatId}}`).

Formato **OBRIGATÓRIO** de saída (um único):

```markdown
{ "out": { "type": "text", "text": "..." } }
```

ou buttons/list/image/audio/audio\_key (como já definimos).

## 7) Switch por out.type + envio via Evolution

- **Text** → POST `/message/sendText`
- **Buttons** → `/message/sendButtons`
- **List** → `/message/sendList`
- **Image/Audio(URL)** → `/message/sendMedia` (com `ptt:true` para PTT)
- **audio\_key** → “Execute Workflow” do subfluxo ÁUDIO (Puxar PTT pronto)

---

## Manifests MCP (copy/cola)

## A) openai-multimodal.server.json

```markdown
{
  "name": "openai-multimodal",
  "transport": { "type": "stdio" },
  "capabilities": ["vision", "audio", "video", "text"],
  "settings": {
    "baseUrl": "${MCP_OPENAI_BASE_URL}",
    "apiKey": "${MCP_OPENAI_API_KEY}",
    "defaultModel": "gpt-4o-mini",
    "maxOutputTokens": 1200
  },
  "endpoints": {
    "POST /multimodal/transcribe": { "binary": true, "returns": { "text": "string" } },
    "POST /multimodal/vision": { "binary": true, "returns": { "text": "string" } }
  }
}
```

## B) whisper.server.json

```markdown
{
  "name": "whisper",
  "transport": { "type": "stdio" },
  "capabilities": ["audio","video"],
  "settings": { "url": "${MCP_WHISPER_URL}" },
  "endpoints": {
    "POST /transcribe": { "binary": true, "returns": { "text": "string" } }
  }
}
```

## C) vision.server.json

```markdown
{
  "name": "vision",
  "transport": { "type": "stdio" },
  "capabilities": ["vision","pdf"],
  "settings": {
    "url": "${MCP_VISION_URL}",
    "apiKey": "${MCP_VISION_API_KEY}"
  },
  "endpoints": {
    "POST /vision": { "binary": true, "returns": { "text": "string" } }
  }
}
```

> Como subir: coloque os JSONs na pasta de servidores MCP, suba via Docker/EasyPanel ou `node` / `bun`, exponha `MCP_SERVER_URL` para o n8n.

---

## Boas práticas rápidas

- **Timeouts**: 30s nos nós de IA; para vídeo longo, considere fila/assíncrono com “wait + polling”.
- **Fallback**: se **download** falhar, responda: “não consegui baixar a mídia, posso seguir por texto?”
- **Logs**: adicione `traceId`, `mediaType`, `latency_ms` (Set) antes do BRANN.
- **Custo**: áudio curto → Whisper; imagem/PDF simples → 4o-mini visão; vídeos longos → Whisper + sumarizador texto.
- **Segurança**: nunca logue binários crus; mascarar tokens; limitar tamanho de arquivo.

---

## Checklist de teste (rápido)

- Texto “oi” → BRANN responde JSON→ sendText.
- Imagem com legenda → Vision MCP → `text` → BRANN → sendText.
- Áudio 10–20s → MCP transcreve → BRANN resume e responde.
- Vídeo curto → MCP transcreve+resume → BRANN decide **buttons** → Evolution envia.

Se quiser, eu já te mando o **workflow JSON do n8n** com: Webhook → EXTRAIR\_MIDIA → Switch → (GET/POST download) → MCP (multimodal) → Set `text` → BRANN → Switch `out.type` → Evolution. Quer com o **Modo A (multimodal único)** para começar e depois clonamos para o Modo B?