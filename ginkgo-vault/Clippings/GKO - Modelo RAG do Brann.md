---
title: "GKO - Modelo RAG do Brann"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/68f81827-b358-832c-94f0-a535191331b7"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
ter., 21 de out. às 20:32

Curto e direto: teu desenho está no caminho certo. Gostei da separação por domínios (MESSAGE / TASK / STATUS / KNOWLEDGE), o “hub” único recebendo o webhook e roteando, e a ideia de normalizar mídia→texto antes do BRANN. Isso conversa bem com o esqueleto do teu fluxo geral (EXTRAIR MÍDIA → Switch por mediaType → transcrição/explicação → normalização → BRANN → Evolution) e o contratinho de saída em JSON do BRANN, que já tens descritos.

Visao-geral-do-fluxo

Visao-geral-do-fluxo

Abaixo vai meu diagnóstico + upgrade “v1.1” do RAG do BRANN com instruções copy/cola.

## Diagnóstico (rápido)

1. **Normalização de entrada**: perfeito transformar áudio/vídeo/imagem em `text` antes do BRANN; mantém o agente simples e barato. Mantém!
	Visao-geral-do-fluxo
2. **Memória**: já prevês chavear por `phone/chatId` e sumarizar histórico. Boa prática.
	Visao-geral-do-fluxo
3. **Saída estruturada**: o “Parser Chain” + Switch por `out.type` reduz caos no WhatsApp. Mantém!
	Visao-geral-do-fluxo
	Visao-geral-do-fluxo
4. **Faltas para RAG**:
	- Falta **índice híbrido** (BM25 + vetor) com **re-rank**.
		- Falta **catálogo de coleções** por cliente/produto e **governança de fontes** (hash/etag, versionamento).
		- Falta **guardrail de citação** (responder “somente com base nas fontes recuperadas” + listar fontes).
		- Falta **feedback loop** (thumbs, correção por usuário, aprendizado leve).

## Arquitetura RAG v1.1 (prática, barata e escalável)

Fluxo lógico:

```markdown
msg → (mídia → texto) → intent(mini) → retrieve(híbrido topK) → re-rank → 
contextual-compression → BRANN(system "grounded") → out(JSON) + refs → send → log/feedback
```

## 1) Supabase/Postgres (pgvector + BM25)

**Extensões e schema (SQL – cole e rode no Supabase):**

