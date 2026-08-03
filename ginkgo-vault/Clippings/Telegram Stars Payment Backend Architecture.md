---
title: "Telegram Stars Payment Backend Architecture"
source: "https://grok.com/c/f6bcd335-2523-4a6a-9ed5-011f70239fd8?rid=68a7c04f-eab6-450b-bc8c-f7172d42d481"
author:
published:
created: 2026-07-23
description: "Grok is an AI assistant built by SpaceXAI. Chat, create images, write code, and get real-time answers from the web and X."
tags:
  - "clippings"
---
\## [https://sharkbot.com.br/](https://sharkbot.com.br/) voce consegue me dizer exatamente como funciona esta plataforma no back-end, pegando a doc oficial do telegram. \*\*Você disse\*\*

\## \*\*Você disse\*\* Sim. Elabore & Valide.

\## Veredito

\## A arquitetura é \*\*replicável como plataforma white-label de conteúdo premium\*\*, com catálogo, carrinho, order bump, pagamento, entrega digital, comunidade privada e campanhas automáticas. A validação encontrou um ponto crítico: \*\*não devemos copiar o fluxo de Pix exatamente como aparece nos prints\*\*. Atualmente, o Telegram exige que bens e serviços digitais vendidos dentro de bots ou Mini Apps sejam pagos exclusivamente com \*\*Telegram Stars (XTR)\*\*, mesmo que o operador tenha checkout externo ou outros gateways. Portanto, a réplica correta deve preservar a experiência comercial, mas substituir o trilho de pagamento interno por Stars. [^1] A análise abaixo cobre o motor técnico e comercial para conteúdo premium lícito e não explícito.

\## 1. O que os prints validam

| Componente | Evidência observada | Confiança |
| --- | --- | --- |
| Onboarding por /start | Mídia, texto e menu inicial | Alta |
| Menu principal | VIP, catálogo avulso e suporte | Alta |
| Catálogo dinâmico | Quantidade de itens, “Ver próximo” e compra | Alta |
| Área “Minhas compras” | Botão presente em vários fluxos | Alta |
| Carrinho | Combinação VIP + produto avulso | Alta |
| Order bump | Oferta adicional antes do pagamento | Alta |
| Checkout individual | QR Code, valor e Pix copia e cola | Alta |
| Confirmação manual | Botão “Paguei, libera meu acesso” | Alta |
| Pagamento por cartão | Link alternativo apresentado | Alta |
| Campanhas automáticas | Mensagens enviadas em horários diferentes | Alta |
| Arquitetura white-label | Mesma estrutura em bots com marcas diferentes | Alta |
| Liberação automática de canal | Provável, mas não aparece concluída nos prints | Média |
| Tecnologia interna usada | Não identificável apenas pela interface | Baixa |
| Gateway específico | Não validado | Baixa |

\## Conclusão da engenharia reversa

O produto não parece ser um workflow isolado. Ele se comporta como um \*\*SaaS multi-tenant para creators\*\*, onde cada cliente possui:

```markdown
Bot próprio
Marca própria
Produtos próprios
Preços próprios
Canal ou comunidade própria
Campanhas próprias
Gateway/configuração financeira própria
```

\## O motor central permanece igual.

\## 2. Arquitetura recomendada

```markdown
PAINEL ADMINISTRATIVO
                                  │
                                  ▼
┌──────────────────────────────────────────────────────────┐
│ BACKEND MULTI-TENANT │
│ │
│ Tenant A Tenant B Tenant C │
│ Bot A Bot B Bot C │
│ Produtos A Produtos B Produtos C │
└──────────────────────────────────────────────────────────┘
          │ │ │
          ▼ ▼ ▼
 Telegram Bot API PostgreSQL Redis
          │ │ │
          └────────────── Event Bus ──────────┘
                                  │
                 ┌────────────────┼────────────────┐
                 ▼ ▼ ▼
             Pagamentos Entregas Campanhas
              Stars e acessos e remarketing
```

\## Stack principal

```markdown
Frontend administrativo:
Next.js + React
Backend:
NestJS + TypeScript
Bot:
grammY ou Telegraf
Banco:
PostgreSQL / Supabase
Cache e sessões:
Redis
Filas:
BullMQ
Automações:
n8n
Armazenamento:
Cloudflare R2, S3 ou MinIO
Infraestrutura:
Docker Compose
Traefik
VPS Hostinger
```

\### Por que não usar somente n8n

O n8n é adequado para:

- campanhas;
- notificações;
- recuperação de usuários;
- relatórios;
- CRM;
- suporte;
- sincronizações;
- alertas administrativos. O núcleo transacional deve ficar no backend:
- callbacks;
- catálogo;
- carrinho;
- pagamentos;
- idempotência;
- permissões;
- entrega;
- controle de assinatura. Transformar tudo em n8n funcionaria inicialmente, mas o projeto acabaria parecendo uma estação espacial montada com extensões elétricas.

---

\## 3. Separação por módulos

\## 3.1 Bot Gateway

Responsável por receber os eventos do Telegram:

```markdown
/start
/callback_query
/pre_checkout_query
/successful_payment
/chat_join_request
/chat_member
/message
```

Rota:

```markdown
POST /webhooks/telegram/:tenantKey
```

O webhook deve usar secret\_token; o Telegram envia esse valor no cabeçalho X-Telegram-Bot-Api-Secret-Token, permitindo validar que a chamada veio da configuração esperada. [^2] Fluxo:

```markdown
Telegram
   ↓
Webhook
   ↓
Validação do secret token
   ↓
Identificação do tenant
   ↓
Deduplicação do update
   ↓
Roteamento para o handler
```

\## 3.2 Motor de navegação

Responsável por:

- menu inicial;
- catálogo;
- paginação;
- carrinho;
- pedidos;
- compras anteriores;
- suporte;
- estados da conversa. Callbacks recomendados:

```markdown
menu:home
menu:catalog
menu:membership
menu:purchases
menu:support
catalog:view:{productId}
catalog:next:{productId}
catalog:previous:{productId}
cart:add:{productId}
cart:remove:{productId}
cart:view
cart:checkout
payment:status:{orderId}
purchase:deliver:{orderId}
```

Não coloque preço ou nome do produto dentro do callback. O callback deve carregar apenas um identificador. O backend consulta o valor oficial no banco. Errado:

```markdown
buy:produto_01:50.00
```

Correto:

```markdown
cart:add:prd_8F3K2
```

---

\## 4. Máquina de estados

\## Estado do usuário

```markdown
NEW
  ↓
STARTED
  ↓
BROWSING
  ↓
CART_ACTIVE
  ↓
CHECKOUT_CREATED
  ↓
PAYMENT_PENDING
  ↓
CUSTOMER
```

Estados paralelos:

```markdown
MEMBERSHIP_ACTIVE
MEMBERSHIP_PAST_DUE
MEMBERSHIP_EXPIRED
BLOCKED
SUPPORT_REQUIRED
```

\## Estado do pedido

```markdown
DRAFT
  ↓
AWAITING_PAYMENT
  ↓
PAID
  ↓
FULFILLING
  ↓
DELIVERED
```

Caminhos alternativos:

```markdown
AWAITING_PAYMENT → EXPIRED
PAID → REFUNDED
PAID → DISPUTED
FULFILLING → DELIVERY_FAILED
```

\## Estado da assinatura

```markdown
PENDING
ACTIVE
GRACE_PERIOD
PAST_DUE
CANCELLED
EXPIRED
REVOKED
```

A plataforma deve manter separados:

- pagamento;
- pedido;
- assinatura;
- direito de acesso. Isso evita o clássico bug: “o pagamento foi aprovado, mas o usuário não recebeu” ou “foi reembolsado e permaneceu no canal”.

---

\## 5. Modelo de dados

\## Entidades centrais

```markdown
tenants
telegram_bots
users
user_sessions
products
product_assets
plans
carts
cart_items
orders
order_items
payments
entitlements
subscriptions
channels
invite_links
campaigns
campaign_messages
campaign_deliveries
support_tickets
audit_logs
webhook_events
```

\## tenants

```markdown
id
name
slug
status
timezone
support_username
terms_url
privacy_url
created_at
updated_at
```

\## telegram\_bots

```markdown
id
tenant_id
telegram_bot_id
username
encrypted_token
webhook_secret
default_language
status
created_at
```

\## users

```markdown
id
tenant_id
telegram_user_id BIGINT
telegram_username
first_name
last_name
language_code
status
started_at
last_interaction_at
referral_code
referral_source
```

