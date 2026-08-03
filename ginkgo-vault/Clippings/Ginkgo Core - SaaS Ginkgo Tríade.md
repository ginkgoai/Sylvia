---
title: "Ginkgo Core - SaaS Ginkgo Tríade"
source: "https://chatgpt.com/g/g-p-68e0a0b393cc8191a0f44ad743e1117d/c/697be7b9-0a20-832d-ac24-6d8f9bae664e"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
levando em conta que essa e minha stack atual no easypanel, podemos instalar o molt aqui ou separado na cloudflare? e como transformamos isso em um saas onde o cliente só usa em uma tela bonita. as funções que ele vai desempenhar são, atendimento humanizado, criação e postagem automatica de conteudo e gestao de trafego

PRV Alimentos (Callima).json

Arquivo

a parte de conteudo fica para o molt, ele tem intergação com nano banana e veo3, vamos apenas deixar visual e automatico e como um plus, o trafego pago ele opera e desempenha no click up como Alfred, no conteudo como nyra e no atendimento para o cliente ele fala e conversa como Brann oq o cliente recebe de fato, atenção desses 3 bots, brann para suporte e configuração ou duvidas, nyra para criação e postagem automatica de conteudo, alfred para automação de ralatorios, campanhas, estratégias e ação no clickup, e uma secretária no whatsapp configurada pelo brann fluxo no n8n, telas de saas intuitivas e bonitas web ou mobile

## A) Onboarding SaaS: Stripe → Molt cria tenant → replica n8n → cria Inbox no Chatwoot → painel pronto

### Objetivo

Em **menos de 3 minutos** após pagar, o cliente:

- faz login no painel
- conecta canais (WhatsApp primeiro)
- já tem **Secretária WhatsApp** ativa (n8n)
- já tem **Inbox Chatwoot** (handoff humano)
- já tem **Brann** pronto para configurar tudo
- e o Molt já deixou Nyra/Alfred “armados” (mesmo que alguns conectores fiquem pendentes)

---

## 1) Componentes (quem faz o quê)

**Stripe**

- cobra e emite eventos (webhook)

**SaaS Controller (API)**

- autenticação
- cria tenant
- guarda status do provisionamento
- impõe limites por plano
- expõe endpoints pro painel

**Molt (Provisioner)**

- executa o “setup automático”
- cria/atualiza variáveis/prompt
- chama n8n e Chatwoot
- registra integrações e credenciais (via controller)

**n8n**

- já tem um “template base” da secretária
- replica/clona e parametriza por `tenant_id`

**Chatwoot**

- cria Inbox por tenant (WhatsApp/IG/Email)
- cria agentes/teams (opcional)
- recebe handoff do n8n

---

## 2) Banco (mínimo obrigatório)

Tabelas (conceito):

- `tenants(id, name, plan, status, created_at)`
- `tenant_provisioning(tenant_id, step, status, meta, updated_at)`
- `integrations(id, tenant_id, provider, status, config_json, secrets_ref)`
- `tenant_prompts(tenant_id, brann_prompt, secretary_prompt, nyra_prompt, alfred_prompt, updated_at)`
- `limits(tenant_id, messages_limit, posts_limit, jobs_limit, ...)`

**Status do tenant**: `PENDING_PAYMENT → PROVISIONING → ACTIVE` (ou `FAILED`)

---

## 3) Fluxo completo (linha do tempo real)

## Passo 0 — Checkout

1. Cliente escolhe plano no painel (Next.js)
2. Painel chama `POST /billing/checkout`
3. Stripe Checkout abre
4. Pagou → Stripe dispara webhook

---

## Passo 1 — Webhook do Stripe (gatilho do onboarding)

**Evento mínimo**: `checkout.session.completed`

### Controller recebe webhook e faz:

1. valida assinatura e assinatura ativa
2. cria tenant (se ainda não existir)
3. cria usuário owner e vincula ao tenant
4. grava `tenant.status = PROVISIONING`
5. dispara o Molt:

`POST /molt/provision` com:

