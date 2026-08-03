---
title: "Lab - Repositorios e ferramentas necessárias"
source: "https://chatgpt.com/g/g-p-6920bddfbb548191ac06d937cdb0b5c0/c/6920c280-76cc-8326-b673-0491f5c4c7da"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
![775c2270-032d-4795-a5b9-9347c2974ea4.png](https://chatgpt.com/backend-api/estuary/content?id=file_000000009488720e8bb5d99f113f30d3&ts=495691&p=fs&cid=1&sig=faa17acacd381ec0a41c8322e43eb8372c4502d7c830faebaea90cf56653f4ec&v=0) ![ade3a381-948d-4a2d-bb94-6e2a454809ae.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000386071f5898efa7602c4470d&ts=495691&p=fs&cid=1&sig=26fbfae97b57109ae5643b4f0543d118bcd44866801d9f168059915499a9a4dc&v=0)

foi

![b04f0bdb-a4f8-4150-8379-b450176c4fe6.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000e59c720ea355aa79b08416b1&ts=495691&p=fs&cid=1&sig=7ce2308d918208c65b86bfe7d0e42bc493c7c9a5a8d0095dc3b1c659b70d2fb1&v=0) ![6c24dc69-2bc8-441b-8bfd-b429e4d84e89.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000c0c471f5a848a80863e3db78&ts=495691&p=fs&cid=1&sig=22d5194b891abcd575d9a6839d6755773ce8210e1813eca7ef7268e2c0ceb086&v=0) ![20c0db90-0ea9-4a7f-8fc6-d8939f6505c1.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000bd3471f5a7a13a4d7c748e1d&ts=495691&p=fs&cid=1&sig=2b5883101a9649b8b9b686fb8edb1f37eac6cf823180bad9e970c1dc55428a7a&v=0) ![0f897db8-6eae-4b61-8569-5cd235d74b60.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000a36c71f59797a35eeb7538d7&ts=495691&p=fs&cid=1&sig=9c991ed5d4d2adef0e85164e74b43e468ef0e7d5214ef5d2ef0681d727d334ca&v=0)

esse app?

![7fe1c8ac-18b6-42ac-8adc-7fb1ef83b721.png](https://chatgpt.com/backend-api/estuary/content?id=file_000000006f3071f58104f24a4a2d954b&ts=495691&p=fs&cid=1&sig=6751145714b79e78adec07e8984525fc9c5aa4063305322d5d50646dab429f5a&v=0) ![d635d06f-b9d2-43ab-ad46-b093912b9679.png](https://chatgpt.com/backend-api/estuary/content?id=file_000000007030720ea44bd43335e3fb5f&ts=495691&p=fs&cid=1&sig=088af25085d97ad859ef3dc98b533101654738cd656ddd6f4d133476bb493b48&v=0)

sex., 21 de nov. às 19:00

![19a22363-dd80-4073-9e7b-3aa06d065fe5.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000083871f59c7f228e18c24259&ts=495691&p=fs&cid=1&sig=532caa219ade662037f3981dd55e2cff1048c6b135c4bfda853a80065874afe8&v=0)

Perfeito.  
**Agora SIM o Git está ativo e funcionando no seu sistema.**  
Podemos finalmente conectar o VS Code aos repositórios da Ginkgo e começar a construir.

Vamos direto ao próximo passo.

---

## ✔️ PASSO 1 — Criar pasta mãe “ginkgo” e entrar nela

No terminal do VS Code:

```markdown
cd C:\Users\User
mkdir ginkgo
cd ginkgo
```

Se já existir, só entre:

```markdown
cd C:\Users\User\ginkgo
```

---

## ✔️ PASSO 2 — Clonar o repositório Ginkgo-Leaf

```markdown
git clone https://github.com/ginkgosystems/ginkgo-leaf.git
```

Se ao clonar aparecer uma janela pedindo login GitHub → aceite e faça login.  
Quando terminar, você verá:

```markdown
Cloning into 'ginkgo-leaf'...
done.
```

---

## ✔️ PASSO 3 — Abrir o projeto dentro do VS Code

Menu:

**Arquivo → Abrir Pasta → C:\\Users\\User\\ginkgo\\ginkgo-leaf**

Agora a esquerda (Explorer) vai mostrar:

```markdown
ginkgo-leaf
  LICENSE
  README.md
  .gitignore
```

---

## ✔️ PASSO 4 — Me mande um print da tela nesse momento

Preciso ver:

- o VS Code aberto com a pasta **ginkgo-leaf** expandida à esquerda
- o terminal aberto embaixo
- assim eu te passo os comandos corretos (versão PowerShell compatível com Windows) para criar TODA a estrutura de diretórios:
```markdown
src/
docs/
tests/
infra/
public/
...
```

E também o commit inicial.

---

### 🚀 Você destravou o ambiente. Agora a Ginkgo começa a tomar forma real.

Manda o print do ginkgo-leaf aberto para continuarmos.

1/2

![3c2f5fb7-fdda-41d1-a692-bbdc86f68887.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000e41471f59bfcf7e16d3c395a&ts=495691&p=fs&cid=1&sig=b5dc61acfc999bd0c9197528746ab6ab8484ba67c50ac5208714bf84107856f5&v=0)

Perfeito — **Git instalado e funcionando**, agora vamos realmente colocar a Ginkgo dentro do VS Code.

O que falta agora é **clonar o repositório e abrir a pasta correta**.  
Você ainda não entrou na pasta da Ginkgo e nem clonou nada — por isso o Explorer (lado esquerdo) está vazio.

Vamos resolver isso em 3 comandos.

---

## ✅ PASSO 1 — Ir para a pasta onde você vai guardar os projetos

No terminal:

```markdown
cd C:\Users\User
mkdir ginkgo
cd ginkgo
```

Se já existir a pasta, apenas:

```markdown
cd C:\Users\User\ginkgo
```

---

## ✅ PASSO 2 — Clonar o ginkgo-leaf

Agora:

```markdown
git clone https://github.com/ginkgosystems/ginkgo-leaf.git
```

Se pedir login/autorizar → aceite.

Você deve ver algo como:

```markdown
Cloning into 'ginkgo-leaf'...
Receiving objects...
Resolving deltas...
Done.
```

---

## ✅ PASSO 3 — Abrir a pasta no VS Code

Menu superior:

**Arquivo → Abrir Pasta…**

Escolha:

```markdown
C:\Users\User\ginkgo\ginkgo-leaf
```

Quando abrir, o lado esquerdo (Explorer) deve mostrar:

```markdown
LICENSE
README.md
.gitignore
```

E o terminal agora deve estar assim:

```markdown
PS C:\Users\User\ginkgo\ginkgo-leaf>
```

---

## ❗ Envie o próximo print com:

- A pasta **ginkgo-leaf** aparecendo no Explorer (lado esquerdo)
- O terminal mostrando que você está dentro dela

Assim seguimos para:

- Criar toda a estrutura de pastas com comandos PowerShell
- Commit inicial
- Repetir para Wave, Pyre, Infra

A Ginkgo finalmente vai estar **estruturada como empresa**.

2/2

![45962c28-778c-4567-b44b-608500a787e0.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000520471f5bc4d32247aa8e61b&ts=495691&p=fs&cid=1&sig=39e86686494a8737f325873451add954c86d5303c815cb2d6ab2cf1e28a9ed48&v=0)

passo 1

Perfeito, o passo 1 está certinho:  
no rodapé já aparece `PS C:\Users\User\ginkgo>` → você está dentro da pasta certa.

Agora vem o passo 2.

---

## PASSO 2 — Clonar o repositório ginkgo-leaf

No mesmo terminal, rode:

```markdown
git clone https://github.com/ginkgosystems/ginkgo-leaf.git
```

Quando terminar, você pode conferir com:

```markdown
dir
```

Deve aparecer uma pasta `ginkgo-leaf`.

---

## PASSO 3 — Abrir essa pasta no VS Code

1. Menu superior: **Arquivo → Abrir Pasta…**
2. Navegue até:  
	`C:\Users\User\ginkgo\ginkgo-leaf`
3. Selecione essa pasta e confirme.

O lado esquerdo (Explorer) deve mostrar algo como:

- `.gitignore`
- `LICENSE`
- `README.md`

E o terminal vai ficar assim:

```markdown
PS C:\Users\User\ginkgo\ginkgo-leaf>
```

---

Faça o `git clone`, abra a pasta `ginkgo-leaf` e me manda o próximo print com ela aparecendo no Explorer. Aí eu te dou os comandos PowerShell para criar TODA a estrutura do Leaf (src, docs, infra, etc.) em um tiro só.

2/2