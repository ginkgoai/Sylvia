---
title: "Ginkgo Core - Modelo de plataforma web"
source: "https://chatgpt.com/g/g-p-68e0a0b393cc8191a0f44ad743e1117d/c/69264d7c-6154-8332-96bb-e352c3766765"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
Segue o modelo do site do Leaf como plataforma web com login/cadastro, landing focada no produto e backend de atendimento no Chatwoot.

---

## 1\. Arquitetura geral

- **Frontend (Web App + Landing)**
	- Framework: React/Next.js (ou Lovable gerando o app web).
		- Duas áreas:
		- **Landing pública** (`/`)
				- **Plataforma Leaf** (`/app/*`) apenas para logados.
- **Autenticação e dados dos usuários**
	- Supabase/Postgres para usuários, organizações, planos, etc., encaixa perfeito com o stack que você já usa.
		relatorio
- **Backend de atendimento**
	- **Chatwoot** como coração do suporte:
		- Widget de chat na landing e na área logada.
				- API do Chatwoot para criar contatos, conversas, tags e atributos (plano, status, etc.).

---

## 2\. Estrutura de páginas

### 2.1. Landing Page – /

Visual: seguir identidade do Leaf (Ginkgo azul/futurista, fundo escuro, glow leve, animações suaves).

Blocos:

1. **Hero**
	- Logo Leaf (animada/3D se possível).
		- Headline direta:  
		“Seu time de IAs para atendimento, conteúdo e operação – em uma assinatura mensal.”
		- Subheadline:  
		“Brann atende, Nyra cria, Alphie organiza. Você só foca em vender.”
		- CTAs:
		- “Começar agora” → `/auth/register`
				- “Entrar na plataforma” → `/auth/login`
		- Chatwoot widget flutuante: “Precisa de ajuda? Fale com a equipe Leaf”.
2. **Como o Leaf funciona**
	- 3 cards, um para cada IA:
		- **Brann** – Atendimento e vendas via WhatsApp.
				- **Nyra** – Conteúdo e social media.
				- **Alphie** – Operação, relatórios e bastidores.
		- Cada card com mini fluxograma/resumo.
3. **Planos**
	- Cards com:
		- Nome do plano (ex.: Leaf Base, Leaf Wave, Leaf Full).
				- Para quem é.
				- Entregas principais (checklist claro).
				- CTA: “Assinar” (link para checkout/Hotmart/Stripe) ou “Quero conversar” abrindo Chatwoot.
4. **Para quem é**
	- Lista: pequenos negócios, experts, infoprodutores, clínicas, imobiliárias etc.
		- Depoimentos ou mini-cases (mesmo fake no MVP).
5. **Sessão “Por trás do Leaf”**
	- Foto/ilustração tua.
		- Texto curto “Sobre o criador / CEO & Arquiteto de IA”.
		- CTA: “Projeto personalizado” → section na própria página ou `/projeto-personalizado`.
6. **FAQ**
	- Perguntas típicas: contratos, cancelamento, suporte, prazos de implementação, etc.
7. **Rodapé**
	- Links: Termos, Privacidade, Contato.
		- Link para WhatsApp e redes sociais da Ginkgo.

---

### 2.2. Autenticação

#### /auth/register

Campos:

- Nome completo
- E-mail
- Senha
- Nome do negócio
- Nicho (select)
- Tamanho da equipe (opcional)
- Aceite de Termos / Privacidade

Ações:

1. Cria usuário e organização no banco (Supabase).
2. Faz login automaticamente.
3. Chama API do **Chatwoot**:
	- Cria **Contact** com:
		- Nome, email, nome do negócio.
				- Custom attributes: `plan="trial" | "paid"`, `source="leaf_website"`.
		- Cria uma **conversation** inicial com mensagem padrão:
		- “Novo cliente criado a partir do site Leaf”.

Redireciona para `/app/onboarding`.

#### /auth/login

Campos:

- E-mail
- Senha

Ações:

- Autentica via Supabase.
- Redireciona para `/app/dashboard`.

---

### 2.3. Área logada – Plataforma Leaf

Base: layout com sidebar lateral e header superior.

Rotas principais:

1. **`/app/dashboard`**
	- Boas-vindas personalizadas.
		- “Status da sua assinatura”.
		- 3 blocos:
		- Ativação do Brann.
				- Ativação da Nyra.
				- Ativação da Alphie.
		- Botão “Falar com suporte” (abre Chatwoot ou embed).