```markdown
{
  "tenant_id": "uuid",
  "plan": "pro",
  "owner_email": "x",
  "brand": { "name": "...", "niche": "...", "tone": "...", "timezone": "America/Sao_Paulo" }
}
```

**Regra anti-bug:** webhook tem que ser idempotente (se receber duas vezes, não duplica nada).

---

## Passo 2 — Molt Provisioning (pipeline em etapas)

O Molt executa um **state machine** (com retry e logs). Etapas sugeridas:

### Etapa 2.1 — Inicialização

- cria `tenant_prompts` padrão (Brann/Nyra/Alfred/Secretária) com placeholders
- seta limites por plano
- marca `step=INIT OK`

### Etapa 2.2 — Chatwoot: criar Inbox padrão

Chamar Chatwoot API:

- criar **account** (opcional; se você usar 1 account geral, use “inboxes por tenant”)
- criar **inbox “WhatsApp – {tenant}”**
- criar **inbox “Email – {tenant}”** (opcional)
- criar **labels padrão**: `vip`, `boleto`, `urgente`, `handoff`, `lead`

Salvar no banco:

- `integrations(provider="chatwoot", config_json={account_id,inbox_ids,...})`

Marcar `step=CHATWOOT OK`

### Etapa 2.3 — n8n: replicar workflow da secretária

Aqui é onde SaaS vira “mágica”.

**Estratégia recomendada (multi-tenant A):**

- você mantém **1 workflow base** (Template)
- ao provisionar:
	- cria **1 cópia** do workflow com nome `tenant-{id}-secretary`
		- injeta variáveis (tenant\_id, prompts, inbox Chatwoot, números, etc.)

Injeções mínimas:

- `TENANT_ID`
- `SECRETARY_PROMPT`
- `CHATWOOT_INBOX_ID`
- `EVOLUTION_INSTANCE` (quando o cliente conectar)
- `SUPABASE_TENANT_NAMESPACE` (para RAG)

Marcar `step=N8N OK`

### Etapa 2.4 — Criar “Canais pendentes”

Como o cliente ainda não conectou WhatsApp/IG/Email, você cria “slots”:

- `integrations(provider="whatsapp", status="PENDING")`
- `integrations(provider="instagram", status="PENDING")`
- `integrations(provider="email", status="PENDING")`
- `integrations(provider="ads_meta", status="PENDING")`
- `integrations(provider="clickup", status="PENDING")`

Marcar `step=INTEGRATIONS OK`

### Etapa 2.5 — Finalizar

- `tenants.status = ACTIVE`
- `tenant_provisioning.status = DONE`
- emitir evento pro painel (websocket/polling): “Ambiente pronto”

---

## 4) Depois do onboarding: conexão de canais (primeiro login)

No primeiro acesso, o painel mostra um wizard curto:

## Wizard 1 — Conectar WhatsApp (Evolution)

Cliente clica “Conectar” → você cria/atribui instance.

Fluxo:

1. Painel chama `POST /integrations/whatsapp/start`
2. Controller chama Evolution API para gerar QR / status
3. Retorna QR pro painel
4. Quando conectar:
	- Controller salva `whatsapp.instance_id` / token
		- Molt atualiza workflow n8n do tenant com essas variáveis
		- Marca integração `ACTIVE`

## Wizard 2 — Base de conhecimento (RAG via Manus → Supabase)

Cliente sobe docs:

1. upload para storage (R2/S3)
2. cria job `KB_INGEST`
3. Molt envia para Manus
4. Manus grava na Supabase com `tenant_id`
5. Secretária (n8n) já consulta essa base

## Wizard 3 — ClickUp (Alfred)

OAuth/token → salva → Alfred começa:

- criar Space/Folder padrão (opcional)
- criar listas “Campanhas”, “Relatórios”, “Backlog”, “Ações do Dia”

---

## 5) O “contrato” entre Painel e Backend (endpoints mínimos)

### Billing

- `POST /billing/checkout`
- `POST /billing/webhook` (Stripe)

### Tenants

- `GET /tenant/me`
- `GET /tenant/provisioning-status`

