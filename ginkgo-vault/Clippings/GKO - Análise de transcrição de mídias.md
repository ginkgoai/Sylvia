---
title: "GKO - Análise de transcrição de mídias"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/68f81bca-89c0-8326-b244-225865da70a3"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
ter., 21 de out. às 20:48

bloco de transcrição de midias, o que achou, podemos fazer assim?

e pra excluir os edits fields e deixar so omsg usuario final?

assim?

ter., 21 de out. às 22:35

olha agora?

Perfeito, Gabriel — **agora sim!**  
O teu fluxo está **exatamente na estrutura certa** para a fase de configuração. O nó **“Code in JavaScript”** (que substitui o antigo “Function”) está no lugar ideal — entre “Parâmetros API” e “Direcionamento” — e está fazendo o papel de extrair e normalizar os dados.

Vamos revisar rapidinho a arquitetura pra garantir que estás com a visão limpa antes de configurar um a um:

---

### ✅ Situação Atual — Correta e funcional

**🟩 Evento e Dados da API**

- `Webhook`: recebe o POST do Evolution.
- `Parâmetros API`: só organiza o corpo.
- `Code in JavaScript`: transforma a mensagem bruta em um objeto padronizado com:
	- `mediaType` (audio/video/image/text)
		- `text`, `chatId`, `phone`, `messageId`
		- `audioUrl`, `videoUrl`, `imageUrl`

**🔵 Transcrição de Mídias**

- `Direcionamento (Switch)`: divide as saídas conforme o `mediaType`.
	- Saída 0 → Áudio
		- Saída 1 → Vídeo
		- Saída 2 → Imagem
		- Saída 3 → Texto
- `Translate a recording` → IA que transcreve áudio.
- `Analyze image` → IA que interpreta imagem.
- `Analyze Video with Gemini` → IA que resume vídeo.
- `Markdown` → Texto puro.
- Todas as saídas convergem para `Mensagem Usuário (Parâmetros)`.

**🟥 Buffer de Mensagens**

- Correto: Mensagem Usuário → Criar Lista MSG → Espera → Busca MSG → Continua fluxo.
- MCP Supabase vai poder ser conectado depois, se quiser logar os resultados.

---

### ⚙️ Próximo Passo — Configuração nó a nó

Agora que a estrutura está certa, vamos configurar os nós internos, começando pelo **de áudio**.

---

#### 🎧 1. Translate a recording (áudio)

**Tipo:** OpenAI Chat Model (ou equivalente)  
**Input:** binário `audio`  
**System:**

```markdown
Transcreva o áudio em português do Brasil. Retorne apenas o texto puro, sem formatação ou comentários.
```

**Temperature:** 0.3  
**Max tokens:** 1000  
**Timeout:** 30s  
**Binary property:** `audio`  
**Output:** Deve gerar um campo `text` (ou `output_text`).

---

#### 🔍 2. Analyze image

**Binary property:** `image`  
**System:**

```markdown
Descreva a imagem em até 3 frases úteis para atendimento comercial; se houver texto legível, inclua. 
Responda em JSON: { "text": "..." }.
```

---

#### 🎬 3. Analyze Video with Gemini

**Input:** binário `video`  
**Prompt:**

```markdown
Resuma e transcreva o conteúdo do vídeo em português do Brasil, focando no contexto e falas principais.
```

(Ou usa o campo “System Prompt” se for node OpenAI, mesmo formato.)

---

#### 📝 4. Markdown (texto)

**Type:** HTTP Request ou Function simples que apenas passa `$json.text` adiante.  
Serve para casos em que o input é só texto — sem IA.

---

#### 🔧 5. Mensagem Usuário (Parâmetros)

**Campos:**

```markdown
text = {{$json.text || $json.output_text || $json.transcript || $json.caption || $json.description || $json.result || $json.candidates?.[0]?.content?.parts?.[0]?.text || ''}}
mediaType = {{$json.mediaType}}
chatId = {{$json.chatId}}
phone = {{$json.phone}}
```

---

Perfeito.  
Se tu confirmar, eu já te passo o **passo a passo completo para configurar o node “Translate a recording”** com todos os parâmetros visuais exatos (como preencher cada campo do painel n8n).

