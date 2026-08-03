## Visão geral

Landing page single-page em `/` com estética de museu contemporâneo: muito branco, tipografia Playfair Display italic contrastando com Inter e JetBrains Mono, seções generosas em respiro, animações fade-up suaves e portfólio como peça central. As fotos enviadas entram como prova de capacidade técnica — sem citar marcas de terceiros.

## Stack (adaptada)

TanStack Start + React 19 + TypeScript + Tailwind v4 + shadcn + Framer Motion + Embla Carousel + React Hook Form + Zod + Sonner + Lucide. Equivalente completo ao pedido de Next.js/Framer Motion.

## Tokens de design (do protótipo escolhido)

- Cores: `--background #fafafa`, `--foreground #121212`, `--muted #71717a`, `--border #e4e4e7`, superfície escura `#0a0a0a`.
- Fontes carregadas via `<link>` no `__root.tsx`: Playfair Display 700 italic (display), Inter 400/500 (corpo), JetBrains Mono 400 (kicker/labels).
- Easing: `cubic-bezier(0.16, 1, 0.3, 1)`; keyframe `fade-up` global.
- Botões primários: preto sólido, texto branco, uppercase tracking-widest, sem raio (sharp corners fiéis à direção).

## Assets

Upload de todas as fotos enviadas (2 lotes: Mickey/Minnie, elfos, Papai Noel, Buda, baleias, mangue, trenó, cogumelos, Ferrero/Arcor/Lacta bunny, cookies Bauducco, esqueleto de dinossauro, painéis Celebra 2025, EPS studio) via `lovable-assets create` a partir de `/mnt/user-uploads/`, gerando pointers `.asset.json` em `src/assets/portfolio/`. Cada foto recebe categoria (Personagens, Corporativo, Esculturas, Natal, Páscoa, Temáticos, Institucional, Eventos) e alt genérico focado em técnica ("Escultura em EPS acabada em dourado", "Personagem gigante em fibra de vidro", etc.), sem nomes de marcas.

## Estrutura de arquivos

```text
src/
  routes/
    index.tsx                 ← landing (head SEO + JSON-LD)
  components/
    landing/
      Nav.tsx                 mix-blend-difference fixo
      Hero.tsx                título + 2 CTAs + hero image reveal
      Clients.tsx             faixa de logos (placeholders prontos)
      Stats.tsx               5 contadores animados (IntersectionObserver + framer)
      Services.tsx            grid 3x3 com ícones Lucide
      Portfolio.tsx           masonry + filtro categoria + Lightbox
      Lightbox.tsx            Dialog shadcn + Embla navegação
      Process.tsx             timeline 8 etapas (bg preto, borda-l)
      Differentiators.tsx     grid 4x2
      BeforeAfter.tsx         placeholder preparado (2 slots)
      QuoteCta.tsx            CTA "Seu projeto merece sair do papel" + WhatsApp
      QuoteForm.tsx           RHF+Zod, Sonner toast, preparado p/ CRM
      Faq.tsx                 shadcn Accordion (7 perguntas)
      Footer.tsx              contato, redes, mapa embed
      WhatsAppFab.tsx         botão flutuante persistente
  data/
    portfolio.ts              array tipado das fotos + categoria
    services.ts, process.ts, faq.ts, differentiators.ts
```

## Seções (fiel à direção)

