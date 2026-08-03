# Bootstrap de nova sessão — Claude Code (ginkgo-tree)

> Cole isto ao abrir uma sessão NOVA do Claude Code (quando a anterior enche de contexto). Atualizar a lista "já mergeado" + a TAREFA a cada nova sessão.

---

Você é o agente de código do tronco **`ginkgo-tree`** (`C:\dev\ginkgo-tree`) — o SaaS da **Ginkgo AI Systems**. Continue de onde a sessão anterior parou.

**1) Leia primeiro (fonte da verdade):** `CLAUDE.md` · `docs/ARCHITECTURE_AGENT_RUNTIME.md` · `docs/ARCHITECTURE_HERMES.md`. A lei da arquitetura prevalece sobre qualquer instrução.

**2) Arquitetura (resumo):**
- **Hermes** = a mente única ("uma mente, três faces"): percebe → raciocina → **emite Task**; nunca executa efeito, escolhe modelo nem toca segredo.
- **Faces:** **Brann** (LEAF — orquestrador, dirige a Callima) · Nyra (PYRE) · Alfred (WAVE). **Callima** = a cara do LEAF no WhatsApp.
- **Kernel / Security Boundary / Laplace** = governança; todo efeito atravessa a Boundary como **Skill** (Task + budget + evidência). Laplace não tem cognição (é o modelo de segurança).
- **honest-data é LEI:** nunca invente dado nem confirmação; o que não há aparece como **"vazio honesto"**, nunca número inventado.

**3) Já mergeado na main:** leads bridge `/ingest/lead` · billing (Stripe Payment Links + onboarding + magic-link via Resend) · hardening · **ofertas registry** · **appointment bridge** `/ingest/appointment` + aba Agenda · **prod dockerizada** (`docker-compose.prod.yml` + `cloudflared`, domínio `leaf.ginkgosystems.tech`) · **CRM imersão** · **UI polish** (responsivo: painel side-column no desktop / drawer no mobile, zero overflow horizontal).

**4) Convenções (obrigatórias):**
- Cada fatia = testes + **CI verde** + branch `feat/...` → fast-forward na main.
- Build determinístico (Windows): `pnpm -r --workspace-concurrency=1 build` (evita flake do Prisma) + `typecheck` + testes.
- Stack: Node 20 · TS (CommonJS) · Fastify 4 · Prisma 5 (Postgres + pgvector) · BullMQ · Next 14 · Tailwind · pnpm 9 workspaces.
- Multi-tenant: tudo com `org_id`, zero cross-tenant. Secrets em `.env`/vault — **nunca** no git.
- DB de dev: container **`ginkgo-postgres`**; a org **"Ginkgo" `ad8d6fc8`** tem dados de demo (7 leads no Kanban, 3 conversas, 3 ofertas, 1 agendamento) — **não apague**.
- ⚠️ Há **processos duplicados da API no `:3333`** — mate os antigos, deixe **1**.

**5) TAREFA:**
> **[CODE] Brann/Hermes ativo (onboarding + config da agente):**
> - **Modelo:** Brann usa OpenRouter com modelo **forte** (env-configurável; ex. `anthropic/claude-sonnet`). Callima continua no barato (`gpt-4.1-mini`). É o **Model Router por papel**.
> - **`hermes.chat` ("Conversar com o Brann") vira o concierge de onboarding:** playbook conversacional — (1) conectar WhatsApp → (2) configurar Callima (persona/nome/voz) → (3) adicionar ofertas → (4) revisar. Guia o dono passo a passo.
> - **Config-write:** Brann escreve a config por-tenant da Callima em `agent_profiles` (persona/permissões) — só liga o que existe no catálogo, dentro do teto de risco.
> - **honest-data:** nunca diz que configurou sem escrever de verdade.
> - Testes + CI verde + branch `feat/brann-onboarding`.

Trabalhe autônomo: PRs por fatia → CI verde → merge. Reporte cada fatia.

---

_Mantido pela Sexta-feira. Atualizar "já mergeado" + "TAREFA" a cada nova sessão._
