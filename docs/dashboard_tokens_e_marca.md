# Dashboard: design tokens + Unificação de marca

## A) Prompt pro Claude Code (aplicar tokens no dashboard) — sem crédito
> Tarefa: herdar a identidade visual do site no app web do LEAF (apps/web). NÃO redesenhar.
>
> Fonte da verdade:
> - `landing page ginkgo-sale/ginkgo-ai-site-main/tailwind.config.ts`
> - `.../src/index.css` (bloco `:root` + classes utilitárias)
> - Resumo em `C:\sexta-feira\docs\ginkgo_design_tokens.md`
>
> Passos:
> 1. Ler as 3 fontes acima antes de editar (não inventar valores).
> 2. No app web do LEAF: copiar o bloco `:root` de variáveis HSL pro globals.css.
> 3. Mesclar `theme.extend` do tailwind (colors shadcn, fontFamily Inter/Space Grotesk/
>    JetBrains Mono, radius 1rem, keyframes/animation) no tailwind config do app.
> 4. Importar as 3 fontes (Google Fonts ou self-host).
> 5. Trazer utilitárias: `glass-card`, `glow-primary`, `gradient-text-primary/whatsapp/accent`.
> 6. Criar paleta semântica por agente: leaf=verde(#10b981→#22c55e), wave=azul(#2563eb),
>    pyre=laranja(#F97316), full=roxo(#7c3aed). Usar em cards/badges/CTAs.
> 7. Aplicar o tema sem mexer na lógica/estrutura dos componentes existentes.
> 8. Verificar: tsc limpo, build ok, e screenshot de 1-2 telas pra confirmar visual.
> Commits pequenos. Marca = "Ginkgo AI" (G-Tech aposentado).

## B) Checklist de unificação de marca (SUA ação — manual em cada plataforma)
Marca única: **Ginkgo AI Systems** · @handle alvo: **ginkgosystems** (onde der;
manter o mais próximo onde já existe) · domínio: **ginkgosystems.tech** ·
1 link: **linktr.ee/ginkgosystems** · logo: árvore azul (mesma em todas).

Frase-âncora (bio): "Agentes de IA sob medida — atendimento, conteúdo e tráfego
que trabalham 24/7. ginkgosystems.tech"

Por plataforma (nome de exibição + @handle se der + bio + foto + capa + link):
- [ ] Instagram (@ginkgo.ai) → padronizar bio/foto/capa/link; avaliar handle.
- [ ] TikTok (@ginkgo.ai.systems) → bio/foto + tirar "G-Tech".
- [ ] X (@ginkgo_systems) → **tirar "G-Tech" da bio**, padronizar.
- [ ] Facebook (Ginkgo AI Systems) → bio/foto/capa + link.
- [ ] LinkedIn (Ginkgo AI Systems) → bio/foto/capa + serviços.
- [ ] YouTube → nome/foto/capa + link (canal lofi entra na fase 2).
- [ ] Linktree (linktr.ee/ginkgosystems) → revisar todos os links → site.
- [ ] Aposentar "G-Tech" em TODAS as bios/descrições.

Regra: mesma foto (árvore azul), mesma frase-âncora, mesmo link em todas.
```