2. **`/app/brann`**
	- Explica o que ele faz.
		- Checklist de implementação:
		- Conectar WhatsApp.
				- Enviar docs da empresa.
				- Configurar mensagens principais.
		- Botão “Configurar com suporte” → abre Chatwoot com tag `brann_onboarding`.
3. **`/app/nyra`**
	- Painel simples: calendário de conteúdo, status das redes, botão para enviar briefing.
		- Botão “Quero um calendário de posts” → dispara mensagem pré-pronta no Chatwoot.
4. **`/app/alphie`**
	- Resumo de tarefas/rotinas que o Leaf vai cuidar.
		- Links para planilhas/CRMs/aplicações externas se existirem.
		- CTA “Organizar minha operação” → Chatwoot.
5. **`/app/configuracoes`**
	- Dados da conta.
		- Dados da empresa.
		- Plano atual, botão de upgrade/downgrade.

---

## 3\. Integração com Chatwoot (backend de atendimento)

Pontos-chave:

1. **Widget no site**
	- Script global do Chatwoot injectado:
		- Na Landing: suporte pré-venda.
				- Na área logada: suporte pós-venda + operacional.
		- Em usuários logados, passar `identifier_hash` /dados do usuário para o Chatwoot (para unificar contato).
2. **Criação automática de contato**
	- No cadastro:
		- Chamada `POST /api/v1/accounts/{account_id}/contacts` com:
			- `name`, `email`, `custom_attributes` (plano, nicho, tamanho da empresa, id\_supabase).
		- Tag: `leaf_user`.
3. **Conversas guiadas**
	- Templates de mensagem inicial:
		- Onboarding geral.
				- Assistência para Brann, Nyra, Alphie.
		- Cada botão/CTA interno no app pode abrir o Chatwoot com contexto:
		- Ex: “Preciso ativar o Brann no meu WhatsApp” → envia como primeira mensagem.
4. **Centralização do suporte**
	- Todo contato site → Chatwoot.
		- Humanos + agentes de IA (Brann/Leaf) respondendo por lá.
		- No futuro, você pode plugar n8n para automatizar respostas ou triagens.

---

## 4\. Modelo de prompt para construir isso (Manus/Lovable ou similar)

Você pode colar algo assim na ferramenta de geração de app:

> “Quero uma plataforma web chamada **Leaf**, com:
> 
> 1. **Landing page pública** em `/` com:
> - Hero explicando que o Leaf é um time de IAs para negócios (Brann, Nyra e Alphie).
> - Sessão ‘Como funciona’, cards para cada IA.
> - Sessão de planos com 3 planos (Base, Intermediário, Full) com botões de assinatura.
> - Sessão ‘Sobre o criador’ com espaço para foto, nome e texto curto do CEO.
> - FAQ e rodapé com links para termos, privacidade e redes sociais.
> - Inserir o script de widget do Chatwoot em todas as páginas.
> 2. **Sistema de autenticação** com Supabase:
> - Páginas `/auth/register` e `/auth/login`.
> - Cadastro com campos: nome, e-mail, senha, nome do negócio, nicho, tamanho da equipe.
> - Após cadastro, criar um registro de organização e vincular ao usuário.
> - Redirecionar para `/app/onboarding`.
> 3. **Área logada** sob `/app/*` com:
> - Layout com sidebar e header.
> - `/app/dashboard`: boas-vindas, status do plano, cards de Brann, Nyra e Alphie com CTAs.
> - `/app/brann`, `/app/nyra`, `/app/alphie`: páginas de descrição e checklists de implementação com botões para abrir o suporte.
> - `/app/configuracoes`: dados do usuário, dados da empresa, plano atual.
> 4. **Integração com Chatwoot**:
> - Adicionar o script do widget do Chatwoot globalmente.
> - Ao registrar novo usuário, chamar uma função backend que crie um contato no Chatwoot via API com nome, e-mail, nome do negócio e atributos personalizados (plano, nicho, id do usuário).
> - Criar uma conversa inicial no Chatwoot para cada novo registro com uma mensagem padrão de onboarding.
> - Na área logada, quando o usuário clicar nos botões ‘Falar com suporte’ ou ‘Configurar Brann/Nyra/Alphie’, abrir o widget do Chatwoot e enviar uma mensagem inicial correspondente (ex.: ‘Quero ajuda para configurar o Brann’).
> 5. **Design**:
> - Visual futurista, baseado no Leaf/Ginkgo: fundo escuro, tons de azul, roxo e detalhes em neon.
> - Botões grandes, tipografia moderna, micro animações em hover.
> - Responsivo para desktop e mobile.
> 
> Gere todo o frontend (componentes, rotas) e a lógica mínima de backend necessária (funções para integração com a API do Chatwoot e cadastro de usuários), pronto para deploy em produção.”

