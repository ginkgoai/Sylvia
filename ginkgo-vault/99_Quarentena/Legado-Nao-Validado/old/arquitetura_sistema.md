# Arquitetura do Sistema de Produção de Conteúdo: Vitória Lima

## Visão Geral da Arquitetura

Para criar a influenciadora Vitória Lima de forma escalável e realista, usaremos uma arquitetura baseada em microsserviços orquestrada pelo **n8n**. Esta abordagem permite que você, como operador, apenas insira o roteiro (ou deixe a IA gerar) e o sistema entregue o vídeo final pronto para postagem.

### Stack Tecnológico Recomendado
1. **Orquestração:** n8n (Self-hosted ou Cloud)
2. **Geração de Imagens (Base/Avatar):** Nano Banana API
3. **Geração de Áudio (Voz):** ElevenLabs API
4. **Geração de Vídeo (Animação):** HeyGen API v3
5. **LLM (Roteiros/Variações):** Claude (Anthropic)
6. **Armazenamento:** Supabase Storage (para assets e vídeos finais)

## Fluxo de Automação (Pipeline n8n)

O pipeline de produção de um vídeo (ex: "Shake Pós-Treino") seguirá este fluxo automatizado:

### Passo 1: Entrada de Dados (Trigger)
- **Webhook ou Interface n8n:** Você envia o roteiro base (ex: os roteiros do arquivo `pasted_content_2.txt`).
- **Processamento LLM (Claude):** O Claude recebe o roteiro e o divide em duas partes:
  1. O texto exato que será falado (para o ElevenLabs).
  2. As instruções visuais/B-roll (para edição posterior).

### Passo 2: Geração de Áudio (ElevenLabs)
- O n8n envia o texto falado para a API do ElevenLabs.
- **Configuração:** Usar uma voz clonada ou pré-selecionada com sotaque sulista/curitibano leve.
- **Retorno:** Arquivo de áudio `.mp3` ou `.wav`.
- O n8n salva este áudio temporariamente no Supabase.

### Passo 3: Geração de Vídeo (HeyGen API v3)
- O n8n faz uma chamada POST para o endpoint `/v3/video-agents` ou usa a funcionalidade de *Photo Avatar* da HeyGen.
- **Payload:**
  - `avatar_id`: O ID do avatar da Vitória (previamente criado na HeyGen usando uma imagem do Nano Banana).
  - `audio_url`: O link público do áudio gerado no Passo 2 (armazenado no Supabase).
- A HeyGen inicia a geração assíncrona.

### Passo 4: Polling e Download
- O n8n entra em um loop de *polling* (ou aguarda um webhook da HeyGen) verificando o status do vídeo (`GET /v3/videos/{video_id}`).
- Quando o status for `completed`, o n8n faz o download do vídeo final (`video_url`).
- O vídeo é salvo no Supabase Storage na pasta `/prontos_para_postar`.

### Passo 5: Notificação
- O n8n envia uma mensagem para o seu Telegram/WhatsApp (via Evolution API) avisando: "Gabriel, o vídeo 'Shake Pós-Treino' está pronto! [Link para download]".

## Estratégia de Criação do Avatar (Setup Inicial)

Antes de rodar a automação, você precisará configurar os assets base:

1. **Geração da Imagem Base (Nano Banana):**
   - Prompt sugerido: *"Corpo inteiro na academia, short cintura alta e top cropped preto, cabelo liso castanho médio com ombré leve, pele morena clara com glow natural, sorriso aberto, abdômen definido natural. Estilo foto de iPhone 16 Pro, iluminação de academia moderna."*
   - Gere várias opções e escolha a melhor.

2. **Criação do Avatar na HeyGen:**
   - Faça upload da imagem escolhida para a HeyGen para criar um *Photo Avatar*.
   - Anote o `avatar_id` gerado.

3. **Criação da Voz no ElevenLabs:**
   - Use a ferramenta de Voice Design ou clone uma voz que tenha o tom exato descrito nos prompts (animada, prática, sotaque leve).
   - Anote o `voice_id`.

## Contornando Limitações Técnicas (O "Pulo do Gato")

Como a HeyGen não gera movimentos complexos (como dançar ou misturar whey), a estratégia de edição será:

- **A Automação gera o "Talking Head":** O vídeo gerado pela HeyGen será a Vitória falando o texto com sincronia labial perfeita.
- **Edição Final (CapCut/InShot):** Você pegará este vídeo e fará cortes dinâmicos. Quando o roteiro disser "mostra embalagem Whey", você corta a imagem da HeyGen e insere um B-roll (vídeo stock ou gravado por você) de mãos preparando o shake, mantendo a voz da Vitória rolando por cima.
- Isso cria a ilusão perfeita de um vídeo orgânico do TikTok, misturando o rosto hiper-realista da IA com ações físicas reais.
