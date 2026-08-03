---
title: "GKO - Configuração nós saída"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/68fdb6eb-99a0-8331-8da1-39cb87768714"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
dom., 26 de out. às 2:51

![c6b10eca-7c70-4ae9-8573-12c3d85b6f4a.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000312c620e8a497a61de51b888&ts=495692&p=fs&cid=1&sig=bb7887796fc348d47ff47d9498ef4d2d44466ddac89f00d528dc2af0cc04ac4c&v=0)

4

![68cfbb86-17c9-4ab9-b380-bb40c0c37c22.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000783061f592b9ad87d136ffdc&ts=495692&p=fs&cid=1&sig=b143c7ad36c46174375df023cb633a971b2efa0fcc3f2bdd357032f00466f015&v=0) ![b224dd8c-211e-4438-9bc5-f226d5a17685.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000af0861f5ad9d748192718369&ts=495692&p=fs&cid=1&sig=7cd35554457563aa17c0c159f17b319c018f41ae42680ca1774bc2dfa26895c9&v=0) ![4fe8dcd8-3dfb-479d-a29f-daba4c34e36a.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000553061f586d98294975273dc&ts=495692&p=fs&cid=1&sig=8a36de49f1cc7a431839b89b5f59784429e14353abd3f40025a8df3cf259677b&v=0) ![e9a0cfa0-a72c-4a3f-9523-760688fb29ae.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000d1b461f597bcfe8047d262da&ts=495692&p=fs&cid=1&sig=6ce8f49209cc1fbad78027174d18cdf55627734b022ca86e9130baac9125554c&v=0)

Ajuste prático para padronizar os dois nós Evolution (envio único e envio em loop):

---

### 🔹 Evolution (único)

Usado quando `out_list.length == 1`

**Parâmetros:**

- **Recurso:** `Mensagem`
- **Operação:** `Enviar Texto`
- **Nome da Instância:**
	```markdown
	{{ $json.instance || 'BRANN' }}
	```
- **Número do Destinatário:**
	```markdown
	{{ $json.phone }}
	```
- **Mensagem:**
	```markdown
	{{ $json.out_list[0] || $json.text || '' }}
	```

---

### 🔹 Evolution1 (loop)

Usado dentro do `Loop Over Items`

**Parâmetros:**

- **Recurso:** `Mensagem`
- **Operação:** `Enviar Texto`
- **Nome da Instância:**
	```markdown
	{{ $json.instance || 'BRANN' }}
	```
- **Número do Destinatário:**
	```markdown
	{{ $json.phone }}
	```
- **Mensagem:**
	```markdown
	{{ $json.segment }}
	```

---

### 🔸 Observações

1. Ambos usam a mesma **credencial** (ex.: `Evolution account 2`).
2. O `segment` vem do Split Out.
3. Não use campos `{{ $Parametros API }}` — remova isso, use só `$json`.
4. No fluxo principal, mantenha a decisão pelo `IF`:
	- **true:** envia pelo loop (`Split Out` → `Loop` → `Evolution1` → `Wait`)
		- **false:** envia direto (`Evolution`).

---

Se quiser, posso gerar o **JSON do bloco DISPARO completo** pronto para importar no n8n. Deseja isso agora?

![f0ce4e72-b3ea-4fc9-9553-bb047efeafa9.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000b12c61f59d2f51bb78a99db3&ts=495692&p=fs&cid=1&sig=cd1b4c002cf191916fcb4826487a26671c8d4ce63b498fa664422eaa9db43c74&v=0)

agora olhando o fluxo geral esta faltando algum node ou tool?

Sim. Estão faltando 6 pontos críticos para ficar robusto:

1. Antiduplicação de envio  
	Inserir antes do bloco SAÍDA, após o Buffer. Node: **Function** “Dedup Msg”.
```markdown
// evita reenvio por messageId/phone por 10 min
const { messageId, phone } = $json;
const key = \`${phone}:${messageId}\`;
const ttlMs = 10*60*1000;
const now = Date.now();
const seen = $flow.get(key) || 0;
if (now - seen < ttlMs) return []; // drop
$flow.set(key, now);
return [{ json: $json }];
```
2. Rate limit por destinatário  
	Entre `Loop Over Items` e `Evolution1`. Node: **Function** “Per-Number Throttle”.