### Integrations

- `POST /integrations/whatsapp/start`
- `POST /integrations/whatsapp/confirm` (ou callback)
- `POST /integrations/clickup/connect`
- `POST /integrations/meta/connect`
- `POST /integrations/email/connect`

### Knowledge

- `POST /kb/upload`
- `POST /kb/ingest/start`
- `GET /kb/ingest/status`

### Prompts/Config (Brann UI)

- `GET /config`
- `POST /config` (atualiza tom de voz, horário, regras)  
	→ Molt aplica e atualiza n8n/assistentes.

---

## 6) Idempotência e anti-caos (obrigatório em SaaS)

- Stripe webhook: usar `event.id` guardado para não processar duas vezes
- Provision steps: cada etapa tem `step_key` + `DONE`
- Requisições Molt→Controller com `request_id`
- Se falhar no meio, reexecuta só o que está pendente

---

## 7) O que o cliente sente (UX)

- Pagou → “estamos preparando seu ambiente”
- 30–90s → “ambiente pronto”
- Conecta WhatsApp → QR
- Sobe docs → barra de progresso
- Pronto: secretária respondendo + Chatwoot recebendo handoff
- Brann no painel para “me diga o que você vende e como quer falar”

---

## Próximo output (eu já consigo te entregar agora, sem perguntar mais nada)

Escolhe um destes para eu detalhar em seguida:

1. **Mapa de variáveis** (todas as envs e placeholders: `TENANT_ID`, prompts, Chatwoot IDs, Supabase namespace, Evolution instance etc.)
2. **Especificação do “Template n8n Secretária”** (quais nós, quais campos devem ser parametrizados, e como o Molt injeta as variáveis)
3. **Especificação Chatwoot multi-tenant** (1 account vs account por tenant, e como isolar inbox/agents/labels)

Responda com **1, 2 ou 3**.

1

## 1) Mapa de variáveis (env + placeholders) — padrão multi-tenant “A”

A ideia: **um único padrão** que serve para Brann (admin), Secretária WhatsApp (n8n), Nyra (conteúdo no Molt) e Alfred (ClickUp). Tudo sempre com `TENANT_ID`.

---

## A) Variáveis globais do SaaS Controller (API)

**Obrigatórias**

- `APP_ENV=prod|staging`
- `PUBLIC_APP_URL=https://app.seudominio`
- `PUBLIC_API_URL=https://api.seudominio`
- `JWT_SECRET=...`
- `DB_URL=postgres://...`
- `REDIS_URL=redis://...`
- `STRIPE_SECRET_KEY=...`
- `STRIPE_WEBHOOK_SECRET=...`

**Recomendadas**

- `ENCRYPTION_KEY=...` (criptografar tokens de integrações)
- `RATE_LIMIT_GLOBAL_PER_MIN=...`
- `DEFAULT_TIMEZONE=America/Sao_Paulo`

---

## B) Variáveis globais do Molt (Provisioner)

- `MOLT_API_KEY=...` (para o Controller autorizar chamadas)
- `CONTROLLER_BASE_URL=https://api.seudominio`
- `N8N_BASE_URL=http://n8n:5678` (interno) ou URL externa
- `N8N_API_KEY=...` (ou basic auth)
- `CHATWOOT_BASE_URL=https://chat.seudominio`
- `CHATWOOT_API_TOKEN=...`
- `MANUS_BASE_URL=...`
- `MANUS_API_KEY=...`
- `SUPABASE_URL=...`
- `SUPABASE_SERVICE_ROLE_KEY=...`
- `R2_ENDPOINT=...` (se usar)
- `R2_ACCESS_KEY=...`
- `R2_SECRET_KEY=...`
- `R2_BUCKET=...`

**Conteúdo (Nyra)**

- `NANO_BANANA_API_KEY=...`
- `VEO3_API_KEY=...`

---

## C) Variáveis por tenant (guardadas no DB e injetadas onde precisa)

Essas são **as variáveis “de cliente”**. Você guarda em `tenant_config` / `tenant_prompts` / `integrations`.

