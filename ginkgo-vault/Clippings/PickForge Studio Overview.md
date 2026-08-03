---
title: "PickForge Studio Overview"
source: "https://chatgpt.com/c/6a5ece60-19d4-83e9-993d-daf72177c3a6"
author:
published:
created: 2026-07-20
description: "ChatGPT conversation with 2 messages"
tags:
  - "clippings"
---
O projeto **[^1]** chamou atenção porque resolve um dos maiores gargalos do desenvolvimento com IA: reduzir o atrito entre identificar um problema na interface e enviar contexto suficiente para um agente corrigir o código. Toda a suíte é **local-first**, open source e voltada para quem usa agentes como Claude Code e Codex. [^1]

### Componentes da suíte

**1\. PickForge**

- Seleciona um widget diretamente na aplicação Flutter em execução.
- Envia automaticamente:
	- código-fonte;
		- árvore de componentes;
		- screenshot;
		- contexto para o agente.
- Fluxo: selecionar → IA altera → Hot Reload → repetir. [^1]

---

**2\. PickLab**  
É provavelmente a parte mais interessante.

Funciona como um laboratório para agentes.

- Android Emulator
- Desktop Linux
- Screenshots
- Clique
- Digitação
- Logs
- Playwright para aplicações nativas

Na prática, um agente pode **ver** e **interagir** com um aplicativo. [^1]

---

**3\. PickScribe**

Ditado totalmente local.

Pipeline:

voz → whisper.cpp → LLM corrige → cola no campo ativo.

Sem depender de serviços em nuvem. [^1]

---

**4\. PickGauge**

Monitora consumo de:

- Claude Code
- Codex

Mostra histórico de uso e estimativa da cota restante sem armazenar senhas. [^1]

---

**5\. PickArena**

Benchmark para modelos em tarefas reais de Flutter.

Avalia:

- compilação;
- testes ocultos;
- repetição de execuções;
- revisão humana.

Isso evita comparar modelos apenas por benchmarks sintéticos. [^1]

---

A ideia central é excelente: **reduzir o ciclo entre observação, decisão e execução**.

Na arquitetura da Ginkgo, isso poderia inspirar um módulo semelhante para além do Flutter.

```
Usuário
      │
      ▼
Tela/Web/App
      │
      ▼
Selecionar componente
      │
      ▼
Hermes
      │
      ├── Screenshot
      ├── DOM
      ├── Logs
      ├── Código
      ├── Git
      ├── Banco
      ├── Stack Trace
      └── Contexto RAG
      │
      ▼
Laplace valida
      │
      ▼
Claude / GPT / Gemini
      │
      ▼
Patch
      │
      ▼
Deploy de teste
      │
      ▼
Teste automático
      │
      ▼
Merge
```

Esse conceito poderia evoluir para um **Ginkgo Forge**, funcionando como uma camada universal para:

- Flutter
- React
- Next.js
- Lovable
- n8n
- Chatwoot
- Supabase
- Docker
- Mobile
- Dashboards internos

---

## Integração com Sylvia

Na arquitetura que você descreveu anteriormente, faz bastante sentido que a Sylvia seja a interface operacional desse processo:

- **Hermes** → coordena a tarefa.
- **Sylvia** → interpreta a interface e conversa com o desenvolvedor.
- **Laplace** → valida contexto, RAG e segurança.
- **Brann** → documenta automaticamente a alteração.
- **Alfred** → registra métricas e custos.

Assim, a IA deixa de apenas responder perguntas e passa a operar como um engenheiro com contexto completo.

---

## Avaliação

**Conceito:** 9,5/10

Pontos fortes:

- reduz drasticamente o contexto manual;
- arquitetura local-first;
- uso consistente de MCP;
- foco em produtividade real.

Limitações:

- atualmente é bastante centrado em Flutter;
- não cobre todo o ciclo DevOps;
- ainda depende de agentes externos para raciocínio e implementação.

Para a visão da Ginkgo, a oportunidade é ampliar esse conceito para um sistema multimodal e multiplataforma, capaz de inspecionar qualquer aplicação, reunir contexto automaticamente e acionar agentes especializados para corrigir, validar, testar e documentar mudanças em um fluxo único.

[^1]: [pickforge.dev](https://pickforge.dev/?utm_source=chatgpt.com)