# Guia de Implementação Técnica: Operação Vitória Lima (@vitorialima.fit)

Este documento detalha a arquitetura de sistemas, integrações entre APIs e fluxos de automação necessários para dar vida à influenciadora de IA Vitória Lima, focando em escalabilidade e implementação prática.

## 1. Arquitetura do Sistema Recomendada

Para construir uma operação escalável de produção de conteúdo, utilizaremos uma arquitetura baseada em microsserviços orquestrada pelo **n8n**. Esta abordagem permite que você, como operador, gerencie a operação de forma centralizada.

### Stack Tecnológico
- **Orquestração:** n8n (Self-hosted via Docker ou Cloud)
- **Geração de Imagens (Base/Avatar):** Nano Banana API
- **Geração de Áudio (Voz):** ElevenLabs API
- **Geração de Vídeo (Animação):** HeyGen API v3
- **LLM (Roteiros/Variações):** Claude (Anthropic)
- **Armazenamento:** Supabase Storage (para assets e vídeos finais)
- **Notificações:** Evolution API (WhatsApp) ou Telegram Bot

## 2. Avaliação dos Prompts e Estratégia

Os prompts fornecidos (`pasted_content.txt` e `pasted_content_2.txt`) apresentam uma base de negócios e marketing excepcional. A persona (mulher de 28 anos, Curitiba, foco em glúteos/abdômen) é altamente conectada com o público-alvo do TikTok Shop Brasil.

### Ajustes Técnicos Necessários
A principal limitação técnica atual é que a HeyGen (e outras IAs de vídeo) não gera movimentos corporais complexos do zero (ex: "Vitória suada saindo da academia", "mistura no shaker", "dança trend atual").

**Solução Arquitetural (O "Pulo do Gato"):**
O sistema automatizado gerará o "Talking Head" (o rosto da Vitória falando com sincronia labial perfeita). A edição final (feita no CapCut) utilizará a técnica de B-Roll:
1. O avatar da HeyGen fala o roteiro.
2. Cortes dinâmicos inserem vídeos stock ou gravados (B-Roll) de mãos preparando o shake, pernas fazendo agachamento, etc.
3. A voz da Vitória (ElevenLabs) continua narrando por cima do B-Roll.

Isso cria a ilusão perfeita de um vídeo orgânico, misturando o rosto hiper-realista da IA com ações físicas reais.

## 3. Setup Inicial (Assets Base)

Antes de ativar a automação, você precisará configurar os assets fundamentais:

### 3.1. Geração da Imagem Base (Nano Banana)
Utilize a API do Nano Banana para gerar a foto perfeita da Vitória.
**Prompt Sugerido:**
> "Corpo inteiro na academia, short cintura alta e top cropped preto, cabelo liso castanho médio com ombré leve, pele morena clara com glow natural, sorriso aberto, abdômen definido natural. Estilo foto de iPhone 16 Pro, iluminação de academia moderna."

### 3.2. Criação do Avatar (HeyGen)
1. Acesse o painel da HeyGen.
2. Faça upload da imagem gerada pelo Nano Banana para criar um **Photo Avatar**.
3. Anote o `avatar_id` gerado (será usado na API).

### 3.3. Criação da Voz (ElevenLabs)
1. Use a ferramenta de Voice Design do ElevenLabs para criar uma voz feminina, animada, com sotaque sulista/curitibano leve.
2. Anote o `voice_id` gerado.

## 4. Fluxo de Automação (Pipeline n8n)

O pipeline de produção de um vídeo seguirá este fluxo automatizado no n8n:

### Passo 1: Entrada de Dados (Trigger)
- **Webhook:** Você envia o roteiro base (ex: os roteiros do arquivo fornecido) via webhook para o n8n.
- **Processamento LLM (Claude):** O Claude recebe o roteiro e o divide em duas partes:
  1. O texto exato que será falado (para o ElevenLabs).
  2. As instruções visuais/B-roll (para edição posterior).

### Passo 2: Geração de Áudio (ElevenLabs)
- O n8n faz uma chamada POST para a API do ElevenLabs enviando o texto falado.
- O n8n recebe o arquivo de áudio (`.mp3`) e o salva temporariamente no Supabase Storage, gerando uma URL pública (`audio_url`).

### Passo 3: Geração de Vídeo (HeyGen API v3)
- O n8n faz uma chamada POST para o endpoint `/v3/video-agents` da HeyGen.

**Exemplo de Payload (HeyGen API v3):**
```json
{
  "prompt": "Texto do roteiro aqui",
  "avatar_id": "SEU_AVATAR_ID",
  "voice_id": "SEU_VOICE_ID"
}
```
*Nota: A HeyGen v3 permite enviar o prompt de texto diretamente, e a IA deles cuida da geração do áudio se o `voice_id` for fornecido, ou você pode usar a funcionalidade de Lipsync enviando o `audio_url` gerado pelo ElevenLabs.*

### Passo 4: Polling e Download
- A geração de vídeo na HeyGen é assíncrona. O n8n entra em um loop de *polling* verificando o status do vídeo (`GET /v3/videos/{video_id}`).
- Quando o status for `completed`, o n8n faz o download do vídeo final (`video_url`).
- O vídeo é salvo no Supabase Storage na pasta `/prontos_para_postar`.

### Passo 5: Notificação
- O n8n envia uma mensagem via Evolution API (WhatsApp) ou Telegram avisando: "Gabriel, o vídeo 'Shake Pós-Treino' está pronto! [Link para download]".

## 5. Custos Estimados (APIs)

A estrutura de custos da HeyGen (Pay-as-you-go) é altamente viável para esta operação:
- **Photo Avatar:** $0.05 por segundo.
- **Custo por vídeo (30s):** ~$1.50.
- **Custo semanal (5 vídeos):** ~$7.50.
- **Custo mensal (20 vídeos):** ~$30.00.

Somando os custos do ElevenLabs e Claude, a operação técnica de geração de conteúdo custará menos de $50/mês, permitindo alta margem de lucro com as vendas no TikTok Shop.

## 6. Próximos Passos (Como Copiloto Operador)

Como seu copiloto, estruturei a arquitetura. Agora, os passos práticos para você executar são:

1. **Gerar a imagem base** da Vitória usando o Nano Banana.
2. **Criar o Photo Avatar** na HeyGen e anotar o `avatar_id`.
3. **Criar a voz** no ElevenLabs e anotar o `voice_id`.
4. **Configurar o workflow no n8n** seguindo a arquitetura acima (posso fornecer o JSON do workflow do n8n se desejar na próxima iteração).

A estratégia de marketing e os roteiros estão perfeitos. Com esta arquitetura técnica, você terá uma linha de produção de conteúdo escalável e de altíssima qualidade.