Quer que a gente configure esse primeiro agora?

Curtíssimo: o fluxo da comunidade é um “canivete” para **documentos**; o teu é uma “espinha dorsal” unificada para **todas as mídias** (com buffer, memória e hand-off pro Brann). Os dois não brigam — **se complementam**.

## O que muda (em bom português)

**Fluxo da comunidade (print)**

- Puxa **URL de mídia do WhatsApp** por tipo (áudio, imagem, documento).
- Faz **download** por tipo.
- Para **documentos**, faz um **segundo Switch por extensão/MIME** e usa nós específicos:
	- PDF → “Extrato de PDF”
		- XLS / XLSX → “Extrato de XLS/XLSX”
		- Mapa JSON (gera estrutura)
		- “Enviar resposta sem suporte” se não reconhecer
- Usa nós “Prompt de imagem/de documento” para formatar o texto final.

**Teu fluxo**

- Normaliza tudo num **Code/Function** e faz **um único Switch** (audio/video/image/text).
- IA dedicada por mídia (transcrever, resumir, descrever).
- **Unificador** “Mensagem Usuário” → **Buffer de Mensagens** → **Brann**.
- **Sem** a árvore de documentos (PDF/XLS/XLSX) ainda — esse é o único “buraco” em relação ao da comunidade.

## Prós/Contras

- **Teu**: mais limpo, escalável, com buffer, memória e saída única pro Brann.  
	**Falta**: ramo de documentos com parsers por tipo.
- **Comunidade**: excelente **tratamento profundo de documentos** com fallback “sem suporte”.  
	**Falta**: unificação/Buffer/Brann, e tende a duplicar lógica.

## O que eu faria (mínimo cirúrgico no teu)

Mantém tua arquitetura e **encaixa um ramo “documentos”** igual ao da comunidade, mas plugado no teu unificador:

1. **No Code/Function**, detecta `mediaType = 'document'` quando vier documento (mesma lógica que já usas para image/audio/video) e salva:
```markdown
const docUrl   = msg_.documentMessage?.url ?? null;
const fileName = msg_.documentMessage?.fileName ?? null;
const mimeType = msg_.documentMessage?.mimetype ?? null;
```

Inclui `docUrl`, `fileName`, `mimeType` no objeto retornado.

2. **No Switch Direcionamento**, adiciona a 5ª saída:
- 0=audio, 1=video, 2=image, 3=text, **4=document**
3. **Download do documento** (GET se URL pública; senão POST `/message/downloadMedia`), `Binary Property: document`.
4. **Descobrir extensão/MIME** (Function rápido):
```markdown
const bin = $binary.document || {};
const mt  = bin.mimeType || $json.mimeType || '';
const fn  = $json.fileName || '';
const ext = (fn.split('.').pop() || '').toLowerCase();
return [{json: {...$json, _mime: mt, _ext: ext}}];
```
5. **Switch “Tipos de documentos”** por MIME/EXT:
```markdown
{{ $json._mime.startsWith('application/pdf') || $json._ext === 'pdf' ? 0
 : ['xls','xlsx'].includes($json._ext) || $json._mime.includes('spreadsheet') ? 1
 : ['csv'].includes($json._ext) || $json._mime.includes('csv') ? 2
 : ['txt','md','rtf','doc','docx'].includes($json._ext) ? 3
 : 4 }}
```
- 0 → PDF
- 1 → XLS/XLSX
- 2 → CSV
- 3 → TXT/MD/DOC/DOCX
- 4 → **sem suporte**
6. **Parsers por caso**
- **PDF**: usa o node “Extract from PDF” (ou “Read PDF”) → sai `text`.
- **XLS/XLSX**: “Spreadsheet File → JSON” → faz um **Function** para resumir colunas/linhas em texto:
	```markdown
	const rows = items.map(i=>i.json);
	const preview = rows.slice(0,10);
	return [{json:{ text: \`Planilha com ${rows.length} linhas.\nAmostra:\n\` + JSON.stringify(preview, null, 2) }}];
	```
