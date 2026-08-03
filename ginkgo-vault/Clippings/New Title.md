---
title: "New Title"
source: "https://chatgpt.com/c/6a5b85f7-d5a8-83e9-babd-4c2e8ffc3f64"
author:
published:
created: 2026-07-23
description: "ChatGPT conversation with 7 messages"
tags:
  - "clippings"
---
**Você disse**

---

**Você disse**

podemos validar nós mesmo? utilizando a melhor opção para cada com o resultado final sendo este? somar a uma dashboard de configuração e criação entre aspas em massa, exemplo 30 bots, tornar replicavel, copia e cola.

---

## Veredito

**Sim. É viável construir uma plataforma própria com o resultado visual e funcional semelhante ao painel da imagem, preparada para operar 30, 100 ou mais bots a partir de templates.**

A mudança decisiva é que o Telegram agora oferece oficialmente o conceito de **Management Bot**. Um bot principal pode ser habilitado no BotFather para permitir que usuários criem bots gerenciados por ele. Após a confirmação da criação, o bot gerenciador recebe um evento `managed_bot`, consegue obter o token com `getManagedBotToken` e também pode rotacioná-lo posteriormente. Isso elimina boa parte do trabalho artesanal que antes exigia copiar tokens manualmente. [^1]

O escopo deve permanecer voltado a conteúdo premium lícito e não explícito: comunidades, cursos, creators, clubes, newsletters, mentorias e bibliotecas digitais.

---

## 1\. Produto final

O produto seria uma espécie de:

## Ginkgo Bot Factory

```
Painel central
   │
   ├── Criar ou conectar bot
   ├── Aplicar template
   ├── Personalizar marca
   ├── Configurar produtos
   ├── Configurar pagamentos
   ├── Configurar campanhas
   ├── Publicar
   └── Monitorar vendas e usuários
            │
            ▼
    30+ bots operando
    no mesmo motor central
```

Não teremos 30 projetos, 30 bancos e 30 instalações.

Teremos:

```
1 plataforma
1 backend
1 painel
1 banco multi-tenant
1 infraestrutura de filas
30 configurações de bots
```

Cada bot será uma “skin” independente sobre o mesmo motor.

---

## 2\. Validação do modelo da imagem

O painel apresentado possui os seguintes domínios funcionais:

| Área visível | Função equivalente na plataforma |
| --- | --- |
| Dashboard | Receita, conversão e atividade |
| Meus Robôs | Gestão dos bots |
| Meus Fluxos | Funis e árvores de mensagens |
| Redirecionadores | Links rastreáveis e deep links |
| Remarketing | Campanhas e recuperação |
| Postagens | Broadcasts e agendamentos |
| Gateways | Configuração financeira |
| Rastreamento | Pixels, UTM e eventos |
| Checkout | Produtos, ofertas e pedidos |
| Bio Link | Landing page pública |
| Webhooks | Integrações externas |
| Clientes | Base de usuários |
| Financeiro | Pedidos, pagamentos e repasses |
| Afiliados | Comissões e referências |
| Ranking e premiações | Gamificação |
| Roleta | Recompensas e aquisição |

Tecnicamente, tudo isso é reproduzível. Porém, o MVP não deve copiar todos os botões do painel logo de início. Isso produziria um porta-aviões antes de validar se o motor liga.

---

## 3\. Arquitetura correta

```
CONTROL PLANE
                Painel administrativo Next.js
                             │
            ┌────────────────┼────────────────┐
            ▼                ▼                ▼
      Configurações       Templates       Analytics
            │                │                │
            └────────────────┼────────────────┘
                             ▼
                    API multi-tenant
                   NestJS + TypeScript
                             │
       ┌─────────────────────┼─────────────────────┐
       ▼                     ▼                     ▼
Bot Provisioner        Flow Engine           Commerce Engine
       │                     │                     │
       ▼                     ▼                     ▼
Telegram API         Redis + BullMQ         Orders + Stars
       │                     │                     │
       └─────────────────────┼─────────────────────┘
                             ▼
                   PostgreSQL / Supabase
                             │
               ┌─────────────┴─────────────┐
               ▼                           ▼
         Object Storage                  n8n
           R2/S3              Integrações e automações
```

## Control plane

É o painel semelhante ao da imagem:

- cria bots;
- clona templates;
- altera conteúdo;
- configura produtos;
- publica campanhas;
- consulta métricas;
- gerencia clientes.

## Data plane

É o motor invisível:

- recebe os webhooks;
- responde aos comandos;
- controla carrinhos;
- registra pagamentos;
- entrega produtos;
- dispara campanhas;
- controla permissões.

Essa separação impede que o painel administrativo e os bots se transformem em um único monólito radioativo.

---

## 4\. Melhor tecnologia para cada camada

| Camada | Escolha recomendada | Motivo |
| --- | --- | --- |
| Painel | Next.js + TypeScript | Interface, SSR e ecossistema |
| Componentes | shadcn/ui + Tailwind | Dashboard rápido e consistente |
| API | NestJS com Fastify | Modularidade e alto volume de eventos |
| Telegram | grammY | Middleware, sessões e TypeScript |
| Banco | PostgreSQL/Supabase | Multi-tenant e transações |
| ORM | Prisma ou Drizzle | Schema e migrations |
| Filas | Redis + BullMQ | Campanhas, entregas e retries |
| Fluxos | Engine JSON própria | Versionamento e clonagem |
| Automações | n8n | CRM, relatórios e integrações |
| Arquivos | Cloudflare R2 | Armazenamento de mídias |
| Analytics inicial | PostgreSQL | Suficiente no MVP |
| Analytics futuro | ClickHouse | Eventos em grande escala |
| Monitoramento | Sentry + OpenTelemetry | Erros e rastreamento |
| Deploy | Docker + Traefik | Compatível com sua VPS |
| Segredos | Vault/KMS ou criptografia de aplicação | Proteção dos tokens |

## Papel do n8n

O n8n entra como braço robótico, não como cérebro principal.

Use para:

```
CRM
Relatórios
Alertas
Recuperação de usuários
Notificações administrativas
Integrações externas
Sincronização de dados
```

Não use como núcleo de:

```
Callbacks
Carrinho
Pagamento
Controle de acesso
Entrega
Sessões
Idempotência
```

---

## 5\. Criação em massa de bots

Existem dois caminhos oficiais.

## Caminho A — Management Bot

É a melhor escolha para o produto.

O operador cria um bot gerenciador e ativa o **Bot Management Mode**. A plataforma gera links com nome e username pré-preenchidos:

```
https://t.me/newbot/ManagerBot/NovoBotUsername?name=Novo+Bot
```

O usuário confirma a criação no Telegram. Depois disso:

```
Telegram cria o bot
        ↓
Manager recebe managed_bot
        ↓
Backend chama getManagedBotToken
        ↓
Token é criptografado
        ↓
Webhook é configurado
        ↓
Template é aplicado
        ↓
Bot fica online
```

Esse mecanismo é documentado oficialmente pelo Telegram. [^1]

## Caminho B — Conectar token existente

O operador já criou o bot e cola o token:

```
Adicionar bot
→ informar token
→ validar getMe
→ registrar webhook
→ aplicar template
→ publicar
```

O painel deve suportar os dois caminhos:

```
[ Criar bot automaticamente ]
[ Conectar bot existente ]
```

## Limitação operacional

O processo via Management Bot ainda inclui uma confirmação do proprietário no Telegram. Portanto, para 30 bots teremos aproximadamente:

```
90% automatizado
10% confirmação oficial do Telegram
```

Não recomendo automatizar contas pessoais ou sessões de usuário para contornar essa confirmação.

---

## 6\. Processo de provisionamento

Ao criar um bot, o backend executará um job:

```
PROVISION_REQUESTED
        ↓
BOT_CREATED_OR_CONNECTED
        ↓
TOKEN_VALIDATED
        ↓
TOKEN_ENCRYPTED
        ↓
WEBHOOK_REGISTERED
        ↓
PROFILE_CONFIGURED
        ↓
COMMANDS_CONFIGURED
        ↓
TEMPLATE_CLONED
        ↓
ASSETS_ATTACHED
        ↓
SMOKE_TEST_EXECUTED
        ↓
ACTIVE
```