```markdown
-- Extensões
create extension if not exists vector;
create extension if not exists pg_trgm;
create extension if not exists unaccent;

-- Tabelas base
create table if not exists kb_collections (
  id uuid primary key default gen_random_uuid(),
  slug text unique not null,            -- ex: 'ginkgo-docs', 'cliente-x'
  title text not null,
  created_at timestamptz default now()
);

create table if not exists kb_documents (
  id uuid primary key default gen_random_uuid(),
  collection_id uuid references kb_collections(id) on delete cascade,
  source_url text,                       -- link ou caminho
  path text,                             -- ex: 'docs/contratos/v1.pdf'
  mime text,
  etag text,                             -- hash do arquivo para idempotência
  meta jsonb default '{}'::jsonb,
  created_at timestamptz default now(),
  unique(collection_id, path)
);

-- Chunking + embeddings
-- escolha 1536 para text-embedding-3-small; para -3-large use 3072
create table if not exists kb_chunks (
  id uuid primary key default gen_random_uuid(),
  document_id uuid references kb_documents(id) on delete cascade,
  chunk_idx int not null,
  content text not null,
  tokens int,
  embedding vector(1536),
  meta jsonb default '{}'::jsonb
);

-- Busca full-text (BM25-like) com trigram + unaccent
create index if not exists idx_chunks_content_gin on kb_chunks
  using gin ( ( (unaccent(content)) gin_trgm_ops ) );

create index if not exists idx_chunks_doc on kb_chunks(document_id);
create index if not exists idx_docs_collection on kb_documents(collection_id);
create index if not exists idx_chunks_embedding on kb_chunks using ivfflat (embedding vector_cosine_ops) with (lists = 100);

-- Função de upsert de documento e chunks (RPC)
create or replace function kb_upsert_document(
  p_collection_slug text,
  p_path text,
  p_source_url text,
  p_mime text,
  p_etag text,
  p_chunks text[],
  p_embeddings vector[]
) returns uuid
language plpgsql as $$
declare
  v_collection_id uuid;
  v_document_id uuid;
  i int;
begin
  select id into v_collection_id from kb_collections where slug = p_collection_slug;
  if v_collection_id is null then
    insert into kb_collections(slug, title) values (p_collection_slug, initcap(p_collection_slug))
    returning id into v_collection_id;
  end if;

  -- idempotência por (collection, path) + etag
  select id into v_document_id from kb_documents where collection_id = v_collection_id and path = p_path;
  if v_document_id is null then
    insert into kb_documents(collection_id, source_url, path, mime, etag)
    values (v_collection_id, p_source_url, p_path, p_mime, p_etag)
    returning id into v_document_id;
  else
    update kb_documents set source_url = p_source_url, mime = p_mime, etag = p_etag where id = v_document_id;
    delete from kb_chunks where document_id = v_document_id; -- reprocessa
  end if;

  for i in 1 .. array_length(p_chunks,1) loop
    insert into kb_chunks(document_id, chunk_idx, content, embedding)
    values (v_document_id, i-1, p_chunks[i], p_embeddings[i]);
  end loop;

  return v_document_id;
end$$;

-- Busca híbrida (RPC): retorna topK por BM25 e por vetor
create or replace function kb_search_hybrid(
  p_collection_slugs text[],
  p_query text,
  p_query_embedding vector,
  p_k int default 8,
  p_alpha float default 0.5  -- 0.0=BM25 puro | 1.0=vetor puro
) returns table(
  chunk_id uuid,
  content text,
  score float,
  source_url text,
  path text
)
language sql as $$
  with cte_col as (
    select id from kb_collections where slug = any(p_collection_slugs)
  ),
  bm25 as (
    select c.id as chunk_id, c.content,
           1.0 - (similarity(unaccent(c.content), unaccent(p_query)))::float as score_bm25,
           d.source_url, d.path
    from kb_chunks c
    join kb_documents d on d.id = c.document_id
    where d.collection_id in (select id from cte_col)
    order by unaccent(c.content) <-> unaccent(p_query)
    limit p_k
  ),
  vec as (
    select c.id as chunk_id, c.content,
           (1.0 - (c.embedding <=> p_query_embedding))::float as score_vec,
           d.source_url, d.path
    from kb_chunks c
    join kb_documents d on d.id = c.document_id
    where d.collection_id in (select id from cte_col)
    order by c.embedding <=> p_query_embedding
    limit p_k
  ),
  unioned as (
    select b.chunk_id, b.content, b.score_bm25, null::float as score_vec, b.source_url, b.path from bm25 b
    union all
    select v.chunk_id, v.content, null::float, v.score_vec, v.source_url, v.path from vec v
  )
  select chunk_id,
         content,
         coalesce(avg(score_vec),0)*p_alpha + coalesce(avg(score_bm25),0)*(1.0-p_alpha) as score,
         source_url, path
  from unioned
  group by chunk_id, content, source_url, path
  order by score asc
  limit p_k;
$$;
```

> Resultado: coleções por cliente/produto, upsert idempotente, busca híbrida rápida e barata.

## 2) n8n – blocos (copy/cola do que falta)

- **Embeddings**: usa `text-embedding-3-small` (custo/benefício ótimo).
- **Re-rank**: usa um “OpenAI Chat” leve como re-ranker (gpt-4o-mini) com prompt de 1-passo.

**Node “Retriever (HTTP Request → Supabase RPC kb\_search\_hybrid)”**  
Method: POST  
URL: `https://<PROJECT>.supabase.co/rest/v1/rpc/kb_search_hybrid`  
Headers:

```markdown
apikey: {{ $env.SUPABASE_SERVICE_ROLE }}
Authorization: Bearer {{ $env.SUPABASE_SERVICE_ROLE }}
Content-Type: application/json
```

Body (JSON):

```markdown
{
  "p_collection_slugs": ["ginkgo-docs","contratos","faq","planos"],
  "p_query": "={{$json.text}}",
  "p_query_embedding": "={{$json.query_embedding}}",
  "p_k": 8,
  "p_alpha": 0.55
}
```

**Node “Embed Query (Function + OpenAI Embeddings)”**

1. Function: `return [{json:{query:$json.text.slice(0,2000)}}];`
2. OpenAI Embeddings: model `text-embedding-3-small` → salva em `query_embedding`.

**Node “Re-Rank (OpenAI Chat)”**  
Prompt (System):

```markdown
Você recebe uma PERGUNTA e uma LISTA DE TRECHOS (content + path).
Devolva apenas os 5 melhores, em JSON:
{ "top": [ { "content": "...", "path": "..." } ] }
Critério: relevância semântica E utilidade factual. Penalize duplicatas.
```

