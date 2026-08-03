# Site institucional Ginkgo — Spec (Claude Code)

Repo: `GITS FONTE/landing page ginkgo-sale/ginkgo-ai-site-main` (Vite + Tailwind v3 + shadcn).
Repo SEPARADO do LEAF — sem conflito com o Inbox. Tema/tokens: `ginkgo_design_tokens.md`.
Roster: `roster_agentes_ginkgo.md`. Posicionamento/loop: `ecossistema_ginkgo_visao.md`.

## Direção visual (aprovada)
- **Híbrido**: nav + hero + CTA final em **dark navy**; seções de conteúdo (agentes, como
  funciona, planos) em **claro (branco / azul-claro #F5F8FF)**. Mobile-first, responsivo.
- Tipografia: Space Grotesk (títulos) + Inter (corpo). Primário azul #2563eb / roxo #6d5efc.
- Cores por agente: Pyre/Nyra=âmbar #f59e0b · Wave/Alfred=azul #2563eb · Leaf/Brann=verde #16a34a.

## Apresentação dos agentes (aprovado: "produtos em destaque, personas como rosto")
Cards = produtos (Leaf/Wave/Pyre); cada card mostra o piloto: **Nyra** (Pyre), **Alfred**
(Wave), **Brann** (Leaf). **Callima** = "a sua secretária de IA" na página do Leaf.

## Páginas
1. **Home** (`/`): nav → hero dark → seção "Os agentes" (3 cards c/ piloto) → "Como funciona"
   (loop: Nyra cria → Alfred anuncia → Lead WhatsApp → Callima converte → CRM/pago → Alfred
   atribui) → teaser de Planos (4 cards) → faixa CTA dark + footer. (Ver mock híbrido aprovado.)
2. **/planos**: 4 produtos (Leaf $79/$199/$499 · Wave $99/$249 · Pyre $99/$249 · Full $599),
   toggle mensal/anual (−17%), bloco de top-ups GTK, explicação do modelo de tokens.
3. **Landings de produto (SEO — slug = keyword):**
   - `/atendente-ia-no-whatsapp` (Leaf · Callima · Brann)
   - `/gestor-de-trafego-ia` (Wave · Alfred)
   - `/agente-de-conteudo-ia` (Pyre · Nyra + avatar HeyGen)
   Cada landing: H1 = a keyword, subcopy, benefícios (checklist), prints (placeholder),
   "casos de uso", FAQ, CTA duplo (Teste grátis / Falar no WhatsApp).

## Técnico
- Componentizar: Nav, Hero, AgentCard, HowItWorks (loop), PlanCard, CTASection, Footer.
- Dados de planos/agentes num arquivo de config (TS) reaproveitável entre home/planos/landings.
- **SEO**: <title>/meta description por página, Open Graph, **JSON-LD** (Organization +
  Product por landing), sitemap.xml, canonical, hreflang pt-BR/en (mercado global).
- **i18n**: textos preparados pra PT/EN (vende global; site em PT agora, EN depois).
- CTAs: "Começar" → signup do app (URL do dashboard); "Falar no WhatsApp" → wa.me (a própria
  Callima atende). Sem inventar integração — usar URLs configuráveis em env/config.
- Acessibilidade (contraste AA), performance (imagens otimizadas, lazy), 100% responsivo.
- NÃO hardcodar cores soltas — usar os tokens do tailwind.config do repo (estender se faltar).

## Escopo
- v1: Home + /planos + 1 landing piloto (`/atendente-ia-no-whatsapp`). Demais landings = v2.
- v2: landings de Wave e Pyre, versão EN, blog, prova social/depoimentos reais.

## Aceite
- Home híbrida fiel ao mock; /planos com os 8 preços + toggle anual + top-ups; 1 landing SEO
  com H1 keyword + JSON-LD; responsivo mobile; build/lint OK; Lighthouse SEO ≥ 90.

## Dependências
- URL do app/signup e número WhatsApp (config). Prints reais das telas (quando o dashboard
  estiver pronto — usar placeholders até lá).
