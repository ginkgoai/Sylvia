---
title: "GKO - Análise de template e ajustes"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/68fce885-f898-832d-84e5-b0b76a38a69c"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sáb., 25 de out. às 12:10

este e o modelo final do template, analise cuidadosamente bloco por bloco e me diz se precisa trocar/adicionar ou remover algum no, depois vamos as configurações, observe bloco verde chega e e passada a mensagem ao bloco azul que transforme qualquer midia texto ou audio em texto levando ao buffer que vizualiza a mensagem para o leitor une tudo em uma só e envia ao agent observe as tools desse agent principalmente as de supabase, duas base vetoriais para acessar os respectitivos documentos e um mcp tool da supabase para realizar ações nas bases de salvar informações de um novo contato ou um novo documento, e envio da mensagem de forma cadenciada para mimetizar uma conversa humana. se estiver okay a contrução dessa forma segue o passo a passo para configurarmos.

sáb., 25 de out. às 13:13

parametros agora?

?

?

audio,

?

proximos

?

CONTINUA

de novo

eu copiei/colei\]

video

Sim. Configure assim:

1. **Obter mídia em base2 (vídeo)**
- Converter Para MP4: **on**
- Saída binária: campo **data**
2. **Analyze video (Gemini)**
- Credential: **Google Gemini(PaLM) api account**
- Resource: **Video**
- Operation: **Analyze Video**
- Model: **models/gemini-2.0-flash**  
	(se não aparecer, use **models/gemini-1.5-flash-latest**)
- Text input:  
	`Resuma o vídeo em 1–2 frases. Extraia ações, objetos, locais e horários, em JSON.`
- Input Type: **Video Bytes (binary)**
- Input Binary Field: **data**
- Simplify Output: **on**
3. **Map4 (raw) → JSON**
```markdown
{
  "text": "{{ $json.text || $json.output || '' }}",
  "mediatype": "video",
  "chatid": "{{ $json.chatid }}",
  "phone": "{{ $json.phone }}",
  "messageid": "{{ $json.messageid }}",
  "traceid": "{{ $json.traceid }}",
  "meta": {{ $json.meta || {} }}
}
```

Observação: se o nó “Analyze video” só aceitar **URL**, troque o passo 1 por um **HTTP Request (GET)** que baixa o binário do WhatsApp para **data**, e mantenha o Input Type como **Video Bytes (binary)**.

Certo. Manda as dúvidas.

Se ajudar, checagens rápidas do fluxo:

- Webhook → Normalize: nomes de campos padronizados (`text`, `mediatype`, `phone`, `chatid`, `messageid`, `traceid`, `url`, `meta`).
- Roteamento: `mediatype` exato (`text|audio|image|video|document|sticker`), fallback ativo.
- Download/Obter base64: campo binário sempre **`data`**; timeout ≥ 60s.
- Limites: áudio ≤ 25 MB (OpenAI), vídeo depende do modelo Gemini; usar conversão MP4 quando precisar.
- Extração docs: PDF/XLS/XLSX apontam para **`data`**; pages join = true; planilha com `Header Row`.
- Map finais: JSON válido, sem vírgula sobrando; `meta` objeto, não string.
- Buffer: idempotência por `messageid` / `traceid`; retries exponenciais; dedupe antes do Agent.
- Agent: tools com chaves via credencial, não em texto; sanitizar outputs.
- Disparo: templates de mensagem e variáveis testadas; numeração com DDI.

Diz o que quer validar primeiro: roteamento, limites de tamanho, campos dos Maps, ou integração dos modelos.

esse e um modelo para adaptarmos do que vai ser o mcp / ingestção rag do brann, precisamos que seja um modelo automatico / semi automatico de ingetar documentos nas tabelas memorys e docs ou cadastrar leads / clientes, tudo o brann faz pela mcp tool, possivel assim? me ajude a vizualizar e projete ajustes

Sim. Dá para deixar 100% operável via MCP, com ingestão RAG e cadastro de leads/clientes semi-automática. Abaixo vai o desenho objetivo.

## Objetivo

Um único “MCP Tool: brann” que executa:

- `ingest {source}`: busca, de-duplica, normaliza, faz OCR/embeddings e grava nas tabelas `memories` e `docs`.
- `register_client {payload}`: cria/atualiza lead/cliente e relaciona documentos.
- `status {job_id}` e `reindex {scope}`: observabilidade e reprocesso.

## Modelo de dados (Supabase)

```markdown
-- Clientes/Leads
create table clients (
  id uuid primary key default gen_random_uuid(),
  external_ref text unique,        -- e.g. phone/email/cnpj
  name text,
  phone text,
  email text,
  stage text,                      -- lead|client|inactive
  meta jsonb default '{}'::jsonb,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

-- Documentos brutos
create table docs (
  id uuid primary key default gen_random_uuid(),
  source text,                     -- drive|whatsapp|upload|url
  uri text,                        -- path/url/id
  sha256 text unique,              -- de-dup global
  filename text,
  mime text,
  size_bytes bigint,
  pages int,
  text_full text,                  -- pós OCR/parse
  meta jsonb default '{}',
  owner_client_id uuid references clients(id),
  created_at timestamptz default now()
);

-- Chunks indexados (RAG)
create table memories (
  id uuid primary key default gen_random_uuid(),
  doc_id uuid references docs(id) on delete cascade,
  chunk_no int,
  chunk text,
  vector vector(3072),             -- conforme modelo
  meta jsonb default '{}',
  created_at timestamptz default now()
);

-- Jobs de ingestão
create table ingest_jobs (
  id uuid primary key default gen_random_uuid(),
  command text,                    -- ingest|reindex|register_client
  args jsonb,
  status text,                     -- queued|running|done|error
  errors jsonb,
  started_at timestamptz,
  finished_at timestamptz
);

create index on memories using ivfflat (vector) with (lists=100);
```

