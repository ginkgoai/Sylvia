---
title: "SaaS e Arquitetura MCP"
source: "https://chatgpt.com/c/6a678c2b-faec-83e9-8dc2-cc04462756bc"
author:
published:
created: 2026-07-27
description: "ChatGPT conversation with 6 messages"
tags:
  - "clippings"
---
**Você disse**

---

A lógica dele está **certa economicamente**, mas **incompleta arquiteturalmente**.

O que ele descreveu não é exatamente um SaaS tradicional. É um modelo de **plataforma de controle + execução custeada pelo cliente**:

```
Cliente
  ↓
Claude Cowork / Claude Code / OpenClaw / Hermes
  ↓
MCP da Ginkgo
  ↓
Fluxos, APIs e serviços
  ↓
CRM, WhatsApp, agenda, pagamentos, relatórios
```

A Ginkgo vende o **sistema nervoso**. O usuário fornece o cérebro e paga a energia elétrica dele.

## O ponto correto da conversa

Você pode disponibilizar um conjunto de MCPs, ferramentas e agentes para o cliente conectar ao Claude, Hermes ou outro host compatível.

O MCP segue uma arquitetura cliente-servidor: o aplicativo de IA funciona como host e conecta-se a servidores MCP, que expõem ferramentas para consultar bancos, executar APIs e realizar ações. Portanto, construir uma ferramenta uma vez pode permitir seu uso por diferentes agentes compatíveis. [^1]

Exemplo:

```
leaf_search_contacts
leaf_update_lead
leaf_send_whatsapp
leaf_schedule_meeting
leaf_generate_proposal
leaf_get_sales_report
```

O cliente poderia dizer:

> “Encontre os leads parados há cinco dias, crie uma abordagem personalizada e envie para aprovação.”

O Claude, Hermes ou OpenClaw decide quais ferramentas chamar. A Ginkgo cobra pelo acesso à infraestrutura, permissões e automações.

## Onde a afirmação “não gasto tokens” engana

Você deixa de pagar diretamente pela inferência do cliente, mas continua pagando por:

- hospedagem dos servidores MCP;
- banco, filas, Redis e armazenamento;
- autenticação e gestão de credenciais;
- logs, auditoria e observabilidade;
- processamento de webhooks;
- WhatsApp, transcrição, voz e serviços externos;
- suporte técnico;
- correção de execuções erradas;
- segurança, limites e prevenção de abuso.

Ou seja:

```
Economiza tokens ≠ custo operacional zero
```

É como vender uma tomada e dizer que não paga a conta de luz. Correto, mas ainda há fiação, transformador, manutenção e alguém ligando porque o micro-ondas derrubou o prédio.

## O MCP não substitui o backend

Esse é o ponto mais importante.

O MCP apenas **expõe capacidades**. Ele não garante sozinho:

- ordem correta das etapas;
- idempotência;
- retries;
- aprovação humana;
- consistência transacional;
- isolamento entre clientes;
- controle de acesso;
- limite financeiro;
- recuperação de falhas;
- cumprimento de SLA.

A frase “cadastra os fluxos no MCP e deixa o bot se virar” funciona para uso pessoal ou protótipo. Em produção multiempresa, pode virar uma distopia corporativa em que o agente envia 4.000 mensagens porque interpretou “fale com todos” com entusiasmo demais.

O correto é:

```
Agente decide intenção
        ↓
Policy Engine valida
        ↓
Workflow executa
        ↓
Sistema registra evidência
        ↓
Humano aprova ações críticas
```

## Hermes, OpenClaw e Claude Cowork não ocupam o mesmo lugar

### Hermes Agent

O Hermes faz mais sentido como **runtime controlável e incorporável** à infraestrutura da Ginkgo.

Ele suporta MCP para conectar ferramentas externas como bancos, APIs, GitHub e serviços internos. Também possui gateway para múltiplos canais, incluindo WhatsApp, Telegram, Slack e Discord. [^2]

Uso ideal:

- agente gerenciado pelo Leaf;
- agentes internos da Ginkgo;
- execução em VPS;
- personas especializadas;
- modelos intercambiáveis;
- integração profunda com o produto.

### OpenClaw

O OpenClaw é mais próximo de um **operador pessoal autônomo**, com gateway multicanal, habilidades, memória e acesso amplo ao ambiente. A documentação oficial o posiciona como gateway de agentes para diversos canais de comunicação. [^3]

Uso ideal:

- operações internas;
- clientes técnicos;
- automação pessoal;
- agentes com autonomia prolongada;
- execução local ou em VPS privada.

O problema é justamente sua força: muita autonomia e acesso aumentam a superfície de risco. Não é algo que eu colocaria diretamente no centro do Leaf para clientes comuns sem sandbox, permissões mínimas e aprovação humana.

### Claude Cowork

O Cowork faz sentido como **interface operacional do próprio usuário**, não como fundação exclusiva do seu SaaS. A Anthropic passou a disponibilizá-lo também em web e mobile, com sessões executadas remotamente. [^4]

Uso ideal:

- o cliente operar arquivos e projetos;
- conectar MCPs da Ginkgo;
- executar tarefas administrativas;
- usar a própria assinatura ou consumo;
- evitar que a Ginkgo banque integralmente a inferência.

Dependência crítica: seu produto ficaria parcialmente subordinado ao preço, limites, disponibilidade e mudanças comerciais da Anthropic.

## Arquitetura recomendada para o Leaf

Não escolha entre “SaaS tradicional” e “cliente paga o bot”. Use os dois.

```
┌───────────────────────────────────────────┐
│              LEAF CONTROL PLANE           │
│ CRM · Inbox · Usuários · Billing · Logs   │
│ Permissões · Aprovações · Configurações   │
└───────────────────┬───────────────────────┘
                    │
             Leaf Agent Gateway
                    │
       ┌────────────┼─────────────┐
       │            │             │
 Managed Hermes   BYOK API      External Agent
 Ginkgo paga      Cliente paga  Cowork/OpenClaw
 parcialmente     tokens        via MCP
       │            │             │
       └────────────┼─────────────┘
                    │
          Workflow/Policy Engine
         n8n + workers + filas
                    │
 WhatsApp · Agenda · CRM · E-mail · Pagamentos
```

### Camada 1 — Leaf obrigatório

Independentemente do agente escolhido:

- autenticação;
- workspace;
- contatos;
- conversas;
- pipeline;
- configurações;
- auditoria;
- faturamento;
- permissões;
- painel operacional.

### Camada 2 — Hermes gerenciado

Para o cliente comum:

- conecta o WhatsApp;
- escolhe uma persona;
- ativa a IA;
- começa a usar.

Sem API keys, terminais ou zoológico de configurações.

### Camada 3 — BYOK

O cliente técnico pode conectar:

- chave de API própria;
- provedor preferido;
- limites de consumo;
- modelo específico.

Você cobra pelo Leaf, não necessariamente pelo modelo.

### Camada 4 — Bring Your Own Agent

Plano avançado:

- Claude Cowork;
- Claude Code;
- OpenClaw;
- Hermes privado;
- outros clientes MCP.

O Leaf fornece um **MCP Gateway seguro**, com ferramentas permitidas por usuário, workspace e plano.

## Modelo comercial

### Leaf Standard

```
Mensalidade
+ franquia de IA
+ excedente por consumo
```

Melhor experiência para pequenas empresas.

### Leaf BYOK

```
Mensalidade menor
+ cliente fornece a API key
+ Ginkgo cobra infraestrutura e produto
```

Boa margem e previsibilidade.

### Leaf Agent Connect

