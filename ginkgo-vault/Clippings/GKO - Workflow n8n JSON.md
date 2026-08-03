---
title: "GKO - Workflow n8n JSON"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/692225ef-93ac-8327-aa60-1a9a764c2f4e"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sáb., 22 de nov. às 18:06

Aqui vai um **fluxo simples, limpo e funcional** de **injeção de documentos no Qdrant** usando **n8n + seu cluster Qdrant Cloud**.  
Pensa nisso como um cano direto: **upload → split → embed → gravar vetor → pronto.**  
Sem gordura, sem ruído. Apenas o necessário para começar a alimentar o cérebro vetorial da Ginkgo.

---

## ✔️ OBJETIVO

Criar um pipeline de ingestão manual onde você envia **PDF/TXT/DOCX**, o n8n:

1. Recebe o arquivo (form)
2. Extrai o conteúdo
3. Divide em chunks
4. Gera embeddings
5. Salva no Qdrant

---

## ✔️ ARQUITETURA MENTAL (grafo sci-fi)

```markdown
[On Form Submission]
        ↓
[Extract File Text]
        ↓
[Split in Chunks  (300–500 tokens)]
        ↓
[OpenAI Embeddings  (text-embedding-3-large)]
        ↓
[Qdrant Upsert Vector]
```

Essa é a **rota mínima** para qualquer RAG simples. É o esqueleto do Leaf, Brann, Wave — tudo parte daqui.

---

## ✔️ PASSO A PASSO (COPY/COLA)

## 🔹 1. Node — On Form Submission

Use o “Form Trigger” do n8n.

Campos:

- File (input type = file)
- categoria (opcional)
- origem (opcional)

**Output esperado**:

```markdown
binary.data
json.nome_do_arquivo
```

---

## 🔹 2. Node — Convert Binary → Texto (PDF/TXT/DOCX)

Use o node **"Read Binary File"** ou **"Extract from File"** dependendo do formato.

Se o arquivo for PDF, use:

**Node:** *PDF Extract*

Config:

- **Binary Property:** `data`
- **Extract Text:** ON

Resultado esperado:

```markdown
json.text
```

Se for TXT ou DOCX:

- Use “Convert Binary to Text”
- Encoding: UTF-8

---

## 🔹 3. Node — Function → Chunk Splitter

Cria chunks de 300–500 tokens (ideal para embeddings baratos e úteis).

Cole exatamente:

```markdown
const text = $json.text || "";
const chunkSize = 800; // ~300–500 tokens
const chunks = [];

for (let i = 0; i < text.length; i += chunkSize) {
  chunks.push(text.slice(i, i + chunkSize));
}

return chunks.map((c, idx) => ({
  json: {
    chunk: c,
    index: idx,
    source: $json.filename || $json.fileName || "manual-upload"
  }
}));
```

Saída = vários itens, cada um contendo:

```markdown
chunk
index
source
```

---

## 🔹 4. Node — OpenAI Embeddings

Use **text-embedding-3-large (barata + excelente)**.

Config:

- Model: **text-embedding-3-large**
- Input: `{{$json.chunk}}`
- Output field: `embedding`

Resultado esperado:

```markdown
json.embedding (array de float)
json.chunk
json.source
json.index
```

---

## 🔹 5. Node — HTTP Request → Qdrant Upsert

O n8n ainda não tem node nativo completo para Qdrant Cloud, então faça por **HTTP POST**.

### Coisas que você precisa do Qdrant:

- URL base do cluster (ex: `https://xxxxx.us-east4-0.aws.cloud.qdrant.io`)
- API KEY do cluster
- Nome da collection: **ginkgo\_docs** (exemplo)

### Criar Collection antes:

Execute isso no Qdrant (no painel **Collections → Create**):

**Collection name:** `ginkgo_docs`  
**Vector size:** 3072 (embedding-3-large)  
**Distance:** cosine

### Node HTTP (copy/cola)

**Method:** POST  
**URL:**

```markdown
https://SEU-CLUSTER.qdrant.io/collections/ginkgo_docs/points
```

**Headers:**

```markdown
Content-Type: application/json
api-key: SEU_API_KEY
```

**Body (raw):**

```markdown
{
  "points": [
    {
      "id": "={{$json.source + '-' + $json.index}}",
      "vector": "={{$json.embedding}}",
      "payload": {
        "text": "={{$json.chunk}}",
        "source": "={{$json.source}}",
        "index": "={{$json.index}}"
      }
    }
  ]
}
```

