---
title: "Análise e replicação bot"
source: "https://chatgpt.com/c/6a5b85f7-d5a8-83e9-babd-4c2e8ffc3f64"
author:
published:
created: 2026-07-23
description: "ChatGPT conversation with 6 messages"
tags:
  - "clippings"
---
**Você disse**

---

Os prints mostram que **não é apenas um bot simples**, mas um motor de vendas white-label reutilizado para diferentes perfis. “Manas Nunes” e “Ruiva Isabel” possuem quase o mesmo esqueleto funcional, mudando marca, catálogo, preço e conteúdo.

O padrão é compatível com uma plataforma pronta de bots para creators, semelhante ao SharkBot, mas os prints não confirmam qual fornecedor está por trás.

## Arquitetura identificada

```
Aquisição / anúncio / link
          ↓
        /start
          ↓
Prévia em vídeo ou imagem
          ↓
Menu principal
├── Grupo/Comunidade VIP
├── Conteúdos avulsos
└── Suporte
          ↓
Oferta principal
          ↓
Order bump / produto adicional
          ↓
Carrinho
          ↓
Checkout Pix ou cartão
          ↓
Verificação do pagamento
          ↓
Liberação do acesso ou produto
```

## 1\. Fluxo de entrada

Ao executar `/start`, o bot envia:

1. mídia de apresentação;
2. texto curto;
3. teclado inline com três opções:
	- acesso VIP;
		- conteúdos avulsos;
		- suporte.

O suporte aparenta ser um botão URL, indicado pelo ícone de link externo.

Representação provável:

```json
{
  "inline_keyboard": [
    [{"text": "Grupo VIP", "callback_data": "menu:vip"}],
    [{"text": "Conteúdo avulso", "callback_data": "menu:store"}],
    [{"text": "Suporte", "url": "https://t.me/usuario_suporte"}]
  ]
}
```

Também há envio automático de outra mídia após o menu, provavelmente uma sequência programada de conversão.

## 2\. Loja de produtos avulsos

O bot possui um catálogo navegável, não apenas links fixos.

Fluxo observado:

```
Conteúdo avulso
    ↓
Página inicial da loja
    ↓
Ver conteúdos
    ↓
Produto atual
├── Comprar
├── Ver próximo
├── Minhas compras
└── Menu
```

A mensagem informa a quantidade total de produtos disponíveis. Em um dos bots aparecem **27 conteúdos cadastrados**.

Cada produto possui provavelmente:

```
product_id
tenant_id
título
descrição
preço
imagem ou vídeo de prévia
arquivos entregáveis
posição no catálogo
status ativo/inativo
```

O botão “Ver próximo” indica um cursor salvo na sessão do usuário:

```json
{
  "telegram_user_id": 123456,
  "catalog_position": 7,
  "last_product_id": "produto_007"
}
```

Callbacks prováveis:

```
store:open
store:view:produto_001
store:next:produto_001
store:buy:produto_001
purchases:list
menu:home
```

## 3\. Carrinho e order bump

O fluxo VIP oferece um produto adicional antes do checkout.

```
Usuário escolhe VIP
        ↓
Oferta adicional
├── Comprar VIP + adicional
└── Comprar somente VIP
```

Isso confirma que existe um carrinho real:

```json
{
  "user_id": 123456,
  "items": [
    {
      "type": "subscription",
      "id": "vip_monthly",
      "price": 5000
    },
    {
      "type": "digital_product",
      "id": "avulso_01",
      "price": 10000
    }
  ],
  "total": 15000
}
```

A divergência observada entre o preço anunciado no botão e o valor exibido no checkout de outro print sugere uma destas situações:

- carrinho persistente;
- bundle VIP mais produto avulso;
- oferta dinâmica;
- campanha com preço diferente;
- erro de configuração do bot.

Essa divergência deve ser evitada na réplica. O preço exibido na oferta precisa ser calculado a partir do próprio pedido, nunca digitado manualmente em mensagens diferentes.