```
Mensalidade do Leaf
+ acesso ao MCP Gateway
+ pacotes de ferramentas
+ auditoria e governança
```

Voltado a usuários de Claude, OpenClaw e ambientes corporativos.

### Ginkgo Private Agent Cloud

```
Setup
+ mensalidade de infraestrutura
+ runtime Hermes/OpenClaw privado
+ manutenção
+ governança
```

Oferta premium para empresas.

## Decisão objetiva

Para a **operação interna da Ginkgo**, a ideia do Tech Lead é excelente:

```
Claude Cowork ou OpenClaw
          ↓
MCPs Ginkgo
          ↓
Sistemas internos
```

Para o **Leaf como produto**, não terceirize completamente a inteligência ao cliente. Isso destruiria a promessa de onboarding em menos de dez minutos.

A melhor arquitetura é:

> **Hermes como motor padrão gerenciado, MCP como camada universal de integração e Claude/OpenClaw como modos avançados opcionais.**

Assim, o Leaf não vira apenas “mais um chatbot”. Ele se torna o **painel de comando neutro para agentes**, capaz de trocar o cérebro sem reconstruir o corpo inteiro.

---

**Você disse**

Podemos fazer algo extremamente básico para ser comercializado rapidamente, esqueça toda a estrutura, Leaf, projetos e Ginkgo, vamo algo basicao, tipo montar um MCP completo nichado, um canivete suíço para o sistema e ia, e faça um conecte a ia ao seu sistema em segundos, API ou como precisar, conseguindo plugar a ia nativamente ao sistema pré existente do usuário, para realizar escritas, automações, etc

---

Sim. E a forma mais rápida de comercializar isso **não é começar como SaaS self-service**. É começar como um **produto-serviço padronizado**:

## Produto: AI System Bridge

> **Conecte sua IA ao seu sistema em segundos.**

Você transforma a API de qualquer CRM, ERP, SaaS ou sistema interno em ferramentas que uma IA consegue consultar e executar.

```
IA do cliente
     ↓
MCP remoto
     ↓
Camada de segurança e permissões
     ↓
API do sistema existente
     ↓
CRM · ERP · Pedidos · Financeiro · Suporte
```

O produto não substitui o sistema do cliente. Ele adiciona uma **camada de ação por IA** sobre o que já existe.

O MCP é adequado para isso porque permite que servidores exponham ferramentas estruturadas para consulta, escrita e execução em sistemas externos. Para conexões remotas, o transporte padrão é Streamable HTTP. [^1]

---

## O que o cliente consegue fazer

Depois de conectado, ele pode pedir:

> “Liste os clientes com pagamentos atrasados.”

> “Atualize o status deste pedido para enviado.”

> “Crie uma proposta para esta empresa.”

> “Abra um chamado para o setor financeiro.”

> “Busque todos os leads sem contato nos últimos sete dias.”

> “Gere um resumo das vendas deste mês.”

Cada ação vira uma ferramenta MCP:

```
search_customers
get_customer
create_customer
update_customer
list_orders
update_order_status
create_invoice
create_support_ticket
generate_sales_report
trigger_workflow
```

A IA interpreta o pedido. O Bridge executa a ação permitida na API do sistema.

---

## A proposta real

Não vender:

> “Construímos um servidor MCP.”

Vender:

> **Sua IA passa a operar o sistema que sua empresa já usa.**

MCP fica na camada técnica. É o motor, não o outdoor.

### Headline

**Conecte sua IA ao seu sistema em segundos.**

### Subheadline

Transforme a API do seu ERP, CRM ou SaaS em ações seguras que agentes de IA podem consultar, criar, atualizar e automatizar.

### CTA

**Conectar meu sistema**

---

## O MVP brutalmente enxuto

O primeiro produto precisa fazer somente seis coisas.

## 1\. Cadastrar um sistema

O cliente informa:

```
Nome do sistema
URL base da API
Método de autenticação
Documentação OpenAPI
```

OpenAPI fornece uma descrição padronizada dos endpoints, parâmetros, autenticação, entradas e saídas de uma API. Isso permite automatizar boa parte da criação das ferramentas. [^5]

## 2\. Importar a API

O cliente envia:

```
openapi.json
openapi.yaml
URL do Swagger
```

O sistema identifica:

```
GET /customers
POST /customers
PATCH /orders/{id}
GET /reports/sales
```

## 3\. Converter endpoints em ferramentas

Exemplo:

```
PATCH /orders/{id}
```

Vira:

```
update_order_status(
  order_id,
  status,
  tracking_code
)
```

A ferramenta recebe nome, descrição, parâmetros obrigatórios e formato de resposta.

## 4\. Definir permissões

Cada ferramenta recebe uma classificação:

```
READ
WRITE
CRITICAL
```

Exemplo:

```
search_customers       → READ
update_customer        → WRITE
delete_customer        → CRITICAL
refund_payment         → CRITICAL
```

Ações críticas exigem aprovação humana.

## 5\. Gerar o MCP remoto

O cliente recebe uma URL:

```
https://api.systembridge.ai/mcp/workspace_123
```

E conecta essa URL a um cliente compatível com MCP.

Para servidores remotos protegidos, a especificação atual define uma camada de autorização baseada em OAuth 2.1 e metadados do recurso protegido. Isso deve entrar na versão comercial, não ser tratado como “vemos depois”. [^6]

## 6\. Registrar execuções

Painel simples:

```
Data
Usuário
Ferramenta
Parâmetros
Resposta
Status
Tempo de execução
Aprovação
```

Nada além disso no primeiro MVP.

---

## O que não construir agora

Corte sem piedade:

- chat próprio;
- agente autônomo;
- RAG;
- memória;
- marketplace;
- editor visual de workflows;
- múltiplos modelos;
- geração de conteúdo;
- cobrança de tokens;
- aplicação mobile;
- observabilidade cinematográfica;
- automação via navegador;
- conexão direta genérica com bancos;
- suporte a SOAP e sistemas desktop.

O produto inicial não precisa “pensar”. Ele precisa **conectar e executar**.

A inteligência fica do lado do cliente. O produto vende a ponte, a segurança e o controle.

---

## Arquitetura mínima

```
┌───────────────────────────────┐
│ Cliente MCP / Agente de IA    │
└───────────────┬───────────────┘
                │ Streamable HTTP
                ▼
┌───────────────────────────────┐
│ MCP Gateway                   │
│                               │
│ Autenticação                  │
│ Descoberta de ferramentas     │
│ Validação de entrada          │
│ Rate limit                    │
│ Logs                          │
└───────────────┬───────────────┘
                ▼
┌───────────────────────────────┐
│ Policy Engine                 │
│                               │
│ READ → executar               │
│ WRITE → validar               │
│ CRITICAL → pedir aprovação    │
└───────────────┬───────────────┘
                ▼
┌───────────────────────────────┐
│ Adaptador OpenAPI/REST        │
└───────────────┬───────────────┘
                ▼
┌───────────────────────────────┐
│ Sistema do cliente            │
│ CRM · ERP · SaaS · Backoffice │
└───────────────────────────────┘
```

---

## Stack recomendada

Para o motor MCP:

```
TypeScript
Node.js
MCP TypeScript SDK v1.x
Hono ou Express
PostgreSQL
Prisma
Docker
```

O SDK oficial TypeScript já fornece servidor, cliente, ferramentas, Streamable HTTP, stdio e auxiliares de autenticação. A documentação atual recomenda a linha v1.x para produção enquanto a v2 permanece em desenvolvimento. [^7]

