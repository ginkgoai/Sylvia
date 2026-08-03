---
title: "GKO - Configurando fluxo n8n"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/68c9e821-b1f8-832a-817f-a9b8a32a1062"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
ter., 16 de set. às 19:44

Base De Conhecimento Do Brann (google Drive → Supabase Rag)

## Base de Conhecimento do Brann (Google Drive → Supabase RAG)

> Objetivo: transformar suas pastas do **Google Drive** em uma **base de conhecimento consultável** pelo Brann, com **README por pasta**, indexação de conteúdo (PDF/Docs), **chunking**, **embeddings** em **Supabase (Postgres + pgvector)** e **busca híbrida** (vetorial + keyword).

---

## Visão Geral (3 camadas)

1. **Fonte**: Google Drive (pastas curadas). Cada pasta tem um **README.md** curto (sumário) + PDFs/Docs.
2. **Indexação** (n8n): job que lê mudanças nas pastas, extrai texto, corta em chunks, gera embeddings e grava no Supabase.
3. **Consulta** (Brann): a cada pergunta, **lê primeiro os READMEs relevantes**, depois busca chunks, cita fontes e responde.

---

## Estrutura de Pastas (Drive)

- `GINKGO/INSTITUCIONAL/README.md`
- `GINKGO/COMERCIAIS/README.md`
- `GINKGO/PRODUTOS/README.md`
- `GINKGO/PLAYBOOKS/README.md`
- `GINKGO/CLIENTES/README.md`
- `GINKGO/FAQ/README.md`

**Modelo de README.md (copiar/colar)**

\# README – \<NOME DA PASTA>

\*\*Propósito\*\*: (1–3 linhas do que está aqui)

\*\*Quando usar\*\*: (situações típicas)

\*\*Top 5 tópicos\*\*: bullets curtas

\*\*Docs críticos\*\*: \[Nome do doc A\] (resumo 1 linha), \[Nome do doc B\]...

\*\*Palavras‑chave\*\*: lista curta separada por vírgula

> Dica: mantenha **curto e pragmático**. O README vira o *resumo enxuto do conhecimento total daquela pasta*.

---

## Supabase – Banco (Postgres + pgvector)

### 1) Extensão pgvector

create extension if not exists vector;

### 2) Tabelas

\-- fontes/pastas do Drive

create table if not exists kb\_sources (

id uuid primary key default gen\_random\_uuid(),

drive\_folder\_id text not null,

drive\_folder\_path text not null,

title text,

created\_at timestamptz default now(),

updated\_at timestamptz default now()

);

\-- documentos

create table if not exists kb\_documents (

id uuid primary key default gen\_random\_uuid(),

source\_id uuid references kb\_sources(id) on delete cascade,

drive\_file\_id text not null,

drive\_name text not null,

mime\_type text,

path text,

sha256 text, -- para deduplicação

is\_readme boolean default false,

word\_count int,

updated\_at\_gdrive timestamptz,

created\_at timestamptz default now(),

updated\_at timestamptz default now()

);

\-- chunks

create table if not exists kb\_chunks (

id uuid primary key default gen\_random\_uuid(),

document\_id uuid references kb\_documents(id) on delete cascade,

chunk\_index int not null,

content text not null,

embedding vector(3072), -- text-embedding-3-large (ajuste se usar outro)

created\_at timestamptz default now()

);

### 3) Policies (Row Level Security)

alter table kb\_sources enable row level security;

alter table kb\_documents enable row level security;

alter table kb\_chunks enable row level security;

create policy "read\_kb" on kb\_sources for select using (true);

create policy "read\_kb\_docs" on kb\_documents for select using (true);

create policy "read\_kb\_chunks" on kb\_chunks for select using (true);

> Ajuste policies conforme o seu auth. Em produção, restrinja por usuário/role (JWT claims).

---

## n8n – Fluxo de Indexação (Drive → Supabase)

**Nós principais**

1. **HTTP Trigger / Cron**: rodar manual ou de hora em hora.
2. **Google Drive – List Files in Folder**: para cada pasta (source). Use `includeTrashed=false`.
3. **Google Drive – Download File**: baixar conteúdo.
4. **Extratores**:
	- PDF → **PDF Extract** (ou node/func custom com `pdf-parse`).
		- Google Docs → **Google Docs – Get Document Content**.
		- Markdown/README → já é texto.
5. **Normalize Text (Function)**: remove quebras, espaços duplos.
6. **Chunking (Function)**: quebra em ~ **800–1200 tokens** com sobreposição ~ **120 tokens**.
7. **Hash (Function)**: `sha256` do texto para dedup.
8. **OpenAI – Embeddings**: `text-embedding-3-large`.
9. **Supabase – Upsert**:
	- `kb_sources` (se necessário)
		- `kb_documents` (marca `is_readme` quando `drive_name` = `README.md`)
		- `kb_chunks` (conteúdo + embedding)

**Snippet – Chunking (Function node)**

const maxTokens = 1000; // aprox. 800–1200 tokens

const overlap = 120;