Se quiser, na próxima etapa posso detalhar os campos exatos da organização/tabelas no Supabase e os endpoints do Chatwoot que você deve chamar em cada ação.

Perfeito, então: **nada de app logado, só LEAF como “casca visual” em cima do Chatwoot**, que é a plataforma real.

Vou te entregar 2 coisas:

1. Modelo de landing do Leaf (seções + CTAs).
2. Como isso conversa com o Chatwoot + prompt pronto pra jogar na Manus/Lovable.

---

## 1\. Conceito do Leaf

- O Leaf é:
	- **Uma landing-page SaaS** bonita, futurista, com cara de plataforma.
		- **Por baixo**, tudo que é “plataforma” (suporte, onboarding, dúvidas, pedido de implementação) acontece **dentro do Chatwoot**.
- Na prática:
	- O usuário nunca vê painel interno.
		- Ele vê uma landing de produto + botão em tudo que importa.
		- Cada botão abre o **widget do Chatwoot** ou direciona para um **link/URL de inbox/Whats**.

Pensa assim: Leaf é um “launcher de intents” e o Chatwoot é a “nave-mãe de operação”.

---

## 2\. Estrutura da Landing do Leaf

Rota única: `/` (one-page).

### 2.1 Hero

Elementos:

- Logo do Leaf / Ginkgo.
- Headline:
	- “Seu time de IAs plugado no seu negócio em uma assinatura mensal.”
- Subheadline:
	- “Brann atende, Nyra cria, Alphie organiza. Você só precisa dizer o que quer vender.”
- CTAs:
	- Botão principal: **“Quero ativar o Leaf”** → abre Chatwoot com tag `lead_leaf_ativacao`.
		- Secundário: **“Ver planos”** → scroll para sessão Planos.
- Chatwoot widget fixo no canto: “Fale com o time Leaf”.

### 2.2. Como funciona

Três colunas:

- **Brann** (Atendimento & Vendas)
	- “Atende seus clientes no WhatsApp, vende, agenda, responde objeções.”
		- Botão: “Ativar Brann no meu negócio” → Chatwoot com mensagem inicial específica.
- **Nyra** (Conteúdo & Social Media)
	- “Cria, agenda e posta conteúdos alinhados com a sua oferta.”
		- Botão: “Quero conteúdo automático” → Chatwoot com mensagem inicial.
- **Alphie** (Operação & Bastidores)
	- “Organiza tarefas, monitora processos e entrega relatórios.”
		- Botão: “Organizar minha operação” → Chatwoot.

Todos os botões abrem o mesmo widget, mas com **texto inicial diferente**, para você taguear na entrada.

### 2.3. Planos

3 cards simples:

- **Leaf Base**
	- Para autônomos / pequenos negócios.
		- Entregas básicas de Brann + Nyra.
		- Botão: “Assinar Leaf Base”.
		- Pode ir para:
			- Link de pagamento (Hotmart/Stripe) **ou**
						- Chatwoot com tag `plano_base_interesse`.
- **Leaf Pro**
	- Para negócios em crescimento.
		- Brann + Nyra + Alphie com mais recorrência.
		- Botão: “Assinar Leaf Pro”.
- **Leaf Full / Futurista**
	- Tudo incluído + melhorias contínuas.
		- Botão: “Falar sobre Leaf Full” (leva direto pro Chatwoot, sem checkout direto).

Visual:

- Layout SaaS padrão: cards com preço, bullet points e um selo tipo “Mais escolhido”.

### 2.4. Para quem é

Lista de perfis:

- Infoprodutores
- Prestadores de serviço
- Clínicas / consultórios
- Imobiliárias
- Lojas online

