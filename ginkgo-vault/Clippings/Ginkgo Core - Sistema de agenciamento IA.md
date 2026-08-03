---
title: "Ginkgo Core - Sistema de agenciamento IA"
source: "https://chatgpt.com/g/g-p-68e0a0b393cc8191a0f44ad743e1117d/c/68e09c53-5a60-8327-9948-bc934617ef80"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sáb., 4 de out. às 1:10

Imagine, eu quero fazer um super sistema de agenciamento ALL service, uma frente o Brann atendimento, vendedor, FAQ humanizado, outra frente a Nyra agente de ia que cria e posta todo o conteúdo público das redes sociais, e Alphie o assistente geral que fica de olho nos emails, nos agentes Brann e Nyra, financeiro, contratos, relatórios, organizando toda essas informações da empresa no NOTION, um CRM via pipedrive, se tiver mais ideias de integrações úteis coloque e como e pra que servirão, o principal quero que o cliente, quem vai ter acesso a esse ecossistema de ias consiga controlar, administrar, ativar/desativar funções, quero que faça isso por meio de uma interface no LOVABLE que usa uma ia integrada para ser feito os ajustes e integrações por meio de linguagem natural

bora arquitetar teu “trio parada dura” de IAs — Brann (vendas/FAQ), Nyra (conteúdo) e Alphie (back-office) — com um cockpit único no **Lovable** onde o cliente liga/desliga recursos e dá ordens em linguagem natural. Vou te dar: visão geral, integrações úteis, fluxos n8n, esquema do Supabase, bases Notion, mapeamento Pipedrive, toggles/ACL, e um “tradutor” NL→Ações pra tua UI do Lovable. Copia/cola sem dó. 😎

---

## 1) Arquitetura em 1 parágrafo (pra ter o mapa mental)

- **Lovable App (Cockpit do Cliente)**: interface com chat/caixa de comandos + toggles. O cliente escreve “pause WhatsApp fora do horário” e a IA converte isso em ação (feature flag, agendamento, update de variáveis).
- **n8n** como orquestrador: webhooks (Evolution API), agendadores (Cron), watchers (Gmail), conectores (Pipedrive/Notion/Meta/X), roteador por agente.
- **Supabase**: autenticação (multi-tenant), flags de recursos, filas de tarefas, storage de mídia, logs, RAG do Brann (FAQ/Docs).
- **Notion**: HQ de operações (Contratos, Financeiro, Conteúdo, Relatórios), boards de tarefas.
- **Pipedrive**: CRM de vendas (leads→deals), funis, atividades.
- **MCP/Tools** (opcional, mas letal): Google Drive, Apify, ElevenLabs, Docs e Scrapers sob chamada controlada.
- **Observabilidade**: logs e dashboards (Supabase table + painel no Lovable).

---

## 2) Recursos (por agente) + integrações úteis

### Brann (atendimento/FAQ/fechamento)

- **Canais**: WhatsApp (Evolution API), futuramente Telegram/Instagram DM.
- **Funções**: captação de lead, FAQ com RAG (Supabase), catálogo, agendamento, calculadoras, contratos (DocuSign), follow-up, relatórios semanais.
- **Integrações**: Evolution API, Pipedrive (persons/deals/activities), Google Calendar (ou Cron interno), DocuSign, ElevenLabs (voz, se áudio).

### Nyra (conteúdo público)

- **Funções**: pauta mensal, criação (imagem/vídeo/copy), calendário, aprovação, publicação, clipping de métricas.
- **Integrações**: Meta Graph (IG/FB), X API (se tiver), YouTube (uploads/cortes via ffmpeg em worker), TikTok (via parceiros/Buffer/Metricool), Notion (Calendário Editorial), Cloud storage (Supabase).

### Alphie (back-office/BI/coordenação)

