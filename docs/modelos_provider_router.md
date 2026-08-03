# Modelos & Provider Router — referência (jun/2026)

Como tokenizamos (GTK) e escondemos o provedor atrás do **Provider Router** (aiGateway/
tokenRouter), trocar de modelo é CONFIG, não obra. Modelos chineses abertos são a principal
**alavanca de custo/margem**. Tabela de referência pra quando ligarmos o Model Router do tronco.

## Preços (via OpenRouter, USD por 1M tokens in/out) — verificar no painel antes de fixar
| Modelo | in/out (~) | Bom para | Notas |
|---|---|---|---|
| Qwen3.5-9B | $0,10 / $0,15 | chat Callima + **multimodal/visão** | barato e entende imagem/doc |
| DeepSeek V4 Flash | $0,14 / $0,28 | chat rápido da Callima | custo-base baixo p/ GTK |
| DeepSeek V4 Pro | $0,46 / $0,92 | tarefas que exigem mais cabeça | reasoning forte |
| GLM-5.1 | (ver painel) | código/agêntico (lado dev) | SWE-bench alto |
| Kimi K2.6 | (ver painel) | multimodal rápido | <500ms |
| Comparação | 5–30× + barato | — | vs GPT/Claude/Gemini flagship |

## Grátis no OpenRouter (~27 modelos) — USO INTERNO/DEV apenas
`deepseek-chat-v3.1:free`, `qwen3-235b-a22b:free`, `zhipu glm-4.5-air:free`, `GLM-4.7-Flash`.
⚠️ Rate-limit + frequentemente **logam/treinam com os dados** → NUNCA com dado de cliente/PII.

## Política de roteamento (proposta)
- **Callima (produção, dados de cliente)**: modelo PAGO com no-log como **primário** (ex.: DeepSeek
  V4 Flash ou Qwen3.5) + **fallback** barato; failover automático no Router.
- **Multimodal-in** (imagem/áudio/doc do cliente): Qwen-VL / Kimi (pago).
- **Interno (Sexta-feira/dev/teste)**: pode usar `:free`.
- **Por-tenant configurável**: cliente enterprise pode vetar provedor/jurisdição → trocar a rota
  sem mexer no produto.
- **Margem**: GTK vendido ≥ 3–4× o custo do provedor (a tabela acima derruba o custo-base).

## Cuidados
- open-weight ≠ self-hosted: via OpenRouter o dado ainda vai a um provedor → escolher no-train/no-log.
- self-host só quando houver GPU/necessidade de soberania (não agora).
- manter primário estável + fallback; não rotacionar pra bleeding-edge em produção sem teste.

## Futuro (Pyre, quando gerar): modelos abertos de imagem/vídeo (Qwen-Image, Wan, Hunyuan) —
também baratos; mesma lógica de Router. Hoje só ENVIO de mídia, sem geração.
