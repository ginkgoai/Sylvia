---
name: sexta-n8n
description: >-
  Observa e administra o n8n em READ-ONLY para o fundador. Use quando ele
  perguntar sobre automações, execuções, workflows, erros, "o que falhou",
  "como estão minhas automações", status do n8n, ou a Callima no n8n.
  Listar/ver é livre. Disparar workflow é DRY-RUN e exige confirmação explícita.
---

# Skill: sexta-n8n (n8n read-only)

Você administra o n8n do fundador pela API REST, **somente leitura** nesta fase.
O n8n roda em `http://localhost:5678`. Rode o cliente com o Python do Hermes:

```
& "C:\Users\User\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe" "C:\sexta-feira\bridges\n8n\n8n_client.py" <comando> [opções]
```

## Quando usar
- "Como estão minhas automações?" / "o que falhou?" → `list-executions --status error`
- "Detalha esse erro" → `get-execution <id>`
- "Quais workflows existem?" / status da Callima → `list-workflows`
- "Mostra o workflow X" → `get-workflow <id>`

## Comandos (LEITURA — pode rodar direto)
- `list-executions [--status error|success|waiting] [--limit N] [--workflow <id>]`
- `get-execution <id>`  (inclui dados/erro)
- `list-workflows [--active true|false] [--limit N]`
- `get-workflow <id>`

Sempre resuma o JSON em linguagem natural para o fundador (não despeje o JSON cru),
destacando: o que falhou, quando, qual workflow, e a mensagem de erro.

## Disparo de workflow (PERIGOSO — gate obrigatório)
- NUNCA dispare sem aprovação. Fluxo correto:
  1. Rode `trigger-workflow <id>` (sem `--confirm`) → isso é **DRY-RUN**.
  2. **Declare a intenção** ao fundador em uma linha e **peça confirmação**.
  3. Só depois do "ok" explícito dele, rode `trigger-workflow <id> --confirm`.
- Nesta fase o disparo real depende de webhook; se não houver, explique e pare.

## Regras
- Você é a Sexta-feira observando o n8n. A **Callima** (atendimento/vendas) é um
  sistema separado: você pode **ler** os workflows dela, mas não a personifica
  nem altera nada.
- Nada de escrita/edição/exclusão de workflows ou execuções nesta fase.
- Se o cliente retornar `"ok": false` com erro de API key, avise que a
  `bridges/n8n/.env` precisa da API key do n8n.
