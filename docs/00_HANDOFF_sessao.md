# HANDOFF — retomar a Ginkgo numa nova sessão (ler PRIMEIRO)

Responder em pt-BR. Parceiro técnico sênior da Ginkgo. Ler também `00_INDEX_specs.md`.

## Decisão mestra
**Tronco canônico = `ginkgo-tree`** (Fable: Kernel/Boundary/tokens/HITL, back+front, 3 corpos).
`leaf` (Supabase) = doador de UX (aposentar após portar). Construir SEMPRE no tronco.
Repo tronco: `GITS FONTE/ginkgo-tree/ginkgo-tree` (.git aqui; duplo-aninhamento a achatar — item E).

## Estado do tronco (rodando)
Docker sobe limpo: ginkgo-api(:3333 healthy)/web(:3000)/worker/postgres+pgvector(:5433)/redis(:6380)/
n8n(:5679)/evolution(:8081). /health db+redis+queue ok. Kernel+Boundary+ledger GTK+HITL reais.
Dashboard (Ginkgo OS) lindo, login funciona, 50k GTK seed.

## Build em andamento (Claude Code no repo ginkgo-tree, branches LOCAIS, sem push)
Cadeia: main → feat/inbox-v1 → feat/suite-shell → ... e no tronco:
feat/design-ginkgo (Shell+Visão geral) → feat/inbox-design (Inbox 3-pane, gate 77/77) → **feat/crm-kanban (Kanban, EM CURSO — prompt já dado)**.
Próximo após Kanban: **composer-humano** (prompt pronto abaixo).

## Skills no tronco (.claude/skills/) — Claude Code carrega por trigger
ginkgo(design) · motion · frontend · fastify · n8n · stripe-billing · security-review · dataviz ·
research · remotion · pyre-avatar · wave-ads.

## Pricing (CONFIRMADO, USD): Leaf $79/$199/$499 · Wave $99/$249 · Pyre $99/$249 · Full $599.
GTK tokenizado + top-ups; modelos chineses baratos (DeepSeek/Qwen) via Provider Router p/ margem.

## Roster: Leaf=Brann · Pyre=Nyra · Wave=Alfred · Callima=secretária do cliente. Sexta-feira orquestra; Laplace governa.

## GITS FONTE (limpa)
ginkgo-tree (tronco) · compose stack (ops vivo + workflows/_biblioteca com 121 n8n) · landing page
ginkgo-sale (site) · leaf (doador) · _legacy_ginkgo (o fundador leva pra fora).
Pendente limpeza: mover node_modules/.next do ginkgo-tree p/ legacy QUANDO pausar o build; achatar duplo-aninhamento (item E, pro Code).

## ai-stack (Callima protótipo — separado do tronco, na máquina)
Containers ai-stack-* (postgres 5434, evolution 8080, n8n 5678, redis 6379, anythingllm 3001).
Instância CALLIMA = `open` (número do fundador 5553991338911). Fluxos n8n ATIVOS: Callima, AUDIO FEM,
ENVIAR MIDIA, LEAF Brann Actions Consumer. **Única trava p/ ver a Callima completa = crédito OpenRouter**
(LLM). Áudio = ElevenLabs (saldo separado). Teste: mandar WhatsApp pro número CALLIMA.

## Pendências do fundador (externas, destravam P0)
1. **Crédito OpenRouter (~$10)** → liga Callima + todo o compute. 2. **Portfólio Meta** (WhatsApp Cloud + Marketing API) → canais oficiais + Wave. 3. **Stripe USD**. 4. **fal.ai/HeyGen** (Pyre, depois). 5. **Postiz/Elasticsearch** (Content Engine).

## Próximos passos (ordem)
1. Code: Kanban (em curso) → composer-humano (prompt em `prompt_composer_humano.md`).
2. Validar Callima no WhatsApp quando o crédito entrar (acompanhar execução n8n ai-stack).
3. Mover regeneráveis do tronco + achatar (E). 4. Portar resto da UX (pricing/site) pro tronco.
5. Site institucional (repo separado) + landings SEO.

## Docs-fonte (em C:\sexta-feira\docs\)
00_INDEX_specs · suite_arquitetura_spec · app_leaf/wave/pyre_spec · inbox/crm_funil/pricing_impl specs ·
dashboard_arquitetura_3corpos · ecossistema_ginkgo_visao · roster_agentes_ginkgo · tokenizacao_arquitetura ·
modelos_provider_router · meta_portfolio_requisitos · gap_helena_vs_leaf · auditoria_gitsfonte ·
skills_portfolio_curado · site_institucional_spec · pyre/wave/helena briefs.