Input: junta `items` do RPC em lista; o node devolve `top`.

**Node “Context Compressor (Function)”**

```markdown
const top = $json.top || [];
const maxChars = 6000;
let used = 0, out = [];
for (const it of top) {
  if (used + it.content.length + 100 > maxChars) break;
  out.push(\`• Fonte: ${it.path}\n${it.content}\`);
  used += it.content.length + 100;
}
return [{ json: { context: out.join('\n\n'), refs: top.map(t=>t.path) } }];
```

**Antes do BRANN**, faça um `Set`:

- `ctx` = `{{$json.context}}`
- `refs` = `{{$json.refs}}`
- `user_text` = `{{$json.text}}`

E no **BRANN System Prompt**, adicione 3 linhas de “grounding”:

```markdown
RESPONDA SOMENTE com base em CONTEXTO_FORNECIDO.
Se a resposta não estiver nas fontes, diga brevemente que não encontrou e ofereça opções (botões).
Liste as fontes no final: "Fontes: <path1>; <path2>; ...".
```

Mantém o formato de saída em JSON como já definiste; as fontes podem ir concatenadas no `out.text` (para não quebrar teu Parser).

Visao-geral-do-fluxo

Visao-geral-do-fluxo

## 3) Ingestão de documentos (MCP\_KNOWLEDGE)

Teu bloco **AGENT\_KNOWLEDGE** fica responsável por:

- Receber `{collection_slug, path, source_url, mime, file(binary)}`.
- Fazer **chunking** (ex: 800–1200 tokens, overlap 120).
- Gerar embeddings para cada chunk.
- Chamar o **RPC `kb_upsert_document`** (uma vez por documento).

**Chunking (Function – exemplo simples):**

```markdown
const text = $json.text; // vindo de OCR/PDF->txt
const size = 1200, overlap = 120;
let chunks = [];
for (let i=0; i<text.length; i+= (size - overlap)) {
  chunks.push(text.slice(i, i+size));
}
return [{ json: { chunks } }];
```

**Embeddings em lote**: usa “Split In Batches” + “OpenAI Embeddings”; guarda lista `embeddings`.

**RPC upsert (HTTP)**  
Body:

```markdown
{
  "p_collection_slug":"={{$json.collection_slug}}",
  "p_path":"={{$json.path}}",
  "p_source_url":"={{$json.source_url}}",
  "p_mime":"={{$json.mime}}",
  "p_etag":"={{$json.etag}}",
  "p_chunks":"={{$json.chunks}}",
  "p_embeddings":"={{$json.embeddings}}"
}
```

## 4) Guardrails & Telemetria

- **Alçapão de erro de mídia** já está previsto (“não consegui baixar a mídia…”). Excelente – mantenha.
	Visao-geral-do-fluxo
- **Trace**: adicione `traceId`, `latency_ms`, `retrieved_count`, `reranked_count`.
- **Feedback**: capture 👍/👎 do usuário em um endpoint e grave em `kb_feedback (traceId, good:boolean, note,text)`.

## 5) Variáveis.env (complemento)

```markdown
SUPABASE_URL=...
SUPABASE_ANON_KEY=...
SUPABASE_SERVICE_ROLE=...
OPENAI_API_KEY=...

EVOLUTION_BASE_URL=...
EVOLUTION_TOKEN=...
EVOLUTION_INSTANCE=BRANN
```

(As de Evolution já batem com teu documento.)

Visao-geral-do-fluxo

## Checklist de prontidão

- `pgvector` + índices criados; RPCs `kb_upsert_document` e `kb_search_hybrid` funcionando.
- Pipeline de ingestão (PDF/Doc/Imagem→OCR→chunk→embed→upsert) idempotente por `etag`.
- Retriever híbrido + re-rank + compressor conectados antes do BRANN.
- Prompt do BRANN com **grounding** e **fontes** no `out.text`.
- Logs + feedback.
- Testes E2E: texto, imagem, áudio, vídeo, e pergunta “fora do escopo” (deve negar com elegância).
	Visao-geral-do-fluxo
	Visao-geral-do-fluxo

---

Quer ir na jugular? Posso te mandar o **JSON de import** do bloco `AGENT_KNOWLEDGE` (n8n) já com: chunking, embeddings, RPC upsert, e o **retriever+rerank+compressor** plug-and-play para pendurar antes do BRANN.