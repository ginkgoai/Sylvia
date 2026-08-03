---
title: "GKO - O que é automação"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/68d0afb9-4444-832f-967f-2138acb2ed1e"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
dom., 21 de set. às 23:09

O que aparece no vídeo é o **Botpress Studio**, uma plataforma de criação de chatbots.  
O fluxo mostrado é um **menu interativo de múltipla escolha**, típico de automação de atendimento no WhatsApp Business.

### O que está acontecendo nessa tela

- A aba aberta é **“Generic Business – Custom Behavior”**, ou seja, um comportamento personalizado de um bot.
- Há um **bloco de “Escolha Múltipla”**, que permite ao usuário escolher serviços.
- Cada opção leva a um subfluxo:
	- **OP1\_botchat (em inglês)** → Explicação sobre os chatbots da empresa.
		- **OP2 (em inglês)** → Automatizações de chamadas.
		- **OP3 (em inglês)** → Consultar fornecedores.
		- **OP4 (em inglês)** → Conectar o negócio ao serviço principal.

### Em resumo

Essa automação é um **chatbot de WhatsApp criado no Botpress**, que oferece um menu com diferentes opções de serviços de automação e integração de IA. O usuário digita ou seleciona a opção e o bot direciona para o fluxo certo (responder, explicar, integrar com sistemas externos, etc.).

É o tipo de fluxo que você também pode montar para a Ginkgo:

- Primeiro menu → **Catálogo de serviços**.
- Cada opção → **explicação automática** ou **integração com APIs externas** (agenda, CRM, pagamentos).

Quer que eu te mostre como você faria esse mesmo menu **versão Ginkgo**, já traduzido e adaptado para seus planos (Básico, Avançado, Futurista, On Demand)?

Sim

Perfeito, Gabriel. Vou te montar uma versão equivalente do menu que apareceu no vídeo, mas já pensada para a **Ginkgo**, usando seus planos (Básico, Avançado, Futurista e On Demand).

---

### Estrutura do Menu (versão Ginkgo)

**Bloco inicial – Escolha Múltipla**  
Mensagem:  
“Escolha abaixo o serviço que você deseja conhecer:”

**Opções:**

1. **Plano Básico** – Automação inicial, fluxos simples no WhatsApp/Instagram.
	- Subfluxo: Explica benefícios (economia de tempo, respostas rápidas, catálogo simples).
		- Ação: Mostrar botão para falar com atendimento humano se quiser contratar.
2. **Plano Avançado** – Integrações com CRM, agendamento automático, funil de vendas.
	- Subfluxo: Explica que conecta leads direto ao CRM, automatiza lembretes e pagamentos.
		- Ação: Oferece demonstração em vídeo ou PDF explicativo.
3. **Plano Futurista** – IAs inteligentes multi-canal (voz, texto, e-mail), relatórios semanais.
	- Subfluxo: Mostra diferenciais (assistente com IA 24/7, análises automáticas, relatórios no WhatsApp).
		- Ação: Perguntar se deseja “Ver um caso prático” ou “Agendar conversa”.
4. **Plano On Demand (Imagine)** – Projetos sob medida.
	- Subfluxo: Pergunta “Qual desafio você gostaria de automatizar?” e abre campo livre.
		- Ação: Direciona a resposta para pipeline de propostas personalizadas.

---

### Fluxo visual (simplificado)

- **Escolha Múltipla**  
	↳ **OP1\_Básico** → mensagem + ação  
	↳ **OP2\_Avançado** → mensagem + ação  
	↳ **OP3\_Futurista** → mensagem + ação  
	↳ **OP4\_OnDemand** → mensagem + ação

---

### Adaptação prática

Se você quiser, eu posso já montar o **fluxo pronto em JSON para Botpress** (ou até n8n, se preferir). Assim você só importa, edita os textos e já ativa.

Quer que eu prepare direto esse **JSON para Botpress**, igual o do vídeo, mas com as opções Ginkgo?

No botpress

Showtime, Gabriel. Vou te deixar com um fluxo **pronto pra montar no Botpress Studio** em 10 min: nomes exatos de nós, textos já revisados e as expressões pra roteamento. É o mesmo “menu de múltipla escolha” do vídeo, adaptado pros planos da Ginkgo.

