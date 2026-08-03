# Checklist de Credenciais — cascas n8n

Configure cada credencial no n8n (Credentials → New) e marque aqui. Os workflows
só EXECUTAM se a credencial existir; o disparo da Sexta-feira só funciona depois.

## Núcleo (prioridade alta — usados em quase tudo)
- [ ] **OpenAI** (GPT-4/4o/4o-mini, embeddings) — platform.openai.com — usado em: 1,2,3,6,7,15,16,17,28,33,35,37,56,81 (quase todos)
- [ ] **Blotato** (publicação multi-rede) — blotato.com — usado em: 1,2,3,6,33
- [ ] **Google** (OAuth: Sheets/Gmail/Calendar/Drive) — console.cloud.google.com — usado em: 2,3,8,16,17,35,37,33,FB
- [ ] **Telegram Bot** (entrada/notif. — separado do bot da Sexta-feira) — @BotFather — usado em: 1,6,28
- [ ] **WordPress** (app password) — seu site WP — usado em: 7,9

## Geradores de mídia (por pilar de vídeo/imagem)
- [ ] **Veo3** (Google AI vídeo) — 2
- [ ] **Seedance** — 3
- [ ] **PiAPI** (DiffRhythm música) — 6
- [ ] **Flux** (Together AI / HuggingFace) — 27
- [ ] **Replicate** (imagem) — 28
- [ ] **Midjourney** + **Kling** + **Creatomate** — 56

## Pesquisa / dados
- [ ] **Perplexity** — 1,7
- [ ] **YouTube Data API** — 15
- [ ] **RapidAPI** (instagram-scraper-api2) — 28
- [ ] **RSS** (sem key; só feeds) — 16

## Específicos
- [ ] **RetellAI** + **Twilio** (voz/SMS) — 8
- [ ] **DeepSeek** (via OpenRouter) — 9
- [ ] **Notion** (integration token) — 9
- [ ] **Instagram Business** (Graph API / Meta) — 28
- [ ] **LinkedIn** (OAuth) — 37
- [ ] **imgbb** (host de imagem) — 33
- [ ] **Discord Bot** + **MCP Discord** — 81
- [ ] **Facebook Graph** (Marketing API) + **NocoDB** + **Google Gemini** — FB

## CALLIMA (comercial — já configurado, NÃO mexer)
Evolution API, OpenAI, Gemini, Claude, Postgres, Redis. Sexta-feira só observa.

---
Ordem sugerida de ativação dos pilares:
1. OpenAI + Google (destrava a maioria).
2. Blotato + Telegram (pilar vídeo social: 1,2,3,6,33).
3. WordPress (blog: 7,9).
4. Geradores de mídia conforme for ligar cada casca de vídeo/imagem.
