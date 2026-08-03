# Leaf — MVP enxuto (produto)

> Decisão confirmada (Gabriel, 2026-06-22). Leaf = **Callima (WhatsApp) + painel web do cliente**.

## O produto (1 frase)
O cliente assina o Leaf → ganha a **Callima** atendendo no WhatsApp dele **+** um **painel web** onde vê e configura. Nada além disso no MVP.

## Painel (escopo, ordem de valor)
1. **Conversas/Leads** *(tela-herói)* — lista de leads capturados pela Callima (nome, empresa, necessidade, status, telefone, última msg). Read.
2. **Conexão WhatsApp** — parear número (QR Evolution) + status.
3. **Conhecimento** — cliente edita a base da Callima (oferta/FAQ/preço) → atualiza o RAG.
4. **Plano & uso** — plano, GTK/uso, assinar/gerenciar (base já feita pelo Code: pricing/GTK + assinaturas).

Fora do MVP: métricas avançadas, multi-agente, automações custom, transcrição completa no painel.

## Régua de UX — "Netflix-like" (norte, aplicar como camada sobre o core)
- **Self-serve, zero atrito:** assinar → conectar WhatsApp (QR) → Callima no ar em minutos, sem humano.
- **Valor instantâneo:** primeiro lead aparece **ao vivo** no painel = o "aha".
- **Onboarding (wizard):** 1) conectar WhatsApp via QR · 2) definir oferta/FAQ (→ RAG) · 3) "oi" de teste → Callima responde → "seu agente está vivo". WhatsApp dos dois lados (atende o cliente final; pode onboardar o dono).
- **80/20 do premium:** QR instantâneo · **feed de leads em tempo real** · first-run wizard · empty states honestos · **status ao vivo real** (honest-data vira UX: "conectado ✅", "12 leads esta semana") · design system limpo.
- **Ordem:** core confiável (Callima capta + painel mostra) PRIMEIRO; polish/onboarding self-serve DEPOIS. Não polir core frágil.

## Arquitetura (lean · governada · honest-data)
- **Tronco `ginkgo-tree` = o produto** (auth, web, billing já existem). O painel é área nova nele.
- **Bridge (decisão A):** a Callima fica no n8n e **reporta lead/conversa pra uma API do tronco** (`POST /ingest/lead`). O **tronco é a fonte da verdade**; o painel lê de lá (não do banco do n8n). Migra a Callima pro runtime do tronco quando o produto andar.
- **honest-data:** o painel mostra o estado REAL (lead/conversa/conexão) — nunca sintetizado.
- **Conhecimento:** cliente edita no painel → grava no tronco → sincroniza pro workspace AnythingLLM `callima` (o RAG). Loop fechado.
- **Auth do ingest:** token de serviço **por-org** (a Callima detém na config do n8n) → resolve a org pelo token. Nunca JWT de usuário no n8n. org sempre do JWT no painel; sem `id` no path (sem superfície cross-tenant); 404 cross-tenant.

## Fatias (sequência)
1. **[Code] Conversas/Leads + ingest** — `Lead` model (tenant-scoped) · `POST /ingest/lead` (idempotente, auth por token de org) · `GET /leads` · tela `/app/leads`. ← **primeira**
2. **[Sexta-feira/n8n] Bridge** — a Callima passa a chamar `POST /ingest/lead` ao salvar lead (hoje grava em `callima_leads`; passa a reportar pro tronco também).
3. **[Code] Conexão WhatsApp** — parear (QR Evolution) + status, por tenant.
4. **[Code] Conhecimento self-service** — editar base → sync RAG.
5. **[Code] Plano & uso** — já tem base; só expor no painel.

_Mantido pela Sexta-feira._
