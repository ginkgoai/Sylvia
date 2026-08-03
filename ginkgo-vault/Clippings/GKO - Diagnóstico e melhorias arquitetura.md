---
title: "GKO - Diagnóstico e melhorias arquitetura"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/68f8121b-dd40-832c-a1e6-3ff49d9af1c8"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
ter., 21 de out. às 20:07

![e0a2d141-10e1-47ef-a35b-a3163ca71c3a.png](https://chatgpt.com/backend-api/estuary/content?id=file_000000002b7461f5a868cc2f5ef83859&ts=495692&p=fs&cid=1&sig=dee5e980d1f0e2a7747987ad6c6e1a3bf0339cd98c52561d94db857de271b076&v=0)

Perfeito, Gabriel — o teu diagrama já está no caminho certo: um “AI Agent” orquestrando MCPs (Drive, Gmail, LinkedIn, Twitter, Utilities) e um canal de I/O (Webhook → Code → Discord/WA). Falta só o “cérebro de mídias” para fechar o ciclo em WhatsApp: áudio, vídeo, imagem e documento viram **texto limpo** antes de cair no BRANN. Abaixo te entrego:

- Diagnóstico rápido do que tens
- Melhorias de arquitetura (com MCP de Mídias)
- Passo-a-passo “copy/cola” para n8n (bloco de transcrição)
- Schemas de Tools p/ teu Chat Model (function-calling)
- Docker (opcional) p/ subir os serviços de mídia
- Checklist de validação

---

## 1) Diagnóstico (onde estás forte e onde falta cola)

- **Forte**: Orquestração por um agente central com MCPs conectados (Drive, Gmail, etc.), ótimo para “ação” (buscar, enviar, listar, responder).
- **Gap**: Entrada multimídia. Falta um **MCP de Mídias** (ou microserviços REST) que entregue uma **única saída canônica** `{"text":"..."}` para qualquer tipo (áudio/vídeo/imagem/PDF/DOCX).
- **Risco atual**: cada tipo de mídia virar um formato diferente de resposta e “quebrar” teu BRANN. Vamos normalizar.

---

## 2) Arquitetura proposta (simples e escalável)

Cria um **Media MCP** (ou 4 microserviços REST atrás de um MCP) com **quatro ferramentas**:

1. `media.transcribe_audio`  
	Entrada: `{ "url" | "base64", "mime", "lang": "pt" }`  
	Saída: `{ "text": "..." }`  
	Engine: *faster-whisper/whisperX* (+ `ffmpeg` p/ normalizar).
2. `media.transcribe_video`  
	Entrada idem; por baixo: `ffmpeg` extrai áudio → whisper.
3. `media.describe_image`  
	Entrada: idem; Engine: **GPT-4o-mini visão** (caption+OCR) ou **Tesseract** + um “captioner” (modelo leve).  
	Saída: `{ "text": "..." }`
4. `media.parse_document`  
	PDF/DOCX/PNG escaneado.  
	Engine: **unstructured** / **pymupdf** / **docling** (fica leve e privado).  
	Saída: `{ "text": "..." }`

> Contrato Único de Saída = **sempre** `{ "text": "..." }`. Isso simplifica o node “Format Response” e a conversa do BRANN.

---

## 3) n8n — bloco de transcrição (copy/cola essencial)

## 3.1 Variáveis de ambiente

No n8n (Settings → Environment variables):

```markdown
EVOLUTION_BASE_URL=https://SEU-HOST:PORTA
EVOLUTION_TOKEN=SEU_TOKEN
EVOLUTION_INSTANCE=BRANN

MEDIA_MCP_URL=http://media-mcp:8080   # (outra opção: microserviços REST)
```

## 3.2 EXTRAIR MÍDIA (Function)

Cole exatamente (sem renomear variáveis); ele detecta o tipo e puxa URLs/caption do WA/Evolution:

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

## 3.3 Switch por mediaType

- Saídas: `0=audio`, `1=video`, `2=image`, `3=text`
- Expressão:
```markdown
{{$json.mediaType === 'audio' ? 0 : $json.mediaType === 'video' ? 1 : $json.mediaType === 'image' ? 2 : 3}}
```

## 3.4 Download da mídia (GET direto se tiver URL; senão POST Evolution)

**IF (tem URL http?)** → **HTTP Request (GET)**  
Response: **File**, `Binary Property` = `media`  
URL: `={{$json.audioUrl || $json.videoUrl || $json.imageUrl}}`

**ELSE** → **HTTP Request (POST)** Evolution:

- URL: `={{$env.EVOLUTION_BASE_URL}}/message/downloadMedia/{{$env.EVOLUTION_INSTANCE}}`
- Headers: `Authorization: ={{'Bearer ' + $env.EVOLUTION_TOKEN}}`
- Body (JSON): `{"messageId":"={{$json.messageId}}"}`
- Response: **File**, `Binary Property` = `media`

> Padroniza o nome binário como `media` para reutilizar o mesmo nó de envio ao MCP.

## 3.5 Chamada ao Media MCP (um nó por tipo, mesma forma)

**HTTP Request → POST**  
URL (exemplos):

- Áudio: `={{$env.MEDIA_MCP_URL}}/tools/media.transcribe_audio`
- Vídeo: `={{$env.MEDIA_MCP_URL}}/tools/media.transcribe_video`
- Imagem: `={{$env.MEDIA_MCP_URL}}/tools/media.describe_image`
- Documento: `={{$env.MEDIA_MCP_URL}}/tools/media.parse_document`

Tipo: **Multipart Form-Data**  
Campos:

- `file`: **Binary** = `media`
- `lang`: `pt` (ou detectado)
- (opcional) `mime`: `={{$binary.media.mimeType}}`

**Resposta esperada**: JSON `{ "text": "..." }`

## 3.6 Normalização → Set (Format Response)

Em todos os ramos:

```markdown
text = {{$json.text || $json.output_text || $json.transcript || $json.caption || $json.description || $json.result || ''}}
```

## 3.7 Devolve ao teu agente

Daqui em diante segue o teu fluxo: **BRANN** → Parser → Segmentos → **Enviar Mensagem** (Evolution).  
Se quiser PTT, mantém o subfluxo `audio_key` que já combinamos e dispara o Kokoro.

---

## 4) Registrar as Tools no Chat Model (function-calling)

Se preferir deixar o **Chat Model** decidir **quando** usar o MCP de mídias (em vez do Switch), registra estas Tools no node OpenAI do n8n:

### media.transcribe\_audio (schema)

```markdown
{
  "name": "media.transcribe_audio",
  "description": "Transcreve áudio para texto PT-BR.",
  "parameters": {
    "type": "object",
    "properties": {
      "url": { "type": "string", "description": "URL pública do arquivo de áudio." },
      "mime": { "type": "string" },
      "lang": { "type": "string", "default": "pt" }
    },
    "required": ["url"]
  }
}
```

### media.transcribe\_video

```markdown
{
  "name": "media.transcribe_video",
  "description": "Transcreve/Resume fala de vídeo. Extrai áudio com ffmpeg.",
  "parameters": {
    "type": "object",
    "properties": {
      "url": { "type": "string" },
      "mime": { "type": "string" },
      "lang": { "type": "string", "default": "pt" }
    },
    "required": ["url"]
  }
}
```

### media.describe\_image

```markdown
{
  "name": "media.describe_image",
  "description": "OCR+legenda curta útil para atendimento.",
  "parameters": {
    "type": "object",
    "properties": {
      "url": { "type": "string" },
      "mime": { "type": "string" }
    },
    "required": ["url"]
  }
}
```

### media.parse\_document

```markdown
{
  "name": "media.parse_document",
  "description": "Extrai texto estruturado de PDF/DOCX.",
  "parameters": {
    "type": "object",
    "properties": {
      "url": { "type": "string" },
      "mime": { "type": "string" }
    },
    "required": ["url"]
  }
}
```

> No n8n, cada Tool pode chamar um **Execute Workflow** que faz: baixar binário → chamar o endpoint do Media MCP → devolver `{text}` para o Chat Model.

---

## 5) (Opcional) Docker para subir os serviços de mídia

`docker-compose.yml` enxuto, local e barato:

```markdown
version: "3.8"
services:
  ffmpeg:
    image: jrottenberg/ffmpeg:6.0-ubuntu
    command: ["-version"]

  whisperx:
    image: ghcr.io/m-bain/whisperx:latest
    volumes: [ "./data:/data" ]
    ports: [ "9001:9001" ]
    command: ["python","server.py","--host","0.0.0.0","--port","9001"]
    # retorna /transcribe -> {"text": "..."}

  unstructured:
    image: downloads.unstructured.io/unstructured-io/unstructured-api:latest
    environment:
      - UNSTRUCTURED_API_KEY=local
    ports: [ "9002:8000" ]
    # POST /general/v0/general -> texto

  media-mcp:
    image: ghcr.io/teu-org/media-mcp:latest   # (ou um pequeno FastAPI teu)
    environment:
      - WHISPERX_URL=http://whisperx:9001
      - UNSTRUCTURED_URL=http://unstructured:8000
    ports: [ "8080:8080" ]
    depends_on: [ whisperx, unstructured ]
```

> Se não quiser MCP agora, usa **só REST** (os mesmos endpoints) e troca `MEDIA_MCP_URL` pelos hosts acima.

---

## 6) Boas práticas (segurança, custo e confiabilidade)

- **Entrada hostil**: valida MIME/ tamanho dos arquivos; limite de 25–50MB por padrão.
- **Timeouts**: n8n → 30–60s; Whisper pode exigir 90s para vídeos longos (quebra em chunks).
- **Logs/Tracing**: adiciona `traceId`, `mediaType`, `latency_ms` antes do BRANN.
- **Fallback**: se download falhar, responde **texto**: “não consegui baixar a mídia; posso seguir por texto?”.
- **Custo**: GPT-4o-mini para imagem/ocr leve; só sobe p/ 4o normal se precisar de leitura densa/diagrama pesado.
- **Privado**: documentos sensíveis → parse com `unstructured` local.

---

## 7) Checklist de “pronto para rodar”

- `.env` no n8n com `EVOLUTION_*` e `MEDIA_MCP_URL`
- EXTRAIR MÍDIA (Function) colado e testado
- Switch por `mediaType` entregando 4 saídas
- Download GET/POST com binário **media**
- POST no **media-mcp** por tipo (áudio/vídeo/imagem/doc)
- `Set` unificando para `text`
- Passagem para BRANN e envio via Evolution
- Logs e fallback de erro habilitados

---

Se quiser, na próxima te mando um **sub-workflow n8n (JSON de import)** só do bloco de transcrição com os 4 ramos já plugados no `MEDIA_MCP_URL` e respostas normalizadas; aí tu só conecta no teu Switch azul e pronto.