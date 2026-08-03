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

Depois de configurar os nós e a base (a fundação do fluxo no **n8n**), o próximo passo é dar vida a esse esqueleto. É tipo montar um robô: primeiro você encaixa os braços e pernas (os nós), depois precisa ligar os fios, programar o cérebro e ensinar o comportamento. A ordem lógica costuma ser assim:

### 1\. Configuração interna de cada nó

Agora que eles já estão conectados, você abre cada nó e define:

- **Triggers**: o que dispara o fluxo (mensagem recebida no WhatsApp, formulário preenchido, evento de calendário etc.).
- **Credenciais**: tokens, chaves de API e permissões necessárias para os nós conversarem entre si.
- **Parâmetros**: se um nó é de “Enviar Mensagem”, você define texto, variáveis dinâmicas (como {{nome}}) e regras.

### 2\. Fluxo lógico e condições

Aí vem a parte de ensinar o robô a “pensar”:

- Criar **condições (Switch/IF)** para ramificar o atendimento: FAQ, captura de lead, encaminhar para humano.
- Usar **variáveis/set** para armazenar dados como telefone, nome, intenção da mensagem.
- Encadear funções auxiliares (ex.: formatação de texto, cálculos, chamadas externas).

### 3\. Extras opcionais (camadas de inteligência)

- **IA**: plugar GPT/Claude para respostas naturais.
- **Whisper ou STT**: transformar áudio em texto.
- **Banco de dados/Planilha**: salvar leads e conversas.
- **Webhooks/CRMs**: mandar dados pra fora (HubSpot, Pipedrive, Notion etc.).

### 4\. Testes controlados

Com tudo configurado, você roda testes:

- Enviar mensagens de exemplo e ver se seguem o caminho certo.
- Monitorar logs de cada nó pra ajustar erros.
- Usar ambientes de sandbox antes de ir pro cliente real.

### 5\. Deploy e manutenção

- Publicar o fluxo em produção.
- Documentar o que cada nó faz.
- Implementar monitoramento (notificações caso algum nó quebre).
- Atualizar quando surgirem novas necessidades (FAQ, integrações, promoções).

Resumindo: **depois da montagem vem a programação interna, os testes e o refinamento**, até o fluxo estar sólido, automático e confiável.

Quer que eu organize isso em um **checklist prático** (do que fazer na ordem, tipo passo a passo clicável) ou prefere que eu te desenhe um mapa mental de como fica a evolução do fluxo?

Base De Conhecimento Do Brann (google Drive → Supabase Rag)

Baixar

Perfeito, dá pra transformar tuas pastas do Drive em “memória” do Brann sim — já deixei um **guia completo** com SQL, snippets de chunking, esquema do Supabase e o “protocolo README-primeiro” **no canvas ao lado**. Bora implementar em 3 passos práticos:

### Passo A — Preparar o Drive (5 min)

- Em **cada pasta**, crie um `README.md` curtinho (modelo no canvas) dizendo: propósito, quando usar, top 5 tópicos, docs críticos, palavras-chave.
- Nomeie arquivos de forma clara: `2025-09-16 – Pitch Ginkgo – v1.pdf`.

### Passo B — Indexação (n8n → Supabase)

- Fluxo “ **Indexação** ”: Cron/HTTP Trigger → Listar arquivos da(s) pasta(s) → Baixar → Extrair texto (PDF/Docs) → **Normalize** → **Chunk** (~1.000 tokens, overlap ~120) → **Embeddings** (`text-embedding-3-large`) → **Upsert** no Supabase (tabelas e índices no canvas).
- Marque `README.md` com `is_readme=true`.
- Dedup: use `sha256` do conteúdo; só reindexe se o hash mudar.

### Passo C — Consulta (Brann → RAG)

- **Política do Brann**: “Leia primeiro os README.md relevantes; depois busque chunks. Sempre cite o arquivo e caminho.”
- Busca **híbrida**: vetor (cosine) + palavra-chave quando fizer sentido.
- Formate a resposta com **citações** e aviso se houver divergência.

Quer que eu já te entregue o **checklist clicável do n8n** (nós exatos e ordem), ou prefere que eu gere primeiro o **SQL no Supabase** e testemos com uma pasta piloto?

Sim

Showtime. Vou te entregar **os dois**: SQL pronto do Supabase (copy/cola) **e** o **checklist clicável do n8n** com nós, ordem e expressões. A ideia é: tu roda o SQL, testa com **1 pasta piloto** do Drive, e o fluxo já grava tudo no banco.

## 1) Supabase — SQL (copy/cola)

Cria o banco de vetores e as tabelas. Depois ativa RLS básica (abre leitura; em produção a gente restringe por role).