Esse node será executado **uma vez para cada chunk** → ingestão perfeita.

---

## ✔️ COMO TESTAR

1. Ative o workflow
2. Abra o form
3. Envie um PDF com 4+ páginas
4. Veja:
	- 10–30 chunks gerados
		- Cada chunk recebendo embedding
		- Qdrant recebendo todos os vetores

No painel do Qdrant, vá em:

**Collections → ginkgo\_docs → Points → Browse**

Você verá cada registro com:

- payload.text
- source
- embedding
- id

---

## ✔️ RESULTADO

Com esse pipeline, você tem:

- **Ingestão manual perfeita**
- **Chunks otimizados**
- **Embeddings de alta qualidade**
- **Persistência vetorial no Qdrant**
- **Pronto para construir um RAG corporativo (Brann / Leaf / Wave)**

---

## ✔️ QUER A VERSÃO EXPORT (JSON) DO N8N PRONTA?

Posso gerar:

- 📄 Pipeline de Ingestão Manual
- 📄 Pipeline de Ingestão Automática via URL
- 📄 Pipeline de Ingestão em Massa via Drive
- 📄 Pipeline Leaf RAG (consulta + rerank + cite sources)

Só escolher qual.

Quer que eu gere **o JSON pronto para import** no seu n8n?

Perfeito. Aqui vão os **2 workflows em JSON para importar direto no n8n**:

- Ingestão em massa via Google Drive → Qdrant
- RAG de consulta (pergunta → busca vetorial → resposta da IA)

Use como **base** e só ajusta credenciais/IDs de pasta/coleção.

---

## 0\. Variáveis de ambiente (n8n → Settings → Environment variables)

Crie estas 4 env vars:

- `OPENAI_API_KEY` = sua API key da OpenAI
- `QDRANT_URL` = URL base do cluster Qdrant
	- Ex.: `https://xxxxxxxx.us-east4-0.aws.cloud.qdrant.io`
- `QDRANT_API_KEY` = API key do Qdrant
- `QDRANT_COLLECTION` = nome da coleção (ex.: `ginkgo_docs`)

---

## 1) Workflow — Ingestão em Massa via Drive → Qdrant

Este fluxo:

1. Trigger manual
2. Lista todos os arquivos de uma pasta do Google Drive
3. Faz download de cada arquivo
4. Converte binário → texto (para arquivos de texto / PDFs simples)
5. Corta em chunks
6. Gera embeddings (OpenAI → HTTP)
7. Faz upsert no Qdrant

> No node “Google Drive - List Files” troque `SEU_FOLDER_ID_AQUI` pelo ID da pasta.

