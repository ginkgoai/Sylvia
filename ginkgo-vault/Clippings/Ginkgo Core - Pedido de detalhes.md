---
title: "Ginkgo Core - Pedido de detalhes"
source: "https://chatgpt.com/g/g-p-68e0a0b393cc8191a0f44ad743e1117d/c/69d0a1e1-2aec-83e9-9ef7-53e7f1f1e906"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sáb., 4 de abr. às 2:30

<iframe title="internal://deep-research" src="https://connector_openai_deep_research.web-sandbox.oaiusercontent.com/?app=chatgpt&amp;darkModeType=increased&amp;locale=pt-BR&amp;deviceType=desktop" allow="camera *; clipboard-read *; clipboard-write *; fullscreen *; local-network-access *; microphone *; web-share *" allowfullscreen=""></iframe>

## Documento de arquitetura — Ginkgo Agent OS

Baseado em padrões reaproveitáveis de mercado, com reconstrução própria e limpa.

---

## 1\. Visão central

A Ginkgo não deve ser um amontoado de bots.  
Deve ser um **sistema operacional de agentes**.

Pensa assim:

**LLM solto = mercenário**  
**Agente com memória, regras, ferramentas e telemetria = unidade de elite**

O objetivo é transformar Leaf, Wave e Pyre em módulos do mesmo núcleo.

---

## 2\. Princípio estrutural

## Núcleo da plataforma

Um núcleo único chamado:

**Ginkgo Agent OS**

Esse núcleo controla 6 camadas:

1. **Runtime de agentes**
2. **Sistema de memória**
3. **Barramento de ferramentas e integrações**
4. **Camada de permissões e governança**
5. **Telemetria, analytics e auditoria**
6. **Interfaces e canais**

---

## 3\. Bloco 1 — Core Runtime

Esse é o motor. O reator da nave.

## 3.1 Função

Executar agentes de forma padronizada, independente do canal.

Ou seja:

- o mesmo agente pode atuar no WhatsApp;
- no dashboard web;
- via API;
- no Telegram;
- em automações n8n;
- em painéis internos.

## 3.2 Componentes

### A. Agent Executor

Responsável por:

- receber input;
- carregar contexto;
- decidir fluxo;
- chamar ferramentas;
- montar resposta;
- registrar tudo.

### B. Session Manager

Controla:

- sessão atual;
- histórico curto;
- contexto ativo;
- identidade do usuário;
- tenant do cliente.

### C. Intent Router

Decide:

- qual agente atende;
- qual skill entra em ação;
- se precisa de humano;
- se é consulta, execução ou análise.

### D. Policy Engine

Aplica:

- limites;
- regras do cliente;
- guardrails;
- permissões por ação.

### E. Response Composer

Monta a resposta no formato ideal:

- texto curto;
- texto estruturado;
- áudio;
- JSON;
- relatório;
- tarefa;
- evento de calendário;
- ação no CRM.

---

## 4\. Como o Runtime deve funcionar

## Fluxo padrão

**Entrada → Normalização → Roteamento → Memória → Ferramentas → Resposta → Log**

Exemplo no Brann:

1. lead manda áudio no WhatsApp
2. sistema transcreve
3. detecta intenção
4. puxa contexto do lead
5. consulta catálogo / agenda / CRM
6. responde em texto ou áudio
7. registra tudo no histórico e analytics

Exemplo no Alfred:

1. usuário pede análise da campanha
2. Alfred puxa métricas
3. compara período
4. detecta gargalo
5. gera diagnóstico
6. recomenda ação
7. opcionalmente executa mudança com aprovação

---

## 5\. Bloco 2 — Memory System

Esse é o cérebro persistente. Sem isso, agente é peixe dourado com Wi-Fi.

## 5.1 Arquitetura de memória em camadas

### A. Org Memory

Memória global da Ginkgo.  
Contém:

- princípios da plataforma;
- regras globais;
- estilo institucional;
- padrões de segurança;
- taxonomia de agentes.

### B. Tenant Memory

Memória do cliente.  
Contém:

- dados da empresa;
- oferta;
- política comercial;
- horários;
- processos;
- identidade;
- canais;
- objetivos.

### C. Workspace Memory

Memória do produto/ambiente.  
Exemplo:

- Leaf de um cliente
- Wave da mesma empresa
- Pyre da mesma empresa

Cada workspace tem:

- configurações próprias;
- ferramentas próprias;
- base documental própria;
- metas próprias.

### D. Agent Memory

Memória da persona operacional.  
Exemplo:

- Brann sabe vender, qualificar e encaminhar
- Alfred sabe analisar, otimizar e reportar
- Nyra sabe criar, adaptar e publicar

### E. User Memory

Preferências do operador humano.  
Exemplo:

- formato de resposta favorito;
- dashboards preferidos;
- idioma;
- nível de detalhe;
- permissões especiais.

### F. Session Memory

Contexto de curtíssimo prazo.  
Exemplo:

- conversa atual;
- objetivo atual;
- arquivos recentes;
- ação em andamento.

---

## 6\. Tipos de memória

## 6.1 Memória operacional

Para ações rápidas:

- status de lead;
- etapa do funil;
- tarefa em aberto;
- campanha ativa.

## 6.2 Memória documental

Para consulta:

- PDFs;
- contratos;
- FAQs;
- playbooks;
- propostas;
- SOPs;
- briefings.

## 6.3 Memória comportamental

Para adaptação:

- perfil do cliente;
- tom preferido;
- gatilhos de decisão;
- padrões de uso;
- horários de interação.

## 6.4 Memória analítica

Para inteligência:

- métricas históricas;
- conversões;
- eficiência por agente;
- custo por operação;
- ROI por cliente.

---

## 7\. Estrutura técnica sugerida para memória

## Curto prazo

- **Redis** para contexto imediato e sessão

## Longo prazo estruturado

- **Postgres / Supabase** para registros persistentes

## Conhecimento semântico

- **Qdrant** ou vetores no Supabase para RAG

## Arquivos brutos

- **Supabase Storage** para documentos, áudios, imagens, vídeos

---

## 8\. Regras de ouro da memória

1. **Toda memória precisa de escopo**  
	Nada de contexto vazando entre clientes.
2. **Toda memória precisa de metadata**  
	Exemplo:
- tenant\_id
- agent\_id
- source
- created\_at
- updated\_at
- sensitivity
- confidence
3. **Toda memória precisa de política de retenção**  
	Nem tudo deve viver para sempre.
4. **Toda memória precisa de auditabilidade**  
	Quem gerou, quando, por quê, com base em quê.

---

## 9\. Bloco 3 — Agent OS / Sistema operacional de agentes

Esse é o que transforma ferramentas dispersas em plataforma.

## 9.1 Conceito