IDs de usuários do Telegram devem ser armazenados como BIGINT; a documentação alerta que eles podem ter até 52 bits significativos. [^3]

\## products

```markdown
id
tenant_id
type
name
description
price_stars
status
position
preview_asset_id
delivery_strategy
created_at
updated_at
```

Tipos:

```markdown
DIGITAL_ITEM
BUNDLE
MEMBERSHIP
COURSE
DOWNLOAD
COMMUNITY_ACCESS
```

\## product\_assets

```markdown
id
tenant_id
product_id
asset_type
telegram_file_id
storage_key
display_order
protect_content
created_at
```

O telegram\_file\_id permite reutilizar arquivos já enviados sem realizar upload repetido.

\## carts

```markdown
id
tenant_id
user_id
status
currency
subtotal
discount
total
expires_at
created_at
updated_at
```

\## orders

```markdown
id
tenant_id
user_id
cart_id
public_reference
status
currency
subtotal
discount
total
paid_at
delivered_at
created_at
```

\## payments

```markdown
id
tenant_id
order_id
provider
provider_payment_id
telegram_payment_charge_id
status
amount
currency
raw_payload
paid_at
refunded_at
created_at
```

\## entitlements

Representa o direito de consumir algo:

```markdown
id
tenant_id
user_id
product_id
order_id
status
granted_at
expires_at
revoked_at
delivery_count
```

\## subscriptions

```markdown
id
tenant_id
user_id
plan_id
status
started_at
current_period_start
current_period_end
cancel_at_period_end
cancelled_at
created_at
```

\## webhook\_events

```markdown
id
tenant_id
source
external_event_id
event_type
payload
processing_status
received_at
processed_at
```

Restrição essencial:

```markdown
UNIQUE(source, external_event_id)
```

\## Isso fornece idempotência.

\## 6. Fluxo inicial

```markdown
Usuário abre deep link
        ↓
/start campanha_x
        ↓
Backend registra:
- usuário
- origem
- campanha
- horário
        ↓
Bot envia mídia de apresentação
        ↓
Bot apresenta:
- comunidade premium
- catálogo
- compras
- suporte
```

Payload do deep link:

```markdown
https://t.me/NomeDoBot?start=ig_reel_023
```

Registro:

```markdown
{
  "source": "instagram",
  "campaign": "reel_023",
  "creator": "tenant_a"
}
```

Isso permite calcular:

```markdown
Cliques
Inícios
Visualizações de produto
Checkouts
Pagamentos
Receita por campanha
Conversão por origem
```

---

\## 7. Catálogo

\## Tela principal

```markdown
Biblioteca Premium
27 itens disponíveis.
[ Ver catálogo ]
[ Minhas compras ]
[ Voltar ao menu ]
```

\## Produto

```markdown
Prévia
Título
Descrição curta
Preço
[ Comprar ]
[ Próximo ]
[ Anterior ]
[ Minhas compras ]
[ Menu ]
```

\## Paginação

Não é necessário gravar apenas uma posição global na sessão. Use:

```markdown
product.position
```

Ao clicar em próximo:

```markdown
SELECT *
FROM products
WHERE tenant_id = :tenant
  AND status = 'ACTIVE'
  AND position > :current_position
ORDER BY position
LIMIT 1;
```

Caso não exista próximo item:

```markdown
Retornar ao primeiro
ou
Mostrar “fim do catálogo”
```

---

\## 8. Carrinho e order bump

\## Fluxo

```markdown
Produto principal
       ↓
Adicionar ao carrinho
       ↓
Oferta complementar
       ↓
Aceitar ou recusar
       ↓
Resumo do pedido
       ↓
Pagamento
```

\## Regras

O carrinho deve calcular valores exclusivamente no servidor:

```markdown
total = items.reduce(
  (sum, item) => sum + item.unitPrice * item.quantity,
  0
);
```

Nunca aceite preço vindo do Telegram.

\## Order bump configurável

```markdown
{
  "trigger_product_id": "membership_monthly",
  "offered_product_id": "bundle_extra",
  "discount_type": "FIXED",
  "discount_value": 10,
  "active": true
}
```

O painel deve permitir:

- ativar ou desativar;
- definir produto;
- definir preço;
- limitar por campanha;
- limitar a primeira compra;
- medir aceitação.

---

\## 9. Pagamento validado para 2026

\## Problema do fluxo observado

Os prints mostram:

```markdown
Produto digital
→ checkout dentro do bot
→ Pix/cartão externo
→ entrega digital
```

Pelas regras atuais da plataforma, esse fluxo não deve ser reproduzido para vendas digitais realizadas dentro do Telegram. O pagamento deve usar Telegram Stars. [^1]

\## Fluxo correto

```markdown
Usuário clica em comprar
        ↓
Backend cria pedido
        ↓
Bot executa sendInvoice
currency = XTR
        ↓
Telegram envia pre_checkout_query
        ↓
Backend valida:
- pedido
- preço
- estoque/regra
- usuário
        ↓
answerPreCheckoutQuery
        ↓
Telegram envia successful_payment
        ↓
Backend grava pagamento
        ↓
Cria entitlement
        ↓
Entrega conteúdo
```

Para produtos digitais, o Telegram determina o uso de XTR, e o fluxo oficial exige armazenar o telegram\_payment\_charge\_id, inclusive para possíveis reembolsos. [^1]

\## Pseudocódigo

```markdown
async function handleSuccessfulPayment(update: TelegramUpdate) {
  const payment = update.message?.successful_payment;
  if (!payment) return;
  await database.transaction(async (tx) => {
    const existing = await tx.payment.findUnique({
      where: {
        telegramPaymentChargeId: payment.telegram_payment_charge_id
      }
    });
    if (existing) return;
    const order = await tx.order.findByPayload(
      payment.invoice_payload
    );
    if (!order || order.status !== "AWAITING_PAYMENT") {
      throw new Error("Invalid order state");
    }
    await tx.payment.create({
      orderId: order.id,
      provider: "TELEGRAM_STARS",
      telegramPaymentChargeId:
        payment.telegram_payment_charge_id,
      amount: payment.total_amount,
      currency: payment.currency,
      status: "PAID"
    });
    await tx.order.update(order.id, {
      status: "PAID",
      paidAt: new Date()
    });
    await tx.entitlement.grantFromOrder(order.id);
  });
  await deliveryQueue.add("deliver-order", {
    orderId: payment.invoice_payload
  });
}
```

\## Assinaturas

O Telegram também suporta assinaturas pagas com Stars. [^3] Para o MVP, existem duas estratégias:

\### Estratégia A — Compra avulsa

Mais simples:

```markdown
Pagamento único
→ acesso permanente ao produto
```

\### Estratégia B — Assinatura

```markdown
Pagamento recorrente
→ acesso durante o período ativo
→ revogação ao expirar
```

---

\## 10. Entrega digital

\## Estratégia 1 — Entrega pelo bot

```markdown
Pagamento confirmado
        ↓
Worker consulta product_assets
        ↓
Bot envia mídias
        ↓
protect_content = true
        ↓
Registra entrega
```

O Bot API oferece protect\_content, que restringe encaminhamento e salvamento de mensagens protegidas. Isso reduz compartilhamentos casuais, embora não elimine capturas de tela ou gravação externa. [^3]

\## Estratégia 2 — Biblioteca interna

O usuário acessa:

```markdown
Minhas compras
   ↓
Produto adquirido
   ↓
Reabrir conteúdo
```

Antes de entregar:

```markdown
SELECT *
FROM entitlements
WHERE tenant_id = :tenant
  AND user_id = :user
  AND product_id = :product
  AND status = 'ACTIVE';
```

\## Estratégia 3 — Mini App

Uma Mini App fornece:

- catálogo visual;
- biblioteca;
- filtros;
- busca;
- carrinho;
- histórico;
- perfil;
- assinatura. O Telegram permite que Mini Apps funcionem como interfaces completas dentro do aplicativo. [^4]

\### Recomendação

```markdown
MVP:
Bot com botões inline
Versão 2:
Bot + Mini App para catálogo e painel do cliente
```

---

\## 11. Acesso a comunidade privada

\## Fluxo seguro

```markdown
Pagamento confirmado
       ↓
Entitlement ativo
       ↓
Bot cria link temporário
       ↓
Link gera solicitação de entrada
       ↓
Bot recebe chat_join_request
       ↓
Consulta assinatura
       ↓
Aprova ou recusa
```

O Telegram permite criar links que geram solicitações de entrada e fornece eventos e métodos para aprovar ou negar essas solicitações. O bot precisa ser administrador e ter permissão para convidar usuários. [^3]

