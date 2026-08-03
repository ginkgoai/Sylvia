---
title: "Ginkgo Core - Resumo do Projeto Ginkgo"
source: "https://chatgpt.com/g/g-p-68e0a0b393cc8191a0f44ad743e1117d/c/6952db65-8a48-832f-811a-961d33522072"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
seg., 29 de dez. às 16:50

Abaixo está o **resumo mestre, filtrado e estruturado**, contendo **apenas o que a Manus precisa saber** para entender, operar e evoluir o projeto **Ginkgo AI Systems / LEAF (SaaS)** sem ruído, sem contexto desnecessário e sem historicidade irrelevante.

Pense nisso como o **“DNA operacional”** do projeto — se alguém apagar todo o resto e sobrar isso, o sistema ainda nasce funcional.

---

## GINKGO AI SYSTEMS

## Documento de Contexto Técnico-Estratégico (para Manus)

---

## 1\. Visão Geral do Projeto

A **Ginkgo AI Systems** é um ecossistema de produtos SaaS baseados em **agentes de IA + automação**, entregues em modelo de **assinatura estilo Netflix** para empresas.

O objetivo central é **substituir operações humanas repetitivas** (atendimento, marketing, tráfego, organização interna) por **agentes autônomos supervisionáveis**, com onboarding simples, escalabilidade alta e custo previsível.

O ecossistema inicial possui **3 produtos principais**:

- **LEAF** → Atendimento inteligente (WhatsApp-first)
- **PYRE** → Social media + criação e publicação automatizada
- **WAVE** → Gestão de tráfego pago + CRM + analytics

Todos operam sob a mesma fundação técnica.

---

## 2\. Produto Principal (Foco Inicial): LEAF

### O que é o LEAF

O **LEAF** é um **agente de IA operacional** que atua diretamente no **WhatsApp**, não como chatbot genérico, mas como **funcionário digital**.

Ele:

- Atende clientes
- Entende intenção
- Coleta dados
- Registra tudo em banco
- Executa ações reais (agendar, enviar docs, registrar lead, escalar humano)

### Diferencial-chave

> “Não é conversa. É operação.”

---

## 3\. Arquitetura Técnica Base (Obrigatória)

### Stack central

- **Entrada**
	- WhatsApp via **Evolution API**
		- Futuro: Instagram (ManyChat), Web chat, App próprio
- **Orquestração**
	- **n8n** (self-hosted)
		- Atua como cérebro de fluxo, decisões e integrações
- **IA / Agentes**
	- **Manus** como camada de agente (LLM + tools)
		- Prompts mestres + personas
		- RAG quando necessário
- **Dados**
	- **Supabase (PostgreSQL)**
		- Leads
				- Conversas
				- Agendamentos
				- Logs
				- Preferências
		- **Redis** (memória curta)
		- Vetores quando necessário (pgvector / qdrant)
- **Infra**
	- VPS Hostinger
		- Docker
		- EasyPanel

---

## 4\. Persona Base do LEAF (Agente)

### Conceito

Cada cliente **recebe uma versão personalizada do LEAF**, adaptada ao nicho.

Existe um **prompt base** que é adaptado no onboarding.

### Funções mínimas do agente

1. Atendimento inicial automático
2. Classificação de intenção
3. Coleta de dados estruturados
4. Registro em banco
5. Respostas contextuais
6. Handoff humano quando necessário
7. Follow-up automático

---

## 5\. Onboarding do Cliente (Modelo Netflix)

Fluxo ideal (100% automatizável no futuro):

1. Cliente assina plano (Stripe)
2. Recebe acesso
3. Conecta WhatsApp via QR Code
4. Descreve o negócio em linguagem natural
5. Escolhe:
	- Nome do agente
		- Tom de voz
		- Voz (quando áudio ativo)
6. Sistema:
	- Gera prompt
		- Cria tabelas
		- Ajusta fluxos
7. Cliente entra direto em uso

**Sem calls longas. Sem setup manual.**

---

## 6\. Planos do LEAF (Resumo)

- **Base**
	- Atendimento WhatsApp 24/7
		- Registro de leads
		- FAQ inteligente
- **Intermediário**
	- Tudo do Base
		- Follow-ups automáticos
		- Integração com CRM / agenda
		- Relatórios simples
- **Avançado**
	- Tudo acima
		- Integrações externas
		- Lógicas personalizadas
		- Suporte prioritário
		- Possível site/app incluso

---

## 7\. PYRE (Produto 2)

### O que é

Agente de **social media autônomo**.

### Funções

- Planejamento de conteúdo
- Criação (texto, imagem, vídeo)
- Publicação automática (IG / TikTok / FB)
- Calendário editorial
- Relatórios

### Stack

- n8n
- Manus
- NanoBanana / Veo3 / Runway
- APIs de redes sociais

---

## 8\. WAVE (Produto 3)

### O que é

Agente de **gestão de tráfego pago + CRM**.

### Funções

- Monitorar campanhas
- Registrar métricas
- Sugerir otimizações
- Organizar leads
- Relatórios automáticos

### Stack

- n8n
- Supabase
- APIs Meta / Google
- Notion / dashboards

---

## 9\. Filosofia do Sistema

- Tudo é **replicável**
- Tudo é **configurável por linguagem natural**
- Humanos entram apenas:
	- Para exceções
		- Para vendas enterprise
		- Para suporte avançado

O objetivo é escalar de **10 → 100 → 1.000 clientes** sem medo.

---

## 10\. Papel da Manus no Projeto

A **Manus** deve entender que:

- Ela **não é apenas IA de resposta**
- Ela atua como:
	- Cérebro do agente
		- Executor de tarefas
		- Decisor contextual
- Sempre integrada ao n8n
- Sempre operando com dados reais

Ela precisa:

- Respeitar estrutura de dados
- Usar contexto do cliente
- Executar ações, não só falar

---

## 11\. Estado Atual do Projeto

- Arquitetura definida
- Produto LEAF como prioridade
- Site Ginkgo + site LEAF em construção
- Infra Docker pronta
- Fluxos n8n sendo refinados
- Manus sendo contextualizada (este documento faz parte disso)

---

## 12\. Próximo Passo Natural

1. Transformar este resumo em **PDF oficial**
2. Usar o PDF como:
	- Documento de contexto da Manus
		- Base para investidores
		- Manual interno de produto
3. Depois:
	- Quebrar em versões menores (README, onboarding, pitch)

---

### Confirmação

No próximo passo eu posso:

- Converter este conteúdo em **PDF estruturado**
- Criar **versão visual (capa, sumário, diagrama)**
- Adaptar para **prompt de ingestão direta da Manus**

Diga apenas:  
**“Gerar PDF”** ou **“Adaptar para prompt da Manus”**.

gerar

PDF gerado com sucesso.

Ginkgo\_AI\_Systems\_Resumo\_Manus.pdf

Próximos upgrades possíveis (rápidos e estratégicos):

- Versão **mais visual** (capa, sumário, seções bem marcadas).
- **Diagrama de arquitetura** (fluxo WhatsApp → n8n → Manus → Supabase).
- Versão **prompt-ready** para ingestão direta na Manus (texto otimizado para memória longa).
- Versão **investidor/partner** com menos técnico e mais visão de produto.

Indique qual versão deseja evoluir a seguir.