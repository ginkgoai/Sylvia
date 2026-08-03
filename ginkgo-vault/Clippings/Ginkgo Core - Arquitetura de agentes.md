---
title: "Ginkgo Core - Arquitetura de agentes"
source: "https://chatgpt.com/g/g-p-68e0a0b393cc8191a0f44ad743e1117d/c/68fb0f81-9eec-8328-a9ee-b104e2e23e5b"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sex., 24 de out. às 2:32

Vamos organizar. O Brann é um atendimento conversacional adaptativo. Nyra um conglomerado de automações de criação e postagem de mídia. E o Alphie um banco de dados vivo com todo conteúdo da empresa.

Definições claras:

- Brann: atendimento conversacional adaptativo em WhatsApp/Web. Vende, qualifica, agenda, lê a base do Alphie e aciona fluxos.
- Nyra: fábrica de conteúdo + publicação. Gera, agenda e posta em múltiplos canais. Aprende com resultados.
- Alphie: “cérebro-dados” vivo. Fonte única de verdade: clientes, interações, ativos, docs, métricas e permissões.

Arquitetura mínima:

- Entradas: Evolution API (WhatsApp), Web chat, Formulários, Webhooks.
- Orquestração: n8n.
- Dados: Postgres + VectorDB (pgvector) + S3 compatível.
- Identidade/segurança: Vault (secrets), JWT por cliente.
- Observabilidade: logs + métricas (PostHog/Grafana).

Contratos entre agentes:

```markdown
// Mensagem -> Brann
{ "type":"user_message","channel":"whatsapp","user_id":"...","text":"...", "media":[{"url":"...", "mime":"..."}] }
// Brann -> Alphie (consulta)
{ "type":"rag_query","tenant_id":"...","query":"politica de troca", "top_k":5 }
// Nyra -> Alphie (brief)
{ "type":"content_brief","goal":"lançar plano Futurista", "constraints":["tons: técnico e direto"] }
// Nyra -> Scheduler (publicação)
{ "type":"schedule_post","network":"instagram","asset_id":"...","when":"2025-10-25T19:00:00Z" }
```

Modelo de dados do Alphie (núcleo):

```markdown
-- clientes/contatos
create table contacts(
  id uuid primary key, tenant_id uuid, name text, phone text unique, email text,
  tags text[], created_at timestamptz default now()
);

-- interações (Brann)
create table interactions(
  id uuid primary key, tenant_id uuid, contact_id uuid references contacts(id),
  channel text, role text check (role in ('user','assistant','tool')),
  content jsonb, created_at timestamptz default now()
);

-- conhecimento (RAG)
create table knowledge_docs(
  id uuid primary key, tenant_id uuid, title text, source text, url text,
  content text, embedding vector(1536), metadata jsonb, updated_at timestamptz default now()
);

-- ativos de mídia (Nyra)
create table media_assets(
  id uuid primary key, tenant_id uuid, kind text, path text, metadata jsonb,
  created_at timestamptz default now()
);

-- posts e agenda
create table posts(
  id uuid primary key, tenant_id uuid, caption text, asset_id uuid references media_assets(id),
  network text, status text check (status in ('draft','scheduled','published','failed')),
  scheduled_at timestamptz, published_at timestamptz, metrics jsonb
);

-- automações
create table automations(
  id uuid primary key, tenant_id uuid, name text, n8n_workflow_id text, status text,
  triggers jsonb, last_run timestamptz
);
```

Papel de cada agente:

- Brann
	- Entrada unificada, triagem, RAG com Alphie, ações: “agendar demo”, “gerar proposta”, “abrir chamado”.
		- Foco: conversão, CSAT, tempo de resposta.
- Nyra
	- Brief→roteiro→geração→QA→agendamento→postagem→análise.
		- Foco: alcance, CTR, conversões assistidas.
- Alphie
	- CRUD de tudo. Indexa e versiona. Expõe APIs para RAG, analytics e governance.

Fluxos n8n essenciais:

- brann\_inbound → detecta intenção → RAG(Alphie) → resposta → ações.
- nyra\_campaign → gera variações → cria assets → schedule → publica → puxa métricas.
- alphie\_ingest → coleta docs/mídia → extrai texto → gera embeddings → upsert.

Variáveis (.env) mínimas:

```markdown
EVOLUTION_API_KEY=
OPENAI_API_KEY=
POSTGRES_URL=
S3_ENDPOINT=  S3_KEY=  S3_SECRET=  S3_BUCKET=
JWT_SECRET=
POSTHOG_KEY=
```

KPIs por agente:

- Brann: FRT, ART, taxa de qualificação, agendamentos, CSAT.
- Nyra: % aprovação de QA, posts/dia, engajamento, conversão por post.
- Alphie: latência de busca, cobertura de docs indexados, erros de ingestão.

Onboarding em 15 minutos:

1. Checkout → cria tenant → emite credenciais e link do WhatsApp (EVOLUTION QR).
2. Wizard: importar logo e brand kit → conectar redes → subir PDFs/FAQs → criar 3 intents do Brann.
3. Seed: Nyra gera 7 posts base + calendário. Alphie indexa todo o material.

Governança:

- Multitenancy por tenant\_id. Filtragem em todas as queries.
- RBAC simples: admin, editor, viewer.
- PII: criptografia em repouso. Logs sem dados sensíveis.

Próximas ações objetivas:

1. Criar as tabelas acima no Postgres e habilitar pgvector.
2. Subir três workflows n8n: brann\_inbound, nyra\_campaign, alphie\_ingest.
3. Carregar 20 documentos críticos no Alphie e testar RAG do Brann com 10 perguntas reais.