Rota de webhook por bot:

```
POST /webhooks/telegram/{botPublicId}
```

Cada bot terá um `secret_token` próprio. O Telegram envia esse segredo no cabeçalho `X-Telegram-Bot-Api-Secret-Token`, permitindo validar as chamadas recebidas. [^2]

Exemplo interno:

```
/webhooks/telegram/bot_01
/webhooks/telegram/bot_02
/webhooks/telegram/bot_03
```

Não exponha o token verdadeiro na URL.

---

## 7\. Template “copia e cola”

O coração do produto será um blueprint versionado.

```json
{
  "name": "creator-premium-v1",
  "version": 1,
  "branding": {
    "displayName": "{{BOT_NAME}}",
    "supportUsername": "{{SUPPORT_USERNAME}}",
    "language": "pt-BR"
  },
  "startFlow": "flow_welcome",
  "menus": [
    {
      "id": "home",
      "buttons": [
        {
          "label": "Comunidade Premium",
          "action": "flow:membership"
        },
        {
          "label": "Biblioteca",
          "action": "flow:catalog"
        },
        {
          "label": "Minhas compras",
          "action": "purchases:list"
        },
        {
          "label": "Suporte",
          "action": "support:open"
        }
      ]
    }
  ],
  "flows": [
    {
      "id": "flow_welcome",
      "steps": [
        {
          "type": "send_media",
          "asset": "{{WELCOME_MEDIA}}"
        },
        {
          "type": "send_message",
          "text": "{{WELCOME_TEXT}}"
        },
        {
          "type": "show_menu",
          "menuId": "home"
        }
      ]
    }
  ]
}
```

Ao clonar:

```
Template base
   ↓
Substituir variáveis
   ↓
Criar produtos
   ↓
Copiar fluxos
   ↓
Copiar campanhas
   ↓
Associar mídias
   ↓
Publicar
```

## Importação em massa

O painel pode aceitar CSV:

```
name,username,template,brand,support,language
Academy One,academy_one_bot,course-v1,academy-one,@support,pt-BR
Community Two,community_two_bot,community-v1,community-two,@support,en-US
News Three,news_three_bot,newsletter-v1,news-three,@support,pt-BR
```

Depois:

```
Importar CSV
→ validar usernames
→ gerar 30 provisionamentos
→ criar links oficiais
→ acompanhar confirmações
→ ativar automaticamente
```

---

## 8\. Runtime para 30 bots

Não precisamos iniciar um servidor separado para cada bot.

```
Telegram updates
        ↓
Bot Gateway compartilhado
        ↓
Identificar bot pelo webhook
        ↓
Carregar configuração do Redis
        ↓
Executar fluxo
        ↓
Persistir evento
```

Cache:

```
bot:{botId}:config
bot:{botId}:commands
bot:{botId}:template
bot:{botId}:rate_limit
```

Banco:

```
bots
bot_credentials
bot_settings
bot_templates
flow_definitions
flow_versions
flow_executions
users
user_states
products
orders
payments
entitlements
campaigns
campaign_deliveries
```

Todas as tabelas operacionais devem carregar:

```
tenant_id
bot_id
```

Assim, os dados do Bot A nunca cruzam com o Bot B.

---

## 9\. Motor de fluxos

A área “Meus Fluxos” não deve usar workflows n8n diretamente.

Ela deve funcionar como uma máquina de estados própria:

```
Trigger
   ↓
Condição
   ↓
Mensagem
   ↓
Botões
   ↓
Aguardar
   ↓
Segmentar
   ↓
Criar pedido
   ↓
Entregar
```

Tipos de nós:

```
Start
Send Message
Send Media
Show Buttons
Condition
Delay
Set Variable
HTTP Request
Create Order
Send Invoice
Check Entitlement
Grant Access
Revoke Access
Add Tag
Remove Tag
Start Another Flow
End
```

Representação:

```json
{
  "id": "flow_membership",
  "nodes": [
    {
      "id": "start",
      "type": "trigger"
    },
    {
      "id": "offer",
      "type": "send_message",
      "data": {
        "template": "membership_offer"
      }
    },
    {
      "id": "decision",
      "type": "buttons",
      "data": {
        "buttons": [
          {
            "label": "Assinar",
            "next": "checkout"
          },
          {
            "label": "Voltar",
            "next": "home"
          }
        ]
      }
    },
    {
      "id": "checkout",
      "type": "create_order"
    }
  ]
}
```

Isso torna qualquer fluxo clonável e versionável.

---

## 10\. Pagamentos

Para bens digitais, assinaturas e acesso a conteúdo dentro do Telegram, o método nativo deve ser **Telegram Stars**, usando moeda `XTR`. O fluxo oficial utiliza `sendInvoice`, `pre_checkout_query`, `answerPreCheckoutQuery` e `successful_payment`. O identificador `telegram_payment_charge_id` deve ser armazenado para reconciliação e possíveis reembolsos. [^3]

O dashboard pode suportar:

| Gateway | Uso |
| --- | --- |
| Telegram Stars | Produtos digitais dentro do Telegram |
| Pix | Produtos físicos ou operações externas compatíveis |
| Stripe | SaaS, serviços externos e cobrança da plataforma |
| Mercado Pago | Operações externas compatíveis |
| Pagar.me | Operações externas compatíveis |

Para produto digital vendido e entregue dentro do bot ou Mini App, o Telegram exige Stars mesmo que existam outros portais ou gateways externos. [^3]

---

## 11\. Mini App

O bot continuará atendendo por mensagens, mas uma Mini App pode oferecer:

```
Catálogo
Carrinho
Biblioteca
Perfil
Histórico
Assinatura
Cupons
Área de afiliado
Dashboard do comprador
```

Mini Apps podem ser abertas por botões inline, pelo menu do bot ou diretamente pelo perfil. O servidor deve validar `initData`; o objeto `initDataUnsafe` não deve ser tratado como fonte confiável. [^4]

Arquitetura:

```
Bot
 ├── Conversas e notificações
 └── Botão “Abrir plataforma”
              ↓
          Mini App
              ↓
       API compartilhada
```

Para o MVP, não é obrigatória. Para um produto semelhante ao screenshot, torna-se importante na segunda fase.

---

## 12\. Remarketing em massa

Cada bot possui limite gratuito padrão de broadcast de até 30 mensagens por segundo. O Telegram também oferece Paid Broadcasts de até 1.000 mensagens por segundo, cobrando Stars por mensagem enviada acima do limite gratuito. [^2]

A fila deve ser isolada por bot:

```
campaign:{botId}
```

E aplicar:

```
Rate limit por bot
Retry exponencial
Controle de duplicidade
Opt-out
Quiet hours
Segmentação
Supressão de compradores
```

Exemplo:

```
Visualizou produto
        ↓
Não comprou em 2 horas
        ↓
Ainda não possui entitlement?
        ↓
Enviar recuperação
        ↓
Registrar clique
```

---

## 13\. Dashboard MVP

## Menu inicial recomendado

```
Visão Geral

Operação
├── Bots
├── Fluxos
├── Produtos
├── Clientes
├── Pedidos
└── Financeiro

Crescimento
├── Campanhas
├── Segmentos
├── Links rastreáveis
└── Afiliados

Configurações
├── Templates
├── Pagamentos
├── Webhooks
├── Equipe
└── Auditoria
```

## Deixar para depois

```
Ranking
Premiações
Roleta
Bio Link avançado
Marketplace
Gamificação
Relatórios extremamente detalhados
```

O painel mostrado possui boa amplitude, mas o MVP deve concentrar-se no motor que gera receita.

---

## 14\. Criação de 30 bots

O fluxo operacional ideal:

```
1. Criar template mestre
2. Importar CSV com 30 configurações
3. Validar nomes e usernames
4. Gerar 30 links de criação
5. Confirmar os bots no Telegram
6. Capturar tokens automaticamente
7. Registrar webhooks
8. Clonar o template
9. Aplicar marca e produtos
10. Executar smoke test
11. Ativar em lote
```

Tela:

```
Provisionamento em massa

Bot 01   Confirmado   Configurando   80%
Bot 02   Aguardando confirmação
Bot 03   Ativo
Bot 04   Erro no username
Bot 05   Teste aprovado
...
Bot 30   Ativo
```

Ações em massa:

```
Ativar
Pausar
Alterar template
Aplicar campanha
Trocar mensagem
Atualizar produto
Exportar configuração
Rotacionar credenciais
Executar testes
```

---

## 15\. Validação técnica

## Etapa 1 — Três bots

Construir:

```
1 bot gerenciador
3 bots gerenciados
1 template
1 catálogo
1 produto
1 fluxo
1 campanha
1 pagamento de teste
```

Critérios:

```
Criação oficial funcionando
Token recuperado
Webhook configurado
Template clonado
Pagamento registrado
Produto entregue
Dados isolados
```

## Etapa 2 — Dez bots

Validar:

```
Filas
Cache
Campanhas
Atualizações em massa
Isolamento multi-tenant
Falhas parciais
Rollback
```

## Etapa 3 — Trinta bots

Validar:

```
Provisionamento em lote
Carga simultânea
Broadcasts
Rotação de tokens
Recuperação de falhas
Observabilidade
Custos operacionais
```

Não iniciar diretamente com 30. O caminho seguro é:

```
3 → 10 → 30
```

---

## 16\. Critérios de aceite

A plataforma estará validada quando:

| Critério | Meta |
| --- | --- |
| Aplicar template após confirmação | menos de 2 minutos |
| Configurar webhook | automático |
| Clonar bot | sem copiar código |
| Vazamento entre tenants | zero |
| Entrega duplicada | zero |
| Pagamento sem entrega | detectado e reconciliado |
| Atualização de 30 bots | uma operação |
| Pausar bot comprometido | imediato |
| Restaurar versão anterior do fluxo | uma ação |
| Exportar configuração | JSON completo |
| Importar configuração | recriar bot funcional |

---

## 17\. Roadmap realista

## Epic 0 — Fundação

```
Monorepo
Autenticação
Tenants
RBAC
PostgreSQL
Redis
Auditoria
Docker
```

## Epic 1 — Bot Factory

```
Management Bot
Conectar token
Provisionamento
Webhooks
Tokens criptografados
Status dos bots
```

## Epic 2 — Template Engine

```
Blueprint JSON
Variáveis
Clonagem
Versionamento
Importação e exportação
```

## Epic 3 — Flow Builder

```
Editor visual
Nós
Conexões
Condições
Publicação
Rollback
```

## Epic 4 — Commerce

```
Produtos
Pedidos
Stars
Entitlements
Minhas compras
Entrega
```

## Epic 5 — Growth

```
Campanhas
Segmentos
Remarketing
Deep links
Afiliados
Analytics
```

## Epic 6 — Mass Operations

```
CSV
Provisionamento em lote
Alterações em massa
Testes em lote
Dashboard operacional
```

---

## Decisão final

A solução correta não é recriar cada bot individualmente.

É construir:

```
BOT FACTORY
+
TEMPLATE ENGINE
+
FLOW ENGINE
+
COMMERCE ENGINE
+
CAMPAIGN ENGINE
+
PAINEL MULTI-TENANT
```

A principal descoberta é que a criação escalável deixou de ser apenas uma gambiarra em torno do BotFather: o Telegram agora possui infraestrutura oficial para **managed bots**, o que encaixa diretamente no modelo de uma fábrica white-label. [^1]

O próximo artefato técnico deve ser o **Epic 0 + Epic 1**, com schema do banco, estrutura do monorepo, Docker Compose e fluxo completo de criação/conexão dos primeiros três bots.

---

**Você disse**

Certo, e falando das telas e configurações dos bots, o resultado esperado é como o dos prints.

---

Sim. O resultado final deve reproduzir **dois ambientes conectados**:

1. **Dashboard administrativo**, semelhante ao SharkBot do print.
2. **Experiência final dentro do Telegram**, semelhante aos fluxos enviados anteriormente.

Não será apenas uma lista de bots. Será um painel onde cada bot pode ser criado, configurado, clonado, publicado e operado sem editar código.

---

## 1\. Resultado visual esperado

## Dashboard principal

Estrutura semelhante ao print:

```
┌───────────────────────────────────────────────────────────────┐
│ Logo / Workspace                         Usuário / Ajuda       │
├──────────────┬────────────────────────────────────────────────┤
│ Dashboard    │ Faturamento       Conversão        Bots ativos │
│ Ranking      │                                                │
│ Análises     │ Meus Robôs                                     │
│ Financeiro   │                                                │
│ Clientes     │ [ Bot 01 ] [ Bot 02 ] [ Bot 03 ] [ + Novo ]   │
│ Comunidade   │                                                │
│              │ Leads  Vendas  Receita  Status  Template       │
│ Meus Robôs   │                                                │
│ Fluxos       │                                                │
│ Remarketing  │                                                │
│ Postagens    │                                                │
│ Gateways     │                                                │
│ Webhooks     │                                                │
└──────────────┴────────────────────────────────────────────────┘
```

Características:

- tema escuro;
- menu lateral fixo;
- cards de métricas;
- status visual do bot;
- busca e filtros;
- ações rápidas;
- edição por abas;
- criação individual ou em massa;
- indicadores em tempo real.

O objetivo não é copiar a marca SharkBot, mas atingir o mesmo padrão funcional com identidade própria da Ginkgo.

---

## 2\. Tela “Meus Robôs”

Essa será a central operacional.

Cada bot aparece como um card:

```
┌────────────────────────────┐
│ Avatar          ● ONLINE   │
│ Nome do bot                │
│ @username_bot              │
│                            │
│ Leads  1.248   Vendas 137  │
│ Receita R$ 8.490           │
│                            │
│ [Fluxos] [Editar] [⋮]      │
└────────────────────────────┘
```

Ações disponíveis:

```
Abrir painel do bot
Editar configurações
Duplicar bot
Aplicar template
Pausar
Ativar
Testar
Visualizar no Telegram
Exportar configuração
Excluir
Rotacionar token
Ver logs
```

Filtros:

```
Todos
Ativos
Inativos
Com erro
Em configuração
Aguardando Telegram
Sem pagamento configurado
```

Também haverá seleção múltipla:

```
☑ Bot 01
☑ Bot 02
☑ Bot 03

[Aplicar fluxo]
[Alterar mensagem]
[Pausar]
[Ativar]
[Exportar]
```

---

## 3\. Criação de um bot

Ao clicar em **Novo Bot**:

## Etapa 1 — Origem

```
Como deseja adicionar o bot?

[ Criar automaticamente ]
[ Conectar bot existente ]
[ Importar configuração JSON ]
[ Criar vários bots por CSV ]
```

## Etapa 2 — Identidade

```
Nome público
Username
Foto
Descrição
Texto “Sobre”
Idioma
Fuso horário
Nome do suporte
Link do suporte
```

## Etapa 3 — Template

```
Escolha o modelo inicial:

Creator Premium
Comunidade VIP
Curso e mentoria
Biblioteca digital
Newsletter
Catálogo de produtos
Bot personalizado
```

## Etapa 4 — Conteúdo

```
Mensagem de boas-vindas
Imagem ou vídeo inicial
Menu principal
Produtos
Planos
Campanhas
Termos
Suporte
```

## Etapa 5 — Publicação

```
Validar configurações
Registrar webhook
Configurar comandos
Executar teste
Publicar
```

Tela final:

```
Bot criado com sucesso

● Telegram conectado
● Webhook ativo
● Fluxo publicado
● Produto configurado
● Pagamento conectado
● Teste aprovado

[Abrir no Telegram]
[Editar bot]
[Duplicar]
```

---