## Workflow: Ginkgo – Menu Principal

## 1) Nó Start

- Sem configs (vai direto pro próximo).

## 2) Nó Mensagem: Boas-vindas

- Tipo: **Send Message**
- Texto:
	```markdown
	👋 Bem-vindo à Ginkgo AI Systems.
	Escolha abaixo o serviço que você quer conhecer:
	```
- Em seguida, **Choice (buttons)** no mesmo nó:
	- **Plano Básico** → value: `basico`
		- **Plano Avançado** → value: `avancado`
		- **Plano Futurista** → value: `futurista`
		- **Plano On Demand (Imagine)** → value: `ondemand`

> Se preferir capturar por texto digitado, adicione no final do texto:  
> `Você também pode digitar: basico, avancado, futurista, ondemand.`

## 3) Nó Capturar Opção

- Tipo: **Capture**
- Variável de saída: `temp.escolha`
- Mensagem de erro (Invalid):
	```markdown
	Não entendi sua escolha 🤔. Toque num botão ou digite: basico | avancado | futurista | ondemand.
	```

## 4) Nó Normalizar Entrada (opcional)

- Tipo: **Code / Set Variable**
- Código (JavaScript):
	```markdown
	const raw = (temp.escolha?.value || event.payload?.text || '').toString().toLowerCase().trim()
	const map = { 'básico':'basico', 'basico':'basico', 'avançado':'avancado', 'avancado':'avancado', 'futurista':'futurista', 'on demand':'ondemand', 'ondemand':'ondemand', 'imagine':'ondemand' }
	temp.plano = map[raw] || raw
	```

## 5) Nó Roteador

- Tipo: **Switch / Expression**
- Expressão: `temp.plano`
- Cases:
	- value: `basico` → **Plano Básico**
		- value: `avancado` → **Plano Avançado**
		- value: `futurista` → **Plano Futurista**
		- value: `ondemand` → **Plano On Demand**
- Default: volta para **Boas-vindas** (ou mostra erro educado e retorna).

---

## 6) Nó Plano Básico

- Tipo: **Send Message**
- Texto:
	```markdown
	✅ **Plano Básico**
	• Atendimento rápido no WhatsApp/Instagram (FAQ + respostas prontas)
	• Catálogo simples (PDF/imagens) e captação de leads
	• Integração leve com planilha/CRM inicial
	• Onboarding em 48–72h
	Resultado: ganha tempo e não perde lead por demora.
	```
- **Choice CTA**:
	- **Ver exemplo** → value: `demo_basico`
		- **Quero assinar** → value: `assinar_basico`
		- **Voltar ao menu** → value: `menu`
- **Capture** em `temp.acao`
- **Switch (temp.acao?.value)**:
	- `demo_basico` → **Enviar Demo Básico**
		- `assinar_basico` → **Qual canal prefere?**
		- `menu` → **Boas-vindas**

### Nó Enviar Demo Básico

- Mensagem:
	```markdown
	Aqui está um exemplo do fluxo do Básico (vídeo/pdf).
	```
- (Opcional) **Send File/URL**: cole seu link de demo.
- Next → **Qual canal prefere?**

### Nó Qual canal prefere?

- **Choice**:
	- **Falar no WhatsApp** → `whats`
		- **Agendar uma call** → `call`
		- **Voltar ao menu** → `menu`
- **Capture** em `temp.canal`
- **Switch**:
	- `whats` → **Abrir WhatsApp**
		- `call` → **Agendar Call**
		- `menu` → **Boas-vindas**

### Nó Abrir WhatsApp

- Mensagem:
	```markdown
	Perfeito! Vou te encaminhar pro nosso número no WhatsApp pra fechar em 2 minutos.
	```
- **Action**: Send URL (link do seu WhatsApp).
- Next → **Fim ou Menu**.

### Nó Agendar Call

- Mensagem:
	```markdown
	Vamos marcar uma conversa de 15 min?
	```