Cada agente da Ginkgo é uma combinação de:

**Persona + Skills + Memory + Tools + Policies + Analytics**

---

## 10\. Modelo de agente padrão

## Estrutura base

Cada agente deve ter:

### A. Identity Layer

Quem ele é.

- nome
- papel
- missão
- tom
- estilo
- limites

### B. Skill Layer

O que sabe fazer.

- qualificar lead
- gerar proposta
- montar relatório
- criar roteiro
- otimizar campanha

### C. Tool Layer

Quais ferramentas usa.

- WhatsApp
- Chatwoot
- Stripe
- Google Calendar
- Meta Ads
- ClickUp
- Supabase
- n8n
- Drive
- APIs externas

### D. Policy Layer

O que pode ou não pode fazer.

- pode enviar mensagem?
- pode mexer em campanha?
- pode cancelar evento?
- precisa de aprovação humana?
- pode acessar dado financeiro?

### E. Telemetry Layer

Como é medido.

- tempo de resposta
- taxa de execução
- conversão
- satisfação
- economia de horas
- custo por tarefa

---

## 11\. Padrão dos agentes da Ginkgo

## Brann

Papel:

- atendimento
- qualificação
- vendas
- agendamento
- handoff humano

Skills principais:

- lead scoring
- resposta FAQ
- interpretação de áudio
- envio de catálogo
- follow-up
- reativação

## Alfred

Papel:

- operações
- tráfego
- análise
- recomendações
- automação de decisões

Skills principais:

- leitura de métricas
- diagnóstico de campanha
- auditoria
- sugestão de otimização
- geração de relatório
- monitoramento contínuo

## Nyra

Papel:

- criação
- adaptação
- calendário
- publicação
- performance criativa

Skills principais:

- copy
- roteiro
- criativo
- legenda
- adaptação por canal
- agenda de postagem

---

## 12\. Tool Bus da Ginkgo

A Ginkgo precisa de um barramento padrão de ferramentas.

## 12.1 Função

Todo agente chama ferramentas do mesmo jeito.

Em vez de lógica espalhada, criar um padrão:

**tool\_name + permission\_scope + input\_schema + output\_schema + audit\_log**

## 12.2 Exemplo de conectores prioritários

- Evolution API
- Chatwoot
- Supabase
- Qdrant
- Stripe
- Google Calendar
- Google Drive / Docs
- ClickUp
- Meta Ads
- Blotato
- Email
- Webhook genérico

---

## 13\. Sistema de permissões

Aqui mora a diferença entre plataforma profissional e caos bonito.

## 13.1 Níveis de permissão

### Leitura

Pode consultar, mas não alterar.

### Sugestão

Pode propor ação, mas precisa de aprovação.

### Execução assistida

Pode executar com confirmação.

### Execução autônoma limitada

Pode agir dentro de regras.

### Execução autônoma ampla

Reservado para automações muito confiáveis.

## 13.2 Escopos

- por cliente
- por agente
- por usuário
- por ferramenta
- por tipo de ação

---

## 14\. Telemetria e analytics

Se não mede, vira culto. Se mede, vira empresa.

## 14.1 Métricas obrigatórias

- mensagens recebidas
- mensagens resolvidas
- tempo médio de resposta
- tempo economizado
- taxa de handoff
- conversão por canal
- custo por conversa
- custo por automação
- uso por cliente
- falhas por integração

## 14.2 Métricas avançadas

- ROI por agente
- receita influenciada
- gargalos operacionais recorrentes
- skills mais usadas
- taxa de sucesso por tool
- custo por tipo de tarefa

---

## 15\. Interfaces da plataforma

## Dashboard Ginkgo

Painel central com:

- visão de clientes
- agentes ativos
- uso mensal
- custos
- alertas
- status das integrações

## Painel do cliente

Versão simplificada:

- atendimentos
- leads
- tarefas
- campanhas
- conteúdos
- métricas de ROI

## Interfaces conversacionais

- WhatsApp
- Telegram
- web chat
- painel interno
- API

---

## 16\. Roadmap de implementação

## Fase 1 — Foundation

Construir:

- runtime unificado
- memória hierárquica
- tool bus básico
- policy engine simples
- analytics básicos

Entrega prática:

- Brann sólido no WhatsApp
- Alfred lendo dados
- Nyra gerando conteúdo com memória de marca

## Fase 2 — Productization

Construir:

- dashboard por tenant
- gestão de permissões
- skills configuráveis
- onboarding padronizado
- audit log completo

Entrega prática:

- Leaf, Wave e Pyre já como produtos visíveis

## Fase 3 — Intelligence Layer

Construir:

- subagentes
- monitoramento contínuo
- alertas automáticos
- recomendações proativas
- otimização assistida por histórico

Entrega prática:

- Alfred começa a agir como operador sempre atento
- Nyra vira motor criativo contínuo
- Brann melhora com loops de aprendizado operacional

---

## 17\. O que eu faria primeiro na Ginkgo

Ordem cirúrgica:

## Sprint 1

- definir modelo único de agente
- definir modelo único de memória
- definir modelo único de ferramenta
- definir modelo único de log

## Sprint 2

- plugar Brann nesse padrão
- separar sessão, memória e tools
- criar skills formais
- medir tudo

## Sprint 3

- replicar o mesmo padrão no Alfred
- depois Nyra
- depois dashboard multi-tenant

---

## 18\. Estrutura-resumo da arquitetura

## Core Runtime

Motor de execução padronizado para todos os agentes

## Memory System

Memória hierárquica, multi-tenant, rastreável

## Agent OS

Sistema que organiza identidade, skills, tools, policies e métricas

## Tool Bus

Barramento de integrações unificado

## Policy Engine

Controle de permissões, risco e governança

## Analytics Layer

Prova de valor, custo e performance

---

## 19\. Decisão estratégica final

A Ginkgo não precisa copiar uma ferramenta.  
Precisa construir a própria infraestrutura com lógica de elite.

O alvo não é “ter um Claude Code brasileiro”.  
O alvo é:

**ter um sistema operacional de agentes que controla atendimento, conteúdo e operações como uma central de comando.**

Claude mostrou uma direção.  
A Ginkgo pode transformar isso em ecossistema.

Se quiser, no próximo passo eu transformo isso em um **PRD técnico completo da Ginkgo Agent OS**, com:

- arquitetura de módulos,
- schema inicial de banco,
- entidades principais,
- e backlog MVP em formato de build.

