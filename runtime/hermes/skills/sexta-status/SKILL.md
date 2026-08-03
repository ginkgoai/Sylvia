---
name: sexta-status
description: >-
  Fonte de verdade de status, consumo e jobs (tabela sexta.status_events).
  Use quando o fundador perguntar "como estão minhas automações", "o que rodou
  hoje", "o que falhou", "resumo de status", "consumo", "quanto gastei",
  ou pedir um panorama das execuções/jobs recentes. SOMENTE LEITURA.
---

# Skill: sexta-status (status_events read-only)

`sexta.status_events` (Postgres do leaf) é a **fonte única de verdade** de
status/consumo/jobs. Você só LÊ — o role `sexta_app` não tem permissão de
escrita (append-only é garantido no banco). Rode com o Python do Hermes:

```
& "C:\Users\User\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe" "C:\sexta-feira\bridges\db\status_reader.py" <comando> [opções]
```

## Comandos
- `recent [--limit N] [--source n8n|hermes|claude_api|bullmq] [--status done|failed|running|...]`
  → últimos eventos (mais recentes primeiro).
- `summary [--hours N]` → contagem por source/status na janela (default 24h).

## Como responder
- "Como estão minhas automações?" → `summary --hours 24` e, se houver falhas,
  complemente com `recent --status failed` e resuma em linguagem natural
  (quantas rodaram, quantas falharam, o que precisa de atenção).
- "O que falhou?" → `recent --status failed`.
- Para detalhe técnico de uma execução do n8n, combine com a skill **sexta-n8n**
  (`get-execution <id>`).
- Sempre resuma; não despeje JSON cru. Se `cost_usd` aparecer, some e reporte o gasto.

## Regras
- Nunca tente UPDATE/DELETE — não há permissão e é proibido (append-only §5).
- Se vier `"ok": false`, explique o erro (ex.: container parado, senha ausente).
