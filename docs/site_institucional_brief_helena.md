# Ginkgo — Brief do Site Institucional (inspirado no Helena CRM)

Estudo de helenacrm.com (home + páginas de produto) → o que adaptar pra Ginkgo.
NÃO copiar copy/visual deles; copiar a **estrutura e a estratégia**, com identidade
Ginkgo (azul/branco + dark navy; agentes Leaf/Wave/Pyre/Full).

## O que o Helena faz muito bem (e devemos imitar)
1. **Landing page por produto/keyword (SEO).** Eles têm uma página focada por termo de
   busca: /agente-de-ia-para-whatsapp, /crm-integrado-com-whatsapp,
   /sistema-de-atendimento-whatsapp, /receba-pagamentos-pelo-whatsapp. Cada uma com
   hero + benefícios + prints + casos de uso + FAQ + CTA. → **maior fonte de tráfego orgânico.**
2. **Mega-menu por categoria** (Produtos → CRM e Vendas / Atendimento / Automações & IA).
3. **Prova social forte:** logos de clientes, badges (Meta Business Provider, AWS),
   números (6000+ clientes, 52 mil usuários, 1,5 bi msgs/ano), página de Status.
4. **CTA duplo:** "Teste Grátis" (self-serve) + "Falar com especialista/Ver demonstração" (vendas).
5. **Seções de confiança:** estabilidade/uptime, portal de privacidade (LGPD), FAQ accordion.
6. **Mobile-first / responsivo** de ponta a ponta.

## Estrutura da HOME (adaptada Ginkgo)
1. Top nav: logo Ginkgo + mega-menu **Produtos** (Atendimento=Leaf/Callima · Conteúdo=Pyre ·
   Tráfego=Wave · Ecossistema=Full) + Recursos + Planos + **Entrar** + **Teste Grátis**.
2. Hero: badge + H1 ("Agentes de IA que atendem, vendem e crescem seu negócio 24/7")
   + subcopy + 2 CTAs (Teste Grátis / Ver demonstração) + ilustração (árvore/holograma).
3. Faixa de prova social (logos de clientes + "+X empresas").
4. **3 cards de solução**: Atendimento (Leaf), Conteúdo (Pyre), Tráfego (Wave) — ícone+título+texto.
5. Blocos de feature alternados (print + bullets): Inbox/CRM, Funil conversacional, Mídia.
6. "Como funciona na prática" (passo a passo / vídeo demo).
7. Integrações (WhatsApp/Meta, n8n, APIs).
8. Teaser de Planos (Leaf/Wave/Pyre/Full) → leva pra /planos.
9. Confiança: segurança/LGPD + estabilidade + (futuro) status.
10. FAQ (accordion). 11. Footer rico (Soluções, Recursos, Segurança, social, badges).

## Landing por produto (SEO) — criar uma por agente
Slugs keyword-rich (espelhando a tática do Helena):
- /atendente-ia-no-whatsapp  (Leaf/Callima)
- /agente-de-conteudo-ia      (Pyre)
- /gestor-de-trafego-ia       (Wave)
- /crm-no-whatsapp            (o CRM do dashboard)
Cada landing: Hero (H1 = a keyword) → benefícios → prints do produto → casos de uso
("onde faz diferença") → FAQ → CTA. Isso alimenta o Content Engine (Pyre) e o SEO.

## Identidade (Ginkgo, NÃO Helena)
- Reusar os tokens já extraídos: dark navy (#0B0F1C→#05070E), primary azul #2563eb→roxo
  #7c3aed, branco; cores por agente Leaf=verde / Wave=azul / Pyre=laranja / Full=roxo.
- Suportar **light + dark** (o Helena usa `color-scheme: light dark`). Hoje a Ginkgo é
  só dark — vale ter um modo claro (azul/branco) p/ o site institucional.
- Tipografia: Space Grotesk (títulos) + Inter (corpo) — já definido.

## Confiança / conversão (copiar a tática)
- Badge "Integração Oficial Meta" quando o portfólio BR sair.
- Portal de Privacidade/LGPD + página de Status (temos o uptime do ai-stack).
- CTA duplo em todo lugar: Teste Grátis 14d + Falar no WhatsApp (a própria Callima!).
- Prova social: começar com cases reais conforme fecharmos clientes.

## Responsividade
- Tudo mobile-first (maioria do tráfego BR é mobile). Validar dashboard + site no celular.

## Recomendação de execução
1. Repaginar a HOME do site (ginkgosystems.tech) nessa estrutura — mock no Claude Design.
2. Criar as 3–4 landings de produto (SEO) — reaproveitam o Content Engine depois.
3. Alinhar o /pricing (dashboard) e a /planos (site) com Leaf/Wave/Pyre/Full.
4. Dashboard: manter dark navy; garantir responsivo; preencher telas vazias.
