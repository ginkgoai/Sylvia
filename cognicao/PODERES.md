# Poderes plugáveis da Sylvia — arsenal e disparo determinístico

> A Sylvia é copilota com acesso informativo amplo e poderes de execução **estreitos, nomeados e auditáveis**. Poder não listado aqui não existe. Cada poder mapeia para um nível de `AUTONOMIA.md`.

## Arsenal disponível (stack Docker `leaf` + serviços)

| Poder | Acesso | Nível | Implementação |
|---|---|---|---|
| **n8n — ler** (workflows, execuções, status) | API n8n read-only | A0 | `runtime/bridges/n8n/` (cliente pronto) |
| **n8n — disparar fluxo** | Webhook/API por fluxo **allowlisted** | A2/A3* | runbook por fluxo (ver abaixo) |
| **Postgres — consultar** (leaf, status_events, métricas) | usuário read-only | A0 | `runtime/bridges/db/` |
| **Postgres — escrever** | somente `sexta.status_events` (append-only) | A2 | role `sexta_app` já provada |
| **Redis** | leitura de filas/estado | A0 | via bridge/skill |
| **RAG** (AnythingLLM ou sucessor) | consulta à base indexada | A0 | `runtime/bridges/rag/` |
| **APIs externas — ler** (agenda, e-mail, métricas de canal) | credencial fora do repo | A0 | MCPs/skills, uma a uma |
| **APIs externas — escrever** (enviar, publicar, alterar) | idem | **A3** | sempre gate ou runbook |
| **MCPs** | conforme plugado | herda o nível da ação | catálogo mantido aqui |
| **Filesystem do workspace** | ler/escrever neste repo | A2 | ferramentas nativas do runtime |
| **Git** | add/commit local; **push com aprovação** | A2 / A3 | rotina de memória |

\* Disparo de fluxo n8n é A2 quando o fluxo é interno e reversível (ex.: gerar relatório, reindexar RAG) e **A3 quando o fluxo toca o mundo externo** (mensagem, publicação, gasto, dado de cliente).

## Padrão de disparo determinístico (runbook de fluxo)

Todo fluxo que a Sylvia pode disparar sozinha precisa de um runbook em `cognicao/runbooks/`, confirmado pelo fundador em `Decisoes/`:

```markdown
# Runbook — <nome do fluxo>
- Fluxo n8n: <id/nome do workflow> · Webhook: <rota, sem token>
- O que faz (1 frase) · Efeito externo: sim/não
- Nível: A2 | A3-pré-aprovado
- Limites: volume máx/dia, horário, escopo de dados
- Gatilho permitido: pedido do fundador | heartbeat | condição X
- Registro: entrada no ledger + linha no diário (obrigatório)
- Aborto: como interromper e como reverter
```

Sem runbook escrito e confirmado, o disparo exige aprovação explícita na conversa (uma linha de intenção + "ok").

## Ordem de construção das skills (workspace `skills/`)

1. `sylvia-status` — lê `sexta.status_events` e saúde do stack (A0). Base: skill Hermes existente.
2. `sylvia-n8n` — lista workflows e execuções, read-only (A0).
3. `sylvia-rag` — consulta RAG (A0).
4. `sylvia-flows` — dispara **apenas** fluxos com runbook, validando allowlist antes (A2/A3).
5. Conectores MCP (agenda, e-mail, métricas) — leitura primeiro; escrita só com gate.

## Regras

1. Credencial nunca no workspace: env/`~/.openclaw/`/gerenciador de segredos. Os bridges leem de `.env` locais (gitignorados).
2. Todo disparo deixa rastro: ledger (`action`) + diário do dia. Sem rastro = incidente.
3. Falha de ferramenta não vira retry infinito: 2 tentativas, depois reportar.
4. Novo poder = proposta da Sylvia → runbook → confirmação do fundador → entra nesta tabela via commit. Nada entra "por conveniência" no meio de uma tarefa.
