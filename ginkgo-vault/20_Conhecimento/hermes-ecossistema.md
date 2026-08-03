# Ecossistema Hermes Agent — achados (clips, 2026-06-12)

> Síntese dos clippings que o fundador salvou em `Clippings/`. Relevante para o **Jarvis (Sexta-feira)**, que roda no Hermes Agent (Nous). Alimenta a decisão de billing e o Sprint E.

## Sacada principal
Muito do "Jarvis TODO" **já é nativo no Hermes**: gateways de **Telegram, Discord e WhatsApp**, **MCP nativo**, **cron**, **learning loop + Curator** (ciclo 7 dias), **routing de provider com fallback**, **profiles multi-instância**. → encurta o Sprint E e sugere reavaliar quanto do bot Discord custom é preciso.

## Mapeado nas decisões pendentes
- **P0 (segredos):** `hermes-ops-kit` traz gestão de segredos (Bitwarden/Vaultwarden) + auditoria MCP → forma durável de resolver os tokens vazados.
- **P4 (billing grátis→Claude):**
  - `deepclaude` (DeepSeek/OpenRouter, "17x mais barato") serve **só ao agente de código** (Claude Code) — **não ao Jarvis/Cowork** (proxy não suporta MCP nem visão).
  - `rtk-hermes`: −60–90% de tokens de shell, zero config.
  - **Claude Fable 5**: Hermes já suporta (`/model anthropic/claude-fable-5`). Estratégia: Fable 5 p/ `/goal` complexos, modelos baratos no cron.
- **Memória / reflexão (Fase 8):** `self-improving` (padrão `.learnings/`), `personal-api` (vault Obsidian → identidade do agente), `SkillClaw` (auto-evolui skills c/ rollback).
- **Orquestração:** `mission-control` (cockpit + custo), `CorpusIQ` (36+ conectores via MCP), `web-researcher`/`relay-for-telegram` (HermesHub).
- **Voz (Orb):** GAP confirmado — montar por fora (Whisper + TTS).

## HermesHub
Registro curado de skills da comunidade (`hermeshub.xyz`), com scanner de segurança antes de listar. Instala via `hermes skills install github:amanning3390/hermeshub/skills/<nome>`. Padrão aberto agentskills.io.

## TOP 5 para adotar
1. personal-api · 2. rtk-hermes · 3. hermes-ops-kit · 4. self-improving (.learnings) · 5. mission-control.

## Caveats
Sem skill nativa de n8n/AnythingLLM/Postiz (vão por MCP/webhook). Muita coisa é beta. Parte é OpenClaw/cross-platform, não Hermes-puro.
