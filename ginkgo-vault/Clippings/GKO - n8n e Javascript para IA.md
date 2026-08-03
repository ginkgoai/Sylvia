---
title: "GKO - n8n e Javascript para IA"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/690024a6-dc5c-8333-acbf-3d3aa6b0f7a7"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
![Imagem gerada: Fluxo do Agente WhatsApp com n8n](https://chatgpt.com/backend-api/estuary/content?id=file_00000000f56861f5b2087bf391fd33c3&ts=495692&p=fs&cid=1&sig=f5380b3f257c146539c8ef2ba0d42728d358aa6fc5ba0d3427c8f2f232fe0e2d&v=0) ![](https://chatgpt.com/backend-api/estuary/content?id=file_00000000f56861f5b2087bf391fd33c3&ts=495692&p=fs&cid=1&sig=f5380b3f257c146539c8ef2ba0d42728d358aa6fc5ba0d3427c8f2f232fe0e2d&v=0) ![](https://chatgpt.com/backend-api/estuary/content?id=file_00000000f56861f5b2087bf391fd33c3&ts=495692&p=fs&cid=1&sig=f5380b3f257c146539c8ef2ba0d42728d358aa6fc5ba0d3427c8f2f232fe0e2d&v=0) ![Imagem gerada: Fluxo de Automação WhatsApp AI](https://chatgpt.com/backend-api/estuary/content?id=file_00000000b0a061f5b66d51290d542251&ts=495692&p=fs&cid=1&sig=af2aab5c8d8b4139fda546ca0ce3ed8723d5fff6321c722163be72cd83d64a81&v=0) ![](https://chatgpt.com/backend-api/estuary/content?id=file_00000000b0a061f5b66d51290d542251&ts=495692&p=fs&cid=1&sig=af2aab5c8d8b4139fda546ca0ce3ed8723d5fff6321c722163be72cd83d64a81&v=0) ![](https://chatgpt.com/backend-api/estuary/content?id=file_00000000b0a061f5b66d51290d542251&ts=495692&p=fs&cid=1&sig=af2aab5c8d8b4139fda546ca0ce3ed8723d5fff6321c722163be72cd83d64a81&v=0) ![Imagem gerada: Fluxo de Trabalho no n8n](https://chatgpt.com/backend-api/estuary/content?id=file_00000000f98061f59026d5a2f175ad21&ts=495692&p=fs&cid=1&sig=6cd3289bb312471101226d7f5ea457f9c9b598f9472c793374fae57a9cd90a67&v=0) ![](https://chatgpt.com/backend-api/estuary/content?id=file_00000000f98061f59026d5a2f175ad21&ts=495692&p=fs&cid=1&sig=6cd3289bb312471101226d7f5ea457f9c9b598f9472c793374fae57a9cd90a67&v=0) ![](https://chatgpt.com/backend-api/estuary/content?id=file_00000000f98061f59026d5a2f175ad21&ts=495692&p=fs&cid=1&sig=6cd3289bb312471101226d7f5ea457f9c9b598f9472c793374fae57a9cd90a67&v=0) ![Imagem gerada: Automação de Fluxo com n8n](https://chatgpt.com/backend-api/estuary/content?id=file_0000000079a861f5ab18d7584f4ca37a&ts=495692&p=fs&cid=1&sig=ce2f655973ebaa41c68ef0a16d154edd9ff52227c8508bf9a259ff9df7453c06&v=0) ![](https://chatgpt.com/backend-api/estuary/content?id=file_0000000079a861f5ab18d7584f4ca37a&ts=495692&p=fs&cid=1&sig=ce2f655973ebaa41c68ef0a16d154edd9ff52227c8508bf9a259ff9df7453c06&v=0) ![](https://chatgpt.com/backend-api/estuary/content?id=file_0000000079a861f5ab18d7584f4ca37a&ts=495692&p=fs&cid=1&sig=ce2f655973ebaa41c68ef0a16d154edd9ff52227c8508bf9a259ff9df7453c06&v=0)

ter., 28 de out. às 20:14

qui., 30 de out. às 22:19

![c8d3d59e-2ae5-4145-b237-c7344e252753.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000b5fc61f5a1fb7d6a0976c6da&ts=495692&p=fs&cid=1&sig=d9990beb0912f55abf0ad6fce30a43156ec2a495550f6ff341c18ed21748bd08&v=0)

sex., 31 de out. às 2:15

Sim, mas faltou remover o gatilho que ainda força JSON.

Faça isso:

1. Parameters → **Response Format: Text**
2. Abra **model\_kwargs** → **remova** o bloco:
```markdown
response_format: { "type": "json_object" }
```
3. Garanta 2 mensagens:
- **messages\[0\].role = system** → seu System Message.
- **messages\[1\].role = user** → o texto limpo do nó anterior:
```markdown
{{$item(0, 'Normalize Final').$json.text}}
```
4. Base URL correta: `https://api.openai.com/v1`
5. Modelo: `gpt-4o-mini`
6. Temperature: 0.2–0.4, Max tokens: 1200.

Teste rápido no próprio nó:

- INPUT de teste: `{"text":"Explique o plano Básico sem formatação."}`
- Execute. A **Output** deve vir em texto simples.

Se quiser voltar a exigir JSON estruturado:

- Response Format: **JSON**
- model\_kwargs.response\_format: `{ "type": "json_object" }`
- Acrescente no **system**: “Responda **EXCLUSIVAMENTE em JSON** …”.

Causa: você quer “achatar” a saída do BRANN e devolver **só o texto humano**, sem JSON, sem markdown, sem emojis.  
Use este **Code (JavaScript)** logo após o nó do LLM/Agent e antes do envio.

## Code — “Text Final”

```markdown
// Entrada possível:
// 1) objeto: { out: { type:"text", text:"..." } }
// 2) string JSON: '{"out":{"type":"text","text":"..."}}'
// 3) texto solto com markdown

const src = $json.output ?? $json;  // se seu nó anterior coloca em "output", use isso

function safeParse(s) {
  try { return JSON.parse(s); } catch { return null; }
}

function pickText(x) {
  if (!x) return "";
  if (typeof x === "string") {
    // tenta parsear JSON
    const j = safeParse(x.trim());
    if (j) return pickText(j);
    // fallback: regex pega "text":"..."
    const m = x.match(/"text"\s*:\s*"([\s\S]*?)"/);
    if (m) return m[1];
    return x;
  }
  if (typeof x === "object") {
    return x.out?.text ?? x.text ?? x.message?.content ?? "";
  }
  return String(x);
}

function clean(s) {
  if (!s) return "";
  let t = s;

  // remove blocos \`\`\`code\`\`\` e \`inline\`
  t = t.replace(/\`\`\`[\s\S]*?\`\`\`/g, " ");
  t = t.replace(/\`[^\`]*\`/g, " ");

  // [texto](url) -> texto
  t = t.replace(/\[([^\]]+)\]\(([^)]+)\)/g, "$1");

  // remove tags HTML
  t = t.replace(/<[^>]+>/g, " ");

  // remove markdown leve (* _ ~ # >)
  t = t.replace(/[*_~>#]/g, "");

  // remove emojis e pictogramas
  t = t.replace(/[\p{Extended_Pictographic}\p{Emoji_Presentation}]/gu, "");

  // normaliza espaços
  t = t.replace(/\s+/g, " ").trim();

  // corta ruído tipo “Out: { ... }” que sobrou
  t = t.replace(/^out\s*:\s*/i, "").trim();

  return t;
}

const raw = pickText(src);
const text = clean(raw);

return { json: { text } };
```

## Encadeamento

1. **OpenAI / Agent BRANN** → sai `output`
2. **Code “Text Final”** (acima) → sai `{ text }`
3. **HTTP Request → Evolution `/sendMessage`**  
	Body:
```markdown
{ "to": "={{$json.phone || $item(0,'Normalize Final').$json.phone}}", "text": "={{$json.text}}" }
```

## Observações

- Se seu nó anterior já coloca o JSON em outro campo, ajuste `const src = $json.output ?? $json;`.
- O código tolera: objeto, string JSON ou texto solto.
- Remove markdown, HTML e emojis. Mantém acentuação e pontuação.

O nó **IF** quebrou porque você usou **“is true”** com um **string**. Esse operador espera um booleano. O valor `{{$json.text}}` é `"Oi! …"` (string), não `true/false`.

Correções válidas. Escolha 1:

1. **String não vazia**  
	Parameters → Conditions → **String**
- Value1: `{{$json.text}}`
- Operation: **not equal**
- Value2: `""`
2. **Boolean explícito**  
	Parameters → Conditions → **Boolean**
- Value1: `{{ !!($json.text && $json.text.trim().length) }}`
- Operation: **is true**
3. **Converter tipos**  
	Ligue a opção **Convert types where required** e mantenha:
- Value1: `{{ $json.text }}`
- Operation: **is true**  
	Obs.: menos explícito. Prefira 1 ou 2.

Dica adicional n8n:

- Se o IF não recebe diretamente o item certo, referencie o nó anterior:  
	`{{$item(0, 'Text Final').$json.text}}`
- Para checar nulo/indefinido e vazio em uma vez:  
	`{{ !!($item(0,'Text Final').$json.text ?? '').trim() }}`

Depois do IF:

- Ramo **true** → enviar mensagem.
- Ramo **false** → fallback curto: “Não veio texto útil.”