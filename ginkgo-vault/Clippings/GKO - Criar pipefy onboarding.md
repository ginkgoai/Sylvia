---
title: "GKO - Criar pipefy onboarding"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/68e889f8-c94c-8331-b443-6ca128f20b49"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sex., 10 de out. às 1:22

Perfeito — você está na tela de criação de **templates com agentes de IA** dentro do **Pipefy**, que é justamente o ponto ideal pra montar o **fluxo de onboarding da Ginkgo (via Alphie)**. Vamos estruturar passo a passo o **pipe** ideal para o seu caso.

---

### 🎯 Objetivo do Pipe

Gerenciar **o onboarding automático de novos clientes**, desde o pagamento até a entrega do setup inicial (Brann, Nyra e Alphie configurados).

---

### 🧩 Estrutura do Pipe (etapas sugeridas)

1. **Entrada de Cliente (Trigger)**
	- Origem: integração com Stripe ou formulário do site.
		- Campos:
		- Nome do cliente
				- E-mail
				- WhatsApp
				- Plano escolhido (Básico / Futurista / Imagine)
				- ID da compra (Stripe)
				- Data da assinatura
2. **Coleta de Informações (Formulário Onboarding)**
	- Alphie envia link/formulário com:
		- Nome público para o agente de atendimento (ex: “Atendente João”)
				- Nome público para o agente criativo (ex: “Nyra Ana”)
				- Descrição do negócio
				- Instagram / Site / Redes
				- Cores da marca
				- Objetivos principais (vendas, marketing, suporte etc.)
3. **Verificação e Configuração**
	- Alphie (via n8n) verifica os dados → dispara setup:
		- Criação do workspace (Supabase, CRM, Drive)
				- Instalação do Brann e Nyra (Evolution API / n8n)
				- Envio de mensagem inicial no WhatsApp
4. **Teste & Validação**
	- Campos:
		- Status do Brann (ativo/testado)
				- Status da Nyra (postagem teste ok)
				- Status do Alphie (relatórios e CRM)
				- Checklist automático ✅
5. **Entrega ao Cliente**
	- Envio do **tutorial personalizado** (documento + vídeo)
		- Campos:
		- Link do tutorial
				- Mensagem enviada via WhatsApp
				- Data da entrega
6. **Monitoramento Inicial (7 dias)**
	- Campos:
		- Feedback do cliente
				- Correções automáticas (se houver erro detectado)
				- Status final: “Onboarding Concluído”

---

### ⚙️ Automações que você pode ativar no Pipefy

- **Integração Stripe → Pipefy:** cria o card automaticamente quando há nova venda.
- **Pipefy → n8n:** Alphie recebe webhook com os dados e dispara configuração.
- **Pipefy → WhatsApp (Evolution API):** envia mensagens automáticas de boas-vindas e acompanhamento.
- **Pipefy → Supabase/Notion:** cria registro do cliente no CRM.
- **Pipefy → Discord:** notifica o canal #onboarding sobre novos clientes.

---

### 💡 Template-base para escolher

Na tela que você enviou, escolha:

> **"KYB (Know Your Business / Conheça seu Negócio) – Pessoa Jurídica"**

Esse modelo é o mais próximo do que precisamos — ele já traz validações e coleta de dados automáticas que podemos adaptar para “Know Your Client / Onboarding Ginkgo”.

---

Se quiser, posso te montar **o blueprint pronto** desse pipe — já com **nomes das fases, campos personalizados e automações** (formato `.json` para importar no Pipefy).  
Quer que eu gere esse blueprint completo agora?

sex., 10 de out. às 2:49

![afdd627b-3030-46d2-9e0e-d866c419e98d.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000e13061f59ad61949a90493e1&ts=495692&p=fs&cid=1&sig=5d03bc385caa3dc24e231e14a7199ea5bba8dd1de2e78c8adb43389d4666be45&v=0)

E Aqui/

Perfeito — essa é a tela inicial onde o **Pipefy AI** te pede para digitar o que você quer que ele crie.  
É aqui que vamos guiar a IA para gerar automaticamente o **pipe completo de onboarding da Ginkgo**.

Segue o texto exato que você pode colar na caixa roxa:

---

**Prompt para colar no Pipefy:**

> Crie um pipe completo de *onboarding de novos clientes da Ginkgo AI Systems*. O objetivo é automatizar o processo desde o pagamento até a entrega do setup inicial com os agentes de IA (Brann, Nyra e Alphie).
> 
> Estruture com as seguintes fases:
> 
> 1. **Nova Assinatura Recebida** — coleta dados do Stripe ou formulário: nome, e-mail, WhatsApp, plano e ID da compra.
> 2. **Formulário de Configuração** — cliente responde com nomes desejados para seus agentes, descrição do negócio, redes sociais e cores da marca.
> 3. **Configuração Automática** — integração com n8n e Supabase para gerar ambiente, instalar os agentes e confirmar status.
> 4. **Teste e Validação** — campos para Alphie marcar: Brann ativo, Nyra postando, CRM configurado.
> 5. **Entrega e Tutorial** — envio do link de tutorial personalizado e confirmação da entrega.
> 6. **Monitoramento Inicial (7 dias)** — feedback, correções e encerramento.
> 
> Adicione campos de texto, lista e checkbox conforme necessário e prepare o pipe para receber automações externas via webhook do n8n.  
> Nome do pipe: **Onboarding Ginkgo AI Systems**

