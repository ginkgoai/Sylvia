# Pyre — Funcionalidades (referência: PlaySquad)

PlaySquad = plataforma all-in-one pra creators, **billing por crédito compartilhado entre
ferramentas** (igual ao nosso GTK) + histórico por projeto. Valida o modelo Ginkgo.
Aqui mapeio as funcionalidades aplicáveis ao **Pyre** (agente de conteúdo).

## Os 4 módulos da PlaySquad
1. **Clips AI** — vídeo longo → clipes virais. Detecção automática de highlights, legendas
   multi-idioma, formatação vertical 9:16 (Shorts/Reels/TikTok). (~ "1 vídeo → infinitos clipes")
2. **Trend Scanner** — rastreia milhares de fontes em tempo real; tendências por nicho/keyword,
   alertas, **score de viralidade**.
3. **Monitor Outlier** (Channel Analyzer) — monitora canais concorrentes e destaca vídeos que
   **romperam a média** do canal (outliers/breakouts) vs média histórica.
4. **Audio Lab** — narração neural, 50+ vozes, 15 idiomas, estilos/tons (sem estúdio).
Extras: workspace unificado (áudio/vídeo/SEO/roteiros/analytics), projetos com histórico,
export em qualquer formato, integração YouTube. Pricing deles: $8/30k créd · $15/60k créd
(créditos compartilhados, renovam por ciclo, pague pelo uso).

## Pyre = Content Engine (já iniciado) + Creator Suite (novo, inspirado na PlaySquad)
Hoje o Pyre é o motor de conteúdo (Planner→Core→Atomizador→Asset→HITL→Postiz). A PlaySquad
mostra que falta a camada de **produção criativa**. Pyre passa a ter 2 frentes:
- **A) Content Engine** (publica pela marca do cliente): gera posts/legendas, agenda no Postiz,
  HITL. (em construção)
- **B) Creator Suite** (ferramentas sob demanda, consumo em GTK):
  - **Pyre Clips** — vídeo longo → cortes verticais com legenda (Shorts/Reels/TikTok).
  - **Pyre Trends** — radar de tendências por nicho/keyword + score.
  - **Pyre Radar** — monitor de concorrentes/outliers (o que estourou).
  - **Pyre Voice** — narração TTS multi-idioma (já temos ElevenLabs).

## Mapeamento técnico + custo GTK (entra na tabela gtk_costs)
| Módulo Pyre | O que faz | APIs/stack | Custo GTK (calibrar) |
|------|------|------|------|
| Pyre Clips | highlights + corte 9:16 + legenda | LLM p/ marcar momentos + ffmpeg + ASR (Whisper) p/ legenda | por minuto de vídeo (~ X GTK/min) |
| Pyre Voice | narração neural | ElevenLabs (já temos) | por minuto de áudio (básico vs premium) |
| Pyre Trends | tendências por nicho | busca/scraping (Bright Data/Nimble) + LLM p/ score | por pesquisa (~ Y GTK) |
| Pyre Radar | outliers de concorrentes | YouTube Data API / APIs sociais + cálculo de média | por análise (~ Z GTK) |
| Content post | gerar post/legenda | OpenRouter | ~10 GTK |
| Content image | imagem | gerador de imagem | ~25 GTK |
| Content motion | vídeo curto/motion | gerador de vídeo | ~80 GTK |

Créditos GTK **compartilhados** entre todos os módulos (modelo PlaySquad/Manus) — já é o
nosso desenho. Plano Pyre Base $99 (8k GTK) / Pro $249 (25k GTK) cobre o uso típico; excedente
via top-up. Calibrar GTK→custo real garantindo margem ≥ alvo antes do launch.

## Diferencial Ginkgo (não copiar — superar)
PlaySquad é self-serve pra creator. O Pyre é **agente** dentro do ecossistema Ginkgo: integra
com atendimento (Leaf/Callima) e tráfego (Wave) — ex.: Trends alimenta o Planner do Content
Engine; clipes/voz viram catálogo de mídia que a Callima envia; Radar informa a estratégia de
ADS do Wave. É produção + distribuição + atendimento num só lugar, governado (HITL/Laplace).

## MVP do Pyre (ordem sugerida) — depois das prioridades P0 do LEAF
1. **Pyre Voice** (já temos ElevenLabs — menor esforço, valor imediato).
2. **Pyre Trends** (busca + score) — alimenta o Content Engine.
3. **Pyre Clips** (vídeo→shorts) — maior esforço (ffmpeg/ASR/render), maior "uau".
4. **Pyre Radar** (outliers concorrentes) — depende de YouTube Data API.
Cada módulo: consome GTK pela tabela, salva output por projeto, exporta. UI no /dashboard/studio
(que já existe como rota — vira o "estúdio Pyre").

## Pendências
- Confirmar com founder se Pyre v1 entra agora ou após P0 do LEAF (atendimento/CRM primeiro).
- Definir gerador de imagem/vídeo (motion) e API de tendências (Bright Data/Nimble já no plugin).


---
## Agente: NYRA (persona do Pyre)
Nyra opera o Estúdio Pyre. Módulos: Voice, Trends, Clips, Radar + **Pyre Avatar (HeyGen)**.
- **Pyre Avatar (HeyGen API)**: gera vídeo short de **influencer de IA (avatar)** falando um
  roteiro da Nyra → vertical pronto p/ Reels/TikTok/Shorts. Diferente do Clips (que corta vídeo
  existente): aqui é GERAÇÃO do zero. Custo GTK por vídeo mais alto (avatar) — calibrar.
  Ordem MVP atualizada: Voice → Trends → Clips → **Avatar(HeyGen)** → Radar.
