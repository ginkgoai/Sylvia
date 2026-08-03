---
title: "GKO - Ativar MCP Tools"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/69082004-bde0-8331-8d64-8846f19c45e5"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
seg., 3 de nov. às 0:22

eu consigo fazer o brann ativar essa mcp tool para tanto ler documentos informativos que precisar na base como tambem enviar documentos ou midia ativando um subworkflow, ou enviar email, agendar chamada google calendar, todas funcoes impostas e necessarias??

Sim. Dá para o BRANN acionar o MCP e executar leitura de docs, envio de mídia via sub-workflow, e ações como e-mail, evento no Google Calendar e inserts no Supabase. A arquitetura é: BRANN (tool-calling) → Router no n8n → MCP Server (tools) → sub-workflows/HTTP. O bloco de áudio e o envio Evolution seguem igual ao que já está no seu fluxo.

Visao-geral-do-fluxo

## Plano direto

1. **Ativar MCP Tools**
- No orquestrador onde aparece “MCP Tools (Deactivated)” habilite e informe o endpoint do seu MCP Server.
	- **URL**: `ws://SEU_HOST:SEU_PORT/mcp` ou `http://.../mcp` conforme seu server.
		- **Auth**: defina `MCP_API_KEY` e passe no header `Authorization: Bearer ...`.
- Reinicie o container que hospeda o cliente MCP e o server MCP.
2. **Definir o contrato de ferramentas (JSON Schema)**  
	Cole no campo “Tools / Functions” do modelo (ou arquivo do MCP) estes esquemas mínimos. Eles viram o *contrato* que o BRANN pode chamar:
```markdown
[
  {
    "name": "gko_docs.search",
    "description": "Busca contextual em base de documentos da Ginkgo.",
    "parameters": {
      "type": "object",
      "properties": {
        "query": { "type": "string" },
        "top_k": { "type": "integer", "default": 5 }
      },
      "required": ["query"]
    }
  },
  {
    "name": "gko_memories.search",
    "description": "Busca em memórias curtas/longas do cliente/atendimento.",
    "parameters": {
      "type": "object",
      "properties": {
        "query": { "type": "string" },
        "top_k": { "type": "integer", "default": 5 }
      },
      "required": ["query"]
    }
  },
  {
    "name": "supabase.create_row",
    "description": "Cria linha em tabela do Supabase.",
    "parameters": {
      "type": "object",
      "properties": {
        "table": { "type": "string" },
        "data": { "type": "object", "additionalProperties": true }
      },
      "required": ["table","data"]
    }
  },
  {
    "name": "gmail.send_message",
    "description": "Envia e-mail para o cliente.",
    "parameters": {
      "type": "object",
      "properties": {
        "to": { "type": "string" },
        "subject": { "type": "string" },
        "body": { "type": "string" }
      },
      "required": ["to","subject","body"]
    }
  },
  {
    "name": "gcal.create_event",
    "description": "Cria evento no Google Calendar.",
    "parameters": {
      "type": "object",
      "properties": {
        "title": { "type": "string" },
        "start_iso": { "type": "string" },
        "end_iso": { "type": "string" },
        "attendees": { "type": "array", "items": { "type": "string" } },
        "meet": { "type": "boolean", "default": true }
      },
      "required": ["title","start_iso","end_iso"]
    }
  },
  {
    "name": "media.send_ptt",
    "description": "Dispara áudio PTT pré-pronto via subworkflow de áudio.",
    "parameters": {
      "type": "object",
      "properties": {
        "phone": { "type": "string" },
        "key": { "type": "string" }
      },
      "required": ["phone","key"]
    }
  }
]
```
3. **Router no n8n para cada tool**
- Após o nó do modelo, use um **Switch** em `{{$json.tool_name}}`.
- Para cada case, chame um **Execute Workflow** específico ou um **HTTP Request** para o seu MCP Server, mapeando `arguments` para os nós:
	- `gko_docs.search` e `gko_memories.search`: chame o MCP; ele consulta sua vector-store e retorna `answers[]`.
		- `supabase.create_row`: nós `Supabase → Insert`.
		- `gmail.send_message`: nó Gmail API → `send`.
		- `gcal.create_event`: Google Calendar → `create`.
		- `media.send_ptt`: acione o **sub-workflow de áudio** já previsto no seu desenho com `phone` e `key`. Esse sub-fluxo envia PTT via Evolution conforme a seção “Subfluxo AUDIO” do seu PDF.
		Visao-geral-do-fluxo
