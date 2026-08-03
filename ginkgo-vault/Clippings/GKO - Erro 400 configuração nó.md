---
title: "GKO - Erro 400 configuração nó"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/69065ec6-ba70-8325-9258-7f917c2f8129"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sáb., 1 de nov. às 16:25

Objetivo: obter o URL do áudio, transcrever e enviar ao agent.

## Fluxo mínimo

Webhook → `ExtrairÁudioURL` → IF(tem URL) → \[GET Áudio\]: \[Baixar via Evolution\] → OpenAI Transcriptions → `PrepararParaAgent` → HTTP Agent

## 1) Function ExtrairÁudioURL  (copy/cola)

Extrai `audioUrl`, `messageId`, `chatId`, `phone`.

```markdown
// nome do nó: ExtrairÁudioURL
const payload = items[0]?.json ?? {};
const body = payload.body ?? payload;
const data = body.data ?? body;
const key = data.key ?? {};
const msg = data.message ?? body.message ?? {};

// url direta quando o Evolution inclui nos tipos de mídia
const audioUrl = msg.audioMessage?.url ?? null;

const messageId = key.id || data.messageId || body.messageId || payload.messageId || "";
const chatId = key.remoteJid || data.chatId || body.chatId || payload.chatId || "";
const phone = (chatId || "").replace(/@c.us|@s.whatsapp.net/g, "");

return [{ json: { ...payload, audioUrl, messageId, chatId, phone } }];
```

## 2) IF “tem URL?”

Condição:

```markdown
={{ $json.audioUrl && $json.audioUrl.startsWith('http') }}
```
- True → vai para **GET Áudio**.
- False → vai para **Baixar via Evolution**.

## 3A) HTTP GET Áudio

- Method: GET
- URL: `={{$json.audioUrl}}`
- Response: File
- Binary Property: `audio`

## 3B) HTTP Baixar via Evolution

Quando não existe URL direta.

- Method: POST
- URL: `={{$env.EVOLUTION_BASE_URL}}/message/downloadMedia/{{$env.EVOLUTION_INSTANCE}}`
- Headers:
	- `Authorization: ={{'Bearer ' + $env.EVOLUTION_TOKEN}}`
		- `Content-Type: application/json`
- Body raw (JSON):
```markdown
{ "messageId": "={{$json.messageId}}" }
```
- Response: File
- Binary Property: `audio`

## 4) OpenAI Transcriptions

- Resource: Audio Transcriptions
- Model: `whisper-1`
- Input: Binary
- Binary Property: `audio`
- Saída esperada: campo `text` com a transcrição.

## 5) Function PrepararParaAgent

Padroniza payload para seu agent.

```markdown
// nome do nó: PrepararParaAgent
const j = items[0].json;
return [{
  json: {
    from: j.phone,
    chatId: j.chatId,
    messageId: j.messageId,
    type: "audio_transcript",
    transcript: j.text || j.transcription || j.transcript || ""
  }
}];
```

## 6) HTTP Enviar ao Agent

- Method: POST
- URL: `={{$env.AGENT_URL}}/inbox/messages`
- Headers:
	- `Authorization: ={{'Bearer ' + $env.AGENT_TOKEN}}`
		- `Content-Type: application/json`
- Body raw (JSON): `={{$json}}`

## Variáveis no n8n

```markdown
EVOLUTION_BASE_URL=https://seu-host:suaporta
EVOLUTION_INSTANCE=BRANN
EVOLUTION_TOKEN=xxxxx
AGENT_URL=https://agent.seudominio/api
AGENT_TOKEN=yyyyy
```

## Notas rápidas

- O nó do seu print dava 400 porque usava operação errada e `messageId` inconsistente. Acima padroniza.
- Whisper aceita mp3/ogg/m4a/mp4/webm. Sem conversão.
- Se o WhatsApp expirar a mídia, a rota de download retorna 400. Trate com mensagem de falha ou peça reenvio.