## 4\. Painel interno de cada bot

Ao abrir um bot, teremos abas:

```
Visão geral
Configuração
Fluxos
Produtos
Comunidade
Campanhas
Clientes
Pedidos
Financeiro
Integrações
Logs
```

---

## 5\. Aba “Visão geral”

Informações específicas daquele bot:

```
Receita hoje
Receita no mês
Novos usuários
Conversão
Ticket médio
Pedidos pendentes
Assinaturas ativas
Checkouts abandonados
```

Gráficos:

```
Leads por dia
Vendas por dia
Receita por produto
Conversão por origem
Desempenho das campanhas
```

Atividade recente:

```
14:32 Novo usuário iniciou o bot
14:30 Pedido criado
14:28 Pagamento confirmado
14:28 Produto entregue
14:15 Campanha enviada
```

---

## 6\. Configuração da identidade do bot

Campos:

```
Nome
Username
Avatar
Descrição curta
Descrição completa
Idioma
Fuso horário
Moeda visual
Suporte
Termos
Política de privacidade
```

Configurações visuais:

```
Cor principal do painel
Ícone do bot
Imagem de capa
Estilo dos textos
Uso de emojis
Rodapé das mensagens
```

Configurações técnicas:

```
Token
Webhook
Secret token
Status
Última atualização
Último evento recebido
Versão do template
```

O token deve aparecer mascarado:

```
123456:AA********************X9
```

---

## 7\. Configuração do /start

Tela visual:

```
Mensagem inicial

Tipo de mídia:
( ) Imagem
( ) Vídeo
( ) GIF
( ) Sem mídia

[Selecionar arquivo]

Texto:
┌─────────────────────────────────────┐
│ Bem-vindo, {{first_name}}...        │
└─────────────────────────────────────┘

Botões:
[ Comunidade Premium ]
[ Conteúdos ]
[ Minhas compras ]
[ Suporte ]
```

Pré-visualização lateral:

```
┌──────────────────────┐
│ Telegram Preview     │
│                      │
│ [imagem]             │
│ Bem-vindo...         │
│                      │
│ [Comunidade Premium] │
│ [Conteúdos]          │
│ [Minhas compras]     │
│ [Suporte]            │
└──────────────────────┘
```

Isso permite editar e ver o resultado antes de publicar.

---

## 8\. Construtor de menus

Cada botão será configurado visualmente.

Exemplo:

```
Texto do botão:
Comunidade Premium

Ação:
[ Abrir fluxo ]

Fluxo:
Oferta VIP

Posição:
Linha 1

Largura:
100%
```

Tipos de ação:

```
Abrir fluxo
Abrir produto
Abrir catálogo
Abrir compras
Abrir URL
Abrir suporte
Criar checkout
Executar webhook
Voltar ao menu
```

O operador pode arrastar os botões:

```
┌─────────────────────────────┐
│ Comunidade Premium          │
├─────────────────────────────┤
│ Catálogo                    │
├──────────────┬──────────────┤
│ Compras      │ Suporte      │
└──────────────┴──────────────┘
```

---

## 9\. Construtor de fluxos

A experiência será semelhante a n8n, ManyChat ou Typebot, mas focada em Telegram.

```
[ Trigger /start ]
         ↓
[ Enviar vídeo ]
         ↓
[ Enviar mensagem ]
         ↓
[ Mostrar menu ]
         ↓
[ Usuário escolheu VIP? ]
      ↙                 ↘
    Sim                 Não
     ↓                   ↓
[Oferta]             [Catálogo]
```

Nós do editor:

```
Mensagem
Imagem
Vídeo
Áudio
Documento
Álbum
Botões
Condição
Aguardar
Variável
Tag
Produto
Carrinho
Checkout
Verificar pagamento
Liberar acesso
Remover acesso
Enviar webhook
Iniciar outro fluxo
Finalizar
```

Cada fluxo terá:

```
Rascunho
Versão publicada
Histórico de versões
Teste
Rollback
Duplicar
Exportar
```

---

## 10\. Produtos e conteúdos avulsos

Tela de produtos:

```
Produtos

[+ Novo produto] [Importar] [Reordenar]

Produto A    R$ 50    Ativo
Produto B    R$ 25    Ativo
Produto C    R$ 90    Rascunho
```

Configuração de produto:

```
Nome
Descrição
Preço
Tipo
Capa
Prévia
Arquivos entregáveis
Ordem no catálogo
Status
Limite de acesso
Proteção de conteúdo
```

Tipos:

```
Conteúdo avulso
Pacote
Assinatura
Comunidade
Curso
Arquivo
Link externo
```

O comportamento será igual ao observado:

```
Prévia
Descrição
Preço

[Comprar]
[Ver próximo]
[Minhas compras]
[Menu]
```

---

## 11\. Catálogo

Configurações:

```
Título do catálogo
Mensagem introdutória
Quantidade de produtos por página
Ordem dos produtos
Filtros
Categorias
Produto inicial
Comportamento ao chegar ao final
```

Opções:

```
Voltar ao primeiro item
Mostrar fim do catálogo
Abrir menu
Exibir produtos recomendados
```

---

## 12\. Área “Minhas compras”

Configuração da tela:

```
Mensagem de apresentação
Exibir data da compra
Exibir preço
Permitir reenvio
Limite de reenvios
Exibir produtos expirados
Botão de suporte
```

Resultado no Telegram:

```
Minhas compras

1. Produto A
Comprado em 23/07/2026

[Visualizar novamente]

2. Produto B
Acesso válido até 23/08/2026

[Acessar]
```

---

## 13\. Configuração de comunidade premium

Campos:

```
Nome do plano
Descrição
Preço
Duração
Canal ou grupo
Mensagem antes da compra
Mensagem após a compra
Mensagem de renovação
Mensagem de expiração
Período de tolerância
```

Automação:

```
Pagamento confirmado
→ criar permissão
→ gerar convite
→ aprovar entrada
→ registrar acesso
```

Expiração:

```
Assinatura vencida
→ enviar aviso
→ aguardar tolerância
→ remover do canal
→ oferecer renovação
```

---

## 14\. Order bump e upsell

Configuração visual:

```
Produto principal:
Plano Premium

Oferta complementar:
Pacote Extra

Texto:
Adicione também este conteúdo por...

Preço original:
R$ 50

Preço da oferta:
R$ 30

[Ativar order bump]
```

Resultado:

```
Antes de finalizar, deseja adicionar o pacote?

[Sim, adicionar]
[Não, continuar]
```

Também poderemos configurar:

```
Upsell depois da compra
Downsell
Bundle
Desconto para primeira compra
Oferta limitada por campanha
```

---

## 15\. Checkout e pagamentos

A tela terá:

```
Métodos ativos
Telegram Stars
Stripe
Pix
Mercado Pago
Gateway personalizado
```

Para cada produto, o sistema define o trilho compatível com sua entrega e com as regras da plataforma.

Configurações:

```
Mensagem de checkout
Expiração do pedido
Mensagem de pagamento pendente
Mensagem de pagamento aprovado
Mensagem de falha
Mensagem de reembolso
```

Pedidos:

```
#PED-1032
Usuário
Produto
Valor
Status
Gateway
Data
Entrega
```

Status visuais:

```
Pendente
Pago
Entregue
Expirado
Reembolsado
Falhou
Em disputa
```

---

## 16\. Remarketing

Tela:

```
Campanhas

Recuperação de carrinho     Ativa
Boas-vindas D+1             Ativa
Produto recomendado         Pausada
Renovação de assinatura     Ativa
```

Editor:

```
Público:
Usuários que abriram o produto e não compraram

Aguardar:
2 horas

Condição:
Ainda não comprou?

Mensagem:
Você deixou algo para trás...

Botão:
[Continuar compra]
```

Configurações:

```
Frequência máxima
Horário permitido
Intervalo
Segmento
Bot
Produto
Campanha
UTM
```

---

## 17\. Postagens

Área para publicação em massa:

```
Criar postagem
Selecionar bots
Selecionar público
Adicionar mídia
Agendar
Testar
Publicar
```