Mini textos e ícones.

Botão final:  
**“Não sabe se o Leaf serve pra você?”** → Chatwoot: “Me ajuda a entender se o Leaf serve para meu negócio”.

### 2.5. Sessão “Por trás do Leaf”

- Foto/ilustração tua como **CEO & Arquiteto de IA**.
- Texto curto:
	- Quem você é.
		- Breve visão: “Quero que pequenos negócios tenham um time de IAs como grandes empresas”.
- Botão:
	- **“Projeto personalizado com o criador”** → Chatwoot com tag `projeto_personalizado_ceo`.

### 2.6. FAQ

Perguntas do tipo:

- “Em quanto tempo o Leaf fica funcionando?”
- “Preciso aparecer em vídeo?”
- “Como funciona o pagamento?”
- “Tem fidelidade? Posso cancelar quando quiser?”

Final da sessão:

- Botão: **“Minha dúvida não está aqui”** → Chatwoot.

### 2.7. Chamada final (footer hero)

Seção final com:

- Frase forte:
	- “Enquanto você pensa se vale a pena, alguém está usando IA para atender, vender e crescer 24/7.”
- Botão grande: **“Começar com o Leaf agora”** → Chatwoot.

Rodapé com:

- Termos de uso.
- Política de privacidade.
- Contatos e redes.

---

## 3\. Como essa landing “encaixa” no Chatwoot

Tudo se baseia em **3 coisas**:

1. **Widget do Chatwoot** embutido no site (script global).
2. **Mensagens iniciais diferentes** para cada CTA.
3. **Tags/atributos** no Chatwoot para organizar o funil.

### 3.1. Widget

Você adiciona o script padrão do Chatwoot no `<head>` ou antes do `</body>` do site.

Cada botão do site faz:

- `window.$chatwoot.run()` (ou equivalente) para abrir o widget.
- Envia uma mensagem inicial (texto default) do tipo:
	- “Oi, quero ativar o Leaf no meu negócio.”
		- “Oi, quero saber mais sobre o plano Leaf Pro.”
		- “Oi, quero um projeto personalizado com o criador.”

Isso já chega no Chatwoot pronto pra você:

- Taggear automaticamente pelo texto ou via automação (Webhook + n8n).
- Jogar em filas diferentes se quiser (pré-venda, suporte, projeto premium).

### 3.2. Organização interna

Você pode:

- Criar **Automations** no Chatwoot que:
	- Se mensagem inicial contém “Ativar Brann” → adiciona tag `brann_onboarding`.
		- Se contém “Leaf Pro” → tag `leaf_pro`.
		- Se contém “projeto personalizado” → move para inbox VIP.

Resultado:  
Landing = só interface.  
Chatwoot = CRM de suporte, vendas, onboarding, tudo centralizado.

---

## 4\. Prompt pronto para jogar na Manus/Lovable (ou similar)

Use algo assim:

> “Quero uma **landing page de um SaaS chamado Leaf**, da Ginkgo, que funciona como uma casca visual por cima do Chatwoot.
> 
> Requisitos:
> 
> 1. **Página única `/`** com layout de plataforma SaaS:
> - Hero com headline, subheadline, logo e dois botões:
> 	- ‘Quero ativar o Leaf’ (abre o widget de chat).
> 		- ‘Ver planos’ (scroll para a sessão de planos).
> - Sessão ‘Como funciona’ com três cards:
> 	- Brann (IA de atendimento e vendas).
> 		- Nyra (IA de conteúdo e social media).
> 		- Alphie (IA de operação e relatórios).  
> 		Cada card com texto curto e botão de ação que abre o chat.
> - Sessão de planos com 3 planos (Leaf Base, Leaf Pro, Leaf Full) com preço, bullets de benefícios e botões:
> 	- Nos planos básicos, botão pode apontar para um link de pagamento (colocar placeholder).
> 		- Em todos os planos, opção de botão para ‘Falar com o time’ que abre o chat.
> - Sessão ‘Para quem é’ com ícones e pequenos textos (infoprodutor, prestador de serviço, clínica, imobiliária, loja online).
> - Sessão ‘Por trás do Leaf’ com espaço para foto do CEO e texto curto; botão ‘Projeto personalizado com o criador’ que abre o chat.
> - Sessão de FAQ com 6–8 perguntas e respostas padrão e botão ‘Minha dúvida não está aqui’ abrindo o chat.
> - Chamada final com botão grande ‘Começar com o Leaf agora’, também abrindo o chat.
> - Rodapé com links de termos, privacidade e redes sociais.
> 2. **Integração com Chatwoot**:
> - Adicionar o script global do widget do Chatwoot em todas as páginas.
> - Todo botão de ação relevante deve abrir o widget do Chatwoot (pode usar uma função JavaScript global `openLeafChat(initialMessage)`).
> - A função `openLeafChat` deve:
> 	- Abrir o widget do Chatwoot.
> 		- Preencher uma mensagem inicial diferente conforme o botão (ex.: ‘Quero ativar o Leaf’, ‘Quero ativar o Brann’, ‘Quero saber sobre Leaf Pro’, ‘Quero um projeto personalizado com o criador’).
> 3. **Design**:
> - Estilo futurista, inspirado em IA: fundo escuro, tons de azul e ciano, alguns detalhes em neon.
> - Componentes com bordas suaves, sombras discretas e tipografia moderna.
> - Responsivo para desktop e mobile.
> 
> Não quero área logada nem dashboard; a ‘plataforma’ é o próprio Chatwoot. A landing deve parecer uma plataforma SaaS, mas todas as ações de uso e suporte são resolvidas via chat.”