## UX da MCP Tool (contrato)

- `ingest --source=drive --query="folder:brann_rag"`  
	Opcional: `--owner=external_ref`, `--mode=auto|semi`, `--force` (ignorar de-dup).
- `register_client --external_ref=+55999 --name="..." --email="..." --meta='{...}'`
- `status --job=<uuid>` / `reindex --scope=client:<external_ref>|doc:<sha256>|all`

## Pipeline de ingestão (automático/semi)

1. **Discovery**  
	Source adapters: Drive, URL, WhatsApp media, upload. Saída: {uri, filename, mime, size}.
2. **Download seguro**  
	Timeout, range requests, “nonDownloadable” handler.
3. **Hash**  
	`sha256(file)` → dedupe global (`docs.sha256 unique`).
4. **Parse/OCR**
	- PDF: texto+imagens; OCR se necessário.
		- XLS/XLSX: normalização tabular → text/plain com cabeçalhos.
		- Imagem: OCR.
		- Vídeo: transcrição opcional.
5. **Persist Doc**  
	Upsert em `docs` por `sha256`. Vincula `owner_client_id` se informado.
6. **Chunking**  
	Token splitter (tamanho estável, ex. 800 tokens, overlap 120).
7. **Embeddings**  
	Modelo único (ex.: `text-embedding-3-large` ou Gemini Embeddings). Grava em `memories`.
8. **Observabilidade**  
	Grava `ingest_jobs`. Emite progresso para `status`.
9. **Modo semi-auto**  
	Pausa antes de `Persist Doc` para revisão: usuário aprova/edita metadados e dono; então continua.

## Ajustes no seu fluxo (n8n), mapeando o print

1. **“Search files and folders” → “Loop Over Items” → “Download file” → “createHash”**  
	✅ manter. Garanta `sha256` em um campo fixo `hash`.
2. **Switch (mimes)**  
	✅ já existe. Aplique OCR/parse por ramo.  
	Sugestão: encapsular em Subworkflow “ParseAnyDocument”.
3. **Record Manager**  
	Substituir planilha por **Supabase (MCP\_SUPABASE)**:
	- `docs.upsert({ sha256, uri, mime, size, pages, text_full, filename, source, owner_client_id, meta })`
		- retorna `doc_id`.
4. **Token Splitter + Embeddings (OpenAI/Gemini)**  
	Use um nó “Chunker” com saída `{doc_id, chunk_no, chunk, meta}` → “Embedder” → “Insert memories”.
5. **Dois ramos**
	- `GKO_DOCS`: persiste documentos.
		- `GKO_MEMORIES`: persiste chunks.  
		Orquestre por **Merge → continue both** para reduzir latência.
6. **Reprocesso/Idempotência**  
	Antes de processar, faça `select * from docs where sha256=:hash`. Se existe e `--force` falso, **skip** tudo exceto reindex.
7. **Cliente**  
	Adicione nó MCP `register_client` que upserta em `clients` e devolve `client_id`.  
	Passe `owner_client_id` adiante para vincular documentos.
8. **Entrada via Brann**
	- Do WhatsApp: quando vier um PDF/IMG/XLS, dispare `ingest --source=whatsapp --owner=<phone>`.
		- Para cadastro: `register_client` a partir do buffer (nome + telefone extraídos).
9. **Fila/Backpressure**  
	Introduza uma “Queue” simples com Supabase: `ingest_jobs(status='queued')`. Um worker do n8n consome em batches (ex. 3 concorrentes), marca `running/done/error` e atualiza.
10. **Erro/Retry**  
	Retries exponenciais por etapa (download, parse, embeddings). Regra: nunca gravar `memories` sem `doc_id` persistido.

## Limites e modelos

- OCR: PDFs scanneados e imagens > use Tesseract ou Vision API.
- Embeddings: dimensione `vector` conforme o modelo.
- Vídeo: transcrever antes de indexar; chunk por timestamps de frase.
- Privacidade: PII no `text_full` opcionalmente mascarada; guarde original em storage, não no `docs.text_full` se sensível.

## Segurança

- Scopes por credencial no MCP.
- Assinaturas temporárias para download (URL curta).
- Auditoria: who/when no `ingest_jobs` e `clients.updated_at`.

## Visual (como ficará)

- À esquerda: **Triggers** (schedule, webhook do Brann, manual MCP).
- Núcleo: **Discovery → Download → Hash → Parse/OCR → Upsert docs → Chunk → Embed → Upsert memories**.
- À direita: **Status/Logs** e **Ações MCP** (`status`, `reindex`, `register_client`).

## Prontos para montar

- Te passo os **schemas** acima, os **comandos MCP** e os **blocos n8n**:
	- Subworkflow `ParseAnyDocument`
		- Subworkflow `ChunkAndEmbed(doc_id, text_full, meta)`
		- Nodes Supabase: `upsert_docs`, `insert_memories_batch`, `upsert_client`, `jobs_update`.

Diz onde quer começar: comandos MCP, schemas no Supabase ou os subflows no n8n.