## 4\. Checkout Pix

O bot gera:

- QR Code;
- Pix copia e cola;
- descrição do pedido;
- valor;
- botão para copiar;
- botão para verificar pagamento;
- em um fluxo, opção de cartão;
- alternativa para quem não consegue copiar o Pix.

Fluxo correto:

```
Bot cria pedido
      ↓
Backend solicita cobrança ao gateway
      ↓
Gateway devolve QR e Pix copia e cola
      ↓
Bot exibe a cobrança
      ↓
Gateway envia webhook de pagamento
      ↓
Backend atualiza pedido
      ↓
Bot entrega o produto
```

O botão:

```
“Paguei, libera meu acesso”
```

não pode simplesmente confiar no clique. Ele deve consultar o gateway:

```
GET /payments/{payment_id}
```

ou verificar o status salvo após o webhook:

```
PENDING → PAID → DELIVERED
```

### Estados do pagamento

```
CREATED
PENDING
PAID
FAILED
EXPIRED
REFUNDED
CHARGEBACK
```

### Estados do pedido

```
CART
AWAITING_PAYMENT
PAID
PROCESSING
DELIVERED
CANCELLED
```

O QR Code e o código Pix devem ser individuais para cada pedido, com identificador próprio. Pix estático cria uma reconciliação digna de um episódio distópico: dinheiro entrando e ninguém sabendo de qual usuário veio.

## 5\. Entrega de conteúdo

Para produto avulso:

```
Pagamento confirmado
       ↓
Criação do entitlement
       ↓
Envio das mídias pelo bot
       ↓
Produto aparece em “Minhas compras”
```

Para comunidade VIP:

```
Pagamento confirmado
       ↓
Assinatura ativada
       ↓
Bot gera convite temporário
       ↓
Usuário entra no canal privado
       ↓
Sistema acompanha vencimento
```

Tabela de permissões:

```
entitlements
├── id
├── tenant_id
├── telegram_user_id
├── product_id
├── subscription_id
├── status
├── granted_at
├── expires_at
└── revoked_at
```

“Minhas compras” deve consultar essa tabela e permitir reenvio apenas do que o usuário realmente adquiriu.

## 6\. Campanhas automáticas

Os prints da Ruiva Isabel mostram mensagens enviadas em horários diferentes, mesmo sem uma ação imediata do usuário. Isso indica campanhas programadas.

Arquitetura:

```
Scheduler
   ↓
Segmentação de usuários
   ↓
Fila de envio
   ↓
Telegram Bot API
   ↓
Registro de entrega e clique
```

Segmentos possíveis:

```
Usuários que iniciaram e não compraram
Checkout criado e não pago
Compradores de produto avulso
Assinantes ativos
Assinantes vencidos
Usuários inativos há 3, 7 ou 14 dias
```

Isso pode ser feito com Redis/BullMQ, Celery ou n8n. Para quase 100 mil usuários mensais, não é recomendável executar tudo somente em workflows n8n sequenciais.

## 7\. Forte evidência de sistema multi-tenant

Os dois bots compartilham:

- estrutura de menu;
- catálogo avulso;
- botão “Ver próximo”;
- “Minhas compras”;
- checkout Pix;
- botão de confirmação;
- venda VIP;
- campanhas;
- mesma organização visual.

Logo, a arquitetura mais provável é:

```
Painel administrativo
                            ↓
┌──────────────────────────────────────────────────┐
│               Backend multi-tenant               │
│                                                  │
│ Tenant A → Bot Manas Nunes                       │
│ Tenant B → Bot Ruiva Isabel                      │
│ Tenant C → Outro creator                        │
└──────────────────────────────────────────────────┘
             ↓             ↓             ↓
          Telegram      Pagamentos     Banco
```

Cada conta possui configurações próprias:

```
tenant
├── nome
├── bot_token
├── identidade
├── suporte
├── canal VIP
├── gateway
├── produtos
├── preços
├── mensagens
└── campanhas
```

Um único backend pode atender dezenas ou centenas de bots:

```
POST /telegram/webhook/{tenant_id}
POST /payments/webhook/{gateway}/{tenant_id}
```

## 8\. Banco de dados recomendado

```
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
telegram_channels
campaigns
campaign_deliveries
support_requests
event_logs
```

Eventos que devem ser registrados:

```
bot_started
menu_opened
vip_clicked
store_opened
product_viewed
product_next_clicked
checkout_created
pix_copied
payment_check_clicked
payment_confirmed
content_delivered
channel_joined
subscription_expired
```

## 9\. Stack adequada para replicação

```
Telegram Bot API
        ↓
Node.js + NestJS
ou Python + FastAPI
        ↓
PostgreSQL / Supabase
        ↓
Redis
        ↓
BullMQ ou Celery
        ↓
Gateway Pix/cartão
        ↓
S3/R2 + Telegram file_id
        ↓
Painel administrativo
```

### Papel do n8n

Use n8n para:

- campanhas;
- recuperação de checkout;
- alertas internos;
- relatórios;
- sincronização com CRM;
- atendimento;
- notificações administrativas.

Não usaria n8n como único núcleo do bot. Com muitos usuários, catálogo, carrinho, pagamentos e callbacks, o backend tradicional deve ser o cérebro; o n8n funciona como sistema nervoso periférico.

## 10\. Proteções necessárias

- não confiar no botão “Paguei”;
- usar webhook assinado pelo gateway;
- criar Pix dinâmico;
- impedir entrega duplicada;
- usar idempotência nos webhooks;
- limitar convites do canal;
- expirar links de acesso;
- remover assinantes vencidos;
- registrar auditoria;
- armazenar segredos em variáveis de ambiente;
- não expor token do bot;
- proteger conteúdo encaminhado quando aplicável;
- manter backup externo das mídias;
- aplicar marcação individual nos arquivos quando necessário.

Os QR Codes e códigos Pix aparecem completos nos prints. Nos próximos, o ideal é ocultá-los, junto com identificadores de transação e dados do recebedor.

## Conclusão técnica

O sistema observado é composto por cinco motores:

```
1. Funil de entrada
2. Catálogo de produtos
3. Carrinho e order bump
4. Pagamentos e permissões
5. Campanhas de recuperação
```

A melhor réplica não seria um bot isolado, mas uma **plataforma white-label de bots de conteúdo premium**, configurável por cliente. A mesma base poderia atender comunidades, cursos, mentorias, newsletters, clubes e bibliotecas digitais, alterando apenas identidade, catálogo e regras de acesso.

Posso continuar o mapeamento funcional com prints sanitizados das etapas posteriores à confirmação de pagamento, sem incluir as mídias sensíveis.

---

**Você disse**

Sim. Elabore & Valide.

---

## Veredito

A arquitetura é **replicável como plataforma white-label de conteúdo premium**, com catálogo, carrinho, order bump, pagamento, entrega digital, comunidade privada e campanhas automáticas.

A validação encontrou um ponto crítico: **não devemos copiar o fluxo de Pix exatamente como aparece nos prints**. Atualmente, o Telegram exige que bens e serviços digitais vendidos dentro de bots ou Mini Apps sejam pagos exclusivamente com **Telegram Stars (`XTR`)**, mesmo que o operador tenha checkout externo ou outros gateways. Portanto, a réplica correta deve preservar a experiência comercial, mas substituir o trilho de pagamento interno por Stars. [^1]

A análise abaixo cobre o motor técnico e comercial para conteúdo premium lícito e não explícito.

---

## 1\. O que os prints validam

| Componente | Evidência observada | Confiança |
| --- | --- | --- |
| Onboarding por `/start` | Mídia, texto e menu inicial | Alta |
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

