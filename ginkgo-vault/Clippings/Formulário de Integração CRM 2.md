---
title: "Formulário de Integração CRM"
source: "https://chatgpt.com/c/6a5befc4-603c-83e9-8b8c-04c2365d9cb7"
author:
published:
created: 2026-07-19
description: "ChatGPT conversation with 7 messages"
tags:
  - "clippings"
---
**Você disse**

este é meu cliente, preciso que voce crie um formulario de integração, todas informações que vou precisar dele, para configurar CRM=Chatwoot e Leaf=Callima

---

**Você disse**

eu botei teu prompt no typeform, como mando para o cliente agora

---

Ficou bom. Agora eu faria um pequeno refinamento antes de enviar. A ideia é que o cliente sinta que está entrando em uma plataforma premium da Ginkgo, não apenas respondendo a um formulário.

### 1\. Adicione uma tela de boas-vindas

**Título**

**Texto**

> Este formulário reúne todas as informações necessárias para configurarmos sua Inteligência Artificial, CRM, automações e integrações. O preenchimento leva aproximadamente **15 a 20 minutos**. Quanto mais completas forem as respostas, mais precisa será a implantação.

Botão:

> Iniciar implantação

---

### 2\. Organize em seções

Em vez de dezenas de perguntas seguidas, utilize páginas com títulos:

- 🏢 Empresa
- 👤 Responsável
- 💼 Produtos e Serviços
- 📞 Atendimento
- 🤖 Inteligência Artificial
- 📚 Base de Conhecimento
- 🔗 Integrações
- 🎯 Objetivos
- 📂 Upload de Arquivos
- ✅ Finalização

O Typeform fica muito mais agradável dessa forma.

---

### 3\. Adicione uploads

Permita que o cliente envie:

- Logo
- Catálogo
- Tabela de preços
- Contratos
- PDFs
- Manual da empresa
- Apresentação institucional

Isso economiza horas de coleta depois.

---

### 4\. Tela final

**Título**

> Recebemos suas informações!

**Texto**

> Nossa equipe iniciará a configuração do ambiente.
> 
> Próximas etapas:
> 
> - Análise das informações
> - Configuração do CRM (Chatwoot)
> - Configuração da IA (Leaf / Callima)
> - Treinamento da base de conhecimento
> - Testes finais
> 
> Você receberá atualizações durante todo o processo.

---

## Como enviar ao cliente

No Typeform:

1. Clique em **Share** (canto superior direito).
2. Publique o formulário.
3. Copie o link público.
4. Envie por WhatsApp ou e-mail.

Exemplo de mensagem:

> Olá, **\[Nome\]**!
> 
> Para iniciarmos a implantação da sua IA e do CRM, precisamos que você preencha o formulário abaixo. Ele reúne todas as informações necessárias para configurar seu ambiente de forma personalizada.
> 
> **Tempo estimado:** 15 a 20 minutos.
> 
> **Link:** https://seu-formulario.typeform.com/to/XXXXXX
> 
> Caso tenha dúvidas durante o preenchimento, estamos à disposição.

---

## Evolução recomendada para a Ginkgo

Este Typeform deve ser uma solução temporária. Conforme o **Leaf** evoluir, substitua-o por um portal próprio, por exemplo:

```
portal.ginkgosystems.tech

↓

Login

↓

Onboarding

↓

Upload de documentos

↓

Status da implantação

↓

Checklist

↓

Treinamento

↓

Suporte
```

Assim, o onboarding deixa de ser apenas um formulário e passa a ser a primeira experiência do cliente com a plataforma da Ginkgo, reforçando a percepção de valor e centralizando todo o processo de implantação.

---

**Você disse**

formulario criado mas como passo para o cliente acessar???

---

Você está na tela do **Workspace**, não na tela do formulário. Faça o seguinte:

### Método 1 (mais simples)

1. Clique em **FORMULÁRIO DE IMPLANTAÇÃO — GINKGO AI SYSTEMS**.
2. Aguarde abrir o editor.
3. No canto superior direito clique em **Share**.
4. Clique em **Publish** (se ainda não estiver publicado).
5. Escolha **Get link** ou **Copy link**.
6. Copie o link e envie ao cliente.

O link ficará parecido com:

```
https://form.typeform.com/to/AbCdEfGh
```

Esse é o link público.

---

### Método 2

Dentro do editor do formulário:

**Share → Link → Copy**

---

## Se o botão "Share" não aparecer

Normalmente é porque o formulário ainda está em modo de edição. Abra o formulário e procure por:

Após publicar, o link será gerado automaticamente.

---

## Recomendo também

Crie um QR Code para o formulário e coloque esse link dentro do seu onboarding.

Exemplo:

```
Olá, Ricardo!

Para iniciarmos a implantação da sua IA Ginkgo, preencha o formulário abaixo.

Tempo médio: 15 minutos.

🔗 https://form.typeform.com/to/XXXXXXXX

Após o envio iniciaremos a configuração do Chatwoot, Leaf, CRM e das automações.
```

### Se não encontrar o botão

Abra o formulário e envie um print da tela do editor (onde aparecem as perguntas). A partir dessa tela consigo indicar exatamente onde clicar, pois a interface do Typeform muda um pouco entre versões.

---

**Você disse**

deveria ficar assim essa tela?

---

Não. Na verdade, essa tela indica que houve um problema na configuração da primeira página.

O texto:

> `" 🏢 Empresa`

mostra que provavelmente o título da pergunta ou da seção foi interpretado incorretamente.

### O que deveria aparecer

Se for uma **Statement/Welcome Screen**, deveria ficar algo como:

---

## Bem-vindo à Ginkgo AI Systems

Este formulário reúne as informações necessárias para configurarmos seu CRM, IA (Leaf/Callima), Chatwoot e automações.

⏱ Tempo estimado: **15 a 20 minutos**

Clique em **Começar** para iniciar.

**\[ Começar \]**

---

### Depois disso

A primeira pergunta seria:

**Dados da Empresa**

Qual é a razão social da empresa?

---

## O que eu acredito que aconteceu

Você colocou:

```
🏢 Empresa
```

como uma pergunta do tipo **Text**, e não como uma **Section** ou **Statement**.

Por isso o Typeform mostra apenas aquele texto solto.

---

## Eu faria assim

```
Página 1
──────────────

Bem-vindo à Ginkgo AI Systems

↓

Página 2
──────────────

🏢 Empresa

↓

Razão Social

↓

Nome Fantasia

↓

CNPJ

↓

...
```

---

## Outra observação importante

Vejo no canto inferior direito:

> **Powered by Typeform**

Isso significa que o formulário já está **público**.

Ou seja, você já pode enviar esse link para alguém.

O problema não é o compartilhamento, e sim a experiência inicial.

---

## Posso ir além

Pela arquitetura que você vem construindo para a Ginkgo, eu montaria esse onboarding no padrão de empresas como Stripe, Notion e Linear, com:

- fundo preto;
- detalhes em dourado e verde Ginkgo;
- barra de progresso;
- perguntas condicionais (o cliente só vê o que faz sentido);
- upload inteligente de documentos;
- animações discretas;
- copy institucional.

O resultado fica com aparência de um software SaaS premium, e não de um formulário genérico. Isso reforça imediatamente a percepção de valor da Ginkgo antes mesmo da implantação.