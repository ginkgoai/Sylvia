---
title: "GKO - Guia deploy ALFRED"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/692a6937-d720-832d-9e87-b615ac6c0f58"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sáb., 29 de nov. às 0:32

![5e48fd11-d552-474c-a223-bb90bd247c6b.png](https://chatgpt.com/backend-api/estuary/content?id=file_000000008a1c71f59b965dfb76f68d33&ts=495692&p=fs&cid=1&sig=8bd5d224a58b9eb0666bcd846bf91d08f8cc7151dfc0d00eb6212dac3497a1bc&v=0)

git

![285fa2bd-d2ff-432a-b559-8cd961949ff8.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000014871f585969ea116861912&ts=495692&p=fs&cid=1&sig=e702661f4354a95ea0410938ff9ab094418c5d92e6e159f70673573d4e22131e&v=0)

bem explicado pois me perco facile para colocar essa pasta, onde? e depois rodar oq, onde

![bf0089bf-2504-428a-88c5-240af8569244.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000d2a471f5bd27a7a39de41377&ts=495692&p=fs&cid=1&sig=5ab205eedd414290ccdd937b530240f122a8c35d5ea4073e3f0d02f20d366823&v=0)

aqui?

Sim, é **exatamente aí** que vamos trabalhar. Você já está dentro da VPS como `root`. Agora é só seguir a sequência:

---

## 1) Criar a pasta do projeto

No terminal (esse da imagem), rode:

```markdown
mkdir -p /root/projects
cd /root/projects
```

---

## 2) Enviar o ALFRED\_DEPLOY\_FINAL.zip para a VPS

Ainda nesse terminal da Hostinger:

1. No topo direito da janela do terminal tem um **ícone de upload** (normalmente uma setinha pra cima).
2. Clique nele e escolha o arquivo `ALFRED_DEPLOY_FINAL.zip` do seu computador.
3. Depois do upload, confira com:
```markdown
ls
```

Você deve ver algo como:

```markdown
ALFRED_DEPLOY_FINAL.zip
```

---

## 3) Descompactar o ALFRED

```markdown
apt update && apt install -y unzip   # só se unzip não estiver instalado
cd /root/projects
unzip ALFRED_DEPLOY_FINAL.zip -d alfred
cd alfred
ls
```

Agora você deve ver os arquivos da API (main.py, requirements.txt etc.).

---

## 4) Preparar para o GitHub

Dentro de `/root/projects/alfred`:

```markdown
git init
git add .
git commit -m "Deploy ALFRED - versão final"
git remote add origin https://github.com/ginkgosystems/alfred-api.git
git branch -M main
git push -u origin main
```

Se pedir usuário/senha:

- usuário: seu usuário do GitHub
- senha: um **Personal Access Token** (se usar 2FA).

---

Quando terminar esse push, abre o GitHub no repositório `ginkgosystems/alfred-api` e vê se os arquivos estão lá.

Assim que estiverem, eu te guio imediatamente para o **deploy no Railway** e depois para **trocar a URL no n8n**.

Perfeito, você está exatamente no lugar certo — só falta **achar o botão de upload**, e ele realmente fica meio escondido dependendo do navegador.

Vamos resolver isso *sem erro*.

---

## ✅ Onde fica o botão de upload no Terminal da Hostinger

No terminal web da Hostinger, o botão fica **na barra superior**, geralmente no canto direito, com um ícone de:

**📤 Uma setinha para cima (upload)**  
ou  
**📁 Um botão “Upload files”**

Mas dependendo do zoom da tela, ele some da barra.

---

## 🔍 SOLUÇÃO RÁPIDA: Mostrar o botão

Faça isso:

## 👉 1. Aumente ou reduza o zoom da página

Pressione:

```markdown
CTRL + 0
```

ou

```markdown
CTRL + -
```

Isso geralmente **faz o botão aparecer**.

---

## 👉 2. Expanda o terminal com o botão de tela cheia

Tem um botão de tela cheia no canto direito do terminal (ícone de retângulo).  
Clique nele — o botão de upload costuma aparecer só no modo expandido.

---

## 👉 3. Olhe na BARRA SUPERIOR do terminal web

Você verá algo assim:

```markdown
📁  Upload files     ⟳  Restart     ⛁  Reset     …
```

Clica em **Upload files**.

---

## 👉 4. Se mesmo assim NÃO aparecer: usamos SFTP (100% garantido)

Esse método sempre funciona.

### Instale WinSCP ou FileZilla

E conecte com:

- **Host:** 72.60.146.6
- **User:** root
- **Senha:** a mesma do painel Hostinger
- **Porta:** 22
- **Protocolo:** SFTP

Depois navegue até:

```markdown
/root/projects
```

E arraste o `ALFRED_DEPLOY_FINAL.zip` para lá.

---

## 🚀 Qual método você quer?

Escolha:

**A) Quero tentar achar o botão de upload (zoom / tela cheia)**  
**B) Vamos direto pelo SFTP (WinSCP/FileZilla)**

