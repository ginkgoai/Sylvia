---
title: "GKO - Rota de documentos n8n"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/6928d593-5774-8327-9327-3ee59d6252c6"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
qui., 27 de nov. às 19:49

Análise do Bloco "TRANSCRIÇÃO" 1. Nó Route Types (Switch) Função: Este é o "roteador" de mídias. Ele olha o campo mensagem\_tipo que normalizamos no bloco anterior e direciona o fluxo para o caminho certo. Configuração: Você configurou rotas para text, audioMessage, imageMessage, videoMessage, e documentMessage. Está perfeito. Isso garante que cada tipo de mídia receba o tratamento adequado. 2. Rotas Existentes (Áudio, Imagem, Vídeo) Áudio: Code in JavaScript (provavelmente para converter/preparar) → OpenAI Transcribe Recording → Map1. Lógica sólida e direta para transcrição de áudio. Imagem: Convert to File → OpenAI Analyze Image → Map5. Perfeito para OCR e análise de imagem. Vídeo: Convert to File1 → Analyze video → Map6. Também correto, provavelmente usando um modelo de visão para resumir ou transcrever o conteúdo do vídeo. 3. O Problema: A Rota de Documentos (documentMessage) Fluxo Atual (Desativado): Download Document → Supabase Vector Store → AI Agent. Por que não funciona diretamente: Os nós de IA padrão (como o da OpenAI) geralmente não aceitam um arquivo binário (como um PDF) diretamente para "transcrição" da mesma forma que aceitam áudio ou imagem. Eles precisam do texto extraído do documento primeiro. O Supabase Vector Store serve para armazenar e buscar texto já processado (embeddings), não para extraí-lo. Solução: Usar o Manus (Coringa) como um Serviço de Extração de Texto (OCR/Parser) Sua ideia de baixar o documento, enviá-lo para o Supabase e me deixar transcrevê-lo é genial. Isso cria um fluxo assíncrono e muito poderoso. Vamos refinar e implementar essa lógica: Passo A: O n8n Baixa o Documento e o Armazena Download Document (Ativar este nó): Este nó receberá a URL do documento enviada pela Evolution API. Ele deve ser configurado para baixar o arquivo e disponibilizá-lo como um dado binário no fluxo do n8n. Novo Nó: Supabase Storage Upload Adicione um nó do Supabase para fazer upload de arquivos (Storage). Bucket: Crie um bucket no seu Supabase chamado, por exemplo, document\_uploads. Ação: Configure o nó para pegar o arquivo binário do Download Document e fazer o upload para este bucket. É importante que o nome do arquivo seja único (pode usar o mensagem\_id ou um UUID). Resultado: Este nó retornará a URL pública ou o caminho do arquivo recém-criado no Supabase Storage. Passo B: O n8n me Delega a Tarefa de Transcrição Nó Coringa (HTTP Request para Manus): Agora, em vez de chamar um nó de IA, você me chama. Ação: Você me envia uma requisição com a tarefa de processar o documento que acabou de ser salvo. Exemplo do Body da Requisição para mim: JSON { "task": "extract\_text\_from\_document", "context": { "document\_url": "{{ $json.supabase\_public\_url }}", // A URL pública do arquivo que o nó anterior retornou "original\_message\_id": "{{ $json.mensagem\_id }}", "user\_phone": "{{ $json.numero\_lead }}" } } Passo C: Eu (Manus) Faço o Trabalho Pesado Minha Execução Interna: Eu recebo a URL do documento no Supabase Storage. Eu baixo o arquivo (PDF, DOCX, etc.). Eu uso minhas próprias ferramentas internas de OCR (Optical Character Recognition) e parsing de documentos para extrair todo o texto contido nele. Eu retorno o texto extraído para o seu fluxo n8n. Exemplo da Minha Resposta (JSON): JSON { "status": "success", "intent": "document\_text\_extraction", "data": { "extracted\_text": "Este é todo o conteúdo de texto que foi extraído do documento PDF...", "character\_count": 12345, "page\_count": 5 }, "suggested\_reply": "Recebi e processei o documento que você enviou. Ele contém X páginas e fala sobre \[resumo do conteúdo\]. Como posso te ajudar com base nele?", "logs": \[...\] } Passo D: O n8n Unifica o Resultado Nó Map7 (Ativar e Renomear para Set Transcribed Text): Este nó receberá a minha resposta. Ele deve ser configurado para extrair o campo data.extracted\_text do meu JSON. O resultado dele será um campo MENSAGEM (ou transcribed\_text) que conterá o texto completo do documento. Nó Text Final: Este nó agora pode receber o texto transcrito de qualquer uma das rotas (áudio, imagem, vídeo ou documento), unificando o fluxo. A partir daqui, o texto pode ser enviado para o BRANN para interpretação e resposta. Resumo da Nova Arquitetura para Documentos: Route Types → Download Document → Supabase Storage Upload → Coringa (call Manus) → Set Transcribed Text → Text Final Esta abordagem é superior porque: É Universal: Funciona para PDF, DOCX, TXT, etc. É Robusta: O armazenamento no Supabase cria um registro do arquivo original. É Poderosa: Eu posso usar as melhores ferramentas de OCR e parsing para cada tipo de arquivo, uma complexidade que você não precisa gerenciar no n8n. Próximos Passos: Crie um bucket chamado document\_uploads no seu Supabase Storage. Ajuste o fluxo de documentos no n8n para seguir a arquitetura que desenhamos. Vamos fazer um teste de ponta a ponta: envie um PDF para o WhatsApp e veja o texto extraído aparecer no final do fluxo. VAMOS CONFIGURAR A TRANSCRIÇÃO DE DOCUMENTOS USANDO A MANUS COMO TRADUTOR

qui., 27 de nov. às 21:23

mudo algo?

agora foi

e aqui

assim?

confere

?

este?

e esse?

Arquitetura: Pipeline de Ingestão e Qualificação de Conhecimento O Conceito: Qualquer documento (contrato, proposta, relatório, artigo) enviado para o BRANN não é apenas lido para responder a uma pergunta imediata. Ele é ingerido, processado, classificado e armazenado permanentemente na base de conhecimento da Ginkgo, tornando o sistema mais inteligente a cada novo arquivo. O Fluxo (Versão 2.0): Fase 1: Captura e Armazenamento (n8n) Webhook → Tratamento de Dados: Um documento é recebido via WhatsApp. Route Types: O fluxo é direcionado para a rota documentMessage. Download Document: O n8n baixa o arquivo. Supabase Storage Upload: O n8n faz o upload do arquivo bruto para um bucket no Supabase Storage, por exemplo, raw\_uploads. Metadados: Ao fazer o upload, o n8n já pode associar metadados importantes: user\_phone, message\_id, upload\_timestamp. Resultado: O n8n obtém a URL do arquivo armazenado. Fase 2: Delegação e Processamento Profundo (Manus/Coringa) Coringa (call Manus): O n8n me aciona, mas agora com uma tarefa mais estratégica. Novo Body da Requisição para mim: JSON { "task": "ingest\_and\_qualify\_document", "context": { "document\_url": "{{ $json.supabase\_public\_url }}", "source\_channel": "whatsapp", "uploaded\_by": "{{ $json.numero\_lead }}", "original\_message\_id": "{{ $json.mensagem\_id }}" } } Minha Execução Interna (Onde a Mágica Acontece): a. Extração: Eu baixo o documento da URL e extraio todo o seu conteúdo textual usando OCR/parsing. b. Análise e Sumarização: Eu leio o texto extraído e realizo uma análise semântica para entender: Qual é o tópico principal do documento? (Contrato, Fatura, Artigo de IA, Relatório de Vendas?) Quais são as entidades chave? (Nomes de pessoas, empresas, valores, datas). Qual é o resumo do documento? Qual é a importância ou sensibilidade do conteúdo? (Confidencial, Público, Financeiro). c. Geração de Embeddings: Eu pego o texto (seja ele completo ou dividido em pedaços/chunks) e o transformo em vetores numéricos (embeddings) para busca semântica futura. d. Decisão de Roteamento: Com base na análise, eu decido em qual(is) tabela(s) do Supabase essa informação deve residir. Fase 3: Armazenamento Estruturado e Resposta (Manus → n8n) Minha Ação no Supabase: Eu não devolvo apenas o texto. Eu preparo e executo as operações no Supabase. Exemplo de Decisão: Se o documento for um contrato de um novo cliente: Ação 1: Inserir os chunks de texto e seus embeddings na tabela kb\_chunks com metadados { "type": "contract", "customer\_id": "...", "status": "active" }. Ação 2: Atualizar a tabela customers para o cliente correspondente, adicionando uma nota em seu registro: notes: "Contrato assinado e ingerido em \[data\]. Link no Storage: \[URL\]". Se o documento for um artigo genérico sobre IA: Ação 1: Apenas inserir os chunks e embeddings na kb\_chunks com metadados { "type": "general\_knowledge", "topic": "AI" }. Minha Resposta para o n8n: Eu informo ao n8n exatamente o que eu fiz. Exemplo da Minha Resposta (JSON): JSON { "status": "success", "intent": "document\_ingestion\_and\_qualification", "data": { "document\_summary": "O documento é um contrato de 12 páginas para o plano Wave com a empresa 'Acme Corp', assinado por João Silva.", "storage\_operations": \[ { "table": "kb\_chunks", "action": "insert", "rows\_affected": 25 }, { "table": "customers", "action": "update", "rows\_affected": 1 } \] }, "suggested\_reply": "Recebido e arquivado! Processei o contrato com a Acme Corp. e já atualizei o cadastro deles em nosso sistema. Há algo mais que eu possa fazer?", "logs": \[...\], "meta": { "notes": "Documento classificado como 'Contrato' e associado ao cliente XYZ." } } Fase 4: Confirmação (n8n → Usuário) Set Final Message: O n8n recebe meu suggested\_reply. Send to WhatsApp: O BRANN usa a sugestão para dar uma resposta inteligente e contextual ao usuário, confirmando que a ação foi concluída com sucesso. Vantagens Desta Arquitetura Sistema Auto-Aperfeiçoável: Sua base de conhecimento cresce e se torna mais valiosa a cada interação. Automação de Processos de Negócio: Você não está só transcrevendo, está automatizando o arquivamento de contratos, a qualificação de documentos, etc. Inteligência Centralizada: A lógica complexa de "o que fazer com este documento?" fica centralizada em mim, mantendo o fluxo do n8n limpo e focado na orquestração. Escalabilidade: Este modelo suporta dezenas, centenas ou milhares de documentos sem que você precise alterar o fluxo do n8n. Esta é a visão correta. É como se constrói um verdadeiro "cérebro" corporativo, e não apenas um chatbot. Estou 100% alinhado e pronto para operar desta forma. Podemos começar a adaptar o fluxo para este modelo mais avançado.

qui., 27 de nov. às 23:58

Boa. Vamos transformar esse conceito do “Alfred/Manus ingestor” em fio de cobre no n8n, nó por nó.

Vou assumir essa sequência, que já aparece no print:

`Route Types (document) → Download Document → Inserir Supabase → Public cUrl → Alfred → Map7 → Text Final → BUFFER`

E que **quem faz OCR, resumo, embeddings e operações no Supabase é a Manus**, via task `ingest_and_qualify_document` (Vector Store do n8n deixa de ser obrigatório).

---

## 1\. Nó: Download Document

Se já está baixando o PDF, só garante três pontos:

- **Tipo**: HTTP Request (ou nó Evolution específico)
- **Output**:
	- Aba **Binary**: deve existir um binário, ex.: `data`
		- Aba **JSON**: já vem com:
		- `mensagem_id`
				- `numero_lead` (telefone)
				- qualquer outro metadado útil

Se o binário tiver outro nome, use ele nas próximas etapas (ex.: `document` em vez de `data`).

---

## 2\. Nó: Inserir Supabase (HTTP Upload)

Esse é o uploader de PDF pro bucket `raw_uploads`.

### Parameters

- **Method**: `POST`
- **URL**:
```markdown
https://<SEU_PROJECT>.supabase.co/storage/v1/object/raw_uploads/{{ $json.mensagem_id }}.pdf
```

Substitua `<SEU_PROJECT>` pelo subdomínio do teu Supabase, ex.:

```markdown
https://ginkgoxyz.supabase.co/storage/v1/object/raw_uploads/{{ $json.mensagem_id }}.pdf
```

### Headers

Ativa **Send Headers** e adiciona:

1. `apikey`
	```markdown
	={{ $env.SUPABASE_API_KEY }}
	```
2. `Authorization`
	```markdown
	=Bearer {{ $env.SUPABASE_API_KEY }}
	```
3. `Content-Type`
	```markdown
	application/pdf
	```
4. `x-upsert`
	```markdown
	true
	```

### Body

- **Send Body**: ON
- **Body Content Type**: `Binary File`
- **Binary Property**:  
	`data`  
	(ou o nome do binário vindo do Download Document)

Saída esperada (JSON):

```markdown
{
  "Key": "raw_uploads/123456.pdf"
}
```

---

## 3\. Nó: Public cUrl (Set)

Aqui você cria a URL pública que o Alfred vai usar.

### Parameters

- **Operation**: `Set`
- **Mode**: `Add Fields`

Adicionar campo:

- **Name**: `publicUrl`
- **Value (Expression)**:
```markdown
={{ 'https://<SEU_PROJECT>.supabase.co/storage/v1/object/public/raw_uploads/' + $json.mensagem_id + '.pdf' }}
```

Substitua `<SEU_PROJECT>` pelo mesmo de cima.

Se quiser já carregar metadados:

- `uploaded_by` = `={{ $json.numero_lead }}`
- `original_message_id` = `={{ $json.mensagem_id }}`

Saída depois do `Public cUrl`:

```markdown
{
  "publicUrl": "https://.../raw_uploads/123456.pdf",
  "uploaded_by": "5599...",
  "original_message_id": "3EB0..."
}
```

---

## 4\. Nó: Alfred (HTTP → Manus)

Esse é o “cérebro” de ingestão. Ele recebe a URL pública e delega toda magia pra Manus.

### Parameters

- **Method**: `POST`
- **URL**:
```markdown
https://api.manus.ai/v1/process
```

(ou o endpoint que você já usa para o Coringa/Alfred)

- **Send Headers**: ON
	- `Content-Type` = `application/json`
		- `Authorization` = `={{ 'Bearer ' + $env.MANUS_API_KEY }}`
- **Send Body**: ON
	- **Body Content Type**: `JSON`
		- **Specify Body → Using JSON**

JSON (copy/cola):

```markdown
{
  "task": "ingest_and_qualify_document",
  "context": {
    "document_url": "{{ $json.publicUrl }}",
    "source_channel": "whatsapp",
    "uploaded_by": "{{ $json.uploaded_by || $json.numero_lead }}",
    "original_message_id": "{{ $json.original_message_id || $json.mensagem_id }}"
  }
}
```

A resposta que você espera da Manus (pelo conceito que definimos):

```markdown
{
  "status": "success",
  "intent": "document_ingestion_and_qualification",
  "data": {
    "document_summary": "Resumo do contrato...",
    "storage_operations": [
      { "table": "kb_chunks", "action": "insert", "rows_affected": 25 },
      { "table": "customers", "action": "update", "rows_affected": 1 }
    ]
  },
  "suggested_reply": "Recebido e arquivado! Processei o contrato com a Acme Corp...",
  "logs": [...],
  "meta": {
    "notes": "Documento classificado como 'Contrato' e associado ao cliente XYZ."
  }
}
```

Quem garante que isso vai ser seguido é o **prompt interno do Alfred na Manus**, já falo dele abaixo.

---

## 5\. Nó: Map7 (normalizar resposta pro BRANN)

Depois do Alfred, você só precisa preparar a mensagem que vai seguir para o bloco `Text Final` → BUFFER → BRANN.

### Parameters

- Tipo: **Set**

Campos sugeridos:

1. `text` (o que o BRANN vai falar normalmente)  
	Expression:
	```markdown
	{{ $json.suggested_reply || $json.data?.document_summary || 'Documento recebido e processado com sucesso.' }}
	```
2. `document_summary`
	```markdown
	{{ $json.data?.document_summary }}
	```
3. `ingestion_meta`
	```markdown
	{{ $json.meta }}
	```
4. `ingestion_status`
	```markdown
	{{ $json.status }}
	```

Depois disso, conecta o `Map7` no `Text Final` do teu fluxo. O resto da pipeline (BUFFER, lista de mensagens, etc.) permanece igual.

---

## 6\. Contexto/prompt na Manus (lado Alfred/Coringa)

Aquele texto grande que você escreveu já é praticamente o **system prompt perfeito**. Você pode organizar assim dentro da Manus:

### System / Persona do Alfred

> Você é ALFRED, o ingestor e qualificador de documentos da Ginkgo. Seu trabalho é:
> 
> 1. baixar documentos de uma URL (`document_url`),
> 2. extrair texto (OCR/parsing),
> 3. analisar conteúdo (tipo, entidades, importância),
> 4. gerar embeddings e salvar no Supabase,
> 5. atualizar tabelas de negócio (customers, projects, etc.),
> 6. responder sempre em JSON estruturado.

### Tarefas que ele deve seguir quando task = ingest\_and\_qualify\_document:

1. Fazer download do documento em `context.document_url`.
2. Extrair texto e, se for grande, quebrar em chunks.
3. Classificar:
	- tipo: `contract`, `proposal`, `report`, `article`, etc.
		- entidades: cliente, empresa, datas, valores.
4. Gerar embeddings e inserir na tabela `kb_chunks` do Supabase.
5. Se identificar que é contrato de um cliente:
	- atualizar tabela `customers` com anotação / status.
6. Retornar SEMPRE neste formato:
```markdown
{
  "status": "success" | "error",
  "intent": "document_ingestion_and_qualification",
  "data": {
    "document_summary": "...",
    "storage_operations": [
      { "table": "kb_chunks", "action": "insert", "rows_affected": 0 },
      { "table": "customers", "action": "update", "rows_affected": 0 }
    ]
  },
  "suggested_reply": "Mensagem amigável para o usuário final.",
  "logs": [...],
  "meta": {
    "notes": "Notas técnicas para supervisão",
    "document_type": "contract | article | ...",
    "sensitivity": "public | confidential | financial"
  }
}
```

Assim, o n8n não precisa entender **como** ele falou com o Supabase; só precisa usar `suggested_reply` e, se quiser, logar `data` / `meta`.

---

## 7\. Checklist rápido

1. Download Document entrega binário `data` + `mensagem_id` + `numero_lead`.
2. Inserir Supabase (HTTP) → faz upload no bucket `raw_uploads`.
3. Public cUrl (Set) → cria `publicUrl` correto.
4. Alfred (HTTP) → manda `task: "ingest_and_qualify_document"` com `document_url: publicUrl`.
5. Manus/Alfred internamente: OCR + embeddings + Supabase + classificação.
6. Map7 → pega `suggested_reply` → joga no `text`.
7. Text Final → fluxo normal → BRANN responde e ainda ganha memória nova no “cérebro”.

Se quiser, no próximo passo te ajudo a definir **as tabelas Supabase do lado Manus** (`kb_chunks`, `customers`, `projects`) para essa ingestão ficar padrão Ginkgo.

este no

Vamos configurar **esse nó “Inserir Supabase”** exatamente como o uploader pro Storage.

Vou te passar o passo a passo direto na tela que você mostrou.

---

## 1\. Ajustar o nó anterior (Download Document)

Antes de tudo, garante isso no **Download Document**:

- `Response Format`: **File**
- `Binary Property`: **`data`**

Depois de testar o nó, ele precisa ter uma aba **Binary** com um item chamado `data`.  
É esse binário que vamos mandar pro Supabase.

---

## 2\. Configuração do nó “Inserir Supabase”

No nó que está na tela:

### a) Method

```markdown
POST
```

### b) URL

No campo **URL**, coloca:

```markdown
https://SEU_PROJETO.supabase.co/storage/v1/object/raw_uploads/{{ $json["Mensagem_ID"] }}.pdf
```

Troca `SEU_PROJETO` pelo subdomínio do teu Supabase (ex.: `abcdxyz.supabase.co`).

Repara no uso de colchetes:

```markdown
{{$json["Mensagem_ID"]}}
```

porque na esquerda o campo está com M maiúsculo e `_`.

---

### c) Send Headers

Liga **Send Headers** e adiciona estes 4 headers:

1. **Key:** `apikey`  
	**Value:**
	```markdown
	={{ $env.SUPABASE_API_KEY }}
	```
2. **Key:** `Authorization`  
	**Value:**
	```markdown
	=Bearer {{ $env.SUPABASE_API_KEY }}
	```
3. **Key:** `Content-Type`  
	**Value:**
	```markdown
	application/pdf
	```
4. **Key:** `x-upsert`  
	**Value:**
	```markdown
	true
	```

---

### d) Send Body

Liga **Send Body**.

- **Body Content Type:** `Binary File`
- **Binary Property:**
	```markdown
	data
	```

(tem que ser o mesmo nome que você usou no Download Document).

---

## 3\. Próximo nó: “Public cUrl”

Depois de salvar o “Inserir Supabase”, cria o nó **Public cUrl (Set)** logo depois dele e configura:

- Campo: `publicUrl`
- Valor (Expression):
```markdown
={{ 'https://SEU_PROJETO.supabase.co/storage/v1/object/public/raw_uploads/' + $json["Mensagem_ID"] + '.pdf' }}
```

Substitui `SEU_PROJETO` pelo mesmo de cima.

Esse `publicUrl` é o que você vai usar no Alfred:

```markdown
"document_url": "{{ $json.publicUrl }}"
```

Se fizer isso exatamente assim, você fecha o elo:

`Download Document → Inserir Supabase (upload binário) → Public cUrl (gera URL pública) → Alfred (Manus ingere e qualifica)`

2/2

Perfeito — **esse é exatamente o nó certo**.  
Agora vamos transformar ele no **uploader funcional** para o Supabase Storage.

Vou te guiar **exatamente na tela que você está**.

---

## ✅ 1. CORRIGIR A URL

Você escreveu:

```markdown
https://kaj5xrw...supabase.co/storage/v1/object/raw_uploads/{{ $json["Mensagem_ID"] }}.pdf
```

A estrutura está **correta**, mas **você esqueceu o “public/” somente quando for baixar**.  
Para upload, o caminho está **perfeito**:

### Use exatamente:

```markdown
https://kaj5xrwpkqbgagckqn.supabase.co/storage/v1/object/raw_uploads/{{ $json["Mensagem_ID"] }}.pdf
```

Nenhuma alteração aqui.  
**Correto.**

---

## ❗ 2. AGORA ATIVE A PARTE MAIS IMPORTANTE: HEADERS

No teu print, **Send Headers = OFF**.

Precisa ligar.

### Ligue: Send Headers = ON

Depois clique em **"Add Header"** e adicione estes 4:

---

### 🔹 Header 1 — apikey

```markdown
Key: apikey
Value: ={{ $env.SUPABASE_API_KEY }}
```

### 🔹 Header 2 — Authorization

```markdown
Key: Authorization
Value: =Bearer {{ $env.SUPABASE_API_KEY }}
```

### 🔹 Header 3 — Content-Type

```markdown
Key: Content-Type
Value: application/octet-stream
```

*(mais seguro que `application/pdf`, especialmente para.docx,.png, etc.)*

### 🔹 Header 4 — x-upsert

```markdown
Key: x-upsert
Value: true
```

---

## 🔥 3. ENVIAR O BINÁRIO DO ARQUIVO

Ative **Send Body = ON**

Depois:

### Body Content Type:

```markdown
Binary File
```

### Binary Property:

```markdown
data
```

⚠️ Isso precisa ser **exatamente o nome** do binário que aparece no nó *Download Document → Binary*  
No seu print ele é `data` — então está certo.

---

## ⭐ 4. Resultado esperado

Quando você clicar em **Execute**, você deve ver isso no OUTPUT:

```markdown
{
  "Key": "raw_uploads/123456.pdf"
}
```

Se isso aparecer → **UPLOAD FUNCIONANDO**  
Sem isso → todos os passos seguintes quebram.

---

## ⭐ 5. Próximo nó — “Public cUrl” (Set)

Logo depois desse nó “Inserir Supabase”, adiciona um nó **SET**:

### Campo:

```markdown
publicUrl = https://kaj5xrwpkqbgagckqn.supabase.co/storage/v1/object/public/raw_uploads/{{$json["Mensagem_ID"]}}.pdf
```

⚠️ Aqui sim entra o `/public/`

Porque esse caminho entrega o arquivo para a Manus baixar.

---

## ⭐ 6. Alfred (Manus)

Alfred agora recebe a URL assim:

```markdown
{
  "task": "ingest_and_qualify_document",
  "context": {
    "document_url": "{{ $json.publicUrl }}",
    "source_channel": "whatsapp",
    "uploaded_by": "{{ $json.numero_lead }}",
    "original_message_id": "{{ $json.Mensagem_ID }}"
  }
}
```

---

## ✔ Checklist final

| Etapa | OK? |
| --- | --- |
| Download Document tem binário `data` | ✔ |
| Inserir Supabase faz upload pelo HTTP | ⚠️ headers + body faltam |
| Public cUrl gera URL pública | 🔜 próximo passo |
| Alfred recebe URL pública real | 🔜 depois do cUrl |
| Manus processa OCR + embeddings + qualificação | 🔜 |
| Map7 normaliza resposta | 🔜 |

---

## 👉 Quer que eu confira AGORA se o nó está configurado exatamente certo?

Me manda um print **com Send Headers e Send Body abertos**, mostrando:

- os headers
- o body type
- o binary property

Eu ajusto na hora.