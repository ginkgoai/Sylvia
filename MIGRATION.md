# MIGRATION — Sexta-feira → Sylvia (2026-08-03)

Reorganização do centro de comando e nascimento do repo `sylvia`.

> **Adendo 2026-08-16:** OpenClaw permanece como runtime principal da Sylvia, porém Hermes **não está mais em desativação**. Ele foi reclassificado como **execution runtime governado**, subordinado à Sylvia/OpenClaw e ao Agent OS. Ver `docs/feature_sylvia_execution_fabric.md` e a decisão `ginkgo-vault/00_Cerebro/Decisoes/2026-08-16-openclaw-hermes-execution-fabric.md`.

## Renomeação

- A assistente **"Sexta-feira" passa a se chamar "Sylvia"**. Persona, constituição e boot novos na raiz (`SYLVIA.md`, `SOUL.md`, `AGENTS.md`, `CLAUDE.md`).
- A pasta local continua `C:\sexta-feira` (renomear quebraria Hermes/leaf/paths legados); o repo GitHub chama-se `sylvia`. Renomear a pasta é opcional e fica para depois da estabilização da arquitetura OpenClaw + Hermes.

## De → Para

| Antes | Agora |
|---|---|
| `hermes/` | `runtime/hermes/` |
| `memory/` (compat Hermes) | `runtime/hermes-memory-compat/` (congelado) |
| `bridges/` | `runtime/bridges/` |
| `callima/` | `runtime/callima/` |
| `db/` | `runtime/db/` |
| `dashboard-orb/` | `runtime/dashboard-orb/` |
| `.sexta_db_pw.txt` (raiz) | `runtime/.sexta_db_pw.txt` (segue fora do git) |
| Constituição rascunho (`ginkgo-vault/10_Marca/sexta-feira.md`) | Superada por `SYLVIA.md` (mantida como histórico) |
| — | `cognicao/` (memória, triagem de clippings, autonomia, heartbeat) |
| — | `empresas/` (Ginkgo: ecossistema + 10 produtos + briefs; Scale Group) |
| — | `operacao/` (contas e canais, financeiro) |
| — | `runtime/openclaw/SETUP.md` (runtime principal) |
| Hermes como cérebro da Sexta-feira | Hermes como executor subordinado da Sylvia |

`ginkgo-vault/` e `docs/` permaneceram no lugar (vault Obsidian intacto; `00_Cerebro` segue sendo a memória canônica).

## Atenção — caminhos que mudaram

Referências antigas a `C:\sexta-feira\bridges|callima|hermes|memory|db` em docs e no Hermes instalado apontam para os caminhos novos sob `runtime\`.

A arquitetura de 2026-08-03 previa retirar Hermes após a migração ao OpenClaw. Essa parte foi superada em 2026-08-16: **Hermes permanece, mas não como cérebro**. OpenClaw mantém identidade, canais, heartbeat e coordenação; Hermes executa missões autorizadas e pode delegar engenharia ao Coding Fabric (OpenCode/Codex/Claude Code).

## Fora do git (continua local)

- Segredos: `.env*`, `*.key`, `*.token`, `*.pem`, `.sexta_db_pw.txt` etc. (`.gitignore`).
- `ginkgo-vault/75_Studio/agencia-hot/vip-gabi/` — **repositório git independente** (cliente da agência); não entra no repo `sylvia`. Se quiser versionar junto no futuro: converter em submódulo ou repo privado próprio.
- `node_modules/`, caches, logs.

## Pendências pós-migração

1. **Revogar o PAT** usado no primeiro push (foi colado em chat) e criar credencial limpa para uso contínuo.
2. Rotacionar tokens antigos já expostos (Telegram bot Friday, n8n API key, n8n MCP token, AnythingLLM) — pendência herdada do STATE legado.
3. Gerar os **dossiês comerciais completos** a partir de `empresas/*/briefs_fonte/` (um por produto + ecossistema + Scale Group).
4. Instalar/estabilizar OpenClaw como runtime principal (`runtime/openclaw/SETUP.md`).
5. Reconfigurar Hermes para o novo papel de execution runtime e implementar `docs/feature_sylvia_execution_fabric.md`.
6. Integrar OpenCode ao Hermes e validar em repositório descartável antes de qualquer projeto real.
7. Preencher `operacao/CONTAS_E_CANAIS.md` (inventário real de contas).
8. Triagem do backlog de clippings (`cognicao/TRIAGEM_CLIPPINGS.md`) até zerar `00_Inbox` e depurar `20_Conhecimento/Referencias`.
9. Decidir destino definitivo de `ginkgo-vault/99_Quarentena/` (manter local-only ou depurar).
