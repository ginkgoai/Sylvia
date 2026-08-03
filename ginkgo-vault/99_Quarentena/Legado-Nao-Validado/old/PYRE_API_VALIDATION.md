# PYRE — Validação de APIs (Fase 1)

**Data:** 21 de Abril de 2026  
**Status:** ✅ Validação Completa  
**Objetivo:** Confirmar viabilidade técnica de cada API da stack Pyre

---

## 1. POSTIZ API — Orquestração de Publicação em Redes Sociais

### Status: ✅ VIÁVEL

**Endpoint Base:** `https://api.postiz.com/public/v1`

**Autenticação:**
- Bearer Token (API Key) no header `Authorization`
- OAuth2 disponível para multi-usuário

**Capacidades Principais:**
- Publicar em **32+ plataformas** (Instagram, TikTok, Facebook, LinkedIn, X, Pinterest, Threads, etc.)
- Agendamento de posts
- Upload de mídia (imagens, vídeos)
- Análise de posts

**Endpoints Críticos:**
```
POST /posts                    # Criar/agendar post
GET /integrations             # Listar contas conectadas
POST /upload                  # Upload de mídia
GET /posts                    # Listar posts
DELETE /posts/{id}            # Deletar post
PUT /posts/{id}               # Atualizar status
```

**Rate Limit:** 30 requisições/hora (suficiente para MVP)

**Payload Exemplo (Agendamento):**
```json
{
  "type": "schedule",
  "date": "2024-12-14T10:00:00.000Z",
  "posts": [{
    "integration": { "id": "integration-id" },
    "value": [{ "content": "Conteúdo aqui", "image": [] }],
    "settings": { "__type": "instagram" }
  }]
}
```

**Integração com Pyre:** Perfeita para publicação automatizada. Postiz será o "executor" de todas as publicações.

---

## 2. BLOTATO API — Publicação Alternativa + Criação de Conteúdo

### Status: ✅ VIÁVEL

**Endpoint Base:** `https://api.blotato.com` (com MCP Server disponível)

**Autenticação:**
- API Key no header `Authorization`
- Requer subscription paga (começa com geração de key)

**Capacidades Principais:**
- Publicar em múltiplas redes
- Criar vídeos/imagens via templates
- Agendamento com slots de tempo
- Suporte nativo para n8n e Make

**Endpoints Críticos:**
```
POST /accounts                # Listar contas conectadas
POST /posts                   # Publicar post
GET /posts                    # Listar posts
POST /schedules               # Agendar publicação
POST /visuals                 # Criar conteúdo visual
```

**Payload Exemplo (Publicação Imediata):**
```json
{
  "type": "now",
  "posts": [{
    "integration": { "id": "account-id" },
    "value": [{ "content": "Texto", "image": [] }],
    "settings": { "__type": "instagram" }
  }]
}
```

**Integração com Pyre:** Pode ser usado como alternativa a Postiz ou complemento para funcionalidades de criação visual.

---

## 3. NANOBANANA API — Geração de Imagens

### Status: ✅ VIÁVEL

**Endpoint Base:** `https://api.nanobananaapi.ai/api/v1`

**Autenticação:**
- Bearer Token no header `Authorization`

**Capacidades Principais:**
- Text-to-Image (geração a partir de prompt)
- Image-to-Image (edição de imagens)
- Múltiplas resoluções (1:1, 16:9, 9:16, etc.)
- Geração de 1-4 imagens por requisição

**Endpoints Críticos:**
```
POST /nanobanana/generate    # Gerar/editar imagem
GET /nanobanana/{taskId}     # Verificar status
```

**Payload Exemplo:**
```json
{
  "prompt": "A serene mountain landscape at sunset",
  "numImages": 1,
  "type": "TEXTTOIMAGE",
  "image_size": "16:9",
  "callBackUrl": "https://seu-backend.com/callback"
}
```

**Modelo:** Gemini 3.1 Flash Image (Nano Banana 2)

**Integração com Pyre:** Será o roteador padrão para geração de imagens. Suporta callbacks para notificação assíncrona.

---

## 4. SEEDANCE 2.0 API — Geração de Vídeos

### Status: ✅ VIÁVEL

**Endpoint Base:** `https://seedanceapi.org/v2`

**Autenticação:**
- Bearer Token no header `Authorization`

**Capacidades Principais:**
- Text-to-Video (5s, 10s, 15s)
- Image-to-Video
- Múltiplas resoluções (16:9, 9:16, 4:3, 3:4)
- Dois modelos: `seedance-2.0` (qualidade) e `seedance-2.0-fast` (velocidade)

**Endpoints Críticos:**
```
POST /v2/generate            # Iniciar geração
GET /v2/status?task_id=...   # Verificar status
```

**Pricing:**
- 5s: 240 créditos (standard) / 160 (fast)
- 10s: 480 créditos (standard) / 320 (fast)
- 15s: 720 créditos (standard) / 480 (fast)

**Payload Exemplo:**
```json
{
  "prompt": "A cinematic aerial shot over coastline at golden hour",
  "aspect_ratio": "16:9",
  "duration": 10,
  "model": "seedance-2.0",
  "callback_url": "https://seu-backend.com/callback"
}
```

**Integração com Pyre:** Ideal para MVP fase 2. Suporta callbacks para notificação assíncrona.