1. **Nav fixa** mix-blend-difference, monotype JetBrains "Zavan / Scenography" + links Portfolio/Processo/Contato.
2. **Hero** centralizado: kicker "Curadoria de Espaços" · H1 Playfair italic "Cenografia que transforma ideias em experiências inesquecíveis" · 2 CTAs (Solicitar orçamento âncora, Ver portfólio âncora) · imagem 21:9 grande abaixo com Embla auto-slide das melhores fotos.
3. **Clientes** — faixa cinza clara com 5 slots itálicos placeholder ("Marca 01"…), pronto para trocar por logos.
4. **Números** — 5 contadores (Projetos, Anos, Clientes, Estados, Peças) animados on-scroll.
5. **Serviços** — 9 cards (Esculturas EPS, Personagens gigantes, Cenografia corporativa, Ambientações temáticas, Fachadas, Displays, Cenários para eventos, Projetos especiais, Produção personalizada), cada um com ícone Lucide + descrição curta.
6. **Portfólio** — masonry 12-col responsivo com peças em tamanhos variados (4/8/4 col), filtro por categoria em JetBrains Mono, Lightbox com navegação teclado/gesto. Todas as fotos enviadas distribuídas nas 8 categorias.
7. **Processo** — bloco preto, timeline 8 etapas (Briefing → Instalação) com número, título, descrição.
8. **Diferenciais** — grid 4x2 minimal, sem ícones pesados.
9. **Antes e Depois** — 2 slots preparados com legenda "Em breve".
10. **CTA + Formulário** — título Playfair "Seu projeto merece sair do papel." + formulário (nome, empresa, e-mail, WhatsApp, tipo de projeto select, mensagem) validado com Zod, envia via `console.log` + Sonner (pronto para plugar webhook CRM depois), botão WhatsApp secundário.
11. **FAQ** — Accordion shadcn com as 7 perguntas.
12. **Footer** — 3 colunas: contato (WhatsApp/email/endereço placeholder), redes (Instagram, Facebook, LinkedIn), mapa (iframe Google Maps placeholder). Copyright + selos.
13. **FAB WhatsApp** — círculo verde discreto, canto inferior direito, aria-label.

## SEO e performance

- `head()` em `src/routes/index.tsx`:
  - title "Zavan Cenografia — Esculturas, Cenografia e Ambientações Personalizadas"
  - description ~155 chars focado em orçamento nacional
  - og:title, og:description, og:type=website, og:url=/, twitter:card=summary_large_image
  - canonical `/`
- `__root.tsx`: mantém defaults + Organization JSON-LD (Zavan Cenografia, sameAs Instagram/Facebook/LinkedIn, contactPoint WhatsApp).
- `index.tsx` scripts: FAQPage JSON-LD (7 Q&A) + BreadcrumbList.
- Imagens: `loading="lazy"`, `decoding="async"`, `width`/`height` explícitos, alt descritivo por técnica.
- H1 único no hero; h2 por seção; h3 em cards.
- Preload da fonte Playfair e imagem hero via `head().links`.
- Sem `og:image` no build inicial (evita placeholder ruim); hosting injeta screenshot.

## Conversão

- 4 CTAs distribuídos: hero, meio (após portfólio), CTA principal, FAB permanente.
- Formulário com validação inline e mensagem de sucesso Sonner.
- Links WhatsApp com `https://wa.me/` + número placeholder editável em `data/contact.ts`.
- Hooks preparados: `onQuoteSubmit` isolado para plugar CRM/GA/Meta Pixel depois — comentário TODO explícito.

## Animações

- `motion.div` com `whileInView` `fade-up` sequencial (stagger 0.08s) em títulos e cards.
- Contadores animados via hook `useCountUp` disparado no IntersectionObserver.
- Hero slider auto-play 4s, pausa on-hover.
- Hover cards: `scale-[1.02]` + revelação de legenda inferior.
- Portfolio filter com `AnimatePresence` + layout animation.

## Acessibilidade

Contraste AA (preto/branco garantem), aria-labels em ícones-only (FAB, nav mobile), foco visível, alt em todas imagens, semantic `<main>`/`<section>`/`<nav>`/`<footer>`.

## Fora de escopo (placeholders prontos)

- Logos reais de clientes (5 slots).
- Fotos "Antes e Depois" (2 slots).
- Número WhatsApp, e-mail, endereço, coordenadas do mapa, handles das redes — todos centralizados em `src/data/contact.ts` para você editar depois.
- Integração real CRM/GA4/GTM/Meta Pixel — estrutura pronta, chaves entram quando você fornecer.

Depois que você aprovar, executo tudo em um passo: upload dos assets, criação dos componentes, wiring do SEO/JSON-LD e verificação do build.