## Conclusão da engenharia reversa

O produto não parece ser um workflow isolado. Ele se comporta como um **SaaS multi-tenant para creators**, onde cada cliente possui:

```
Bot próprio
Marca própria
Produtos próprios
Preços próprios
Canal ou comunidade própria
Campanhas próprias
Gateway/configuração financeira própria
```

O motor central permanece igual.

---

## 2\. Arquitetura recomendada

```
PAINEL ADMINISTRATIVO
                                  │
                                  ▼
┌──────────────────────────────────────────────────────────┐
│                    BACKEND MULTI-TENANT                   │
│                                                          │
│  Tenant A        Tenant B        Tenant C                 │
│  Bot A           Bot B           Bot C                    │
│  Produtos A      Produtos B      Produtos C               │
└──────────────────────────────────────────────────────────┘
          │                 │                 │
          ▼                 ▼                 ▼
 Telegram Bot API      PostgreSQL          Redis
          │                 │                 │
          └────────────── Event Bus ──────────┘
                                  │
                 ┌────────────────┼────────────────┐
                 ▼                ▼                ▼
             Pagamentos       Entregas        Campanhas
              Stars          e acessos       e remarketing
```

## Stack principal

```
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

### Por que não usar somente n8n

O n8n é adequado para:

- campanhas;
- notificações;
- recuperação de usuários;
- relatórios;
- CRM;
- suporte;
- sincronizações;
- alertas administrativos.

O núcleo transacional deve ficar no backend:

- callbacks;
- catálogo;
- carrinho;
- pagamentos;
- idempotência;
- permissões;
- entrega;
- controle de assinatura.

Transformar tudo em n8n funcionaria inicialmente, mas o projeto acabaria parecendo uma estação espacial montada com extensões elétricas.

---

## 3\. Separação por módulos

## 3.1 Bot Gateway

Responsável por receber os eventos do Telegram:

```
/start
/callback_query
/pre_checkout_query
/successful_payment
/chat_join_request
/chat_member
/message
```

Rota:

```
POST /webhooks/telegram/:tenantKey
```

O webhook deve usar `secret_token`; o Telegram envia esse valor no cabeçalho `X-Telegram-Bot-Api-Secret-Token`, permitindo validar que a chamada veio da configuração esperada. [^2]

Fluxo:

```
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

## 3.2 Motor de navegação

Responsável por:

- menu inicial;
- catálogo;
- paginação;
- carrinho;
- pedidos;
- compras anteriores;
- suporte;
- estados da conversa.

Callbacks recomendados:

```
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

Não coloque preço ou nome do produto dentro do callback. O callback deve carregar apenas um identificador. O backend consulta o valor oficial no banco.

Errado:

```
buy:produto_01:50.00
```

Correto:

```
cart:add:prd_8F3K2
```

---

## 4\. Máquina de estados

## Estado do usuário

```
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

```
MEMBERSHIP_ACTIVE
MEMBERSHIP_PAST_DUE
MEMBERSHIP_EXPIRED
BLOCKED
SUPPORT_REQUIRED
```

## Estado do pedido

```
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

```
AWAITING_PAYMENT → EXPIRED
PAID → REFUNDED
PAID → DISPUTED
FULFILLING → DELIVERY_FAILED
```

## Estado da assinatura

```
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
- direito de acesso.

Isso evita o clássico bug: “o pagamento foi aprovado, mas o usuário não recebeu” ou “foi reembolsado e permaneceu no canal”.

---

## 5\. Modelo de dados

## Entidades centrais

```
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

## tenants

```sql
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

## telegram\_bots

```sql
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

## users

```sql
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

IDs de usuários do Telegram devem ser armazenados como `BIGINT`; a documentação alerta que eles podem ter até 52 bits significativos. [^3]

## products