---

## 5. HEYGEN API — Geração de Vídeos com Avatar

### Status: ✅ VIÁVEL

**Endpoint Base:** `https://api.heygen.com/v3`

**Autenticação:**
- API Key no header `x-api-key`

**Capacidades Principais:**
- Video Agent (prompt único → vídeo completo)
- Photo Avatar (foto estática → vídeo com lip-sync)
- Digital Twin (vídeo pessoal → clone avatar)
- Video Translation (tradução com lip-sync)
- Lipsync (sincronização de áudio)

**Endpoints Críticos:**
```
POST /video-agents           # Criar vídeo com agente
POST /video                  # Criar vídeo com avatar
GET /video/{id}              # Status do vídeo
```

**Pricing:**
- Video Agent: $0.0333/segundo
- Photo Avatar: $0.05/segundo
- Digital Twin: $0.0667/segundo

**Payload Exemplo (Video Agent):**
```json
{
  "prompt": "Create a video about AI automation",
  "avatar_id": "avatar-123",
  "voice_id": "voice-456"
}
```

**Integração com Pyre:** Excelente para criar vídeos com apresentadores/avatares. Pode ser usado em automações recorrentes.

---

## 6. ELEVENLABS API — Síntese de Voz (TTS)

### Status: ✅ VIÁVEL

**Endpoint Base:** `https://api.elevenlabs.io/v1`

**Autenticação:**
- API Key no header `xi-api-key`

**Capacidades Principais:**
- Text-to-Speech em 70+ idiomas
- 5000+ vozes disponíveis
- Streaming de áudio em tempo real
- Clonagem de voz (Instant Voice Clone)
- Geração de efeitos sonoros

**Endpoints Críticos:**
```
POST /text-to-speech/{voice_id}    # Gerar áudio
GET /voices                        # Listar vozes
POST /voice/add                    # Adicionar voz customizada
```

**Payload Exemplo:**
```json
{
  "text": "The first move is what sets everything in motion.",
  "model_id": "eleven_multilingual_v2",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.75
  }
}
```

**Output Formats:** MP3, WAV, PCM, μ-law

**Integração com Pyre:** Será usado para:
1. Interface conversacional com áudio (agente Pierre)
2. Narração de vídeos
3. Legendas em áudio para conteúdo

---

## 7. GEMMA 4 — Roteador Inteligente (LLM Local/Grátis)

### Status: ✅ VIÁVEL

**Acesso:** Google AI Studio (gratuito até quota)

**Capacidades:**
- Classificação de intenção do usuário
- Roteamento de tipo de mídia
- Geração de captions/legendas
- Processamento local (sem custos)

**Integração com Pyre:** Será o primeiro nó de roteamento. Classifica o que o usuário quer criar.

---

## 8. CLAUDE OPUS 4.7 — Raciocínio Complexo

### Status: ✅ VIÁVEL

**Acesso:** Anthropic API

**Capacidades:**
- Interpretação de referências anteriores
- Configuração de automações complexas
- Análise de contexto longo
- Geração de prompts sofisticados

**Integração com Pyre:** Usado apenas quando necessário raciocínio profundo (economia de custos).

---

## 9. STRIPE — Pagamentos e Tokenização

### Status: ✅ VIÁVEL

**Acesso:** Stripe API

**Capacidades:**
- Pagamento via cartão
- Tokenização segura
- Webhooks para eventos
- Gerenciamento de clientes

**Integração com Pyre:** Processamento de pagamentos para planos (Free, Criador, Pro, Studio).

---

## Matriz de Compatibilidade

| API | MVP | Fase 2 | Fase 3 | Custo | Status |
|-----|-----|--------|--------|-------|--------|
| Postiz | ✅ | ✅ | ✅ | Grátis | Validado |
| Blotato | ✅ | ✅ | ✅ | Pago | Validado |
| NanoBanana | ✅ | ✅ | ✅ | Pago | Validado |
| Seedance 2.0 | ❌ | ✅ | ✅ | Pago | Validado |
| HeyGen | ❌ | ✅ | ✅ | Pago | Validado |
| ElevenLabs | ✅ | ✅ | ✅ | Pago | Validado |
| Gemma 4 | ✅ | ✅ | ✅ | Grátis | Validado |
| Claude Opus | ✅ | ✅ | ✅ | Pago | Validado |
| Stripe | ✅ | ✅ | ✅ | Pago | Validado |

---

## Fluxo de Integração Recomendado

```
Usuário → ElevenLabs (áudio) → Gemma 4 (classificação)
  ↓
  Tipo de conteúdo?
  ├─ Imagem → NanoBanana
  ├─ Vídeo → Seedance 2.0
  ├─ Avatar → HeyGen
  └─ Áudio → ElevenLabs
  ↓
Claude Sonnet (gerar prompt refinado)
  ↓
API de Geração (callback assíncrono)
  ↓
Postiz/Blotato (publicar)
  ↓
Stripe (cobrar créditos)
```

---

## Conclusão

**Todas as APIs foram validadas e são viáveis para o MVP do Pyre.** A stack está pronta para arquitetura.

**Próxima Fase:** Desenhar a arquitetura completa do sistema com fluxos de dados, schema de banco e roteador inteligente.
