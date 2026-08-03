---
title: "GKO - Integração Alphie Trello"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/68fb11d3-f464-8333-9135-f6b78fcd887b"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sex., 24 de out. às 2:42

Agora me ajude a visualizar o seguinte. Alphie funcional modo local ollama com toda a persona dele, instruções, e grande conhecimento sobre a ginkgo e operações. Com aquela função de deixar ele online em rede eu consigo fazer uma integração dele com o aplicativo Trello, para ele operar instruções para o usuário/disparar avisos, mensagens prontas no whatsapp quando necessário fazer alguma atividade.

Sim. Arquitetura enxuta e operável agora.

## Visão-geral

- **Input**: eventos do Trello + mensagens do usuário.
- **Alavancas**: Alphie local (Ollama) + RAG da Ginkgo + n8n para orquestração + Evolution API para WhatsApp.
- **Output**: criar/atualizar cards, comentar, disparar avisos no WhatsApp, lembrar prazos.

## Stack mínima

- **Compute**: VPS ou máquina local com Docker.
- **IA**: Ollama (`llama3.1:8b` ou `qwen2.5:7b`), `nomic-embed-text` para vetores.
- **RAG**: SQLite/Chroma local.
- **Orquestração**: n8n.
- **Apps**: Trello API, Evolution API (WhatsApp), opcional Kokoro TTS.

---

## 1) Alphie local com persona e rede

**Modelfile** (persona + regras):

```markdown
FROM llama3.1:8b
SYSTEM:
Você é o Alphie, operador interno da Ginkgo. Objetivo: executar rotinas operacionais, monitorar prazos no Trello, sugerir próximos passos e notificar no WhatsApp via Evolution API. Regras: respostas curtas, objetivas; nunca inventar dados; quando faltar contexto, pedir o mínimo necessário; formatar comandos para n8n em JSON.
```

**Servir o modelo**

```markdown
ollama pull llama3.1:8b
ollama pull nomic-embed-text
ollama serve  # expõe em http://localhost:11434
```

**API fina para rede** (Node/Express, ponte simples):

```markdown
import express from "express";
import fetch from "node-fetch";
const app = express(); app.use(express.json());

app.post("/alphie/chat", async (req,res)=>{
  const {messages} = req.body; // [{role:"system|user|assistant", content:"..."}]
  const r = await fetch("http://localhost:11434/api/chat", {
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body: JSON.stringify({model:"llama3.1:8b", messages})
  });
  res.json(await r.json());
});
app.listen(8787);
```

---

## 2) RAG da Ginkgo (conhecimento vivo)

**Ingestão**:

1. Varre pastas/Notion/Drive → extrai texto.
2. Gera embeddings (`/api/embeddings` do Ollama).
3. Grava em Chroma/SQLite com metadados: `{fonte, data, tag}`.

**Consulta**:

- n8n nó “HTTP Request” → `/embeddings` + top-k no banco → envia “contexto” + pergunta ao `/alphie/chat`.

---

## 3) Integração Trello

**Permissões**: `TRELLO_KEY`, `TRELLO_TOKEN`.  
Ações essenciais via n8n “HTTP Request”:

- Criar card: `POST https://api.trello.com/1/cards?name=...&idList=...`
- Comentar: `POST https://api.trello.com/1/cards/{id}/actions/comments`
- Mover card: `PUT https://api.trello.com/1/cards/{id}?idList=...&pos=top`
- Checklist: `POST /1/cards/{id}/checklists`

**Webhooks Trello → n8n**

- Endpoint n8n público: `POST https://{seu-n8n}/webhook/trello`
- Registra:
```markdown
curl -X POST "https://api.trello.com/1/webhooks/?key=$TRELLO_KEY&token=$TRELLO_TOKEN" \
-d "callbackURL=https://{seu-n8n}/webhook/trello" \
-d "idModel={ID_DO_BOARD}" -d "description=Ginkgo Trello Hook"
```

---

## 4) WhatsApp via Evolution API

Env vars: `EVOLUTION_KEY`, `EVOLUTION_INSTANCE`.  
**Mensagem texto**:

```markdown
curl -X POST "https://{evolution}/message/sendText/$EVOLUTION_INSTANCE" \
-H "apikey: $EVOLUTION_KEY" -H "Content-Type: application/json" \
-d '{"number":"55DDDNNNNNNN","text":"[Alerta] Tarefa X vence em 1h. Responda 1) iniciar 2) adiar 3) delegar."}'
```

**Áudio TTS (opcional Kokoro)**: Alphie gera texto → rota TTS → envia áudio pelo endpoint de mídia da Evolution.

---

## 5) Orquestração n8n (fluxos)

**Fluxo A – Eventos Trello → Alphie → Ações**

1. **Webhook** (Trello)
2. **Router** por evento: `createCard`, `updateCard`, `dueSoon`, `checklistComplete`
3. **RAG**: busca contexto do card (brief, owner, SLA)
4. **HTTP Request** → `/alphie/chat` com:
```markdown
{
  "messages":[
    {"role":"system","content":"use formato JSON de comandos"},
    {"role":"user","content":"Evento: dueSoon | Card: {{name}} | Descrição: {{desc}} | Due: {{due}}"}
  ]
}
```
5. **IF**: resposta contém `{"action":"notify_whatsapp"}` → **HTTP Request** Evolution
6. **IF**: `{"action":"comment_trello"}` → comentar no card
7. **IF**: `{"action":"create_subtasks"}` → criar checklist

**Fluxo B – Rotina proativa**

- **Cron**: a cada hora
- Busca cards com `due` < 24h
- Para cada card → Alphie sugere plano em 3 passos
- Dispara WhatsApp para responsável + comenta no card

**Fluxo C – Comando do usuário no WhatsApp**

- **Webhook Evolution** → mensagem do usuário
- Classifica intenção com Alphie: “iniciar”, “adiar 2h”, “delegar @nome”
- Aplica no Trello e confirma no WhatsApp

---

## 6) Protocolo de comandos do Alphie

Padronize a saída do Alphie para o n8n parsear:

```markdown
{
  "action": "notify_whatsapp|comment_trello|create_subtasks|move_card",
  "target": {"trello_card_id":"...", "whatsapp_number":"55..."},
  "payload": {
    "message":"Texto objetivo",
    "checklist":[ "Passo 1", "Passo 2", "Passo 3" ],
    "to_list":"ID_LISTA_DESTINO",
    "due_offset_minutes": 120
  }
}
```

**Prompt de saída segura**:

> “Seja estrito. Responda **apenas** um JSON válido conforme o protocolo. Não inclua texto fora do JSON.”

---

## 7) Variáveis de ambiente

```markdown
TRELLO_KEY=
TRELLO_TOKEN=
TRELLO_BOARD_ID=
EVOLUTION_KEY=
EVOLUTION_INSTANCE=
ALPHIE_API_BASE=http://localhost:8787
RAG_DB_PATH=/data/rag.db
```

---

## 8) Testes rápidos

- **Ping Alphie**:
```markdown
curl -X POST http://localhost:8787/alphie/chat \
-H "Content-Type: application/json" \
-d '{"messages":[{"role":"user","content":"Resumo do board Leaf hoje em 3 bullets."}]}'
```
- **Simular Trello**:
```markdown
curl -X POST https://{seu-n8n}/webhook/trello -H "Content-Type: application/json" \
-d '{"action":{"type":"updateCard","data":{"card":{"id":"abc","name":"Onboarding Leaf","desc":"..."}, "old":{"due":null}}}}'
```

---

## 9) Segurança e confiabilidade

- Assine webhooks com secret e verificação HMAC.
- Rate-limit em Evolution e Trello.
- Logs estruturados no n8n + retenção local.
- Fila opcional (Redis) para picos.

---

## 10) Próximo passo de execução

1. Subir `ollama serve` + API ponte em `:8787`.
2. Criar coleções RAG e rodar ingestão dos docs da Ginkgo.
3. Conectar webhooks Trello ↔ n8n e Evolution ↔ n8n.
4. Implementar Fluxos A/B/C com o protocolo JSON acima.
5. Testes fim-a-fim com um board “Leaf-Pilot”.

Se quiser, envio os JSONs do n8n desses três fluxos já prontos para importação.