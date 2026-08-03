---
title: "Lab - Descrição aplicativo Ginkgo Piper"
source: "https://chatgpt.com/g/g-p-6920bddfbb548191ac06d937cdb0b5c0/c/690a3dd2-e7d8-832d-82b5-5de5d8623e31"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
ter., 4 de nov. às 14:54

Segue a base “pronta-para-montar” do **Ginkgo Piper** no Lovable. Foco: app web funcional, já com lógica, estrutura de dados, fluxos e cópia inicial. Você cola isso no Lovable como guia de seções, componentes e automações.

## 1) Proposta de valor

Conteúdo curto em vídeo e texto, estilo feed vertical. A IA lê fontes, resume, cria cards dinâmicos e quizzes. O usuário aprende em micro-blocos, salva coleções, recebe rotinas diárias e compartilha.

## 2) Loop principal

Entrada → Coleta de fontes → Resumo/segmentação por IA → Geração de cards (texto, áudio TTS, imagem) → Publicação no feed → Interação (like, salvar, comentar, quiz) → Reforço espaçado e notificações → Progresso e badges.

## 3) Personas

- Curador (Nyra): publica coleções temáticas.
- Aprendiz: consome, salva, faz quizzes.
- Autor convidado: envia links e materiais, ganha créditos.
- Admin: modera, revisa, aprova.

## 4) Arquitetura lógica

Frontend: Lovable (páginas, componentes, estados).  
Backend leve: Supabase (Auth + DB + Storage) + n8n (ingestão, RAG, automações) + Evolution API para WhatsApp opcional.  
IA: ChatGPT/Claude para resumo, classificação e quizzes; ElevenLabs TTS opcional; RAG no Supabase (docs vs memories) para coleções aprofundadas.

## 5) Mapa de páginas (Lovable)

1. Landing / Home pública  
	Hero, “Como funciona”, CTA “Entrar”.
2. Explorar  
	Filtros: tema, nível, duração, idioma. Cards de coleção.
3. Coleção (detalhe)  
	Capa, descrição, autor, sequência de cards, botão “Começar”.
4. Leitor de Cards (player)  
	Navegação vertical, TTS play, quiz inline, referências.
5. Busca  
	Prompt com sugestões, histórico, chips de filtros.
6. Minhas Coleções  
	Salvos, em andamento, concluídos; progresso e badges.
7. Autores / Submissões  
	Form de envio de link/arquivo, status de aprovação.
8. Painel Admin  
	Filas de aprovação, edições, métricas e feedbacks.
9. Conta  
	Perfil, preferências, notificações, exportação de dados.

## 6) Componentes chave (Lovable)

- CardPiper: título, resumo ≤ 280 chars, tag, tempo, ações.
- QuizInline: 1 pergunta + 3 opções + feedback.
- AudioBadge: play/pausa + progresso.
- ProgressBar: por coleção e global.
- FilterChips: tema, duração, formato.
- SubmitSource: URL + upload + tags.
- AdminQueue: tabela com aprovar/editar/publicar.

## 7) Modelo de dados (Supabase SQL)

```markdown
-- usuários
create table profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  username text unique,
  role text check (role in ('learner','author','admin')) default 'learner',
  prefs jsonb default '{}'::jsonb,
  created_at timestamptz default now()
);

-- coleções
create table collections (
  id uuid primary key default gen_random_uuid(),
  slug text unique,
  title text not null,
  cover_url text,
  description text,
  tags text[],
  difficulty text check (difficulty in ('beginner','intermediate','advanced')),
  est_minutes int,
  author_id uuid references profiles(id),
  status text check (status in ('draft','review','published')) default 'draft',
  created_at timestamptz default now()
);

-- cards
create table cards (
  id uuid primary key default gen_random_uuid(),
  collection_id uuid references collections(id) on delete cascade,
  order_index int,
  kind text check (kind in ('summary','insight','quote','quiz','reference','image','audio')),
  content jsonb not null, -- schema abaixo
  created_at timestamptz default now()
);

-- progresso
create table progress (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references profiles(id) on delete cascade,
  collection_id uuid references collections(id) on delete cascade,
  card_id uuid references cards(id) on delete cascade,
  status text check (status in ('seen','completed')) default 'seen',
  updated_at timestamptz default now(),
  unique(user_id, card_id)
);

-- likes/saves
create table interactions (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references profiles(id) on delete cascade,
  target_kind text check (target_kind in ('collection','card')),
  target_id uuid not null,
  type text check (type in ('like','save')) not null,
  created_at timestamptz default now(),
  unique(user_id, target_kind, target_id, type)
);

-- submissões de fonte por autores
create table submissions (
  id uuid primary key default gen_random_uuid(),
  submitted_by uuid references profiles(id),
  source_url text,
  source_file_url text,
  notes text,
  tags text[],
  status text check (status in ('queued','processing','needs_changes','approved','rejected','published')) default 'queued',
  created_at timestamptz default now()
);

-- RAG: índice de documentos (resumos longos)
create table rag_docs (
  id uuid primary key default gen_random_uuid(),
  submission_id uuid references submissions(id),
  title text,
  url text,
  chunk text,
  embedding vector(1024), -- ajuste ao provedor
  meta jsonb,
  created_at timestamptz default now()
);
```

## Esquema cards.content (JSON)