{ "workflow": "ElevenLabs TTS com Evolution API", "nodes\_configuration": { "1\_when\_executed\_by\_another\_workflow": { "name": "When Executed by Another Workflow", "type": "n8n-nodes-base.executeWorkflowTrigger", "parameters": {}, "notes": "Recebe os dados do workflow pai", "expected\_input": { "text": "Texto para converter em áudio", "voice\_id": "21m00Tcm4TlvDq8ikWAM", "phone": "5511999999999", "instance": "nome\_da\_instancia" } }, "2\_elevenlabs\_tts": { "name": "ElevenLabs TTS", "type": "n8n-nodes-base.httpRequest", "parameters": { "method": "POST", "url": "=https://api.elevenlabs.io/v1/text-to-speech/{{ $json.voice\_id || '21m00Tcm4TlvDq8ikWAM' }}", "authentication": "genericCredentialType", "genericAuthType": "httpHeaderAuth", "sendHeaders": true, "headerParameters": { "parameters": \[ { "name": "xi-api-key", "value": "=SUA\_API\_KEY\_AQUI" }, { "name": "Content-Type", "value": "application/json" } \] }, "sendBody": true, "contentType": "json", "bodyParameters": { "parameters": \[\] }, "jsonBody": "={\\n \\"text\\": \\"{{ $json.text }}\\",\\n \\"model\_id\\": \\"eleven\_multilingual\_v2\\",\\n \\"voice\_settings\\": {\\n \\"stability\\": 0.5,\\n \\"similarity\_boost\\": 0.8,\\n \\"style\\": 0.0,\\n \\"use\_speaker\_boost\\": true\\n }\\n}", "options": { "response": { "response": { "responseFormat": "file", "outputPropertyName": "data" } } } }, "notes": "Converte texto em áudio usando ElevenLabs" }, "3\_write\_binary\_file": { "name": "Write Binary File", "type": "n8n-nodes-base.writeBinaryFile", "parameters": { "fileName": "=/tmp/audio\_{{ $now.toFormat('yyyyMMdd\_HHmmss') }}.mp3", "dataPropertyName": "data", "options": {} }, "notes": "Salva o arquivo de áudio temporariamente" }, "4\_processar\_resposta": { "name": "Processar Resposta", "type": "n8n-nodes-base.code", "parameters": { "mode": "runOnceForAllItems", "jsCode": "const items = $input.all();\\nconst result = \[\];\\n\\nfor (const item of items) {\\n result.push({\\n json: {\\n phone: item.json.phone,\\n instance: item.json.instance,\\n audioPath: item.json.fileName,\\n audioData: item.binary.data\\n },\\n binary: {\\n data: item.binary.data\\n }\\n });\\n}\\n\\nreturn result;" }, "notes": "Prepara os dados para envio via Evolution API" }, "5\_evolution2": { "name": "Evolution2", "type": "n8n-nodes-base.httpRequest", "parameters": { "method": "POST", "url": "=https://SUA\_EVOLUTION\_API/message/sendMedia/{{ $json.instance }}", "authentication": "genericCredentialType", "genericAuthType": "httpHeaderAuth", "sendHeaders": true, "headerParameters": { "parameters": \[ { "name": "apikey", "value": "SUA\_APIKEY\_EVOLUTION" }, { "name": "Content-Type", "value": "application/json" } \] }, "sendBody": true, "contentType": "json", "bodyParameters": { "parameters": \[\] }, "jsonBody": "={\\n \\"number\\": \\"{{ $json.phone }}\\",\\n \\"mediatype\\": \\"audio\\",\\n \\"mimetype\\": \\"audio/mpeg\\",\\n \\"media\\": \\"{{ $binary.data }}\\",\\n \\"fileName\\": \\"audio.mp3\\"\\n}", "options": {} }, "notes": "Envia o áudio via WhatsApp usando Evolution API" } }, "credentials\_needed": { "elevenlabs": { "type": "Header Auth", "header\_name": "xi-api-key", "header\_value": "SUA\_CHAVE\_ELEVENLABS", "get\_key\_at": "https://elevenlabs.io/app/settings/api-keys" }, "evolution\_api": { "type": "Header Auth", "header\_name": "apikey", "header\_value": "SUA\_CHAVE\_EVOLUTION", "url\_base": "https://sua-evolution-api.com" } }, "voice\_ids\_elevenlabs": { "portugues\_brasil": \[ { "id": "FGY2WhTYpPnrIDTdsKH5", "name": "Laura", "language": "pt-BR" }, { "id": "GBv7mTt0atIp3Br8iCZE", "name": "Thiago", "language": "pt-BR" } \], "ingles": \[ { "id": "21m00Tcm4TlvDq8ikWAM", "name": "Rachel" }, { "id": "EXAVITQu4vr4xnSDxMaL", "name": "Bella" } \] }, "exemplo\_chamada": { "from\_parent\_workflow": { "text": "Olá! Esta é uma mensagem de teste do sistema de TTS.", "voice\_id": "FGY2WhTYpPnrIDTdsKH5", "phone": "5511999999999", "instance": "minha\_instancia" } } }

Correção de ponta a ponta. Envie áudio do ElevenLabs para WhatsApp via Evolution sem escrever arquivo nem JS extra.

## Fluxo final

When Executed by Another Workflow → ElevenLabs TTS → Evolution sendMedia

## 1) ElevenLabs TTS (HTTP Request)

- Method: POST
- URL:
```markdown
=https://api.elevenlabs.io/v1/text-to-speech/{{ $json.voice_id || '21m00Tcm4TlvDq8ikWAM' }}
```
- Headers:
```markdown
xi-api-key: ={{$env.ELEVEN_API_KEY}}
Content-Type: application/json
Accept: audio/mpeg
```
- Body (JSON):
```markdown
{
  "text": "={{$json.text}}",
  "model_id": "eleven_multilingual_v2",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.8,
    "style": 0,
    "use_speaker_boost": true
  }
}
```
- Options → Response:
	- Response Format: **File**
		- Output property name: **audio** ← importante

Resultado: sai com `binary.audio` contendo MP3.

## 2) Evolution — enviar áudio (HTTP Request)