```markdown
# PRD Técnico — Ginkgo Agent OS

## 1. Visão do produto

O **Ginkgo Agent OS** é a camada central que transforma os agentes da Ginkgo em uma infraestrutura operacional unificada, multi-tenant, auditável e expansível.

Ele existe para sustentar:

- **Leaf** → atendimento, vendas, CRM conversacional
- **Wave** → operações, tráfego, análise, execução
- **Pyre** → criação de conteúdo, calendário, publicação, performance criativa

A proposta não é criar “mais um bot”.

A proposta é criar um **sistema operacional de agentes**, onde cada agente funciona como um módulo inteligente com:

- identidade
- memória
- skills
- ferramentas
- permissões
- telemetria

---

## 2. Objetivo principal

Construir uma base única para que qualquer agente da Ginkgo possa:

1. receber inputs de múltiplos canais
2. entender contexto e intenção
3. acessar memória e conhecimento
4. usar ferramentas com segurança
5. executar ações
6. responder no formato ideal
7. registrar tudo para auditoria, analytics e melhoria contínua

---

## 3. Problema que resolve

Hoje, plataformas com agentes costumam sofrer de cinco doenças clássicas:

### 3.1 Fragmentação
Cada agente nasce como uma gambiarra isolada:
- prompt solto
- webhook solto
- tabela solta
- memória improvisada
- lógica espalhada

### 3.2 Falta de governança
O agente até “funciona”, mas:
- ninguém sabe o que ele pode fazer
- ninguém sabe quem autorizou
- ninguém sabe por que respondeu daquele jeito

### 3.3 Memória ruim
Sem memória hierárquica:
- o agente esquece contexto
- mistura informações
- não respeita escopo por cliente
- vira um oráculo com amnésia

### 3.4 Integrações caóticas
Cada integração nasce diferente:
- payload diferente
- autenticação diferente
- logs inexistentes
- sem camada de permissão

### 3.5 Sem prova de valor
Sem analytics:
- não dá para medir ROI
- não dá para provar economia
- não dá para vender recorrência com clareza

---

## 4. Objetivo de negócio

O Ginkgo Agent OS deve permitir que a Ginkgo:

- reduza o tempo de criação de novos agentes
- replique arquitetura entre clientes com rapidez
- aumente previsibilidade operacional
- reduza risco técnico e jurídico
- venda produto recorrente com telemetria e ROI visível
- padronize atendimento, conteúdo e operações em uma única base

---

## 5. Escopo do MVP

O MVP do Ginkgo Agent OS inclui:

- runtime unificado de agentes
- memória hierárquica multi-tenant
- barramento de ferramentas padronizado
- camada de permissões
- auditoria de ações
- analytics básicos
- suporte inicial a Brann, Alfred e Nyra
- suporte aos canais e integrações prioritários

Não inclui no MVP:

- auto-otimização completa
- fine-tuning dedicado por cliente
- subagentes avançados
- recomendação proativa contínua em background
- orchestration complexa entre múltiplos agentes simultâneos

---

## 6. Princípios do sistema

### 6.1 Multi-tenant por padrão
Nada pode vazar entre clientes.

### 6.2 Agent-first, mas infra-first
O foco parece ser o agente, mas a vantagem competitiva está na infraestrutura.

### 6.3 Toda ação precisa ser rastreável
Sem trilha de auditoria, não existe operação séria.

### 6.4 Ferramentas devem ser plugáveis
Conectores precisam seguir o mesmo contrato.

### 6.5 O canal não define o cérebro
WhatsApp, dashboard, Telegram ou API devem reutilizar o mesmo core.

### 6.6 Resposta não é o fim
Cada interação deve alimentar:
- memória
- analytics
- melhoria operacional
- contexto futuro

---

## 7. Arquitetura lógica

\`\`\`text
[Canais]
  ├─ WhatsApp
  ├─ Dashboard Web
  ├─ Telegram
  ├─ API
  └─ Webchat

        ↓

[Input Normalizer]
        ↓
[Intent Router]
        ↓
[Policy Engine]
        ↓
[Agent Runtime]
        ├─ Memory Loader
        ├─ Skill Resolver
        ├─ Tool Executor
        ├─ Response Composer
        └─ Audit Logger

        ↓

[Memory System]
  ├─ Session Memory
  ├─ User Memory
  ├─ Agent Memory
  ├─ Workspace Memory
  ├─ Tenant Memory
  └─ Org Memory

        ↓

[Tool Bus]
  ├─ Evolution API
  ├─ Chatwoot
  ├─ Supabase
  ├─ Qdrant
  ├─ Stripe
  ├─ Google Calendar
  ├─ Google Drive
  ├─ ClickUp
  ├─ Meta Ads
  └─ Webhooks

        ↓

[Analytics + Audit + Observability]
```

---

## 8\. Módulos do sistema

## 8.1 Core Runtime

### Responsabilidade

Executar agentes de forma padronizada.

### Funções

- receber input estruturado
- montar contexto
- identificar agente e skill
- aplicar políticas
- chamar ferramentas
- gerar resposta
- registrar execução

### Inputs esperados

- tenant\_id
- workspace\_id
- agent\_id
- user\_id ou contact\_id
- canal
- mensagem/evento
- arquivos anexos
- metadados do contexto

### Outputs esperados

- resposta ao usuário
- ações executadas
- logs
- métricas
- eventos para memória

---

## 8.2 Input Normalizer

### Responsabilidade

Transformar qualquer entrada em um formato comum.

### Deve normalizar

- texto
- áudio transcrito
- imagem com OCR/visão quando necessário
- documentos
- eventos de sistema
- cliques em dashboard
- chamadas API

### Output padrão sugerido

```markdown
{
  "event_type": "message.received",
  "channel": "whatsapp",
  "tenant_id": "t_123",
  "workspace_id": "w_leaf_1",
  "agent_id": "brann",
  "actor_id": "contact_456",
  "message": {
    "type": "text",
    "content": "Quero saber o preço"
  },
  "attachments": [],
  "timestamp": "2026-04-04T16:00:00Z"
}
```

---

## 8.3 Intent Router

### Responsabilidade

Decidir qual fluxo deve ser ativado.

### Pode decidir

- qual agente responde
- qual skill executar
- se precisa consultar memória
- se precisa chamar ferramenta
- se deve encaminhar para humano
- se a ação é bloqueada pela policy

### Exemplo

Mensagem:

> “Quero agendar uma reunião amanhã”

Roteamento:

- agente: Brann
- skill: `schedule_meeting`
- tools: Google Calendar
- policy: execução assistida

---

## 8.4 Policy Engine

### Responsabilidade

Aplicar regras operacionais, de segurança e de governança.

### Deve validar

- escopo do tenant
- permissões do agente
- permissões do operador
- sensibilidade da ação
- necessidade de confirmação
- limite por canal
- limite por ferramenta

### Níveis de permissão

- `read`
- `suggest`
- `confirm_required`
- `limited_autonomous_execution`
- `full_autonomous_execution`

### Exemplo

Alfred pode:

- ler métricas do Meta Ads
- sugerir mudança de campanha
- pausar campanha somente com confirmação humana