Para este MVP, eu não usaria Laravel como núcleo do MCP.

Laravel pode entrar posteriormente para:

```
dashboard
billing
administração
usuários
backoffice
```

Mas usar Laravel + Node + filas + Redis + microsserviços desde o primeiro cliente é montar a Estrela da Morte para entregar uma bicicleta.

### Stack inicial real

```
Monólito TypeScript
PostgreSQL
Docker
Uma aplicação
Um domínio
Um endpoint MCP
```

Sem Redis inicialmente. Sem Kubernetes. Sem n8n obrigatório.

---

## Modelo de implantação mais rápido

## Não comece self-service

Comece assim:

1. cliente envia a documentação da API;
2. vocês escolhem de 5 a 15 ações;
3. geram o MCP usando um template;
4. implantam uma instância;
5. entregam a URL e a configuração;
6. cobram setup e mensalidade.

Cada novo cliente utiliza o mesmo núcleo e recebe apenas:

```
configuração
credenciais
ferramentas
políticas
domínio ou workspace
```

Isso é uma **fábrica de MCPs**, não uma plataforma completa.

Depois de três a cinco clientes, os padrões reais mostram quais partes devem virar self-service.

---

## Primeiro nicho recomendado

Não lance como “conecta qualquer coisa”.

Isso transforma o negócio em consultoria infinita.

Comece com:

> **SaaS, ERPs e CRMs que já possuem API REST ou OpenAPI documentada.**

Cliente ideal:

```
Software house
SaaS B2B
ERP regional
CRM vertical
Sistema de gestão
Plataforma de atendimento
```

Essas empresas já têm:

- API;
- autenticação;
- entidades organizadas;
- ações repetitivas;
- base de clientes;
- interesse em adicionar IA sem reconstruir o produto.

A oferta para uma software house fica ainda mais forte:

> “Transformamos sua API em uma camada de IA que você pode oferecer para todos os seus clientes.”

Você vende uma integração e pode alcançar dezenas ou centenas de contas através de um único parceiro.

---

## Limites comerciais claros

A primeira versão suporta:

```
REST
JSON
OpenAPI
API Key
Bearer Token
OAuth
Webhooks simples
```

Não suporta inicialmente:

```
Sistema sem API
Automação por navegador
Aplicativo desktop legado
SOAP
Acesso direto irrestrito ao banco
Endpoints sem documentação
```

Sistema sem API vira serviço separado de desenvolvimento de adaptador.

Assim você evita vender “conecte qualquer sistema” e descobrir que o sistema do cliente foi desenvolvido em 2009 por alguém chamado Juninho, que sumiu com a senha do servidor.

---

## Segurança mínima obrigatória

O canivete suíço deve ter lâminas identificadas. Não uma ferramenta chamada:

```
execute_any_http_request
```

Ou:

```
execute_sql
```

Isso entregaria à IA acesso praticamente irrestrito.

Cada ação deve ser explícita:

```
create_customer
update_order
cancel_invoice
```

E possuir:

```
schema rígido
escopo
limite de chamadas
timeout
log
idempotência
aprovação
lista de campos permitidos
```

Exemplo:

```
A IA pode alterar:
- telefone
- e-mail
- responsável
- status

A IA não pode alterar:
- saldo
- limite financeiro
- proprietário da conta
- permissões
```

---

## Modelo de cobrança

Não cobre por token. A IA e o modelo são do cliente.

Cobre por:

```
sistema conectado
quantidade de ferramentas
volume de execuções
ambientes
retenção de logs
aprovações
SLA
```

## Oferta fundadora

Para os três primeiros clientes:

```
Setup: R$ 1.490
Mensalidade: R$ 297

1 sistema
Até 10 ferramentas
1 ambiente
Logs por 30 dias
Suporte básico
IA/API paga pelo cliente
```

## Oferta padrão após validação

```
Setup: R$ 3.900
Mensalidade: R$ 790

1 sistema
Até 25 ferramentas
Homologação e produção
Controle de permissões
Aprovação de ações críticas
Logs por 90 dias
```

## White-label para software houses

```
Setup: a partir de R$ 7.500
Mensalidade por parceiro
Cobrança adicional por workspace
Identidade personalizada
```

---

## Prazo realista

## Motor-base

```
Dias 1–2
Servidor MCP remoto
Registro de ferramentas
Chamadas REST

Dias 3–4
Importação OpenAPI
Autenticação
Validação de schemas

Dias 5–6
Logs
Permissões
Aprovação de ações

Dia 7
Docker
Deploy
Documentação
Demo comercial
```

Em aproximadamente **sete dias de desenvolvimento focado**, é plausível ter o motor demonstrável.

O primeiro cliente pode exigir mais dois ou três dias para mapeamento e homologação.

---

## A verdade sobre “em segundos”

A mensagem pode ser:

> **Conecte sua IA ao seu sistema em segundos.**

Mas a promessa operacional correta é:

> Depois que a API estiver configurada, conectar uma IA compatível ao MCP leva segundos.

Para uma API OpenAPI limpa, o onboarding pode levar poucos minutos. Para um sistema sem API, não existe botão mágico. Existe desenvolvimento de integração com maquiagem de botão mágico.

---

## Demonstração comercial ideal

Crie um sistema fictício chamado **Acme CRM** com:

```
20 clientes
30 leads
15 pedidos
5 cobranças atrasadas
```

Disponibilize estas ferramentas:

```
list_leads
search_customers
create_customer
update_lead_status
list_overdue_invoices
create_support_ticket
generate_sales_summary
```

Grave uma demonstração:

```
Usuário:
“Encontre os leads sem contato há mais de cinco dias.”

IA:
“Encontrei oito leads.”

Usuário:
“Marque os três maiores como prioridade e crie tarefas para amanhã.”

IA:
“A ação afetará três registros. Deseja aprovar?”

Usuário:
“Sim.”

IA:
“Registros atualizados e tarefas criadas.”
```

Em 40 segundos o comprador entende o produto inteiro.

---

## Definição final

O produto não é apenas um MCP nichado.

É:

> **Uma camada universal e segura de ações por IA para sistemas que já possuem API.**

A versão inicial deve ser vendida como implantação padronizada, não como SaaS aberto.

```
OpenAPI entra
        ↓
Ferramentas MCP saem
        ↓
IA consulta e escreve
        ↓
Empresa mantém controle
```

Nome provisório mais direto:

## SystemBridge

**Conecte sua IA ao seu sistema em segundos.**

Alternativas:

```
NativeBridge
MCP Forge
ActionLayer
SystemLink AI
Nexo Bridge
```

A decisão tática correta é construir primeiro o **template de integração OpenAPI → MCP**, adicionar dez ferramentas demonstrativas e colocar o piloto à venda antes de criar qualquer dashboard sofisticado.

---

**Você disse**

Dívida o Passo a Passo em Épicos instrutivos para Claude

---

## SystemBridge MVP — Épicos instrutivos para Claude

Objetivo: construir uma ponte que transforme uma API REST/OpenAPI existente em ferramentas MCP utilizáveis por Claude, agentes e clientes compatíveis.

```
OpenAPI/Swagger
      ↓
Catálogo controlado de operações
      ↓
Ferramentas MCP
      ↓
IA consulta e altera o sistema
      ↓
Logs, permissões e aprovações
```

A estratégia é entregar primeiro um **produto-serviço configurável**, não uma plataforma universal com 97 telas e crise de identidade.

---

## Prompt mestre do projeto

Envie este prompt ao Claude antes de iniciar os épicos.

