# Deploy de produção — runbook (Hostinger + Cloudflare)

> Decisões (Gabriel, 2026-06-26): VPS **Hostinger** · **Cloudflare** (DNS + TLS + proxy) · domínio **`leaf.ginkgosystems.tech`** · **Stripe test** (migra pra live depois). 🔑 = ação do fundador · ⚙️ = eu/Code.

## Fase 0 — LOCAL + Cloudflare Tunnel (AGORA, até ter ticket pra VPS)
> Decisão (Gabriel): hospedar a versão **prod localmente** pros primeiros clientes; VPS quando o caixa justificar. O enabler é o **Cloudflare Tunnel**.

- **`cloudflared` (Cloudflare Tunnel):** expõe o stack local em **`leaf.ginkgosystems.tech`** — público, TLS na borda, **sem VPS, sem abrir porta, sem IP público**. (Você já tem Cloudflare → encaixa.)
- Roda o **mesmo `docker-compose.prod`** na tua máquina; o `cloudflared` (container) faz o ingress → `web` + `api` locais.
- Stripe test webhook + WhatsApp + dashboard do cliente → todos chegam pelo túnel (`leaf.ginkgosystems.tech`).
- **Migração pra VPS depois = trivial:** o mesmo compose sobe na Hostinger; só troca o ingress (túnel → Caddy) e o DNS.
- ⚠️ **Caveats honestos (é bootstrap, não produção robusta):** a máquina precisa ficar **ligada 24/7** (autostart no boot + desligar suspensão) — se ela cai, o cliente cai. Olho no recurso (16GB no limite → ~1–3 clientes antes de apertar). **Backup do volume do Postgres desde o 1º cliente.**

## Mapa de subdomínios (`ginkgosystems.tech`)
> Decisão (Gabriel, 2026-06-26). Domínio agora no **Cloudflare** (nameservers `sharon`/`west.ns.cloudflare.com`).

- **`ginkgosystems.tech` (raiz)** → **site inicial** (landing/marketing).
- **`leaf.ginkgosystems.tech`** → **dashboard LEAF** (login + app) — via **Cloudflare Tunnel → local**. ← agora.
- **`wave.ginkgosystems.tech`** → dashboard WAVE (depois, quando WAVE existir).
- **`pyre.ginkgosystems.tech`** → dashboard PYRE (depois).
- **Existentes preservados:** `www`→Vercel · `app`→ginkgo-platform (Pages) · `chat`→72.60.146.6 · `send`→Resend (email: MX/SPF/DKIM).
- **Webhooks/API:** Stripe + ingest entram pelo mesmo túnel do `leaf` (rota `/api` + `/webhooks/*` → api local), ou um `api.` dedicado — defino ao montar o túnel.

## Fase 1 — VPS (quando o caixa justificar)
### Alvo
1 VPS Hostinger rodando o **bundle PRODUTO** em Docker: tronco (**api + web + worker + Postgres/pgvector**) + **n8n Runtime** + **Evolution** (WhatsApp) + **AnythingLLM** (RAG) + **Redis**. **Cloudflare** na frente. Domínio `leaf.ginkgosystems.tech`.

## Sequência
- **A. ⚙️ [CODE] Dockerizar o tronco** — Dockerfiles (api/web/worker) + `docker-compose.prod.yml` + `.env.example` + Caddy de origem. *(prompt no chat)*
- **B. 🔑 Provisionar a VPS Hostinger** — KVM, **≥4 vCPU / 8–16GB / NVMe**, Ubuntu 22/24; instalar Docker + compose.
- **C. 🔑 Cloudflare** — adicionar `ginkgosystems.tech` → DNS **A `leaf` → IP da VPS** (proxied, nuvem laranja). TLS **Full (strict)** + **Origin Certificate** do Cloudflare instalado no Caddy (cert grátis, 15 anos, esconde o IP).
- **D. ⚙️ Migração** — `compose down` local → `pg_dump` + copia named volumes → `compose up -d` na VPS → restaura DBs.
- **E. 🔑 Secrets no `.env` da VPS** — Stripe (test) keys + webhook secret · ingest token · Resend · Evolution · OpenRouter. *(nunca no git)*
- **F. ⚙️ Webhooks públicos** — Stripe → `https://leaf.ginkgosystems.tech/webhooks/stripe` (test) · Evolution → o n8n público.
- **G. ⚙️ Smoke test self-serve** — assina com cartão de teste (outro email) → magic-link (Resend) → criar senha → tenant ativo → conecta WhatsApp → Callima atende.
- **H. (depois) 🔑 Stripe live** — ativa a conta live → troca keys + price-ids + webhook live.

## TLS com Cloudflare (o jeito limpo)
Cloudflare termina o TLS na borda (cert deles pro `leaf.`); a origem usa um **Cloudflare Origin Certificate** (Caddy serve) com mode **Full (strict)**. Sem dor de Let's Encrypt na origem + IP escondido.

## Notas
- **Stripe test** roda o funil INTEIRO (cartões de teste `4242…`) — só não move dinheiro real. Valida o self-serve sem esperar a verificação da conta live.
- Stack cabe num Hostinger KVM ~8–16GB; se apertar (Evolution + n8n + tronco + RAG), sobe o plano.
- Split de blast-radius (produto vs ops/Twenty/Postiz) fica pra depois — começa com 1 VPS (ver `infra_alvo_vps.md`).

## Quem faz o quê
- **⚙️ Code:** dockeriza o tronco (A).
- **⚙️ Eu (Sexta-feira):** runbook, config do Caddy/origem, coordenar migração (D/F/G).
- **🔑 Você:** Resend (email) · provisionar VPS (B) · Cloudflare+DNS (C) · secrets (E) · Stripe live quando quiser (H).

_Mantido pela Sexta-feira._
