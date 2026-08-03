---
title: "GKO - Erro no nó OpenAI"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/690aed19-c4b4-8327-9b8b-7ddce8f20292"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
qua., 5 de nov. às 3:22

![b5dfc927-685b-48bf-a654-6a92af014604.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000ecf8720e9bdd00f941cbfd31&ts=495692&p=fs&cid=1&sig=1e2f3d290e148ac4d77e414db4d0e95ca6fbd2f1b2772dd36fde254420febe8e&v=0) ![c472de01-396f-476f-86f2-9bfcb4a42916.png](https://chatgpt.com/backend-api/estuary/content?id=file_0000000064fc720eaa28c6deae377244&ts=495692&p=fs&cid=1&sig=331cf5faaed26531683a915cb693b93368731f872cb836c19f14e2d1e80a2380&v=0)

?

esse?

Não. Esse **Extract from File** serve para *converter binário em JSON*, o oposto do que você precisa.

Procure exatamente o nó chamado:

> **Move Binary Data**

Se ele não aparecer, é porque sua versão do n8n está desatualizada.  
Nesse caso, há duas alternativas rápidas:

---

### ✅ Alternativa 1 — usar Function Item

Adicione um nó **Function Item** antes do OpenAI e cole este código:

```markdown
// converte Base64 em binário "data"
const base64 = $json.Base64;
return {
  binary: {
    data: {
      data: Buffer.from(base64, 'base64'),
      mimeType: 'image/png',
      fileName: 'input.png'
    }
  }
};
```

Depois ligue esse nó no OpenAI (Input Data Field Name = `data`).

---

### ✅ Alternativa 2 — atualizar o n8n

Atualize via terminal (Docker ou local):

```markdown
npm install -g n8n@latest
```

ou no Docker Compose:

```markdown
image: n8nio/n8n:latest
```

Depois disso o nó **Move Binary Data** aparecerá normalmente.

?

Use **Convert to File**. Configure para transformar o Base64 em binário chamado `data`.

### Passo a passo no nó “Convert to File”

- **Binary Property**: `data`
- **File Name**: `input.png` *(ou `.jpg`, `.webp`, conforme o tipo)*
- **Content Type**: `image/png` *(ajuste para `image/jpeg` etc.)*
- **Data Source**: **From String**
- **String Property**:
	```markdown
	={{$json.Base64.replace(/^data:.*;base64,/, '')}}
	```
	*(remove prefixo `data:...;base64,` se existir)*
- **Encoding**: **Base64**

### No nó OpenAI (Analyze Image)

- **Input Type**: Binary File(s)
- **Input Data Field Name**: `data`

Se for áudio/vídeo, apenas troque:

- **File Name**: `input.mp3` / `input.mp4`
- **Content Type**: `audio/mpeg` / `video/mp4`

Execute o Convert to File e verifique a aba **Binary** do item: deve aparecer `data`. Depois o OpenAI executa sem erro.

![1647a16e-ccc5-43a7-929b-cada9e6347d9.png](https://chatgpt.com/backend-api/estuary/content?id=file_0000000095d4720ead36056ec0acbcbe&ts=495692&p=fs&cid=1&sig=035900b63a39196716390efc6847f4ba3553069fdbb5b7f4a851bdc49c944498&v=0)

Na tela, o **Convert to File** está configurado incorretamente — ele não entende automaticamente que “Base64” é o campo de entrada.

Aqui está o ajuste exato:

---

### ✅ Configuração correta do nó Convert to File

**Operation:** `Convert to File`  
**Binary Property:** `data`  
**File Name:** `input.png`  
**Content Type:** `image/png`  
**Data Source:** `From String`  
**String Property:**

```markdown
={{$json.Base64}}
```

**Encoding:** `Base64`

---

### 🔁 Depois disso:

1. Clique **Execute Node** → verifique se aparece aba **Binary** no output com o campo `data`.
2. Ligue esse nó direto no **OpenAI (Analyze Image)**.
3. No OpenAI mantenha:
	- **Input Type:** Binary File(s)
		- **Input Data Field Name:** `data`

---

Assim o OpenAI receberá o binário corretamente, e o erro “expects binary file ‘data’” desaparecerá.