```
Você atuará como Arquiteto Principal e Product Engineer do projeto SystemBridge.

MISSÃO

Construir um MVP comercial que permita conectar uma IA a um sistema existente por meio de MCP.

O sistema deverá:

1. Receber uma especificação OpenAPI.
2. Interpretar os endpoints disponíveis.
3. Permitir selecionar quais operações serão expostas.
4. Converter operações selecionadas em ferramentas MCP.
5. Executar chamadas na API original.
6. Validar entradas e respostas.
7. Aplicar permissões.
8. Registrar todas as execuções.
9. Exigir aprovação para ações críticas.
10. Disponibilizar um servidor MCP remoto.

PROPOSTA COMERCIAL

“Conecte sua IA ao seu sistema em segundos.”

A frase significa que, depois de a API do cliente estar configurada, ele consegue conectar sua IA ao endpoint MCP rapidamente.

ESCOPO INICIAL

Suportar:

- REST;
- JSON;
- OpenAPI 3.x;
- API Key;
- Bearer Token;
- autenticação por headers personalizados;
- operações GET, POST, PUT, PATCH e DELETE;
- MCP remoto usando Streamable HTTP;
- logs;
- rate limiting;
- permissões;
- aprovação de ações críticas;
- múltiplos workspaces.

NÃO IMPLEMENTAR AGORA

- chat próprio;
- agente próprio;
- RAG;
- memória de conversas;
- marketplace;
- editor visual de workflows;
- aplicação mobile;
- Kubernetes;
- múltiplos microsserviços;
- automação por navegador;
- SOAP;
- acesso genérico ao banco de dados;
- execução arbitrária de SQL;
- ferramenta genérica de HTTP irrestrito.

STACK

- Node.js;
- TypeScript;
- SDK oficial do MCP;
- Fastify;
- PostgreSQL;
- Prisma;
- Zod;
- Docker;
- Vitest;
- Pino para logs;
- Swagger/OpenAPI para a API administrativa.

ARQUITETURA

Construir inicialmente como monólito modular.

Estrutura sugerida:

src/
  app/
  config/
  database/
  workspaces/
  credentials/
  openapi/
  tools/
  execution/
  policies/
  approvals/
  audit/
  mcp/
  demo/

REGRAS DE EXECUÇÃO

1. Trabalhe somente no épico solicitado.
2. Não antecipe funcionalidades de épicos futuros.
3. Antes de implementar, analise o estado atual do repositório.
4. Apresente um plano resumido.
5. Implemente em etapas pequenas.
6. Crie testes para comportamentos críticos.
7. Não deixe mocks silenciosos em produção.
8. Não esconda erros com fallbacks genéricos.
9. Não exponha credenciais em logs.
10. Mantenha isolamento entre workspaces.
11. Toda ferramenta precisa ter schema explícito.
12. Nenhum endpoint da API importada deve ser exposto automaticamente sem aprovação.
13. DELETE e operações financeiras devem ser críticas por padrão.
14. Ao terminar, execute lint, testes e build.
15. Gere um relatório contendo:
   - arquivos criados;
   - arquivos alterados;
   - decisões técnicas;
   - testes executados;
   - limitações atuais;
   - próximo passo recomendado.

Não altere requisitos ou stack sem justificar objetivamente.
```

---

## Épico 1 — Fundação do projeto

## Objetivo

Criar a base executável do SystemBridge.

## Entregáveis

- projeto TypeScript;
- servidor Fastify;
- configuração por variáveis de ambiente;
- PostgreSQL;
- Prisma;
- logs estruturados;
- health check;
- Docker Compose;
- testes iniciais;
- documentação de execução local.

## Critério de pronto

```
docker compose up
```

Deve iniciar aplicação e banco, com:

```
GET /health
```

Retornando algo como:

```json
{
  "status": "ok",
  "database": "connected",
  "version": "0.1.0"
}
```

## Prompt para Claude

```
Execute o ÉPICO 1 — FUNDAÇÃO DO PROJETO.

OBJETIVO

Criar a fundação executável do SystemBridge usando:

- Node.js;
- TypeScript;
- Fastify;
- PostgreSQL;
- Prisma;
- Zod;
- Pino;
- Vitest;
- Docker Compose.

IMPLEMENTE

1. Inicialização do projeto.
2. Configuração TypeScript em modo strict.
3. Carregamento e validação de variáveis de ambiente com Zod.
4. Servidor Fastify modular.
5. Integração com Prisma e PostgreSQL.
6. Logger estruturado com Pino.
7. Endpoint GET /health.
8. Tratamento centralizado de erros.
9. Graceful shutdown.
10. Dockerfile.
11. docker-compose.yml.
12. Scripts de desenvolvimento, build, lint, test e start.
13. Testes do health check e validação de configuração.
14. README com instruções locais.

VARIÁVEIS MÍNIMAS

- NODE_ENV;
- PORT;
- DATABASE_URL;
- LOG_LEVEL;
- APP_BASE_URL;
- MASTER_ENCRYPTION_KEY.

RESTRIÇÕES

- Não implemente autenticação.
- Não implemente MCP.
- Não implemente importação OpenAPI.
- Não crie frontend.
- Não crie microsserviços.
- Não use Redis.

CRITÉRIOS DE ACEITAÇÃO

- docker compose up inicia banco e aplicação;
- migrations podem ser executadas;
- GET /health retorna HTTP 200;
- falha de banco é reportada corretamente;
- npm run build funciona;
- npm test funciona;
- nenhuma credencial aparece nos logs.

Ao terminar, entregue o relatório técnico obrigatório.
```

---

## Épico 2 — Workspaces, usuários técnicos e credenciais

## Objetivo

Criar a separação entre clientes e armazenar credenciais de APIs externas com segurança.

## Entregáveis

- workspaces;
- chaves de acesso administrativas;
- sistemas conectados;
- credenciais criptografadas;
- isolamento lógico por workspace;
- endpoints administrativos básicos.

## Modelo inicial

```
Workspace
 ├── API Keys
 ├── Connected Systems
 ├── Credentials
 ├── OpenAPI Documents
 ├── Tools
 └── Execution Logs
```

## Critério de pronto

Deve ser possível:

1. criar workspace;
2. criar uma chave administrativa;
3. cadastrar um sistema;
4. cadastrar credencial criptografada;
5. impedir acesso cruzado entre workspaces.

## Prompt para Claude