Me diga qual, e eu te guio milimetricamente.

![205b8b0d-27f6-4314-a8d9-d1a95ad89219.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000582471f5abe5afe9d16b5b2c&ts=495692&p=fs&cid=1&sig=4d5c83a2414aff2288be67df42e6627d85c82449c3a3ff4d8f92bfbb9b2a4179&v=0)

nao encontrie

Sem problema, vamos pela rota que sempre funciona: **SFTP (tipo “Explorer” plugado direto na VPS)**.  
Esquece o botão de upload do terminal.

Vou assumir que você está no Windows.

---

## 1) Conectar na VPS via WinSCP (ou FileZilla)

### 1.1. Baixar o cliente

Use um desses (qual preferir):

- **WinSCP**: recomendado → pesquisando “WinSCP download”
- ou **FileZilla Client**

Vou usar WinSCP no passo a passo, mas no FileZilla é praticamente igual.

---

### 1.2. Dados de conexão (os mesmos do painel da Hostinger)

No WinSCP:

- File protocol: **SFTP**
- Host name: **72.60.146.6**
- Port number: **22**
- User name: **root**
- Password: **senha root** que aparece no painel da VPS

Clique em **Login**.

Se aparecer alerta de chave/host, aceite.

---

## 2) Enviar o ALFRED\_DEPLOY\_FINAL.zip para /root/projects

Quando conectar, você verá duas janelas:

- Esquerda → seu PC
- Direita → servidor (VPS)

Na janela da direita:

1. Navegue até a pasta:
	- Clique em cima: `/`
		- Depois vá entrando: `root` → `projects`
		- Caminho final: `/root/projects`

Se a pasta não aparecer, é só criar:

- Botão direito → **New → Directory** → nome: `projects`
- Entre em `/root/projects`.

Na janela da esquerda:

2. Ache o arquivo `ALFRED_DEPLOY_FINAL.zip` no seu computador.
3. Arraste o ZIP da esquerda para a direita (para dentro de `/root/projects`).

Feito isso, o arquivo já estará no servidor.

---

## 3) Confirmar no terminal

Volte no **terminal da VPS** (aquele que você já abriu):

```markdown
cd /root/projects
ls
```

Você deve ver:

```markdown
ALFRED_DEPLOY_FINAL.zip
```

Se aparecer, perfeito.

---

## 4) Descompactar o ALFRED

Ainda no terminal:

```markdown
apt update && apt install -y unzip   # só precisa uma vez

cd /root/projects
unzip ALFRED_DEPLOY_FINAL.zip -d alfred
cd alfred
ls
```

Agora devem aparecer os arquivos da API (main.py, requirements.txt, etc.).

---

## 5) Inicializar Git e conectar no GitHub

Dentro de `/root/projects/alfred`:

```markdown
git init
git add .
git commit -m "Deploy ALFRED - versão final"

git remote add origin https://github.com/ginkgosystems/alfred-api.git
git branch -M main
git push -u origin main
```

Se o Git pedir:

- **Username**: seu usuário do GitHub
- **Password**: um **Personal Access Token** (se tiver 2FA).  
	Você gera em: GitHub → Settings → Developer settings → Personal access tokens → Fine-grained.

Depois do `git push` dar certo, abra:

`https://github.com/ginkgosystems/alfred-api`

e confira se os arquivos apareceram.

---

## 6) Próximo passo (quando isso estiver ok)

Assim que os arquivos estiverem no GitHub, o fluxo será:

1. Railway → conectar o repo `ginkgosystems/alfred-api`
2. Configurar as variáveis:
	```markdown
	ALFRED_API_KEY=alfred-ginkgo-secret-2025
	PORT=8000
	```
3. Pegar a URL final (ex.: `https://algo.up.railway.app`)
4. Colar essa URL no n8n (ALFRED\_API\_URL).

Faz primeiro até o **git push** funcionar.  
Depois disso, me diz: “arquivos já estão no GitHub”, e eu já te passo o passo a passo do Railway.