Exemplo:

```
Bots selecionados: 18
Usuários elegíveis: 42.430
Envio estimado: 28 minutos

[Enviar teste]
[Agendar]
[Publicar agora]
```

---

## 18\. Clientes

Tabela:

```
Nome
Telegram
Bot
Status
Tags
Compras
Receita
Última interação
```

Perfil do cliente:

```
Dados do Telegram
Origem
Histórico de mensagens
Produtos visualizados
Carrinho
Pedidos
Pagamentos
Compras
Assinaturas
Campanhas recebidas
Logs
```

Ações:

```
Conceder produto
Revogar produto
Adicionar tag
Remover tag
Enviar mensagem
Bloquear
Abrir suporte
```

---

## 19\. Configuração em massa para 30 bots

Teremos um **Template Mestre**.

Exemplo:

```
Template: Creator Premium v1

Inclui:
✓ Fluxo /start
✓ Menu
✓ Catálogo
✓ Minhas compras
✓ Comunidade
✓ Checkout
✓ Order bump
✓ Remarketing
✓ Suporte
```

Ao criar um novo bot:

```
Duplicar template
→ trocar nome
→ trocar avatar
→ trocar textos
→ trocar mídias
→ trocar produtos
→ trocar canal
→ publicar
```

Variáveis:

```
{{BOT_NAME}}
{{CREATOR_NAME}}
{{SUPPORT_USERNAME}}
{{WELCOME_TEXT}}
{{WELCOME_MEDIA}}
{{COMMUNITY_NAME}}
{{PRICE}}
{{CHANNEL_ID}}
```

Para 30 bots, será possível editar em planilha:

```
Bot
Nome
Username
Avatar
Template
Produto
Preço
Canal
Suporte
Status
```

Depois executar:

```
[Aplicar configurações]
[Publicar 30 bots]
```

---

## 20\. Biblioteca de templates

Tela:

```
Templates

Creator Premium v1
Curso v1
Comunidade v1
Newsletter v1
Catálogo v1

[Usar template]
[Duplicar]
[Editar]
[Exportar]
```

Cada template inclui:

```
Fluxos
Menus
Mensagens
Produtos de exemplo
Campanhas
Variáveis
Configurações
```

Não inclui:

```
Tokens
Dados de clientes
Pedidos
Pagamentos
Segredos
```

---

## 21\. Importação e exportação

Cada bot poderá ser exportado como JSON:

```json
{
  "bot": {
    "name": "Bot Exemplo",
    "language": "pt-BR"
  },
  "template": "creator-premium-v1",
  "menus": [],
  "flows": [],
  "products": [],
  "campaigns": [],
  "settings": {}
}
```

Fluxo copia e cola:

```
Exportar Bot A
→ baixar JSON
→ importar como Bot B
→ substituir variáveis
→ publicar
```

Ou diretamente:

```
[Duplicar bot]
```

---

## 22\. Critério de aceite visual e funcional

O produto estará correto quando o operador conseguir:

```
Entrar no painel
→ criar um bot
→ aplicar um template
→ editar textos e mídias
→ configurar produtos
→ publicar
→ testar no Telegram
```

Sem abrir:

```
VS Code
Terminal
n8n
Banco de dados
BotFather manualmente, salvo confirmação necessária
```

E o usuário final receberá:

```
/start
→ apresentação
→ menu
→ catálogo
→ compra
→ pagamento
→ entrega
→ minhas compras
→ campanhas
```

Exatamente como a experiência estrutural dos prints, mas com:

- identidade própria;
- arquitetura escalável;
- gestão em massa;
- versionamento;
- logs;
- segurança;
- isolamento entre bots;
- painel configurável.

## Escopo correto do primeiro produto

A primeira versão deve entregar estas telas:

```
1. Login
2. Dashboard
3. Meus Robôs
4. Criar Bot
5. Configuração do Bot
6. Editor do /start
7. Construtor de Menus
8. Construtor de Fluxos
9. Produtos
10. Pedidos
11. Clientes
12. Campanhas
13. Templates
14. Operações em Massa
15. Logs
```

Esse conjunto já entrega o resultado dos prints e estabelece a fundação para escalar de 3 para 30 bots sem replicar código, infraestrutura ou workflows manualmente.

---

**Você disse**

para iniciarmos um mvp funcional, vir prompt, qual o passo a passo

---

## Estratégia correta do MVP

Não começaria pela plataforma completa de 30 bots. O caminho seguro é:

```
1 bot funcional
→ 3 bots isolados
→ template clonável
→ operações em massa
→ 30 bots
```

Para o primeiro MVP, conectaremos bots existentes por token. A criação automática de managed bots fica para uma segunda fase, porque o fluxo oficial envolve MTProto, permissões específicas de manager bot e confirmação do proprietário. [^5]

Para produtos digitais entregues dentro do Telegram, o pagamento do MVP deve usar Telegram Stars com moeda `XTR`. [^3]

Todos os bots usarão webhooks HTTPS com um `secret_token` individual. [^2]

---

## Escopo fechado do MVP

## Incluído

```
Dashboard escuro semelhante aos prints
Meus Robôs
Conectar bot por token
Ativar, pausar, testar e excluir bot
Configuração de identidade
Editor do /start
Editor do menu principal
Pré-visualização estilo Telegram
Produtos digitais
Catálogo com “Ver próximo”
Carrinho simples
Order bump
Pagamento com Telegram Stars
Minhas compras
Entrega automática
Clientes
Pedidos
Campanha simples
Template clonável
Duplicação de bot
Importação de configuração JSON
Logs e auditoria
```

## Fora do primeiro MVP

```
Management Bot automático
Editor visual em grafo
Mini App
Afiliados
Ranking
Premiações
Roleta
Bio Link
Múltiplos gateways
Checkout externo
30 bots em produção imediata
```

O editor visual em grafo é bonito, mas no MVP seria uma ponte holográfica construída antes do motor. Primeiro fazemos o runtime funcionar; depois desenhamos os fios.

---

## Stack definida

```
Monorepo: pnpm + Turborepo
Dashboard: Next.js + TypeScript
UI: Tailwind + shadcn/ui
API: NestJS com Fastify
Telegram: grammY
Banco: PostgreSQL
ORM: Prisma
Cache e filas: Redis + BullMQ
Arquivos local: MinIO
Arquivos produção: Cloudflare R2
Autenticação: Supabase Auth
Testes: Vitest + Playwright
Infra: Docker Compose + Traefik
Observabilidade: logs estruturados + Sentry
```

Estrutura:

```
bot-factory/
├── apps/
│   ├── web/
│   ├── api/
│   ├── bot-worker/
│   ├── campaign-worker/
│   └── delivery-worker/
├── packages/
│   ├── database/
│   ├── telegram/
│   ├── flow-engine/
│   ├── queue/
│   ├── security/
│   └── shared/
├── infrastructure/
├── docs/
└── tests/
```

---

## Regra para usar os prompts

Execute **um prompt por vez** no Codex.

Só avance quando o agente entregar:

```
Implementação concluída
Arquivos alterados
Migrations executadas
Testes passando
Build passando
Como testar manualmente
Pendências reais
```

Não envie todos de uma vez. Mega-prompt costuma produzir mega-entulho.

---

## Cabeçalho permanente

Cole este bloco no início de todos os prompts seguintes:

```
Você atuará como Principal Product Engineer e Arquiteto do projeto Bot Factory.

REGRAS FIXAS

- Trabalhe diretamente no repositório atual.
- Antes de alterar qualquer arquivo, inspecione a estrutura existente.
- Não reescreva partes funcionais sem necessidade.
- Não crie mocks onde já for possível uma integração real.
- Não implemente funcionalidades fora do escopo desta etapa.
- Preserve arquitetura multi-tenant desde o início.
- Toda entidade operacional deve possuir tenantId e, quando aplicável, botId.
- Nunca exponha tokens ou segredos em logs, respostas HTTP ou frontend.
- Utilize TypeScript estrito.
- Utilize validação de entrada.
- Todas as migrations devem ser versionadas.
- Operações críticas devem ser idempotentes.
- Não avance silenciosamente diante de erros.
- Crie testes para o comportamento implementado.
- Ao final execute lint, typecheck, testes e build.
- Documente como executar e validar manualmente.

FORMATO DE ENTREGA

1. Resumo da implementação
2. Arquivos criados e alterados
3. Decisões arquiteturais
4. Comandos executados
5. Resultado dos testes
6. Passo a passo para validação manual
7. Riscos ou pendências
```