- Method: POST
- URL:
```markdown
={{$env.EVOLUTION_BASE_URL}}/message/sendMedia/{{ $json.instance || $env.EVOLUTION_INSTANCE }}
```
- Headers:
```markdown
apikey: {{$env.EVOLUTION_API_KEY}}
Content-Type: application/json
```
- Body (JSON):
```markdown
{
  "number": "={{ $json.phone.match(/@c\.us|@s\.whatsapp\.net/) ? $json.phone : $json.phone + '@c.us' }}",
  "mediatype": "audio",
  "mimetype": "audio/mpeg",
  "fileName": "tts.mp3",
  "media": "={{$binary.audio.data}}"
}
```

Observações técnicas

- Use `Accept: audio/mpeg` no ElevenLabs para receber binário direto.
- Não use `{{ $binary.data }}` no JSON. O correto é `{{$binary.audio.data}}` que é a string base64.
- `Write Binary File` e “Processar Resposta” são desnecessários. Remova.
- `number` precisa terminar com `@c.us`. A expressão adiciona se faltar.
- Se quiser “áudio de voz” (PTT) e sua versão da Evolution suportar, adicione `"ptt": true` no corpo.
- Parametrize via env:
```markdown
ELEVEN_API_KEY=...
EVOLUTION_BASE_URL=https://sua-evolution
EVOLUTION_API_KEY=...
EVOLUTION_INSTANCE=BRANN
```

Entrada esperada no gatilho filho

```markdown
{
  "text": "Olá! Esta é uma mensagem de teste.",
  "voice_id": "FGY2WhTYpPnrIDTdsKH5",
  "phone": "5511999999999",
  "instance": "BRANN"
}
```

Se precisar manter o salvamento em disco, troque o `Output property name` para `data` e use `{{$binary.data.data}}` no corpo do Evolution.

Plano de ação nó-por-nó. Copie e cole exatamente.

## 0) Variáveis de ambiente no n8n

```markdown
ELEVEN_API_KEY=coloque_sua_chave
EVOLUTION_BASE_URL=https://SEU-HOST:PORTA
EVOLUTION_API_KEY=coloque_sua_chave
EVOLUTION_INSTANCE=BRANN
```

## 1) When Executed by Another Workflow

Sem parâmetros. Entrada esperada do workflow pai:

```markdown
{
  "text": "Olá! Mensagem teste.",
  "voice_id": "FGY2WhTYpPnrIDTdsKH5",
  "phone": "5511999999999",
  "instance": "BRANN"
}
```

## 2) ElevenLabs TTS (HTTP Request)

- Method: `POST`
- URL:
```markdown
=https://api.elevenlabs.io/v1/text-to-speech/{{ $json.voice_id || '21m00Tcm4TlvDq8ikWAM' }}
```
- Headers:
```markdown
xi-api-key: ={{$env.ELEVEN_API_KEY}}
Content-Type: application/json
Accept: audio/mpeg
```
- Body → JSON:
```markdown
{
  "text": "={{$json.text}}",
  "model_id": "eleven_multilingual_v2",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.8,
    "style": 0,
    "use_speaker_boost": true
  }
}
```
- Options → Response:
	- Response Format: **File**
		- Output property name: **audio**

> Saída: `binary.audio` com o MP3.

## 3) Write Binary File (opcional, só se quiser salvar no disco)

- File Name:
```markdown
=/tmp/tts_{{ $now.toFormat('yyyyMMdd_HHmmss') }}.mp3
```
- Binary Property: `audio`

> Se não precisa salvar, pule este nó e ligue o ElevenLabs direto no Evolution.

## 4) Evolution2 (HTTP Request) — enviar áudio

- Method: `POST`
- URL:
```markdown
={{$env.EVOLUTION_BASE_URL}}/message/sendMedia/{{ $json.instance || $env.EVOLUTION_INSTANCE }}
```
- Headers:
```markdown
apikey: {{$env.EVOLUTION_API_KEY}}
Content-Type: application/json
```
- Body → JSON:
```markdown
{
  "number": "={{ $json.phone.match(/@c\.us|@s\.whatsapp\.net/) ? $json.phone : $json.phone + '@c.us' }}",
  "mediatype": "audio",
  "mimetype": "audio/mpeg",
  "fileName": "tts.mp3",
  "media": "={{$binary.audio.data}}"
}
```

## 5) Teste rápido

No workflow pai, use um **Execute Workflow** apontando para este fluxo e passe o JSON de entrada do passo 1. Verifique:

- ElevenLabs retorna **Status 200** e `binary.audio` presente.
- Evolution responde `{ "status": "success" }` ou similar.

## Erros comuns e correção

- **binary incorreto**: use `{{$binary.audio.data}}`, não `{{$binary.data}}`.
- **número inválido**: sempre termine com `@c.us`. Expressão acima faz isso.
- **401 no ElevenLabs**: checar `ELEVEN_API_KEY` e header `xi-api-key`.
- **401/403 no Evolution**: checar `EVOLUTION_API_KEY` e URL base.
- **415/400 no Evolution**: `Content-Type: application/json` e `media` em base64.
- **latência alta**: remova o Write Binary File.

Quer a versão JSON de importação do n8n com esses quatro nós? Posso enviar pronta.