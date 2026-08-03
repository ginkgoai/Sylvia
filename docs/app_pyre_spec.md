# App PYRE — Estúdio de Conteúdo (agente Nyra)

Acento âmbar. Rotas sob `/(dashboard)/pyre/...` (reaproveita a rota `studio`).
Base: `pyre_funcionalidades_playsquad.md`. Créditos GTK compartilhados (modelo PlaySquad).

## Seções (sidebar do app Pyre)
1. **Visão geral** — projetos recentes, saldo GTK, atalhos pros módulos.
2. **Voice (Nyra)** — narração TTS (ElevenLabs): texto/roteiro → áudio; vozes/idiomas/tom.
3. **Trends** — radar de tendências por nicho/keyword + score de viralidade; alimenta pauta.
4. **Clips** — vídeo longo → cortes verticais 9:16 com legenda (highlights por IA).
5. **Avatar (HeyGen)** — vídeo short de influencer de IA: roteiro da Nyra → avatar fala →
   vertical pronto. Geração do zero (complementa o Clips). GTK mais alto por vídeo.
6. **Radar** — outliers de canais concorrentes (o que rompeu a média). (YouTube Data API)
7. **Content Engine** — calendário editorial + geração de posts/legendas + agendamento via
   **Postiz** + HITL (aprovar antes de publicar). Liga com o esqueleto n8n já criado.
8. **Projetos** — histórico/outputs por projeto, export em qualquer formato.

## GTK (tabela gtk_costs — calibrar)
- post ~10 · imagem ~25 · motion ~80 · voz ~8/min · clip por min de vídeo · avatar(HeyGen) alto
  · trend search ~Y · radar análise ~Z. Saldo único compartilhado com Leaf/Wave.

## Cruzamentos
- Outputs (clipe/voz/avatar) viram `media_assets` que a Callima (Leaf) envia. Peças aprovadas
  podem virar criativo no Wave. Trends informa pauta do Content Engine e ângulo de ADS.

## Dependências
- ElevenLabs (já temos) · gerador de imagem/vídeo (definir) · HeyGen API · API de tendências
  (Bright Data/Nimble já no ambiente) · Postiz (precisa do fix Elasticsearch — pendente).
- Implementar após P0 do LEAF. MVP: **Voice → Trends → Clips → Avatar(HeyGen) → Radar →
  Content Engine**.

## Aceite
- Cada módulo gera output real, debita GTK pela tabela, salva no projeto, exporta; estados
  completos; identidade âmbar; outputs aparecem na Mídia do Leaf; lint/build OK.
