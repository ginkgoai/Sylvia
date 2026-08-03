# Catálogo de Workflows n8n (lote do fundador)

Objetivo: padrões a rodar no n8n e **disparar pela Sexta-feira via prompt**.
Classificação de disparo: só `webhook` (POST livre) e `executeWorkflowTrigger`
são prontos pra disparo externo. Schedule/Manual/Telegram/Chat/Form/Gmail/Notion
trigger → PRECISA-WEBHOOK (adicionar um Webhook trigger pra Sexta-feira acionar).

| # | Workflow | Gatilho | Disparável? | Propósito | Serviços | Inputs |
|---|---|---|---|---|---|---|
| 1 | Clone Viral TikToks + 9 plataformas | telegramTrigger | PRECISA-WEBHOOK | Clona TikTok viral c/ avatar IA e auto-posta | Telegram, Perplexity, Blotato, OpenAI, Sheets | URL TikTok |
| 2 | AI Videos Veo3 + Blotato | scheduleTrigger | PRECISA-WEBHOOK | Gera vídeo IA (Veo3) e posta diário | Veo3, Blotato, OpenAI, Sheets | tópico (planilha) |
| 3 | Viral Videos Seedance | scheduleTrigger | PRECISA-WEBHOOK | Gera vídeo Seedance → TikTok/YT/IG | Seedance, Blotato, OpenAI, Sheets | tópico/prompt |
| 6 | Social videos via Telegram+GPT4 | telegramTrigger | PRECISA-WEBHOOK | Cria/publica vídeo social de prompt/imagem | Telegram, GPT-4, Blotato, PiAPI | prompt/imagem |
| 7 | Blog GPT-4 + Perplexity + WordPress | chatTrigger + formTrigger | PRECISA-WEBHOOK | Cria post de blog e publica WP | GPT-4, Perplexity, WordPress | tópico |
| 8 | Lead Qualification RetellAI | googleSheetsTrigger + 2x webhook | WEBHOOK (callbacks) | Qualifica lead por voz (SMS+ligação) | RetellAI, OpenAI, Sheets, Twilio | lead (nome, tel E.164) |
| 9 | Blog Notion MCP + DeepSeek + WP | notionTrigger | PRECISA-WEBHOOK | Notion update → conteúdo IA → WP | Notion, DeepSeek, WordPress | página Notion |
| 15 | YouTube Trend Finder | chatTrigger | PRECISA-WEBHOOK | Acha vídeos em tendência por nicho | OpenAI, YouTube API | nicho |
| 16 | Newsletter tech RSS+OpenAI+Gmail | scheduleTrigger x2 | PRECISA-WEBHOOK | Newsletter semanal personalizada | RSS, OpenAI, Gmail | feeds RSS |
| 17 | Gmail auto-responder (drafts) | gmailTrigger | PRECISA-WEBHOOK | Cria rascunho de resposta IA | Gmail, OpenAI | e-mail recebido |
| 27 | Flux AI Image Generator | formTrigger (flux4free) | PRECISA-WEBHOOK | Gera imagem com Flux | Flux, HTTP | prompt imagem |
| 28 | Instagram trends + imagem IA | scheduleTrigger | PRECISA-WEBHOOK | Trends IG → imagem IA → posta IG | RapidAPI, Replicate, IG Graph, Telegram | hashtag/tópico |
| 33 | Multi-Platform Social Content | chatTrigger + executeWorkflowTrigger | EXECUTE-WORKFLOW | Posts X/IG/FB/LinkedIn/Threads + imagem | OpenAI, Blotato, imgbb, Drive | tema |
| 35 | Google Calendar Assistant | chatTrigger | PRECISA-WEBHOOK | Cria/consulta eventos por linguagem natural | OpenAI, Google Calendar | comando NL |
| 37 | LinkedIn posts + aprovação email | scheduleTrigger | PRECISA-WEBHOOK | Gera post LinkedIn c/ aprovação por e-mail | OpenAI, Sheets, Gmail, LinkedIn | temas (planilha) |
| 56 | Animated Stories (MJ+Kling) | manualTrigger | PRECISA-WEBHOOK | Roteiro→imagens→vídeo montado | GPT-4o-mini, Midjourney, Kling, Creatomate | tema |
| 81 | Discord control via GPT4o+MCP | chatTrigger | PRECISA-WEBHOOK | Controla Discord por linguagem natural | GPT-4o, MCP Client | comando NL |
| 84 | Gmail MCP Server | mcpTrigger (gmail-enhanced) | WEBHOOK (MCP) | Toolkit Gmail exposto via MCP | Gmail, MCP | chamadas MCP |
| FB | Facebook Ads → Gemini → Sheets | manualTrigger | PRECISA-WEBHOOK | Analisa ads FB e grava insights | FB Graph, NocoDB, Gemini, Sheets | Ad Account ID, Sheet ID |
| ⚠ | **CALLIMA** (produto comercial) | webhook POST + executeWorkflowTrigger | **OBSERVAR — não disparar** | Agente vendas WhatsApp | Evolution API, OpenAI, Gemini, Claude, Postgres, Redis | payload Evolution |

## Leitura estratégica

- **Quase nenhum é disparável como veio.** A maioria usa Schedule/Manual/Telegram/
  Chat/Form/Gmail/Notion trigger. Pra Sexta-feira disparar via prompt, cada padrão
  precisa de uma **porta de entrada Webhook** (ou virar sub-workflow com
  executeWorkflowTrigger).
- **CALLIMA = observar, não disparar nem personificar.** Tem webhook próprio (Evolution).
- **Serviços por frequência (priorizar credenciais/MCP):** OpenAI → Blotato →
  Google (Sheets/Gmail/Calendar/Drive/Gemini) → Telegram → WordPress → geradores de
  mídia (Veo3/Seedance/Flux/Replicate/Midjourney/Kling/Creatomate).

## Categorias
- Vídeo social/auto-post: 1, 2, 3, 6, 56, 33(parcial)
- Posts multi-plataforma: 33, 37
- Imagem IA: 27, 28
- Blog/escrito: 7, 9
- E-mail: 16, 17, 84
- Leads/vendas: 8, CALLIMA(comercial)
- Calendário: 35 · Trends: 15 · ChatOps: 81 · Ads: FB