---

## 8.5 Skill Resolver

### Responsabilidade

Mapear intenção para capacidades executáveis.

### Exemplo de skills

#### Brann

- qualify\_lead
- answer\_faq
- send\_catalog
- schedule\_visit
- follow\_up\_lead
- handoff\_to\_human

#### Alfred

- fetch\_campaign\_metrics
- diagnose\_campaign
- generate\_report
- suggest\_budget\_shift
- create\_ops\_task

#### Nyra

- generate\_copy
- create\_content\_plan
- adapt\_post\_for\_channel
- generate\_caption
- schedule\_content

---

## 8.6 Tool Bus

### Responsabilidade

Padronizar a comunicação com integrações externas.

### Contrato da ferramenta

Cada ferramenta deve expor:

- `tool_name`
- `description`
- `permission_scope`
- `input_schema`
- `output_schema`
- `timeout`
- `retry_policy`
- `audit_level`

### Exemplo de contrato

```markdown
{
  "tool_name": "google_calendar.create_event",
  "permission_scope": "calendar.write",
  "input_schema": {
    "title": "string",
    "start_at": "datetime",
    "end_at": "datetime",
    "attendees": "array"
  },
  "output_schema": {
    "event_id": "string",
    "event_url": "string"
  },
  "audit_level": "high"
}
```

---

## 8.7 Response Composer

### Responsabilidade

Transformar o resultado da execução em resposta útil.

### Formatos possíveis

- texto curto
- texto estruturado
- markdown
- JSON
- áudio
- relatório
- card de dashboard
- tarefa criada
- evento criado
- mensagem de confirmação

### Regras

- adaptar ao canal
- respeitar o tom do agente
- evitar verbosidade desnecessária
- destacar CTA principal
- registrar versão final enviada

---

## 8.8 Audit Logger

### Responsabilidade

Registrar tudo o que teve impacto operacional.

### Deve guardar

- input bruto e normalizado
- decisão de roteamento
- memória consultada
- ferramentas usadas
- outputs
- ação executada
- confirmação humana
- falhas
- timestamps
- custo estimado

---

## 8.9 Analytics Layer

### Responsabilidade

Transformar operações em métricas de produto e negócio.

### Métricas básicas

- volume de mensagens
- tempo médio de resposta
- taxa de resolução
- taxa de handoff
- skills mais usadas
- falhas por integração
- uso por cliente

### Métricas de valor

- leads qualificados
- reuniões agendadas
- conversões influenciadas
- tarefas executadas
- conteúdos publicados
- horas economizadas
- custo operacional por fluxo

---

## 9\. Sistema de Memória

## 9.1 Estrutura hierárquica

### Org Memory

Memória global da Ginkgo.

Contém:

- regras institucionais
- padrões de resposta
- políticas de segurança
- taxonomia dos agentes
- padrões globais de tool usage

### Tenant Memory

Memória do cliente.

Contém:

- nome da empresa
- oferta
- horários
- políticas internas
- posicionamento
- preferências comerciais
- dados de operação

### Workspace Memory

Memória do produto/ambiente.

Exemplos:

- Leaf do Cliente A
- Wave do Cliente A
- Pyre do Cliente A

### Agent Memory

Memória da função do agente.

Exemplos:

- Brann: vendas, atendimento, qualificação
- Alfred: tráfego, relatório, operações
- Nyra: criação, adaptação, calendário

### User Memory

Memória do operador humano.

Contém:

- preferências de visualização
- idioma
- formato de relatório
- nível de autonomia permitido

### Session Memory

Contexto imediato.

Contém:

- conversa atual
- objetivo atual
- últimos eventos
- arquivos recentes
- estado temporário do fluxo

---

## 9.2 Tipos de memória

### Memória relacional

Para entidades:

- clientes
- leads
- campanhas
- tarefas
- conteúdos
- usuários
- agendamentos

### Memória documental

Para:

- contratos
- SOPs
- briefings
- FAQs
- PDFs
- documentos internos

### Memória vetorial

Para:

- recuperação semântica
- RAG
- contexto baseado em similaridade

### Memória efêmera

Para:

- fluxo atual
- checkpoint de execução
- variáveis de curto prazo

---

## 9.3 Stack sugerida

### Redis

Uso:

- sessão
- cache
- estado efêmero
- locks

### Postgres / Supabase

Uso:

- entidades principais
- logs
- auditoria
- configuração
- analytics brutos

### Qdrant ou Supabase Vector

Uso:

- embeddings
- RAG
- busca semântica

### Supabase Storage

Uso:

- PDFs
- imagens
- áudios
- vídeos
- anexos operacionais

---

## 10\. Entidades principais

## 10.1 Tenant

Representa a empresa cliente.

### Campos

- id
- name
- slug
- status
- plan
- timezone
- created\_at
- updated\_at

---

## 10.2 Workspace

Representa um ambiente/produto dentro do tenant.

### Campos

- id
- tenant\_id
- type (`leaf`, `wave`, `pyre`, `ops`)
- name
- status
- config\_json
- created\_at
- updated\_at

---

## 10.3 Agent

Representa o agente configurado.

### Campos

- id
- workspace\_id
- name
- code\_name
- role
- persona\_prompt
- system\_rules
- status
- autonomy\_level
- created\_at
- updated\_at

---

## 10.4 Skill

Representa uma capacidade do agente.

### Campos

- id
- agent\_id
- name
- description
- input\_schema
- output\_schema
- requires\_confirmation
- status
- created\_at
- updated\_at

---

## 10.5 Tool

Representa uma integração disponível.

### Campos

- id
- tenant\_id
- workspace\_id
- tool\_name
- provider
- config\_json
- auth\_ref
- status
- created\_at
- updated\_at

---

## 10.6 Policy

Representa regra de execução.

### Campos

- id
- tenant\_id
- workspace\_id
- agent\_id
- scope
- action
- permission\_level
- conditions\_json
- created\_at
- updated\_at

---

## 10.7 Contact

Representa lead, cliente ou interlocutor.

### Campos

- id
- tenant\_id
- external\_ref
- name
- phone
- email
- tags
- stage
- owner\_user\_id
- metadata\_json
- created\_at
- updated\_at

---

## 10.8 Conversation

Representa sessão conversacional.

### Campos

- id
- tenant\_id
- workspace\_id
- agent\_id
- contact\_id
- channel
- status
- started\_at
- closed\_at
- metadata\_json

---

## 10.9 Message

Representa mensagem trocada.

### Campos

- id
- conversation\_id
- sender\_type
- sender\_id
- message\_type
- content
- raw\_payload
- token\_usage\_json
- created\_at

---

## 10.10 Memory Entry

Representa memória persistida.

### Campos

