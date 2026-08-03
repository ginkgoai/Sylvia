---
title: "GKO - Erro no fluxo n8n"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/6918c4a4-50c8-8333-909c-2573dfc4bf6a"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sáb., 15 de nov. às 15:23

confere

bora

olha

confere

seletor?

Perfeito — agora ficou **claríssimo** o que está impedindo o login.

Você cadastrou **o redirect URI errado**.

A URL que está aí:

```markdown
https://ginkgo.app.n8n.cloud/rest/oauth2-credential/callback
```

👉 Essa é a **URL do n8n Cloud**, NÃO do seu Painel EasyPanel / VPS.  
Por isso o Google bloqueou.

Seu n8n está rodando em:

```markdown
https://studio.ginkgosystems.tech
```

Então seu redirect correto é:

```markdown
https://studio.ginkgosystems.tech/rest/oauth2-credential/callback
```

---

## ✅ COMO CORRIGIR (rápido)

1. Na seção **URIs de redirecionamento autorizados**
2. Apague:
```markdown
https://ginkgo.app.n8n.cloud/rest/oauth2-credential/callback
```
3. Clique em **\+ Adicionar URI**
4. Cole exatamente:
```markdown
https://studio.ginkgosystems.tech/rest/oauth2-credential/callback
```
5. Deixe também o de localhost (pode manter):
```markdown
http://localhost:5678/rest/oauth2-credential/callback
```
6. Clique **Salvar**

---

## ⚠️ IMPORTANTE

Depois de salvar:

➡️ Aguarde **30 segundos**  
➡️ Volte no n8n, abra a credencial Google Sheets  
➡️ Clique novamente em:

```markdown
Sign in with Google
```

Agora vai abrir normal, sem erro 400.

---

## Se quiser, posso validar clicando no botão certo ao vivo:

Manda um print do campo atualizado **após você salvar**.

posso salvar?

Sim — **pode salvar agora**.  
Está **100% correto**.

✔ Redirect URI certo  
✔ Client OAuth certo  
✔ Nada faltando  
✔ Nada sobrando

Depois de clicar em **Salvar**:

1. Volte no n8n → Credencial Google Sheets
2. Clique em **Sign in with Google**
3. Escolha sua conta
4. Permita tudo

Agora o login vai funcionar sem erro.

Assim que clicar, me manda o print da tela do n8n autenticando para validarmos o próximo passo.

2/2

Agora sim, **finalmente chegamos na etapa final da configuração do Sheets** – e o erro está claro:

## ❌ Erro: “At least one value has to be added under ‘Values to Send’”

Isso significa:

➡️ Você criou os nomes das colunas  
❌ Mas **não colocou nenhum valor dentro delas**  
➡️ Ou seja, o n8n vê as colunas, mas todas estão **vazias**, sem mapeamento

A solução é simplesmente preencher **cada campo com a expressão certa**.

Vou te entregar AGORA o mapeamento completo.  
É só copiar e colar.

---

## ✅ Preencha assim cada valor em “Values to Send”

### template\_id

```markdown
{{ $("Generate Unique Template ID").json.code }}
```

---

### video\_url

Use o link ORIGINAL do vídeo recebido no Telegram:

```markdown
{{ $("Trigger: Get TikTok URL via Telegram").item.json.message.text }}
```

(Se preferir o link final baixado, use outro, depois te mostro.)

---

### thumbnail\_url

```markdown
{{ $("Upload Thumbnail to Cloudinary").json.secure_url }}
```

---

### overlay\_text

```markdown
{{ $("Extract Overlay Text").json.text }}
```

---

### transcription

```markdown
{{ $("Transcribe Audio to Script (GPT)").json.text }}
```

---

### caption

```markdown
{{ $("Download TikTok Video (RapidAPI)").item.json.data.title }}
```

---

### created\_at

```markdown
{{ new Date().toISOString() }}
```

---

### status

```markdown
new
```

---

## 🧩 Como preencher no n8n

Em cada linha você abre o campo → clica em **Expression** → cola o código acima.

Seu print mostra **todos os campos criados, mas vazios**:

- template\_id: vazio
- video\_url: vazio
- thumbnail\_url: vazio
- overlay\_text: vazio
- transcription: vazio
- caption: vazio
- created\_at: vazio
- status: vazio

➡️ O n8n não deixa salvar porque você está tentando inserir uma linha **sem nenhum valor**.

---

## 🔥 PREVIEW DO RESULTADO FINAL NO SHEETS (quando rodar)

A linha que vai aparecer será algo assim:

| template\_id | video\_url | thumbnail\_url | overlay\_text | transcription | caption | created\_at | status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AYBC098... | https://tiktok... | https://res.cloudinary.com/... | “texto da thumb…” | “transcrição completa…” | “Título original do vídeo” | 2025-11-15T23:00:02Z | new |

---

## 🚀 Depois de colar tudo:

Clique **Execute Step**

E me manda o print do Sheets com a nova linha criada.

Se quiser, posso revisar **um a um** diretamente no seu print do n8n.