- **Funções**: monitor de e-mails (Gmail), financeiro (lê Notion “Financeiro”), contratos (integra DocuSign + Notion), health-check de agentes, relatórios semanais/mensais em PDF.
- **Integrações**: Gmail/Outlook, Notion, DocuSign, Pipedrive (faturamento por deal), Supabase (logs/health).

**Extras inteligentes** (plug-and-play):

- **Apify** (pesquisas/monitoramento concorrentes).
- **Google Drive** (entrada de PDFs para RAG).
- **Stripe/Mercado Pago** (assinaturas + webhooks para status de cliente → toggles).
- **Buffer/Metricool** (se quiser centralizar postagens e analytics sem lidar API por API).

---

## 3) Lovable: “comandos em linguagem natural” → Ações

A IA do Lovable recebe o texto, valida permissões do cliente e gera um **Intent JSON** que os flows do n8n entendem.

### Esquema de Intent (cola no teu router de LLM)

```markdown
{
  "tenant_id": "acme-123",
  "actor": "owner|manager|viewer",
  "intent": "toggle_feature|post_content|set_hours|sync_crm|ingest_docs|report|broadcast|schedule_task",
  "target": "brann|nyra|alphie|global",
  "params": {
    "feature_key": "brann.whatsapp",
    "enabled": true,
    "schedule": "mo-fr 09:00-18:00",
    "platforms": ["instagram","x"],
    "post_id": null,
    "notion_page": null,
    "doc_urls": [],
    "notes": "texto livre do usuário aqui"
  }
}
```

### Exemplos NL → Intent

- “Desliga o WhatsApp do Brann das 20h às 8h e avisa quem mandar msg.” → `{"intent":"set_hours","target":"brann","params":{"feature_key":"brann.whatsapp","schedule":"daily 08:00-20:00"}}`
- “Nyra, gera 5 posts sobre imóveis e agenda pra IG e X essa semana.” → `{"intent":"post_content","target":"nyra","params":{"platforms":["instagram","x"],"notes":"5 posts tema imóveis, CTA captação"}}`
- “Ingerir este PDF no FAQ do Brann.” → `{"intent":"ingest_docs","target":"brann","params":{"doc_urls":["https://.../faq.pdf"]}}`
- “Relatório semanal geral pro meu e-mail.” → `{"intent":"report","target":"alphie","params":{"notes":"semanal completo"}}`

---

## 4) Supabase: schema base (multi-tenant + flags + RAG + jobs)

Copia/cola no SQL editor.

```markdown
-- Tenancy
create table tenants (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  owner_email text not null unique,
  created_at timestamptz default now()
);

-- Users (clientes e equipe)
create table tenant_users (
  id uuid primary key default gen_random_uuid(),
  tenant_id uuid references tenants(id) on delete cascade,
  email text not null,
  role text check (role in ('owner','manager','agent','viewer')) not null default 'owner',
  created_at timestamptz default now(),
  unique(tenant_id, email)
);

-- Feature flags por tenant
create table features (
  key text primary key,              -- ex: 'brann.whatsapp', 'nyra.instagram', 'alphie.gmail'
  description text
);

insert into features(key,description) values
('brann.whatsapp','Canal WhatsApp via Evolution'),
('brann.rag','Base de conhecimento RAG'),
('nyra.instagram','Postagem no Instagram'),
('nyra.x','Postagem no X'),
('alphie.gmail','Monitor de e-mails'),
('global.docusign','Assinatura de contratos');

create table tenant_features (
  tenant_id uuid references tenants(id) on delete cascade,
  feature_key text references features(key) on delete cascade,
  enabled boolean not null default false,
  config jsonb default '{}',
  updated_at timestamptz default now(),
  primary key (tenant_id, feature_key)
);

-- Intent queue (gera pelos comandos do Lovable)
create table intents_queue (
  id bigserial primary key,
  tenant_id uuid references tenants(id) on delete cascade,
  actor_email text,
  payload jsonb not null,
  status text check (status in ('queued','processing','done','error')) default 'queued',
  result jsonb,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

-- Logs (observabilidade)
create table agent_logs (
  id bigserial primary key,
  tenant_id uuid references tenants(id) on delete cascade,
  agent text check (agent in ('brann','nyra','alphie','system')),
  level text check (level in ('debug','info','warn','error')) default 'info',
  message text,
  meta jsonb,
  created_at timestamptz default now()
);

-- RAG: documentos + chunks (simplificado)
create table rag_docs (
  id uuid primary key default gen_random_uuid(),
  tenant_id uuid references tenants(id) on delete cascade,
  title text, source_url text, tags text[],
  created_at timestamptz default now()
);

create table rag_chunks (
  id bigserial primary key,
  doc_id uuid references rag_docs(id) on delete cascade,
  content text,
  embedding vector(1536), -- ajuste ao provedor
  chunk_index int
);
```