```
Execute o ÉPICO 2 — WORKSPACES E CREDENCIAIS.

OBJETIVO

Implementar a base multiworkspace e o armazenamento seguro das credenciais usadas para acessar as APIs dos clientes.

ENTIDADES

Workspace:
- id;
- name;
- slug;
- status;
- createdAt;
- updatedAt.

WorkspaceApiKey:
- id;
- workspaceId;
- name;
- keyHash;
- prefix;
- lastUsedAt;
- expiresAt;
- revokedAt;
- createdAt.

ConnectedSystem:
- id;
- workspaceId;
- name;
- slug;
- baseUrl;
- status;
- createdAt;
- updatedAt.

Credential:
- id;
- workspaceId;
- connectedSystemId;
- name;
- type;
- encryptedPayload;
- keyVersion;
- createdAt;
- updatedAt.

TIPOS DE CREDENCIAL

- API_KEY_HEADER;
- BEARER_TOKEN;
- CUSTOM_HEADERS;
- NONE.

IMPLEMENTE

1. Models e migrations Prisma.
2. Serviço de criação de workspace.
3. Geração de API key segura.
4. Armazenamento somente do hash da API key.
5. Middleware de autenticação por API key.
6. Resolução obrigatória do workspace em cada requisição.
7. Criptografia autenticada das credenciais.
8. Serviço para descriptografar credenciais somente no momento da execução.
9. Endpoints administrativos:
   - POST /admin/workspaces;
   - POST /admin/api-keys;
   - POST /admin/systems;
   - GET /admin/systems;
   - POST /admin/systems/:id/credentials.
10. Redação de dados sensíveis nos logs.
11. Testes de isolamento entre workspaces.
12. Testes de API key inválida, expirada e revogada.

REGRAS

- Nunca retornar o valor completo de uma credencial.
- A API key completa só pode ser exibida uma vez, no momento da criação.
- Nunca persistir API key em texto puro.
- Nunca aceitar workspaceId vindo livremente do corpo quando ele puder ser derivado da autenticação.
- Toda query deve ser filtrada pelo workspace autenticado.
- Não implementar usuários humanos ou login por senha.
- Não implementar OAuth neste épico.

CRITÉRIOS DE ACEITAÇÃO

- dois workspaces não acessam registros um do outro;
- credenciais ficam criptografadas no banco;
- valores sensíveis não aparecem em logs ou respostas;
- chaves revogadas deixam de funcionar imediatamente;
- migrations, build e testes passam.

Ao terminar, entregue o relatório técnico obrigatório.
```

---

## Épico 3 — Importação e normalização de OpenAPI

## Objetivo

Receber uma documentação OpenAPI e transformá-la em um catálogo interno de operações.

## Entradas suportadas

- upload de `.json`;
- upload de `.yaml`;
- URL pública de OpenAPI;
- texto JSON ou YAML.

## Saída esperada

```
GET /customers
  operationId: listCustomers
  parâmetros: page, limit, status
  classificação inicial: READ

PATCH /customers/{id}
  operationId: updateCustomer
  parâmetros: id, body
  classificação inicial: WRITE
```

## Prompt para Claude

```
Execute o ÉPICO 3 — IMPORTAÇÃO E NORMALIZAÇÃO OPENAPI.

OBJETIVO

Permitir que um workspace importe uma especificação OpenAPI 3.x e gerar um catálogo interno normalizado de operações.

ENTIDADES

OpenApiDocument:
- id;
- workspaceId;
- connectedSystemId;
- name;
- version;
- sourceType;
- sourceUrl;
- rawDocument;
- checksum;
- validationStatus;
- validationErrors;
- importedAt;
- createdAt;
- updatedAt.

ApiOperation:
- id;
- workspaceId;
- connectedSystemId;
- openApiDocumentId;
- operationId;
- method;
- path;
- summary;
- description;
- tags;
- parametersSchema;
- requestBodySchema;
- responseSchema;
- securityRequirements;
- riskLevel;
- enabled;
- createdAt;
- updatedAt.

FONTES SUPORTADAS

- JSON enviado no corpo;
- YAML enviado no corpo;
- upload de arquivo;
- URL remota HTTPS.

IMPLEMENTE

1. Parser seguro para OpenAPI 3.0 e 3.1.
2. Validação estrutural do documento.
3. Bloqueio de documentos Swagger 2.0 neste momento, com mensagem explícita.
4. Normalização dos endpoints.
5. Identificação de:
   - path parameters;
   - query parameters;
   - headers permitidos;
   - request body;
   - respostas;
   - security schemes.
6. Geração de operationId quando ele não existir.
7. Classificação inicial:
   - GET e HEAD como READ;
   - POST, PUT e PATCH como WRITE;
   - DELETE como CRITICAL.
8. Persistência do documento original.
9. Checksum para evitar importações duplicadas.
10. Endpoints:
   - POST /admin/systems/:id/openapi/import;
   - GET /admin/systems/:id/openapi;
   - GET /admin/systems/:id/operations.
11. Proteções para importação por URL:
   - somente HTTPS;
   - bloqueio de localhost;
   - bloqueio de IPs privados;
   - limite de tamanho;
   - timeout;
   - limite de redirects.
12. Testes com documentos OpenAPI válidos e inválidos.

RESTRIÇÕES

- Não gerar ferramentas MCP ainda.
- Não executar chamadas na API externa.
- Nenhuma operação deve ficar enabled=true automaticamente.
- Não seguir referências externas inseguras sem validação.

CRITÉRIOS DE ACEITAÇÃO

- importar JSON e YAML;
- listar operações normalizadas;
- rejeitar documento inválido;
- bloquear URLs internas e potenciais SSRF;
- evitar importação duplicada pelo checksum;
- todas as operações começam desativadas;
- testes e build passam.

Ao terminar, entregue o relatório técnico obrigatório.
```

---

## Épico 4 — Curadoria e catálogo de ferramentas

## Objetivo

Permitir que apenas operações escolhidas sejam transformadas em ferramentas.

Uma API pode conter 300 endpoints. O produto não deve entregar uma bazuca para a IA e torcer pela maturidade dela.

## Entregáveis

- habilitar/desabilitar operação;
- editar nome da ferramenta;
- editar descrição;
- restringir campos;
- configurar risco;
- configurar timeout;
- configurar aprovação.

## Prompt para Claude

```
Execute o ÉPICO 4 — CATÁLOGO CONTROLADO DE FERRAMENTAS.

OBJETIVO

Transformar operações OpenAPI selecionadas em definições internas de ferramentas, sem expor automaticamente todos os endpoints.

ENTIDADE

ToolDefinition:
- id;
- workspaceId;
- connectedSystemId;
- apiOperationId;
- name;
- title;
- description;
- inputSchema;
- outputSchema;
- riskLevel;
- requiresApproval;
- timeoutMs;
- enabled;
- allowedRequestFields;
- blockedRequestFields;
- staticParameters;
- createdAt;
- updatedAt.

NÍVEIS DE RISCO

- READ;
- WRITE;
- CRITICAL.

IMPLEMENTE

1. Serviço para criar uma ferramenta a partir de uma ApiOperation.
2. Conversão dos parâmetros OpenAPI para JSON Schema compatível com MCP.
3. Nomes seguros e determinísticos para ferramentas.
4. Validação de nomes duplicados por workspace.
5. Edição de:
   - nome;
   - título;
   - descrição;
   - risco;
   - timeout;
   - campos permitidos;
   - campos bloqueados;
   - parâmetros estáticos;
   - necessidade de aprovação.
6. Endpoints:
   - POST /admin/operations/:id/tools;
   - GET /admin/tools;
   - GET /admin/tools/:id;
   - PATCH /admin/tools/:id;
   - POST /admin/tools/:id/enable;
   - POST /admin/tools/:id/disable.
7. Defaults de segurança:
   - READ: sem aprovação;
   - WRITE: configurável;
   - CRITICAL: aprovação obrigatória;
   - DELETE: sempre CRITICAL;
   - ferramentas novas: desabilitadas.
8. Validação do inputSchema.
9. Testes de geração de schema.
10. Testes de campos permitidos e bloqueados.

REGRAS

- Não criar ferramenta genérica execute_http.
- Não permitir alteração de URL base por chamada da IA.
- Não permitir que a IA defina livremente headers de autenticação.
- Não expor schemas enormes sem normalização.
- Não implementar execução real neste épico.

CRITÉRIOS DE ACEITAÇÃO

- uma operação pode gerar uma ferramenta;
- ferramenta começa desabilitada;
- schemas são válidos;
- campos bloqueados não aparecem no schema final;
- operações DELETE exigem aprovação;
- nomes duplicados são rejeitados;
- testes e build passam.

Ao terminar, entregue o relatório técnico obrigatório.
```

---