```markdown
-- 1) Vetores
create extension if not exists vector;

-- 2) Tabelas
create table if not exists kb_sources (
  id uuid primary key default gen_random_uuid(),
  drive_folder_id text not null,
  drive_folder_path text not null,
  title text,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

create table if not exists kb_documents (
  id uuid primary key default gen_random_uuid(),
  source_id uuid references kb_sources(id) on delete cascade,
  drive_file_id text not null,
  drive_name text not null,
  mime_type text,
  path text,
  sha256 text,
  is_readme boolean default false,
  word_count int,
  updated_at_gdrive timestamptz,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

create table if not exists kb_chunks (
  id uuid primary key default gen_random_uuid(),
  document_id uuid references kb_documents(id) on delete cascade,
  chunk_index int not null,
  content text not null,
  embedding vector(3072),
  created_at timestamptz default now()
);

create index if not exists idx_kb_docs_source on kb_documents(source_id);
create index if not exists idx_kb_chunks_doc on kb_chunks(document_id);
create index if not exists idx_kb_chunks_embed on kb_chunks using ivfflat (embedding vector_cosine_ops) with (lists = 100);

-- 3) RLS (abrir leitura; ajustar depois)
alter table kb_sources enable row level security;
alter table kb_documents enable row level security;
alter table kb_chunks enable row level security;

create policy "read_all_sources" on kb_sources for select using (true);
create policy "read_all_docs"    on kb_documents for select using (true);
create policy "read_all_chunks"  on kb_chunks    for select using (true);
```

## 2) n8n — Checklist clicável (Drive → Supabase)

> **Variáveis do fluxo (Node: “Set • Vars”)**  
> `DRIVE_FOLDER_ID` (id da pasta-piloto), `DRIVE_FOLDER_PATH` (nome/caminho), `SUPABASE_URL`, `SUPABASE_KEY_SERVICE` (service role), `OPENAI_API_KEY`.

### ORDEM DOS NÓS

1. **HTTP Trigger** (ou Cron)  
	Pra rodar manual ou de hora em hora.
2. **Set • Vars**  
	Campos:
	- `DRIVE_FOLDER_ID`: `"PASTE_O_ID_DA_PASTA"`
		- `DRIVE_FOLDER_PATH`: `"GINKGO/INSTITUCIONAL"`
		- `SUPABASE_URL`: `"https://SEU-PROJ.supabase.co"`
		- `SUPABASE_KEY_SERVICE`: `{{$env.SUPABASE_SERVICE_ROLE}}` (ou cola a key por enquanto)
		- `OPENAI_API_KEY`: `{{$env.OPENAI_API_KEY}}`
3. **Google Drive • List Files in Folder**
	- **Folder ID**: `={{$json["DRIVE_FOLDER_ID"]}}` (via expressão pegando do Set)
		- Include Trashed: `false`
		- Resolve file paths: `true`  
		Saída: lista de arquivos.
4. **IF • Filtrar tipos suportados** (opcional, mas ajuda)  
	Condições (OR):
	- `mimeType` **contains** `pdf`
		- `mimeType` **contains** `document`
		- Nome **equals** `README.md`  
		Ramo *True* segue; *False* descarta.
5. **Google Drive • Download File**
	- File ID: `={{$json["id"]}}`
		- Download: `true`  
		Saída binária: `data`.
6. **Switch • Tipo de extração**
	- Avaliar por `mimeType`:
		- Case1: contém `pdf` → vai pra **PDF Extract**
				- Case2: contém `document` (Google Docs) → vai pra **Google Docs Get**
				- Case3: `name === "README.md"` → vai direto pra **Binary → Text** (se vier como texto) ou mantém como já-texto se não binário.

7a) **PDF Extract** (se PDF)

- Input: `binary.data`
- Output: `text`

7b) **Google Docs • Get Document Content** (se GDoc)

- Document ID: `={{$json["id"]}}`
- Output: texto do doc.

7c) **Move Binary Data** (apenas se README veio binário)

- Binary to JSON → `data` → `propertyName: text`
8. **Function • Normalize Text**  
	Código:
	```markdown
	// Usa item.json.text (ou converte se vier em outra prop)
	const t = (item.json.text || item.json.body || "").toString();
	const text = t
	  .replace(/\r/g, "\n")
	  .replace(/\n{3,}/g, "\n\n")
	  .replace(/[ \t]+/g, " ")
	  .trim();
	item.json.text = text;
	item.json.wordCount = text.split(/\s+/).length;
	return item;
	```
	(Em “Execute Once” = false)
9. **Function • Derivar metadados + hash**
	```markdown
	const crypto = require("crypto");
	const name = $json.name || $json.title || "desconhecido";
	const path = $json.path || $json.filePath || $json.name;
	const sha256 = crypto.createHash("sha256").update($json.text || "").digest("hex");
	const is_readme = name.toLowerCase() === "readme.md";
	return [
	  {
	    json: {
	      drive_file_id: $json.id,
	      drive_name: name,
	      mime_type: $json.mimeType || $json.mime_type,
	      path,
	      sha256,
	      is_readme,
	      wordCount: $json.wordCount || null,
	      modifiedTime: $json.modifiedTime || $json.modified_at || null,
	    }
	  }
	];
	```
