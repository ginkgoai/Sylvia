---
title: "GKO - Conexão Supabase no n8n"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/6929f176-18c4-8333-beaa-10ec3b6637f8"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sex., 28 de nov. às 16:01

![1b0ff297-b2ad-47ed-8ae9-fe643524bde2.png](https://chatgpt.com/backend-api/estuary/content?id=file_0000000055ec71f5906fd29afd956b92&ts=495692&p=fs&cid=1&sig=69f24ecda7d0625269ea7a821bfc3fb85b1f606d59fa57d42b8fce66be421138&v=0)

?

sex., 28 de nov. às 17:35

![64d78a86-c311-400a-aea0-8baee1b65d05.png](https://chatgpt.com/backend-api/estuary/content?id=file_000000006a5471f58ec4ef64125c4762&ts=495692&p=fs&cid=1&sig=1a8d13492f7ae4e7132571150fa9790a4d5e55120fa5d39f0bdc7b1553f17d13&v=0) ![3fff3c09-d095-4b3c-871e-c3e1fbb5d997.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000962871f5ab6a0d5b456ecc33&ts=495692&p=fs&cid=1&sig=2078bb25ef6bb3ba84dfeb716abd14f3b517fcd6ee893972d472d89539cc2ee0&v=0) ![c4c65c96-3dcd-4369-a9f7-3ed7316bae49.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000c48071f5b13ef7bb26f056a9&ts=495692&p=fs&cid=1&sig=0527193e7d49f8d5382a186ae9866c3cbb0f3d1f305c408b3af79061b6d832fa&v=0)

confere

![60d7af24-8465-463e-90c1-c1ebc79a3cc7.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000ba5471f596858c49a6565297&ts=495692&p=fs&cid=1&sig=1a97ac3679cb1519bbbd25557b31158f88db8a65913d88fdb2f8ab5ef6f6dfea&v=0) ![51d74c41-0e81-42c3-b56b-45a651b8444b.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000242471f5978ea2b0b2a2a97c&ts=495692&p=fs&cid=1&sig=4917a8c52e318315933289381b91cb09434b3d25b46235bf45904c46436f1913&v=0) ![f4f03067-87ee-4a5f-8eb1-c3de7099bbb8.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000a4a871f5929beecc584c70c6&ts=495692&p=fs&cid=1&sig=822623237c2305e2b9ac1fa46680a49a2e0756c8e59b4ec27a33d4ceed80d562&v=0)

sáb., 29 de nov. às 14:40

Sim — **copiarmos esse fluxo como base é não só uma boa ideia, é a jogada mais inteligente possível** para montar o teu “bibliotecário” da Ginkgo.  
Esse blueprint que você mostrou é exatamente o *esqueleto universal* de um pipeline de ingestão de conhecimento profissional — o mesmo padrão usado por empresas de IA sérias quando querem:

- ler documentos enviados por clientes,
- extrair conhecimento,
- transformar em partes pequenas,
- gerar embeddings,
- e salvar num vetorstore + tabela de metadados.

E o melhor: **ele casa 100% com a tua arquitetura Ginkgo (Supabase + Together/Embeddings + n8n + RAG do Brann/Alphie)**.

Vou te dar agora uma análise rápida (estratégica) + uma versão Ginkgo otimizada (arquitetura final) + passos exatos para copiar/adaptar tudo dentro da tua infra.

---

## ✔️ VISÃO ESTRATÉGICA

Esse fluxo é perfeito porque divide tudo em **Fases Claras**, igual um “bibliotecário digital”:

1. **Entrada bruta** (PDF via Jotform / WhatsApp / Upload)
2. **Extração textual**
3. **Quebra em chunks inteligentes**
4. **Geração de embeddings**
5. **Armazenamento no vetorstore (Supabase Vector)**
6. **Registro de metadados**
7. **Disponibilização para o Agente Brann/Alphie consultar**

É exatamente como a OpenAI, Anthropic e a própria Supabase recomendam para pipelines de Knowledge Ingestion em produção.

---

## ✔️ POR QUE FUNCIONA TÃO BEM NA GINKGO

Porque:

- O Brann consulta o vetorstore o tempo inteiro.
- A Alphie opera dados e documentos da empresa.
- A Manus orquestra fluxos de automação.
- E esse pipeline alimenta os três com *conhecimento vivo*.

Ou seja: **a biblioteca cresce sozinha conforme clientes e documentos chegam.**

---

## ✔️ O QUE EU ADAPTARIA PARA O PADRÃO GINKGO

Aqui está a versão refinada e compatível com tua arquitetura:

## 🔹 Fase 1: Entrada de Documento

**Origem flexível** (qualquer uma):

- JotForm
- WhatsApp (via Evolution API)
- Upload no site Leaf/Pyre/Haven
- Google Drive da Ginkgo
- E-mail dedicado

O trigger apenas salva o binário → envia para o n8n.

---

## 🔹 Fase 2: Extração & Normalização

Usar:

- **pdf-text-extract** (no n8n)
- fallback: GPT-4o-mini Vision (se PDF não tiver texto)

Depois:

- remover cabeçalhos repetidos
- limpar quebras duplicadas
- padronizar espaço e encoding

---

## 🔹 Fase 3: Chunking Inteligente

O pipeline original divide em partes fixas.

Eu recomendo:

- **recursive character splitter** estilo LangChain
- tamanho: **800 tokens**
- overlap: **150 tokens**

Isso faz o Brann responder muito mais corretamente nas buscas.

---

## 🔹 Fase 4: Embeddings

Você pode usar:

### Opção barata (recomendada)

**Together AI – embeddings**  
→ custo muito baixo e qualidade excelente.

### Opção premium

**OpenAI text-embedding-3-large**

### Opção open-source + barata

**Qdrant + jina v2 embeddings**  
(se quiser full self-hosted futuramente)

---

## 🔹 Fase 5: Armazenamento

Supabase (cloud) usando:

- tabela `kb_chunks`
- coluna `content`
- coluna `metadata` (JSONB)
- coluna `embedding` (vector)

**RLS ativado** (mas permissões especiais para Alphie)

---

## 🔹 Fase 6: Registro do Documento

Criar tabela extra:

```markdown
CREATE TABLE documents (
  id uuid primary key default gen_random_uuid(),
  file_name text,
  file_url text,
  uploaded_by text,
  uploaded_at timestamptz default now(),
  tags text[]
);
```

Alphie consegue listar/abrir documentos específicos e inferir contexto.

---

## 🔹 Fase 7: Expor ao Brann (RAG)

O Brann usa uma ferramenta de:

```markdown
query_document(question)
```

Que:

1. Busca embeddings mais próximos
2. Combina contexto
3. Responde com precisão alta
4. Armazena histórico por telefone/session ID

Tudo seamless.

---

## ✔️ A PERGUNTA: “Copiamos esse fluxo?”

Resposta:

**Sim, 100%. E eu adapto contigo para virar o “Pipeline Oficial de Conhecimento da Ginkgo AI Systems”.**

Esse fluxo é:

- claro
- modular
- escalável
- fácil de manter
- fácil de expandir para clientes
- muito poderoso para automação inteligente

E depois que funcionar na Ginkgo, vira um **produto**:

> “Ginkgo Knowledge Engine – leitura automática de documentos, contratos e arquivos enviados pelo WhatsApp, com armazenamento inteligente e busca semântica.”

---

## ✔️ SE QUISER, EU FAÇO AGORA A VERSÃO N8N JSON PRONTA

Posso gerar:

- o JSON COMPLETO importável para n8n
- já com:
	- nodes de upload
		- extração
		- chunking
		- embeddings
		- supabase
		- fallback vision
		- normalização
		- comentários
		- logs
		- mecanismos anti-erro

E ainda:

- a versão 2.0 com atualizações da Alphie
- integração com Evolution (para uploads via WhatsApp)

---

## ✔️ O QUE VOCÊ PREFERE?

Escolha:

**1.** Quero **o fluxo n8n pronto** para importar  
**2.** Quero **o fluxograma detalhado com cada nó**  
**3.** Quero **ambos (ideal)**

Assim montamos o "Cérebro de Documentos" da Ginkgo hoje mesmo.

Perfeito. Vamos transformar esse bloco de baixo (JotForm → Embeddings → Supabase) no **“Bibliotecário Oficial da Ginkgo”** e deixar plugável no GAULA.

Vou separar em:

1. Organização geral do workflow
2. Variáveis de ambiente
3. Configuração nó a nó do fluxo de ingestão (JotForm → Supabase)
4. Como o Brann/GAULA vai consumir isso depois

Baseio a linha em cima daquele fluxograma PDF de ingestão/embeddings que você mostrou.

Visao-geral-do-fluxo

---

## 1) Organização geral no n8n

- Mantém a parte de cima como está: **GAULA** (atendimento + mídia).
- Cria uma faixa visual embaixo chamada **BIBLIOTECÁRIO** (cor diferente):
	- `JotForm Trigger`
		- `Grab New knowledgebase`
		- `Grab the uploaded knowledgebase file`
		- `Extract Text from PDF`
		- `Splitting into Chunks`
		- `Embedding uploaded`
		- `Save the embeddings in DB`

Esse fluxo é **independente** do GAULA: ele só alimenta a base. Depois, GAULA/Brann usam essa base no RAG.

---

## 2) Variáveis de ambiente (n8n → Settings → Environment variables)

No `docker-compose` / `.env` do n8n (ou nas env vars da UI), cria:

```markdown
SUPABASE_URL=https://xajksfzrxnhgpkaxagckgn.supabase.co
SUPABASE_REST_URL=https://xajksfzrxnhgpkaxagckgn.supabase.co/rest/v1
SUPABASE_SERVICE_KEY=sb_secret_...

EMBEDDING_API_URL=https://api.together.xyz/v1/embeddings   # exemplo
EMBEDDING_API_KEY=XXXX
EMBEDDING_MODEL=togethercomputer/m2-bert-80M-8k-retrieval  # ou o que você for usar
```

(Se já estiver usando OpenAI, troca esses três por `OPENAI_API_KEY` / `OPENAI_EMBEDDING_MODEL`.)

---

## 3) Configuração nó a nó – BIBLIOTECÁRIO

### 3.1. JotForm Trigger

Se estiver usando Webhook:

- Node: **Webhook**
- HTTP Method: `POST`
- URL: gera a URL e cola no JotForm como webhook
- Response Mode: `On Received`
- Response Body: algo simples tipo `{ "ok": true }`

O formulário do JotForm deve enviar:

- `pdf_url` (link do PDF)
- `title` (opcional)
- `tags` (opcional)

Se o JotForm já tem integração nativa no n8n, pode usar o node **JotForm Trigger**, mas a lógica de saída é a mesma.

---

### 3.2. Grab New knowledgebase (registrar documento)

Node: **HTTP Request**

- Method: `POST`
- URL:
	```markdown
	{{$env.SUPABASE_REST_URL}}/documents
	```
- Authentication: **None**
- Headers:
	- `apikey` → `{{$env.SUPABASE_SERVICE_KEY}}`
		- `Authorization` → `Bearer {{$env.SUPABASE_SERVICE_KEY}}`
		- `Content-Type` → `application/json`
- Body Content Type: `JSON`
- JSON Body:
	```markdown
	{
	  "file_name": "={{$json.title || 'Contrato sem título'}}",
	  "file_url": "={{$json.pdf_url}}",
	  "uploaded_by": "={{$json.email || 'desconhecido'}}",
	  "tags": "={{$json.tags ? $json.tags.split(',') : []}}"
	}
	```
- Response Format: `JSON`
- Resultado: Supabase cria uma linha em `documents` e devolve `id`.  
	Você usa esse `id` adiante para vincular os chunks.

---

### 3.3. Grab the uploaded knowledgebase file (baixar PDF)

Node: **HTTP Request**

- Method: `GET`
- URL:
	```markdown
	{{$json["pdf_url"]}}
	```
- Authentication: `None`
- Response Format: `File`
- Binary Property: `data`
- Ignore Response Code: `false`

Esse node entrega o PDF em binário na propriedade `data`.

---

### 3.4. Extract Text from PDF

Se estiver usando node nativo:

Node: **Extract from PDF**

- Binary Property: `data`
- Options:
	- `Split Pages` → `false` (você mesmo vai chunkar)
- Output:
	- Campo padrão: `text` (ou `data.text`, dependendo do node — confira na aba JSON após um teste)

Se não tiver node nativo, você pode usar:

- `PDF Extract` comunitário, ou
- chamar um serviço externo (tipo `pdftotext` em API, ou mesmo OpenAI Vision como fallback).

Para este fluxo, vou assumir que sai um campo `text` plano.

---

### 3.5. Splitting into Chunks (Function node)

Node: **Function**

Código:

```markdown
const fullText = items[0].json.text || "";
const docId = items[0].json.id || items[0].json.document_id; // puxa do Supabase se tiver

const maxChars = 2500;   // ~800 tokens
const overlap = 400;

const chunks = [];
let start = 0;

while (start < fullText.length) {
  const end = Math.min(start + maxChars, fullText.length);
  const slice = fullText.slice(start, end);

  chunks.push({
    json: {
      document_id: docId,
      chunk_text: slice,
      chunk_index: chunks.length
    }
  });

  if (end === fullText.length) break;
  start = end - overlap;
}

return chunks;
```

Agora o fluxo vira “multi-item”: um item por chunk.

---

### 3.6. Embedding uploaded (chamar API de embeddings)

Node: **HTTP Request**

- Method: `POST`
- URL:
	```markdown
	{{$env.EMBEDDING_API_URL}}
	```
- Authentication: `None`
- Headers:
	- `Authorization` → `Bearer {{$env.EMBEDDING_API_KEY}}`
		- `Content-Type` → `application/json`
- Body Content Type: `JSON`
- JSON Body (Together como exemplo):
	```markdown
	{
	  "model": "{{$env.EMBEDDING_MODEL}}",
	  "input": "={{$json.chunk_text}}"
	}
	```
- Response Format: `JSON`

Adicione depois um **Set** (ou já use a própria saída) para normalizar:

Node: **Set** (opcional)

- Keep Only Set: `true`
- Campos:
	- `document_id` → `={{$json.document_id}}`
		- `chunk_index` → `={{$json.chunk_index}}`
		- `content` → `={{$json.chunk_text}}`
		- `embedding` → `={{$json.data[0].embedding}}`  
		(ajuste o path conforme a resposta real da API)

---

### 3.7. Save the embeddings in DB (Supabase – kb\_chunks)

Se quiser inserir chunk a chunk:

Node: **HTTP Request**

- Method: `POST`
- URL:
	```markdown
	{{$env.SUPABASE_REST_URL}}/kb_chunks
	```
- Authentication: `None`
- Headers:
	- `apikey` → `{{$env.SUPABASE_SERVICE_KEY}}`
		- `Authorization` → `Bearer {{$env.SUPABASE_SERVICE_KEY}}`
		- `Content-Type` → `application/json`
- Body Content Type: `JSON`
- JSON Body:
	```markdown
	{
	  "document_id": "={{$json.document_id}}",
	  "chunk_index": "={{$json.chunk_index}}",
	  "content": "={{$json.content}}",
	  "embedding": "={{$json.embedding}}"
	}
	```
- Response: `JSON`

Se quiser otimizar, pode antes juntar todos os items em um array e fazer um `POST` único com `[{...}, {...}]`.

---

## 4) Integração com GAULA / Brann

Com a base pronta (`documents` + `kb_chunks`), o Brann passa a ter uma **ferramenta RAG**:

- Ferramenta `search_kb(question)` que:
	1. Gera embedding da pergunta
		2. Faz `POST` em uma função RPC do Supabase (ex.: `match_kb`) que faz a busca de vetores
		3. Retorna top N trechos (`content`) + metadados
		4. Você injeta isso no prompt do Brann (como contexto) antes da resposta final

Esse pedaço a gente pluga depois no bloco verde do GAULA (onde entra o modelo OpenAI).

---

Se quiser, no próximo passo eu te entrego:

- o **SQL completo** das tabelas `documents` e `kb_chunks` com a coluna vector,
- - um exemplo de **RPC `match_kb`** no Supabase,
- - a ferramenta RAG pro Brann (prompt + nó HTTP no GAULA).

Assim você fecha o ciclo:  
**qualquer documento que subir via JotForm entra nessa biblioteca e já vira “memória de conhecimento” para os agentes.**

A arquitetura geral está **certa**, mas do jeito que está dá pra te dizer:

- O fluxo faz sentido.
- Faltam só **alguns ajustes finos de I/O** e uma limpeza de nós herdados do exemplo original.

Vou te organizar isso como checklist rápido, nó a nó, pra você apenas conferir.

---

## 1\. Encadeamento geral

Sequência está correta:

`Download Document → Grab New knowledgebase → Grab the uploaded knowledgebase file link → Extract Text from PDF File → Splitting into Chunks → Embedding Uploaded document → Save the embedding in DB → Alfred → Map7`

Mas, para o teu caso (Supabase + RAG próprio), eu recomendo:

- **Opcionalizar / simplificar**:
	- `Grab New knowledgebase`
		- `Grab the uploaded knowledgebase file link`

Esses dois nós vêm do exemplo da Together (knowledgebase deles).  
Na tua arquitetura, o “knowledgebase” é o **Supabase (documents + kb\_chunks)**, então:

### Melhor versão pra Ginkgo:

```markdown
Download Document
  → (HTTP Supabase) Registrar documento em \`documents\` (pega document_id)
  → Extract Text from PDF (usando o binário do Download Document)
  → Splitting into Chunks (gera vários itens com {document_id, chunk_text, chunk_index})
  → Embedding Uploaded document (usa chunk_text, 1 item = 1 embedding)
  → Save the embedding in DB (insere em \`kb_chunks\`)
  → (Opcional) Alfred (avisar Manus que tem documento novo)
```

Se quiser manter JotForm como origem paralela, ótimo, mas a rota que sai do **Download Document** já resolve qualquer documento vindo do WhatsApp.

---

## 2\. Coisas que você precisa conferir AGORA

### ✅ Download Document

- Output binário: propriedade `data`
- JSON: tem pelo menos `fileName` / `mimeType`

### ✅ Extract Text from PDF File

- Binary Property: `data` (vindo do Download Document)
- Saída: campo `text` no `json` (confere na aba JSON depois de um teste)

### ✅ Splitting into Chunks

Function deve:

- Ler: `items[0].json.text`
- Ter também `document_id` (vindo do Supabase quando você registrar o doc)
- Retornar vários itens:
```markdown
return [{
  json: {
    document_id,
    chunk_text,
    chunk_index
  }
}, ...];
```

### ✅ Embedding Uploaded document

- Chama a API de embeddings **por item**
- Corpo JSON igual a:
```markdown
{
  "model": "{{$env.EMBEDDING_MODEL}}",
  "input": "={{$json.chunk_text}}"
}
```
- Depois faz um **Set** deixando:
```markdown
document_id
chunk_index
content   = chunk_text
embedding = resposta.data[0].embedding
```

### ✅ Save the embedding in DB

- HTTP Request → Supabase REST:
```markdown
{{$env.SUPABASE_REST_URL}}/kb_chunks
```

Body JSON:

```markdown
{
  "document_id": "={{$json.document_id}}",
  "chunk_index": "={{$json.chunk_index}}",
  "content": "={{$json.content}}",
  "embedding": "={{$json.embedding}}"
}
```
- Headers:
	- `apikey` → `{{$env.SUPABASE_SERVICE_KEY}}`
		- `Authorization` → `Bearer {{$env.SUPABASE_SERVICE_KEY}}`
		- `Content-Type` → `application/json`

Rodando com **multi-itens**, cada chunk vira uma linha.

### ✅ Alfred

- Só precisa se você quiser que a Manus receba um evento do tipo:
	- “Documento X foi ingerido, Y chunks criados, tags Z”
- Totalmente opcional para o RAG funcionar.

---

## 3\. Onde está o gargalo real hoje

A lógica do fluxo está ok.  
O problema que você estava vendo (“incorrect host (domain) value”) é **infra de rede/DNS do servidor n8n → Supabase**, não da construção.

Ou seja:

- Se você rodar um HTTP simples `GET https://xajksfzrxnhgpkaxagckgn.supabase.co/rest/v1/` no n8n e falhar com o mesmo erro, é 100% rede.
- Quando essa parte estiver liberada (DNS + porta 443), esse pipeline vai rodar liso.

---

### Resumindo

- **Sim**, a construção está conceitualmente correta.
- Eu só sugiro:
	- remover/ajustar os dois nós herdados do exemplo (ou reconfigurá-los para falar com o Supabase, não com a API da Together),
		- garantir `document_id` propagado e os campos de texto/embedding certinhos.

Se quiser, no próximo passo te mando o **código exato do Function de chunking** + o **SQL das tabelas `documents` e `kb_chunks`** já pronto pra colar na Supabase.