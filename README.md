# Sylvia

Cognição versionada da **Sylvia** — inteligência executiva da holding do fundador (Ginkgo AI Systems + Scale Group + operação pessoal autorizada). Sucessora da "Sexta-feira".

**Divisão de papéis:** Sylvia pensa e dirige como CEO; o fundador opera e decide como dono. Ações externas, gasto e publicação passam por gates de aprovação.

## Comece por aqui

1. **`SYLVIA.md`** — a constituição (fonte única).
2. `AGENTS.md` / `SOUL.md` / `CLAUDE.md` — boot por runtime (OpenClaw, persona, Claude).
3. `cognicao/` — protocolos: memória, triagem de clippings, autonomia, heartbeat.
4. `ginkgo-vault/00_Cerebro/` — memória canônica viva.

## Mapa

| Pasta | Conteúdo |
|---|---|
| `cognicao/` | Protocolos da mente: memória, clippings, autonomia, heartbeat. |
| `empresas/` | Camada de negócio: Ginkgo (ecossistema + 10 produtos + briefs) e Scale Group. |
| `operacao/` | Contas e canais, protocolo financeiro. |
| `ginkgo-vault/` | Biblioteca e memória (Obsidian): cérebro, inbox de clippings, marca, conhecimento, estratégia, conteúdo, plataformas, financeiro, studio/agência, quarentena. |
| `runtime/` | Executável: setup do OpenClaw (alvo), legado Hermes, bridges, Callima, db, dashboard-orb. |
| `docs/` | Specs e auditorias técnicas históricas. |

## Runtime

- **Alvo:** OpenClaw (canais Telegram/WhatsApp, heartbeat, skills) — `runtime/openclaw/SETUP.md`.
- **Oficina:** Claude Cowork / Claude Code sobre este repo.
- **Automação:** stack Docker `leaf` (n8n, Postgres, Redis, Evolution, AnythingLLM).
- **Legado:** Hermes Agent em desativação — histórico em `MIGRATION.md`.

## Regras de ouro

- Segredos e PII jamais entram neste repo (`.gitignore` cobre os padrões; não enfraquecer).
- Clipping novo entra por `ginkgo-vault/00_Inbox/` e só vira memória oficial via triagem.
- Decisão canônica exige confirmação do fundador e registro em `ginkgo-vault/00_Cerebro/Decisoes/`.