\## Link recomendado

```markdown
Uso único
Expiração de 15 minutos
Associado ao usuário
Identificado pelo pedido
```

Tabela:

```markdown
invite_links
-------------
id
tenant_id
user_id
subscription_id
chat_id
invite_link
status
expires_at
used_at
created_at
```

\## Expiração

Job periódico:

```markdown
A cada hora
   ↓
Buscar assinaturas expiradas
   ↓
Revogar entitlement
   ↓
Remover membro
   ↓
Registrar auditoria
   ↓
Enviar opção de renovação
```

---

\## 12. Campanhas e recuperação

\## Segmentos

```markdown
Iniciou e não abriu catálogo
Abriu catálogo e não visualizou produto
Visualizou e não adicionou ao carrinho
Criou checkout e não pagou
Comprou item avulso
Assinatura próxima do vencimento
Assinatura expirada
Usuário inativo
```

\## Eventos

```markdown
user.started
menu.opened
catalog.opened
product.viewed
cart.item_added
cart.abandoned
checkout.created
payment.succeeded
order.delivered
membership.activated
membership.expired
campaign.clicked
support.requested
```

\## Automação no n8n

```markdown
Webhook de evento
        ↓
Identificar segmento
        ↓
Aplicar regra de frequência
        ↓
Aguardar intervalo
        ↓
Verificar se ainda está elegível
        ↓
Enviar campanha
        ↓
Registrar resultado
```

Regra indispensável:

```markdown
Antes de enviar recuperação:
verificar novamente se o usuário comprou.
```

Sem essa checagem, o comprador recebe “você esqueceu de pagar” depois de já ter pago. Excelente para transformar fidelização em filme de terror corporativo.

\## Limites de comunicação

Manter:

```markdown
frequency_cap
quiet_hours
opt_out
blocked_at
last_campaign_at
```

Exemplo:

```markdown
No máximo 1 campanha comercial por 24 horas
Não enviar entre 22h e 8h
Parar após /stop
```

---

\## 13. Painel administrativo

\## Dashboard

```markdown
Receita
Compras
Usuários ativos
Conversão
Ticket médio
Produtos mais vendidos
Checkouts abandonados
Assinaturas ativas
Cancelamentos
Campanhas
```

\## Gestão de produtos

```markdown
Criar produto
Editar produto
Cadastrar mídia
Definir preço em Stars
Ordenar catálogo
Criar bundle
Criar order bump
Ativar ou desativar
```

\## Gestão de usuários

```markdown
Pesquisar usuário
Ver histórico
Ver pagamentos
Ver compras
Conceder acesso
Revogar acesso
Reenviar conteúdo
Bloquear
Abrir suporte
```

\## Campanhas

```markdown
Selecionar segmento
Criar mensagem
Adicionar mídia
Agendar
Testar
Disparar
Pausar
Ver métricas
```

\## Multi-tenant

Um administrador da Marca A nunca pode acessar dados da Marca B. Todas as queries precisam incluir:

```markdown
WHERE tenant_id = :authenticatedTenant
```

\## Não basta confiar no frontend. O isolamento deve existir no backend e, idealmente, com Row Level Security no banco.

\## 14. Segurança

\## Obrigatório

```markdown
Webhook secret token
Tokens criptografados
RBAC administrativo
Idempotência
Rate limiting
Logs de auditoria
Backups
Isolamento multi-tenant
Validação de callbacks
Expiração de sessões
Proteção contra entrega duplicada
```

\## Idempotência de pagamento

```markdown
successful_payment recebido duas vezes
        ↓
consultar telegram_payment_charge_id
        ↓
se já existe:
não cobrar
não entregar novamente
não gerar nova assinatura
```

\## Idempotência da entrega

```markdown
UNIQUE(order_id, product_id, user_id)
```

\## Auditoria

Registrar:

```markdown
Quem concedeu acesso
Quem revogou
Qual pagamento originou o acesso
Quando o conteúdo foi entregue
Qual campanha foi enviada
Quem alterou preço
Quem alterou gateway/configuração
```

\## Segredos

```markdown
BOT_TOKEN
DATABASE_URL
REDIS_URL
ENCRYPTION_KEY
WEBHOOK_SECRET
STORAGE_SECRET
```

\## Nunca armazenar isso em workflows exportados, repositórios públicos ou campos comuns do banco.

\## 15. Suporte, termos e reembolsos

O fluxo oficial para vendas digitais exige suporte claro, termos acessíveis e tratamento de problemas de pagamento. A documentação recomenda /terms, /support e exige capacidade de atender /paysupport; reembolsos em Stars podem ser processados pelo método refundStarPayment. [^1] Comandos:

```markdown
/start
/menu
/catalogo
/compras
/assinatura
/support
/paysupport
/terms
/privacy
/stop
```

Antes do pagamento:

```markdown
[ ] Confirmo que li os termos
```

O registro deve salvar:

```markdown
terms_version
accepted_at
telegram_user_id
```

---

\## 16. Observabilidade

\## Métricas

```markdown
telegram_updates_total
telegram_update_failures
callback_latency
payment_success_rate
payment_failure_rate
delivery_success_rate
delivery_failures
campaign_send_rate
campaign_block_rate
active_subscriptions
expired_subscriptions
queue_depth
```

\## Alertas

```markdown
Webhook sem eventos
Fila acumulada
Falha de banco
Redis indisponível
Pagamento confirmado sem entrega
Entrega duplicada
Muitas falhas do Telegram
Campanha com bloqueios anormais
```

\## Regra operacional crítica

Criar um reconciliador:

```markdown
A cada 15 minutos:
buscar pedidos PAID sem entitlement
buscar pedidos PAID sem entrega
buscar assinaturas ACTIVE vencidas
buscar entregas FAILED
corrigir ou alertar
```

\## Esse processo é a rede de segurança. Webhooks eventualmente falham; a arquitetura não pode depender de perfeição mitológica.

\## 17. Testes de validação

\## Onboarding

- /start cria apenas um usuário;
- repetir /start não duplica dados;
- origem da campanha é registrada;
- menu é exibido corretamente.

\## Catálogo

- próximo e anterior funcionam;
- produto desativado não aparece;
- usuário não altera preço pelo callback;
- fim do catálogo é tratado.

\## Carrinho

- item duplicado não duplica indevidamente;
- order bump pode ser recusado;
- total é recalculado pelo servidor;
- carrinho expirado não gera pedido inválido.

\## Pagamento

- pedido correto é associado à invoice;
- pagamento repetido é ignorado;
- valor divergente bloqueia entrega;
- successful\_payment cria entitlement;
- reembolso revoga acesso quando aplicável.

\## Entrega

- apenas compradores recebem;
- reenvio respeita limite;
- falha gera retry;
- entrega repetida não cria múltiplos direitos.

\## Comunidade

- link expira;
- link não pode ser reutilizado;
- assinatura vencida não entra;
- assinatura ativa é aprovada;
- cancelamento revoga acesso.

\## Multi-tenant

- usuário da Marca A não acessa produto B;
- callback manipulado não cruza tenant;
- administrador A não vê receita B;
- arquivos não vazam entre clientes.

\## Campanhas

- comprador não recebe abandono;
- usuário bloqueado não recebe;
- frequência máxima é aplicada;
- opt-out é respeitado.

---

\## 18. Roadmap de implementação

\## Fase 1 — Fundação

```markdown
Multi-tenant
Cadastro de bots
Webhook
Usuários
Menu
Logs
```

\## Fase 2 — Comércio

```markdown
Produtos
Catálogo
Carrinho
Order bump
Pedidos
Telegram Stars
```

\## Fase 3 — Entrega

```markdown
Entitlements
Minhas compras
Envio de ativos
Proteção
Retry
```

\## Fase 4 — Comunidade

```markdown
Planos
Assinaturas
Links temporários
Join requests
Revogação
```

\## Fase 5 — Automação

```markdown
Eventos
Redis/BullMQ
n8n
Campanhas
Recuperação
Relatórios
```

\## Fase 6 — SaaS

```markdown
Painel administrativo
Onboarding de tenants
RBAC
Cobrança da plataforma
Analytics
White-label
```

---

\## 19. Estrutura de repositório