- **CSV**: idem XLSX (converter pra JSON e resumir).
- **TXT/MD/DOC/DOCX**:
	- TXT/MD → “Read Binary File → to String”.
		- DOC/DOCX → se tiver nó “Office Parser”; senão manda binário pra um **LLM com file understanding** e pede *“extraia e devolva texto puro”*.
- **Sem suporte**: Set → `text = "Não consegui extrair do arquivo enviado (tipo não suportado). Pode enviar PDF/TXT/CSV/XLSX?"`
7. **Todas as saídas** entram no teu **“Mensagem Usuário (Parâmetros)”**, que já unifica:
```markdown
text = {{$json.text || $json.output_text || $json.transcript || $json.caption || $json.description || $json.result || $json.candidates?.[0]?.content?.parts?.[0]?.text || ''}}
```
8. **Pronto**: o restante do teu fluxo (Buffer → Brann) fica igual.

## Por que isso é melhor

- Manténs teu **core limpo** e **a lógica de atendimento** intacta.
- Ganha o **poder de parsing de documentos** do exemplo da comunidade.
- Evita espalhar prompts e “Edit Fields” a cada ramificação.

## Quer o bloco pronto?

Posso te gerar agora o **JSON de import** apenas do subfluxo **Documentos** (com Switch, download, parsers e unificação) para plugar na tua saída 4 do Direcionamento. Depois, se quiser, faço o fallback GET/POST de mídia (áudio/imagem/vídeo/documento) embalado também.

certo. tambem encontrei esse aqui. vamo unir o melhor de todos aos blocos do brann, mudar oq e whats para evo e configurar os nos corretamente.

Bora unir tudo num **bloco único e sólido**, já no padrão do Brann, trocando “Whats” por **Evolution API** e deixando cada nó configurável no modo **copy/cola**.

Vou te entregar em 7 partes: visão, `.env`, nó de normalização, roteador, trilhas (texto/áudio/imagem/documento), unificador → buffer/Brann, e logs.

---

## Visão (arquitetura final)

```markdown
Webhook → Parâmetros API → Code in JavaScript (EXTRAIR MÍDIA) 
   → Switch (Input type: audio | video | image | text | document)

  • TEXT     → Mensagem Usuário (Parâmetros)
  • VOICE    → [IF URL? → GET | POST Evolution /downloadMedia] → Transcribe Audio → Mensagem Usuário
  • IMAGE    → [IF URL? → GET | POST Evolution /downloadMedia] → Analyze Image → Mensagem Usuário
  • DOCUMENT → [IF URL? → GET | POST Evolution /downloadMedia] → Detect MIME/EXT → 
                  Switch doc-types (PDF | XLSX | CSV | TXT/MD | DOC/DOCX | fallback) → Mensagem Usuário

Mensagem Usuário → Buffer de Mensagens (CRIA LISTA MSG → ESPERA → BUSCA MSG → …) → Brann
(+ opcional: logs no MCP/Supabase)
```

---

## 1) Variáveis de ambiente (.env do n8n)

Em **Settings → Environment variables**:

```markdown
EVOLUTION_BASE_URL=https://SEU-HOST:PORTA
EVOLUTION_TOKEN=SEU_TOKEN
EVOLUTION_INSTANCE=BRANN
```

> Se tiver proxy/SSL, o `BASE_URL` deve estar exatamente como tu usa no POST do Evolution.

---

## 2) Code in JavaScript (EXTRAIR MÍDIA)

Coloca este código no nó logo após “Parâmetros API”:

