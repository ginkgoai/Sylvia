# Prompt Fable — MERGE M5b+M5c → main (+ coesão) — 2026-07-06

> Cole no Claude Code (Fable), no repo `C:\dev\ginkgo-tree`. Fatia de INTEGRAÇÃO (não é feature nova): levar a branch pronta pra `main`, provar que o boot aguenta a migração nova, e ressincronizar os docs que a re-auditoria pegou defasados. Disciplina PROCESSO: auditoria adversarial ANTES, loop até o gate verde, review DEPOIS, coesão no fim. honest-data: não afirme "mergeado/verde" sem o comando que prova.

---

Você é o Fable, engenheiro do trunk governado da Ginkgo (LEAF/Callima). Faça a **integração da branch `feat/whatsapp-connect-surface` na `main`** e a coesão de docs. Trabalhe em passos pequenos, provando cada um.

## Contexto (verificado na re-auditoria de hoje)
- A branch **`feat/whatsapp-connect-surface`** está **+2 / −0** em relação a `origin/main` → **fast-forward limpo**. Os 2 commits: **M5b — Ofertas in-chat** (`7bda631`) e **M5c — Conectar WhatsApp / QR** (`ba819ec`). Gate na branch = **381 testes**.
- Traz a migração nova **`20260704000000_connect_task_dedup`** (índice único PARCIAL anti-TOCTOU no connect) — ela roda no **boot da api** via `prisma migrate deploy`.
- ⚠️ **Risco de boot:** se em algum banco a migração **`20260620100000_message_human_agent`** estiver marcada "failed" no `_prisma_migrations`, o `migrate deploy` entra em **crash-loop** (fail-loud por design). O SQL dela é idempotente; a cura é baseline: `prisma migrate resolve --applied 20260620100000_message_human_agent`. Cuidado com o gotcha do `pnpm exec prisma` **engolir args** — use `scripts/db-migrate.sh` / `npx`.

## AUDITORIA PRÉ (adversarial — faça ANTES de tocar em qualquer coisa)
Responda por escrito, com evidência (comando + saída), e **pare se algo divergir**:
1. `git fetch` + `git log --oneline origin/main..feat/whatsapp-connect-surface` — confirme que são **exatamente** os 2 commits esperados e que `main` **não** andou (senão o FF deixa de ser limpo → reavaliar).
2. `git status` limpo? Working tree sem alterações não commitadas (fora `.claude/settings.local.json` untracked, inócuo).
3. A migração `20260704000000` é **aditiva** (índice parcial), sem DROP/rename destrutivo? Confirme lendo o SQL.
4. Há algo em M5b/M5c que **quebre honest-data ou um invariante** (dinheiro/credencial sem R3→HITL, escrita-fantasma, cross-tenant)? Cite os arquivos tocados pelos 2 commits (`git diff --stat origin/main..HEAD`) e julgue.
5. Qual o **estado real** do `_prisma_migrations` no banco de dev? (`SELECT migration_name, finished_at, rolled_back_at FROM _prisma_migrations ORDER BY started_at;`) — a `20260620100000` está applied ou failed **aqui**?

## TAREFAS (loop — um item por vez até o gate verde)
1. **Gate na branch primeiro:** `pnpm install --frozen-lockfile` → `pnpm build` → `pnpm typecheck` → `pnpm test`. Deve fechar **381/381**. Se não, **pare e reporte** (a contagem estática dizia 381; provar de verdade).
2. **Merge fast-forward:** `git checkout main` → `git merge --ff-only feat/whatsapp-connect-surface`. Se o FF for recusado, **pare** (a premissa mudou).
3. **Prova de boot com a migração nova:** suba a api (ou rode `prisma migrate deploy` no banco de dev) e confirme **"No pending migrations"/boot saudável**. Se crash-loop na `20260620100000`, aplique o baseline (`migrate resolve --applied ...`) e re-tente; **documente** exatamente o que fez.
4. **Gate na main pós-merge:** `pnpm test` de novo na `main` → **381/381**. `prisma validate` (drift-guard do CI) verde.
5. **Push:** `git push origin main`. (Ponto de não-retorno; se preferir, deixe este passo por último e sinalize que está pronto pra push.)

## AUDITORIA PÓS (review — depois do merge)
- `git log --oneline -5 main` + `git status` — main = origin/main, árvore limpa.
- Reconfirme **381/381** e `prisma validate` na main.
- Liste o que mudou de comportamento observável (a página `/app/leaf/canal` com QR + Ofertas in-chat) e o que **não** foi provado ainda ao vivo (o **happy-path de envio** depende do pareamento físico — o `brann-confirmer` faz parse de 2 shapes presumidos da Evolution; risco de ROLLED_BACK no 1º pareamento → deixe explícito, não maquie).

## COESÃO (ressincronizar docs — a re-auditoria pegou estes defasados)
6. **`docs/ARCHITECTURE_HERMES.md`** — o cabeçalho diz *"Status: conceptual law. No code."* Isso é **falso hoje**: o runtime existe em `apps/worker/src/hermes-chat-delegate.ts`. Corrija para refletir que a lei conceitual permanece, mas o **delegate governado está implementado** (aponte o arquivo).
7. **`CHECKPOINT.md`** (topo) e **`ANDAMENTO.md`** — sincronize contagens/estado defasados (ex.: "187/187", "76/76", "10 models", "no Boundary impl") para o **atual: 381 testes · 25 models · Boundary shipped · M5b+M5c em main**. Registre a integração de hoje como entrada nova (append), sem reescrever histórico.
8. Se houver **PRD/kickoff** citando M5c como pendente, marque como **DONE (em main)**.

## Definição de pronto
- `main` contém M5b+M5c, **381/381** verde, `prisma validate` ok, api **sobe** com a migração nova aplicada, docs (Hermes/CHECKPOINT/ANDAMENTO) sincronizados, e um **resumo honesto** do que ficou provado vs pendente (envio ao vivo = pós-pareamento).
- **NÃO** faça mais nada além disso nesta fatia (sem HMAC, sem rotação, sem pricing — são as próximas). Uma fatia, um gate.
