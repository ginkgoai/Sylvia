---
title: "Análise e replicação bot"
source: "https://chatgpt.com/c/6a5b85f7-d5a8-83e9-babd-4c2e8ffc3f64"
author:
published:
created: 2026-07-18
description: "ChatGPT conversation with 5 messages"
tags:
  - "clippings"
---
O link público confirma o bot **@ruivaisabelvipbot**, apresentado como “Ruiva Isabel exclusivo”, com cerca de **97.485 usuários mensais** no momento da consulta. A página externa do Telegram não revela menus, preços, pagamentos ou automações internas; esses elementos só aparecem após iniciar o bot. [^1]

Não posso ajudar a acessar ou replicar conteúdo sexual explícito. Posso, porém, analisar e reconstruir com segurança a **arquitetura de assinatura, cobrança e controle de acesso** usada nesse tipo de bot, aplicável a cursos, comunidades, creators, newsletters ou conteúdo premium.

## Arquitetura provável

```
Anúncio / rede social / link
            ↓
Deep link do Telegram
t.me/bot?start=origem_campanha
            ↓
Bot de onboarding
            ↓
Apresentação da oferta
            ↓
Escolha do plano
            ↓
Checkout externo ou pagamento integrado
            ↓
Webhook de pagamento
            ↓
Banco de assinaturas
            ↓
Convite temporário para canal privado
            ↓
Verificação periódica da assinatura
            ↓
Renovação, recuperação ou remoção
```

## Componentes

### 1\. Bot comercial

Responsável por:

- `/start`;
- apresentação da proposta;
- botões de planos;
- FAQ;
- suporte;
- checkout;
- recuperação de carrinho;
- consulta da assinatura;
- acesso ao canal.

### 2\. Canal privado

O conteúdo premium geralmente não fica diretamente no bot. O bot funciona como porteiro digital e libera acesso a:

- canal privado;
- grupo de comunidade;
- biblioteca de arquivos;
- área externa;
- conteúdo programado.

### 3\. Controle de acesso

O sistema deve registrar:

```
telegram_user_id
username
nome
plano
status da assinatura
data de início
data de vencimento
gateway_customer_id
gateway_subscription_id
origem do lead
última interação
canal liberado
```

Estados recomendados:

```
LEAD
→ CHECKOUT_INICIADO
→ PAGAMENTO_PENDENTE
→ ATIVO
→ VENCENDO
→ INADIMPLENTE
→ CANCELADO
→ REMOVIDO
```

## Stack indicada para a Ginkgo

```
Telegram Bot API
        ↓
FastAPI ou Node.js
        ↓
n8n para automações
        ↓
PostgreSQL / Supabase
        ↓
Redis para sessões e filas
        ↓
Gateway de pagamento
        ↓
Canal privado do Telegram
        ↓
Dashboard administrativo
```

### Divisão correta

**Código do bot**

- comandos;
- callbacks;
- segurança;
- geração de links;
- validação de usuários;
- permissões.

**n8n**

- webhooks de pagamento;
- mensagens de cobrança;
- recuperação de checkout;
- lembretes;
- relatórios;
- campanhas;
- sincronização com CRM.

**Supabase/PostgreSQL**

- usuários;
- planos;
- pagamentos;
- eventos;
- acessos;
- campanhas;
- auditoria.

## Fluxos essenciais

### Compra

```
Usuário clica em “Assinar”
→ bot cria checkout individual
→ pagamento é aprovado
→ gateway envia webhook
→ assinatura fica ATIVA
→ bot gera convite de uso único
→ usuário entra no canal
→ evento é registrado
```

### Renovação

```
Gateway confirma renovação
→ vencimento é atualizado
→ acesso permanece ativo
→ recibo ou confirmação é enviado
```

### Inadimplência

```
Pagamento falha
→ status vira INADIMPLENTE
→ mensagens em D+0, D+1 e D+3
→ novo link de pagamento
→ período de tolerância
→ remoção automática do canal
```

### Proteção do canal

- convite com expiração;
- limite de um uso;
- aprovação automática de entrada;
- proibição de links permanentes;
- auditoria de entrada e saída;
- remoção de assinaturas vencidas;
- bloqueio contra reentrada;
- associação entre Telegram ID e compra.

## Estrutura replicável por configuração

```
/config
  brand.json
  plans.json
  messages.json
  menus.json
  campaigns.json

/content
  onboarding/
  previews/
  faq/
  notifications/

/workflows
  payment-approved.json
  payment-failed.json
  subscription-expired.json
  abandoned-checkout.json
  channel-access.json
```

Exemplo:

```json
{
  "brand": {
    "name": "Projeto Premium",
    "support_username": "@suporte"
  },
  "plans": [
    {
      "id": "monthly",
      "name": "Plano Mensal",
      "price_cents": 2990,
      "duration_days": 30
    }
  ]
}
```

Assim, o motor permanece igual e cada projeto troca apenas marca, oferta, mensagens, planos e conteúdo. É uma fábrica de bots, não um bot artesanal mantido com fita isolante.

## O que ainda falta para uma engenharia reversa exata

A página pública não mostra a experiência interna. Para mapear a interface sem analisar conteúdo explícito, servem:

- capturas somente dos menus e botões;
- mensagens de onboarding sem mídia explícita;
- nomes e valores dos planos;
- tela de checkout;
- fluxo após pagamento;
- opções de suporte;
- mensagens de renovação ou cancelamento.

Com isso, é possível produzir o diagrama completo, schema SQL, workflows n8n e prompt de implementação para Codex/Cursor, mantendo apenas a mecânica de assinatura e usando conteúdo apropriado.

---

**Você disse**

Pode ser Eu lhe enviando print a print cada comando?

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

[^1]: [t.me](https://t.me/ruivaisabelvipbot)