```sql
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

```
DIGITAL_ITEM
BUNDLE
MEMBERSHIP
COURSE
DOWNLOAD
COMMUNITY_ACCESS
```

## product\_assets

```sql
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

O `telegram_file_id` permite reutilizar arquivos já enviados sem realizar upload repetido.

## carts

```sql
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

## orders

```sql
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

## payments

```sql
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

## entitlements

Representa o direito de consumir algo:

```sql
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

## subscriptions

```sql
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

## webhook\_events

```sql
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

```sql
UNIQUE(source, external_event_id)
```

Isso fornece idempotência.

---

## 6\. Fluxo inicial

```
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

```
https://t.me/NomeDoBot?start=ig_reel_023
```

Registro:

```json
{
  "source": "instagram",
  "campaign": "reel_023",
  "creator": "tenant_a"
}
```

Isso permite calcular:

```
Cliques
Inícios
Visualizações de produto
Checkouts
Pagamentos
Receita por campanha
Conversão por origem
```

---

## 7\. Catálogo

## Tela principal

```
Biblioteca Premium

27 itens disponíveis.

[ Ver catálogo ]
[ Minhas compras ]
[ Voltar ao menu ]
```

## Produto

```
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

## Paginação

Não é necessário gravar apenas uma posição global na sessão. Use:

```
product.position
```

Ao clicar em próximo:

```sql
SELECT *
FROM products
WHERE tenant_id = :tenant
  AND status = 'ACTIVE'
  AND position > :current_position
ORDER BY position
LIMIT 1;
```

Caso não exista próximo item:

```
Retornar ao primeiro
ou
Mostrar “fim do catálogo”
```

---

## 8\. Carrinho e order bump

## Fluxo

```
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

## Regras

O carrinho deve calcular valores exclusivamente no servidor:

```typescript
total = items.reduce(
  (sum, item) => sum + item.unitPrice * item.quantity,
  0
);
```

Nunca aceite preço vindo do Telegram.

## Order bump configurável

```json
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

## 9\. Pagamento validado para 2026

## Problema do fluxo observado

Os prints mostram:

```
Produto digital
→ checkout dentro do bot
→ Pix/cartão externo
→ entrega digital
```

Pelas regras atuais da plataforma, esse fluxo não deve ser reproduzido para vendas digitais realizadas dentro do Telegram. O pagamento deve usar Telegram Stars. [^1]

## Fluxo correto

```
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

Para produtos digitais, o Telegram determina o uso de `XTR`, e o fluxo oficial exige armazenar o `telegram_payment_charge_id`, inclusive para possíveis reembolsos. [^1]

## Pseudocódigo

```typescript
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

## Assinaturas

O Telegram também suporta assinaturas pagas com Stars. [^3]

Para o MVP, existem duas estratégias:

### Estratégia A — Compra avulsa

Mais simples:

```
Pagamento único
→ acesso permanente ao produto
```

### Estratégia B — Assinatura

```
Pagamento recorrente
→ acesso durante o período ativo
→ revogação ao expirar
```

---

## 10\. Entrega digital

## Estratégia 1 — Entrega pelo bot

```
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

O Bot API oferece `protect_content`, que restringe encaminhamento e salvamento de mensagens protegidas. Isso reduz compartilhamentos casuais, embora não elimine capturas de tela ou gravação externa. [^3]

## Estratégia 2 — Biblioteca interna

O usuário acessa:

```
Minhas compras
   ↓
Produto adquirido
   ↓
Reabrir conteúdo
```

Antes de entregar:

```sql
SELECT *
FROM entitlements
WHERE tenant_id = :tenant
  AND user_id = :user
  AND product_id = :product
  AND status = 'ACTIVE';
```

## Estratégia 3 — Mini App

Uma Mini App fornece:

- catálogo visual;
- biblioteca;
- filtros;
- busca;
- carrinho;
- histórico;
- perfil;
- assinatura.

O Telegram permite que Mini Apps funcionem como interfaces completas dentro do aplicativo. [^4]

### Recomendação

```
MVP:
Bot com botões inline

