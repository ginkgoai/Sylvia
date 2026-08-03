---
title: "GKO - Configuração Antigravity Docker"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/695de9ba-9bb0-832f-a347-341bb2958bb1"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
qua., 7 de jan. às 2:06

![28ee3b2a-2a0c-4854-b5f1-7169be4d36f7.png](https://chatgpt.com/backend-api/estuary/content?id=file_0000000091dc720e9255b6d8637631a5&ts=495692&p=fs&cid=1&sig=7d36c69f7b37dc3d8dd78fd39622168982d919b7423fb8720e87737d5b9f8f81&v=0)

?

qua., 7 de jan. às 3:28

![074b1430-d6e8-4ad3-93b5-df9b9f4c79c3.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000fd38720eaf6a230c741c7538&ts=495692&p=fs&cid=1&sig=f9484bc315661b13ad8a4f9095e929f60292fdecf6b84fa71ef48b95dc773165&v=0) ![8b2a097a-2506-41c9-b296-d5bad5fe07c4.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000deb4720e857c8b1fe51c4ff0&ts=495692&p=fs&cid=1&sig=0b9cfadac4871d24fab7ccf80cd415270c4db0d518a9f376b49200b1d0338d6e&v=0)

?

![e3c2b097-7056-451e-a8cc-42b151d4a070.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000c720720eaedbcb7956009a9b&ts=495692&p=fs&cid=1&sig=980b1cb4c3c4e81be9ac4bfb9bfdf532a6167b4a154eab50a93d3d3d8a91e86a&v=0)

?

Perfeito. Agora está **claríssimo onde você está** — e o próximo passo é **objetivo e inevitável**.

Você tem:

- ✅ **MCP Server Trigger**
- ✅ **Tool name correto (`ping_n8n`)**
- ❌ **Nenhum node de saída**  
	Sem saída, o MCP **escuta**, mas **não responde**. É como um rádio ligado sem alto-falante.

Vamos resolver isso **agora**, etapa por etapa, sem desvio.

---

## ETAPA 1 — Adicionar o node de resposta (obrigatório)

1. Clique no **`+`** logo abaixo de **Tools** no node `ping_n8n`
2. Escolha **Set** (às vezes aparece como *Set values* ou *Edit Fields*)

### Configure o Set node assim:

- **Mode / Options**:  
	👉 marque **Keep Only Set**
- Adicione os campos:
	- **Field 1**
		- Name: `ok`
				- Value: `true`
		- **Field 2**
		- Name: `echo`
				- Value:
			```markdown
			{{$json.message}}
			```

Isso garante que o MCP sempre devolva JSON válido.

---

## ETAPA 2 — Conectar o fluxo

Se não conectou automaticamente:

- Arraste a setinha do **MCP Server Trigger** → **Set**

Visual final esperado:

```markdown
[MCP Server Trigger] ───▶ [Set]
```

---

## ETAPA 3 — Salvar, Publicar e Ativar (ordem importa)

1. Clique **Save**
2. Clique **Publish** (se aparecer no canto superior direito)
3. Garanta que o workflow esteja:
	- **Active = ON**

Sem “Active”, o MCP **não executa em produção**.

---

## ETAPA 4 — Marcar como “Available in MCP”

1. Volte para a **lista de workflows**
2. No workflow `ping_n8n`, clique nos **⋯**
3. Marque:
	- ✅ **Available in MCP**

Esse passo é o que faz o workflow **aparecer para clientes MCP externos**.

---

## ETAPA 5 — Verificação obrigatória

Vá em:  
**Settings → Instance-level MCP**

Você precisa ver:

- `ping_n8n` listado
- Nada de “No workflows enabled”

Se **não aparecer**, pare aqui e me diga.

---

## ETAPA 6 — Teste MCP REAL (fora do editor)

Agora o teste certo, no endpoint de produção:

```markdown
curl -i \
  -H "Authorization: Bearer SEU_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "tool":"ping_n8n",
    "arguments":{"message":"hello"}
  }' \
  https://studio.ginkgosystems.tech/mcp-server/http
```

### Resultado esperado:

```markdown
{
  "ok": true,
  "echo": "hello"
}
```

---

## Próximo checkpoint (me responda só isso)

Depois da **ETAPA 5**:

- O workflow **apareceu** em *Instance-level MCP*? (sim / não)

Se **sim** → próxima etapa é **configurar o Antigravity**  
Se **não** → corrigimos flags/cache/versionamento na hora

Você está a **um node e dois cliques** de fechar o MCP.

![c4080d08-a69c-4908-abc8-1133fda0e82c.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000e52871f5bfbb1eb7bb39d162&ts=495692&p=fs&cid=1&sig=bb65ecaef50ca3273da64cf0381162dc995152b814a8e19f4c9b86d646036a6c&v=0)

Excelente. Essa tela explica **exatamente o que está te travando** — e não é erro seu.

👉 **Você está procurando o node errado no lugar errado.**  
O **Set** que precisamos **NÃO fica em “Tools”**.

Vamos destravar agora, **passo a passo**, sem abstração.

---

## O problema (objetivo)

O botão **\+ abaixo de “Tools”** não adiciona nodes de workflow.  
Ele serve para **MCP Tools internos**, não para **nodes de execução**.

Por isso você não acha **Set** aí.

---

## O caminho correto para adicionar o node de resposta

### ETAPA 1 — Adicionar o node pelo canvas (correto)

1. **Clique no ícone de `+` flutuante do canvas**  
	👉 não o “+” escrito *Tools*  
	👉 é o botão de adicionar **node de workflow**

Se não aparecer:

- Clique com o **botão direito no canvas**
- Ou pressione **A** (atalho de add node)

---

### ETAPA 2 — Buscar o node certo

No modal que abrir:

1. Digite:
```markdown
Set
```
2. Escolha:
- **Set**
- ou **Edit Fields**
- ou **Set values**

(depende da versão, mas o ícone é o mesmo)

✅ **Esse node NÃO aparece na lista de Tools à direita**  
Ele aparece **no modal de add node do canvas**.

---

## ETAPA 3 — Configurar o Set (obrigatório)

No node **Set**:

- Marque: **Keep Only Set**
- Crie os campos:

| Name | Value |
| --- | --- |
| ok | `true` |
| echo | `{{$json.message}}` |

Salve.

---

## ETAPA 4 — Conectar o fluxo

Arraste a conexão:

```markdown
ping_n8n (MCP Server Trigger)
   └──▶ Set
```

Visual final esperado:

```markdown
[MCP Server Trigger] ───▶ [Set]
```

---

## ETAPA 5 — Salvar, Publicar e Ativar

1. **Save**
2. **Publish** (se aparecer)
3. Garanta que o workflow está **Active**

---

## ETAPA 6 — Tornar visível para MCP

1. Vá para a **lista de workflows**
2. Clique nos **⋯** do `ping_n8n`
3. Marque:
	- ✅ **Available in MCP**

---

## ETAPA 7 — Verificação crítica

Vá em:  
**Settings → Instance-level MCP**

Você precisa ver:

- `ping_n8n` listado

---

## Checklist rápido (responda sim/não)

1. Conseguiu adicionar o **Set node pelo canvas**?
2. O fluxo está `MCP Trigger → Set`?
3. O workflow aparece em **Instance-level MCP**?

Com isso resolvido, o próximo passo é **testar o MCP real via curl** e depois **ligar o Antigravity**.

![87ee7bfb-efd1-49d4-9f4a-43a862ff9dfd.png](https://chatgpt.com/backend-api/estuary/content?id=file_000000007528720e8634dc907b914307&ts=495692&p=fs&cid=1&sig=46f68a5ff3ee93cadbb06bc70030e96c22a93bda73bf3e1625adb0f5817655b5&v=0)

Perfeito — agora deu para ver **exatamente onde desviou**.  
Sem rodeio:

👉 **Você adicionou os nodes errados (MCP Client + Edit Fields)**  
👉 **Eles NÃO fazem parte de um MCP Server**  
👉 Isso é outro fluxo (cliente chamando MCP), não o servidor expondo tool.

Vamos corrigir **limpo, em ordem**, como um checklist cirúrgico.

---

## O que deve existir (arquitetura correta)

Para um **MCP SERVER no n8n**, o fluxo é **somente**:

```markdown
[MCP Server Trigger]  ───▶  [Set / Edit Fields]
```

❌ **MCP Client NÃO entra aqui**  
❌ **Tools panel NÃO entra aqui**

---

## ETAPA 1 — Apagar o que não pertence ao fluxo

1. Selecione o node **MCP Client**
2. Delete
3. Selecione o node **Edit Fields (manual)** que está ligado a ele
4. Delete

Você deve ficar **APENAS** com:

- `ping_n8n` (MCP Server Trigger)

---

## ETAPA 2 — Adicionar o node correto (resposta MCP)

Agora atenção ao clique certo 👇

### Como adicionar o node certo

- Clique **com o botão direito no canvas**  
	**OU**
- Pressione **A** no teclado  
	**OU**
- Clique no **\+ flutuante do canvas** (não o “Tools”)

Vai abrir o **Add Node modal**.

### No modal:

- Digite: `Set`
- Escolha **Set** ou **Edit Fields**

---

## ETAPA 3 — Configurar o Set (obrigatório)

No node **Set / Edit Fields**:

1. Marque:
	- ✅ **Keep Only Set**
2. Crie os campos:

| Name | Value |
| --- | --- |
| ok | `true` |
| echo | `{{$json.message}}` |

3. **Save**

---

## ETAPA 4 — Conectar corretamente

Arraste a conexão:

```markdown
ping_n8n  ───▶  Set
```

Visual final correto:

```markdown
[MCP Server Trigger ping_n8n] → [Set]
```

Nada além disso.

---

## ETAPA 5 — Salvar, Publicar e Ativar

1. Clique **Save**
2. Clique **Publish** (se aparecer)
3. Confirme que o workflow está:
	- **Active = ON**

---

## ETAPA 6 — Expor para MCP (passo crítico)

1. Vá para a **lista de workflows**
2. No `ping_n8n`, clique nos **⋯**
3. Marque:
	- ✅ **Available in MCP**

---

## ETAPA 7 — Conferência final

Vá em:

**Settings → Instance-level MCP**

Você precisa ver:

- `ping_n8n` listado

Se não aparecer, o MCP **não existe externamente**.

---

## ETAPA 8 — Teste REAL do MCP (fora do editor)

```markdown
curl -i \
  -H "Authorization: Bearer SEU_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "tool":"ping_n8n",
    "arguments":{"message":"hello"}
  }' \
  https://studio.ginkgosystems.tech/mcp-server/http
```

### Esperado:

```markdown
{
  "ok": true,
  "echo": "hello"
}
```

---

## Resumo em 1 linha

Você estava montando **um cliente MCP dentro do servidor MCP**.  
Agora é **Trigger → Set**, ativar, expor, testar.

### Me responda só isso:

- Depois da **ETAPA 6**, o workflow aparece em **Instance-level MCP**? (sim / não)

A partir do “sim”, o próximo passo é **ligar o Antigravity** em 2 minutos.