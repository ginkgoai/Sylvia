---
title: "GKO - Instalar Chatwoot funcional"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/6918d867-08d0-832d-bd46-def2197e8c2d"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sáb., 15 de nov. às 16:45

não achei

nao deu

Agora ficou 100% claro.

O problema aqui não é mais DNS, nem porta — é **configuração incorreta no Domínio dentro do EasyPanel**.

Vamos corrigir **exatamente**, sem margem de erro.

---

## 🚨 PROBLEMA 1 — Domínio está escrito errado

Você colocou:

```markdown
https://https://chat.ginkgosystems.tech/
```

Perceba o erro:

- Tem **https://https://**
- E o EasyPanel não aceita URL completa — apenas o **domínio puro**, sem protocolo, sem barra.

---

## 🚨 PROBLEMA 2 — O destino está incorreto

Você colocou:

```markdown
http://chatwoot_chatwoot:3000/
```

Isso é **nome interno entre containers**, não endereço local da VPS.

Para Proxy funcionar, deve ser:

```markdown
http://localhost:3000
```

ou

```markdown
http://127.0.0.1:3000
```

---

## 🔥 AGORA VAMOS ARRUMAR CERTO

## 1\. Clique no botão Editar (ícone de lápis)

Na linha do domínio atual.

### Apague e substitua por:

📌 **Domínio:**

```markdown
chat.ginkgosystems.tech
```

📌 **Destino (Forward to):**

```markdown
http://127.0.0.1:3000
```

📌 **Path:**

```markdown
/
```

📌 **HTTPS:**  
deixe **desativado por enquanto**

Salve.

---

## ✅ 2. Função correta do Proxy (explicação rápida)

Fica assim internamente:

```markdown
cloudflare/dns → 72.60.146.63 (sua VPS)
VPS porta 80 → Proxy do EasyPanel
Proxy do EasyPanel → localhost:3000 (Chatwoot)
```

---

## 🚀 3. Clique em Implantar (reiniciar o serviço chatwoot)

Muito importante reiniciar.

---

## 🌐 4. Teste no navegador:

```markdown
http://chat.ginkgosystems.tech
```

---

## ⚠️ Depois disso, mande:

1. Print atualizado da aba **Domínios**
2. Resultado ao acessar o domínio

Se ainda não abrir, eu verifico o firewall da Hostinger com você em menos de 1 minuto.

Vamo destravar isso.

Aí sim, **MEU PARCEIRO!**  
O **Chatwoot está oficialmente ONLINE**, bonito, limpo, rodando pelo domínio e pronto pra integrar no ecossistema da Ginkgo.  
Você liberou o núcleo de atendimento do império.

Agora vamos selar a ativação.

---

## ✅ 1. Preencha o setup inicial

Use exatamente assim para manter padrão Ginkgo:

**Name:**  
Ginkgo Admin

**Company Name:**  
Ginkgo AI Systems

**Work Email:**  
admin@ginkgosystems.tech  
(se quiser outro, pode)

**Password:**  
Crie forte (vai ser o painel principal da central de atendimento)

Desmarque a caixinha de newsletter se quiser.

Clique em **Finish Setup**.

---

## 🔥 2. Depois que criar, vamos seguir para os ajustes obrigatórios

Quando entrar no dashboard, me avise e já vamos:

### ✔ Configurar URL do app

### ✔ Ativar HTTPS (certificado Let’s Encrypt)

### ✔ Criar o primeiro Inbox

### ✔ Conectar WhatsApp via Evolution API

### ✔ Criar o usuário Brann interno

### ✔ Criar o roteador da Ginkgo

### ✔ Integrar Nyra e Alphie (automação webhook dentro do Chatwoot)

**Esse é o coração da operação LEAF.**

---

## 🚀 3. Me avise quando clicar “Finish Setup”

E já mande print do dashboard inicial.

Vamos deixar isso afiado e funcional no nível Ginkgo.

Perfeito.  
O **Chatwoot está ativo, funcional e ligado ao domínio com sucesso**.  
Agora começa a segunda fase: transformar isso na **central oficial de atendimento do ecossistema Ginkgo**, preparada para receber:

- Brann (atendente humanizado)
- Nyra (social/mídia e captação de leads)
- Alphie (gestor/operador/IA de backoffice)

Vamos montar o stack de produção do jeito certo.

---

## 🔥 1. Ajustar Configurações Globais (obrigatório)

No menu esquerdo:

### Configurações → Configurações da Conta (Account Settings)

Configure:

### → Nome da Conta

`Ginkgo AI Systems`

### → URL do Aplicativo

Coloque exatamente:

```markdown
https://chat.ginkgosystems.tech
```

### → Fuso Horário

`America/Sao_Paulo`

### → Idioma

`Português (Brasil)`

Salvar.

---

## 🔐 2. Habilitar HTTPS (Let’s Encrypt)

Agora que o domínio está funcionando, vamos ativar SSL para o painel ficar 100% seguro.

No **EasyPanel → chatwoot → Domínios**:

1. Clique no ícone de “cadeado” (ou opção **HTTPS/SSL**).
2. Ativar **Let’s Encrypt**.
3. Salvar + Reiniciar.

Depois acessar:

```markdown
https://chat.ginkgosystems.tech
```

---

## 📥 3. Criar o Inbox oficial do WhatsApp (Evolution API)

Menu esquerdo:

### Caixa de Entrada → Criar Nova Caixa de Entrada

Selecionar:

### Tipo: API Channel

(Não use WhatsApp Cloud — vamos usar Evolution API que você já tem.)

Nome do Inbox:

```markdown
Brann — Atendente Ginkgo
```

Salvar.

O Chatwoot vai gerar:

- `Inbox Identifier`
- `Callback URL`
- `Webhook URL`

**Deixe essa tela aberta**, porque vamos conectar com Evolution.

---

## 🔌 4. Conectar Evolution API ao Chatwoot

No dashboard da Evolution API:

1. Vá na sua instância (o número que já roda o bot).
2. Abra **Configurações da Instância → Webhooks**.
3. Cole o `Webhook URL` do Chatwoot.
4. Salve.

Agora todo WhatsApp que entrar → cai no Chatwoot.

---

## 🤖 5. Criar o usuário “Brann” dentro do Chatwoot

Menu esquerdo:

### Configurações → Equipe → Adicionar Usuário

Criar:

**Nome:** Brann, o Corvo  
**Email:** brann@ginkgosystems.tech  
**Permissão:** Agent

Esse é o usuário que o n8n vai usar para mensagens automáticas.

---

## 🔄 6. Criar Webhook para automações do n8n

Ainda em:

### Configurações → Webhooks → Criar Webhook

Configurar:

- **URL:** seu endpoint do n8n (ex: `https://n8n.ginkgosystems.tech/webhook/chatwoot`)
- **Eventos:**
	- message\_created
		- message\_updated
		- conversation\_created

Salvar.

Esse webhook alimenta:

- Brann conversando
- Nyra captando leads
- Alphie controlando fluxo interno

---

## 🧩 7. Criar o primeiro fluxo do Brann (essencial)

Agora no n8n:

Fluxo inicial:

```markdown
Webhook (Chatwoot) 
↓
Router (verifica se é áudio, imagem, PDF, texto)
↓
Nós específicos (recognition, transcrição, RAG, persona Brann)
↓
Node Evolution API ou Chatwoot Reply (dependendo do canal)
```

Se quiser, gero esse fluxo completo **pronto para importar**.

---

## 🎨 8. Personalizar o tema do Chatwoot com a identidade Ginkgo

Menu:

### Configurações → Preferências → Branding

Coloque:

- Nome: **Ginkgo AI Systems**
- Cores do tema:  
	Azul (#1a73e8), Branco (#ffffff), Dourado (#ffd700)
- Logo: Ginkgo Leaf

---

## 🚀 9. Confirmar: você quer agora que eu:

### A) Gere o fluxo n8n do Brann (pronto pra importar)?

### B) Configure autossoquete/painel de WhatsApp totalmente automatizado?

### C) Crie o Inbox da Nyra (Instagram, Facebook, WhatsApp secundário)?

### D) Monte o módulo Alphie dentro do Chatwoot para controle interno?

### E) Tudo junto como um “LEAF Setup V1”?

Me diga o que você quer montar primeiro.