## C1) Identidade e branding

- `TENANT_ID=uuid`
- `TENANT_NAME="..."`
- `TENANT_NICHE="..."`
- `TENANT_TONE="formal|casual|premium|..."`
- `TENANT_LANGUAGE="pt-BR"`
- `TENANT_TIMEZONE="America/Sao_Paulo"`

## C2) Planos e limites (billing)

- `PLAN="starter|pro|ultra"`
- `LIMIT_MESSAGES_PER_MONTH=...`
- `LIMIT_POSTS_PER_MONTH=...`
- `LIMIT_JOBS_PER_DAY=...`
- `TOKEN_BALANCE=...` (se usar tokens)

## C3) Prompts (placeholders)

Você salva 4 prompts por tenant:

### Brann (admin/copilot)

- `BRANN_SYSTEM_PROMPT`
- `BRANN_ACTION_SCHEMA` (se usar saída estruturada)

### Secretária WhatsApp (atendimento ao cliente final)

- `SECRETARY_SYSTEM_PROMPT`
- `SECRETARY_FAQ_MODE=strict|flex`
- `HANDOFF_RULES_JSON` (quando mandar pro Chatwoot)

### Nyra (conteúdo)

- `NYRA_BRAND_GUIDE`
- `NYRA_CONTENT_RULES_JSON` (freq, plataformas, formatos)

### Alfred (tráfego/ops)

- `ALFRED_GOALS_JSON`
- `ALFRED_KPI_THRESHOLDS_JSON`

---

## D) Integrações por tenant (config + secrets)

## D1) WhatsApp (Evolution API)

**Config**

- `WA_PROVIDER="evolution"`
- `WA_INSTANCE_NAME="tenant-{TENANT_ID}"`
- `WA_WEBHOOK_URL="https://hooks.seudominio/wa/{TENANT_ID}"`

**Secrets**

- `WA_INSTANCE_TOKEN=...`
- `WA_BASE_URL=...` (URL do Evolution)

**Campos de roteamento**

- `WA_SENDER_JID` normalizado no n8n
- `WA_MESSAGE_ID`

## D2) Chatwoot

**Config**

- `CHATWOOT_ACCOUNT_ID=...`
- `CHATWOOT_INBOX_ID_WHATSAPP=...`
- `CHATWOOT_INBOX_ID_EMAIL=...` (opcional)
- `CHATWOOT_INBOX_ID_INSTAGRAM=...` (opcional)
- `CHATWOOT_LABELS_JSON=...`

**Secrets**

- `CHATWOOT_BOT_TOKEN` (se usar bot)
- `CHATWOOT_API_TOKEN` (global, no Molt/Controller)

## D3) ClickUp (Alfred)

**Config**

- `CLICKUP_WORKSPACE_ID=...`
- `CLICKUP_SPACE_ID=...` (opcional criar automático)
- `CLICKUP_FOLDER_ID=...`
- `CLICKUP_LIST_IDS_JSON=...` (Campanhas, Ações do Dia, Relatórios)

**Secrets**

- `CLICKUP_ACCESS_TOKEN=...`

## D4) Meta (Instagram/Facebook) — quando entrar

**Config**

- `META_PAGE_ID=...`
- `META_IG_BUSINESS_ID=...`

**Secrets**

- `META_ACCESS_TOKEN=...`

## D5) Email

Escolha um provider padrão (ex: SendGrid/Mailgun) para simplificar.

**Config**

- `EMAIL_FROM=...`
- `EMAIL_REPLY_TO=...`

**Secrets**

- `SENDGRID_API_KEY=...` ou `MAILGUN_API_KEY=...`

---

## E) Variáveis que o n8n precisa receber (mínimo para a Secretária)

Essas são as **variáveis “runtime”** do workflow do tenant. O Molt injeta ao clonar/configurar.

### Núcleo

- `TENANT_ID`
- `SECRETARY_SYSTEM_PROMPT`
- `TENANT_TIMEZONE`

### WhatsApp