Com isso você tem: Leaf como vitrine + “console” visual, Chatwoot como plataforma funcional, sem precisar codar painel nenhum agora.

Perfeito, então vamos fixar a definição:

- **Leaf = atendimento. Ponto.**
- Só **BRANN** opera aqui (IA atendente / vendedor).
- **Alphie → Wave**, **Nyra → Pyre** (não entram no Leaf).
- “Plataforma” = **Chatwoot + Brann**, com uma **landing visual da Ginkgo** por cima, usando **só a logo da Ginkgo** (Leaf vira nome do serviço, não uma marca separada).

Vou te entregar:

1. Modelo da landing do Leaf (somente atendimento).
2. Como isso pluga no Chatwoot.
3. Prompt pronto pra jogar na Manus/Lovable.

---

## 1) Modelo da Landing do Leaf (somente atendimento BRANN)

Página única `/`, com vibe de plataforma, mas sem painel logado.

### 1\. Hero (capa)

Elementos:

- **Logo GINKGO** no topo (nada de logo separada pro Leaf).
- Título:
	- “Leaf: seu atendente de IA plugado no WhatsApp e redes.”
- Subtexto:
	- “BRANN atende, responde, vende e registra tudo. Você só acompanha pelo seu painel.”
- CTAs:
	- Botão principal: **“Quero ativar o Leaf no meu negócio”** → abre Chatwoot.
		- Link secundário: **“Falar com alguém agora”** → também abre Chatwoot.

Chatwoot widget fixo no canto, já carregado.

Background: futurista escuro, azul Ginkgo, minimalista.

---

### 2\. Como o Leaf funciona

Seção simples em 3 passos, sempre focando em **BRANN + Chatwoot + WhatsApp**:

1. **Você conecta seus canais**
	- WhatsApp (via Evolution API ou similar)
		- Outros canais (Instagram, Messenger, etc., se quiser citar)
2. **BRANN aprende seu negócio**
	- Briefing, FAQs, produtos/serviços, tom de voz, persona.
3. **BRANN atende por você**
	- Responde leads, direciona pedidos, marca retornos, registra tudo no Chatwoot.

Botão da seção:  
**“Ver como ficaria no meu negócio”** → abre Chatwoot com mensagem inicial.

---

### 3\. Canais atendidos

Grid com ícones:

- WhatsApp
- Instagram (DM)
- Facebook Messenger
- Site (widget)
- Outros (placeholder)

Texto curto:

> “O Leaf é o ‘cérebro de atendimento’ que você pluga nos canais que já usa.  
> A operação roda pelo Chatwoot + BRANN, com tudo registrado por conversa e contato.”

Botão:  
**“Quero conectar meus canais”** → Chatwoot.

---

### 4\. Benefícios do Leaf (focado em atendimento)

Bullets claros, sem viajar:

- Respostas rápidas e consistentes 24/7 (quando você quiser).
- Argumentação de vendas treinada na sua oferta.
- Separação de leads quentes, mornos e frios.
- Histórico organizado no Chatwoot (por cliente, por canal).
- Handoff fácil para humano quando necessário.