---

Depois de colar isso, clica em **“Criar pipe”**.  
Ele vai gerar o esqueleto automaticamente.  
Assim que estiver criado, posso te ajudar a:  
– ajustar os **campos personalizados** (tipos, automações, webhooks);  
– criar o **formulário público** que Alphie envia;  
– conectar o **n8n** para execução automática.

Quer que eu te diga exatamente como configurar esses campos depois que ele gerar o pipe?

![7a1de706-04ce-45aa-a49e-8d6e12257eca.png](https://chatgpt.com/backend-api/estuary/content?id=file_0000000016f0622f952768e6c4e1c957&ts=495692&p=fs&cid=1&sig=85fea10d50279c7315a5ebe301ebb415f44b9874b00677e7674e7026aff6dfd4&v=0)

Excelente — o **pipe de onboarding da Ginkgo** já nasceu exatamente como deveria: organizado, limpo e com o esqueleto certo. Agora é a hora de **afiná-lo para o uso real com Alphie e o n8n**.

Vamos ajustar em três níveis: campos, automações e integrações.

---

### 🔧 1. Ajustar os campos de cada fase

**Formulário inicial (entrada pública)**  
Isso é o gatilho do onboarding.  
Adicione/ajuste:

- Nome do Cliente *(texto curto)*
- E-mail *(texto curto)*
- WhatsApp *(número, formato internacional)*
- Plano escolhido *(lista: Básico, Futurista, Imagine)*
- ID da compra *(texto)*
- **Origem da assinatura** *(opcional: Stripe, Hotmart, Manual)*

Marque **“Formulário público”** para gerar link — é o que Alphie enviará automaticamente.

---

**Nova Assinatura Recebida**  
Serve como registro do pagamento confirmado.

- Data de início
- Método de pagamento *(lista)*
- Status da assinatura *(Ativa, Pendente, Cancelada)*
- Anexo do comprovante *(arquivo)*

🟢 Automação:  
Quando um novo card for criado, **enviar e-mail automático** de boas-vindas (modelo simples com texto + link do formulário de configuração).

---

**Formulário de Configuração**  
Essa é a coleta principal para Alphie.

- Nome desejado do agente de atendimento (Brann)
- Nome desejado da agente criativa (Nyra)
- Descrição do negócio *(texto longo)*
- Links de redes sociais *(texto múltiplo)*
- Cores principais da marca *(texto curto ou lista)*
- Objetivo principal *(vendas, marketing, suporte etc.)*

🟢 Automação:  
Quando o card for movido para esta fase → **enviar automaticamente o link do formulário ao cliente via WhatsApp (Evolution API no n8n)**.

---

**Configuração Automática**  
Aqui Alphie age.

- Tipo de configuração *(Brann, Nyra, Alphie)*
- Prioridade *(Alta/Média/Baixa)*
- Data limite *(automática)*
- Descrição da configuração *(detalhe técnico)*
- Checklist *(status de instalação por agente)*

🟢 Automação:  
Webhook → envia os dados para o n8n, que:

1. Cria ambiente Supabase,
2. Ativa instância Evolution,
3. Retorna status via API → atualiza campos automaticamente.

---

**Teste e Validação**  
Verifica se tudo está funcionando.

- Cenário de teste *(texto)*
- Resultado *(checkbox: Aprovado / Requer ajuste)*
- Data de conclusão
- Responsável pela validação

🟢 Automação:  
Se todos os checkboxes “Aprovado” → mover para “Entrega e Tutorial”.

---

**Entrega e Tutorial**  
Finalização e feedback.

- Link do tutorial personalizado
- Data da entrega
- Notas de feedback
- Canal de entrega (WhatsApp, E-mail, ambos)

🟢 Automação:  
Quando o card entrar nesta fase →

1. Enviar tutorial e mensagem de “Onboarding concluído” via WhatsApp.
2. Criar lembrete em 7 dias para Alphie solicitar feedback.

---

### ⚙️ 2. Automações principais (Pipefy + n8n)

1. **Webhook “Nova Assinatura”** → quando novo cliente entra, dispara fluxo n8n para registrar no CRM Supabase.
2. **Webhook “Formulário de Configuração concluído”** → ativa Alphie para gerar os setups (Brann/Nyra).
3. **Webhook “Entrega e Tutorial”** → envia relatório final + fecha o card.

---

### 🧠 3. Integrações ideais

- **n8n:** toda automação de execução (configuração, notificações e testes).
- **Supabase:** banco de clientes e status.
- **Discord:** notificação no canal `#onboarding` quando nova assinatura entra.
- **WhatsApp (Evolution API):** mensagens automáticas.
- **Google Drive:** armazenar tutoriais e anexos.

---

Se quiser, posso te montar o **modelo JSON completo para importação** no Pipefy (com todos os campos e automações prontas para integração n8n).  
Quer que eu gere esse arquivo pra ti agora?