---

## Prompt 0 — Auditoria e plano executável

```
Faça uma auditoria completa do repositório antes de implementar qualquer funcionalidade.

OBJETIVO

Determinar se devemos evoluir a estrutura atual ou iniciar um novo monorepo para o Bot Factory.

CONTEXTO DO PRODUTO

O Bot Factory será uma plataforma multi-tenant para criação, configuração, duplicação e operação de bots do Telegram.

O MVP deverá conter:

- dashboard administrativo;
- gestão de bots;
- conexão por token;
- configuração de identidade;
- editor de /start;
- menus;
- produtos;
- catálogo;
- pedidos;
- Telegram Stars;
- entrega digital;
- clientes;
- campanhas básicas;
- templates;
- clonagem de bots;
- logs.

STACK ALVO

- pnpm;
- Turborepo;
- Next.js;
- NestJS com Fastify;
- grammY;
- PostgreSQL;
- Prisma;
- Redis;
- BullMQ;
- MinIO;
- Docker Compose.

NESTA ETAPA

- não implemente o produto;
- não faça grandes refactors;
- não instale dependências ainda;
- não delete arquivos;
- não altere infraestrutura ativa.

ENTREGUE

1. inventário do repositório;
2. tecnologias existentes;
3. serviços e containers existentes;
4. riscos de conflito;
5. componentes que podem ser reutilizados;
6. componentes que devem permanecer isolados;
7. arquitetura proposta;
8. estrutura de diretórios;
9. modelo de ambientes;
10. roadmap técnico dividido nas próximas etapas;
11. decisão clara entre novo monorepo ou evolução da estrutura;
12. arquivo docs/MVP_PLAN.md contendo o plano aprovado.

CRITÉRIO DE ACEITE

O plano deve permitir iniciar a fundação sem decisões arquiteturais pendentes.
```

---

## Prompt 1 — Fundação do monorepo

```
Implemente a fundação técnica do Bot Factory seguindo o plano aprovado em docs/MVP_PLAN.md.

OBJETIVO

Criar um monorepo funcional e executável localmente, ainda sem funcionalidades de negócio.

CRIAR

apps/web
apps/api
apps/bot-worker
apps/campaign-worker
apps/delivery-worker

packages/database
packages/shared
packages/security
packages/queue
packages/telegram
packages/flow-engine

CONFIGURAR

- pnpm workspaces;
- Turborepo;
- TypeScript estrito;
- ESLint;
- Prettier;
- variáveis de ambiente validadas;
- Docker Compose;
- PostgreSQL;
- Redis;
- MinIO;
- health checks;
- logs estruturados;
- shutdown gracioso.

ROTAS

API:
GET /health
GET /ready

WEB:
página inicial temporária;
página /login temporária;
página /dashboard temporária.

DOCKER COMPOSE

Deve iniciar:

- postgres;
- redis;
- minio;
- api;
- web;
- bot-worker;
- campaign-worker;
- delivery-worker.

SEGURANÇA

- criar .env.example;
- nunca versionar .env;
- gerar segredos apenas como placeholders;
- não colocar tokens reais.

TESTES

- health check da API;
- conexão com PostgreSQL;
- conexão com Redis;
- build de todos os workspaces.

CRITÉRIO DE ACEITE

O comando abaixo deve subir todo o ambiente:

docker compose up -d

E os comandos abaixo devem passar:

pnpm lint
pnpm typecheck
pnpm test
pnpm build
```

---

## Prompt 2 — Banco multi-tenant e autenticação

```
Implemente o núcleo multi-tenant e a autenticação administrativa.

OBJETIVO

Permitir que um usuário autenticado pertença a um workspace e nunca consiga acessar dados de outro workspace.

ENTIDADES

User
Tenant
TenantMember
Role
Bot
BotCredential
BotSetting
AuditLog

PAPÉIS

OWNER
ADMIN
EDITOR
SUPPORT
VIEWER

REQUISITOS

- utilizar PostgreSQL e Prisma;
- utilizar UUIDs;
- adicionar createdAt e updatedAt;
- usar soft delete quando aplicável;
- criptografar BotCredential;
- nunca retornar o token completo pela API;
- criar tenant padrão no primeiro login;
- implementar middleware de contexto de tenant;
- implementar guards de autenticação e autorização;
- registrar ações administrativas em AuditLog.

ROTAS

GET /me
GET /tenants
POST /tenants
GET /tenants/:tenantId
GET /tenants/:tenantId/members
POST /tenants/:tenantId/members

AUTENTICAÇÃO

Integrar Supabase Auth no frontend e validar JWT no backend.

DASHBOARD

Criar layout autenticado com:

- sidebar;
- header;
- workspace ativo;
- usuário autenticado;
- logout;
- rota protegida /dashboard.

TESTES OBRIGATÓRIOS

- usuário não autenticado recebe 401;
- usuário de Tenant A não acessa Tenant B;
- VIEWER não realiza escrita;
- OWNER realiza todas as operações;
- token de bot nunca aparece sem máscara;
- AuditLog registra alterações.

CRITÉRIO DE ACEITE

Dois tenants de teste devem possuir isolamento comprovado por testes automatizados.
```

---

## Prompt 3 — Conexão e gerenciamento de bots

```
Implemente o módulo Meus Robôs e a conexão de bots existentes por token.

OBJETIVO

Permitir conectar um bot do Telegram, validar o token, armazená-lo com criptografia, configurar webhook e exibir o bot no dashboard.

FLUXO

1. usuário clica em Novo Bot;
2. escolhe Conectar bot existente;
3. informa o token;
4. backend consulta getMe;
5. valida se o token corresponde a um bot;
6. verifica se o bot já está cadastrado;
7. criptografa o token;
8. gera webhookSecret individual;
9. registra webhook HTTPS;
10. configura comandos padrão;
11. salva o status;
12. executa smoke test.

STATUS

DRAFT
CONNECTING
ACTIVE
PAUSED
ERROR
DISCONNECTED

ROTAS

GET /bots
POST /bots/connect
GET /bots/:botId
PATCH /bots/:botId
POST /bots/:botId/test
POST /bots/:botId/pause
POST /bots/:botId/activate
DELETE /bots/:botId
GET /bots/:botId/logs

WEBHOOK

POST /telegram/webhooks/:botPublicId

Validar:

- botPublicId;
- secret header;
- updateId duplicado;
- bot ativo;
- tenant correto.

INTERFACE

Criar tela Meus Robôs semelhante ao layout de referência:

- cards;
- avatar;
- nome;
- username;
- status;
- leads;
- vendas;
- receita;
- botões editar, testar, pausar e abrir no Telegram;
- filtro por status;
- card Novo Bot.

Não inventar métricas: exibir zero enquanto não houver eventos.

TESTES

- token inválido;
- token duplicado;
- webhook inválido;
- segredo incorreto;
- update duplicado;
- pausa do bot;
- isolamento entre tenants.

CRITÉRIO DE ACEITE

Um bot real deve ser conectado e responder ao smoke test sem expor seu token.
```

---

## Prompt 4 — Runtime /start e menu principal