function splitText(txt, size, over) {

const words = txt.split(/\\s+/);

const chunks = \[\];

for (let i = 0; i < words.length; i += (size - over)) {

const part = words.slice(i, i + size).join(' ');

if (part.trim().length) chunks.push(part);

}

return chunks;

}

return items.map((item, idx) => {

const text = item.json.text || '';

const approxTokens = Math.ceil(text.length / 4);

const sizeInWords = Math.floor((maxTokens \* 1.1));

const overlapWords = Math.floor((overlap \* 1.1));

const chunks = splitText(text, sizeInWords, overlapWords);

return {

json: {

...item.json,

chunks

}

};

});

**Snippet – Upsert Chunks via HTTP (Supabase Edge Function)**

{

"method": "POST",

"url": "https://\<project>.supabase.co/functions/v1/kb-upsert",

"headers": {"Authorization": "Bearer {{SUPABASE\_SERVICE\_ROLE}}", "Content-Type": "application/json"},

"body": {

"source": {"drive\_folder\_id": "{{FOLDER\_ID}}", "drive\_folder\_path": "{{FOLDER\_PATH}}"},

"document": {

"drive\_file\_id": "={{$json\[\\"fileId\\"\]}}",

"drive\_name": "={{$json\[\\"name\\"\]}}",

"mime\_type": "={{$json\[\\"mimeType\\"\]}}",

"path": "={{$json\[\\"path\\"\]}}",

"sha256": "={{$json\[\\"sha256\\"\]}}",

"is\_readme": "={{$json\[\\"name\\"\] === 'README.md'}}",

"updated\_at\_gdrive": "={{$json\[\\"modifiedTime\\"\]}}",

"word\_count": "={{$json\[\\"wordCount\\"\]}}"

},

"chunks": "={{$json\[\\"chunks\\"\]}}",

"embeddings": "={{$json\[\\"embeddings\\"\]}}"

}

}

> Você pode pular a Edge Function e gravar direto com **Postgres node** (INSERT/UPSERT) se preferir.

---

## Supabase – Edge Function (opcional, referência)

Pseudocódigo (Deno):

// Recebe {source, document, chunks\[\], embeddings\[\]} e faz upsert transacional

// 1) upsert kb\_sources (by drive\_folder\_id)

// 2) upsert kb\_documents (by drive\_file\_id + sha256)

// 3) delete + insert kb\_chunks (se hash mudou)

---

## Consulta (Brann → Supabase)

### Passo 1 – Buscar READMEs relevantes

- Faça **keyword search** por termos da pergunta nas `kb_documents.is_readme = true` e também vetorial (chunk dos READMEs).
- Retorne trechos curtos dos READMEs primeiro.

### Passo 2 – Busca Híbrida nos Chunks

- Gere embedding da pergunta.
- SQL exemplo (cosine):

with q as (

select cast($1 as vector(3072)) as query

)

select c.id, c.content, d.drive\_name, d.path, d.drive\_file\_id,

1 - (c.embedding <=> q.query) as score

from kb\_chunks c

join kb\_documents d on d.id = c.document\_id,

q

where d.is\_readme = false

order by c.embedding <=> q.query

limit 8;

- Combine com **ILIKE** para palavras‑chave quando fizer sentido.

### Passo 3 – Montar a Resposta com Citações

- Cite nome do arquivo + caminho.
- Se a resposta conflitar entre fontes, **priorize README** e peça validação humana.

---

## Instruções do Prompt do Brann (resumo operacional)

{

"role": "system",

"content": \[

"Você é o Brann, assistente da Ginkgo. Quando precisar de conhecimento da empresa:",

"1) Leia primeiro os README.md das pastas relevantes (resumo enxuto do conhecimento total daquela pasta).",

"2) Depois consulte a base RAG no Supabase (chunks). Use busca híbrida: keyword + vetorial.",

"3) Sempre cite as fontes (nome do arquivo e caminho).",

"4) Se houver divergência entre documentos, priorize README e sinalize a incerteza.",

"5) Seja sucinto, prático e orientado a ação."

\]

}

---

## Boas Práticas

- **Curadoria**: menos é mais. Só suba o que vale ser lembrado.
- **Nomes claros**: `YYYY‑MM‑DD – Título curto – v1.pdf`.
- **Atualização**: job horário + job manual (botão no n8n) para reindexar uma pasta.
- **Observabilidade**: log por documento com status (ok, atualizado, erro, ignorado).
- **Segurança**: use **Service Role** só no backend; no Brann (cliente), use **anon key** com RLS restrito.

---

## Roteiro de Implementação (checklist)

1. Criar READMEs em todas as pastas‑chave no Drive.
2. Criar projeto Supabase, habilitar `vector`, criar tabelas e RLS.
3. No n8n: montar fluxo **Indexação** (Drive → Extract → Normalize → Chunk → Embed → Upsert).
4. Testar com 1 pasta e 2 arquivos (um README + um PDF).
5. Montar fluxo **Consulta** (Embed pergunta → SQL similarity → retorno de trechos + fontes).
6. Ajustar o **prompt do Brann** para seguir o protocolo README‑primeiro.
7. Colocar cron e monitoramento (erro → alerta no WhatsApp/Discord).