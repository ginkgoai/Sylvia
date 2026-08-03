# Ginkgo — Content Engine (Content-Core + Atomizador)

Motor único de conteúdo = produto **Pyre**. 1 ideia → muitos formatos → Postiz.
Tudo desenhado agora; liga quando houver crédito (OpenRouter + APIs de mídia).

## Pilares de marca (governam o gerador)
- **Educar** — IA aplicada, "plantar possibilidades" (o que dá pra fazer).
- **Provar** — cases/portfólio (o que JÁ fizemos com IA).
- **Novidades** — tendências e notícias do nicho.
- **Bastidores/Produto** — Ginkgo, LEAF/Callima em ação.

## Fluxo (n8n)
1. **Planner** (scheduleTrigger semanal): escolhe tema por pilar a partir de
   `content_calendar` (Supabase) + sinais de tendência (busca X/news) + RAG Ginkgo.
   Saída: N **briefs** {tema, ângulo, pilar, canais-alvo, CTA}.
2. **Core Generator** (OpenRouter): gera o "conteúdo-mestre" — ideia + pontos-chave
   + hook + CTA. honest-data (ancorado no que a Ginkgo realmente entrega).
3. **Atomizador** (por canal): transforma o mestre no formato do canal:
   - LinkedIn: post (hook+corpo+CTA) · IG: carrossel 5–8 slides · Reel/Short/TikTok:
     roteiro (hook 3s + beats) · X: thread · Newsletter: seção.
4. **Asset Generator**: imagem (slides/post) via API de imagem; vídeo/motion via
   API de vídeo; locução via ElevenLabs.
5. **Review/HITL (Laplace)**: rascunhos → `brann_actions` (pending) → você aprova.
6. **Publisher**: Postiz agenda/publica por canal (especialistas fora do Postiz:
   YouTube, Newsletter/Resend, Discord).
7. **Feedback**: métricas por canal → Supabase → alimentam o próximo Planner.

## Dados (Supabase)
- `content_calendar` (pilar, tema, data-alvo, status)
- `content_briefs` (brief gerado, canais-alvo)
- `content_posts` (canal, formato, copy, asset_ref, status: draft/approved/scheduled/published, métricas)
- reusa `brann_actions` (HITL) + `media_assets` (arquivos).

## Governança (Laplace)
- Início: NADA publica sem aprovação (HITL no passo 5).
- Depois: auto-publicar canais de baixo risco com teto diário; kill-switch global.
- Cada agente: papel claro, limite, memória controlada, métrica, desligável.

## Piloto LinkedIn (fatia mais fina — começar por aqui)
Planner(semanal/manual) → Core Generator → Atomizador(SÓ LinkedIn) → HITL aprova
→ Postiz(LinkedIn). Sem mídia obrigatória (texto já entrega valor B2B).
APIs mínimas: **OpenRouter** (texto). Imagem opcional.
Depois: ligar IG/Reels/TikTok (imagem+vídeo) reusando o mesmo mestre.

## Mapa nos produtos
- **Pyre** = este Content Engine · **Wave** = ADS/tráfego · **Leaf/Callima** = atendimento.
- A presença digital da Ginkgo É o showroom dos próprios agentes.

## STATUS — esqueleto construído (2026-06-18)
Workflow **"Content Engine — LinkedIn"** (id `k82S6bzBEqtIU5ps`, INATIVO) criado no n8n:
- Schedule Semanal → Brief → **Pyre — Gerar Post** (HTTP OpenRouter, cred openRouterApi
  `XxZ9pd0yUms0f8w7`, modelo google/gemini-2.0-flash-001) → Extrair Texto →
  **Inserir Rascunho (HITL)** (Postgres Supabase `zp3JG0Ln3Dd9ZJ8F` → brann_actions:
  type=social_post, channel=linkedin, status=pending, requires_hitl=true).
- Falta p/ ligar: (1) **crédito OpenRouter**; (2) definir **org_id da Ginkgo** no nó Brief
  (criar um "workspace casa" da Ginkgo ou usar org dedicada); (3) validar o binding do
  Postgres (queryReplacement) na 1a execução real.
- Está no raiz (Personal) — mover p/ pasta via UI se quiser.
- Próximas peças: **Social Publisher** (consumer: brann_actions approved → Postiz) e
  **Atomizador** p/ IG/Reels/X (reusando o mesmo Brief/mestre).
