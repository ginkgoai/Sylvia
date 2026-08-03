---
title: "GKO - Ajuste no roteamento Brann"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/6920ac7f-262c-832d-a084-ea4d3b03ab84"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sex., 21 de nov. às 15:16

![f9994085-4ecf-4554-9ea2-17ffab241ed0.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000ef7c71f5b198a0a280e19208&ts=495692&p=fs&cid=1&sig=15d840e93423b1f64cbb567897ae22e51a5cd57dbf30670edbde483347c3450e&v=0)

mesmo problema

![71b6c67e-bdb7-4a10-82a0-d6e2b046695c.png](https://chatgpt.com/backend-api/estuary/content?id=file_0000000094f471f5bbea4411d1c85ed9&ts=495692&p=fs&cid=1&sig=8487559eb6e9710896d0924918716f77c981e993b2970ea933d1802f92651117&v=0)

?

Boa, essa tela era exatamente o que eu precisava ver.

Sim, o formato está **quase** certo, o ajuste é só de detalhe:

### 1\. Regra (CSV) – como tem que ficar

No bloco da regra:

- Esquerda (Expression):  
	`{{$json.extension}}`
- Operador:  
	`is equal to`
- Direita (Value):  
	`csv` ← só isso, SEM `text/`

Se embaixo ainda aparece escrito `text/csv`, significa que o valor à direita ainda está `text/csv`.  
Abre esse campo, apaga tudo e deixa somente:

```markdown
csv
```

A linha de cima deve ler exatamente:

```markdown
{{$json.extension}} is equal to csv
```

sem nenhuma linha cinza embaixo com `text/csv`.

### 2\. Repete a lógica para os outros

- PDF → `{{$json.extension}} is equal to pdf`
- DOCX → `{{$json.extension}} is equal to docx`
- XLS → `{{$json.extension}} is equal to xls`
- TXT → `{{$json.extension}} is equal to txt`
- etc.

### 3\. Teste rápido que garante que deu certo

1. Manda um **PDF** pro Brann.
2. Abre a execução → nó **Map file extensions** → aba JSON.  
	Tem que ver algo como:
	```markdown
	"extension": "pdf",
	"fileType": "pdf"
	```
3. No nó **Route Document Types**, o item tem que aparecer na aba **PDF**, não em ELSE.

Se depois disso ainda cair em ELSE, o próximo suspeito é o nome do binário no Download (aí te passo o código do Function ajustado pra `data` / `document` conforme estiver aí).

2/2

Boa, agora dá pra padronizar de vez.  
Hoje você está misturando:

- algumas regras olhando `{{$json.extension}}`
- outras olhando `{{$json.fileType}}` com MIME (`application/pdf`, etc.)
- e o Function não está garantindo um padrão.

Vamos colocar tudo no trilho em **2 passos**.

---

## 1) Function “Map file extensions” – padrão único

No nó **Map file extensions**, deixa assim:

```markdown
// Pega o item atual
const item = items[0] || { json: {}, binary: {} };

// Ajuste aqui o nome do binário principal.
// Pelo teu print ele se chama "data".
const bin =
  item.binary?.data ||    // <- principal
  item.binary?.document || // fallback, se um dia mudar
  null;

let fileName = "";
let mimeType = "";
let extension = "unknown";

if (bin) {
  fileName = bin.fileName || "";
  mimeType = bin.mimeType || "";
}

// fallback se vier algo no json
if (!fileName && item.json.fileName) {
  fileName = item.json.fileName;
}
if (!mimeType && item.json.mimeType) {
  mimeType = item.json.mimeType;
}

// calcula extensão
if (fileName && fileName.includes(".")) {
  extension = fileName.split(".").pop().toLowerCase();
} else if (mimeType && mimeType.includes("/")) {
  extension = mimeType.split("/").pop().toLowerCase();
}

// devolve com padrão
return [
  {
    json: {
      ...item.json,
      fileName,
      mimeType,
      extension,         // ex: pdf, xlsx, json
      fileType: mimeType // ex: application/pdf
    },
    binary: item.binary,
  },
];
```

Depois de salvar, roda um teste e, no **Map file extensions → JSON**, você deve ver algo do tipo:

```markdown
{
  "fileName": "contrato.pdf",
  "mimeType": "application/pdf",
  "extension": "pdf",
  "fileType": "application/pdf",
  ...
}
```

Esse é o padrão que vamos usar.

---

## 2) Route Document Types – tudo olhando {{$json.fileType}}

Agora padroniza TODAS as regras do **Route Document Types** assim:

Sempre:

- Expression: `{{$json.fileType}}`
- Operator: `is equal to`
- Value: (MIME abaixo)
- Output Name: conforme o tipo

Sugestão de tabela:

1. **CSV**
	- `{{$json.fileType}} is equal to text/csv`
		- Output Name: `CSV`
2. **HTML**
	- `{{$json.fileType}} is equal to text/html`
		- Output Name: `HTML`
3. **Calendar (ICS)**
	- `{{$json.fileType}} is equal to text/calendar`
		- Output Name: `Calendar`
4. **RTF**
	- `{{$json.fileType}} is equal to text/rtf`
		- Output Name: `RTF`
5. **TXT**
	- `{{$json.fileType}} is equal to text/plain`
		- Output Name: `TXT`
6. **XML**
	- `{{$json.fileType}} is equal to application/xml`  
		(se o Evolution mandar `text/xml`, coloca esse; se quiser, faz duas regras)
		- Output Name: `XML`
7. **PDF**
	- `{{$json.fileType}} is equal to application/pdf`
		- Output Name: `PDF`
8. **XLS**
	- `{{$json.fileType}} is equal to application/vnd.ms-excel`
		- Output Name: `XLS`
9. **XLSX**
	- `{{$json.fileType}} is equal to application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
		- Output Name: `XLSX`
10. **JSON (se quiser tratar separado)**
	- `{{$json.fileType}} is equal to application/json`
		- Output Name: `JSON`
11. **ELSE (fallback)**
	- Regra final:
		- Expression: `{{$json.fileType}}`
				- Operator: `exists`
				- Output Name: `ELSE`

Assim você tem:

- **Função** sempre gerando `fileType = mimeType`
- **Route** sempre roteando por `fileType` (MIME)
- `extension` fica disponível só se você precisar lá na frente.

---

## 3) Conferência rápida

1. Manda um **PDF** pro Brann.
2. `Download Document` → Binary: deve mostrar `application/pdf`.
3. `Map file extensions` → JSON: vê `mimeType: application/pdf` e `fileType: application/pdf`.
4. `Route Document Types` → o item deve estar na aba **PDF**, não em ELSE.

No print que você mandou, o arquivo era `data.json` (`application/json`), então é esperado cair em **JSON** ou **ELSE**, não em PDF. Com o padrão acima, isso fica totalmente controlado.

Se quiser depois, te monto o bloco “Download → Map file extensions → Route Document Types” pronto para importar em qualquer fluxo Brann como módulo padrão de ingestão de documentos.

Sim, dá pra deixar isso bem mais simples e “burro”:  
em vez de tentar adivinhar tipo por tipo, você pode ter um **“Leitor Universal de Documentos”** que recebe qualquer arquivo e devolve apenas **texto limpo** para o Brann.

Pensa assim:  
o Route de tipos é um painel de controle cheio de alavancas; o que você quer agora é um **único funil** que esmague qualquer PDF/DOCX/XLSX/IMG em texto.

Vou te passar o setup enxuto.

---

## 1\. Princípio: 1 nó para ler qualquer arquivo

Hoje você tem:

Webhook → Download Document → Map file extensions → Route Document Types → vários “Extract from …”

O que você quer:

Webhook → Download Document → **OpenAI (Leitor Universal)** → texto → Brann

Ou seja:  
mantém o Download funcionando, e **substitui Route + Extracts** por UM OpenAI Chat Model com arquivo binário.

---

## 2\. Nó “Download Document” (mantém)

Só garante:

- `Response Format: File`
- `Binary Property`: `data` (é o que aparece no print)
- No output, na aba Binary, você vê `data` com:
	- `fileName`
		- `mimeType`
		- `fileSize`

Se isso aparece, estamos prontos.

---

## 3\. Criar o nó “Leitor Universal de Documentos” (OpenAI)

Logo depois de **Download Document**, adiciona:

### 3.1. Node

- Tipo: **OpenAI Chat Model**
- Model: `gpt-4o-mini` (rápido/barato) ou `gpt-4o` se quiser mais robusto
- Input:
	- Marca a opção de **Binary data**
		- `Binary Property`: `data`

### 3.2. System Prompt (coloca algo assim):

```markdown
Você recebe um arquivo em anexo (PDF, Word, planilha, imagem, JSON ou outro formato).

Sua missão:
1. Ler o conteúdo do arquivo.
2. Converter tudo em TEXTO ÚNICO, em português claro.
3. Se for tabela/planilha, transforme em texto estruturado (títulos, linhas principais, valores relevantes).
4. Se o arquivo tiver muito lixo técnico (metadados, HTML, JSON bruto), ignore o ruído e mantenha só o que é útil para entendimento humano.

Retorne APENAS texto corrido, sem JSON, sem marcação especial.
```

### 3.3. User prompt (pode ser simples):

```markdown
Leia o arquivo e devolva o conteúdo em texto útil para atendimento ao cliente.
```

### 3.4. Saída

Esse nó vai gerar algo como:

- `json.output_text` ou `json.choices[0].message.content` (depende do node)

Então você adiciona um **Set** em seguida:

```markdown
text = {{$json.output_text || $json.choices[0].message.content || $json.data || $json.result}}
```

E a partir daí, **todo o resto do fluxo Brann** usa `{{$json.text}}` como se fosse mensagem normal de texto.

---

## 4\. E o Route Document Types, fica onde?

Três opções:

1. **Desliga tudo** (mais simples)  
	Se o objetivo agora é “qualquer documento vira texto para o agente”, você pode simplesmente:
	- Pular o Route
		- Pular Extract from PDF/XLS/XLSX
		- Ligar **Download → OpenAI Leitor → Set(text) → fluxo Brann**
2. Mantém Route só para casos especiais  
	Ex.: quando for XLS ou CSV você quer realmente processar número por número, não só “ler”.  
	Aí você mantém:
	- Se `fileType` específico (ex.: `application/vnd.ms-excel`) → vai para pipeline de planilha
		- Else → cai no **Leitor Universal**
3. Mantém só para JSON bruto  
	Para `application/json`, você pode:
	- Converter com um Function:
		```markdown
		return [
		  {
		    json: {
		      ...$json,
		      text: JSON.stringify($json, null, 2),
		    },
		  },
		];
		```
		- E mandar esse `text` pro Brann.

---

## 5\. Resumão direto

Você não é obrigado a:

- Detectar todos os MIME types
- Fazer Extract separado para PDF/DOCX/XLSX/etc.

Você pode:

1. Baixar o arquivo (`data` binário).
2. Jogar esse binário direto num **OpenAI Chat Model** como input.
3. Dizer pro modelo: “lê qualquer coisa e devolve texto útil”.
4. Padronizar a saída em um campo `text`.
5. Entregar esse `text` pro Brann como se fosse mensagem normal.

Isso transforma o Brann num **“leitor universal de anexos”**: o usuário manda um doc, ele lê, entende, comenta, responde, sem você ficar preso na frição de MIME.

Se quiser, no próximo passo eu te escrevo o “cluster” mínimo em formato de JSON de workflow n8n:  
`Download Document → OpenAI Leitor → Set(text)`, pronto pra importar e plugar no teu fluxo.