```markdown
{
  "summary": {"text": "…"},
  "insight": {"text": "…", "action": "try_this"},
  "quote": {"text": "…", "source": "…"},
  "quiz": {"q":"…","options":["A","B","C"],"answer_index":1,"explain":"…"},
  "reference": {"links":[{"title":"…","url":"…"}]},
  "image": {"url":"…","caption":"…"},
  "audio": {"url":"…","duration": 42}
}
```

## 8) Fluxos n8n (mínimo viável)

1. **Ingestão de fonte**  
	Trigger: nova `submission` com status `queued` → HTTP Request pega URL/arquivo → IA: extrai tópicos → gera `collections` + `cards` rascunho → grava RAG `rag_docs` → seta status `processing` → envia para fila de revisão.
2. **Revisão e publicação**  
	Trigger manual ou cron → aprova/edita → seta `collections.status='published'` → notifica seguidores do tema.
3. **Reforço espaçado**  
	Cron diário → consulta `progress` e datas → envia 1–3 cards pendentes + 1 quiz recap via notificação e e-mail/WhatsApp (Evolution API opcional).
4. **Busca semântica**  
	HTTP endpoint `/search` → recebe termo → consulta embeddings de `rag_docs` e `cards` → retorna coleções e cards ordenados.
5. **TTS opcional**  
	Sub-workflow “TTS” → recebe texto do card → ElevenLabs → salva em Storage → atualiza `cards.content.audio.url`.

## 9) Contratos de API (frontend ↔ n8n/Supabase)

- `GET /collections?status=published&tag=AI&limit=20&offset=0` → lista.
- `GET /collections/:slug` → coleção + cards.
- `POST /progress` `{card_id, status}` → 200/400.
- `POST /interactions` `{target_kind, target_id, type}`.
- `POST /submissions` `{source_url|file, tags, notes}`.
- `POST /search` `{q}` → `{collections:[…], cards:[…]}`.

No Lovable, use ações REST ou integrações Supabase prontas.

## 10) Estados e lógica do player

- Estados: `loading` → `reading` → `quiz_pending` → `answered` → `completed`.
- Regras: concluir card marca `progress`. Quiz certo avança com confete. Errado abre explicação e permite retry.

## 11) Cópia base (PT-BR)

- Hero: “Aprendizado em micro-doses. Alto impacto. Zero ruído.”
- Sub: “Resumos acionáveis, quizzes rápidos e coleções curadas por IA.”
- CTA: “Começar agora”.
- Vantagens: “5–7 min por coleção • Reforço diário • Salve e compartilhe”.

## 12) SEO e descoberta

Título por coleção = `Tema | Ginkgo Piper`.  
Metas OG. Mapa de site. Schema `Article` e `CreativeWork`. Slugs estáveis.

## 13) Métricas

- Ativação: % perfil completo + primeira coleção iniciada.
- Aha: 3 cards completados + 1 quiz acertado.
- Retenção D7/D30.
- Tempo em card.
- Taxa de submissões aprovadas.

## 14) Gamificação simples

Badges: “Primeiros 10 cards”, “5 dias seguidos”, “Autor estreante”.  
Ranking opcional semanal por temas.

## 15) Monetização

Freemium: X coleções/mês.  
Pro: ilimitado + TTS + coleções premium + exportar.  
Teams: workspace, relatórios, trilhas.  
Checkout via Stripe/Hotmart. Bloqueio por role ou feature flag.

## 16) Segurança e privacidade

Auth Supabase. RLS por usuário.  
Uploads validados. Logs de moderação.  
Exportar e apagar dados via Conta.

## 17) Roadmap enxuto

- Semana 1: Landing, Auth, Explorar, Detalhe, Player básico, Supabase tabelas.
- Semana 2: Ingestão n8n v0, fila de revisão, publicação, busca semântica v0.
- Semana 3: Reforço espaçado, TTS opcional, métricas básicas, badges v0.
- Semana 4: Monetização, autores externos, moderação avançada.

## 18) Como montar no Lovable (passo a passo curto)

1. Criar projeto “Ginkgo Piper”.
2. Conectar Supabase (Auth+DB+Storage).
3. Importar tabelas SQL.
4. Páginas: Landing, Explorar, Coleção, Player, Minhas, Submissões, Admin.
5. Componentizar CardPiper, QuizInline, ProgressBar.
6. Conectar listas a `collections` com filtros.
7. Player: data source = `cards` por `collection_id` ordenado.
8. Ações: onView/onLike/onSave → chamadas REST para Supabase RPC ou n8n.
9. Form de submissão → cria `submissions`.
10. Admin → tabela `submissions` + botões “Aprovar/Publicar” chamando n8n.
11. Notificações: e-mail + WhatsApp opcional via Evolution API.

## 19) Exemplos de prompts IA (n8n)

**Resumo denso, 120–180 palavras**  
“Resuma o conteúdo abaixo em até 180 palavras. Dê 1 insight aplicável e 1 chamada para ação curta. Sem floreio.”

**Geração de quiz**  
“Crie 1 pergunta objetiva com 3 opções. Retorne JSON {q, options\[3\], answer\_index, explain}.”

**Tags e nível**  
“Classifique o texto em até 5 tags e um nível entre beginner/intermediate/advanced. Retorne JSON.”

## 20) Checklist de publicação

- Responsivo mobile-first.
- Lighthouse ≥ 90 em Performance e A11y.
- Termos e Política publicados.
- Rotas protegidas.
- Plano Pro desativando paywall só após testes.

Se quiser, envio agora o pacote: SQL final, exemplos de payloads para n8n, e a lista de componentes com props para colar direto no Lovable.