# Auditoria de estado — LEAF / ginkgo-tree (2026-06-27 ~02:30)

> Checada ao vivo (docker, git, psql, health) — não de memória. honest-data.

## 1. Infra (containers) — tudo de pé ✅
| Container | Estado | Papel |
|---|---|---|
| `ginkgo-postgres` | Up 32h (healthy) | DB do tronco (LEAF) |
| `ginkgo-redis` | Up 32h (healthy) | filas/BullMQ do tronco |
| `ai-stack-n8n` | Up 6h | casa da Callima |
| `ai-stack-evolution` | Up 10h | gateway WhatsApp |
| `ai-stack-postgres` | Up 5d (healthy) | DB do n8n |
| `ai-stack-redis` | Up 5d (healthy) | — |
| `ai-stack-anythingllm` | Up 5d (healthy) | RAG |
| `ai-stack-postiz` | Up 5d | social posting (Pyre futuro) |
| `ai-stack-temporal` | Up 5d | workflow engine |

## 2. Callima (o que fatura) — VIVA ✅
- `callima_active = true` · última execução **26/06 18:10** · **17 execuções/24h** — atende, qualifica, manda link, agenda.

## 3. Tronco (git) — main vs Brann
- **`main` @ `0c00384`** (UI polish). Árvore limpa.
- **`feat/brann-onboarding` @ `8a3d89d`** — Brann/Hermes M4-01 **commitado e verde (171/171)**, mas **1 commit À FRENTE da main → AINDA NÃO MERGEADO.** ⬅️ ação pendente.
- Mergeado na main (linha do tempo): assinaturas+GTK → painel leads+ingest → Payment Links → /planos BRL → billing hardening → appointment bridge → ofertas registry → prod dockerizada → prod local (cloudflared) → CRM imersão → UI polish.

## 4. API / Web
- **API `:3333` = healthy** (`db/redis/queue: ok`).
- **Web `:3000` = DOWN** — você vê o dashboard pela preview do Code (ok pra dev). Subir `:3000` limpo só pra gravar a demo.

## 5. Dados (org Ginkgo `ad8d6fc8`)
`leads=9` · `conversations=12` (só 3 eram seed → 9 reais da Callima) · `chat_messages=29` · `offers=5` · `appointments=2` · `agent_profiles=3` · `pipelines=3` · `secrets=14` (cofre).

## 6. Onde paramos (resumo)
O **produto está vivo**: Callima atende no WhatsApp, fecha venda (Payment Links), joga lead no CRM (bridge), agenda no Google Calendar — tudo honest-data. Dashboard LEAF com Inbox/CRM/Agenda/Ofertas/Planos, responsivo. **Última fatia (Brann/Hermes) está pronta e verde, só falta mergear.**

## 7. Bandeiras honestas (gaps)
- 🔴 **Brann não mergeado** (1 commit à frente) — mergear `feat/brann-onboarding` → main.
- 🟡 **Egress allowlist é decorativo** [high, doc backend] — só loga, não bloqueia. Endurecer antes de prod robusta.
- 🟡 **Túnel Cloudflare não está no ar** (login social falhou) — retry pro funil público.
- 🟡 **Web :3000 down** — subir limpo pós-Brann pra gravação.
- ⚪ 17 branches locais stale (já mergeadas) — limpeza cosmética.

## 8. Próximos passos (ordem)
1. **Mergear Brann → main** + subir `:3000` limpo.
2. **(você) Gravar a demo** (~2 min, motion design).
3. **Funil real:** retry túnel Cloudflare (`TUNNEL_TOKEN`) → preencher `.env` prod → `compose up` + smoke test self-serve.
4. **Pós-lançamento:** migração Callima n8n → Hermes (strangler-fig, ver `callima_migracao_hermes.md`) + endurecer egress.

_Auditado pela Sexta-feira._