- id
- tenant\_id
- workspace\_id
- agent\_id
- user\_id
- session\_id
- memory\_scope
- memory\_type
- title
- content
- embedding\_ref
- metadata\_json
- sensitivity
- created\_at
- updated\_at

---

## 10.11 Tool Execution

Representa chamada de ferramenta.

### Campos

- id
- tenant\_id
- workspace\_id
- agent\_id
- tool\_name
- input\_json
- output\_json
- status
- duration\_ms
- error\_message
- audit\_level
- created\_at

---

## 10.12 Audit Event

Representa evento auditável.

### Campos

- id
- tenant\_id
- workspace\_id
- agent\_id
- actor\_type
- actor\_id
- event\_type
- event\_payload
- risk\_level
- created\_at

---

## 10.13 Metric Event

Representa evento analítico.

### Campos

- id
- tenant\_id
- workspace\_id
- agent\_id
- metric\_name
- metric\_value
- dimension\_json
- created\_at

---

## 11\. Schema inicial de banco

## 11.1 Tabelas núcleo

- tenants
- workspaces
- agents
- skills
- tools
- policies
- users
- contacts
- conversations
- messages

## 11.2 Tabelas de inteligência

- memory\_entries
- documents
- document\_chunks
- embeddings\_index

## 11.3 Tabelas operacionais

- tool\_executions
- audit\_events
- metric\_events
- scheduled\_jobs
- approvals

## 11.4 Tabelas de configuração

- channel\_configs
- workspace\_configs
- agent\_configs
- feature\_flags

---

## 12\. Fluxos principais do MVP

## 12.1 Fluxo A — Atendimento do Brann

### Entrada

Lead envia mensagem no WhatsApp.

### Etapas

1. mensagem chega via Evolution API
2. Input Normalizer converte para formato padrão
3. Intent Router identifica intenção
4. Session Memory carrega contexto curto
5. Tenant Memory carrega contexto de negócio
6. Brann skill é selecionada
7. Policy Engine valida ação
8. Tool Bus chama CRM, agenda ou catálogo se necessário
9. Response Composer monta resposta
10. Audit Logger registra tudo
11. Analytics recebe eventos

### Saídas possíveis

- resposta textual
- resposta em áudio
- agendamento
- lead qualificado
- handoff para humano
- atualização no CRM

---

## 12.2 Fluxo B — Análise do Alfred

### Entrada

Usuário solicita análise de campanha.

### Etapas

1. input chega via dashboard ou chat
2. runtime identifica Alfred
3. skill `diagnose_campaign` é acionada
4. tool `meta_ads.fetch_metrics` é chamada
5. memória histórica é consultada
6. Alfred compara períodos e detecta anomalias
7. Response Composer gera relatório
8. Policy Engine decide se só sugere ou executa
9. auditoria registra recomendação

### Saídas possíveis

- diagnóstico
- alerta
- sugestão de otimização
- criação de tarefa
- ação dependente de confirmação

---

## 12.3 Fluxo C — Produção da Nyra

### Entrada

Usuário pede calendário de conteúdo.

### Etapas

1. runtime identifica workspace Pyre
2. memory de marca é carregada
3. skill `create_content_plan` é acionada
4. documentos e histórico recente são consultados
5. Nyra monta plano por canal
6. Response Composer entrega calendário
7. opcionalmente chama ferramenta de agendamento

### Saídas possíveis

- calendário
- roteiros
- copies
- legendas
- conteúdos agendados

---

## 13\. Requisitos funcionais

## 13.1 Runtime

- deve suportar múltiplos agentes
- deve suportar múltiplos canais
- deve isolar tenants
- deve registrar cada execução

## 13.2 Memória

- deve suportar escopos hierárquicos
- deve permitir persistência de memória relevante
- deve diferenciar memória efêmera e persistente
- deve permitir RAG por workspace

## 13.3 Ferramentas

- deve padronizar chamadas de integração
- deve aplicar permissão antes da execução
- deve registrar input/output de forma auditável
- deve suportar retry e timeout

## 13.4 Permissões

- deve permitir permissão por agente, tool e ação
- deve suportar execução assistida
- deve permitir bloqueio por risco

## 13.5 Analytics

- deve coletar eventos de uso
- deve calcular métricas por tenant e workspace
- deve suportar dashboards básicos

---

## 14\. Requisitos não funcionais

### Segurança

- isolamento por tenant obrigatório
- credenciais separadas por cliente quando aplicável
- logs de alto risco protegidos
- políticas de retenção de dados

### Escalabilidade

- arquitetura preparada para múltiplos workspaces por tenant
- execução assíncrona para tarefas longas
- filas para processamento pesado

### Observabilidade

- logs estruturados
- tracing por execução
- alertas de falha
- monitoramento por integração

### Performance

- resposta rápida para interações simples
- recuperação de memória eficiente
- cache para contexto frequente

### Manutenibilidade

- skills versionadas
- tools desacopladas
- configs por ambiente
- prompts e regras versionáveis

---

## 15\. Integrações prioritárias do MVP

### Canal

- Evolution API
- Chatwoot

### Dados

- Supabase
- Redis
- Qdrant

### Agenda

- Google Calendar

### Conteúdo e operação

- ClickUp
- Google Drive / Docs

### Comercial

- Stripe

### Mídia paga

- Meta Ads

### Orquestração

- n8n

---

## 16\. Backlog MVP por blocos

## Bloco A — Foundation

- definir contrato padrão de agent runtime
- definir contrato de tool
- definir contrato de memory entry
- criar tabelas núcleo
- criar pipeline de audit log
- criar métrica mínima por execução

## Bloco B — Brann First

- conectar Evolution API
- criar normalizador de mensagens
- criar skills básicas do Brann
- integrar agenda
- integrar CRM/base de leads
- registrar handoff humano

## Bloco C — Memory System

- Redis para sessão
- Supabase/Postgres para persistência
- storage para anexos
- pipeline de embeddings
- retrieval por tenant/workspace

## Bloco D — Policy + Governance

- matriz de permissões
- execução com confirmação
- log de aprovações
- bloqueio de ações sensíveis

## Bloco E — Analytics MVP

- métricas de volume
- métricas de tempo de resposta
- métricas de resolução
- métricas por skill
- dashboard básico

## Bloco F — Alfred + Nyra

- onboarding de Alfred no mesmo runtime
- onboarding de Nyra no mesmo runtime
- ferramentas específicas
- relatórios e outputs padronizados

---

## 17\. Roadmap de entrega

## Fase 1 — Infra mínima funcional

Objetivo:  
colocar o esqueleto em pé.

Entrega:

- tabelas centrais
- runtime mínimo
- tool bus inicial
- memória curta + persistente
- logs + analytics básicos

## Fase 2 — Brann operacional

