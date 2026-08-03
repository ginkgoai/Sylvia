# Pesquisa HeyGen API v3

## Capacidades Principais

### Modelos Disponíveis
1. **Video Agent** - Gera vídeo completo a partir de um prompt (sem seleção de avatar)
2. **Avatar IV - Digital Twin** - Avatar treinado a partir de vídeo real da pessoa
3. **Avatar IV - Photo Avatar** - Avatar criado a partir de uma foto única
4. **Video Translation** - Traduz vídeos em 175+ idiomas com lip-sync
5. **Lipsync** - Substitui áudio e ressincroniza lábios
6. **Starfish Voices** - Geração de áudio TTS

### Preços (Pay-as-you-go)
- Video Agent: $0.0333/seg
- Photo Avatar: $0.05/seg
- Digital Twin: $0.0667/seg
- Video Translation (Speed): $0.0333/seg
- Video Translation (Precision): $0.0667/seg
- Lipsync (Speed): $0.0333/seg
- Lipsync (Precision): $0.0667/seg
- Voices (Starfish): $0.000667/seg

Mínimo: $5 para começar

### Endpoints Principais (v3)

#### 1. Criar Vídeo com Video Agent
```
POST /v3/video-agents
Headers: X-Api-Key, Content-Type: application/json
Body: {
  "prompt": "string",
  "avatar_id": "string (opcional)",
  "voice_id": "string (opcional)"
}
Response: {
  "session_id": "string",
  "status": "generating",
  "video_id": "string",
  "created_at": timestamp
}
```

#### 2. Verificar Status do Vídeo
```
GET /v3/videos/{video_id}
Headers: X-Api-Key
Response: {
  "id": "string",
  "status": "completed|failed|processing",
  "video_url": "string",
  "thumbnail_url": "string",
  "duration": number
}
```

### Fluxo de Geração
1. POST para criar vídeo (async)
2. Polling com GET ou webhook callback_url
3. Status: pending → processing → completed/failed
4. Download de video_url quando completed

### Autenticação
- API Key gerado em Settings → API do dashboard
- Enviado via header: `X-Api-Key: {key}`
- OAuth 2.0 também disponível

### Integrações Disponíveis
- CLI para terminal
- MCP (Model Context Protocol) para AI agents
- Zapier
- Make.com
- Integração nativa com n8n

### Limites e Uptime
- 99.9% API uptime
- Rate limits por recurso
- SOC 2 Type II e GDPR compliant

## Estratégia para Vitória Lima

### Fluxo Recomendado
1. Usar Video Agent para gerar vídeos a partir de prompts estruturados
2. Ou criar Photo Avatar a partir de foto da Vitória
3. Integrar com n8n para automação de pipeline
4. Usar TTS Starfish para voz com sotaque curitibano
5. Webhook para notificações quando vídeos ficam prontos

### Custos Estimados
- 5 vídeos/semana × 30 segundos × $0.0333 = ~$25/semana = ~$100/mês
- Se usar Photo Avatar: 5 × 30s × $0.05 = ~$7.50/semana = ~$30/mês
- Muito viável para operação de influencer