```markdown
const minGapMs = 1200; // 1,2 s
const k = \`rl:${$json.phone}\`;
const last = $flow.get(k) || 0;
const wait = Math.max(0, minGapMs - (Date.now()-last));
$flow.set(k, Date.now()+wait);
return [{ json:{...$json, _extraWait: wait/1000 } }];
```

Ajuste o **Wait** para `={{$json._extraWait || 1.2}}` seconds.

3. Retry com backoff no Evolution (único e loop)  
	Adicionar após cada Evolution um **IF** “Falhou?”
- Condição: `={{$json.statusCode && $json.statusCode >= 400}}`  
	No ramo true: **Function** “BackoffCtl”:
```markdown
const n = ($json._retry||0)+1;
if (n>3) return [{json:{...$json,_giveup:true}}];
const delay = Math.pow(2,n); // 2s,4s,8s
return [{json:{...$json,_retry:n,_delay:delay}}];
```

→ **Wait** `={{$json._delay}}` seconds → volta ao Evolution.  
Se `_giveup`, mande para “Dead-Letter” (item 4).

4. Dead-Letter e observabilidade  
	Criar coleção mínima:
- **Set** “DLQ payload” com campos: `phone, segment || out_list[0], statusCode, error, messageId, ts`
- **HTTP Request** ou **Supabase** (Insert) para tabela `whats_deadletter`.
- **Webhook** opcional para Slack/Discord de alertas.
5. Opt-out e bloqueio manual  
	Antes do SAÍDA, um **IF** “Opt-out”:
- Condição: `={{$json.optOut === true || ($json.text && $json.text.match(/stop|sair|pare/i))}}`  
	True → **Supabase** update `contacts.opt_out=true` e encerra.  
	False → segue.
6. Marcação de leitura e handoff humano  
	No fim do SAÍDA, após sucesso:
- **HTTP Request** Evolution “markAsRead” (se houver) ou “sendPresence: paused”.
- **IF** “handoff = true” vindo do Agent → manda para rota de **Atendimento Humano** já prevista no seu painel.

Extras úteis e rápidos:

- **Metrics**: após cada envio, **Set** `metrics` e **Supabase** insert em `msg_metrics` (`ok|fail`, latência, tentativas).
- **Typing on/off**: já pode enviar via `options.presence` no Evolution; manter.
- **Fallback multimídia**: se `segment.length > 4096`, cortar e encadear como múltiplos segmentos antes do Split Out.

Onde colocar no diagrama:

- Dedup e Opt-out: entre BUFFER → Agent e antes de SAÍDA.
- Retry/Backoff/Dead-Letter: encapsulam cada Evolution.
- Rate limit: entre Loop e Evolution1.
- Metrics/Read/Handoff: ao final do SAÍDA, em série.

Se quiser, envio um JSON do bloco SAÍDA contendo: Split Out + Loop + Evolution1 + Wait + Retry + DLQ + Métricas, pronto para importar.

sim

Segue o bloco **SAÍDA** pronto para importar no n8n. Ele cobre: normalização, envio único ou em lote, throttle por número, retry com backoff, DLQ via webhook e métricas simples.

> Variáveis de ambiente esperadas  
> `EVOLUTION_BASE_URL` • `EVOLUTION_INSTANCE` • `EVOLUTION_TOKEN` • `DLQ_WEBHOOK_URL` • `METRICS_WEBHOOK_URL`