- `WA_BASE_URL`
- `WA_INSTANCE_NAME`
- `WA_INSTANCE_TOKEN`

### Chatwoot (handoff)

- `CHATWOOT_BASE_URL`
- `CHATWOOT_ACCOUNT_ID`
- `CHATWOOT_INBOX_ID_WHATSAPP`
- `CHATWOOT_API_TOKEN` *(se preferir manter global no n8n, ok)*

### RAG / Supabase

- `SUPABASE_URL`
- `SUPABASE_ANON_OR_SERVICE_KEY` *(ideal service apenas no backend; no n8n use via proxy quando puder)*
- `RAG_TENANT_FILTER=TENANT_ID`
- `RAG_TOPK=5`
- `RAG_MIN_SCORE=0.75` *(exemplo)*

### Regras

- `HANDOFF_CONFIDENCE_THRESHOLD=0.65`
- `MAX_REPLY_CHARS=700` (WhatsApp-friendly)
- `QUIET_HOURS_JSON` (horário comercial, etc.)

---

## F) Como padronizar placeholders dentro dos prompts (pra ficar plugável)

Use sempre placeholders iguais:

- `{{TENANT_NAME}}`
- `{{TENANT_NICHE}}`
- `{{TONE}}`
- `{{POLICIES}}`
- `{{HANDOFF_RULES}}`
- `{{CHANNEL}}`
- `{{LANGUAGE}}`

O Molt faz um “render” final e grava:

- prompt renderizado (para execução)
- prompt-template (para edição depois)

---

## G) Convenção de nomes (para não se perder quando tiver 50 clientes)

- n8n workflows:
	- `tenant-{TENANT_ID}-router`
		- `tenant-{TENANT_ID}-secretary`
		- `tenant-{TENANT_ID}-handoff`
- Chatwoot inbox:
	- `WA - {TENANT_NAME}`
		- `EMAIL - {TENANT_NAME}`
- Evolution instance:
	- `wa-tenant-{TENANT_ID}`

---

## Checklist de “se está certo”

Se você olhar qualquer log/evento e conseguir responder:

- “de qual cliente é?” → `tenant_id`
- “qual canal?” → `channel`
- “qual conversa?” → `external_id`
- “qual bot agiu?” → `agent=brann|nyra|alfred|secretary`

Então o SaaS está “industrial”.

---

Se você quiser o próximo passo lógico, é: **pegar esse mapa e transformar em um “Tenant Config JSON” único**, para o Molt salvar e o n8n consumir sem gambiarras.

Prossiga

## Próximo passo: “Tenant Config JSON” único (fonte da verdade)

Você vai tratar cada cliente como um **objeto de configuração**. O Molt grava isso, o Controller versiona, e o n8n consome (via endpoint) para não depender de 200 variáveis soltas.

### Estrutura recomendada (schema prático)