## Ritmo de trabalho
Fundador manda 1 prompt por vez pro Claude Code (no repo ginkgo-tree) → envia print → eu reviso e
preparo o próximo. PRs limpos, branches locais até decidir publicar. Tasks no widget (TaskCreate/Update).

---
## ATUALIZAÇÃO (fim da sessão 1)
- **Kanban CONCLUÍDO** no tronco: branch `feat/crm-kanban` (de inbox-design), commit local `48359fe`,
  sem push. Funil flexível (3 models + 2 migrações), API Fastify governada, Kanban DnD reusando LeadPanel;
  revisão achou+corrigiu 9 defeitos; gate tsc+eslint0+build+test 77/77; validado com dados reais.
- Cadeia de branches no tronco: feat/design-ginkgo → feat/inbox-design → **feat/crm-kanban** (atual). Tudo LOCAL.
- **Follow-ups pendentes (curtos):**
  1) **Fix AA dos eyebrows** (labels uppercase `ink-3`→`ink-2`) app-wide — dívida de acessibilidade (skill ginkgo exige AA). Micro-prompt.
  2) **Commitar `.claude/skills/`** no repo do tronco (ficaram untracked; são as 12 skills nossas).
  3) Senha dev `ginkgo-dev-123` no usuário demo (só DB local) — não levar pra prod.
- **Próxima fatia:** composer-humano (`prompt_composer_humano.md`). Depois: pricing/GTK + site.
- Pendência de limpeza segue: mover node_modules/.next do ginkgo-tree p/ _legacy_ginkgo quando pausar build; achatar duplo-aninhamento (item E, pro Code).
- Tudo continua LOCAL, sem push (decisão do fundador). main do tronco à frente; publicar só quando ele decidir.

---
## ATUALIZAÇÃO (sessão 2)
- **Estado real > handoff:** AA dos eyebrows e `.claude/skills` JÁ estavam feitos. Branch atual = **`feat/polish-aa`** (de feat/crm-kanban):
  - `fc1e454` — AA eyebrows via token semântico `--color-eyebrow` (= ink-2 #8a93a8); contraste 3.25→5.64–6.20:1 (passa WCAG 2.2 AA). Aplicado em AppSidebar, StageManager, LeadPanel, theme.css.
  - `20cf5f0` — `.claude/skills/` commitado (12 skills, 13 arquivos incl. ginkgo DESIGN.md). LOCAL, sem push.
  - Follow-up aberto (Code): `pnpm lint` repo-wide vermelho **pré-existente** (eslint varre `apps/web/.next/types/**`) — fechar com 1 linha de ignore; gate real = `pnpm typecheck` (verde) + `eslint.ignoreDuringBuilds:true`.
- **INCIDENTE OneDrive (causa-raiz, recorrente):** o tronco vive em `OneDrive\…\GITS FONTE` → o sync **trunca os arquivos do working tree** entre sessões (placeholders Files-On-Demand). Visto na sessão 2: 9 arquivos truncados no fim (schema perdeu Secret/VaultAccess, pnpm-lock mutilado, pyre/page.tsx virou binário). **HEAD íntegro** — só a cópia de trabalho corrompe; o sandbox NÃO consegue apagar no OneDrive (EPERM), então restaurar é nativo.
  - **Restaurar (terminal Windows/Code):** `del .git\index.lock` · `git restore .` · `del .claude\settings.local.json` · `git status` (clean). Pôr `.claude/settings.local.json` no `.gitignore`.
  - **Fix definitivo:** mover `ginkgo-tree` pra fora do OneDrive → `C:\dev\ginkgo-tree` (sem espaços/acentos). Mata a classe de bug E achata o duplo-aninhamento (item E). node_modules/.next: NÃO mover — deletar e `pnpm install` no destino. Docs/_legacy podem ficar no OneDrive.
- **Memória/vault (status, p/ não reperguntar):** secrets-vault (Security Boundary: Secret+VaultAccess, secret-resolver, put-secret, test/boundary) = **feito** (M2-01 slice 1a). Dev-memory vault (`vault/` + CONTEXT_LOG) = **feito** (último drop 06-10). **Memória de runtime/tenant = NÃO existe** por decisão (P004: dev-memory ≠ runtime/tenant memory). Histórico de conversa existe (Conversation/ChatMessage); store de memória longa do cliente, não.
- **Próxima fatia:** composer-humano (`prompt_composer_humano.md`, já apontando p/ `feat/polish-aa`) — colar DEPOIS de `git restore` deixar o tree limpo.