---

## 5) n8n: blocos essenciais (nomeia assim)

**Global**

- `INTENT Webhook` → grava em `intents_queue` → roteia por `intent`.
- `FEATURE Toggle` → CRUD em `tenant_features`.
- `REPORT Builder` → agrega Notion/Pipedrive/Supabase → PDF → e-mail do owner.
- `HEALTH Check` (Cron) → testa Evolution/Meta/Notion/Pipedrive → loga em `agent_logs` e alerta no WhatsApp do admin.

**Brann**

- `EVOLUTION Inbound` (Webhook) → `BRANN Classify` (LLM) → `RAG Search` (Supabase embeddings) → `Compose Answer` → `Pipedrive Upsert` → `Send Reply` (Evolution).
- `DOC Ingest` (HTTP get + splitter + embeddings) → preenche `rag_docs/rag_chunks`.
- `SCHEDULER Business Hours` (verifica `tenant_features.config.schedule`) → fora de horário: responde “voltamos em X” + activity no Pipedrive.

**Nyra**

- `Pauta Generator` (LLM) → Notion “Calendário Editorial”.
- `Asset Maker` (imagem/vídeo) → salva em Supabase Storage.
- `Publisher` (IG/X/YouTube) → lê Notion aprovados → posta → grava URLs e métricas.
- `Metrics Puller` (diário) → atualiza Notion “Métricas” → Alphie usa no relatório.

**Alphie**

- `GMAIL Watcher` → classifica (LLM) → abre tarefa no Notion ou cria activity no Pipedrive.
- `Finance Sync` (Notion ↔ Pipedrive) → calcula MRR/ARR por tenant → salva snapshot em Supabase.
- `Weekly Report` (Cron) → monta PDF e envia.

> Tudo isso conversa via **INTENT Router**: quando o Lovable dispara um JSON de intent, o webhook `INTENT Webhook` joga no `intents_queue` e o fluxo correspondente consome e executa.

---

## 6) Notion: bases sugeridas (pro Alphie organizar)

- **Clientes & Contratos**: Cliente, Plano, Status, Link DocuSign, Vencimento.
- **Financeiro**: Fatura, Valor, Modo (cartão/pix), Pago?, Competência, Cliente.
- **Calendário Editorial**: Post, Plataforma, Status (Ideia/Rascunho/Aprovado/Postado), Data/hora, Anexo, Link publicado.
- **Métricas Sociais**: Data, Plataforma, Post, Alcance, Engajamento, Cliques, Leads.
- **Relatórios**: Semana/mês, PDFs, insights-chave.

---

## 7) Pipedrive: campos & mapeamentos (cola e não pensa)

- **Person**: `whatsapp`, `instagram_handle`, `source` (WhatsApp/IG/Site), `consent` (checkbox).
- **Deal**: `plan_interest` (Starter/Basic/Advanced/Futurist), `lead_stage` (Novo/Qualificado/Proposta/Fechamento), `mrr` (numérico), `next_action_date`.
- **Activity**: tipo `WhatsApp`, `Reunião`, `Follow-up`, com `due_date` e `notes` vindos do Brann.