Objetivo:  
usar o Ginkgo Agent OS em produção real com atendimento.

Entrega:

- WhatsApp
- qualificação
- FAQ
- agendamento
- CRM
- handoff humano

## Fase 3 — Dashboard e governança

Objetivo:  
dar visibilidade operacional e controle.

Entrega:

- painel básico
- auditoria navegável
- permissões
- aprovação de ações

## Fase 4 — Expansão multiagente

Objetivo:  
usar o mesmo core para Alfred e Nyra.

Entrega:

- skills específicas
- workflows por produto
- analytics por produto

---

## 18\. Critérios de sucesso do MVP

O MVP será considerado bem-sucedido se:

- Brann operar sobre o runtime único
- memória por tenant funcionar sem vazamento
- ao menos 5 skills estiverem operacionais
- ao menos 5 integrações estiverem plugadas no Tool Bus
- ações auditáveis estiverem registradas corretamente
- dashboard mostrar métricas mínimas por cliente
- a mesma base permitir onboarding inicial de Alfred e Nyra

---

## 19\. Riscos principais

### Risco 1 — Complexidade excessiva cedo demais

Mitigação:  
focar no Brann como trilho inicial.

### Risco 2 — Memória mal escopada

Mitigação:  
tenant\_id e workspace\_id obrigatórios em toda camada.

### Risco 3 — Integrações virarem caos

Mitigação:  
tool contract rígido e auditável.

### Risco 4 — Prompts descontrolados

Mitigação:  
versionamento e separação entre persona, skill e policy.

### Risco 5 — Sem prova de valor

Mitigação:  
analytics desde o primeiro fluxo.

---

## 20\. Decisão técnica recomendada

### Backend

- FastAPI ou Node.js
- workers assíncronos para jobs longos

### Banco

- Supabase/Postgres

### Sessão e cache

- Redis

### Vetores

- Qdrant ou Supabase Vector

### Storage

- Supabase Storage

### Orquestração

- n8n

### Painel

- Next.js / Lovable depois como camada visual

---

## 21\. Resumo executivo final

O **Ginkgo Agent OS** deve nascer como a base única da inteligência operacional da Ginkgo.

Ele não é apenas uma feature.

Ele é o **núcleo que padroniza**:

- agentes
- memória
- ferramentas
- permissões
- auditoria
- analytics

Se isso for bem construído, a Ginkgo deixa de vender automações soltas e passa a vender um ecossistema replicável, mensurável e escalável.

Em termos simples:

- **Brann** vira a face comercial
- **Alfred** vira o cérebro operacional
- **Nyra** vira o motor criativo
- **Ginkgo Agent OS** vira a usina que mantém tudo vivo

---

## 22\. Próximo documento recomendado

Depois deste PRD, o próximo artefato ideal é:

### Documento 2 — Schema SQL inicial + entidades relacionais

com:

- tabelas
- colunas
- tipos
- chaves
- índices
- relações

### Documento 3 — Arquitetura de APIs e contratos

com:

- endpoints
- payloads
- autenticação
- eventos
- webhooks

### Documento 4 — Backlog técnico por sprints

com:

- sprint 1
- sprint 2
- sprint 3
- critérios de aceite
- dependências
```markdown
Se quiser, eu converto isso agora em um **README de repositório técnico**, mais seco e pronto para colar no projeto.
```

Sim

```markdown
# Ginkgo Agent OS

Infraestrutura central de agentes da Ginkgo AI Systems.

O **Ginkgo Agent OS** é o núcleo técnico que padroniza a execução de agentes, memória operacional, integrações, permissões, auditoria e analytics dentro da plataforma Ginkgo.

Ele sustenta os produtos:

- **Leaf** → atendimento, vendas, CRM conversacional
- **Wave** → operações, análise, tráfego e execução
- **Pyre** → criação, calendário, publicação e performance criativa

---

## Objetivo

Criar uma base única para que qualquer agente da Ginkgo possa:

- receber eventos de múltiplos canais
- entender contexto e intenção
- consultar memória e conhecimento
- usar ferramentas com segurança
- executar ações
- responder no formato ideal
- registrar tudo para auditoria e analytics

---

## Visão

A Ginkgo não deve operar como um conjunto de bots soltos.

Deve operar como um **sistema operacional de agentes**.

Cada agente é tratado como uma unidade padronizada composta por:

- identidade
- skills
- memória
- tools
- policies
- telemetria

---

## Escopo

O repositório do Ginkgo Agent OS cobre:

- runtime unificado de agentes
- sistema de memória hierárquica
- barramento de integrações
- engine de permissões
- trilha de auditoria
- analytics operacionais
- contratos internos de agentes, skills e ferramentas

Não é objetivo deste núcleo:

- servir como frontend principal do cliente
- concentrar lógica de UI específica de cada produto
- depender de um único canal
- funcionar como prompt solto sem governança

---

## Arquitetura lógica

\`\`\`text
[Canais]
  ├─ WhatsApp
  ├─ Dashboard Web
  ├─ Telegram
  ├─ API
  └─ Webchat

        ↓

[Input Normalizer]
        ↓
[Intent Router]
        ↓
[Policy Engine]
        ↓
[Agent Runtime]
        ├─ Memory Loader
        ├─ Skill Resolver
        ├─ Tool Executor
        ├─ Response Composer
        └─ Audit Logger

        ↓

[Memory System]
  ├─ Session Memory
  ├─ User Memory
  ├─ Agent Memory
  ├─ Workspace Memory
  ├─ Tenant Memory
  └─ Org Memory

        ↓

[Tool Bus]
  ├─ Evolution API
  ├─ Chatwoot
  ├─ Supabase
  ├─ Qdrant
  ├─ Stripe
  ├─ Google Calendar
  ├─ Google Drive
  ├─ ClickUp
  ├─ Meta Ads
  └─ Webhooks

        ↓

[Analytics + Audit + Observability]
```

---

## Princípios

### 1\. Multi-tenant por padrão

Nenhum dado pode vazar entre clientes.

### 2\. Canal desacoplado do cérebro

WhatsApp, web, dashboard e API reutilizam o mesmo core.

### 3\. Toda ação relevante deve ser auditável

Sem rastreabilidade, não existe operação séria.

### 4\. Toda ferramenta deve seguir contrato

Integração sem padrão vira sabotagem futura.

### 5\. Memória precisa de escopo

Toda memória deve carregar tenant, workspace, agente e contexto.

### 6\. Analytics desde o início

Sem medição, o produto vira misticismo com webhook.

---

## Módulos centrais

## 1\. Core Runtime

Responsável por:

- receber input estruturado
- carregar contexto e memória
- identificar agente e skill
- aplicar políticas
- acionar ferramentas
- compor resposta
- registrar execução

### Responsabilidades