```markdown
{
  "nodes": [
    {
      "parameters": {
        "functionCode": "// Padroniza para { phone, out_list[] }\nconst p = items[0].json || {};\nlet list = [];\nif (Array.isArray(p.out)) list = p.out.filter(Boolean);\nelse if (typeof p.out === 'string') list = [p.out];\nelse if (p.out && typeof p.out === 'object' && typeof p.out.text === 'string') list = [p.out.text];\nelse if (typeof p.text === 'string') list = [p.text];\nreturn [{ json: { ...p, phone: p.phone || p.chatId || '', out_list: list } }];"
      },
      "id": "Normalize Final",
      "name": "Normalize Final",
      "type": "n8n-nodes-base.function",
      "typeVersion": 2,
      "position": [200, 300]
    },
    {
      "parameters": {
        "conditions": {
          "boolean": [],
          "number": [],
          "string": [],
          "collection": [
            {
              "value1": "={{$json.out_list && $json.out_list.length > 1}}"
            }
          ]
        }
      },
      "id": "IF Many?",
      "name": "IF Many?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [420, 300]
    },
    {
      "parameters": {
        "fieldToSplitOut": "out_list",
        "include": "allOtherFields",
        "options": {
          "destinationFieldName": "segment",
          "includeIndex": true,
          "indexFieldName": "segment_index"
        }
      },
      "id": "Split Out",
      "name": "Split Out",
      "type": "n8n-nodes-base.itemLists",
      "typeVersion": 3,
      "position": [640, 170]
    },
    {
      "parameters": {
        "batchSize": 1
      },
      "id": "Loop Over Items",
      "name": "Loop Over Items",
      "type": "n8n-nodes-base.splitInBatches",
      "typeVersion": 2,
      "position": [860, 170]
    },
    {
      "parameters": {
        "functionCode": "// throttle por número\nconst minGapMs = 1200; // 1.2s\nconst k = \`rl:${$json.phone}\`;\nconst last = $flow.get(k) || 0;\nconst now = Date.now();\nconst wait = Math.max(0, minGapMs - (now - last));\n$flow.set(k, now + wait);\nreturn [{ json: { ...$json, _pace: wait/1000 } }];"
      },
      "id": "Throttle",
      "name": "Throttle",
      "type": "n8n-nodes-base.function",
      "typeVersion": 2,
      "position": [1060, 170]
    },
    {
      "parameters": {
        "url": "={{$env.EVOLUTION_BASE_URL}}/message/sendText/{{$env.EVOLUTION_INSTANCE}}",
        "options": {
          "resolveFullResponse": true
        },
        "authentication": "none",
        "responseFormat": "json",
        "jsonParameters": true,
        "sendBody": true,
        "headerParametersJson": "={\"Authorization\":\"Bearer {{$env.EVOLUTION_TOKEN}}\",\"Content-Type\":\"application/json\"}",
        "bodyParametersJson": "={\"number\":\"{{$json.phone}}\",\"options\":{\"delay\":800,\"presence\":\"composing\"},\"textMessage\":{\"text\":\"{{$json.segment}}\"}}",
        "method": "POST"
      },
      "id": "Evolution1",
      "name": "Evolution1",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4,
      "position": [1260, 170]
    },
    {
      "parameters": {
        "conditions": {
          "collection": [
            {
              "value1": "={{$json.statusCode && $json.statusCode >= 400}}"
            }
          ]
        }
      },
      "id": "Fail? (loop)",
      "name": "Fail? (loop)",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [1460, 170]
    },
    {
      "parameters": {
        "functionCode": "// backoff exponencial até 3 tentativas\nconst n = ($json._retry||0)+1;\nif (n>3) return [{ json:{...$json, _giveup:true} }];\nconst delay = Math.pow(2, n); // 2,4,8s\nreturn [{ json:{...$json, _retry:n, _delay:delay} }];"
      },
      "id": "Backoff (loop)",
      "name": "Backoff (loop)",
      "type": "n8n-nodes-base.function",
      "typeVersion": 2,
      "position": [1660, 120]
    },
    {
      "parameters": {
        "resume": "afterTimeInterval",
        "amount": "={{$json._delay || $json._pace || 1.2}}",
        "unit": "seconds"
      },
      "id": "Wait (loop)",
      "name": "Wait (loop)",
      "type": "n8n-nodes-base.wait",
      "typeVersion": 1,
      "position": [1860, 120]
    },
    {
      "parameters": {
        "functionCode": "// métricas simples\nreturn [{ json: { ts: new Date().toISOString(), phone: $json.phone, ok: true, len: ($json.segment||'').length } }];"
      },
      "id": "Metrics (loop)",
      "name": "Metrics (loop)",
      "type": "n8n-nodes-base.function",
      "typeVersion": 2,
      "position": [1660, 220]
    },
    {
      "parameters": {
        "url": "={{$env.METRICS_WEBHOOK_URL}}",
        "options": { "responseFormat": "string" },
        "authentication": "none",
        "jsonParameters": true,
        "sendBody": true,
        "bodyParametersJson": "={{$json}}",
        "method": "POST"
      },
      "id": "POST Metrics (loop)",
      "name": "POST Metrics (loop)",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4,
      "position": [1860, 220]
    },
    {
      "parameters": {
        "functionCode": "// monta DLQ\nreturn [{ json: { ts: new Date().toISOString(), phone: $json.phone, segment: $json.segment, statusCode: $json.statusCode || null, error: $json.body || $json.error || null } }];"
      },
      "id": "DLQ set (loop)",
      "name": "DLQ set (loop)",
      "type": "n8n-nodes-base.function",
      "typeVersion": 2,
      "position": [1660, 300]
    },
    {
      "parameters": {
        "url": "={{$env.DLQ_WEBHOOK_URL}}",
        "options": { "responseFormat": "string" },
        "authentication": "none",
        "jsonParameters": true,
        "sendBody": true,
        "bodyParametersJson": "={{$json}}",
        "method": "POST"
      },
      "id": "POST DLQ (loop)",
      "name": "POST DLQ (loop)",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4,
      "position": [1860, 300]
    },
    {
      "parameters": {
        "url": "={{$env.EVOLUTION_BASE_URL}}/message/sendText/{{$env.EVOLUTION_INSTANCE}}",
        "options": {
          "resolveFullResponse": true
        },
        "authentication": "none",
        "responseFormat": "json",
        "jsonParameters": true,
        "sendBody": true,
        "headerParametersJson": "={\"Authorization\":\"Bearer {{$env.EVOLUTION_TOKEN}}\",\"Content-Type\":\"application/json\"}",
        "bodyParametersJson": "={\"number\":\"{{$json.phone}}\",\"options\":{\"delay\":800,\"presence\":\"composing\"},\"textMessage\":{\"text\":\"{{$json.out_list[0] || $json.text || ''}}\"}}",
        "method": "POST"
      },
      "id": "Evolution (single)",
      "name": "Evolution (single)",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4,
      "position": [640, 440]
    },
    {
      "parameters": {
        "conditions": {
          "collection": [
            {
              "value1": "={{$json.statusCode && $json.statusCode >= 400}}"
            }
          ]
        }
      },
      "id": "Fail? (single)",
      "name": "Fail? (single)",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [860, 440]
    },
    {
      "parameters": {
        "functionCode": "// backoff single\nconst n = ($json._retry||0)+1;\nif (n>3) return [{ json:{...$json, _giveup:true} }];\nconst delay = Math.pow(2, n);\nreturn [{ json:{...$json, _retry:n, _delay:delay} }];"
      },
      "id": "Backoff (single)",
      "name": "Backoff (single)",
      "type": "n8n-nodes-base.function",
      "typeVersion": 2,
      "position": [1060, 400]
    },
    {
      "parameters": {
        "resume": "afterTimeInterval",
        "amount": "={{$json._delay || 1.2}}",
        "unit": "seconds"
      },
      "id": "Wait (single)",
      "name": "Wait (single)",
      "type": "n8n-nodes-base.wait",
      "typeVersion": 1,
      "position": [1260, 400]
    },
    {
      "parameters": {
        "functionCode": "return [{ json: { ts: new Date().toISOString(), phone: $json.phone, ok: true, len: ($json.out_list && $json.out_list[0] ? $json.out_list[0].length : 0) } }];"
      },
      "id": "Metrics (single)",
      "name": "Metrics (single)",
      "type": "n8n-nodes-base.function",
      "typeVersion": 2,
      "position": [1060, 480]
    },
    {
      "parameters": {
        "url": "={{$env.METRICS_WEBHOOK_URL}}",
        "options": { "responseFormat": "string" },
        "authentication": "none",
        "jsonParameters": true,
        "sendBody": true,
        "bodyParametersJson": "={{$json}}",
        "method": "POST"
      },
      "id": "POST Metrics (single)",
      "name": "POST Metrics (single)",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4,
      "position": [1260, 480]
    },
    {
      "parameters": {
        "functionCode": "return [{ json: { ts: new Date().toISOString(), phone: $json.phone, text: ($json.out_list && $json.out_list[0]) || $json.text || '', statusCode: $json.statusCode || null, error: $json.body || $json.error || null } }];"
      },
      "id": "DLQ set (single)",
      "name": "DLQ set (single)",
      "type": "n8n-nodes-base.function",
      "typeVersion": 2,
      "position": [1060, 560]
    },
    {
      "parameters": {
        "url": "={{$env.DLQ_WEBHOOK_URL}}",
        "options": { "responseFormat": "string" },
        "authentication": "none",
        "jsonParameters": true,
        "sendBody": true,
        "bodyParametersJson": "={{$json}}",
        "method": "POST"
      },
      "id": "POST DLQ (single)",
      "name": "POST DLQ (single)",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4,
      "position": [1260, 560]
    }
  ],
  "connections": {
    "Normalize Final": {
      "main": [ [ { "node": "IF Many?", "type": "main", "index": 0 } ] ]
    },
    "IF Many?": {
      "main": [
        [ { "node": "Split Out", "type": "main", "index": 0 } ],
        [ { "node": "Evolution (single)", "type": "main", "index": 0 } ]
      ]
    },
    "Split Out": {
      "main": [ [ { "node": "Loop Over Items", "type": "main", "index": 0 } ] ]
    },
    "Loop Over Items": {
      "main": [ [ { "node": "Throttle", "type": "main", "index": 0 } ] ]
    },
    "Throttle": {
      "main": [ [ { "node": "Evolution1", "type": "main", "index": 0 } ] ]
    },
    "Evolution1": {
      "main": [ [ { "node": "Fail? (loop)", "type": "main", "index": 0 } ] ]
    },
    "Fail? (loop)": {
      "main": [
        [ { "node": "Backoff (loop)", "type": "main", "index": 0 } ],
        [ { "node": "Metrics (loop)", "type": "main", "index": 0 } ]
      ]
    },
    "Backoff (loop)": {
      "main": [ [ { "node": "Wait (loop)", "type": "main", "index": 0 } ] ]
    },
    "Wait (loop)": {
      "main": [ [ { "node": "Evolution1", "type": "main", "index": 0 } ] ]
    },
    "Metrics (loop)": {
      "main": [ [ { "node": "POST Metrics (loop)", "type": "main", "index": 0 } ] ]
    },
    "Fail? (single)": {
      "main": [
        [ { "node": "Backoff (single)", "type": "main", "index": 0 } ],
        [ { "node": "Metrics (single)", "type": "main", "index": 0 } ]
      ]
    },
    "Backoff (single)": {
      "main": [ [ { "node": "Wait (single)", "type": "main", "index": 0 } ] ]
    },
    "Wait (single)": {
      "main": [ [ { "node": "Evolution (single)", "type": "main", "index": 0 } ] ]
    },
    "Metrics (single)": {
      "main": [ [ { "node": "POST Metrics (single)", "type": "main", "index": 0 } ] ]
    },
    "Evolution (single)": {
      "main": [ [ { "node": "Fail? (single)", "type": "main", "index": 0 } ] ]
    },
    "POST Metrics (loop)": { "main": [ [ { "node": "Loop Over Items", "type": "main", "index": 0 } ] ] },
    "DLQ set (loop)": { "main": [ [ { "node": "POST DLQ (loop)", "type": "main", "index": 0 } ] ] },
    "POST DLQ (loop)": { "main": [ [ { "node": "Loop Over Items", "type": "main", "index": 0 } ] ] },
    "DLQ set (single)": { "main": [ [ { "node": "POST DLQ (single)", "type": "main", "index": 0 } ] ] }
  },
  "meta": { "instanceId": "" },
  "pinData": {}
}
```

Importe como novo workflow e ligue a entrada do seu **BUFFER/Agent** no nó **Normalize Final**.  
Se quiser trocar `webhook` de métricas/DLQ por Supabase, diga que eu envio as versões com inserts REST.