```markdown
{
  "tenant": {
    "id": "uuid",
    "name": "Nome da Marca",
    "niche": "Nicho",
    "tone": "premium|casual|formal",
    "language": "pt-BR",
    "timezone": "America/Sao_Paulo",
    "status": "ACTIVE",
    "plan": "starter|pro|ultra"
  },
  "limits": {
    "messages_per_month": 5000,
    "posts_per_month": 120,
    "jobs_per_day": 200,
    "token_balance": 0
  },
  "agents": {
    "brann": {
      "system_prompt": "..."
    },
    "secretary": {
      "system_prompt": "...",
      "handoff": {
        "enabled": true,
        "confidence_threshold": 0.65,
        "rules": {
          "always_handoff_if": ["pedido de orçamento complexo", "reclamação", "ameaça legal"],
          "handoff_if_unknown": true
        }
      },
      "reply_policy": {
        "max_chars": 700,
        "format": "whatsapp_short",
        "quiet_hours": {"enabled": false}
      },
      "rag": {
        "enabled": true,
        "topk": 5,
        "min_score": 0.75,
        "filter": {"tenant_id": "uuid"}
      }
    },
    "nyra": {
      "brand_guide": "...",
      "content_rules": {
        "platforms": ["instagram", "tiktok", "youtube_shorts", "x"],
        "frequency_per_week": 6,
        "needs_approval": true
      }
    },
    "alfred": {
      "goals": {"primary": "reduzir CPA", "secondary": "aumentar ROAS"},
      "kpi_thresholds": {"cpa_up_pct": 20, "ctr_down_pct": 15},
      "cadence": {"daily_check": true, "weekly_report": true}
    }
  },
  "integrations": {
    "whatsapp": {
      "provider": "evolution",
      "status": "PENDING|ACTIVE",
      "config": {
        "base_url": "https://evo.seudominio",
        "instance_name": "wa-tenant-uuid",
        "webhook_url": "https://hooks.seudominio/wa/uuid"
      },
      "secrets_ref": "sec_whatsapp_uuid"
    },
    "chatwoot": {
      "status": "ACTIVE",
      "config": {
        "base_url": "https://chat.seudominio",
        "account_id": 1,
        "inbox_ids": {"whatsapp": 10, "email": 11}
      },
      "secrets_ref": "sec_chatwoot_global"
    },
    "clickup": {
      "status": "PENDING|ACTIVE",
      "config": {
        "workspace_id": "123",
        "space_id": "456",
        "folder_id": "789",
        "lists": {"campaigns": "1", "actions": "2", "reports": "3"}
      },
      "secrets_ref": "sec_clickup_uuid"
    },
    "manus": {
      "status": "ACTIVE",
      "config": {"base_url": "..."},
      "secrets_ref": "sec_manus_global"
    },
    "supabase": {
      "status": "ACTIVE",
      "config": {"url": "...", "rag_namespace": "tenant_uuid"},
      "secrets_ref": "sec_supabase_global"
    },
    "content_media": {
      "status": "ACTIVE",
      "config": {
        "r2_bucket": "ginkgo-media",
        "path_prefix": "tenant/uuid/"
      },
      "secrets_ref": "sec_r2_global"
    },
    "nyra_engines": {
      "status": "ACTIVE",
      "config": {"nano_banana": true, "veo3": true},
      "secrets_ref": "sec_nyra_engines_global"
    }
  },
  "provisioning": {
    "version": 1,
    "updated_at": "2026-01-29T00:00:00Z"
  }
}
```

---

## Como isso vira execução (sem gambiarra)

### 1) Onde guardar

- **DB (Postgres)**: `tenant_config_current` (jsonb) + `tenant_config_versions` (histórico)
- **Secrets**: ficam fora do JSON (só `secrets_ref`), no EasyPanel/Vault/DB criptografada.

### 2) Como o n8n consome

Em vez de 50 env vars:

- no começo do workflow: `GET /tenant/{tenant_id}/config`
- cache em Redis por 60–300s
- todo node usa `config.agents.secretary...` etc.

### 3) Como o Molt aplica mudanças

Quando o Brann “configura”:

- Painel → `POST /tenant/config` (patch)
- Controller versiona e dispara evento
- Molt recebe evento e:
	- atualiza workflow do n8n (se precisar)
		- atualiza Chatwoot (labels/inbox)
		- atualiza conectores (ClickUp/Meta/etc.)

---

## Regras de ouro (pra não explodir quando tiver 100 clientes)

1. **Somente 1 fonte da verdade:** `Tenant Config JSON`
2. **Secrets nunca dentro do JSON.** Só `secrets_ref`.
3. **Tudo que entra/saí tem tenant\_id** (headers + logs).
4. **Patch granular** (não sobrescreve config inteira por acidente).
5. **Versionamento**: cada mudança gera `version++`.

---

## Próximo deliverable (agora sim fica “plug and play”)

Vou te passar em seguida:

- o **modelo de endpoints** do Controller para isso (`GET config`, `PATCH config`, `Rotate secrets`, `Provision status`)
- e o **mapa de “patches”** que o Brann pode aplicar sem risco (tom de voz, handoff, horários, canais, metas)

Se quer que eu siga nessa linha, prossigo com: **endpoints + payloads + regras de idempotência**.