```markdown
{
  "name": "Ingestão em Massa via Drive → Qdrant",
  "nodes": [
    {
      "id": "ManualTrigger_1",
      "name": "Manual Trigger",
      "type": "n8n-nodes-base.manualTrigger",
      "typeVersion": 1,
      "position": [250, 300],
      "parameters": {}
    },
    {
      "id": "GDriveList_1",
      "name": "Google Drive - List Files",
      "type": "n8n-nodes-base.googleDrive",
      "typeVersion": 1,
      "position": [500, 300],
      "parameters": {
        "resource": "file",
        "operation": "list",
        "returnAll": true,
        "filters": {
          "q": "'SEU_FOLDER_ID_AQUI' in parents and trashed = false"
        }
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "GOOGLE_DRIVE_CREDENTIAL_ID",
          "name": "Google Drive OAuth2"
        }
      }
    },
    {
      "id": "GDriveDownload_1",
      "name": "Google Drive - Download File",
      "type": "n8n-nodes-base.googleDrive",
      "typeVersion": 1,
      "position": [750, 300],
      "parameters": {
        "resource": "file",
        "operation": "download",
        "fileId": "={{$json.id}}",
        "binaryPropertyName": "data"
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "GOOGLE_DRIVE_CREDENTIAL_ID",
          "name": "Google Drive OAuth2"
        }
      }
    },
    {
      "id": "BinaryToText_1",
      "name": "Binary → Text",
      "type": "n8n-nodes-base.binaryToText",
      "typeVersion": 1,
      "position": [1000, 300],
      "parameters": {
        "binaryPropertyName": "data",
        "propertyName": "text",
        "encoding": "utf8"
      }
    },
    {
      "id": "FunctionChunks_1",
      "name": "Split in Chunks",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [1250, 300],
      "parameters": {
        "functionCode": "const fullText = $json.text || \"\";\nconst chunkSize = 800; // ~300-500 tokens\nconst chunks = [];\n\nfor (let i = 0; i < fullText.length; i += chunkSize) {\n  const part = fullText.slice(i, i + chunkSize);\n  if (part.trim().length > 0) {\n    chunks.push(part);\n  }\n}\n\nconst fileName = $json.name || $json.fileName || $json.title || \"drive-upload\";\n\nreturn chunks.map((c, idx) => ({\n  json: {\n    chunk: c,\n    index: idx,\n    source: fileName\n  }\n}));"
      }
    },
    {
      "id": "HTTP_Embeddings_1",
      "name": "OpenAI Embeddings",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 1,
      "position": [1500, 300],
      "parameters": {
        "method": "POST",
        "url": "https://api.openai.com/v1/embeddings",
        "authentication": "none",
        "responseFormat": "json",
        "jsonParameters": true,
        "options": {},
        "body": {
          "model": "text-embedding-3-large",
          "input": "={{$json.chunk}}"
        },
        "headerParametersJson": "={\"Authorization\": \"Bearer \" + $env.OPENAI_API_KEY, \"Content-Type\": \"application/json\"}"
      }
    },
    {
      "id": "FunctionMapEmbedding_1",
      "name": "Map Embedding",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [1750, 300],
      "parameters": {
        "functionCode": "const emb = $json.data?.[0]?.embedding || [];\nreturn [{\n  json: {\n    embedding: emb,\n    chunk: $json.chunk,\n    source: $json.source,\n    index: $json.index\n  }\n}];"
      }
    },
    {
      "id": "HTTP_Qdrant_Upsert_1",
      "name": "Qdrant Upsert",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 1,
      "position": [2000, 300],
      "parameters": {
        "method": "POST",
        "url": "={{$env.QDRANT_URL + '/collections/' + $env.QDRANT_COLLECTION + '/points'}}",
        "authentication": "none",
        "responseFormat": "json",
        "jsonParameters": true,
        "options": {},
        "headerParametersJson": "={\"api-key\": $env.QDRANT_API_KEY, \"Content-Type\": \"application/json\"}",
        "body": "={\n  \"points\": [\n    {\n      \"id\": $json.source + '-' + $json.index,\n      \"vector\": $json.embedding,\n      \"payload\": {\n        \"text\": $json.chunk,\n        \"source\": $json.source,\n        \"index\": $json.index\n      }\n    }\n  ]\n}"
      }
    }
  ],
  "connections": {
    "Manual Trigger": {
      "main": [
        [
          {
            "node": "Google Drive - List Files",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Drive - List Files": {
      "main": [
        [
          {
            "node": "Google Drive - Download File",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Drive - Download File": {
      "main": [
        [
          {
            "node": "Binary → Text",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Binary → Text": {
      "main": [
        [
          {
            "node": "Split in Chunks",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Split in Chunks": {
      "main": [
        [
          {
            "node": "OpenAI Embeddings",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Embeddings": {
      "main": [
        [
          {
            "node": "Map Embedding",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Map Embedding": {
      "main": [
        [
          {
            "node": "Qdrant Upsert",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {}
}
```

---

## 2) Workflow — RAG (Pergunta → Qdrant → Resposta IA)

Este fluxo:

1. Recebe pergunta via Webhook
2. Gera embedding da pergunta
3. Faz `search` na collection do Qdrant
4. Concatena os trechos mais similares
5. Manda contexto + pergunta para o modelo de chat
6. Responde pelo próprio Webhook

> URL do webhook você pega depois de ativar o fluxo (node Webhook).

