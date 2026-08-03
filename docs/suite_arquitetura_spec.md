# Ginkgo Suite — Arquitetura (master spec)

Modelo estilo Manus: **shell único** + **apps distintos**. Um login/org/carteira/governança;
cada produto (Leaf · Wave · Pyre) é um app com página, seções e formato próprios, que se
cruzam quando necessário. Repo: LEAF monorepo (`apps/web` Next.js, `apps/api` Fastify, Supabase).

## O shell (compartilhado entre todos os apps)
- **1 autenticação** (Supabase GoTrue) · **1 organização/tenant** (org_id) · **1 carteira GTK**
  (token_wallets/ledger) · **1 billing** (Stripe USD) · **1 governança** (HITL/kill-switch/
  auditoria — Laplace/Hermes, via brann_actions).
- **App Switcher** (canto sup. esq.): alterna Leaf / Wave / Pyre (+ futuros). Cada app tem
  cor de acento própria (Leaf verde · Wave azul · Pyre âmbar) sobre o mesmo dark navy.
- **Barra global**: saldo GTK visível, alertas (80%/100%), notificações, conta/org, ajuda.
- **Sidebar por app**: muda conforme o app ativo (cada app define suas seções).
- **Áreas globais** (fora dos apps): Conta/Settings, Billing/Planos, Admin/Equipe, Onboarding.

## Convenção de rotas (apps/web/app)
- `/(dashboard)/leaf/...` · `/(dashboard)/wave/...` · `/(dashboard)/pyre/...`
- Globais: `/(dashboard)/settings`, `/billing`, `/(dashboard)/admin`, `/onboarding`.
- (Hoje as rotas são inbox/crm/assistant/studio soltas → reorganizar sob o app dono:
  inbox+crm+assistant+media → Leaf; studio → Pyre; nova área → Wave.)

## Serviços compartilhados (contrato entre apps)
- **GTK wallet** (tokenRouter): qualquer app debita pela `gtk_costs`. Saldo único.
- **Governança**: toda ação sensível de qualquer agente passa por HITL/auditoria.
- **Entidades comuns** no mesmo banco: organizations, profiles, memberships, leads,
  conversations, payments, media_assets, agents. Apps leem/escrevem nas MESMAS tabelas.

## Cruzamentos entre apps (o loop, no produto)
- **Pyre → Leaf**: clipes/voz/avatar gerados viram `media_assets` que a Callima envia no chat.
- **Pyre → Wave**: peças aprovadas no Pyre podem virar criativos no Wave.
- **Wave → Leaf**: clique no anúncio (UTM) cria/atualiza `lead` e abre `conversation` na Inbox.
- **Leaf → Wave**: `lead` ganho + `payment` = receita que o Wave atribui ao criativo (ROAS).
- **Pyre Trends → Pyre/Wave**: tendências informam pauta de conteúdo e ângulo de anúncio.
Tudo no mesmo org_id; nenhum app precisa "integrar" com o outro — leem o mesmo banco.

## Design system compartilhado
- Dark navy base + acento por app. Tokens Tailwind v4 @theme (sem cor hardcoded).
- Componentes comuns: Shell, AppSwitcher, GlobalBar(saldo GTK), Sidebar, LeadPanel
  (o painel de lead reusado em Leaf/Inbox, Kanban e onde fizer sentido), Card, EmptyState,
  ErrorState, Skeleton. Estados loading/empty/error obrigatórios em toda tela.

## Visão por app (specs dedicadas)
- **Leaf** (Atendimento+CRM, agente Brann; secretária do cliente = Callima) → `app_leaf_spec.md`
  Inclui Inbox (`inbox_spec_claudecode.md`) + Funil/Kanban (`crm_funil_spec_claudecode.md`).
- **Wave** (Tráfego, agente Alfred) → `app_wave_spec.md` (base: `wave_funcionalidades_utmify.md`).
- **Pyre** (Conteúdo/Estúdio, agente Nyra) → `app_pyre_spec.md` (base: `pyre_funcionalidades_playsquad.md`).
- **Planos/GTK** (global) → `pricing_impl_claudecode.md` (+ `pricing_tokenizado_ginkgo.md`).
- **Site institucional** (separado) → `site_institucional_spec_claudecode.md`.

## Ordem de execução
P0 LEAF: Shell+AppSwitcher → Inbox → Kanban → Settings/Billing(GTK). Depois Wave MVP, Pyre MVP.
Canais oficiais (WhatsApp Cloud API) + Stripe USD entram quando o founder destravar (Meta/CNPJ).

## Aceite (suíte)
- 1 login leva ao shell; AppSwitcher troca de app preservando org/saldo/sessão.
- Saldo GTK único visível e debitado por qualquer app; pausa em 100%.
- Dados cruzam sem "integração" (mesmo banco). Cada app tem sua identidade de acento.