## Épico 5 — Executor REST seguro

## Objetivo

Executar uma ferramenta chamando a API real do sistema conectado.

## Fluxo

```
Entrada da ferramenta
      ↓
Validação
      ↓
Aplicação de campos fixos
      ↓
Construção segura da requisição
      ↓
Credenciais do workspace
      ↓
API externa
      ↓
Normalização da resposta
```

## Prompt para Claude

```
Execute o ÉPICO 5 — EXECUTOR REST SEGURO.

OBJETIVO

Implementar o mecanismo interno que executa uma ToolDefinition contra a API REST do ConnectedSystem.

IMPLEMENTE

1. Validação dos argumentos com base no inputSchema da ferramenta.
2. Separação correta entre:
   - path parameters;
   - query parameters;
   - request body;
   - headers controlados.
3. Aplicação dos staticParameters.
4. Aplicação das credenciais do ConnectedSystem.
5. Construção segura da URL.
6. Bloqueio de:
   - mudança do host;
   - path traversal;
   - protocolo diferente de HTTPS em produção;
   - redirects para hosts não autorizados;
   - headers arbitrários;
   - credential forwarding.
7. Timeout por ferramenta.
8. Limite de tamanho da resposta.
9. Normalização de respostas JSON.
10. Tratamento de respostas não JSON.
11. Mapeamento de erros externos.
12. Redação de dados sensíveis.
13. Idempotency-Key para operações compatíveis.
14. Endpoint administrativo de teste:
   - POST /admin/tools/:id/test.
15. Modo dry-run que retorna a requisição planejada sem executá-la.
16. Testes usando servidor HTTP simulado.

FORMATO DE RESULTADO INTERNO

- success;
- statusCode;
- data;
- errorCode;
- errorMessage;
- durationMs;
- externalRequestId;
- truncated.

REGRAS

- A URL base vem somente do ConnectedSystem.
- Credenciais nunca podem vir dos argumentos da ferramenta.
- Credenciais nunca devem ser retornadas.
- Não realizar retry automático em POST, PATCH ou DELETE sem garantia de idempotência.
- Nunca registrar corpo completo quando contiver campos sensíveis.
- Ferramentas CRITICAL não podem ser executadas pelo endpoint de teste sem confirmação explícita.

CRITÉRIOS DE ACEITAÇÃO

- operações GET e POST funcionam;
- path, query e body são montados corretamente;
- host não pode ser sobrescrito;
- timeout funciona;
- respostas grandes são truncadas com indicação;
- dry-run não executa a requisição;
- testes e build passam.

Ao terminar, entregue o relatório técnico obrigatório.
```

---

## Épico 6 — Servidor MCP remoto

## Objetivo

Expor as ferramentas habilitadas por meio de um servidor MCP remoto.

## Resultado

O cliente receberá um endpoint semelhante a:

```
https://bridge.exemplo.com/mcp
```

Com autenticação vinculada ao workspace.

## Prompt para Claude

```
Execute o ÉPICO 6 — SERVIDOR MCP REMOTO.

OBJETIVO

Disponibilizar as ToolDefinitions habilitadas como ferramentas MCP remotas usando Streamable HTTP.

IMPLEMENTE

1. Integração com o SDK oficial do MCP.
2. Endpoint MCP remoto.
3. Autenticação do workspace.
4. Listagem dinâmica das ferramentas habilitadas.
5. Conversão de ToolDefinition para definição MCP.
6. Execução de ferramentas por meio do REST Executor.
7. Validação de argumentos antes da execução.
8. Formatação adequada dos resultados MCP.
9. Isolamento de ferramentas por workspace.
10. Limite de concorrência por workspace.
11. Cancelamento e timeout.
12. Identificadores de correlação.
13. Tratamento correto de erros sem expor stack trace.
14. Endpoint administrativo:
   - GET /admin/mcp/config.
15. Geração de instruções de conexão.
16. Cliente MCP de teste para validação end-to-end.
17. Testes:
   - listar ferramentas;
   - executar ferramenta READ;
   - rejeitar ferramenta desabilitada;
   - impedir acesso entre workspaces;
   - validar input inválido.

AUTENTICAÇÃO INICIAL

Utilize Bearer Token específico para conexão MCP.

Armazene somente o hash do token.

O token deve possuir:

- workspaceId;
- nome;
- prefixo;
- expiração opcional;
- status;
- data de último uso.

RESTRIÇÕES

- Não implementar frontend.
- Não implementar agente.
- Não depender de Claude especificamente.
- Não expor ferramentas desabilitadas.
- Não expor ferramentas de outros workspaces.
- Não permitir token administrativo como substituto automático do token MCP.

CRITÉRIOS DE ACEITAÇÃO

- cliente MCP consegue listar ferramentas;
- cliente MCP consegue executar uma ferramenta READ;
- ferramenta WRITE passa pelo mecanismo existente;
- token inválido é rejeitado;
- workspace A não acessa ferramentas do workspace B;
- testes end-to-end e build passam.

Ao terminar, entregue o relatório técnico obrigatório.
```

---

## Épico 7 — Policy Engine e limites operacionais

## Objetivo

Evitar que a IA execute ações permitidas tecnicamente, mas proibidas comercial ou operacionalmente.

## Exemplos

```
Pode atualizar telefone
Não pode atualizar saldo

Pode listar pedidos
Não pode cancelar mais de 3 pedidos por execução

Pode criar tarefas
Não pode criar 500 tarefas de uma vez
```

## Prompt para Claude

```
Execute o ÉPICO 7 — POLICY ENGINE.

OBJETIVO

Criar uma camada de políticas aplicada antes da execução de qualquer ferramenta MCP.

ENTIDADES

Policy:
- id;
- workspaceId;
- toolDefinitionId opcional;
- name;
- type;
- configuration;
- enabled;
- priority;
- createdAt;
- updatedAt.

TIPOS INICIAIS

- FIELD_ALLOWLIST;
- FIELD_BLOCKLIST;
- VALUE_ALLOWLIST;
- MAX_ITEMS;
- RATE_LIMIT;
- TIME_WINDOW;
- REQUIRE_APPROVAL;
- BLOCK_EXECUTION.

IMPLEMENTE

1. Pipeline de avaliação de políticas.
2. Políticas globais do workspace.
3. Políticas específicas por ferramenta.
4. Ordem de prioridade.
5. Resultado estruturado:
   - ALLOW;
   - DENY;
   - REQUIRE_APPROVAL.
6. Mensagem segura explicando o bloqueio.
7. Rate limit:
   - por token;
   - por workspace;
   - por ferramenta.
8. Limite de quantidade de itens em arrays.
9. Bloqueio de campos sensíveis.
10. Restrição de valores.
11. Janela de horário.
12. Endpoints administrativos para criar, editar, listar e desativar políticas.
13. Aplicação obrigatória da política antes do REST Executor.
14. Testes de conflitos e precedência.

REGRAS

- DENY sempre prevalece sobre ALLOW.
- Ação CRITICAL sempre exige aprovação.
- Política nunca pode ser ignorada por argumento enviado pela IA.
- Não criar linguagem de regras complexa neste épico.
- A configuração deve usar JSON validado por schema.

CRITÉRIOS DE ACEITAÇÃO

- bloquear campo proibido;
- limitar número de registros;
- aplicar rate limit;
- exigir aprovação conforme política;
- registrar motivo da decisão;
- testes e build passam.

Ao terminar, entregue o relatório técnico obrigatório.
```

---

## Épico 8 — Auditoria e rastreabilidade

## Objetivo