```markdown
ginkgo-creator-commerce/
├── apps/
│ ├── api/
│ ├── bot-worker/
│ ├── campaign-worker/
│ ├── delivery-worker/
│ ├── admin-dashboard/
│ └── mini-app/
│
├── packages/
│ ├── database/
│ ├── telegram/
│ ├── payments/
│ ├── events/
│ ├── queue/
│ ├── security/
│ └── shared/
│
├── infrastructure/
│ ├── docker/
│ ├── traefik/
│ ├── migrations/
│ └── monitoring/
│
├── n8n/
│ ├── campaigns/
│ ├── alerts/
│ ├── reports/
│ └── crm/
│
└── docs/
    ├── architecture.md
    ├── database.md
    ├── events.md
    ├── security.md
    └── deployment.md
```

---

\## 20. Validação final

\## Funcionalmente validado

A réplica consegue reproduzir:

```markdown
/start
Menu
Catálogo
Paginação
Produto avulso
Carrinho
Order bump
Pagamento
Minhas compras
Assinatura
Comunidade
Campanhas
Suporte
```

\## Não validado pelos prints

Ainda não é possível afirmar:

```markdown
Qual linguagem foi usada
Qual gateway original
Qual banco original
Se o acesso VIP é realmente automático
Como funciona o reembolso
Como ocorre o cancelamento
Como é feito o painel administrativo
Se existe proteção contra fraude
```

\## Alteração obrigatória

```markdown
Arquitetura observada:
Pix/cartão para produto digital dentro do bot
Arquitetura recomendada:
Telegram Stars para produto digital dentro do bot
```

\## Classificação técnica

```markdown
Modelo de negócio: validado
Arquitetura white-label: fortemente validada
Catálogo e checkout: validados
Campanhas automáticas: validadas
Infraestrutura interna original: não identificada
Replicação técnica: viável
Replicação literal do pagamento por Pix: não recomendada
```

\## Os QR Codes e códigos Pix enviados nos prints devem ser tratados como informações expostas. Não reutilize essas capturas publicamente e, nos próximos registros, cubra QR Code, código copia e cola, identificadores e dados do recebedor.

\## \*\*Você disse\*\* podemos validar nós mesmo? utilizando a melhor opção para cada com o resultado final sendo este? somar a uma dashboard de configuração e criação entre aspas em massa, exemplo 30 bots, tornar replicavel, copia e cola.

\## Veredito

\## \*\*Sim. É viável construir uma plataforma própria com o resultado visual e funcional semelhante ao painel da imagem, preparada para operar 30, 100 ou mais bots a partir de templates.\*\* A mudança decisiva é que o Telegram agora oferece oficialmente o conceito de \*\*Management Bot\*\*. Um bot principal pode ser habilitado no BotFather para permitir que usuários criem bots gerenciados por ele. Após a confirmação da criação, o bot gerenciador recebe um evento managed\_bot, consegue obter o token com getManagedBotToken e também pode rotacioná-lo posteriormente. Isso elimina boa parte do trabalho artesanal que antes exigia copiar tokens manualmente. [^5] O escopo deve permanecer voltado a conteúdo premium lícito e não explícito: comunidades, cursos, creators, clubes, newsletters, mentorias e bibliotecas digitais.

\## 1. Produto final

O produto seria uma espécie de:

\## Ginkgo Bot Factory

```markdown
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

Não teremos 30 projetos, 30 bancos e 30 instalações. Teremos:

```markdown
1 plataforma
1 backend
1 painel
1 banco multi-tenant
1 infraestrutura de filas
30 configurações de bots
```

\## Cada bot será uma “skin” independente sobre o mesmo motor.

\## 2. Validação do modelo da imagem

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
| Tecnicamente, tudo isso é reproduzível. Porém, o MVP não deve copiar todos os botões do painel logo de início. Isso produziria um porta-aviões antes de validar se o motor liga. |  |

---

\## 3. Arquitetura correta

```markdown
CONTROL PLANE
                Painel administrativo Next.js
                             │
            ┌────────────────┼────────────────┐
            ▼ ▼ ▼
      Configurações Templates Analytics
            │ │ │
            └────────────────┼────────────────┘
                             ▼
                    API multi-tenant
                   NestJS + TypeScript
                             │
       ┌─────────────────────┼─────────────────────┐
       ▼ ▼ ▼
Bot Provisioner Flow Engine Commerce Engine
       │ │ │
       ▼ ▼ ▼
Telegram API Redis + BullMQ Orders + Stars
       │ │ │
       └─────────────────────┼─────────────────────┘
                             ▼
                   PostgreSQL / Supabase
                             │
               ┌─────────────┴─────────────┐
               ▼ ▼
         Object Storage n8n
           R2/S3 Integrações e automações
```

\## Control plane

É o painel semelhante ao da imagem:

- cria bots;
- clona templates;
- altera conteúdo;
- configura produtos;
- publica campanhas;
- consulta métricas;
- gerencia clientes.

\## Data plane

É o motor invisível:

- recebe os webhooks;
- responde aos comandos;
- controla carrinhos;
- registra pagamentos;
- entrega produtos;
- dispara campanhas;
- controla permissões. Essa separação impede que o painel administrativo e os bots se transformem em um único monólito radioativo.

---

\## 4. Melhor tecnologia para cada camada

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

\## Papel do n8n

O n8n entra como braço robótico, não como cérebro principal. Use para:

```markdown
CRM
Relatórios
Alertas
Recuperação de usuários
Notificações administrativas
Integrações externas
Sincronização de dados
```

Não use como núcleo de:

```markdown
Callbacks
Carrinho
Pagamento
Controle de acesso
Entrega
Sessões
Idempotência
```

---

\## 5. Criação em massa de bots

Existem dois caminhos oficiais.

\## Caminho A — Management Bot

É a melhor escolha para o produto. O operador cria um bot gerenciador e ativa o \*\*Bot Management Mode\*\*. A plataforma gera links com nome e username pré-preenchidos:

```markdown
https://t.me/newbot/ManagerBot/NovoBotUsername?name=Novo+Bot
```

O usuário confirma a criação no Telegram. Depois disso:

```markdown
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

Esse mecanismo é documentado oficialmente pelo Telegram. [^5]

\## Caminho B — Conectar token existente

O operador já criou o bot e cola o token:

```markdown
Adicionar bot
→ informar token
→ validar getMe
→ registrar webhook
→ aplicar template
→ publicar
```

O painel deve suportar os dois caminhos:

```markdown
[ Criar bot automaticamente ]
[ Conectar bot existente ]
```

\## Limitação operacional

O processo via Management Bot ainda inclui uma confirmação do proprietário no Telegram. Portanto, para 30 bots teremos aproximadamente:

```markdown
90% automatizado
10% confirmação oficial do Telegram
```

\## Não recomendo automatizar contas pessoais ou sessões de usuário para contornar essa confirmação.

\## 6. Processo de provisionamento

Ao criar um bot, o backend executará um job:

```markdown
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

```markdown
POST /webhooks/telegram/{botPublicId}
```

Cada bot terá um secret\_token próprio. O Telegram envia esse segredo no cabeçalho X-Telegram-Bot-Api-Secret-Token, permitindo validar as chamadas recebidas. [^2] Exemplo interno:

```markdown
/webhooks/telegram/bot_01
/webhooks/telegram/bot_02
/webhooks/telegram/bot_03
```

\## Não exponha o token verdadeiro na URL.

\## 7. Template “copia e cola”

O coração do produto será um blueprint versionado.

```markdown
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

```markdown
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

\## Importação em massa

O painel pode aceitar CSV:

```markdown
name,username,template,brand,support,language
Academy One,academy_one_bot,course-v1,academy-one,@support,pt-BR
Community Two,community_two_bot,community-v1,community-two,@support,en-US
News Three,news_three_bot,newsletter-v1,news-three,@support,pt-BR
```

Depois:

```markdown
Importar CSV
→ validar usernames
→ gerar 30 provisionamentos
→ criar links oficiais
→ acompanhar confirmações
→ ativar automaticamente
```

---

\## 8. Runtime para 30 bots

Não precisamos iniciar um servidor separado para cada bot.

```markdown
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

```markdown
bot:{botId}:config
bot:{botId}:commands
bot:{botId}:template
bot:{botId}:rate_limit
```

Banco:

```markdown
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

```markdown
tenant_id
bot_id
```

\## Assim, os dados do Bot A nunca cruzam com o Bot B.

\## 9. Motor de fluxos

A área “Meus Fluxos” não deve usar workflows n8n diretamente. Ela deve funcionar como uma máquina de estados própria:

```markdown
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

```markdown
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

```markdown
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

\## Isso torna qualquer fluxo clonável e versionável.

\## 10. Pagamentos