- **Action**: link do Calendly/agenda.
- Next → **Fim ou Menu**.

> **Repita a mesma estrutura** para os outros planos, mudando apenas o conteúdo a seguir.

---

## 7) Nó Plano Avançado

- Mensagem:
	```markdown
	🚀 **Plano Avançado**
	• Funil de vendas com CRM (leads entram prontos no pipeline)
	• Agendamento automático, lembretes e cobrança
	• Integrações: WhatsApp, Instagram, site, formulários
	• Relatórios de conversão básicos (semanal)
	Resultado: menos tarefas manuais, mais conversões sem fricção.
	```
- CTA buttons: `demo_avancado`, `assinar_avancado`, `menu`
- Subnós: **Enviar Demo Avançado**, **Qual canal prefere?** (mesma lógica do Básico)

## 8) Nó Plano Futurista

- Mensagem:
	```markdown
	🤖 **Plano Futurista**
	• IA multimodal: voz + texto + e-mail + web
	• Agente 24/7 com memória, RAG e relatórios inteligentes no WhatsApp
	• Orquestração com n8n (integra vários sistemas)
	• Painel de métricas e automações avançadas
	Resultado: atendimento nível “empresa grande”, com análise e melhoria contínua.
	```
- CTA buttons: `ver_caso_futurista`, `falar_consultor`, `menu`
- `ver_caso_futurista` → envia case/vídeo; depois **Qual canal prefere?**
- `falar_consultor` → vai direto para **Qual canal prefere?**

## 9) Nó Plano On Demand (Imagine)

- Mensagem:
	```markdown
	🧪 **Plano On Demand (Imagine)**
	Diga seu desafio em 1–2 linhas (ex.: “quero extrair leads do Instagram e distribuir por região no WhatsApp”).
	```
- **Capture (free text)** em `temp.brief`
- **Mensagem**:
	```markdown
	Entendi. Vamos estimar o escopo e responder com proposta resumida.
	Você prefere continuar no WhatsApp ou agendar uma call?
	```
- **Choice**: `whats`, `call`, `menu` → reutilize nós **Abrir WhatsApp**, **Agendar Call**, **Boas-vindas**.

---

## 10) Nó Erro Educado (opcional)

- Mensagem:
	```markdown
	Não reconheci essa opção 😅. Use os botões ou digite: basico | avancado | futurista | ondemand.
	```
- Next → **Boas-vindas**

---

## Extras úteis (copiar/colar)

### Validação para aceitar texto digitado

- No **Roteador**, troque `temp.plano` por:
	```markdown
	const t = (temp.plano || '').toLowerCase()
	return ['basico','avancado','futurista','ondemand'].includes(t) ? t : 'default'
	```

### “Voltar ao menu” universal

- Em todos os nós de conteúdo, inclua um botão `Voltar ao menu` (value: `menu`) roteando de volta para **Boas-vindas**.

### Etiquetas (tags) por plano

- Após entrar num plano, adicione um **Action: Set Contact Property/Tag**
	- Ex.: `contact.tags += ['interesse_basico']`
		- Isso ajuda a segmentar follow-ups.

---

## Conteúdos prontos (p/ colar nos nós)

## Bloco “Boas-vindas” (texto + botões)

```markdown
👋 Bem-vindo à Ginkgo AI Systems.
Escolha abaixo o serviço que você quer conhecer:

[ Plano Básico ] [ Plano Avançado ]
[ Plano Futurista ] [ Plano On Demand (Imagine) ]

Você também pode digitar: basico, avancado, futurista, ondemand.
```

## Pitchs dos planos (já acima) e CTAs:

- **Ver exemplo / Ver caso prático** → link de demo/case.
- **Quero assinar / Falar com consultor** → WhatsApp ou Calendly.

---

Se quiser, eu também te entrego isso como **arquivo.json** exportável (um “workflow” com todos os nós já conectados). Posso incluir seus **links reais** (WhatsApp, Calendly, PDFs) e já deixar os **tags** e **webhooks** do n8n plugados. Próximo passo: me manda os links que quer usar (WhatsApp, agenda, vídeos/cases) e eu cuspo o pacote completo prático.