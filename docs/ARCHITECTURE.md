# Sexta-feira — Arquitetura (Fase 1: "a espinha")

> **HISTÓRICO — arquitetura v1.** Este documento preserva o desenho original da Sexta-feira com Hermes como core. A arquitetura atual da Sylvia mantém **OpenClaw como cérebro/runtime principal** e reposiciona **Hermes como execution runtime governado**. Ver `SYLVIA.md` e `docs/feature_sylvia_execution_fabric.md`. Não usar este arquivo como fonte atual para a divisão de responsabilidades OpenClaw/Hermes.

Orquestrador pessoal autônomo do fundador (Gabriel). NÃO é produto, NÃO atende
clientes. Fica por cima do stack `leaf` e comanda os braços executores.

> **CALLIMA ≠ SEXTA-FEIRA.** Callima é o produto comercial (atendimento/vendas
> via WhatsApp na Evolution API + n8n, número comercial). Sexta-feira pode
> **observar** a Callima, mas nunca a personifica nem compartilha toolset.

## Diagrama

```
            FUNDADOR (Gabriel)
                  │
      ┌───────────┴───────────┐
 Dashboard Orb            Telegram
 (voz+texto, web)         (adapter nativo Hermes)
      │  HTTP OpenAI-compat       │
      └───────────┬───────────────┘
                  ▼
        ┌────────────────────┐
        │   HERMES AGENT     │  core (Nous Research, MIT) — NATIVO no Windows
        │  gateway + loop    │
        └─────────┬──────────┘
   tools/skills:  │
   ┌───────┬──────┴───────┬───────────────┐
   ▼       ▼              ▼               ▼
 Claude   n8n REST     AnythingLLM    sexta.status_events
 (API)    (read-only)  (RAG)          (Postgres leaf)
 +MCP
```

## Decisões travadas (Fase 1)

| Tema | Decisão | Motivo |
|---|---|---|
| Runtime Hermes | **Nativo Windows (install.ps1)** | Doc oficial confirma suporte nativo (CLI, gateway, MCP, cron, browser). Só o painel PTY do dashboard é WSL2-only — não usamos. |
| Local do projeto | **C:\sexta-feira** (sem espaços) | §7: paths com espaço quebram tooling Node (Orb e Hermes). Isolado do `compose stack`. |
| Nome "hermes" | Stub FastAPI **aposentado** do leaf | Evitar colisão. "Hermes" = agente Nous. n8n/Postgres/Redis/Evolution = braços. |
| Provider do cérebro | **Anthropic API key direta** | Acesso direto aos modelos Claude. |
| Canal do Orb | **API Server OpenAI-compatible do Hermes** | Documentado (`hermes-api-server`, "Open WebUI + API Server"). Sem inventar protocolo. |
| Status store | `sexta.status_events` no Postgres do leaf | Schema dedicado; role `sexta_app` só INSERT+SELECT (append-only §5). |

## Divergências spec × ferramenta (registradas)

1. **Windows nativo é suportado** (README do Hermes diz "só WSL2", mas a doc atual tem `install.ps1`). Usamos nativo.
2. **Hermes não é serviço docker-compose** — instala via installer e roda como CLI/gateway. O `docker-compose.yml` do projeto cobre só o que é container (Orb); o leaf continua sendo o stack existente.
3. **Hermes tem cron próprio** — conflita com "um relógio só (BullMQ)". Em Fase 1 autonomia está OFF; decidir o relógio único na Fase 2.

## Gates de segurança (Fase 1)

- Toda ação com efeito colateral (enviar email, criar evento, disparar workflow)
  **declara intenção e pede confirmação** antes de executar.
- n8n: **read-only**. Disparo de workflow só com confirmação (dry-run por padrão).
- `status_events`: **append-only**, `sexta_app` sem UPDATE/DELETE/TRUNCATE (provado).
- Ads / gasto de dinheiro / escrita autônoma em prod: **fora de escopo**, não existe no código.

## Fora de escopo (Fase 1)

Meta/Google Ads, escrita autônoma em banco de prod, jobs cron autônomos
(só preparar o gancho BullMQ), relatório completo de consumo de tokens.
Não tocar no workflow CALLIMA nem no número comercial.