Versão 2:
Bot + Mini App para catálogo e painel do cliente
```

---

## 11\. Acesso a comunidade privada

## Fluxo seguro

```
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

## Link recomendado

```
Uso único
Expiração de 15 minutos
Associado ao usuário
Identificado pelo pedido
```

Tabela:

```sql
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

## Expiração

Job periódico:

```
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

## 12\. Campanhas e recuperação

## Segmentos

```
Iniciou e não abriu catálogo
Abriu catálogo e não visualizou produto
Visualizou e não adicionou ao carrinho
Criou checkout e não pagou
Comprou item avulso
Assinatura próxima do vencimento
Assinatura expirada
Usuário inativo
```

## Eventos

```
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

## Automação no n8n

```
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

```
Antes de enviar recuperação:
verificar novamente se o usuário comprou.
```

Sem essa checagem, o comprador recebe “você esqueceu de pagar” depois de já ter pago. Excelente para transformar fidelização em filme de terror corporativo.

## Limites de comunicação

Manter:

```
frequency_cap
quiet_hours
opt_out
blocked_at
last_campaign_at
```

Exemplo:

```
No máximo 1 campanha comercial por 24 horas
Não enviar entre 22h e 8h
Parar após /stop
```

---

## 13\. Painel administrativo

## Dashboard

```
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

## Gestão de produtos

```
Criar produto
Editar produto
Cadastrar mídia
Definir preço em Stars
Ordenar catálogo
Criar bundle
Criar order bump
Ativar ou desativar
```

## Gestão de usuários

```
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

## Campanhas

```
Selecionar segmento
Criar mensagem
Adicionar mídia
Agendar
Testar
Disparar
Pausar
Ver métricas
```

## Multi-tenant

Um administrador da Marca A nunca pode acessar dados da Marca B.

Todas as queries precisam incluir:

```sql
WHERE tenant_id = :authenticatedTenant
```

Não basta confiar no frontend. O isolamento deve existir no backend e, idealmente, com Row Level Security no banco.

---

## 14\. Segurança

## Obrigatório

```
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

## Idempotência de pagamento

```
successful_payment recebido duas vezes
        ↓
consultar telegram_payment_charge_id
        ↓
se já existe:
não cobrar
não entregar novamente
não gerar nova assinatura
```

## Idempotência da entrega

```sql
UNIQUE(order_id, product_id, user_id)
```

## Auditoria

Registrar:

```
Quem concedeu acesso
Quem revogou
Qual pagamento originou o acesso
Quando o conteúdo foi entregue
Qual campanha foi enviada
Quem alterou preço
Quem alterou gateway/configuração
```

## Segredos

```
BOT_TOKEN
DATABASE_URL
REDIS_URL
ENCRYPTION_KEY
WEBHOOK_SECRET
STORAGE_SECRET
```

Nunca armazenar isso em workflows exportados, repositórios públicos ou campos comuns do banco.

---

## 15\. Suporte, termos e reembolsos

O fluxo oficial para vendas digitais exige suporte claro, termos acessíveis e tratamento de problemas de pagamento. A documentação recomenda `/terms`, `/support` e exige capacidade de atender `/paysupport`; reembolsos em Stars podem ser processados pelo método `refundStarPayment`. [^1]

Comandos:

```
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

```
[ ] Confirmo que li os termos
```

O registro deve salvar:

```
terms_version
accepted_at
telegram_user_id
```

---

## 16\. Observabilidade

## Métricas

