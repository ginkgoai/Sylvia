# Ginkgo — Presença Digital + Front (Estratégia)

## Princípio mestre: 1 núcleo de conteúdo → muitos formatos
NÃO rodar 9 pipelines independentes (entropia alta, insustentável solo).
Rodar **1 "cérebro de conteúdo"** (tema/insight da semana) que **atomiza** em
formatos por canal. 1 ideia →
- carrossel (IG) + Reel/Short/TikTok (vídeo curto) + thread (X) +
  post (LinkedIn) + trecho (Newsletter).
As pastas do n8n viram **adaptadores de saída** desse núcleo, publicando via
**Postiz** (já no ar) — não 9 cérebros separados.

## Cada canal tem um JOB (estágio do funil)
Funil: Atrair → Engajar/Educar → Provar/Confiar → Converter → Reter.

| Canal | Job | Estágio | Formato | Métrica-norte |
|---|---|---|---|---|
| TikTok/Reels/Shorts | atrair, descobrir | topo | vídeo curto | novos seguidores/views |
| Instagram (feed/carrossel/stories) | educar, "plantar possibilidade" | meio | carrossel/story | saves/shares/replies |
| X (Twitter) | relevância no nicho, novidades | meio | thread/post | impressões/cliques |
| Newsletter | audiência PRÓPRIA (não alugada) | meio→fundo | e-mail | open/click, lista |
| LinkedIn | prova/portfólio B2B | fundo | case/post | leads B2B/DMs |
| YouTube (lofi Ginkgo) | mundo de marca, always-on | topo/brand | live 24/7 | brand affinity |
| WhatsApp (Callima) + comunidade | converter + reter | fundo | 1:1 + grupo | conversas→assinatura |

## Prioridade (solo + pré-receita): foco em 3, presença nos outros
Acender tudo junto mata você. Ordem de ROI pra B2B de automação IA:
1. **LinkedIn** — é onde seu COMPRADOR B2B está. Maior intenção. Portfólio +
   prova social ("fizemos X com IA"). Provável canal de maior ROI direto.
2. **Instagram + Reels/TikTok** (mesmo motor) — volume e descoberta; educa e
   "planta possibilidade". Topo→meio.
3. **Newsletter** — audiência PRÓPRIA (você não depende de algoritmo). Estratégico
   a longo prazo; começa pequena.
- **X** = secundário, baixo esforço (repurpose de threads).
- **YouTube lofi** = aposta de marca (ver tradeoff abaixo) — só quando barato/automatizado.
- **Facebook** = presença mínima (repost via Postiz, não investir).
- **Discord/Comunidade** = quando houver gente pra reunir (fundo de funil/retenção).

## Consistência de marca (corrigir JÁ — barato, alto impacto de confiança)
Hoje os perfis estão **fragmentados**: ginkgo.ai (IG), ginkgo.ai.systems (TikTok),
ginkgo_systems (X), Ginkgo AI Systems (FB/LinkedIn), ginkgosystems.tech (site),
G-Tech aparecendo junto. Para uma marca isso confunde e derruba confiança.
- Unificar: **nome** ("Ginkgo AI Systems"), **@handle** (escolher 1 padrão e
  igualar onde der), **bio** (mesma frase-âncora), **logo** (árvore azul),
  **1 link** (Linktree → site).
- Decidir o papel do "G-Tech": submarca ou aposentar. Uma marca só comunica melhor.

## YouTube lofi (Ginkgo) — o tradeoff honesto
A ideia é boa de MARCA (mundo/atmosfera Ginkgo, always-on), mas:
- É jogo LENTO, alto esforço de produção, baixa conversão direta. Não é motor de lead.
- Só vale se **barato de rodar** (visual gerado + trilha licenciada/seleção + live 24/7)
  e se você curte. Senão, vira peso. Sugestão: tratar como "fase 2", depois que
  LinkedIn+IG+Newsletter estiverem girando.

## Arquitetura n8n (reduzir entropia das 9+ pastas)
Hoje: X / TikTok / WhatsApp / Newsletter / LinkedIn / IG / Facebook / YouTube /
Discord / ADS — pastas separadas = 9 cérebros.
Alvo: **Content-Core → Postiz** (+ poucos especialistas):
- **1) Content-Core (n8n)**: gera o tema da semana + ângulos + copy base +
  pede assets (imagem/carrossel/vídeo). Governado pela marca (tom, pilares).
- **2) Atomizador**: deriva os formatos por canal a partir do core.
- **3) Postiz** (já no ar): publica/agenda em IG, X, LinkedIn, FB, TikTok, etc.
  → colapsa a maioria das pastas de "publisher" numa só integração.
- **4) Especialistas que ficam fora do Postiz**: YouTube (live/render), Newsletter
  (Resend/lista), Discord (bot/comunidade), ADS (Wave — tráfego pago).
- Mapeia direto nos agentes do site: **Wave**=tráfego/ADS, **Pyre**=conteúdo
  (Content-Core+Atomizador), **Leaf/Callima**=atendimento. Ou seja, a presença
  digital É o show-room dos próprios produtos.

## Front: 1 design system (site + dashboard + assinatura)
Já existe identidade no site (ginkgosystems.tech): tema escuro, árvore azul, e
**cores por agente** (Leaf=verde, Wave=azul, Pyre=laranja, Full=roxo).
- Codificar isso em **tokens** (cores, tipografia, espaçamento, raios) e o
  **dashboard LEAF reutiliza os mesmos tokens** → site, assinatura e app com a
  mesma cara. Não redesenhar: extrair o que já existe e padronizar.
- Assinatura: o site já tem o pricing (Leaf 449 / Wave 1199 / Pyre 899 / Full 2497).
  O fluxo "Assine já" deve cair no cadastro do dashboard (Supabase auth) → trial 14d
  → ativa agente por 1 clique (já é a promessa do site). Front do dashboard segue
  o mesmo design system.

## Sequência sugerida (enquanto sem crédito OpenRouter)
1. **Unificar marca** (handles/bio/logo/link) — manual, barato, hoje.
2. **Tokens de design** (extrair do site) → entregar pro Claude Code aplicar no dashboard.
3. **Desenhar o Content-Core + Atomizador** (arquitetura n8n) — só desenho agora;
   liga quando houver crédito (gera copy/imagem).
4. **LinkedIn primeiro** como canal-piloto do Content-Core (maior ROI B2B).
5. YouTube lofi e Discord/comunidade = fase 2.