Para bens digitais, assinaturas e acesso a conteúdo dentro do Telegram, o método nativo deve ser \*\*Telegram Stars\*\*, usando moeda XTR. O fluxo oficial utiliza sendInvoice, pre\_checkout\_query, answerPreCheckoutQuery e successful\_payment. O identificador telegram\_payment\_charge\_id deve ser armazenado para reconciliação e possíveis reembolsos. [^6] O dashboard pode suportar:

| Gateway | Uso |
| --- | --- |
| Telegram Stars | Produtos digitais dentro do Telegram |
| Pix | Produtos físicos ou operações externas compatíveis |
| Stripe | SaaS, serviços externos e cobrança da plataforma |
| Mercado Pago | Operações externas compatíveis |
| Pagar.me | Operações externas compatíveis |
| Para produto digital vendido e entregue dentro do bot ou Mini App, o Telegram exige Stars mesmo que existam outros portais ou gateways externos. [^6] |  |

---

\## 11. Mini App

O bot continuará atendendo por mensagens, mas uma Mini App pode oferecer:

```markdown
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

Mini Apps podem ser abertas por botões inline, pelo menu do bot ou diretamente pelo perfil. O servidor deve validar initData; o objeto initDataUnsafe não deve ser tratado como fonte confiável. [^7] Arquitetura:

```markdown
Bot
 ├── Conversas e notificações
 └── Botão “Abrir plataforma”
              ↓
          Mini App
              ↓
       API compartilhada
```

\## Para o MVP, não é obrigatória. Para um produto semelhante ao screenshot, torna-se importante na segunda fase.

\## 12. Remarketing em massa

Cada bot possui limite gratuito padrão de broadcast de até 30 mensagens por segundo. O Telegram também oferece Paid Broadcasts de até 1.000 mensagens por segundo, cobrando Stars por mensagem enviada acima do limite gratuito. [^2] A fila deve ser isolada por bot:

```markdown
campaign:{botId}
```

E aplicar:

```markdown
Rate limit por bot
Retry exponencial
Controle de duplicidade
Opt-out
Quiet hours
Segmentação
Supressão de compradores
```

Exemplo:

```markdown
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

\## 13. Dashboard MVP

\## Menu inicial recomendado

```markdown
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

\## Deixar para depois

```markdown
Ranking
Premiações
Roleta
Bio Link avançado
Marketplace
Gamificação
Relatórios extremamente detalhados
```

\## O painel mostrado possui boa amplitude, mas o MVP deve concentrar-se no motor que gera receita.

\## 14. Criação de 30 bots

O fluxo operacional ideal:

```markdown
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

```markdown
Provisionamento em massa
Bot 01 Confirmado Configurando 80%
Bot 02 Aguardando confirmação
Bot 03 Ativo
Bot 04 Erro no username
Bot 05 Teste aprovado
...
Bot 30 Ativo
```

Ações em massa:

```markdown
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

\## 15. Validação técnica

\## Etapa 1 — Três bots

Construir:

```markdown
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

```markdown
Criação oficial funcionando
Token recuperado
Webhook configurado
Template clonado
Pagamento registrado
Produto entregue
Dados isolados
```

\## Etapa 2 — Dez bots

Validar:

```markdown
Filas
Cache
Campanhas
Atualizações em massa
Isolamento multi-tenant
Falhas parciais
Rollback
```

\## Etapa 3 — Trinta bots

Validar:

```markdown
Provisionamento em lote
Carga simultânea
Broadcasts
Rotação de tokens
Recuperação de falhas
Observabilidade
Custos operacionais
```

Não iniciar diretamente com 30. O caminho seguro é:

```markdown
3 → 10 → 30
```

---

\## 16. Critérios de aceite

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

\## 17. Roadmap realista

\## Epic 0 — Fundação

```markdown
Monorepo
Autenticação
Tenants
RBAC
PostgreSQL
Redis
Auditoria
Docker
```

\## Epic 1 — Bot Factory

```markdown
Management Bot
Conectar token
Provisionamento
Webhooks
Tokens criptografados
Status dos bots
```

\## Epic 2 — Template Engine

```markdown
Blueprint JSON
Variáveis
Clonagem
Versionamento
Importação e exportação
```

\## Epic 3 — Flow Builder

```markdown
Editor visual
Nós
Conexões
Condições
Publicação
Rollback
```

\## Epic 4 — Commerce

```markdown
Produtos
Pedidos
Stars
Entitlements
Minhas compras
Entrega
```

\## Epic 5 — Growth

```markdown
Campanhas
Segmentos
Remarketing
Deep links
Afiliados
Analytics
```

\## Epic 6 — Mass Operations

```markdown
CSV
Provisionamento em lote
Alterações em massa
Testes em lote
Dashboard operacional
```

---

\## Decisão final

A solução correta não é recriar cada bot individualmente. É construir:

```markdown
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

\## A principal descoberta é que a criação escalável deixou de ser apenas uma gambiarra em torno do BotFather: o Telegram agora possui infraestrutura oficial para \*\*managed bots\*\*, o que encaixa diretamente no modelo de uma fábrica white-label. [^5] O próximo artefato técnico deve ser o \*\*Epic 0 + Epic 1\*\*, com schema do banco, estrutura do monorepo, Docker Compose e fluxo completo de criação/conexão dos primeiros três bots.

\*\*Você disse\*\* Certo, e falando das telas e configurações dos bots, o resultado esperado é como o dos prints

\## Footnotes

**Sharkbot.com.br** é uma plataforma **SaaS white-label** (multi-tenant) para criação de bots de vendas no Telegram, focada em criadores de conteúdo premium (cursos, comunidades VIP, produtos digitais, etc.). Ela permite que usuários configurem bots personalizados com catálogo, carrinho, order bump, checkout com Pix/cartão (manual ou semi-automático) e entrega de acesso.

A análise abaixo baseia-se em engenharia reversa de interfaces/padrões comuns dessas plataformas (como visto em prints e vídeos tutoriais), combinada com a **documentação oficial do Telegram Bot API** (core.telegram.org/bots/api, payments, etc.). Não tenho acesso ao código-fonte interno do Sharkbot, então isso é uma reconstrução técnica precisa do que deve estar acontecendo no backend.

### Arquitetura Geral (Multi-Tenant / White-Label)

- **Modelo**: Um backend central serve dezenas/centenas de bots ("tenants"). Cada cliente tem seu bot próprio, marca, produtos, preços e configurações.
- **Componentes principais**:
	- **Painel Admin** (provavelmente Next.js/React ou similar): Dashboard para criar bots, configurar fluxos, produtos, campanhas, gateways Pix, etc.
		- **Backend/API**: Node.js/NestJS, Python (Aiogram/Telebot) ou PHP/Laravel — comum em ferramentas brasileiras de automação.
		- **Banco de dados**: PostgreSQL ou MySQL (multi-tenant com tenant\_id em todas as tabelas).
		- **Cache/Filas**: Redis + BullMQ/Redis Queue ou similar para sessões, carrinhos e campanhas.
		- **Integração Telegram**: Webhooks (não polling) + bibliotecas como grammY (TypeScript), Telegraf ou Aiogram.
		- **Armazenamento**: S3/R2 para mídias e assets.
		- **Automações**: n8n ou ferramenta similar para campanhas, remarketing e fluxos.

O fluxo é **event-driven**: Telegram → Webhook → Processamento → Resposta + ações (enviar invoice, entregar conteúdo, etc.).

### Fluxo Técnico Principal (Baseado em Telegram Bot API)

1. **Onboarding e Webhook**:
	- Usuário cria bot via BotFather e cola o token no painel do Sharkbot (ou usa fluxo semi-automático).
		- Backend registra o bot\_token (criptografado), configura webhook: setWebhook com URL como https://api.sharkbot.com/webhooks/telegram/:tenant\_id/:bot\_id.
		- Usa secret\_token (X-Telegram-Bot-Api-Secret-Token header) para validar chamadas legítimas.
2. **Estados e Navegação** (Máquina de Estados/FSM):
	- Armazena estado do usuário no Redis/Banco (user\_sessions, user\_state).
		- Callbacks inline (callback\_query) para menus: menu:home, catalog:next, cart:add:product\_id, etc.
		- Catálogo: Consulta dinâmica em tabela products (com paginação via position ou OFFSET/LIMIT).
3. **Carrinho e Order Bump**:
	- Carrinho temporário no Redis ou banco (carts + cart\_items).
		- Cálculo de total **sempre no servidor** (nunca confia em dados do cliente).
		- Order bump: Após adicionar item principal, oferece upsell configurável.
4. **Pagamento (Ponto Crítico — Pix/Cartão)**:
	- **Não usa Telegram Stars nativo** (apesar de ser o recomendado pela Telegram para produtos digitais em 2026). Usa checkout externo:
		- Bot gera invoice/custom QR Pix (via integração com gateway como Mercado Pago, Pagar.me, ou Pix direto via API bancária).
				- Envia via sendMessage ou sendInvoice (mas com provider externo).
				- Confirmação manual: Botão “Paguei, libera acesso” → Webhook verifica pagamento (polling no gateway ou webhook do provedor Pix) e libera.
		- **Aviso oficial Telegram**: Para bens/serviços **digitais** vendidos **dentro do bot/Mini App**, deve usar **Telegram Stars (XTR)** obrigatoriamente (devido a regras Apple/Google). Fluxos com Pix externo podem violar políticas para apps mobile, mas muitos operam assim com confirmação manual.
5. **Confirmação e Entrega**:
	- Ao confirmar pagamento: Cria entitlement (direito de acesso) na tabela.
		- Entrega:
		- Envia mídias com protect\_content: true.
				- Gera invite link temporário para canal/grupo privado (createChatInviteLink + approveChatJoinRequest).
				- Biblioteca “Minhas Compras”.
		- Revogação automática para assinaturas (job periódico verifica subscriptions).
6. **Campanhas e Remarketing**:
	- Eventos rastreados (user.started, product.viewed, cart.abandoned, etc.).
		- n8n ou engine própria dispara broadcasts (limite ~30 msg/seg por bot).
		- Segmentação baseada em histórico.

### Modelo de Dados Provável (Inferido)

- tenants (clientes/marcas)
- bots (por tenant, com token criptografado)
- users (telegram\_user\_id como BIGINT)
- products, orders, payments (com provider: 'pix' ou similar, raw\_payload)
- entitlements e subscriptions
- campaigns + deliveries

Idempotência via UNIQUE constraints (ex: telegram\_payment\_charge\_id ou referência Pix).

### Tecnologias Mais Prováveis (Inferidas de Padrões Brasileiros)

- **Frontend Painel**: Next.js + Tailwind/shadcn.
- **Backend**: Node.js (NestJS/Express) ou Python.
- **Bot**: grammY ou Telegraf.
- **Filas/Automações**: n8n + Redis.
- **Deploy**: Docker em VPS (Hostinger, etc.).

Isso replica **exatamente** o comportamento descrito nos prints: onboarding /start, catálogo, carrinho, Pix manual, campanhas automáticas, multi-bot white-label.

### Diferenças/Recomendações vs. Oficial Telegram (2026)

- **Melhor prática**: Migrar pagamentos digitais para **Telegram Stars** (sendInvoice com currency: "XTR", pre\_checkout\_query + successful\_payment). Mais automático, compliant e sem confirmação manual.
- Sharkbot parece priorizar **Pix brasileiro** (experiência local) com confirmação manual.

Se você quiser replicar isso (como discutido antes), a arquitetura detalhada nas mensagens anteriores (com Management Bot, templates JSON, etc.) é o caminho mais próximo e escalável. Posso ajudar a refinar o schema SQL, código de webhook ou fluxo específico. Quer que eu gere algum artefato (ex: exemplo de handler em TypeScript)?

Sim. O resultado final deve reproduzir dois ambientes conectados:

Dashboard administrativo, semelhante ao SharkBot do print.

Experiência final dentro do Telegram, semelhante aos fluxos enviados anteriormente. Não será apenas uma lista de bots. Será um painel onde cada bot pode ser criado, configurado, clonado, publicado e operado sem editar código.

1. Resultado visual esperado Dashboard principal Estrutura semelhante ao print: ┌───────────────────────────────────────────────────────────────┐ │ Logo / Workspace Usuário / Ajuda │ ├──────────────┬────────────────────────────────────────────────┤ │ Dashboard │ Faturamento Conversão Bots ativos │ │ Ranking │ │ │ Análises │ Meus Robôs │ │ Financeiro │ │ │ Clientes │ \[ Bot 01 \] \[ Bot 02 \] \[ Bot 03 \] \[ + Novo \] │ │ Comunidade │ │ │ │ Leads Vendas Receita Status Template │ │ Meus Robôs │ │ │ Fluxos │ │ │ Remarketing │ │ │ Postagens │ │ │ Gateways │ │ │ Webhooks │ │ └──────────────┴────────────────────────────────────────────────┘ Características:

tema escuro;

menu lateral fixo;

cards de métricas;

status visual do bot;

busca e filtros;

ações rápidas;

edição por abas;

criação individual ou em massa;

indicadores em tempo real. O objetivo não é copiar a marca SharkBot, mas atingir o mesmo padrão funcional com identidade própria da Ginkgo. 2. Tela “Meus Robôs” Essa será a central operacional. Cada bot aparece como um card: ┌────────────────────────────┐ │ Avatar ● ONLINE │ │ Nome do bot │ │ @username\_bot │ │ │ │ Leads 1.248 Vendas 137 │ │ Receita R$ 8.490 │ │ │ │ \[Fluxos\] \[Editar\] \[⋮\] │ └────────────────────────────┘ Ações disponíveis: Abrir painel do bot Editar configurações Duplicar bot Aplicar template Pausar Ativar Testar Visualizar no Telegram Exportar configuração Excluir Rotacionar token Ver logs Filtros: Todos Ativos Inativos Com erro Em configuração Aguardando Telegram Sem pagamento configurado Também haverá seleção múltipla: ☑ Bot 01 ☑ Bot 02 ☑ Bot 03

\[Aplicar fluxo\] \[Alterar mensagem\] \[Pausar\] \[Ativar\] \[Exportar\] 3. Criação de um bot Ao clicar em Novo Bot: Etapa 1 — Origem Como deseja adicionar o bot?

\[ Criar automaticamente \] \[ Conectar bot existente \] \[ Importar configuração JSON \] \[ Criar vários bots por CSV \] Etapa 2 — Identidade Nome público Username Foto Descrição Texto “Sobre” Idioma Fuso horário Nome do suporte Link do suporte Etapa 3 — Template Escolha o modelo inicial:

Creator Premium Comunidade VIP Curso e mentoria Biblioteca digital Newsletter Catálogo de produtos Bot personalizado Etapa 4 — Conteúdo Mensagem de boas-vindas Imagem ou vídeo inicial Menu principal Produtos Planos Campanhas Termos Suporte Etapa 5 — Publicação Validar configurações Registrar webhook Configurar comandos Executar teste Publicar Tela final: Bot criado com sucesso

● Telegram conectado ● Webhook ativo ● Fluxo publicado ● Produto configurado ● Pagamento conectado ● Teste aprovado

\[Abrir no Telegram\] \[Editar bot\] \[Duplicar\] 4. Painel interno de cada bot Ao abrir um bot, teremos abas: Visão geral Configuração Fluxos Produtos Comunidade Campanhas Clientes Pedidos Financeiro Integrações Logs 5. Aba “Visão geral” Informações específicas daquele bot: Receita hoje Receita no mês Novos usuários Conversão Ticket médio Pedidos pendentes Assinaturas ativas Checkouts abandonados Gráficos: Leads por dia Vendas por dia Receita por produto Conversão por origem Desempenho das campanhas Atividade recente: 14:32 Novo usuário iniciou o bot 14:30 Pedido criado 14:28 Pagamento confirmado 14:28 Produto entregue 14:15 Campanha enviada 6. Configuração da identidade do bot Campos: Nome Username Avatar Descrição curta Descrição completa Idioma Fuso horário Moeda visual Suporte Termos Política de privacidade Configurações visuais: Cor principal do painel Ícone do bot Imagem de capa Estilo dos textos Uso de emojis Rodapé das mensagens Configurações técnicas: Token Webhook Secret token Status Última atualização Último evento recebido Versão do template O token deve aparecer mascarado: 123456:AA\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*X9 7. Configuração do /start Tela visual: Mensagem inicial

Tipo de mídia: ( ) Imagem ( ) Vídeo ( ) GIF ( ) Sem mídia

\[Selecionar arquivo\]

Texto: ┌─────────────────────────────────────┐ │ Bem-vindo, {{first\_name}}... │ └─────────────────────────────────────┘

Botões: \[ Comunidade Premium \] \[ Conteúdos \] \[ Minhas compras \] \[ Suporte \] Pré-visualização lateral: ┌──────────────────────┐ │ Telegram Preview │ │ │ │ \[imagem\] │ │ Bem-vindo... │ │ │ │ \[Comunidade Premium\] │ │ \[Conteúdos\] │ │ \[Minhas compras\] │ │ \[Suporte\] │ └──────────────────────┘ Isso permite editar e ver o resultado antes de publicar. 8. Construtor de menus Cada botão será configurado visualmente. Exemplo: Texto do botão: Comunidade Premium

Ação: \[ Abrir fluxo \]

Fluxo: Oferta VIP

Posição: Linha 1

Largura: 100% Tipos de ação: Abrir fluxo Abrir produto Abrir catálogo Abrir compras Abrir URL Abrir suporte Criar checkout Executar webhook Voltar ao menu O operador pode arrastar os botões: ┌─────────────────────────────┐ │ Comunidade Premium │ ├─────────────────────────────┤ │ Catálogo │ ├──────────────┬──────────────┤ │ Compras │ Suporte │ └──────────────┴──────────────┘ 9. Construtor de fluxos A experiência será semelhante a n8n, ManyChat ou Typebot, mas focada em Telegram. \[ Trigger /start \] ↓ \[ Enviar vídeo \] ↓ \[ Enviar mensagem \] ↓ \[ Mostrar menu \] ↓ \[ Usuário escolheu VIP? \] ↙ ↘ Sim Não ↓ ↓ \[Oferta\] \[Catálogo\] Nós do editor: Mensagem Imagem Vídeo Áudio Documento Álbum Botões Condição Aguardar Variável Tag Produto Carrinho Checkout Verificar pagamento Liberar acesso Remover acesso Enviar webhook Iniciar outro fluxo Finalizar Cada fluxo terá: Rascunho Versão publicada Histórico de versões Teste Rollback Duplicar Exportar 10. Produtos e conteúdos avulsos Tela de produtos: Produtos

\[+ Novo produto\] \[Importar\] \[Reordenar\]

Produto A R$ 50 Ativo Produto B R$ 25 Ativo Produto C R$ 90 Rascunho Configuração de produto: Nome Descrição Preço Tipo Capa Prévia Arquivos entregáveis Ordem no catálogo Status Limite de acesso Proteção de conteúdo Tipos: Conteúdo avulso Pacote Assinatura Comunidade Curso Arquivo Link externo O comportamento será igual ao observado: Prévia Descrição Preço

\[Comprar\] \[Ver próximo\] \[Minhas compras\] \[Menu\] 11. Catálogo Configurações: Título do catálogo Mensagem introdutória Quantidade de produtos por página Ordem dos produtos Filtros Categorias Produto inicial Comportamento ao chegar ao final Opções: Voltar ao primeiro item Mostrar fim do catálogo Abrir menu Exibir produtos recomendados 12. Área “Minhas compras” Configuração da tela: Mensagem de apresentação Exibir data da compra Exibir preço Permitir reenvio Limite de reenvios Exibir produtos expirados Botão de suporte Resultado no Telegram: Minhas compras

1. Produto A Comprado em 23/07/2026

\[Visualizar novamente\]

2. Produto B Acesso válido até 23/08/2026

\[Acessar\] 13. Configuração de comunidade premium Campos: Nome do plano Descrição Preço Duração Canal ou grupo Mensagem antes da compra Mensagem após a compra Mensagem de renovação Mensagem de expiração Período de tolerância Automação: Pagamento confirmado → criar permissão → gerar convite → aprovar entrada → registrar acesso Expiração: Assinatura vencida → enviar aviso → aguardar tolerância → remover do canal → oferecer renovação 14. Order bump e upsell Configuração visual: Produto principal: Plano Premium

Oferta complementar: Pacote Extra

Texto: Adicione também este conteúdo por...

Preço original: R$ 50

Preço da oferta: R$ 30

\[Ativar order bump\] Resultado: Antes de finalizar, deseja adicionar o pacote?

\[Sim, adicionar\] \[Não, continuar\] Também poderemos configurar: Upsell depois da compra Downsell Bundle Desconto para primeira compra Oferta limitada por campanha 15. Checkout e pagamentos A tela terá: Métodos ativos Telegram Stars Stripe Pix Mercado Pago Gateway personalizado Para cada produto, o sistema define o trilho compatível com sua entrega e com as regras da plataforma. Configurações: Mensagem de checkout Expiração do pedido Mensagem de pagamento pendente Mensagem de pagamento aprovado Mensagem de falha Mensagem de reembolso Pedidos: #PED-1032 Usuário Produto Valor Status Gateway Data Entrega Status visuais: Pendente Pago Entregue Expirado Reembolsado Falhou Em disputa 16. Remarketing Tela: Campanhas

Recuperação de carrinho Ativa Boas-vindas D+1 Ativa Produto recomendado Pausada Renovação de assinatura Ativa Editor: Público: Usuários que abriram o produto e não compraram

Aguardar: 2 horas

Condição: Ainda não comprou?

Mensagem: Você deixou algo para trás...

Botão: \[Continuar compra\] Configurações: Frequência máxima Horário permitido Intervalo Segmento Bot Produto Campanha UTM 17. Postagens Área para publicação em massa: Criar postagem Selecionar bots Selecionar público Adicionar mídia Agendar Testar Publicar Exemplo: Bots selecionados: 18 Usuários elegíveis: 42.430 Envio estimado: 28 minutos

\[Enviar teste\] \[Agendar\] \[Publicar agora\] 18. Clientes Tabela: Nome Telegram Bot Status Tags Compras Receita Última interação Perfil do cliente: Dados do Telegram Origem Histórico de mensagens Produtos visualizados Carrinho Pedidos Pagamentos Compras Assinaturas Campanhas recebidas Logs Ações: Conceder produto Revogar produto Adicionar tag Remover tag Enviar mensagem Bloquear Abrir suporte 19. Configuração em massa para 30 bots Teremos um Template Mestre. Exemplo: Template: Creator Premium v1

Inclui: ✓ Fluxo /start ✓ Menu ✓ Catálogo ✓ Minhas compras ✓ Comunidade ✓ Checkout ✓ Order bump ✓ Remarketing ✓ Suporte Ao criar um novo bot: Duplicar template → trocar nome → trocar avatar → trocar textos → trocar mídias → trocar produtos → trocar canal → publicar Variáveis: {{BOT\_NAME}} {{CREATOR\_NAME}} {{SUPPORT\_USERNAME}} {{WELCOME\_TEXT}} {{WELCOME\_MEDIA}} {{COMMUNITY\_NAME}} {{PRICE}} {{CHANNEL\_ID}} Para 30 bots, será possível editar em planilha: Bot Nome Username Avatar Template Produto Preço Canal Suporte Status Depois executar: \[Aplicar configurações\] \[Publicar 30 bots\] 20. Biblioteca de templates Tela: Templates

Creator Premium v1 Curso v1 Comunidade v1 Newsletter v1 Catálogo v1

\[Usar template\] \[Duplicar\] \[Editar\] \[Exportar\] Cada template inclui: Fluxos Menus Mensagens Produtos de exemplo Campanhas Variáveis Configurações Não inclui: Tokens Dados de clientes Pedidos Pagamentos Segredos 21. Importação e exportação Cada bot poderá ser exportado como JSON: { "bot": { "name": "Bot Exemplo", "language": "pt-BR" }, "template": "creator-premium-v1", "menus": \[\], "flows": \[\], "products": \[\], "campaigns": \[\], "settings": {} } Fluxo copia e cola: Exportar Bot A → baixar JSON → importar como Bot B → substituir variáveis → publicar Ou diretamente: \[Duplicar bot\] 22. Critério de aceite visual e funcional O produto estará correto quando o operador conseguir: Entrar no painel → criar um bot → aplicar um template → editar textos e mídias → configurar produtos → publicar → testar no Telegram Sem abrir: VS Code Terminal n8n Banco de dados BotFather manualmente, salvo confirmação necessária E o usuário final receberá: /start → apresentação → menu → catálogo → compra → pagamento → entrega → minhas compras → campanhas Exatamente como a experiência estrutural dos prints, mas com:

identidade própria;

arquitetura escalável;

gestão em massa;

versionamento;

logs;

segurança;

isolamento entre bots;

painel configurável. Escopo correto do primeiro produto A primeira versão deve entregar estas telas:

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
15. Logs Esse conjunto já entrega o resultado dos prints e estabelece a fundação para escalar de 3 para 30 bots sem replicar código, infraestrutura ou workflows manualmente.

**Sim.** Vamos construir o **Ginkgo Bot Factory** exatamente conforme a especificação: um painel administrativo completo (tema escuro, multi-bot, templates, fluxos visuais, etc.) conectado a bots Telegram que reproduzem a experiência dos prints (catálogo, carrinho, order bump, entrega, comunidade, campanhas).

O escopo da **Fase 1 (MVP viável)** cobre todas as telas e fluxos que você listou, com arquitetura escalável para 30+ bots sem editar código.

### Stack Escolhida (Produção-Ready)

- **Monorepo**: Turborepo + pnpm
- **Painel Admin**: Next.js 15 (App Router) + TypeScript + Tailwind + shadcn/ui + TanStack Table + Recharts
- **API Backend**: NestJS (ou tRPC para simplicidade no MVP)
- **Bot Runtime**: grammY (TypeScript, excelente para fluxos)
- **Banco**: PostgreSQL + Prisma
- **Cache/Filas**: Redis + BullMQ
- **Armazenamento**: Cloudflare R2 (ou local)
- **Automações**: n8n (integrado via API)
- **Auth**: NextAuth ou Clerk
- **Deploy**: Docker Compose

### 1\. Estrutura do Repositório (Criação Inicial)

Vou criar a estrutura agora. Execute os comandos no seu ambiente ou confirme para eu prosseguir.

```markdown
mkdir ginkgo-bot-factory && cd ginkgo-bot-factory
npx create-turbo@latest . --example basic
# Adicionar apps: admin (Next.js), api (NestJS), bot-worker
# packages: db (Prisma), telegram, shared
```

**Estrutura principal**:

```markdown
ginkgo-bot-factory/
├── apps/
│   ├── admin/          # Dashboard Next.js
│   ├── api/            # Backend NestJS
│   └── bot-worker/     # Runtime dos bots (grammY)
├── packages/
│   ├── db/             # Prisma schema
│   ├── telegram/       # Utils grammY + handlers
│   └── shared/         # Types, utils
├── docker-compose.yml
└── turbo.json
```

### 2\. Modelo de Dados (Prisma Schema - packages/db)

```markdown
model Tenant {
  id        String   @id @default(cuid())
  name      String
  bots      Bot[]
  users     User[]
  products  Product[]
  // ... entitlements, subscriptions, etc.
}

