# Ginkgo AI — Visão do Ecossistema (Leaf · Wave · Pyre)

Consolida os 3 briefs (Leaf vs Helena, Pyre vs PlaySquad, Wave vs Utmify) numa visão única:
como os agentes se conectam, vendem juntos e por que isso é defensável.

## A tese
Hoje a PME compra ferramentas SOLTAS: um CRM-WhatsApp (Helena), um estúdio de conteúdo
(PlaySquad), um tracker de tráfego (Utmify) — que não conversam entre si. A Ginkgo entrega
os três como **agentes de IA integrados** sobre uma base única (mesmo banco, mesma conta,
mesma governança). O valor não é ter os 3 — é eles **fecharem o loop** juntos.

## Os 3 agentes (corpos) + a espinha
- **Pyre (Conteúdo)** — atrai: gera conteúdo, clipes, voz, descobre tendências (vs PlaySquad).
- **Wave (Tráfego)** — escala: anuncia, atribui venda→anúncio, otimiza ROAS (vs Utmify).
- **Leaf/Callima (Atendimento+CRM)** — converte: atende no WhatsApp, qualifica, agenda,
  cobra, gerencia o funil (vs Helena).
- **Espinha**: governança **Laplace/Hermes** (HITL, kill-switch, auditoria), **GTK**
  (tokens compartilhados), e a **Sexta-feira** orquestrando na operação.

## O loop fechado (o diferencial que ninguém faz)
Pyre cria a peça → Wave roda o anúncio com UTM → o clique vira **lead no WhatsApp** →
Callima atende e qualifica → vira **card no CRM (Leaf)** → fecha e **paga (payments)** →
Wave **atribui a venda de volta ao anúncio/criativo** (server-side/CAPI) e otimiza →
Pyre vê pelo Radar/Trends o que converteu e **cria mais do que funciona**.
Tudo no mesmo banco, mesma conta, com HITL. Helena/PlaySquad/Utmify só veem um pedaço.

## Base compartilhada (por que é barato manter e difícil de copiar)
- **1 banco** (Supabase): organizations, leads, conversations, payments, agents, media,
  token_wallets... os 3 agentes leem/escrevem nas MESMAS tabelas → dados cruzam de graça.
- **1 carteira GTK** por org: créditos compartilhados entre Pyre/Wave/Leaf (modelo Manus/
  PlaySquad). Cliente não gerencia 3 saldos.
- **1 governança**: HITL/kill-switch/auditoria (Laplace) valem pra qualquer ação de qualquer
  agente. Confiança = diferencial vs ferramentas soltas.
- **1 conta/login/cobrança** (Stripe USD, multi-moeda, global).

## Empacotamento comercial (já definido)
- Produtos: **Leaf** $79/$199/$499 · **Wave** $99/$249 · **Pyre** $99/$249 · **Full** $599
  (bundle com pool GTK compartilhado). Top-ups de GTK. Anual −17%.
- Porta de entrada típica: **Leaf** (dor mais aguda = atendimento). Upsell natural → Wave
  (escalar tráfego) e Pyre (alimentar de conteúdo) → **Full** quando os 3 se provam.
- Venda global em USD; Pix add-on regional BR.

## Posicionamento (1 frase)
"A Ginkgo é a operação de IA que **atrai (Pyre), escala (Wave) e converte (Leaf)** — agentes
integrados, governados e cobrados por uso, no lugar de 3 ferramentas soltas que não se falam."

## Roadmap de execução (consolidado)
1. **P0 LEAF** (em curso): Inbox → Funil/Kanban → Planos tokenizados/pricing.
2. **Canais oficiais + cobrança**: WhatsApp Cloud API (Meta) + Stripe USD. (depende do founder)
3. **Wave MVP**: UTM/atribuição → Dashboard ROAS → CAPI → Optimize (usa Meta Marketing API).
4. **Pyre MVP**: Voice → Trends → Clips → Radar (Estúdio em /studio).
5. **Site institucional + /planos** (estrutura Helena-grade) e onboarding.
6. **Full/bundle + White Label** (futuro).

## Papéis (operação vs construção)
- **Operação** (rodando pro cliente): Sexta-feira orquestra; Callima/Leaf, Wave e Pyre executam;
  humano só no HITL.
- **Construção** (evoluir a plataforma): humano + agente de código supervisionado (Laplace).

Docs-fonte: helena→`gap_helena_vs_leaf.md`, pyre→`pyre_funcionalidades_playsquad.md`,
wave→`wave_funcionalidades_utmify.md`, pricing→`pricing_tokenizado_ginkgo.md`,
meta→`meta_portfolio_requisitos.md`, site→`site_institucional_brief_helena.md`.


---
## Roster de agentes (ver roster_agentes_ginkgo.md)
Leaf→**Brann** · Pyre→**Nyra** · Wave→**Alfred** (personas internas de produto).
**Callima** = secretária PERSONALIZÁVEL do cliente (client-facing, sobre o Leaf).
Sexta-feira orquestra; Laplace/Hermes governa. Pyre+HeyGen = vídeos de influencer de IA (avatar).
