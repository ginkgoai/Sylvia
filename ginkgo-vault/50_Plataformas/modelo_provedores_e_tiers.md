# Modelo de provedores & tiers (decisão do fundador — 2026-07-03)

> Resolve o #3 da auditoria (chave compartilhada vs BYO). Cross-produto (LEAF/PYRE/WAVE).

## Default — White-label compartilhado (Standard/Pro)
- A Ginkgo detém as contas de provedor (Evolution, OpenRouter, Groq, ElevenLabs, OpenAI). Toda Callima usa as chaves da Ginkgo; custo embutido no plano.
- **Self-serve sem atrito:** cliente assina, conecta o WhatsApp, configura pelo Brann. Nunca vê um provedor. É o modelo que entrega a visão "cada usuário ganha uma Callima igual".
- **Custo da escolha (obrigatório antes de escalar):** #9 (token por instância + rotação do ingest token) + **teto de uso por tenant** (metering/cap). Blast-radius é o preço do compartilhado.

## Enterprise — BYO, provider-swappable ("modo Odysseus")
- Referência: PewDiePie / *Odysseus* — self-hosted, hardware e modelos próprios, controle total.
- O tenant enterprise **troca provedores** (LLM, STT/TTS, imagem, vídeo, embeddings) **E skills/integrações**, apontando **chaves próprias** (cofre do tenant) — inclusive **LLM local**.
- Ex.: "alimento com minha LLM X, gero imagem com a API Y, vídeo com a Z" — uso dev/power-user, mensal grande e personalizado.
- **Isolamento por construção:** chaves próprias = blast-radius ≈ 1. O tier enterprise **se auto-resolve** o problema de segurança do compartilhado.

## Por que a arquitetura já suporta (doutrina paga)
- Separação IA↔sistema + model-router + skills como abstração → **o provedor é execução atrás de uma abstração**. Trocar OpenRouter→LLM local, ou ElevenLabs→outro TTS, é **STATE/config no Boundary**, não reescrita.
- Logo white-label e BYO são o **mesmo código, STATE diferente** (de quem são as chaves + qual provedor o router nomeia). BYO enterprise = expor o *swap* + apontar o cofre do tenant + validar a chave dele.
- Um tier premium inteiro sai "de graça" da abstração — é a prova de que a doutrina compensa.

## Sequência
- **MVP:** white-label compartilhado (piloto Ginkgo com risco aceito e documentado; #9 antes de qualquer terceiro).
- **Enterprise BYO:** feature pós-MVP — seletor de provedor por-tenant + validação de chave + catálogo de skills trocáveis. Encaixa em LEAF/PYRE/WAVE.