- execução padronizada
- isolamento por tenant
- suporte multiagente
- suporte multicanal
- rastreabilidade completa

---

## 2\. Input Normalizer

Transforma entradas heterogêneas em um formato comum.

### Tipos suportados

- texto
- áudio transcrito
- imagem
- documento
- evento de sistema
- clique em dashboard
- requisição de API

### Exemplo de payload normalizado

```markdown
{
  "event_type": "message.received",
  "channel": "whatsapp",
  "tenant_id": "t_123",
  "workspace_id": "w_leaf_1",
  "agent_id": "brann",
  "actor_id": "contact_456",
  "message": {
    "type": "text",
    "content": "Quero saber o preço"
  },
  "attachments": [],
  "timestamp": "2026-04-04T16:00:00Z"
}
```

---

## 3\. Intent Router

Decide:

- qual agente atende
- qual skill deve ser acionada
- se há necessidade de tool call
- se há necessidade de consulta à memória
- se o caso precisa de humano
- se a policy permite a ação

---

## 4\. Policy Engine

Controla governança e segurança operacional.

### Níveis de permissão

- `read`
- `suggest`
- `confirm_required`
- `limited_autonomous_execution`
- `full_autonomous_execution`

### Exemplos de validação

- escopo do tenant
- sensibilidade da ação
- permissão por ferramenta
- permissão por agente
- confirmação humana obrigatória
- limites por canal

---

## 5\. Skill Resolver

Mapeia intenções para capacidades executáveis.

### Exemplos de skills

#### Brann

- `qualify_lead`
- `answer_faq`
- `send_catalog`
- `schedule_visit`
- `follow_up_lead`
- `handoff_to_human`

#### Alfred

- `fetch_campaign_metrics`
- `diagnose_campaign`
- `generate_report`
- `suggest_budget_shift`
- `create_ops_task`

#### Nyra

- `generate_copy`
- `create_content_plan`
- `adapt_post_for_channel`
- `generate_caption`
- `schedule_content`

---

## 6\. Tool Bus

Padroniza o uso de integrações externas.

Cada ferramenta deve expor contrato explícito.

### Contrato mínimo

- `tool_name`
- `description`
- `permission_scope`
- `input_schema`
- `output_schema`
- `timeout`
- `retry_policy`
- `audit_level`

### Exemplo

```markdown
{
  "tool_name": "google_calendar.create_event",
  "permission_scope": "calendar.write",
  "input_schema": {
    "title": "string",
    "start_at": "datetime",
    "end_at": "datetime",
    "attendees": "array"
  },
  "output_schema": {
    "event_id": "string",
    "event_url": "string"
  },
  "audit_level": "high"
}
```

---

## 7\. Response Composer

Monta a saída final de forma compatível com o canal e com o agente.

### Formatos possíveis

- texto curto
- markdown
- JSON
- áudio
- relatório
- tarefa criada
- evento criado
- confirmação operacional

### Regras

- respeitar tom do agente
- respeitar canal
- ser objetivo
- destacar a ação principal
- registrar o output final

---

## 8\. Audit Logger

Registra tudo o que teve impacto operacional.

### Deve registrar

- input bruto
- input normalizado
- decisão de roteamento
- memória consultada
- skill escolhida
- ferramentas chamadas
- outputs
- confirmação humana
- falhas
- timestamps
- custo estimado

---

## 9\. Analytics Layer

Transforma uso operacional em métricas de produto e negócio.

### Métricas básicas

- volume de mensagens
- tempo médio de resposta
- taxa de resolução
- taxa de handoff
- skills mais usadas
- falhas por integração
- uso por tenant

### Métricas de valor

- leads qualificados
- reuniões agendadas
- conversões influenciadas
- tarefas executadas
- conteúdos publicados
- horas economizadas
- custo operacional por fluxo

---

## Sistema de memória

A memória do Ginkgo Agent OS é hierárquica e multi-tenant.

## Camadas de memória

### Org Memory

Regras e padrões globais da Ginkgo.

### Tenant Memory

Dados, políticas e contexto do cliente.

### Workspace Memory

Contexto do produto ou ambiente específico.

Exemplos:

- Leaf do Cliente A
- Wave do Cliente A
- Pyre do Cliente A

### Agent Memory

Contexto funcional do agente.

Exemplos:

- Brann = atendimento e venda
- Alfred = operações e análise
- Nyra = conteúdo e criatividade

### User Memory

Preferências do operador humano.

### Session Memory

Contexto efêmero da conversa ou execução atual.

---

## Tipos de memória

### Relacional

Para entidades estruturadas:

- clientes
- leads
- campanhas
- tarefas
- agendamentos
- conteúdos

### Documental

Para:

- SOPs
- FAQs
- briefings
- contratos
- PDFs
- playbooks

### Vetorial

Para:

- RAG
- recuperação semântica
- contexto por similaridade

### Efêmera

Para:

- sessão
- fluxo atual
- variáveis temporárias
- checkpoints

---

## Stack sugerida

### Persistência principal

- Postgres / Supabase

### Sessão e cache

- Redis

### Busca vetorial

- Qdrant ou Supabase Vector

### Arquivos

- Supabase Storage

### Orquestração

- n8n

### Runtime / API

- FastAPI ou Node.js

---

## Entidades principais

### Tenant

Representa a empresa cliente.

### Workspace

Representa um ambiente do tenant:

- Leaf
- Wave
- Pyre
- Ops

### Agent

Representa o agente configurado.

### Skill

Representa uma capacidade executável do agente.

### Tool

Representa uma integração disponível.

### Policy

Representa regras de execução e governança.

### Contact

Representa lead, cliente ou interlocutor.

### Conversation

Representa sessão conversacional.

### Message

Representa mensagem trocada.

### Memory Entry

Representa memória persistida.

### Tool Execution

Representa chamada de integração.

### Audit Event

Representa evento auditável.

### Metric Event

Representa evento analítico.

---

## Estrutura de tabelas esperadas

### Núcleo

- `tenants`
- `workspaces`
- `agents`
- `skills`
- `tools`
- `policies`
- `users`
- `contacts`
- `conversations`
- `messages`

### Inteligência

- `memory_entries`
- `documents`
- `document_chunks`
- `embeddings_index`

### Operacional

- `tool_executions`
- `audit_events`
- `metric_events`
- `scheduled_jobs`
- `approvals`

### Configuração

- `channel_configs`
- `workspace_configs`
- `agent_configs`
- `feature_flags`

---

## Fluxos prioritários

## 1\. Brann — Atendimento

### Entrada

Lead envia mensagem via WhatsApp.

### Saída esperada

- resposta
- qualificação
- agendamento
- handoff
- atualização em CRM
- log completo

### Sequência

