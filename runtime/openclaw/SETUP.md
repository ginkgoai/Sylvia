# OpenClaw — runtime da Sylvia (setup)

> Decisão 2026-08-03: OpenClaw é o runtime principal da Sylvia; a cognição permanece agnóstica neste repo. Confirme comandos na doc oficial (docs.openclaw.ai) — o projeto evolui rápido.

## Por que OpenClaw

- Sempre ativo: gateway local com Telegram, WhatsApp e outros canais → **comunicável**.
- Heartbeat e cron nativos → **proatividade** (implementa `cognicao/HEARTBEAT.md`).
- Memória em arquivos markdown no workspace → casa 1:1 com esta cognição.
- Skills e ferramentas plugáveis (bash, browser, MCPs, APIs) → **poderes plugáveis** (n8n, Postgres, Redis via `runtime/bridges/`).
- Multi-agente no roadmap do projeto → **delegação futura** (Sylvia coordenando sub-agentes).

## Instalação (Windows)

1. Recomendado rodar no **WSL2** (Ubuntu) ou Docker — evita atrito de tooling no Windows nativo.
2. Node 22+ instalado, então: `npm install -g openclaw@latest` e rode o onboarding: `openclaw onboard` (configura provider, gateway e canais).
3. Provider: **Anthropic (Claude)** com a API key do fundador. Pendência conhecida: billing definido (ver CHECKPOINT).

## Ligando a cognição (este repo)

O OpenClaw usa um workspace (por padrão `~/.openclaw/workspace`) com `AGENTS.md`, `SOUL.md` e arquivos de memória. Estratégia:

1. Clonar este repo dentro do ambiente do OpenClaw (ex.: `~/sylvia`) e **apontar/sincronizar o workspace para ele** — os `AGENTS.md` e `SOUL.md` da raiz já são os arquivos de boot que o OpenClaw procura.
2. Alternativa simples: copiar `AGENTS.md` + `SOUL.md` para o workspace e manter neles apenas ponteiros para o repo (já estão escritos assim).
3. Memória do dia-a-dia continua sendo escrita em `ginkgo-vault/00_Cerebro/` conforme `cognicao/MEMORIA.md`; commits regulares preservam a evolução (memória versionada).

## Canais

1. **Telegram primeiro**: criar bot novo no @BotFather (ex.: `@SylviaExecBot`) — não reaproveitar o bot "Friday" do Hermes até desativá-lo, para não haver duas mentes no mesmo canal.
2. **Allowlist obrigatória**: somente o user id do fundador (7318821830). Sem grupos, sem DMs de terceiros.
3. WhatsApp depois, quando a rotina Telegram estiver estável (usar número dedicado, nunca o comercial do Leaf).

## Segurança (inegociável)

- Allowlist de remetentes em todos os canais; pairing desligado para desconhecidos.
- Ferramentas com efeito externo só via gates de `cognicao/AUTONOMIA.md` — configurar aprovação para exec sensível.
- Credenciais em variáveis de ambiente/gerenciador do próprio OpenClaw; **nunca** no workspace/repo.
- Gateway apenas local (não expor porta na internet); atualizações do OpenClaw acompanhadas (projeto novo, patches frequentes).

## Heartbeat e cron

- Heartbeat: instruções de `cognicao/HEARTBEAT.md` (briefing diário útil, `HEARTBEAT_OK` quando não houver nada).
- Cron: triagem semanal de clippings, fechamento financeiro semanal, auditoria mensal de acessos.

## Migração do Hermes (legado)

| Item | Destino |
|---|---|
| Bot Telegram "Friday" | Desativar após Sylvia estável no novo bot. |
| `runtime/hermes/config/SOUL.md` | Substituído pelo `SOUL.md` da raiz. |
| Skills `sexta-*` | Recriar como skills OpenClaw usando `runtime/bridges/` (n8n read-only, status, RAG). |
| `runtime/hermes-memory-compat/` | Congelado; memória canônica é o vault. |
| Instalação `%LOCALAPPDATA%\hermes` | Remover quando a migração for confirmada. |

## Critério de pronto (Fase 1 da Sylvia)

1. Sylvia responde no Telegram com a persona do `SOUL.md` e boot do `AGENTS.md`.
2. Lê e escreve memória no vault conforme protocolo.
3. Heartbeat diário entrega briefing executivo real (ou silêncio consciente).
4. Nenhuma ação A3 executada sem aprovação registrada.