```
Implemente o runtime funcional do Telegram para /start e menus inline.

OBJETIVO

O bot conectado deve responder no Telegram com mídia, texto e botões definidos pelo painel.

ENTIDADES

BotFlow
BotFlowVersion
FlowNode
Menu
MenuButton
TelegramUser
BotUser
UserSession
TelegramUpdate
BotEvent

EVENTOS

bot.started
menu.opened
button.clicked
message.sent
message.failed

NÓS INICIAIS

SEND_TEXT
SEND_PHOTO
SEND_VIDEO
SHOW_MENU
OPEN_URL
START_FLOW
END

CALLBACKS

Usar identificadores curtos e opacos.

Não colocar:

- preço;
- texto completo;
- tenantId;
- segredos.

EDITOR

Criar página:

/dashboard/bots/:botId/start

Campos:

- mídia inicial;
- texto;
- botões;
- ação de cada botão;
- ordem;
- largura;
- rascunho;
- publicar;
- restaurar versão.

PREVIEW

Criar preview visual semelhante a uma conversa do Telegram.

RUNTIME

- carregar versão publicada;
- usar cache Redis;
- invalidar cache ao publicar;
- registrar usuário;
- registrar origem do deep link;
- registrar eventos;
- responder callbackQuery;
- impedir execução de versões em rascunho.

TESTES

- /start novo;
- /start repetido;
- deep link;
- menu válido;
- callback inválido;
- fluxo não publicado;
- cache invalidado;
- isolamento entre bots.

CRITÉRIO DE ACEITE

O operador edita o /start no painel, publica e visualiza a mudança real no Telegram sem reiniciar serviços.
```

---

## Prompt 5 — Identidade e configuração visual

```
Implemente a tela completa de configuração do bot.

OBJETIVO

Permitir configurar identidade, mensagens, comandos, suporte e comportamento geral diretamente pelo dashboard.

ABAS

Geral
Identidade
Comandos
Suporte
Segurança
Telegram
Versões

CAMPOS

- nome;
- username somente leitura;
- avatar;
- descrição;
- descrição curta;
- idioma;
- fuso horário;
- suporte;
- termos;
- privacidade;
- mensagem de erro;
- mensagem de manutenção;
- rodapé opcional;
- configuração de emojis;
- status.

AÇÕES TELEGRAM

Ao publicar identidade:

- setMyName;
- setMyDescription;
- setMyShortDescription;
- setMyCommands;
- setMyProfilePhoto quando suportado.

REQUISITOS

- diferenciar rascunho de configuração publicada;
- validar limites dos campos;
- mostrar erros retornados pelo Telegram;
- permitir rollback;
- registrar auditoria;
- apresentar preview.

CRITÉRIO DE ACEITE

Alterações publicadas no dashboard devem aparecer no perfil real do bot e possuir histórico de versões.
```

---

## Prompt 6 — Templates e duplicação

```
Implemente o Template Engine do MVP.

OBJETIVO

Permitir transformar um bot configurado em template e aplicar o mesmo modelo em outro bot.

ENTIDADES

BotTemplate
BotTemplateVersion
TemplateVariable
TemplateDeployment
TemplateAsset

O TEMPLATE DEVE INCLUIR

- configuração do /start;
- menus;
- fluxos;
- textos;
- produtos de exemplo;
- configurações não sensíveis;
- campanhas em rascunho.

NÃO DEVE INCLUIR

- bot token;
- webhook secret;
- usuários;
- clientes;
- pedidos;
- pagamentos;
- credenciais;
- logs.

VARIÁVEIS

{{BOT_NAME}}
{{BRAND_NAME}}
{{SUPPORT_USERNAME}}
{{WELCOME_TEXT}}
{{WELCOME_MEDIA}}
{{PRODUCT_NAME}}
{{CHANNEL_ID}}

AÇÕES

- criar template a partir de um bot;
- editar template;
- versionar;
- duplicar;
- exportar JSON;
- importar JSON;
- aplicar a um bot;
- validar variáveis ausentes;
- visualizar diferenças antes de aplicar.

INTERFACE

Criar páginas:

/dashboard/templates
/dashboard/templates/new
/dashboard/templates/:templateId
/dashboard/bots/:botId/apply-template

TESTES

- template não exporta segredos;
- importação inválida falha;
- variáveis obrigatórias são verificadas;
- aplicação não altera outro tenant;
- rollback funciona.

CRITÉRIO DE ACEITE

Deve ser possível configurar Bot A, gerar um template e recriar a mesma experiência no Bot B sem copiar código.
```

---

## Prompt 7 — Produtos, catálogo e minhas compras

```
Implemente o Commerce Engine inicial.

OBJETIVO

Permitir cadastrar produtos digitais, navegar pelo catálogo no Telegram e consultar produtos adquiridos.

ENTIDADES

Product
ProductAsset
ProductCategory
Catalog
CatalogItem
Cart
CartItem
Order
OrderItem
Entitlement
Delivery

TIPOS DE PRODUTO

DIGITAL_ITEM
BUNDLE
MEMBERSHIP
COMMUNITY_ACCESS

PAINEL

Criar:

- lista de produtos;
- criação e edição;
- upload de capa;
- upload de prévia;
- arquivos entregáveis;
- preço em Stars;
- status;
- ordem do catálogo;
- proteção de conteúdo;
- preview.

TELEGRAM

Implementar:

- abrir catálogo;
- ver produto;
- comprar;
- ver próximo;
- ver anterior;
- minhas compras;
- abrir produto adquirido;
- voltar ao menu.

REGRAS

- preço calculado somente no servidor;
- produto inativo não aparece;
- usuário só acessa entitlement ativo;
- entrega idempotente;
- assets devem usar telegram_file_id quando disponível;
- salvar arquivos também no object storage.

TESTES

- navegação;
- fim do catálogo;
- produto inativo;
- callback manipulado;
- entitlement inválido;
- entrega duplicada;
- isolamento entre bots.

CRITÉRIO DE ACEITE

Um usuário consegue navegar em produtos reais no bot, enquanto outro bot mantém catálogo completamente diferente.
```

---

## Prompt 8 — Carrinho, order bump e Telegram Stars

```
Implemente o pagamento funcional com Telegram Stars.

OBJETIVO

Permitir comprar um produto digital no Telegram, confirmar o pagamento, criar entitlement e entregar o conteúdo automaticamente.

FLUXO

1. adicionar produto ao carrinho;
2. oferecer order bump opcional;
3. aceitar ou recusar;
4. criar pedido;
5. enviar invoice em XTR;
6. processar pre_checkout_query;
7. validar pedido, usuário, moeda e valor;
8. responder à consulta;
9. processar successful_payment;
10. salvar telegram_payment_charge_id;
11. marcar pedido como pago;
12. criar entitlement;
13. enfileirar entrega;
14. confirmar ao usuário.

STATUS DO PEDIDO

DRAFT
AWAITING_PAYMENT
PAID
FULFILLING
DELIVERED
EXPIRED
REFUNDED
FAILED

STATUS DO PAGAMENTO

PENDING
PAID
REFUNDED
DISPUTED
FAILED

REQUISITOS

- idempotência por telegram_payment_charge_id;
- valor recalculado no backend;
- invoice_payload assinado ou opaco;
- reconciliação de pedido pago sem entrega;
- retry de entrega;
- suporte a refundStarPayment;
- auditoria;
- nunca confiar em botão “paguei”.

ORDER BUMP

- produto principal;
- produto adicional;
- ativação;
- valor;
- primeira compra opcional;
- aceitar;
- recusar;
- métricas.

TESTES

- pagamento válido;
- pagamento duplicado;
- valor divergente;
- pedido expirado;
- usuário incorreto;
- entrega falha;
- retry;
- reembolso.

CRITÉRIO DE ACEITE

Um pagamento real de teste deve criar somente um pedido pago, um entitlement e uma entrega.
```

---

## Prompt 9 — Clientes, pedidos e logs

