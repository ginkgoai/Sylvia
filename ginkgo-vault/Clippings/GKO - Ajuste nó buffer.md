---
title: "GKO - Ajuste nó buffer"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/68fbb0d1-789c-832d-aa56-a802493ab401"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sex., 24 de out. às 14:01

vamos só ajeitar os nós externamente do bloco buffer. precisa conter as funcoes de agrupar mensangens, marcar como lido, e opção de reconhecer quando um humano quer assumir a conversa.

Proponho 3 nós externos ao BUFFER, em série: **Agrupar mensagens → Marcar como lido → Detector de handoff humano**. Abaixo, configs “copy/cola”.

## 1) Agrupar mensagens (Function)

Janela curta para juntar digitação em rajada por chatId.

```markdown
// Name: GROUP_MESSAGES
const W_SECONDS = 10; // janela
const now = Date.now();
const s = getWorkflowStaticData('global');
s.buffers ??= {};

const msg = items[0].json; // precisa ter {chatId, messageId, text}
const id = msg.chatId || 'unknown';

if (!s.buffers[id]) s.buffers[id] = { t0: now, list: [] };
s.buffers[id].list.push({ messageId: msg.messageId, text: msg.text });

const ready = (now - s.buffers[id].t0) / 1000 >= W_SECONDS;
if (!ready) {
  // não solta nada ainda; n8n seguirá quando próximo evento cair
  return [];
}

// fecha o lote e solta
const batch = s.buffers[id].list;
delete s.buffers[id];

return [{ json: { ...msg, grouped: true, messages: batch, text: batch.map(x=>x.text).join(' ') } }];
```

Coloque um **Wait** logo antes do próximo nó: Amount=1s.

## 2) Marcar como lido (HTTP Request)

Sua instância Evolution pode variar. Use a que existir:

**Opção A**

```markdown
Method: POST
URL: {{$env.EVOLUTION_BASE_URL}}/chat/read/{{$env.EVOLUTION_INSTANCE}}
Headers:
  Authorization: {{'Bearer ' + $env.EVOLUTION_TOKEN}}
  Content-Type: application/json
Body (JSON):
{ "chatId": "={{$json.chatId}}", "messageIds": "={{$json.messages.map(m=>m.messageId)}}" }
```

**Opção B**

```markdown
Method: POST
URL: {{$env.EVOLUTION_BASE_URL}}/message/sendSeen/{{$env.EVOLUTION_INSTANCE}}
Headers:
  Authorization: {{'Bearer ' + $env.EVOLUTION_TOKEN}}
  Content-Type: application/json
Body (JSON):
{ "chatId": "={{$json.chatId}}" }
```

Se nenhuma existir na sua versão, pule este nó e mantenha o “seen” para depois do envio.

## 3) Detector de handoff humano (Function)

Sinaliza quando o usuário quer humano.

```markdown
// Name: HUMAN_HANDOFF_DETECT
const btn = $json?.buttonId || $json?.selectedButtonId || '';
const text = ($json?.text || '').toLowerCase();

const TRIGGERS = [
  'humano','atendente','pessoa','falar com humano','suporte humano',
  'ligação','telefone','whatsapp humano','preciso de alguém'
];

const matched = TRIGGERS.some(k=>text.includes(k)) || btn === 'humano';

return [{
  json: {
    ...$json,
    handoff: matched ? true : false,
    handoff_reason: matched ? 'user_request' : null
  }
}];
```

## 4) IF roteador

Crie um **IF** após o detector:

- Condition: `={{$json.handoff === true}}`
	- **True** → Subfluxo “HUMANO\_ONCALL” ou fila humana.
		- **False** → segue para o seu nó “BRANN / Parser / Enviar”.

## Saídas esperadas

- `GROUP_MESSAGES` emite um único item com `messages[]` e `text` concatenado.
- Nó de “lido” tenta marcar conversa como lida.
- `HUMAN_HANDOFF_DETECT` define `handoff=true` quando há intenção clara ou botão “humano”.

## Observações rápidas

- Se quiser persistir a janela por falha de nó, troque `global` por Redis (chave `buffer:{chatId}` com TTL 15s).
- Para botão “humano”, mantenha o ID exatamente `humano` na resposta do BRANN.
- Se precisar, adiciono o subfluxo “HUMANO\_ONCALL” com: aviso em grupo interno, tag em CRM e pausa do bot para aquele `chatId`.

Sequência sugerida usando só os nós que já existem no quadro e trocando funções:

1. **CALCULAR MD5 → trocar por “GROUP\_MESSAGES (Function)”**  
	Motivo: aqui entra a lógica de agrupamento. Mantém o **ESPERA** logo depois.
2. **ESPERA → manter**  
	Apenas ajuste para 1–2s.
3. **BUSCA MENS → manter**  
	Continua alimentando os dados do lote.
4. **CATEGORIZA MENS → manter**  
	Acrescenta campo `intent` se já não houver.
5. **ATUALIZA MENS → trocar para “MARK\_AS\_READ (HTTP Request)”**  
	Mesma posição. Passa a marcar como lido na Evolution.
6. **APENDA MENS → manter**  
	Continua gravando no buffer/CRM.
7. **IF ORGANIZADOR → manter e adicionar saída “handoff”**  
	Inserir nova primeira condição: `{{$json.handoff === true}}` → rota HUMANO.
8. **Adicionar 1 nó novo entre CATEGORIZA MENS e IF ORGANIZADOR: “HUMAN\_HANDOFF\_DETECT (Function)”**  
	Só este é novo fora as trocas acima.

Resultado final no fluxo do BUFFER:  
Criar array de itens → **GROUP\_MESSAGES** → Espera → Busca Mens → Categoriza Mens → **MARK\_AS\_READ** → **HUMAN\_HANDOFF\_DETECT** → IF Organizador  
• IF\[handoff=true\] → Fila/On-call humano  
• IF\[default\] → Apêndice/Brann

Remover: **nenhum outro nó**. Só substituir os dois citados e inserir o detector.