4. **Sub-workflow de mídia já padronizado**
- Entrada: `{ phone, key }`.
- Passos: resolver `key` → obter URL do áudio → `POST /message/sendAudio` com `ptt:true` → retorno `{sent:true,url}`. O envio usa as mesmas variáveis de ambiente e padrões de mensagem do seu fluxo Evolution.
	Visao-geral-do-fluxo
5. **Prompt do BRANN para tool-calling**  
	Use um system curto que obriga ferramentas quando necessário:
```markdown
Você é o BRANN. Responda curto e objetivo. 
Se precisar de fatos internos, chame gko_docs.search ou gko_memories.search.
Para tarefas: use supabase.create_row, gmail.send_message, gcal.create_event ou media.send_ptt.
Nunca invente dados. Peça só o mínimo que falta.
```

Formato de saída do modelo: `{"tool_name":"...","arguments":{...}}` quando for usar tool; caso contrário, `{"out":{"type":"text","text":"..."}}` como no seu Parser.

Visao-geral-do-fluxo

6. **Exemplos de chamadas que o modelo deve emitir**
- Ler docs:
```markdown
{"tool_name":"gko_docs.search","arguments":{"query":"política de reembolso Leaf","top_k":3}}
```
- Criar lead:
```markdown
{"tool_name":"supabase.create_row","arguments":{"table":"leads","data":{"phone":"+55XXXXXXXXXXX","nome":"Ana","fonte":"WhatsApp"}}}
```
- E-mail:
```markdown
{"tool_name":"gmail.send_message","arguments":{"to":"ana@exemplo.com","subject":"Proposta Ginkgo","body":"Segue a proposta..."}}
```
- Evento:
```markdown
{"tool_name":"gcal.create_event","arguments":{"title":"Onboarding Leaf","start_iso":"2025-11-05T14:00:00-03:00","end_iso":"2025-11-05T14:30:00-03:00","attendees":["ana@exemplo.com"],"meet":true}}
```
- PTT:
```markdown
{"tool_name":"media.send_ptt","arguments":{"phone":"55XXXXXXXXXXX","key":"onboarding"}}
```
7. **Segurança e governança**
- Whitelist de tabelas Supabase e colunas permitidas.
- Validação de `attendees` e datas ISO antes do Calendar.
- Sanitização de `body` no Gmail.
- Observabilidade: gere `traceId`, `latency_ms` e `tool_name` em um `Set` antes de cada execução e logue em tabela `brann_logs`. O PDF já sugere adicionar `traceId/latency` e fallback de download de mídia.
	Visao-geral-do-fluxo
8. **Teste mínimo ponta-a-ponta**
- Texto “quero assinar e marcar call” → BRANN chama `gcal.create_event` e devolve confirmação.
- “Me manda a proposta por e-mail” → `gmail.send_message`.
- “Cadastra meus dados” → `supabase.create_row`.
- “Me explica por voz” → `media.send_ptt`.

## Correção do “MCP Tools (Deactivated)”

- Habilite o bloco e configure o endpoint do seu server MCP.
- Verifique porta exposta no container e CORS/WS.
- Garanta `MCP_API_KEY` e mapeamento no n8n/Flowise.
- Reinicie os serviços.

Isso cobre leitura de bases internas, envio de mídia pelo sub-workflow, e execuções externas por e-mail, agenda e Supabase sem alterar o restante do fluxo do Evolution e do BRANN já descrito.

Visao-geral-do-fluxo