Registrar quem pediu, o que foi decidido e o que ocorreu.

## Registro mínimo

```
Workspace
Token
Ferramenta
Argumentos redigidos
Decisão da política
Aprovação
Código de resposta
Duração
Erro
Timestamp
```

## Prompt para Claude

```
Execute o ÉPICO 8 — AUDITORIA E RASTREABILIDADE.

OBJETIVO

Registrar de forma segura e consultável todas as tentativas de execução de ferramentas.

ENTIDADE

ExecutionLog:
- id;
- workspaceId;
- connectedSystemId;
- toolDefinitionId;
- mcpTokenId;
- correlationId;
- status;
- riskLevel;
- redactedArguments;
- policyDecision;
- policyReason;
- approvalId;
- externalStatusCode;
- responseSummary;
- errorCode;
- errorMessage;
- durationMs;
- startedAt;
- completedAt;
- createdAt.

STATUS

- RECEIVED;
- VALIDATION_FAILED;
- POLICY_DENIED;
- PENDING_APPROVAL;
- EXECUTING;
- SUCCEEDED;
- FAILED;
- TIMED_OUT;
- CANCELLED.

IMPLEMENTE

1. Criação do log no início da solicitação.
2. Atualização do mesmo registro durante o ciclo de vida.
3. Redação configurável de campos sensíveis.
4. Correlação entre MCP, política, aprovação e execução externa.
5. Endpoints:
   - GET /admin/executions;
   - GET /admin/executions/:id.
6. Filtros por:
   - data;
   - status;
   - ferramenta;
   - sistema;
   - risco;
   - correlationId.
7. Paginação.
8. Retenção configurável.
9. Serviço de limpeza de logs expirados.
10. Logs internos separados da trilha de auditoria.
11. Testes de redação.
12. Testes de isolamento por workspace.

REGRAS

- Nunca armazenar tokens ou credenciais.
- Não armazenar corpos completos por padrão.
- Campos como password, token, secret, authorization e apiKey devem ser redigidos.
- Auditoria não pode impedir uma execução por falha secundária silenciosa; falhas de auditoria devem ser tratadas explicitamente.
- Não retornar logs de outro workspace.

CRITÉRIOS DE ACEITAÇÃO

- cada chamada MCP gera trilha;
- chamadas negadas também são registradas;
- dados sensíveis são redigidos;
- filtros e paginação funcionam;
- testes e build passam.

Ao terminar, entregue o relatório técnico obrigatório.
```

---

## Épico 9 — Aprovação de ações críticas

## Objetivo

Permitir que a IA prepare uma ação, mas só execute após autorização humana.

## Fluxo

```
IA solicita cancelamento
        ↓
Policy Engine exige aprovação
        ↓
Sistema cria Approval Request
        ↓
Operador aprova
        ↓
Execução ocorre uma única vez
```

## Prompt para Claude

```
Execute o ÉPICO 9 — APROVAÇÃO DE AÇÕES CRÍTICAS.

OBJETIVO

Implementar um workflow simples de aprovação humana para ferramentas WRITE ou CRITICAL.

ENTIDADE

ApprovalRequest:
- id;
- workspaceId;
- toolDefinitionId;
- executionLogId;
- requestedArgumentsEncrypted;
- argumentsSummary;
- status;
- requestedAt;
- expiresAt;
- decidedAt;
- decidedBy;
- decisionReason;
- executionStartedAt;
- executionCompletedAt;
- createdAt;
- updatedAt.

STATUS

- PENDING;
- APPROVED;
- REJECTED;
- EXPIRED;
- EXECUTED;
- EXECUTION_FAILED.

IMPLEMENTE

1. Criação da solicitação quando a política retornar REQUIRE_APPROVAL.
2. Armazenamento seguro dos argumentos originais.
3. Resumo redigido para revisão humana.
4. Expiração automática.
5. Endpoints:
   - GET /admin/approvals;
   - GET /admin/approvals/:id;
   - POST /admin/approvals/:id/approve;
   - POST /admin/approvals/:id/reject.
6. Execução após aprovação.
7. Garantia de execução única.
8. Proteção contra:
   - aprovação duplicada;
   - replay;
   - alteração dos argumentos;
   - aprovação após expiração.
9. Atualização da trilha de auditoria.
10. Resultado MCP indicando que a solicitação está aguardando aprovação.
11. Testes de concorrência.
12. Testes de expiração e replay.

REGRAS

- Aprovar não pode aceitar novos argumentos.
- A execução deve usar exatamente os argumentos que foram revisados.
- Ações DELETE sempre passam por aprovação.
- Uma aprovação expirada não pode ser reativada.
- Não implementar notificações externas neste épico.
- Não implementar painel visual.

CRITÉRIOS DE ACEITAÇÃO

- ação crítica cria solicitação;
- aprovação executa a ação uma única vez;
- rejeição impede execução;
- argumentos não podem ser alterados;
- replay é bloqueado;
- auditoria registra todo o fluxo;
- testes e build passam.

Ao terminar, entregue o relatório técnico obrigatório.
```

---

## Épico 10 — CRM fictício e demonstração comercial

## Objetivo

Criar uma demonstração que qualquer comprador entenda em menos de um minuto.

## Sistema fictício

Criar o **Acme CRM** com:

- clientes;
- leads;
- tarefas;
- pedidos;
- cobranças.

## Ferramentas demonstrativas

```
list_leads
search_customers
create_customer
update_lead_status
create_task
list_overdue_invoices
update_order_status
generate_sales_summary
```

## Prompt para Claude

```
Execute o ÉPICO 10 — DEMONSTRAÇÃO COMERCIAL ACME CRM.

OBJETIVO

Criar um sistema fictício simples e integrá-lo ao SystemBridge para demonstrar o fluxo completo OpenAPI → ToolDefinition → MCP → execução.

IMPLEMENTE

1. Um módulo demo chamado Acme CRM.
2. Entidades fictícias:
   - Customer;
   - Lead;
   - Task;
   - Order;
   - Invoice.
3. Seeds realistas:
   - 20 clientes;
   - 30 leads;
   - 15 pedidos;
   - 5 cobranças vencidas.
4. API REST documentada com OpenAPI.
5. Endpoints necessários para gerar as ferramentas:
   - list_leads;
   - search_customers;
   - create_customer;
   - update_lead_status;
   - create_task;
   - list_overdue_invoices;
   - update_order_status;
   - generate_sales_summary.
6. Script automatizado que:
   - cria workspace demo;
   - cria sistema conectado;
   - importa o OpenAPI;
   - cria ToolDefinitions;
   - habilita as ferramentas;
   - cria token MCP.
7. Cenário end-to-end:
   - listar leads sem contato;
   - atualizar prioridade;
   - criar tarefas;
   - registrar logs.
8. Cenário crítico:
   - alteração de status sensível;
   - geração de aprovação;
   - aprovação;
   - execução.
9. Coleção de exemplos curl.
10. Arquivo DEMO.md.
11. Testes end-to-end completos.

ROTEIRO DE DEMONSTRAÇÃO

A demonstração deverá suportar:

“Encontre os leads sem contato há mais de cinco dias.”

Depois:

“Marque os três maiores como prioridade e crie tarefas para amanhã.”

Quando necessário, a execução deve retornar uma solicitação de aprovação.

REGRAS

- O módulo demo deve ficar isolado do núcleo.
- Não misturar dados demo com workspaces reais.
- O seed deve ser determinístico.
- Não criar frontend.
- Não depender de APIs pagas.

CRITÉRIOS DE ACEITAÇÃO

- ambiente demo sobe com um comando;
- MCP lista as ferramentas do Acme CRM;
- fluxo de leitura funciona;
- fluxo de escrita funciona;
- fluxo de aprovação funciona;
- logs mostram todo o ciclo;
- testes e build passam.

Ao terminar, entregue o relatório técnico obrigatório.
```