**Fluxo**: mensagem do WhatsApp → Brann cria/atualiza **Person** + abre **Deal** (se qualificado) + cria **Activity** (próximo passo). Alphie lê **won deals** e joga no Notion Financeiro.

---

## 8) Toggles + ACL (quem liga o quê)

- **Role Owner/Manager**: tudo.
- **Agent**: executar operações sem mexer em billing/contratos.
- **Viewer**: só leitura.

**Exemplos de feature toggles** (em `tenant_features`):

- `brann.whatsapp.enabled`
- `brann.rag.enabled`
- `nyra.instagram.enabled`
- `nyra.x.enabled`
- `alphie.gmail.enabled`
- `global.docusign.enabled`

Config extra vai em `config`:

```markdown
{
  "schedule": "mon-fri 09:00-18:00",
  "ooh_message": "Estamos offline agora, respondemos às 09h. Deixe seu nome e assunto!"
}
```

---

## 9) Variáveis.env (bloco base pro n8n / containers)

```markdown
EVOLUTION_BASE_URL=https://your-evolution-host
EVOLUTION_API_KEY=xxxx
PIPEDRIVE_API_TOKEN=xxxx
NOTION_API_KEY=xxxx
NOTION_DB_FINANCEIRO=xxxxxxxx
NOTION_DB_EDITORIAL=xxxxxxxx
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_SERVICE_ROLE=xxxx
OPENAI_API_KEY=xxxx
ELEVENLABS_API_KEY=xxxx
META_IG_APP_ID=xxxx
META_IG_APP_SECRET=xxxx
X_BEARER_TOKEN=xxxx
GMAIL_CLIENT_ID=xxxx
GMAIL_CLIENT_SECRET=xxxx
```

---

## 10) “Prompt cerebral” do roteador NL (cola no Lovable)

Use um único sistema para padronizar os intents.

```markdown
Você é o “Orquestrador do Ecossistema Ginkgo”.
Objetivo: transformar pedidos em linguagem natural em um JSON válido de INTENT, SEM executar nada.

Regras:
1) Identifique tenant, ator e permissões.
2) Descubra o alvo (brann|nyra|alphie|global) e a ação (toggle_feature|post_content|set_hours|sync_crm|ingest_docs|report|broadcast|schedule_task).
3) Preencha params coerentes; nunca invente credenciais. Se faltar dado crítico, peça um follow-up curto (máx 1 pergunta).
4) Saída SEMPRE só o JSON do intent.

Exemplos NL→JSON: [cole os do item 3]

Validações:
- Se o ator não puder fazer a ação, responda erro de permissão no campo "result" do JSON.
- Se o pedido envolver publicação, manter rascunho=TRUE por padrão, salvo quando o usuário disser “postar agora”.
```

---

## 11) Roteiros n8n “copia/cola” iniciais (pseudonós)

**Intent Router**

- Webhook `/intent`
- Node: “Validate & Upsert” (Supabase)
- Switch por `intent`:
	- `toggle_feature` → Update `tenant_features`
		- `set_hours` → Update `tenant_features.config.schedule`
		- `ingest_docs` → baixar→splitter→embed→ `rag_docs/chunks`
		- `post_content` → criar card no Notion Editorial (+ assets queue p/ Nyra)
		- `report` → enfileirar job `weekly_report`

**Brann Inbound**

- Webhook `/evolution/inbound`
- Get `tenant_features` → se `enabled=false` → resposta de OOH
- Node “Understand” (LLM) → `type: FAQ|Catalogo|Qualificação|Agendar|Orçamento`
- If FAQ → RAG → Compose → Evolution Reply
- If Qualificação → Upsert Person/Deal → Activity → Reply com CTA

**Nyra Publish**

- Cron diário → Query Notion “Aprovado e devido hoje” → Para cada:
	- Render asset (se faltando) → Upload → Post plataforma → Update Notion com link

**Alphie Weekly**

- Cron semanal → Query métricas (Notion) + faturamento (Pipedrive won) + logs (Supabase)
- Monta PDF (HTML→PDF) → E-mail owner