```
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

## Alertas

```
Webhook sem eventos
Fila acumulada
Falha de banco
Redis indisponível
Pagamento confirmado sem entrega
Entrega duplicada
Muitas falhas do Telegram
Campanha com bloqueios anormais
```

## Regra operacional crítica

Criar um reconciliador:

```
A cada 15 minutos:
buscar pedidos PAID sem entitlement
buscar pedidos PAID sem entrega
buscar assinaturas ACTIVE vencidas
buscar entregas FAILED
corrigir ou alertar
```

Esse processo é a rede de segurança. Webhooks eventualmente falham; a arquitetura não pode depender de perfeição mitológica.

---

## 17\. Testes de validação

## Onboarding

- `/start` cria apenas um usuário;
- repetir `/start` não duplica dados;
- origem da campanha é registrada;
- menu é exibido corretamente.

## Catálogo

- próximo e anterior funcionam;
- produto desativado não aparece;
- usuário não altera preço pelo callback;
- fim do catálogo é tratado.

## Carrinho

- item duplicado não duplica indevidamente;
- order bump pode ser recusado;
- total é recalculado pelo servidor;
- carrinho expirado não gera pedido inválido.

## Pagamento

- pedido correto é associado à invoice;
- pagamento repetido é ignorado;
- valor divergente bloqueia entrega;
- `successful_payment` cria entitlement;
- reembolso revoga acesso quando aplicável.

## Entrega

- apenas compradores recebem;
- reenvio respeita limite;
- falha gera retry;
- entrega repetida não cria múltiplos direitos.

## Comunidade

- link expira;
- link não pode ser reutilizado;
- assinatura vencida não entra;
- assinatura ativa é aprovada;
- cancelamento revoga acesso.

## Multi-tenant

- usuário da Marca A não acessa produto B;
- callback manipulado não cruza tenant;
- administrador A não vê receita B;
- arquivos não vazam entre clientes.

## Campanhas

- comprador não recebe abandono;
- usuário bloqueado não recebe;
- frequência máxima é aplicada;
- opt-out é respeitado.

---

## 18\. Roadmap de implementação

## Fase 1 — Fundação

```
Multi-tenant
Cadastro de bots
Webhook
Usuários
Menu
Logs
```

## Fase 2 — Comércio

```
Produtos
Catálogo
Carrinho
Order bump
Pedidos
Telegram Stars
```

## Fase 3 — Entrega

```
Entitlements
Minhas compras
Envio de ativos
Proteção
Retry
```

## Fase 4 — Comunidade

```
Planos
Assinaturas
Links temporários
Join requests
Revogação
```

## Fase 5 — Automação

```
Eventos
Redis/BullMQ
n8n
Campanhas
Recuperação
Relatórios
```

## Fase 6 — SaaS

```
Painel administrativo
Onboarding de tenants
RBAC
Cobrança da plataforma
Analytics
White-label
```

---

## 19\. Estrutura de repositório

```
ginkgo-creator-commerce/
├── apps/
│   ├── api/
│   ├── bot-worker/
│   ├── campaign-worker/
│   ├── delivery-worker/
│   ├── admin-dashboard/
│   └── mini-app/
│
├── packages/
│   ├── database/
│   ├── telegram/
│   ├── payments/
│   ├── events/
│   ├── queue/
│   ├── security/
│   └── shared/
│
├── infrastructure/
│   ├── docker/
│   ├── traefik/
│   ├── migrations/
│   └── monitoring/
│
├── n8n/
│   ├── campaigns/
│   ├── alerts/
│   ├── reports/
│   └── crm/
│
└── docs/
    ├── architecture.md
    ├── database.md
    ├── events.md
    ├── security.md
    └── deployment.md
```

---

## 20\. Validação final

## Funcionalmente validado

A réplica consegue reproduzir:

```
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

## Não validado pelos prints

Ainda não é possível afirmar:

```
Qual linguagem foi usada
Qual gateway original
Qual banco original
Se o acesso VIP é realmente automático
Como funciona o reembolso
Como ocorre o cancelamento
Como é feito o painel administrativo
Se existe proteção contra fraude
```

## Alteração obrigatória