---

## Épico 11 — Deploy comercial mínimo

## Objetivo

Publicar o SystemBridge com segurança suficiente para os primeiros clientes-piloto.

## Infraestrutura mínima

```
VPS
 ├── Traefik ou Caddy
 ├── SystemBridge
 ├── PostgreSQL
 └── Backup
```

## Prompt para Claude

```
Execute o ÉPICO 11 — DEPLOY COMERCIAL MÍNIMO.

OBJETIVO

Preparar o SystemBridge para implantação em uma VPS Docker com HTTPS, banco persistente e procedimentos operacionais básicos.

IMPLEMENTE

1. Dockerfile de produção multi-stage.
2. Docker Compose de produção.
3. Healthcheck de container.
4. Configuração para reverse proxy.
5. HTTPS obrigatório em produção.
6. Headers de segurança.
7. Limite de tamanho de request.
8. Configuração de CORS restritiva.
9. Rate limiting global.
10. Usuário não root no container.
11. Persistência PostgreSQL.
12. Script de migration.
13. Script de backup.
14. Script de restauração documentado.
15. Rotação de logs.
16. Endpoint de readiness.
17. Endpoint de liveness.
18. Checklist de variáveis de ambiente.
19. RUNBOOK.md.
20. DEPLOYMENT.md.
21. Procedimento de rotação de:
   - master encryption key;
   - API keys;
   - MCP tokens;
   - credenciais externas.
22. Smoke test após deploy.

RESTRIÇÕES

- Não implementar Kubernetes.
- Não implementar alta disponibilidade.
- Não implementar autoscaling.
- Não adicionar serviços sem necessidade.
- Não colocar segredos dentro da imagem Docker.
- Não expor PostgreSQL publicamente.

CRITÉRIOS DE ACEITAÇÃO

- aplicação sobe em modo produção;
- banco não fica exposto;
- HTTPS é suportado pelo reverse proxy;
- migrations são executáveis;
- backup e restauração estão documentados;
- healthchecks funcionam;
- smoke test valida o endpoint MCP;
- build e testes passam.

Ao terminar, entregue o relatório técnico obrigatório.
```

---

## Épico 12 — Kit de implantação de clientes

## Objetivo

Transformar o código em um serviço repetível.

O primeiro cliente não pode exigir reconstrução completa. Cada implantação deve ser principalmente configuração.

## Entregáveis

- questionário técnico;
- checklist de API;
- modelo de mapeamento;
- template de políticas;
- procedimento de homologação;
- relatório de entrega.

## Prompt para Claude

```
Execute o ÉPICO 12 — KIT DE IMPLANTAÇÃO DE CLIENTES.

OBJETIVO

Criar os materiais e scripts necessários para configurar um novo cliente de forma padronizada.

CRIE

1. docs/client-onboarding/questionnaire.md
2. docs/client-onboarding/api-requirements.md
3. docs/client-onboarding/security-checklist.md
4. docs/client-onboarding/tool-mapping-template.md
5. docs/client-onboarding/policy-template.md
6. docs/client-onboarding/homologation-checklist.md
7. docs/client-onboarding/delivery-report-template.md
8. docs/client-onboarding/client-connection-guide.md
9. examples/client-config.example.json
10. scripts/bootstrap-client.ts

O QUESTIONÁRIO DEVE LEVANTAR

- nome do sistema;
- URL da API;
- ambiente de homologação;
- ambiente de produção;
- documentação OpenAPI;
- forma de autenticação;
- operações desejadas;
- campos sensíveis;
- ações que exigem aprovação;
- limites de volume;
- usuários responsáveis;
- retenção de logs;
- SLA esperado.

O SCRIPT bootstrap-client DEVE

1. criar workspace;
2. cadastrar ConnectedSystem;
3. importar OpenAPI;
4. listar operações;
5. aceitar uma allowlist de operationIds;
6. gerar ToolDefinitions;
7. aplicar políticas declarativas;
8. gerar token MCP;
9. produzir um relatório sem expor segredos.

REGRAS

- O script não pode habilitar endpoints fora da allowlist.
- DELETE deve permanecer crítico.
- Credenciais devem ser fornecidas por variáveis de ambiente ou entrada segura.
- Não incluir credenciais nos arquivos de exemplo.
- Documentar rollback.

CRITÉRIOS DE ACEITAÇÃO

- um novo workspace demo pode ser configurado pelo script;
- somente operações permitidas são expostas;
- políticas são aplicadas;
- token MCP é gerado;
- guia de conexão é produzido;
- build e testes passam.

Ao terminar, entregue o relatório técnico obrigatório.
```

---

## Ordem de execução

## MVP demonstrável

Execute primeiro:

```
Épico 1 — Fundação
Épico 2 — Workspaces e credenciais
Épico 3 — Importação OpenAPI
Épico 4 — Catálogo de ferramentas
Épico 5 — Executor REST
Épico 6 — Servidor MCP
Épico 10 — Demonstração
```

Nesse ponto já existe algo vendável para demonstração.

## MVP comercial seguro

Depois:

```
Épico 7 — Policy Engine
Épico 8 — Auditoria
Épico 9 — Aprovações
Épico 11 — Deploy
Épico 12 — Kit de implantação
```

---

## Definição da versão 0.1

A versão inicial estará pronta quando conseguir executar este ciclo:

```
1. Criar workspace
2. Cadastrar sistema
3. Informar credencial
4. Importar OpenAPI
5. Selecionar endpoints
6. Gerar ferramentas
7. Criar token MCP
8. Conectar uma IA
9. Listar ferramentas
10. Consultar dados
11. Escrever dados
12. Bloquear ações proibidas
13. Aprovar ações críticas
14. Consultar auditoria
```

## Regra para conduzir Claude

Envie **um épico por vez**. Depois de cada entrega, mande:

```
Revise criticamente a implementação do épico anterior.

1. Verifique se todos os critérios de aceitação foram atendidos.
2. Execute lint, testes e build.
3. Procure:
   - falhas de isolamento entre workspaces;
   - vazamento de credenciais;
   - endpoints sem autenticação;
   - validações incompletas;
   - tratamento genérico de erros;
   - código duplicado;
   - dependências desnecessárias;
   - mocks presentes no caminho de produção.
4. Corrija os problemas encontrados.
5. Não avance para o próximo épico.
6. Entregue o relatório final de validação.
```

Isso impede o clássico efeito “Claude construiu uma cidade futurista, mas esqueceu de ligar o esgoto”.

[^1]: [modelcontextprotocol.io](https://modelcontextprotocol.io/docs/getting-started/intro?utm_source=chatgpt.com)

[^2]: [github.com](https://github.com/nousresearch/hermes-agent?utm_source=chatgpt.com)

[^3]: [openclaw.ai](https://openclaw.ai/?utm_source=chatgpt.com)

[^4]: [docs.anthropic.com](https://docs.anthropic.com/en/release-notes/claude-apps?utm_source=chatgpt.com)

[^5]: [spec.openapis.org](https://spec.openapis.org/oas/v3.1.1.html?utm_source=chatgpt.com)

[^6]: [modelcontextprotocol.io](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization?utm_source=chatgpt.com)

[^7]: [github.com](https://github.com/modelcontextprotocol/typescript-sdk?utm_source=chatgpt.com)