Um micro-card lateral:  
“Tecnologia da Ginkgo rodando em cima do Chatwoot e automações n8n.”

---

### 5\. Planos de atendimento Leaf (opcional, mas recomendável)

3 cards, todos focados em atendimento BRANN:

- **Leaf Start**
	- 1 canal (WhatsApp)
		- FAQs + respostas básicas
		- Horário configurado
		- Botão: “Quero o Leaf Start” → Chatwoot ou link de pagamento.
- **Leaf Growth**
	- Até 2–3 canais
		- Argumentação de vendas personalizada
		- Monitoria e ajustes mensais
		- Botão: “Quero o Leaf Growth”.
- **Leaf Prime**
	- Atendimento completo multi-canal
		- Scripts de vendas avançados
		- Ajustes contínuos + relatórios
		- Botão: “Falar sobre o Leaf Prime” → Chatwoot (sem checkout direto).

Importante: aqui você não cita Alphie nem Nyra. Só **atendimento BRANN**.

---

### 6\. “Por trás do Leaf” (Ginkgo + você)

Seção com:

- Logo Ginkgo + teu nome como “CEO & Arquiteto de IA”.
- Pequeno texto:
	- “O Leaf é o serviço de atendimento da Ginkgo, pensado para pequenas e médias empresas que querem um atendente de IA operando em cima do Chatwoot e do WhatsApp, adaptado à sua persona, seu produto e seu jeito de falar.”
- Botão:
	- **“Quero um atendimento desenhado direto com o criador”** → abre Chatwoot com mensagem específica.

---

### 7\. FAQ

Perguntas alinhadas ao modelo:

- Preciso trocar meu WhatsApp?
- Em quanto tempo o Leaf começa a atender?
- Como o BRANN aprende sobre meu negócio?
- O que eu preciso entregar para começar?
- Como funciona a cobrança?
- E se eu quiser pausar/cancelar?

Final da seção:  
**“Minha dúvida não está aqui”** → Chatwoot.

---

### 8\. Fechamento

Frase de impacto:

> “Enquanto você tenta dar conta de tudo, alguém já colocou um atendente de IA pra receber cada lead no lugar dele.”

Botão gigante:  
**“Ativar o Leaf agora”** → Chatwoot.

Rodapé enxuto com:  
Termos, Privacidade, contato, redes (marca Ginkgo).

---

## 2) Como tudo isso encaixa no Chatwoot

Nada de painel próprio. Só:

- **Landing = interface bonita**
- **Chatwoot = plataforma real**
- **BRANN = motor de IA por trás**

Pontos práticos:

1. **Widget do Chatwoot**
	- Script global no site.
		- Todos os botões importantes chamam uma função JS, tipo:  
		`openLeafChat("mensagem inicial x")`.
2. **Função openLeafChat(message)**  
	Conceito:
	- Abre o widget.
		- Preenche a primeira mensagem com algo como:
		- “Quero ativar o Leaf no meu negócio.”
				- “Quero o plano Leaf Growth.”
				- “Quero um atendimento desenhado direto com o criador.”
3. **Automação no Chatwoot**
	- Você configura regras:
		- Se mensagem contém “Leaf Start” → tag `leaf_start`.
				- Se mensagem contém “Leaf Growth” → tag `leaf_growth`.
				- Se mensagem contém “criador” → manda pra inbox VIP.

Resultado:  
Toda a lógica de funil, triagem e suporte é governada no próprio Chatwoot.

---

## 3) Prompt pronto para Manus / Lovable (copiar e colar)

Use algo assim:

> “Quero uma **landing page única** para um serviço chamado **Leaf**, que é o serviço de atendimento da empresa Ginkgo.
> 
> Importante:
> 
> - O Leaf é **somente atendimento**, operado pela IA BRANN, em cima do **Chatwoot** e do **WhatsApp/outros canais do cliente**.
> - Não quero área logada, dashboard nem painel próprio.
> - A plataforma real é o **Chatwoot**. A landing é só a ‘casca visual’ para vender e acionar o atendimento.
> 
> Estrutura da página `/`:
> 
> 1. **Hero (capa)**
> - Mostrar apenas a **logo da Ginkgo** (o Leaf é o nome do serviço, não uma marca separada).
> - Título: algo como ‘Leaf: seu atendente de IA plugado no WhatsApp e redes.’
> - Subtítulo: ‘BRANN atende, responde, vende e registra tudo. Você só acompanha pelo seu painel.’
> - Botão principal: ‘Quero ativar o Leaf no meu negócio’ → chama uma função `openLeafChat("Quero ativar o Leaf no meu negócio")`.
> - Botão secundário: ‘Falar com alguém agora’ → também chama `openLeafChat("Quero falar com alguém agora sobre o Leaf")`.
> 2. **Seção ‘Como o Leaf funciona’**
> - Explicar em três passos simples:
> 	1. Você conecta seus canais (WhatsApp e outros).
> 		2. BRANN aprende seu negócio (briefing, FAQs, produtos, tom de voz).
> 		3. BRANN passa a atender por você, e tudo fica registrado no Chatwoot.
> - Botão: ‘Ver como ficaria no meu negócio’ → `openLeafChat("Quero ver como o Leaf ficaria no meu negócio")`.
> 3. **Seção de canais atendidos**
> - Ícones de WhatsApp, Instagram, Facebook Messenger e Site.
> - Texto explicando que o Leaf funciona como um ‘cérebro de atendimento’ em cima do Chatwoot, plugado nesses canais.
> - Botão: ‘Quero conectar meus canais’ → `openLeafChat("Quero conectar meus canais ao Leaf")`.
> 4. **Seção de benefícios do Leaf (focado em atendimento)**
> - Bullets como: respostas mais rápidas, organização das conversas no Chatwoot, filtragem de leads quentes, etc.
> 5. **Seção de planos (opcional, mas já preparada)**
> - Três cards: Leaf Start, Leaf Growth, Leaf Prime (por exemplo).
> - Cada card com bullets resumidos e um botão:
> 	- ‘Quero o Leaf Start’ → `openLeafChat("Quero o plano Leaf Start")`.
> 		- ‘Quero o Leaf Growth’ → `openLeafChat("Quero o plano Leaf Growth")`.
> 		- ‘Falar sobre o Leaf Prime’ → `openLeafChat("Quero falar sobre o plano Leaf Prime")`.
> - (Opcional) Campo/link de pagamento com placeholder para URL externa de checkout.
> 6. **Seção ‘Por trás do Leaf’**
> - Espaço para explicar que o Leaf é o serviço de atendimento da Ginkgo.
> - Espaço para foto/nome do CEO como arquiteto de IA.
> - Botão: ‘Quero um atendimento desenhado direto com o criador’ → `openLeafChat("Quero um atendimento desenhado direto com o criador do Leaf")`.
> 7. **FAQ**
> - 6–8 perguntas e respostas comuns sobre implementação, prazo, pagamento e cancelamento.
> - Botão final: ‘Minha dúvida não está aqui’ → `openLeafChat("Minha dúvida não está aqui, quero tirar uma dúvida sobre o Leaf")`.
> 8. **Fechamento**
> - Frase de impacto e um botão grande: ‘Ativar o Leaf agora’ → `openLeafChat("Quero ativar o Leaf agora")`.
> - Rodapé simples com termos de uso, política de privacidade e redes sociais da Ginkgo.
> 
> Tecnologias e visual:
> 
> - Página responsiva, estilo SaaS moderno, fundo escuro com tons de azul (padrão Ginkgo), tipografia limpa, bordas suaves e alguns detalhes sutis de brilho/IA.
> 
> Integração com Chatwoot:
> 
> - Incluir o script global do widget do Chatwoot (colocar um placeholder para o código).
> - Implementar uma função JavaScript global `openLeafChat(initialMessage)` que:
> 	- Abre o widget do Chatwoot.
> 		- Preenche/enfileira a mensagem inicial `initialMessage` no chat, para que ela seja enviada automaticamente ou copiada pelo usuário.
> 
> Lembrar: o Leaf é somente o serviço de atendimento com BRANN. Alphie e Nyra pertencem a outros produtos (Wave e Pyre) e não devem ser mencionados nessa página.”

Se quiser, no próximo passo posso te ajudar a escrever as **mensagens exatas** que o BRANN (via Chatwoot) deve mandar nos primeiros contatos de cada botão (script de abordagem).