```
Implemente as telas operacionais de clientes, pedidos e eventos.

OBJETIVO

Dar ao operador visibilidade completa sobre o comportamento e as transações de cada bot.

CLIENTES

Tabela com:

- nome;
- username;
- bot;
- origem;
- status;
- tags;
- compras;
- valor total;
- primeira interação;
- última interação.

PERFIL DO CLIENTE

- dados do Telegram;
- eventos;
- produtos visualizados;
- carrinho;
- pedidos;
- pagamentos;
- entitlements;
- entregas;
- campanhas;
- suporte.

PEDIDOS

Tabela com:

- referência;
- usuário;
- bot;
- produtos;
- total;
- status;
- pagamento;
- entrega;
- datas.

LOGS

- filtro por bot;
- evento;
- usuário;
- severidade;
- período;
- correlationId.

AÇÕES ADMINISTRATIVAS

- reenviar produto;
- conceder entitlement;
- revogar entitlement;
- adicionar tag;
- bloquear;
- desbloquear.

Toda ação manual deve exigir permissão e gerar AuditLog.

CRITÉRIO DE ACEITE

O administrador deve conseguir descobrir por que um usuário pagou e não recebeu sem consultar diretamente o banco.
```

---

## Prompt 10 — Campanhas básicas

```
Implemente o Campaign Engine básico.

OBJETIVO

Permitir enviar mensagens para segmentos específicos sem duplicidade e com controle de frequência.

ENTIDADES

Segment
Campaign
CampaignMessage
CampaignAudience
CampaignDelivery
UserTag
Suppression

SEGMENTOS INICIAIS

- iniciou e não comprou;
- visualizou produto e não comprou;
- carrinho abandonado;
- comprador;
- usuário inativo;
- usuários com uma tag.

PAINEL

- criar campanha;
- escolher bot;
- escolher segmento;
- escrever mensagem;
- anexar mídia;
- adicionar botão;
- enviar teste;
- agendar;
- pausar;
- cancelar;
- ver resultados.

FILA

Usar BullMQ com fila individualizada logicamente por bot.

CONTROLES

- rate limiting;
- retry exponencial;
- quiet hours;
- opt-out;
- frequência máxima;
- não enviar para usuários bloqueados;
- revalidar o segmento antes do envio;
- registrar sucesso e falha.

COMANDOS

/stop deve suprimir campanhas comerciais.
/start não deve remover supressão automaticamente.

CRITÉRIO DE ACEITE

Uma campanha deve ser testada com usuários controlados e nunca enviada para compradores quando o segmento for abandono.
```

---

## Prompt 11 — Operações em massa

```
Implemente operações em massa após validar três bots individualmente.

OBJETIVO

Permitir configurar e atualizar vários bots sem repetir trabalho manual.

FUNCIONALIDADES

- seleção múltipla;
- aplicar template;
- atualizar mensagem;
- adicionar produto;
- pausar;
- ativar;
- testar;
- exportar;
- executar diagnóstico;
- publicar versão.

IMPORTAÇÃO CSV

Colunas:

name
token
template
brandName
supportUsername
language
timezone

REQUISITOS

- validar arquivo antes de executar;
- exibir preview;
- mostrar linha com erro;
- processar em fila;
- acompanhar progresso;
- permitir retry;
- não armazenar CSV com tokens permanentemente;
- criptografar tokens imediatamente;
- excluir conteúdo sensível após o processamento.

STATUS DO JOB

QUEUED
VALIDATING
RUNNING
PARTIAL_SUCCESS
COMPLETED
FAILED
CANCELLED

INTERFACE

Criar página:

/dashboard/mass-operations

Exibir:

- bot;
- etapa;
- progresso;
- resultado;
- erro;
- retry.

CRITÉRIO DE ACEITE

Aplicar um template em três bots deve gerar três configurações isoladas e funcionais sem interferência cruzada.
```

---

## Prompt 12 — Dashboard final semelhante aos prints

```
Refine o dashboard administrativo para atingir o resultado visual esperado.

OBJETIVO

Criar uma interface premium, escura, funcional e consistente com a referência visual, sem copiar marca, textos ou ativos proprietários.

TELAS

- login;
- dashboard;
- meus robôs;
- criar bot;
- detalhe do bot;
- configuração;
- editor do /start;
- menus;
- produtos;
- clientes;
- pedidos;
- campanhas;
- templates;
- operações em massa;
- logs.

DIREÇÃO VISUAL

- fundo preto profundo;
- sidebar fixa;
- bordas sutis;
- tipografia clara;
- cards de bots;
- status online e offline;
- cards de métricas;
- hierarquia visual limpa;
- densidade adequada para desktop;
- responsividade;
- estados vazios;
- skeletons;
- erros;
- loading;
- tooltips.

DASHBOARD PRINCIPAL

Exibir métricas reais:

- faturamento;
- bots totais;
- bots ativos;
- bots inativos;
- leads;
- vendas;
- conversão.

Não usar números fictícios.

MEUS ROBÔS

Cada card deve exibir:

- avatar;
- nome;
- username;
- status;
- leads;
- vendas;
- receita;
- template;
- ações rápidas.

QUALIDADE

- acessibilidade;
- navegação por teclado;
- contraste;
- componentes reutilizáveis;
- sem estilos duplicados;
- sem dados hardcoded;
- Playwright para fluxos principais.

CRITÉRIO DE ACEITE

O painel deve parecer um produto SaaS operacional, e não um conjunto de páginas administrativas genéricas.
```

---

## Prompt 13 — Hardening, deploy e validação

```
Prepare o MVP para validação controlada em produção.

OBJETIVO

Executar testes de ponta a ponta com três bots reais e publicar a infraestrutura.

VALIDAR

- login;
- isolamento multi-tenant;
- conexão de bot;
- webhook;
- /start;
- menus;
- catálogo;
- carrinho;
- order bump;
- Stars;
- entitlement;
- entrega;
- minhas compras;
- clientes;
- pedidos;
- campanhas;
- templates;
- duplicação;
- logs.

INFRAESTRUTURA

- Docker production;
- Traefik;
- HTTPS;
- migrations;
- backups;
- health checks;
- restart policies;
- limites de recursos;
- rotação de logs;
- Sentry;
- alertas;
- política de retenção.

RECONCILIAÇÃO

Criar jobs para detectar:

- pedido pago sem entitlement;
- entitlement sem entrega;
- entrega falha;
- bot sem webhook;
- webhook com erro;
- campanha travada;
- bot inativo inesperadamente.

DOCUMENTAÇÃO

Criar:

docs/DEPLOYMENT.md
docs/OPERATIONS.md
docs/SECURITY.md
docs/TELEGRAM_SETUP.md
docs/TEST_PLAN.md
docs/ROLLBACK.md

CRITÉRIOS FINAIS

- três bots reais online;
- um template compartilhado;
- dados isolados;
- uma compra concluída;
- uma entrega concluída;
- uma campanha controlada;
- nenhum segredo exposto;
- lint, typecheck, testes e build passando;
- processo documentado para adicionar o quarto bot.
```

---

## Ordem operacional

```
Prompt 0  — Auditoria
Prompt 1  — Fundação
Prompt 2  — Multi-tenant
Prompt 3  — Conectar bots
Prompt 4  — /start e menus
Prompt 5  — Identidade
Prompt 6  — Templates
Prompt 7  — Produtos
Prompt 8  — Pagamentos
Prompt 9  — Operação
Prompt 10 — Campanhas
Prompt 11 — Massa
Prompt 12 — UI final
Prompt 13 — Produção
```

## Gates de escala

```
Gate 1:
1 bot responde /start

Gate 2:
1 bot vende e entrega

Gate 3:
3 bots possuem dados isolados

Gate 4:
Template replica configuração

Gate 5:
Operação em massa funciona

Gate 6:
Escalar para 10 bots

Gate 7:
Escalar para 30 bots
```

O primeiro comando prático é executar o **Prompt 0** no diretório onde o novo projeto será construído. Não deixe o agente iniciar código antes de devolver e fechar o `MVP_PLAN.md`.

[^1]: [core.telegram.org](https://core.telegram.org/bots/features)

[^2]: [core.telegram.org](https://core.telegram.org/bots/api)

[^3]: [core.telegram.org](https://core.telegram.org/bots/payments-stars)

[^4]: [core.telegram.org](https://core.telegram.org/bots/webapps)

[^5]: [core.telegram.org](https://core.telegram.org/api/bots/managed-bots)