model Bot {
  id            String   @id @default(cuid())
  tenantId      String
  telegramId    BigInt?
  username      String   @unique
  token         String   @encrypted // Criptografado
  webhookSecret String
  name          String
  avatar        String?
  templateId    String?
  status        BotStatus @default(ACTIVE)
  config        Json     // Configurações gerais (JSON)
  flows         Flow[]
  products      Product[]
  // métricas cached
}

model Flow {
  id        String   @id @default(cuid())
  botId     String
  name      String
  nodes     Json     // JSON do construtor visual (nós + conexões)
  version   Int
  published Boolean
  // trigger, etc.
}

model Product {
  id          String   @id @default(cuid())
  botId       String
  name        String
  priceStars  Int?     // Para Stars
  priceBRL    Decimal? // Para Pix
  type        ProductType
  assets      Asset[]
  position    Int
}

enum BotStatus { ACTIVE PAUSED CONFIGURING ERROR }
```

### 3\. Criação de Bots (Management Bot + Templates)

- **Criar automaticamente**: Usa Telegram Management Bot (oficial).
- **Template Engine**: JSON com variáveis {{BOT\_NAME}}, etc. Ao clonar:
	1. Copia flows, menus, products.
		2. Substitui variáveis.
		3. Registra webhook via setWebhook.
		4. Configura comandos.

**Exemplo de handler de provisionamento** (no API):

```markdown
async createBot(data: CreateBotDto) {
  const template = await this.templateService.get(data.templateId);
  const bot = await this.botRepo.create({ ...data, config: template.config });

  // Configura webhook
  await this.telegramService.setWebhook(bot.id, bot.token);

  // Aplica template
  await this.flowService.cloneFromTemplate(bot.id, template);
}
```

### 4\. Construtor de Fluxos (Visual)

Usar **React Flow** ou **X6** no painel. Nós salvos como JSON:

```markdown
{
  "nodes": [
    { "id": "start", "type": "trigger", "data": { "trigger": "/start" } },
    { "id": "msg1", "type": "message", "data": { "text": "Bem-vindo {{first_name}}" } },
    { "id": "menu1", "type": "buttons", "data": { "buttons": [...] } }
  ],
  "edges": [...]
}
```

O bot-worker executa esse grafo com um interpreter simples (state machine).

### 5\. Pagamentos

- Suporte dual: **Telegram Stars** (obrigatório para digital puro) + Pix (manual/semi-automático via gateway).
- sendInvoice + successful\_payment handler.

### 6\. Telas do Painel (Admin Next.js)

- **Tema escuro** via Tailwind + shadcn.
- **Meus Robôs**: Grid de cards com TanStack Table para filtros/ações em massa.
- **Editor /start e Menus**: Formulário + preview em iframe ou componente simulando Telegram.
- **Construtor de Fluxos**: React Flow integrado.
- **Produtos/Catálogo**: Tabela + drag-and-drop para ordem.
- **Campanhas**: Segmentos + scheduler.
- **Operações em Massa**: Upload CSV → job BullMQ processa 30 bots.

### Próximos Passos Imediatos

1. Confirmar: Quer que eu gere o **Prisma schema completo** primeiro?
2. Ou o **setup do monorepo + admin layout** (com sidebar, dashboard cards, tema escuro)?
3. Ou o **bot-worker base** com webhook e handler de /start + menus?

Diga "gere o schema completo" ou "inicie com o admin layout" ou qualquer tela específica, e eu crio os arquivos via ferramentas (escrevo código, docker, etc.). Podemos iterar tela por tela até o MVP estar funcional.

Isso entrega **exatamente** o que você descreveu: painel profissional sem tocar código, templates clonáveis, experiência Telegram idêntica aos prints, e escalabilidade para 30+ bots.

primeiro vamos cravar o local de desenvolvimeto, antigravity? cursor? vscode?

**Resposta direta:**

Vamos cravar o ambiente de desenvolvimento **agora**.

### Recomendação Forte (Minha escolha principal):

**Cursor** (o melhor para este projeto)

**Por quê?**

- É basicamente um **VS Code turbinado com IA** (Claude 3.5 / GPT-4o / Grok).
- Excelente para projetos grandes com monorepo (Turborepo + Next.js + NestJS/Prisma).
- Tem **Composer mode** (edição em massa de arquivos), o que vai acelerar muito a criação de múltiplas telas, componentes shadcn, flows, etc.
- Refatoração inteligente, entendimento de todo o codebase.
- Perfeito para o que vamos fazer: criar dezenas de telas, componentes reutilizáveis, Prisma schema, handlers de bot, etc.

### Alternativas:

| Ferramenta | Vantagem | Desvantagem | Recomendado? |
| --- | --- | --- | --- |
| **Cursor** | Melhor IA + VS Code completo | Ainda em crescimento | **Sim (Principal)** |
| **VS Code** | Mais maduro, extensões infinitas | IA mais lenta (sem Composer) | Boa alternativa |
| **Zed** | Muito rápido | IA ainda inferior | Não para agora |
| **Antigravity** | ? (não uso) | Desconhecido no meu contexto | Não recomendo |

---

**Decisão final recomendada:**

**Vamos usar Cursor.**

### Próximo passo imediato:

1. Baixe/instale o **Cursor** (cursor.com) se ainda não tiver.
2. Crie a pasta do projeto:
	```markdown
	mkdir ginkgo-bot-factory
	cd ginkgo-bot-factory
	```
3. Me avise quando estiver com o Cursor aberto na pasta vazia.

Aí eu te guio passo a passo para:

- Inicializar o monorepo Turborepo
- Configurar o Prisma + PostgreSQL (via Docker)
- Criar a estrutura de pastas
- Setup do tema escuro + shadcn/ui
- Criar o layout base do dashboard (sidebar + header)

Quer seguir com **Cursor**? Ou prefere **VS Code** mesmo?

Responda só com "Cursor" ou "VS Code" que já cravamos e partimos para a criação.

[^1]: [core.telegram.org](https://core.telegram.org/bots/payments-stars?utm_source=chatgpt.com)

[^2]: [core.telegram.org](https://core.telegram.org/bots/api)

[^3]: [core.telegram.org](https://core.telegram.org/bots/api-changelog)

[^4]: [core.telegram.org](https://core.telegram.org/bots?utm_source=chatgpt.com)

[^5]: [core.telegram.org](https://core.telegram.org/bots/features)

[^6]: [core.telegram.org](https://core.telegram.org/bots/payments-stars)

[^7]: [core.telegram.org](https://core.telegram.org/bots/webapps)