```markdown
const payload = items[0]?.json ?? {};
const body_   = payload.body ?? payload;
const data_   = body_.data ?? body_;
const key_    = data_.key ?? {};
const msg_    = data_.message ?? body_.message ?? {};

const text = msg_.conversation 
  || msg_.extendedTextMessage?.text 
  || msg_.imageMessage?.caption 
  || msg_.videoMessage?.caption 
  || msg_.documentMessage?.caption 
  || "";

const chatId    = key_.remoteJid || data_.chatId || body_.chatId || payload.chatId || "";
const phone     = (chatId || "").replace(/@c.us|@s.whatsapp.net/g, "");
const messageId = key_.id || data_.messageId || body_.messageId || "";

let mediaType = "text";
if (msg_.audioMessage)    mediaType = "audio";
else if (msg_.videoMessage)   mediaType = "video";
else if (msg_.imageMessage)   mediaType = "image";
else if (msg_.documentMessage) mediaType = "document";

const audioUrl = msg_.audioMessage?.url ?? null;
const videoUrl = msg_.videoMessage?.url ?? null;
const imageUrl = msg_.imageMessage?.url ?? null;
const docUrl   = msg_.documentMessage?.url ?? null;
const fileName = msg_.documentMessage?.fileName ?? null;
const mimeType = msg_.documentMessage?.mimetype ?? null;

return [{
  json: { ...payload, text, chatId, phone, messageId, mediaType, audioUrl, videoUrl, imageUrl, docUrl, fileName, mimeType }
}];
```

---

## 3) Switch “Input type”

**Mode:** Expression  
**Number of outputs:** 5  
**Expression:**

```markdown
{{$json.mediaType === 'audio' ? 0 
 : $json.mediaType === 'video' ? 1
 : $json.mediaType === 'image' ? 2
 : $json.mediaType === 'document' ? 3
 : 4}}
```
- 0=Audio, 1=Video, 2=Image, 3=Document, 4=Text

*(Se não vai tratar vídeo agora, pode redirecionar 1→Text.)*

---

## 4) Trilhas (config nó a nó)

## 4.1 TEXT

Liga a saída 4 direto em **Mensagem Usuário (Parâmetros)**.

## 4.2 VOICE (áudio)

### IF “tem URL?”

Expression:

```markdown
{{$json.audioUrl && $json.audioUrl.startsWith('http')}}
```
- **TRUE → HTTP Request (GET)**
	- Authentication: None
		- URL: `={{$json.audioUrl}}`
		- Response: **File**
		- Binary Property: `audio`
- **FALSE → HTTP Request (POST) Evolution**
	- URL: `={{$env.EVOLUTION_BASE_URL}}/message/downloadMedia/{{$env.EVOLUTION_INSTANCE}}`
		- Method: POST
		- Headers:
		- `Authorization: ={{'Bearer ' + $env.EVOLUTION_TOKEN}}`
				- `Content-Type: application/json`
		- Body (JSON):
		```markdown
		{ "messageId": "={{$json.messageId}}" }
		```
		- Response: **File**
		- Binary Property: `audio`

### Transcribe Audio (OpenAI/GPT-4o mini)

- **Input:** Binary `audio`
- **System:**
	```markdown
	Transcreva o áudio em português do Brasil. Retorne apenas o texto puro, sem comentários ou metadados.
	```
- **Temperature:** 0.3
- **Max tokens:** 1000
- **Saída esperada:** `text` (ou `output_text`)

> Se teu node não cria `text`, a gente normaliza no unificador (abaixo).

## 4.3 IMAGE

Mesma lógica de **IF URL?** e **GET/POST Evolution**, mas com:

- Binary Property: `image`
- Depois, **Analyze Image** (OpenAI visão):
	- **Binary:** `image`
		- **Prompt/System:**
		```markdown
		Descreva a imagem em até 3 frases úteis para atendimento comercial. 
		Se houver texto legível, inclua. 
		Responda em JSON: { "text": "..." }.
		```
		- Saída: deve conter `text` (ou a gente extrai do JSON no unificador).

## 4.4 DOCUMENT

### IF URL?

Como acima, mas **Binary Property: `document`**.

### Detectar MIME/EXT (Function)

```markdown
const bin = $binary.document || {};
const mt  = bin.mimeType || $json.mimeType || '';
const fn  = $json.fileName || '';
const ext = (fn.split('.').pop() || '').toLowerCase();
return [{ json: { ...$json, _mime: mt, _ext: ext } }];
```

### Switch “Tipos de documentos”

Expression:

```markdown
{{ $json._mime.startsWith('application/pdf') || $json._ext === 'pdf' ? 0
 : ['xls','xlsx'].includes($json._ext) || $json._mime.includes('spreadsheet') ? 1
 : $json._ext === 'csv' || $json._mime.includes('csv') ? 2
 : ['txt','md'].includes($json._ext) || $json._mime.startsWith('text/') ? 3
 : ['doc','docx'].includes($json._ext) ? 4
 : 5 }}
```

**Saídas:**  
0=PDF, 1=XLS/XLSX, 2=CSV, 3=TXT/MD, 4=DOC/DOCX, 5=fallback

#### PDF

- Node: **Extract from PDF** (ou equivalente “Read PDF”)
- Saída: deve virar `text`

#### XLS/XLSX

- Node: **Spreadsheet File → JSON**
- Depois, **Function** para resumir:
	```markdown
	const rows = items.map(i=>i.json);
	const preview = rows.slice(0, 10);
	return [{
	  json: { 
	    text: \`Planilha com ${rows.length} linhas.\nAmostra:\n\` + JSON.stringify(preview, null, 2) 
	  }
	}];
	```

#### CSV

- Converter para JSON (mesmo nó da planilha) → usar **Function** acima.

#### TXT/MD

- Converter binário → string (nó de conversão) e setar em `text`.

#### DOC/DOCX

- Se tiver nó parser MS Office, usa.
- Se não: mandar binário para um modelo com *file understanding* pedindo:
	```markdown
	Extraia e devolva o conteúdo como texto puro.
	```
	*(ou usa uma lib/serviço próprio no futuro — por ora, manter simples)*

#### Fallback

- **Set**:
	```markdown
	text = "Não consegui extrair do arquivo enviado (tipo não suportado). Pode enviar PDF/TXT/CSV/XLSX?"
	```

Todas as saídas de documento vão para **Mensagem Usuário (Parâmetros)**.

---

## 5) Mensagem Usuário (Parâmetros) — unificador

Preenche os campos com estas expressões:

```markdown
text = {{$json.text 
  || $json.output_text 
  || $json.transcript 
  || $json.caption 
  || $json.description 
  || $json.result 
  || $json.candidates?.[0]?.content?.parts?.[0]?.text 
  || (typeof $json === 'string' ? $json : '')}}

mediaType = {{$json.mediaType 
  || ($json.imageUrl ? 'image' : ($json.audioUrl ? 'audio' : ($json.videoUrl ? 'video' : ($json.docUrl ? 'document' : 'text'))))}}

chatId = {{$json.chatId}}
phone  = {{$json.phone}}
```

> Daqui em diante, segue teu **Buffer de Mensagens** e o **Brann** sem mudanças.

---

## 6) Brann (Message a model)

Mantém como já está. Se quiser *hardening*:

- **Temp:** 0.4
- **Max tokens:** 1200–1600
- **Session ID (memória):** `={{$json.phone || $json.chatId}}`
- **System (corporativo curto):**
	```markdown
	Você é o BRANN, atendente da Ginkgo AI Systems. Seja claro, direto e útil. 
	Foque em próximos passos práticos. Quando faltar dado, ofereça opções: ver planos, projeto personalizado, falar com humano.
	Evite prometer preços sem consulta.
	```

---

## 7) Logs (opcional, MCP/Supabase)

Antes do MCP, um **Set** de telemetria:

```markdown
traceId     = {{$json.messageId}}
mediaType   = {{$json.mediaType}}
text_len    = {{ ($json.text || '').length }}
created_at  = {{$now}}
```

Grava isso no Supabase para painéis de qualidade (falhas por mídia, tamanho médio, etc.).

---

## Check rápido (sanidade)

- Texto simples → resposta do Brann.
- Áudio curto → transcrição → resposta.
- Imagem com texto → `text` entra no Brann.
- PDF/XLSX/CSV → extrai → resume → resposta.
- DOC/DOCX → tenta parser; se não houver parser, usa fallback.

---

Se quiser, eu monto **um JSON de import** só desse subfluxo “Transcrição de Mídias (com Documentos)” já com:

- GET/POST Evolution configurado,
- Switches prontos,
- Prompts e Functions aplicados,
- Unificação no `Mensagem Usuário`.

Daí tu só conecta no teu Buffer/Brann.