10. **Function • Chunking**
```markdown
const text = $json.text || "";
const maxChars = 4000;     // ≈1000 tokens
const overlap = 500;       // ≈120 tokens
const chunks = [];
for (let i = 0; i < text.length; i += (maxChars - overlap)) {
  chunks.push(text.slice(i, i + maxChars));
}
return chunks.map((c, i) => ({ json: { ...$json, chunk_index: i, chunk: c } }));
```
11. **OpenAI • Embeddings**
- **Operation**: Create Embeddings
- **Model**: `text-embedding-3-large`
- **Text**: `={{$json["chunk"]}}`
- **Credentials**: tua OpenAI Key
- Resultado mapeado em `embeddings` (vector).
12. **Postgres • Upsert kb\_documents**
- Credentials: Supabase Postgres
- Query (Use **Query** → **Insert/Update** manual):
```markdown
with src as (
  insert into kb_sources (drive_folder_id, drive_folder_path, title)
  values ({{$json["DRIVE_FOLDER_ID"]}}, {{$json["DRIVE_FOLDER_PATH"]}}, split_part({{$json["DRIVE_FOLDER_PATH"]}}, '/', -1))
  on conflict (drive_folder_id) do update set drive_folder_path = excluded.drive_folder_path
  returning id
), doc as (
  insert into kb_documents (source_id, drive_file_id, drive_name, mime_type, path, sha256, is_readme, word_count, updated_at_gdrive)
  select id, {{$json["drive_file_id"]}}, {{$json["drive_name"]}}, {{$json["mime_type"]}},
         {{$json["path"]}}, {{$json["sha256"]}}, {{$json["is_readme"]}},
         {{$json["wordCount"]}}, {{$json["modifiedTime"]}}::timestamptz
  from src
  on conflict (drive_file_id) do update set
    drive_name = excluded.drive_name,
    mime_type = excluded.mime_type,
    path = excluded.path,
    is_readme = excluded.is_readme,
    word_count = excluded.word_count,
    updated_at_gdrive = excluded.updated_at_gdrive,
    sha256 = excluded.sha256,
    updated_at = now()
  returning id
)
select id as document_id from doc;
```
- **Add Additional Fields**: salva `document_id` no item para o próximo nó.
13. **Postgres • Replace kb\_chunks (apenas se hash mudou)**  
	Estratégia simples: apagar e inserir (em produção dá para otimizar).
- Primeiro **Function • Prepare Insert**:
	```markdown
	// Transforma embedding array → formato Postgres: '[...]'
	const emb = $json.data?.[0]?.embedding || $json.embeddings || [];
	return {
	  json: {
	    document_id: $json.document_id,
	    chunk_index: $json.chunk_index,
	    content: $json.chunk,
	    embedding: '[' + emb.join(',') + ']'
	  }
	};
	```
- **Postgres Query**:
	```markdown
	-- Apagar e inserir num bloco. Se quiser idempotência real, compare sha256 antes.
	delete from kb_chunks where document_id = {{$json["document_id"]}};
	insert into kb_chunks (document_id, chunk_index, content, embedding)
	values ({{$json["document_id"]}}, {{$json["chunk_index"]}}, {{$json["content"]}}, {{$json["embedding"]}}::vector);
	```

> **Dica**: se o “delete” por chunk estiver pesado, faz um nó **Postgres** antes para deletar **uma vez por documento** (usando *Continue On Fail* = true), e depois encadeia os inserts chunk a chunk.

14. **IF • is\_readme → Tag** (opcional)  
	Se `is_readme` = true, manda logar num **Discord/Telegram** ou **Notion** pra confirmar que a pasta tem README.
15. **Respond / Webhook Reply**  
	Retorna um resumo: total de arquivos, total de chunks inseridos, e erros (se tiver).

---

## Teste rápido (piloto)

1. Cria `README.md` na pasta-piloto do Drive (3–8 linhas).
2. Sobe **1 PDF e 1 Google Doc**.
3. Coloca o **Folder ID** no `Set • Vars`.
4. Executa o fluxo.
5. Confere no Supabase → `kb_documents` e `kb_chunks` se entrou direitinho.

## Consulta (no Brann)

Quando o Brann receber pergunta, ele faz:

1. **“README-first”**: busca `is_readme = true` por keyword e/ou embedding (prioriza trechos curtos).
2. Vetorial em `kb_chunks`:
	```markdown
	with q as (select cast($1 as vector(3072)) as v)
	select c.content, d.drive_name, d.path, 1 - (c.embedding <=> q.v) as score
	from kb_chunks c
	join kb_documents d on d.id = c.document_id, q
	where d.is_readme = false
	order by c.embedding <=> q.v
	limit 8;
	```
3. Monta resposta **citando arquivo + caminho**.

---

Quer que eu já gere **um JSON de export do n8n** com esses nós prontos para importar e tu só trocar as credenciais?