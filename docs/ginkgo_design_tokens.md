# Ginkgo AI — Design Tokens (extraídos do site)

Fonte: `landing page ginkgo-sale/ginkgo-ai-site-main` (tailwind.config.ts + src/index.css).
Marca: **Ginkgo AI** (G-Tech aposentado). Tema escuro premium.
Objetivo: o **dashboard LEAF reusa estes mesmos tokens** → site, assinatura e app
com a mesma cara. shadcn/ui já é a base nos dois (components.json).

## Cores (HSL — convenção shadcn)
- background: 228 40% 4%   | foreground: 0 0% 100%
- card/popover: 228 40% 5% | border: 0 0% 12% | input: 228 40% 6%
- primary: 230 80% 60% (azul) | primary-foreground: 0 0% 100%
- secondary: 270 80% 55% (roxo)
- accent: 43 74% 49% (gold) | accent-foreground: 230 50% 2%
- muted: 230 20% 15% | muted-foreground: 220 15% 55%
- destructive: 0 84% 60% | ring: 230 80% 60%
- neon.cyan: 191 100% 50% | neon.blue: 217 91% 60% | gold.light: 43 74% 65%
- radius: 1rem (lg). md = radius-2px, sm = radius-4px

## Fundo
- body gradient: linear-gradient(to bottom, #0B0F1C, #070A14, #05070E)

## Tipografia
- sans (corpo): **Inter**
- display (títulos h1–h6): **Space Grotesk**
- mono: **JetBrains Mono**

## Efeitos-assinatura (reusar no dashboard)
- `glass-card`: rgba(255,255,255,0.04) + blur(24px) + border rgba(255,255,255,0.08)
  + radius 1rem + sombra; hover: levanta 4px + borda mais clara.
- `glow-primary` (botão): gradient #2563eb→#7c3aed, peso 600; hover: lift + glow azul.
- gradient-text: primary #2563eb→#7c3aed | whatsapp #10b981→#22c55e | accent gold.
- Animações: fade-in, float, glow-pulse, shimmer, particle (já definidas no config).

## Paleta por agente (do pricing — semântica de produto)
Usar como cor-tema de cada produto (cards, badges, CTAs):
- **Leaf** (Atendimento): verde — #10b981 → #22c55e (= gradient whatsapp). 
- **Wave** (Tráfego): azul — primary #2563eb / neon.blue.
- **Pyre** (Conteúdo): laranja — sugerido #F97316 (não há var no CSS; padronizar).
- **Full** (Ecossistema): roxo — secondary #7c3aed.

## Como aplicar no dashboard (LEAF) — pro Claude Code
1. Copiar o bloco `:root` de variáveis (cores acima) pro `index.css`/`globals.css` do app web.
2. Copiar o `theme.extend` do tailwind.config (cores, fontFamily, radius, keyframes/animation).
3. Importar as fontes (Inter, Space Grotesk, JetBrains Mono).
4. Trazer as classes utilitárias: `glass-card`, `glow-primary`, `gradient-text-*`.
5. Definir `agent` palette (leaf/wave/pyre/full) como tokens semânticos reutilizáveis.
6. NÃO redesenhar — só herdar. Dashboard = mesma linguagem visual do site.

Repo do site (local): `...\GITS FONTE\landing page ginkgo-sale\ginkgo-ai-site-main`
Repo do dashboard: `...\GITS FONTE\ginkgo-dashboard` (e/ou apps/web do leaf).