```
Arquitetura observada:
Pix/cartão para produto digital dentro do bot

Arquitetura recomendada:
Telegram Stars para produto digital dentro do bot
```

## Classificação técnica

```
Modelo de negócio: validado
Arquitetura white-label: fortemente validada
Catálogo e checkout: validados
Campanhas automáticas: validadas
Infraestrutura interna original: não identificada
Replicação técnica: viável
Replicação literal do pagamento por Pix: não recomendada
```

Os QR Codes e códigos Pix enviados nos prints devem ser tratados como informações expostas. Não reutilize essas capturas publicamente e, nos próximos registros, cubra QR Code, código copia e cola, identificadores e dados do recebedor.

---

**Você disse**

podemos validar nós mesmo? utilizando a melhor opção para cada com o resultado final sendo este? somar a uma dashboard de configuração e criação entre aspas em massa, exemplo 30 bots, tornar replicavel, copia e cola.

---

## Veredito

**Sim. É viável construir uma plataforma própria com o resultado visual e funcional semelhante ao painel da imagem, preparada para operar 30, 100 ou mais bots a partir de templates.**

A mudança decisiva é que o Telegram agora oferece oficialmente o conceito de **Management Bot**. Um bot principal pode ser habilitado no BotFather para permitir que usuários criem bots gerenciados por ele. Após a confirmação da criação, o bot gerenciador recebe um evento `managed_bot`, consegue obter o token com `getManagedBotToken` e também pode rotacioná-lo posteriormente. Isso elimina boa parte do trabalho artesanal que antes exigia copiar tokens manualmente. [^5]

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

Esse mecanismo é documentado oficialmente pelo Telegram. [^5]

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

Para bens digitais, assinaturas e acesso a conteúdo dentro do Telegram, o método nativo deve ser **Telegram Stars**, usando moeda `XTR`. O fluxo oficial utiliza `sendInvoice`, `pre_checkout_query`, `answerPreCheckoutQuery` e `successful_payment`. O identificador `telegram_payment_charge_id` deve ser armazenado para reconciliação e possíveis reembolsos. [^6]

O dashboard pode suportar:

| Gateway | Uso |
| --- | --- |
| Telegram Stars | Produtos digitais dentro do Telegram |
| Pix | Produtos físicos ou operações externas compatíveis |
| Stripe | SaaS, serviços externos e cobrança da plataforma |
| Mercado Pago | Operações externas compatíveis |
| Pagar.me | Operações externas compatíveis |

Para produto digital vendido e entregue dentro do bot ou Mini App, o Telegram exige Stars mesmo que existam outros portais ou gateways externos. [^6]

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

Mini Apps podem ser abertas por botões inline, pelo menu do bot ou diretamente pelo perfil. O servidor deve validar `initData`; o objeto `initDataUnsafe` não deve ser tratado como fonte confiável. [^7]

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

A principal descoberta é que a criação escalável deixou de ser apenas uma gambiarra em torno do BotFather: o Telegram agora possui infraestrutura oficial para **managed bots**, o que encaixa diretamente no modelo de uma fábrica white-label. [^5]

O próximo artefato técnico deve ser o **Epic 0 + Epic 1**, com schema do banco, estrutura do monorepo, Docker Compose e fluxo completo de criação/conexão dos primeiros três bots.

[^1]: [core.telegram.org](https://core.telegram.org/bots/payments-stars?utm_source=chatgpt.com)

[^2]: [core.telegram.org](https://core.telegram.org/bots/api)

[^3]: [core.telegram.org](https://core.telegram.org/bots/api-changelog)

[^4]: [core.telegram.org](https://core.telegram.org/bots?utm_source=chatgpt.com)

[^5]: [core.telegram.org](https://core.telegram.org/bots/features)

[^6]: [core.telegram.org](https://core.telegram.org/bots/payments-stars)

[^7]: [core.telegram.org](https://core.telegram.org/bots/webapps)