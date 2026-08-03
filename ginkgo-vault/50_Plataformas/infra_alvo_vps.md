# Infra — alvo VPS (desenhar agora, deployar depois)

> Decisão (Gabriel, 2026-06-22): **MVP/receita primeiro no local**; migrar pra VPS quando o caixa justificar. Projetar desde já pra migração ser trivial.

## Hoje (local — máquina HONRADO, 16GB, Docker VM 8GB — no limite)
- **ai-stack** (docker-compose, `C:\dev\ai-stack`): n8n + Evolution + AnythingLLM + Redis + Postgres + Postiz + Temporal → runtime do agente + **Callima viva**.
- **tronco** `ginkgo-tree` (`C:\dev`): produto (api+web+db) — dev/local.
- Cofre + RAG (AnythingLLM workspace `callima`).
- **Não cabe mais nada** (Twenty/CRM fica pra depois).

## Alvo (VPS, quando migrar) — separar por blast-radius
- **Runtime / PRODUTO** (serve clientes; precisa uptime, TLS, backup):
  - tronco `api` + `web` + Postgres(+pgvector)
  - Callima/agent runtime (n8n governado) + Evolution (WhatsApp) + AnythingLLM (RAG) + Redis
- **Ops / INTERNO** (Ginkgo pra si — pode ser VPS/instância separada, menor):
  - Twenty (CRM interno) · Postiz (social) · automações internas
- **"VPS capaz de tudo":** 1 VPS robusta (ex. 8 vCPU / 16–32GB / NVMe) roda tudo; OU split 2 VPS (produto vs ops) pra isolar blast-radius. Recomendo começar com 1 boa e splitar quando crescer.
- **Borda:** domínio + TLS (reverse proxy: Caddy/Traefik) · secrets em env/secret-manager · backups (pg_dump + volumes) · observabilidade básica.

## Gatilhos de migração (quando mover)
1. **1º cliente pagante em produção** (uptime > máquina local), ou
2. Callima precisa rodar **24/7** sem depender da sua máquina, ou
3. **Vários tenants** reais (multi-tenant de verdade).
Até lá: local = dev + demo + primeiros testes.

## Prep "de graça" (manter a disciplina = migração trivial)
- ✅ Tudo container-izado, **named volumes**, fora do OneDrive (portável).
- ✅ Tronco governado (auth/billing/honest-data) = **cloud-ready por design**.
- ✅ Secrets em `.env`/credential (não hardcoded) → fácil mover.
- ⏳ **Backups** dos volumes/DB (pra migração E segurança) — montar quando subir o 1º pagante.
- Migração = `docker compose down` local → copiar `data/` + volumes → `up -d` no VPS → DNS + TLS.

## Foco atual (o que faz dinheiro — NÃO depende do VPS)
1. **Leaf — fatia Leads** (Code, em build): painel + `POST /ingest/lead`.
2. **Callima fecha venda** (pagamento): Stripe link + SyncPay Pix + loop webhook→Brann→parabéns.
3. RAG de vendas ✅ (já no ar).

_Mantido pela Sexta-feira._