---

## 12) Segurança & governança (sem dor de cabeça)

- **Principle of Least Privilege**: tokens por tenant, scopes mínimos.
- **Audit Trail**: cada intent gera `agent_logs` + snapshot de `tenant_features` alterados.
- **Rate limiting**: por tenant nos endpoints de intent e ingestão.
- **Filas**: conteúdos de Nyra passam por status “Aprovar antes” por padrão.
- **DLP leve**: filtros para dados sensíveis em logs (mask de e-mail/telefone).

---

## 13) Como o cliente usa (exemplos reais no cockpit do Lovable)

- “Ativa o Brann no WhatsApp, horário comercial, mensagem de fora do horário educada.”
- “Nyra, 3 posts por semana sobre automação para corretores, CTA pro WhatsApp.”
- “Ingesta este PDF do contrato e disponibiliza pro Brann responder dúvidas.”
- “Alphie, relatório semanal amanhã 8h no meu e-mail.”

A interface mostra: **status por agente**, **toggles**, **fila de intents**, e um **log humano-legível** do que foi feito.

---

## 14) Próximos passos (rápidos e certeiros)

1. Criar as tabelas do Supabase (SQL acima).
2. Subir os 4 fluxos n8n (Intent Router, Brann Inbound, Nyra Publish, Alphie Weekly).
3. Conectar Evolution, Pipedrive, Notion e um canal social (começa por IG).
4. Publicar o cockpit no Lovable com o prompt do orquestrador e o schema de Intent.
5. Rodar um **teste e2e**: “Nyra, gera 1 post e agenda para amanhã 10h (rascunho).” → ver Notion/queue → postar.

Se quiser, eu já te entrego **JSONs de exemplo de n8n**, um **prompt de classificação do Brann**, e um **modelo de página Notion** pra só duplicar. Também dá pra adicionar “Planos e billing” (Stripe/Mercado Pago) com webhooks que **ativam/desativam** features automaticamente por tenant. Vamos plugar isso no teu stack atual e deixar teu trio — Brann, Nyra e Alphie — rodando como banda afinada em palco de neon. 🚀

Conseguiríamos de alguma forma automatizar o deploy de todo esse ecossistema? Cliente comprou = recebe o acesso e faz a configuração por linguagem natural

100% sim — dá pra deixar **“comprou ⇒ recebeu acesso ⇒ configura tudo por linguagem natural”** num clique. A lógica é tratar o onboarding como **provisionamento automatizado** com este pipeline:

## Como fica o “tapete vermelho” do deploy

1. **Checkout** (Stripe ou Mercado Pago)
	- Cada plano tem `metadata` com: `tier`, `features_default`, `limits`.
		- Evento: `payment_succeeded` (Stripe) ou `payment.created` / `payment.updated` (MP).
2. **Webhook de Billing ⇒ Orquestrador**
	- Um **Worker** (Cloudflare Worker, FastAPI em VPS, o que preferir) recebe o webhook e dispara um **Job “ProvisionarTenant”** numa fila (Supabase/Redis).
		- Por que fila? Idempotência e retentativa sem estourar nada.
3. **Provisionamento infra + app (idempotente)**
	- **Supabase**: cria `tenant`, `tenant_users`, `tenant_features` (defaults por plano), gera **API Keys** do cliente (scopadas).
		- **Lovable**: cria o “workspace”/projeto com o cockpit já vivo e **magic link** pro owner.
		- **n8n**: não cria uma instância por cliente; usa **um único n8n multi-tenant** com flows já prontos. Só grava um **registro de credenciais pendentes** (Notion/Pipedrive/etc.) e habilita webhooks `…/inbound?tenant_id=…`.
		- **RAG**: cria pastas de storage e insere as páginas-base no Notion (modelos “Financeiro”, “Editorial”, “Relatórios”).
		- **Canais**: prepara “slots” (Evolution API session placeholder) e deixa **status = pending\_auth** até o cliente conectar o WhatsApp.
