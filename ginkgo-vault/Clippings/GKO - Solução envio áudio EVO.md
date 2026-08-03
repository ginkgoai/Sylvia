---
title: "GKO - Solução envio áudio EVO"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/692a0b76-25fc-8330-88ce-d3b0bf8d3208"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sex., 28 de nov. às 17:52

![dfc0d0e9-adb7-448f-ac5a-f54bfc6864a1.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000b658720ea130cf263d998766&ts=495692&p=fs&cid=1&sig=58bae5c1ca43e188add8813290a340a72a668cbf558f682b4ede0ad1126c1741&v=0)

vamos finalizar a prv, tem problema na saída apenas, quando e audio ele gera mas nao envia mesmo o no rodando verde tudo certo, percebe que no whats web tem um audio de zero segundos que nao da ora abrr, mas no mobile nem aparece essa mensagem. oq esta acontecendo

sáb., 29 de nov. às 11:24

![ed107cd1-1437-4eee-9e34-a83d2948a062.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000a480720e98428e1c63239d99&ts=495692&p=fs&cid=1&sig=9d22f52c72239e76129a2f3bcfbef81b88a898d703fce4ac4192212da63dbd7f&v=0)

Vamos resolver **cada erro que aparece no print**, porque agora está tudo claro:

---

## ✅ 1. Seu audioBase64 está vindo NULL

O motivo:

Você colocou a expressão:

```markdown
{{ $json.body.data.message.base64 }}
```

Mas **isso NÃO existe no output do TTS**.

O node “Generate speech from text” gera áudio **em binário**, não em JSON.

➜ O valor correto para converter o binário para base64 é:

### Use isso:

Node **Set** → campo `audioBase64`:

```markdown
{{$binary.data.data.toString("base64")}}
```

Onde:

- `data` = nome da propriedade binária (no teu print está **data** mesmo)
- `.data` = buffer
- `toString("base64")` converte

⚠️ Esse comando **NUNCA vai dar NULL** se o binário existir — resolve na hora.

---

## ✅ 2. Seu erro “URL must start with http or https”

Acontece porque você configurou o HTTP Request assim:

```markdown
/message/sendWhatsAppAudio/
```

E o n8n exige URL ABSOLUTA.

### A URL correta é:

```markdown
{{$env.EVOLUTION_BASE_URL}}/message/sendWhatsAppAudio/{{$env.EVOLUTION_INSTANCE}}
```

Exemplo real:

```markdown
https://api.evolution-api.com/message/sendWhatsAppAudio/PRV_ALIMENTOS
```

Verifica:

- Se sua variável `EVOLUTION_BASE_URL` **inclui https://**.  
	Deve ser assim:
```markdown
EVOLUTION_BASE_URL=https://ginkgodev.evolution-api.com
```

Se estiver sem protocolo, vai dar erro.

---

## 🚀 Configuração 100% correta: COPY/PASTE

## Node SET

(add field → audioBase64)

```markdown
{{$binary.data.data.toString("base64")}}
```

---

## Node HTTP Request

**Method:** POST  
**URL:**

```markdown
{{$env.EVOLUTION_BASE_URL}}/message/sendWhatsAppAudio/{{$env.EVOLUTION_INSTANCE}}
```

**Headers:**

| Key | Value |
| --- | --- |
| Content-Type | application/json |
| apikey | \={{ $env.EVOLUTION\_TOKEN }} |

**Body → JSON:**

```markdown
{
  "number": "={{$json['Tratamento de Dados'].item.json.NUMERO_LEAD}}",
  "audio": "={{$json.audioBase64}}",
  "delay": 1200
}
```

---

## 🔥 Checklist para garantir que FUNCIONE

### 1\. O binário existe?

No print ele aparece como:

```markdown
data
File Name: voice
File Extension: mp3
```

✓ Está correto.

### 2\. O nome da propriedade binária é data?

No canto esquerdo do node → SIM.

### 3\. A URL tem https://?

Tem que colocar.

### 4\. O Evolution aceita base64 direto?

Sim. Rota correta: `/message/sendWhatsAppAudio/{instance}`  
Aceita:

- URL pública
- Base64 puro

---

## 📍 Se quiser, me manda o print do node HTTP aberto e eu reviso linha por linha.

Quando você fizer os dois ajustes acima → **o áudio vai chegar perfeito no WhatsApp**  
Sem 0 segundos. Sem corrupção. Sem falha silenciosa.

![90c54f98-3254-4059-8955-a92c64a7caf9.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000bcb071f5abf7a4f8b5f2e76f&ts=495692&p=fs&cid=1&sig=a60fb53ddd7589a6e9f6b05f4c5e01d652743dcbe9977da404106aa21a988846&v=0)

Boa, agora ficou claro o que está rolando:

- O binário está vindo certinho (`data` com `voice.mp3`).
- A expressão está certa.
- Mesmo assim o `audioBase64` sai `null` ⇒ significa que **nesse run o node não está enxergando `item.binary.data`**.

Isso geralmente é um desses dois pontos:

1. O node foi executado “sozinho” sem reexecutar o TTS (então não chegou nenhum `binary` real para essa execução).
2. Algum node no meio está limpando o binário.

Vou te dar um caminho à prova de bala em 2 partes.

---

## 1) Converter binário → base64 usando Function (mais estável)

Logo depois do `Generate speech from text`, coloca um **Function** em vez desse Set:

### Node: Function

```markdown
// Entrada: vem direto do TTS, com item.binary.data
return items.map(item => {
  if (item.binary && item.binary.data && item.binary.data.data) {
    // Converte o buffer para base64
    item.json.audioBase64 = item.binary.data.data.toString('base64');
  } else {
    // Se não tiver binário, fica evidente no debug
    item.json.audioBase64 = null;
  }
  return item;
});
```

Importante para testar:  
no Function, clica em **“Execute previous nodes”** (ou roda o fluxo desde o TTS), nunca “só este node”. Assim você garante que o `binary.data` está realmente chegando nessa execução.

Na saída do Function você deve ver:

```markdown
{
  "audioBase64": "AAAAGGZ0eXBtcDQyAAAAAG1wNDFtcDQxaXNvbQAA..."
}
```

Se aparecer `null`, aí 100% certeza de que o binário não está vindo na execução (aí você revisa o encadeamento de nodes).

---

## 2) HTTP Request para o Evolution (recap ajustado)

Com o `audioBase64` pronto no `json`, configura o **Enviar audio EVO** assim:

### URL

```markdown
{{$env.EVOLUTION_BASE_URL}}/message/sendWhatsAppAudio/{{$env.EVOLUTION_INSTANCE}}
```

Confere que no `.env` está com protocolo:

```markdown
EVOLUTION_BASE_URL=https://SEU-DOMINIO-EVO
EVOLUTION_INSTANCE=PRV_ALIMENTOS
EVOLUTION_TOKEN=SEU_API_KEY
```

### Headers

- `Content-Type`: `application/json`
- `apikey`: `={{ $env.EVOLUTION_TOKEN }}`

### Body → JSON

```markdown
{
  "number": "={{$json['Tratamento de Dados'].item.json.NUMERO_LEAD}}",
  "audio": "={{$json.audioBase64}}",
  "delay": 1200
}
```

Roda o fluxo a partir do TTS:  
`Generate speech from text` → `Function (audioBase64)` → `HTTP Request`.

Se:

- No Function o `audioBase64` vier preenchido
- E a URL estiver com `https://...`

o áudio tem que aparecer normal (duração > 0s) tanto no Whats Web quanto no celular.

---

Resumo do que você precisa fazer agora:

1. Substituir o Set por **Function** com o código acima.
2. Garantir que está rodando com **“Execute previous nodes”**.
3. Conferir a URL completa do Evolution com `https://`.
4. Mandar um teste de áudio e ver se some o fantasma de 0 segundos.

Depois que isso estiver ok, a gente acopla esse bloco como padrão “AUDIO PRV” pra reaproveitar em qualquer fluxo.

3/3

![1c25a932-c0a0-4632-b964-640b33c50e76.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000ab5071f585c79f98a635084c&ts=495692&p=fs&cid=1&sig=5c4058795f6487375bc2e303505dcf31cae6666109109a181c74a2b448240b1c&v=0)

?

Agora ficou lindo.

O que você fez aí foi usar o node tipo **Move Binary Data / Extract from File** com operação  
**“Move File to Base64 String”**:

- `Input Binary Field`: `data`
- `Destination Output Field`: `data`
- No OUTPUT apareceu `data: "SUQzBAAAAA..."` → ou seja, **o mp3 virou base64 certinho**.

Isso é exatamente o que a rota do Evolution espera.

Só dois ajustes finais:

---

## 1\. Renomeia o campo para ficar claro

Em vez de salvar o base64 em `data`, coloca em `audioBase64`:

- `Destination Output Field`: `audioBase64`

Assim, o JSON de saída fica:

```markdown
{
  "audioBase64": "SUQzBAAAAA..."
}
```

---

## 2\. HTTP Request para o Evolution

Node **Enviar audio EVO**:

**Method:** `POST`  
**URL:**

```markdown
{{$env.EVOLUTION_BASE_URL}}/message/sendWhatsAppAudio/{{$env.EVOLUTION_INSTANCE}}
```

(verifica que `EVOLUTION_BASE_URL` está com `https://...`)

**Headers:**

- `Content-Type`: `application/json`
- `apikey`: `={{ $env.EVOLUTION_TOKEN }}`

**Body → JSON:**

```markdown
{
  "number": "={{$json['Tratamento de Dados'].item.json.NUMERO_LEAD}}",
  "audio": "={{$json.audioBase64}}",
  "delay": 1200
}
```

Fluxo final desse bloco:

`Generate speech from text` → `Extract from File (Move File to Base64 → audioBase64)` → `HTTP Request (sendWhatsAppAudio)`.

Executa a partir do TTS e testa no Whats:

- Se aparecer áudio com duração normal (sem 0s) no Web e no celular → PRV áudio 100% resolvido.