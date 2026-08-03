---
title: "Análise e replicação bot"
source: "https://chatgpt.com/c/6a5b85f7-d5a8-83e9-babd-4c2e8ffc3f64"
author:
published:
created: 2026-07-20
description: "ChatGPT conversation with 5 messages"
tags:
  - "clippings"
---
Sim. Envie **print a print**, seguindo cada botão e comando do bot.

Para eu mapear corretamente, capture:

1. Tela inicial após `/start`
2. Cada menu e submenu
3. Botões exibidos em cada etapa
4. Mensagens automáticas
5. Tela de seleção de plano
6. Checkout e formas de pagamento
7. Mensagem após pagamento ou acesso liberado
8. Fluxo de suporte, renovação e cancelamento
9. Mensagens de erro ou tentativa de acesso sem assinatura

Envie os prints em ordem e, junto de cada um, escreva algo como:

```
Etapa 01
Comando: /start
Botão clicado: Assinar agora
Resultado: abriu seleção de planos
```

Pode ocultar:

- conteúdo explícito;
- nomes pessoais;
- telefone;
- e-mail;
- QR Code;
- CPF;
- IDs de pagamento;
- links privados de acesso.

Com os prints, vou construir progressivamente:

```
Mapa UX
→ árvore de comandos
→ callbacks dos botões
→ estados do usuário
→ lógica de pagamento
→ controle do canal
→ banco de dados
→ workflows n8n
→ arquitetura replicável
```

Envie primeiro o print da tela imediatamente após o `/start`.

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

[^1]: [core.telegram.org](https://core.telegram.org/bots/payments-stars?utm_source=chatgpt.com)

[^2]: [core.telegram.org](https://core.telegram.org/bots/api)

[^3]: [core.telegram.org](https://core.telegram.org/bots/api-changelog)

[^4]: [core.telegram.org](https://core.telegram.org/bots?utm_source=chatgpt.com)