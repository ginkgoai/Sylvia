# ROADMAP — Fase 1 (a espinha) + além

## Critérios de aceite da Fase 1 (status)
1. Falar com a Sexta-feira por Dashboard Orb (voz+texto) e Telegram, com 4 estados do orb.
   → Telegram + persona: **OK** (modelo grátis). Orb: **pendente**.
2. "Manda email de teste" → declara intenção + pede confirmação → executa via MCP Gmail.
   → **pendente** (ponte Claude + MCP Gmail/Calendar com gate).
3. "Como estão minhas automações" → lê status_events e resume.
   → leitor + skill **OK**; falta n8n ESCREVER em status_events (nó na CALLIMA) + teste via bot.
4. Pergunta à base → consulta AnythingLLM e responde com fonte.
   → fiação **OK**; falta motor do AnythingLLM (Native + Nous) + docs.
5. Nada irreversível/gasto sem confirmação; Ads não existem no código. → **mantido**.
6. status_events recebe linhas reais do n8n ao fim das execuções. → **pendente** (nó de escrita).

## Trabalho paralelo (produto CALLIMA)
- Config nó-a-nó + fixes estruturais + buffer guard + ramo documento.
- Publicar Callima como agente de vendas WhatsApp.

## Fases futuras (NÃO agora)
- Conversão das 18 cascas em workflows disparáveis pela Sexta-feira (Webhook + registry + trigger gated).
- Meta/Google Ads (budget_guardian + spend_approval_gate + audit log) — gasto real.
- Relógio único (BullMQ vs cron do Hermes) + jobs autônomos.
- Trocar provider p/ Claude (qualidade) + roteamento Haiku/Sonnet/Opus.
- Memória longa avançada / honcho; relatório de consumo de tokens.