4. **E-mail automático de boas-vindas**
	- Envia: **link do Lovable**, **magic link** (sem senha), e o **comando inicial**: “Escreva ‘configurar meu ecossistema’ e responda as 4 perguntas”.
5. **Onboarding por Linguagem Natural (no Lovable)**
	- O cliente digita: “configurar meu ecossistema”.
		- O “Orquestrador NL” (teu prompt roteador) faz perguntas curtas:
		- “Conectar Pipedrive? \[Autorizar\]” (OAuth)
				- “Conectar Notion? \[Autorizar\]” (OAuth)
				- “Ativar WhatsApp? Cole a URL da sessão do Evolution ou clique ‘conectar’.”
				- “Janelas de atendimento, assinatura de contratos (DocuSign), redes da Nyra (IG/X)?”
		- Cada resposta vira um **Intent JSON** e preenche `tenant_features/config`.
6. **Teste E2E em 1 comando**
	- O cliente clica “Rodar teste” → o n8n:
		- cria um post rascunho da Nyra,
				- manda uma msg de teste no WhatsApp via Brann,
				- gera um mini relatório via Alphie e entrega no e-mail.
		- Painel mostra ✅/❌ e como corrigir (sempre NL).

---

## O esqueleto técnico (copia/cola mental)

### A) Webhook Handler (pseudo)

```markdown
// /billing/webhook
onEvent(evt) {
  if (evt.type in ["payment_succeeded","payment.updated"]) {
    const ref = evt.data.customer_email;
    enqueue("ProvisionarTenant", {
      email: ref,
      tier: evt.data.metadata.tier,
      features: evt.data.metadata.features_default,
      payment_id: evt.data.id
    });
  }
}
```

### B) Job ProvisionarTenant (ordem das operações)

1. **Idempotência**: se já existir `tenant` com esse e-mail, sai com ok.
2. `insert tenants(...) returning tenant_id`
3. `insert tenant_users(owner)` com esse e-mail
4. `insert tenant_features` em lote conforme o plano (brann.whatsapp=false, nyra.instagram=false, …)
5. Criar **workspace Lovable** e gravar `lovable_project_id` no `tenant_features.config`
6. Inserir **Notion templates** (via tua app Notion) e salvar `notion_db_ids` no config
7. Gravar **chaves provisórias** /placeholders p/ Evolution, Pipedrive, etc.
8. Enviar **magic link** pro dono
9. Logar tudo em `agent_logs` (level=info)

### C) Supabase: defaults no provisionamento

```markdown
insert into tenant_features(tenant_id, feature_key, enabled, config)
values
  (:tenant, 'brann.whatsapp', false, '{"status":"pending_auth"}'),
  (:tenant, 'brann.rag', true,  '{"ingestion":"manual","status":"ready"}'),
  (:tenant, 'nyra.instagram', false, '{"status":"pending_auth"}'),
  (:tenant, 'nyra.x', false, '{"status":"pending_auth"}'),
  (:tenant, 'alphie.gmail', false, '{"status":"pending_auth"}'),
  (:tenant, 'global.docusign', false, '{"status":"pending_auth"}');
```

### D) n8n multi-tenant (sem dor)

- Todos os webhooks aceitam `tenant_id` (querystring ou header).
- Primeiro nó: “Load Tenant Config” (Supabase) → sai do fluxo cedo se a feature estiver off.
- **Credenciais**: nada hardcoded em cred store do n8n; puxe tokens **do Supabase** (criptografados) por `tenant_id`. Assim dá pra escalar sem clonar fluxo.
- **Templates de flow**: quando quiser, você também consegue importar automaticamente via **n8n REST API** numa esteira CI (mas o comum é ter 1 conjunto fixo de flows).

### E) OAuth & segredos