```markdown
{
  "name": "RAG Qdrant → OpenAI",
  "nodes": [
    {
      "id": "Webhook_1",
      "name": "Webhook IN",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300],
      "parameters": {
        "httpMethod": "POST",
        "path": "rag-query",
        "responseMode": "onReceived",
        "options": {},
        "responseData": {
          "responseBody": "={{$json.answer}}"
        }
      }
    },
    {
      "id": "FunctionNormalize_1",
      "name": "Normalize Question",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [500, 300],
      "parameters": {
        "functionCode": "const body = $json || {};\nconst question = body.question || body.q || body.text || \"\";\nreturn [{ json: { question } }];"
      }
    },
    {
      "id": "HTTP_Embedding_Q_1",
      "name": "OpenAI Embedding (Q)",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 1,
      "position": [750, 300],
      "parameters": {
        "method": "POST",
        "url": "https://api.openai.com/v1/embeddings",
        "authentication": "none",
        "responseFormat": "json",
        "jsonParameters": true,
        "options": {},
        "body": {
          "model": "text-embedding-3-large",
          "input": "={{$json.question}}"
        },
        "headerParametersJson": "={\"Authorization\": \"Bearer \" + $env.OPENAI_API_KEY, \"Content-Type\": \"application/json\"}"
      }
    },
    {
      "id": "FunctionExtractVec_1",
      "name": "Extract Vector",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [1000, 300],
      "parameters": {
        "functionCode": "const v = $json.data?.[0]?.embedding || [];\nreturn [{ json: { vector: v, question: $json.question } }];"
      }
    },
    {
      "id": "HTTP_Qdrant_Search_1",
      "name": "Qdrant Search",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 1,
      "position": [1250, 300],
      "parameters": {
        "method": "POST",
        "url": "={{$env.QDRANT_URL + '/collections/' + $env.QDRANT_COLLECTION + '/points/search'}}",
        "authentication": "none",
        "responseFormat": "json",
        "jsonParameters": true,
        "options": {},
        "headerParametersJson": "={\"api-key\": $env.QDRANT_API_KEY, \"Content-Type\": \"application/json\"}",
        "body": "={\n  \"vector\": $json.vector,\n  \"limit\": 5,\n  \"with_payload\": true\n}"
      }
    },
    {
      "id": "FunctionBuildContext_1",
      "name": "Build Context",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [1500, 300],
      "parameters": {
        "functionCode": "const question = $json.question;\nconst results = $json.result || $json || {};\nconst points = results || [];\n\nlet context = \"\";\n(points.length ? points : (results.points || [])).forEach((p, i) => {\n  const payload = p.payload || {};\n  const text = payload.text || \"\";\n  context += \`\\n[${i+1}] ${text}\`;\n});\n\nreturn [{\n  json: {\n    question,\n    context\n  }\n}];"
      }
    },
    {
      "id": "HTTP_OpenAI_Chat_1",
      "name": "OpenAI Chat (Answer)",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 1,
      "position": [1750, 300],
      "parameters": {
        "method": "POST",
        "url": "https://api.openai.com/v1/chat/completions",
        "authentication": "none",
        "responseFormat": "json",
        "jsonParameters": true,
        "options": {},
        "headerParametersJson": "={\"Authorization\": \"Bearer \" + $env.OPENAI_API_KEY, \"Content-Type\": \"application/json\"}",
        "body": "={\n  \"model\": \"gpt-4.1-mini\",\n  \"messages\": [\n    {\n      \"role\": \"system\",\n      \"content\": \"Você é um assistente especializado em responder com base estrita no contexto de documentos fornecido. Se a resposta não estiver clara no contexto, diga explicitamente que não há informação suficiente nos documentos. Responda de forma objetiva em PT-BR.\"\n    },\n    {\n      \"role\": \"user\",\n      \"content\": \"Contexto:\\n\" + $json.context + \"\\n\\nPergunta: \" + $json.question\n    }\n  ]\n}"
      }
    },
    {
      "id": "FunctionExtractAnswer_1",
      "name": "Extract Answer",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [2000, 300],
      "parameters": {
        "functionCode": "const choice = $json.choices?.[0]?.message?.content || \"Não consegui gerar uma resposta.\";\nreturn [{ json: { answer: choice } }];"
      }
    }
  ],
  "connections": {
    "Webhook IN": {
      "main": [
        [
          {
            "node": "Normalize Question",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalize Question": {
      "main": [
        [
          {
            "node": "OpenAI Embedding (Q)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Embedding (Q)": {
      "main": [
        [
          {
            "node": "Extract Vector",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Vector": {
      "main": [
        [
          {
            "node": "Qdrant Search",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Qdrant Search": {
      "main": [
        [
          {
            "node": "Build Context",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Build Context": {
      "main": [
        [
          {
            "node": "OpenAI Chat (Answer)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat (Answer)": {
      "main": [
        [
          {
            "node": "Extract Answer",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {}
}
```

---

Se quiser, no próximo passo posso:

- Adaptar o RAG para entrar direto no fluxo do **BRANN** (usando o formato de `out.type` que você já definiu).
- Ou montar um terceiro workflow só de “Ingestão por Upload Manual” para o painel interno da Ginkgo.