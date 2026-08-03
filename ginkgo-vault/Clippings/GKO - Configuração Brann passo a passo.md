---
title: "GKO - Configuração Brann passo a passo"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/6916b48f-9d30-8327-aa95-7dfae04fceb3"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sex., 14 de nov. às 1:48

![ff1b8dd4-b4aa-4b31-8291-f909249bc904.png](https://chatgpt.com/backend-api/estuary/content?id=file_000000007e1071f5bc16c84a85904b5c&ts=495692&p=fs&cid=1&sig=8fa693405ed206c4ae3bfadeb3dcaba2608f75ed415260dc4f30945bb5608947&v=0) ![b44da254-8668-479a-84f2-e4c5da41f4ee.png](https://chatgpt.com/backend-api/estuary/content?id=file_0000000067d0720eaf2cb5c3c09293b9&ts=495692&p=fs&cid=1&sig=7060564b062b28acbc0d620a5072c75945e07a559905987d8404971e6889dff5&v=0) ![8abe067a-64e4-4cc9-a5c1-d183094f667e.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000c06471f5ac9cf099340b0af1&ts=495692&p=fs&cid=1&sig=5e702d2cacb2a148b41d4f0d80740aec95ad024faf751280a374363657c4c0ac&v=0) ![f57930e5-349d-44c4-a6fb-a04c99bde197.png](https://chatgpt.com/backend-api/estuary/content?id=file_0000000071a071f59315ed010869530f&ts=495692&p=fs&cid=1&sig=6613c41ff0eb12039f8a62186902cba23ebcaae6260db8c1baa4696b416bd399&v=0) ![b437c832-59e5-4c57-8300-18fcc4f0c505.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000c1b071f5b50c1b5baae8e829&ts=495692&p=fs&cid=1&sig=9c98dd13465839ef0f19331edf0aa2e7fea283330e25ae2af0a532f38021a842&v=0) ![5997229c-5a4c-4128-a981-aafffb970dd4.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000264871f586630ef56ef4e63f&ts=495692&p=fs&cid=1&sig=10dcdace7c590309f43d547fdbf50fc0a2d3768f3c6486dce1edf1f831f4c1e5&v=0) ![5497056e-7a34-4f43-a94c-9d52c0409715.png](https://chatgpt.com/backend-api/estuary/content?id=file_0000000048c871f58ffde44c8ce8e36e&ts=495692&p=fs&cid=1&sig=3b9a17e97caaee5a47a1522295d9e7a3871e653d19ee77ea9ee0512e289cc3c1&v=0) ![151bb80a-e9ee-4d07-80bb-46be03311455.png](https://chatgpt.com/backend-api/estuary/content?id=file_0000000025d4720e8db323a6117d2a00&ts=495692&p=fs&cid=1&sig=2286661063e4627bd6a31698179ef5d02d31b1d6f268773118e724427929aa77&v=0)

vamos configurar o brann, precisamos validar todas as transrições restantes imagem video e doc e consertar a quebra de texto final que esta dando erro, e ajeitar o prompt deixar ele perfeito para o fluxo, configurar corretamente o no de base vetorial. faça um passo a passo para alinhar tudo isso até podermos ligar para o atendimento real a um cliente.

![2a762975-3e69-4f09-ae05-616d7e207019.png](https://chatgpt.com/backend-api/estuary/content?id=file_000000000cfc720ebc88f8655ea39807&ts=495692&p=fs&cid=1&sig=007e3c9eec9e0751b5785e24e389fd4dd61bc3c1ca102bf85aadec9ad31afabf&v=0) ![24ad0642-43a5-4222-913e-5af7c4bc4740.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000935c720ebb7fd3a23f1e3fa8&ts=495692&p=fs&cid=1&sig=70dfcd88029ac164767ff5111bad7050295ed964d08b5da9fd1195b3e45fc051&v=0)

imagem okay bora pro videoa contrução e essa? ou diferente

Use isso no campo **Text Input**:

```markdown
Você é um assistente analisando um vídeo recebido pelo WhatsApp.

1) Descreva em português, de forma objetiva, o que acontece no vídeo.
2) Liste ações importantes, objetos relevantes, locais e pessoas envolvidas.
3) Se houver falas audíveis, resuma o que foi dito em 1–2 frases.
4) No final, explique em 1 frase qual é a intenção provável do vídeo no contexto de um atendimento ou suporte.

Responda sempre em texto corrido, sem markdown, sem bullets e sem usar códigos. Seja claro e direto.
```

Perfeito, o motivo é o mesmo que tinha no vídeo.

No print:

- **INPUT**: `MENSAGEM_TIPO = "documentMessage"`
- **Regra do Document** no Route Types:  
	`{{ $json.MENSAGEM_TIPO }} is equal to document`

Ou seja, o valor real é **`documentMessage`**, mas a regra está esperando **`document`**.  
Por isso a aba **Document** mostra “No output data in this branch”.

---

## Ajuste no Route Types para PDF/Document

1. Abra o node **Tipos de Rotas**.
2. Vá até a regra de **Document**.
3. Deixe exatamente assim:
- Expression:
```markdown
{{ $json.MENSAGEM_TIPO }}
```
- Operador: `is equal to`
- Value:
```markdown
documentMessage
```
- `Rename Output`: ON
- `Output Name`: `Document`
4. Clique em **Execute previous nodes** e depois **Execute step** no `Tipos de Rotas`.
5. No painel OUTPUT, selecione a aba **Document**: agora deve aparecer 1 item com:
	- `Base64` do arquivo
		- `Mensagem_ID`
		- etc.

A partir daí, esse item segue para o seu fluxo:

```markdown
Document  →  Baixar documento  →  extensões de arquivos de mapa  →  Tipos de documentos da rota (CSV/HTML/PDF/...)
```

Quando isso estiver aparecendo na aba **Document**, me manda o próximo print (provavelmente do node “Baixar documento” ou da rota “PDF”) que eu fecho a parte de transformar o PDF em texto para o Agent.

Ótimo, a rota está certa. Agora é só deixar o caminho do **PDF → TEXTO** redondinho pro Agent.

Hoje:

```markdown
Route Types (Document)
   ↓
Download Document
   ↓
Map file extensions
   ↓
Route Document Types (PDF)
   ↓
Extract from PDF
   ↓
Map3
   ↓
Text Final → resto do fluxo/Agent
```

Vou te dar o “copy/cola” pra cada nó dessa rota.

---

## 1\. Download Document

Aqui você precisa sair já com o **arquivo binário** ou com **Base64**.

Exemplo usando Evolution (ajuste pro endpoint que você estiver usando):

- Node: HTTP Request (renomeado pra **Download Document**)
- Method: `POST`
- URL: `={{$json.url || 'https://evo.ginkgo…/downloadMedia'}}` (se já vier `url` no JSON, usa ela)
- Body (JSON):
```markdown
{
  "instance": "={{$json.INSTANCIA}}",
  "apikey": "={{$json.APIKEY}}",
  "messageId": "={{$json.Mensagem_ID}}"
}
```

Se a resposta vier em **Base64**, adiciona logo depois um **Move Binary Data** (ou aproveita o próprio Download Document com Response Binary).

### Caso venha Base64

Adicione um node `Move Binary Data` logo após (se ainda não tiver):

- Operation: `Move Base64 String to File`
- Base64 Input Field:
```markdown
={{ $json.Base64 }}
```
- Put Output File In Field: `data`
- Options:
	- File Name:
```markdown
{{$json.fileName || $json.nome_arquivo || 'documento.pdf'}}
```
- File Extension: `pdf`

Depois disso, o item tem `binary.data` com o PDF.

Se o seu **Download Document** já está configurado pra receber binário, só garante que o **Binary Property** seja `data`.

---

## 2\. Map file extensions (JS)

Esse JS precisa gerar um campo único `extension` para o roteador de documentos.

No node **Map file extensions** (Code):

```markdown
const item = items[0].json;

const name =
  item.fileName ||
  item.nome_arquivo ||
  item.filename ||
  '';

const mime =
  item.mimetype ||
  item.mime_type ||
  '';

let ext = '';

if (name && name.includes('.')) {
  ext = name.split('.').pop().toLowerCase();
} else if (mime) {
  if (mime === 'application/pdf') ext = 'pdf';
  else if (mime.includes('excel') || mime.includes('spreadsheet')) ext = 'xlsx';
  else if (mime.includes('csv')) ext = 'csv';
  else if (mime.startsWith('text/')) ext = 'txt';
}

return [
  {
    json: {
      ...item,
      extension: ext || 'outro',
    },
  },
];
```

Resultado esperado: `extension = "pdf"` quando o arquivo for PDF.

---

## 3\. Route Document Types (rotear PDF, XLS, etc.)

No node **Route Document Types**:

- Mode: `Rules`.
- Para o PDF:
	- Expression:
	```markdown
	{{ $json.extension }}
	```
	- `is equal to` → `pdf`
		- `Rename Output`: ON
		- `Output Name`: `PDF`

Conecta a saída `PDF` no node **Extract from PDF**.

Os outros ramos (CSV, XLS, etc.) você já tem na tela; só garante que todos usam `{{ $json.extension }}` como expressão.

---

## 4\. Extract from PDF

Node **Extract from PDF**:

- Binary Property: `data` (o mesmo nome que você usou lá no Move Binary Data / Download).
- Operation: `Extract Text`
- Options:
	- `Split Pages`: desativado, a não ser que você queira texto por página.
		- `Encoding`: deixe padrão.

Execute o node com um PDF real e veja a aba **JSON**. Normalmente ele devolve:

```markdown
{
  "text": "conteúdo completo do pdf…"
}
```

---

## 5\. Map3 – transformar PDF em MENSAGEM para o fluxo

No **Map3** (o da rota do PDF):

- Mode: `Manual Mapping`.
- Fields to set:
1. `MENSAGEM` (String):
```markdown
{{ $json.text || $json.content || '' }}
```
2. `NUMERO_LEAD` (ou `phone`, conforme seu padrão):
```markdown
{{$json.NUMERO_LEAD}}
```
3. (Opcional) `MENSAGEM_TIPO`:
```markdown
'pdf'
```

Deixe `Include Other Input Fields` desligado, exceto se você quiser carregar mais contexto.

Conecte a saída do **Map3** para o mesmo ponto do fluxo onde o texto da imagem, áudio e vídeo já está indo (seu `Text Final` / `AGRUPA MSG`).

---

## 6\. Teste rápido do PDF

1. Mandar um PDF pelo WhatsApp.
2. Logs:
	- `Route Types` → branch **Document** com `Base64`.
		- `Download Document` → Binary `data`.
		- `Map file extensions` → `extension: "pdf"`.
		- `Route Document Types` → branch **PDF** com 1 item.
		- `Extract from PDF` → JSON com `text`.
		- `Map3` → JSON com `MENSAGEM` já em texto.
3. Conferir se o Agent responde com base no conteúdo do PDF (como se o texto tivesse sido digitado).

Com isso, você fecha o pacote:

- Imagem → descrita e interpretada.
- Vídeo → resumido e transcrito.
- PDF → extraído e jogado como mensagem de texto.

Tudo convergindo na mesma entrada do Brann para o Agent.