---
title: "GKO - Erro de conexão n8n"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/69294060-c588-832f-938d-c887f832a45a"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sex., 28 de nov. às 3:25

1/2

Qual resposta você prefere? Elas podem demorar um pouco para carregar.

Resposta 1

Esse erro do n8n:

> “The connection cannot be established, this usually occurs due to an incorrect host (domain) value”

não é de policy, body ou cabeçalho.  
É erro de **conexão**: o n8n não está conseguindo chegar no host que você passou (ou no host salvo na credencial Supabase).

Vou te guiar em 3 checks rápidos e depois deixar o modelo de node já “correto” para o upload.

---

## 1\. Conferir a credencial “Supabase 2”

1. No n8n, vá em **Credenciais → Supabase → Supabase 2**.
2. O campo **Host** tem que ser **exatamente** o “Project URL” do Supabase:
	```markdown
	https://xajsxfaxhpghegxcgkgn.supabase.co
	```
	(sem `/rest/v1`, sem `/storage/v1`, sem caminho extra, sem espaço na frente).
3. Em **Service Role Secret**, use a chave `service_role` do projeto (Settings → API → Project API Keys).

Se o Host tiver qualquer coisa a mais, tipo `/storage/v1/object/...`, arruma para ficar só o domínio.

---

## 2\. Testar se o n8n consegue falar com o Supabase

Cria um **HTTP Request** simples só para teste:

- **Method:** `GET`
- **URL:** `https://xajsxfaxhpghegxcgkgn.supabase.co/rest/v1/`
- **Authentication:** `Predefined Credential Type`
	- **Credential Type:** `Supabase API`
		- **Credential for Supabase API:** `Supabase 2`

Resultado:

- Se der **o mesmo erro de host**, é 100% algo com:
	- Host errado na credencial, ou
		- DNS/saída de rede do servidor onde o n8n está rodando.
- Se esse GET funcionar, então a conexão está ok e podemos focar na URL/corpo do upload.

---

## 3\. Ajustar o node de upload para o bucket raw\_uploads

Partindo do seu print, o formato de URL está quase certo, só vamos deixar o modelo “limpo”:

### URL

Na aba **Parameters** do HTTP Request:

```markdown
https://xajsxfaxhpghegxcgkgn.supabase.co/storage/v1/object/raw_uploads/{{ $json["File Name"] }}
```

Dicas:

- Garante que não tem espaço antes do `https://`.
- Se o nome do arquivo vier com espaços, o mais seguro é:
	```markdown
	https://xajsxfaxhpghegxcgkgn.supabase.co/storage/v1/object/raw_uploads/{{ encodeURI($json["File Name"]) }}
	```

### Authentication

- **Authentication:** `Predefined Credential Type`
- **Credential Type:** `Supabase API`
- **Supabase API:** `Supabase 2` (a credencial corrigida do passo 1)

### Headers

Liga **Send Headers** e usa:

1. Header `Content-Type`:
	- Name: `Content-Type`
		- Value: `{{ $json["Mime Type"] }}`  
		(ou fixa `application/json` / `application/pdf` /etc., se quiser testar)
2. (Opcional, mas útil) `x-upsert` para permitir sobrescrever arquivo:
	- Name: `x-upsert`
		- Value: `true`

### Body

- **Send Body:** ligado
- **Body Content Type:** `n8n Binary File`
- **Input Data Field Name:** `data`  
	(tem que bater com o nome da propriedade binária que vem do node **Download Document** – no teu print, é `data` mesmo)

---

## 4\. Se ainda assim continuar com o mesmo erro de host

Se, mesmo com tudo acima correto, o erro continuar igual:

- Muito provável que o servidor do n8n esteja sem saída para a internet ou com DNS bloqueando `*.supabase.co`.
- Nesse caso:
	- Testa um HTTP Request para `https://google.com` ou `https://api.ipify.org?format=json`.
		- Se der o mesmo erro, é infra/rede (Docker, firewall, VPS, etc.), não é o fluxo.

---

Resumo prático:

1. Corrige o **Host** da credencial Supabase 2 para só o domínio do projeto.
2. Testa um GET simples em `rest/v1`.
3. Com isso ok, usa a URL:
	```markdown
	https://xajsxfaxhpghegxcgkgn.supabase.co/storage/v1/object/raw_uploads/{{ encodeURI($json["File Name"]) }}
	```
	com body `n8n Binary File (data)` + `Content-Type`.

Se quiser, no próximo print me manda também a tela da **credencial Supabase 2** e do pequeno HTTP de teste, que eu vou pontuando exatamente onde mexer.

Resposta 2

Esse erro não é do arquivo nem do header.  
A mensagem “The connection cannot be established, this usually occurs due to an incorrect host (domain) value” significa que o n8n nem consegue chegar no domínio que você colocou na URL.

Vamos atacar em duas frentes: corrigir a URL/credencial e te dar o modelo 100% certo de upload pro Storage.

---

## 1\. Conferir o domínio do Supabase

1. No painel do Supabase, vá em:  
	**Settings → Configuration → API**
2. Copie exatamente o campo **Project URL**.  
	Ele deve ser algo como:  
	`https://xajsxfaxhpgbagxgckgn.supabase.co`
3. No node **Inserir Supabase**, substitua o começo da URL pelo que você copiou, ficando assim:
```markdown
https://xajsxfaxhpgbagxgckgn.supabase.co/storage/v1/object/raw_uploads/{{ $json["File Name"] }}
```

Pontos críticos aqui:

- Sem espaço antes ou depois da URL.
- Sem outro protocolo (tipo `http://`).
- Domínio **exatamente** igual ao do Supabase (um caractere errado já dá esse erro de host).

Se o domínio estiver 100% certo e ainda assim der esse erro, quase sempre é:

- n8n rodando em ambiente com bloqueio de saída (firewall/proxy).
- Variável `N8N_ALLOWED_OUTBOUND_HOSTS` configurada sem incluir `xajsxfaxhpgbagxgckgn.supabase.co`.

Se você estiver usando essa variável, garanta que tenha algo assim no ambiente do n8n:

```markdown
N8N_ALLOWED_OUTBOUND_HOSTS=evolution-api.meudominio.com,manus.ai,xajsxfaxhpgbagxgckgn.supabase.co
```

E reinicie o serviço.

---

## 2\. Modelo de node HTTP Request para upload no Storage

Vou te passar a config “limpa” que funciona, pra você comparar com a sua:

**Node:** HTTP Request  
**Method:** `POST`  
**URL:**

```markdown
https://xajsxfaxhpgbagxgckgn.supabase.co/storage/v1/object/raw_uploads/{{ $json["File Name"] }}
```

(onde `raw_uploads` é o nome do bucket)

### Autenticação

Para eliminar qualquer ruído de credencial, você pode:

- Em **Authentication**: selecionar `None`
- E setar os headers manualmente:

Headers:

1. `apikey` → chave anon ou service-role do Supabase
2. `Authorization` → `Bearer SEU_TOKEN_AQUI`
3. `Content-Type` →
	```markdown
	{{ $json["Mime Type"] || 'application/octet-stream' }}
	```

### Body

- **Send Body:** ligado
- **Body Content Type:** `Binary File`
- **Input Data Field Name:** `data`  
	(é o nome do campo binário vindo do node “Download Document” – na sua tela está “data”, então ok)

---

## 3\. Checklist rápido pra você debugar em 1–2 minutos

1. Substituir a URL inteira pelo **Project URL + /storage/v1...** copiado do Supabase.
2. Rodar o node de novo:
	- Se o erro mudar para 401/403/404 → domínio ok, só ajustar auth/caminho.
		- Se continuar “cannot be established / incorrect host (domain)” → é rede/bloqueio/DNS.
3. Se tiver `N8N_ALLOWED_OUTBOUND_HOSTS` configurada, adicionar o domínio do Supabase e reiniciar o n8n.

---

Se quiser, no próximo passo posso te mandar a versão usando diretamente o node **Supabase** do n8n (recurso Storage → Upload), que evita ter que cuidar manualmente da URL e deixa o fluxo mais “à prova de bala”.