- Tenha **apps multi-tenant** (Notion, Pipedrive, Google, Meta).
- No Lovable, os botões “Conectar X” abrem o OAuth, voltam com `code` pro teu Worker, que troca por tokens e salva em `tenant_secrets` (tabela separada, criptografada).
- O orquestrador responde “Conexão ativa!” e habilita o toggle correspondente.

---

## “Mas e a infra? Vai em Docker, K8s ou EasyPanel?”

- Dá pra rodar **tudo em Docker Compose no EasyPanel/Hostinger**:
	- `proxy` (Caddy/Traefik)
		- `orchestrator` (Node/FastAPI)
		- `n8n` (multi-tenant)
		- `redis` (fila opcional)
		- **Supabase** é SaaS (recomendado).
- Se você quiser **one-click deploy** real oficial, empacota:
	- **Terraform** para DNS, buckets, secrets, Postgres (se não for Supabase).
		- **Ansible** ou **GitHub Actions** pra subir compose e aplicar `SQL migrations` + `seed` (tabelas/feature defaults).
- Para ambientes maiores, Helm/Kubernetes entra bonito — mas teu cenário atual com EasyPanel está ok e rápido.

---

## A mágica do “configurar por linguagem natural”

Você já tem o **router NL**. Agora ele também assume **onboarding**:

- “Conectar Pipedrive” → gera intent `connect_crm` e abre OAuth.
- “Ativar WhatsApp” → gera intent `connect_whatsapp` e pede a `EVOLUTION_SESSION_URL` (ou cria via API, se seu Evolution permitir).
- “Definir horário do Brann 9–18h” → `set_hours` + validação.
- “Quero plano Futurista pra 2 marcas” → `upgrade_tier` + dispara checkout de diferença de plano.

Tudo vira **Intents** idempotentes, auditados e reversíveis.

---

## Backoffice automático (upgrade/downgrade/cancelar)

- **Upgrade**: webhook de pagamento atualiza `tenant_features` e limites; dispara uma verificação de credenciais faltantes e envia to-do pro cliente (NL).
- **Downgrade**: desativa features extras, mantém dados por 30 dias; Alphie avisa o que será afetado.
- **Cancelamento/Reembolso**: dispara um **Deprovision Job** (revoga tokens, pausa webhooks, exporta Notion/CSV se necessário).

---

## Segurança e confiabilidade (sem drama)

- **Idempotência** em tudo (chave: `payment_id`).
- **Rate limit** por `tenant_id` no endpoint `/intent`.
- **Auditoria**: toda mudança de toggle/config vira linha em `agent_logs`.
- **Secrets** isolados (Supabase Row Level Security + criptografia app-side).
- **Chaos button**: botão “Reset de credenciais” por agente (só owner).

---

## O que eu já deixo pronto pra ti (quando quiser colar no teu stack)

- **SQL** de schema + seeds (já te dei a base, expando com `tenant_secrets`).
- **Spec do Intent** (pronto) + **prompts** do roteador de onboarding.
- **Blueprint do Worker** de webhook (Stripe/MP) + fila + Job `ProvisionarTenant`.
- **Flows n8n** (4 principais: Intent Router, Brann Inbound, Nyra Publish, Alphie Weekly) padronizados para `tenant_id`.
- **Templates Notion** (DB Financeiro, Editorial, Relatórios) com propriedades corretas.
- **E-mail de boas-vindas** e **checklist NL** no Lovable.

Se quiser, na próxima te mando o **pacote “seed de provisionamento”**:

- script `bootstrap.sql`,
- `orchestrator.example.env`,
- `compose.yml` com serviços,
- REST `postman_collection.json` (webhooks & intents),
- e os **prompts** polidos pro onboarding por linguagem natural.

Resultado: o cliente paga, recebe o link, fala com a interface (“configurar meu ecossistema”), e em minutos está com Brann-Nyra-Alphie **ligados, auditados e versionáveis** — sem você ficar suando no SSH. Quer que eu já descreva o Worker (FastAPI) do webhook + fila com o payload certinho pra copiar e colar?