1. receber evento
2. normalizar
3. rotear intenção
4. carregar memória
5. validar policy
6. executar skill
7. chamar tool se necessário
8. compor resposta
9. registrar auditoria
10. emitir métricas

---

## 2\. Alfred — Análise e operação

### Entrada

Usuário pede análise ou ação operacional.

### Saída esperada

- diagnóstico
- alerta
- recomendação
- tarefa criada
- ação confirmada

### Sequência

1. receber comando
2. identificar workspace e agente
3. carregar contexto histórico
4. buscar dados da integração
5. executar análise
6. verificar policy
7. sugerir ou executar
8. registrar tudo

---

## 3\. Nyra — Conteúdo

### Entrada

Usuário pede conteúdo, calendário ou adaptação.

### Saída esperada

- calendário
- roteiro
- copy
- legenda
- conteúdo agendado

### Sequência

1. receber input
2. carregar brand memory
3. selecionar skill criativa
4. consultar histórico e contexto
5. gerar saída
6. opcionalmente agendar
7. registrar analytics

---

## Integrações prioritárias

### Canais

- Evolution API
- Chatwoot

### Dados e memória

- Supabase
- Redis
- Qdrant

### Agenda

- Google Calendar

### Conteúdo e operação

- ClickUp
- Google Drive / Docs

### Comercial

- Stripe

### Mídia paga

- Meta Ads

### Orquestração

- n8n

---

## Requisitos funcionais

### Runtime

- suportar múltiplos agentes
- suportar múltiplos canais
- isolar tenants
- registrar cada execução

### Memória

- suportar escopos hierárquicos
- persistir contexto relevante
- permitir RAG por workspace
- diferenciar curto e longo prazo

### Ferramentas

- padronizar input/output
- aplicar permissão antes da execução
- registrar chamadas
- suportar timeout e retry

### Governança

- permissão por agente, ação e ferramenta
- confirmação humana quando necessário
- auditoria completa

### Analytics

- coletar eventos
- medir uso
- medir valor operacional
- suportar dashboard inicial

---

## Requisitos não funcionais

### Segurança

- isolamento por tenant
- segregação de credenciais
- retenção de dados
- proteção de logs sensíveis

### Escalabilidade

- múltiplos workspaces por tenant
- workers assíncronos
- filas para processamento pesado

### Observabilidade

- logs estruturados
- tracing por execução
- alertas de falha
- monitoramento por integração

### Performance

- resposta rápida em fluxos simples
- recuperação eficiente de memória
- cache para contexto frequente

### Manutenibilidade

- skills versionadas
- tools desacopladas
- configs por ambiente
- prompts separados por camada

---

## Backlog inicial

## Bloco A — Foundation

- definir contratos internos
- criar entidades núcleo
- implementar runtime mínimo
- implementar audit logger
- implementar metric event pipeline

## Bloco B — Brann First

- integrar Evolution API
- criar normalizador de mensagens
- criar skills básicas
- integrar agenda
- integrar CRM/base de leads
- registrar handoff humano

## Bloco C — Memory System

- Redis para sessão
- Postgres para persistência
- storage para anexos
- embeddings pipeline
- retrieval por tenant/workspace

## Bloco D — Policy + Governance

- matriz de permissões
- aprovações
- bloqueio de ações sensíveis
- log de confirmação

## Bloco E — Analytics MVP

- métricas de uso
- métricas de tempo
- métricas por skill
- dashboard básico

## Bloco F — Expansão multiagente

- onboarding de Alfred
- onboarding de Nyra
- tools específicas
- outputs padronizados

---

## Roadmap

## Fase 1 — Infra mínima funcional

Entrega:

- tabelas centrais
- runtime básico
- tool bus inicial
- memória curta + persistente
- logs + analytics básicos

## Fase 2 — Brann em produção

Entrega:

- atendimento WhatsApp
- FAQ
- qualificação
- agendamento
- CRM
- handoff humano

## Fase 3 — Governança e painel

Entrega:

- dashboard inicial
- auditoria navegável
- permissões
- fluxo de confirmação

## Fase 4 — Expansão

Entrega:

- Alfred no mesmo core
- Nyra no mesmo core
- analytics por produto
- arquitetura consolidada multiagente

---

## Critérios de sucesso

O Ginkgo Agent OS será considerado validado quando:

- Brann operar sobre runtime único
- memória por tenant estiver isolada corretamente
- ao menos 5 skills estiverem funcionais
- ao menos 5 integrações estiverem conectadas
- ações auditáveis estiverem registradas corretamente
- dashboard exibir métricas mínimas por cliente
- Alfred e Nyra puderem ser onboardados sem reescrever o core

---

## Riscos

### Complexidade excessiva cedo demais

Mitigação:

- começar por Brann
- limitar escopo do MVP

### Memória mal escopada

Mitigação:

- `tenant_id` e `workspace_id` obrigatórios em toda camada

### Integrações caóticas

Mitigação:

- tool contract rígido

### Prompts desorganizados

Mitigação:

- separar persona, skill e policy

### Falta de prova de valor

Mitigação:

- analytics desde a primeira execução

---

## Estrutura recomendada do repositório

```markdown
ginkgo-agent-os/
├─ apps/
│  ├─ api/
│  ├─ worker/
│  └─ dashboard/
├─ packages/
│  ├─ core-runtime/
│  ├─ memory-system/
│  ├─ tool-bus/
│  ├─ policy-engine/
│  ├─ analytics/
│  ├─ audit/
│  ├─ shared-types/
│  └─ agent-definitions/
├─ integrations/
│  ├─ evolution-api/
│  ├─ chatwoot/
│  ├─ google-calendar/
│  ├─ stripe/
│  ├─ clickup/
│  ├─ meta-ads/
│  └─ supabase/
├─ infra/
│  ├─ docker/
│  ├─ migrations/
│  ├─ scripts/
│  └─ environments/
├─ docs/
│  ├─ architecture/
│  ├─ prd/
│  ├─ api/
│  └─ runbooks/
└─ README.md
```

---

## Decisão final

O Ginkgo Agent OS não deve nascer como um chatbot melhorado.

Ele deve nascer como a camada que padroniza inteligência operacional dentro da Ginkgo.

Em termos práticos:

- **Brann** é a face comercial
- **Alfred** é o operador analítico
- **Nyra** é o motor criativo
- **Ginkgo Agent OS** é a infraestrutura que conecta, governa e mede tudo

Esse núcleo é o que transforma automações soltas em produto replicável.

---

## Próximos documentos recomendados

1. `DATABASE_SCHEMA.md`
2. `API_CONTRACTS.md`
3. `MVP_SPRINTS.md`
4. `AGENT_SPEC_BRANN.md`
5. `AGENT_SPEC_ALFRED.md`
6. `AGENT_SPEC_NYRA.md`