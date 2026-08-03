# n8n → sexta.status_events (nó de escrita)

A Sexta-feira LÊ `sexta.status_events`. Quem ESCREVE é o n8n, no fim de cada
workflow (sucesso e falha). Adicione os nós abaixo na CALLIMA (e nos demais
workflows relevantes).

## 1. Credencial Postgres no n8n (uma vez)
n8n → Credentials → New → **Postgres**:

- Host: `postgres`        (nome do serviço na rede docker; NÃO use localhost)
- Database: `aistack_db`
- User: `sexta_app`
- Password: (rode `Get-Content C:\sexta-feira\.sexta_db_pw.txt` e cole o valor após o `=`)
- Port: `5432`   ·   SSL: `disable`

> `sexta_app` só tem INSERT/SELECT em `sexta.status_events` — não consegue
> escrever em mais nada. É proposital (menor privilégio).

## 2. Nó de SUCESSO (fim do fluxo feliz)
Node **Postgres** → Operation: **Execute Query**:

```sql
INSERT INTO sexta.status_events (source, job_ref, status, payload)
VALUES (
  'n8n',
  '{{ $workflow.id }}',
  'done',
  json_build_object(
    'workflow', '{{ $workflow.name }}',
    'execution_id', '{{ $execution.id }}'
  )::jsonb
);
```

## 3. Nó de FALHA (caminho de erro)
No workflow, ligue um node **Postgres** ao output de erro (ou use um
**Error Trigger** separado), Operation **Execute Query**:

```sql
INSERT INTO sexta.status_events (source, job_ref, status, payload)
VALUES (
  'n8n',
  '{{ $workflow.id }}',
  'failed',
  json_build_object(
    'workflow', '{{ $workflow.name }}',
    'execution_id', '{{ $execution.id }}',
    'error', '{{ $json.error || "erro" }}'
  )::jsonb
);
```

## 4. Validar
Depois de uma execução, a Sexta-feira deve ver a linha:
```
status_reader.py recent --source n8n
```
ou pergunte no Telegram: "como estão minhas automações?"

> Dica: para um Error Trigger global que cobre TODOS os workflows de uma vez,
> crie um workflow "Sexta · Error Sink" com um **Error Trigger** + este nó de
> falha; assim qualquer workflow que quebrar grava em status_events sem você
> editar cada um.
