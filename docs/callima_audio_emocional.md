# Callima — Áudio emocional ([[AUDIO]])

Como fazer a Callima mandar áudios humanos, em momentos-chave, com contexto.
Mecanismo já existe: o agente escreve um trecho dentro de `[[AUDIO]] ... [[/AUDIO]]`;
o `CODE`/`Audio Logic` extrai e envia como voz (sub-workflow AUDIO FEM).

## Regras p/ o PROMPT da Callima
QUANDO usar (no máximo 1 áudio por resposta, NÃO em toda mensagem):
- Boas-vindas calorosa no 1º contato.
- Fechar/confirmar venda ou agendamento (comemorar com o cliente).
- Tranquilizar cliente ansioso ou insatisfeito (tom humano, acolhedor).
- Agradecimento / parabéns genuínos.

QUANDO NÃO usar: respostas curtas operacionais, listas, links, dados técnicos,
preços/tabelas — isso vai como texto.

COMO escrever o trecho falado:
- Linguagem FALADA, 1ª pessoa, curta (1–3 frases, ~5–15s).
- Sem markdown, sem ler emoji, sem listas. Pausas naturais ok ("olha...", "então,").
- Contextual: usar o nome do lead e o assunto da conversa.
- A resposta de texto normal continua; o trecho de voz vai dentro de
  `[[AUDIO]] ... [[/AUDIO]]`.

## ElevenLabs (sub-workflow AUDIO FEM) — settings p/ soar humano
- Modelo: `eleven_multilingual_v2` (estável e emotivo) OU `eleven_v3`
  (mais expressivo; aceita tags inline `[warmly]`, `[laughs]`, `[sighs]`).
- Voice settings:
  - `stability`: 0.30–0.40 (mais baixo = mais emoção/variação)
  - `similarity_boost`: 0.75
  - `style`: 0.40–0.60 (mais alto = mais expressivo)
  - `use_speaker_boost`: true
- Voz: PT-BR feminina expressiva.
- O texto enviado ao TTS é o mesmo do bloco `[[AUDIO]]` (já em estilo falado).

## Onde aplicar
- Prompt: adicionar a seção "QUANDO/COMO usar [[AUDIO]]" ao system prompt da Callima.
- ElevenLabs: ajustar o body do nó "Generate speech from text" no AUDIO FEM
  (voice_settings acima + model_id).
- Aplicar junto com a virada do OpenRouter (quando o agente volta a responder),
  pra calibrar com conversas reais.
