---
title: "Diretrizes Meta Propaganda"
source: "https://chatgpt.com/c/6a67a006-a47c-83e9-b150-75fd28f8900a"
author:
published:
created: 2026-07-27
description: "ChatGPT conversation with 2 messages"
tags:
  - "clippings"
---
**Você disse**

Como isso é feito nas diretrizes da meta?

---

A propaganda mistura duas coisas diferentes: **capacidade técnica** e **permissão para enviar**.

A API oficial realmente suporta volumes enormes. Mas ela não transforma uma lista fria em uma lista autorizada. A Meta fornece a rodovia; o opt-in continua sendo o pedágio.

## Como uma operação oficial funciona

### 1\. Cada cliente conecta a própria conta Meta

O modelo correto para revendedores é:

```
Cliente
  ↓
Meta Business Portfolio
  ↓
WhatsApp Business Account — WABA
  ↓
Número comercial
  ↓
Embedded Signup
  ↓
Plataforma do revendedor
```

O cliente autoriza o acesso pelo **Embedded Signup**, interface oficial que pode ser incorporada ao painel do fornecedor. É assim que Tech Providers e Solution Partners integram contas de clientes em escala, sem pedir senha ou capturar QR Code. [^1]

A estrutura provavelmente usada pela empresa da imagem é algo próximo disto:

```
Painel Infinity Send
├── Cliente A → WABA A → números A1, A2...
├── Cliente B → WABA B → números B1, B2...
├── Templates aprovados
├── Listas segmentadas
├── Scheduler e filas
├── Cloud API / Marketing Messages API
└── Webhooks de entrega, leitura e falha
```

Os “15 milhões por dia” provavelmente representam **capacidade agregada entre contas, números e clientes**, não necessariamente um único número.

## 2\. Só pode receber campanha quem deu consentimento

Para iniciar mensagens, a pessoa precisa:

- ter fornecido o número;
- ter autorizado receber mensagens daquela empresa;
- saber aproximadamente que tipo de conteúdo receberá;
- conseguir cancelar facilmente.

A Meta recomenda consentimento separado por categoria, como ofertas, atualizações de pedidos e recomendações. Solicitações de cancelamento, bloqueio ou interrupção devem ser respeitadas imediatamente. [^2]

Um registro aceitável de opt-in deveria armazenar:

```json
{
  "phone": "5511999999999",
  "business_id": "cliente_123",
  "consent_category": "marketing_promotions",
  "source": "landing_page",
  "consent_text_version": "v3",
  "timestamp": "2026-07-27T14:30:00-03:00",
  "ip_or_event_id": "evidence_abc123",
  "status": "active"
}
```

Comprar uma base, importar números coletados de grupos ou disparar para pessoas que nunca aceitaram contato continua sendo spam, mesmo que o envio saia pela API oficial.

## 3\. Campanhas iniciadas pela empresa usam templates

Fora da janela de atendimento, a empresa só pode iniciar uma conversa usando um **template previamente aprovado** pela Meta.

Exemplo:

```
Olá, {{1}}.

Você autorizou receber ofertas da {{2}}.
Hoje temos {{3}}.

Ver oferta: {{4}}

Para não receber mais mensagens, responda SAIR.
```

Depois que o usuário responde, abre-se uma janela de atendimento de 24 horas. Dentro dela, a empresa pode responder com mensagens livres, automações ou agentes de IA. Fora dela, volta a ser necessário usar templates aprovados. [^2]

Para campanhas, a Meta também oferece a **Marketing Messages API**, destinada exclusivamente a templates de marketing e otimizada para decidir quais mensagens têm maior probabilidade de serem relevantes e entregues. [^3]

## 4\. Como chegam tecnicamente a 15 milhões por dia

A Cloud API suporta, por número comercial:

- até **80 mensagens por segundo**, por padrão;
- até **1.000 mensagens por segundo**, após upgrade automático de throughput. [^4]

Quinze milhões de mensagens em 24 horas equivalem a aproximadamente:

```
15.000.000 ÷ 86.400 = 174 mensagens por segundo
```

Um número no limite padrão teria capacidade teórica de:

```
80 × 86.400 = 6.912.000 mensagens/dia
```

Portanto, tecnicamente, três números com throughput padrão já ultrapassariam 15 milhões por dia. Um número com high throughput também teria capacidade bruta suficiente.

Mas **throughput não é autorização de audiência**. Existem ainda os limites de destinatários únicos. A documentação atual apresenta uma progressão do portfólio empresarial:

```
250 destinatários únicos
→ 2.000
→ 10.000
→ 100.000
→ ilimitado
```

Os aumentos dependem de caminhos de escalabilidade, uso legítimo, qualidade e crescimento automático. O cálculo considera destinatários únicos dentro de uma janela móvel de 24 horas, não simplesmente o total bruto de mensagens enviadas. [^5]

Além disso, a Meta mantém limites de marketing por usuário. Uma campanha pode estar autorizada e ainda assim não ser entregue quando o destinatário já recebeu excesso de mensagens comerciais ou demonstra baixa probabilidade de engajamento. [^6]

## 5\. O que acontece quando a qualidade cai

A Meta observa sinais como:

- bloqueios;
- denúncias;
- cancelamentos;
- baixa interação;
- feedback negativo;
- templates sinalizados;
- envio não esperado pelo usuário.

As consequências podem incluir pausa de templates, redução de limites, bloqueios de envio por períodos determinados ou suspensão definitiva da conta. [^7]

Por isso, uma operação profissional usa:

```
Fila de envio
  ↓
Limitação por segundo
  ↓
Segmentação por interesse
  ↓
Controle de frequência
  ↓
Webhook de entrega
  ↓
Bloqueio e opt-out
  ↓
Atualização da suppression list
  ↓
Monitoramento da qualidade
```

## O problema na afirmação “qualquer nicho”

Tomada literalmente, essa promessa não está de acordo com as regras.

A política restringe ou proíbe determinados setores e usos, incluindo algumas categorias financeiras, produtos regulados, serviços de encontros, marketing multinível, produtos e serviços adultos, atividades ilegais e outras verticais consideradas de alto risco. Algumas exceções dependem de país, idade, licenciamento e aprovação específica. [^2]

Portanto:

| Afirmação | Realidade |
| --- | --- |
| “API oficial” | Pode ser verdadeira |
| “15 milhões por dia” | Tecnicamente possível |
| “Qualquer volume” | Depende dos limites e da qualidade |
| “Qualquer nicho” | Incorreto literalmente |
| “Lista fria” | Não permitida |
| “Revenda” | Permitida com estrutura correta |
| “Entrega garantida” | Não existe |

## Modelo seguro para o Leaf

A oferta não deveria ser “disparo em massa”. O posicionamento mais sustentável seria:

> **Infraestrutura oficial de campanhas conversacionais no WhatsApp para bases consentidas.**

Arquitetura recomendada:

```
Leaf Campaigns
├── Embedded Signup oficial
├── WABA separado por cliente
├── Cofre de tokens
├── Ledger de consentimento
├── Importador com validação de opt-in
├── Gerenciador de templates
├── Segmentação de audiência
├── Scheduler e BullMQ
├── Rate limiter por número
├── Cloud API
├── Marketing Messages API
├── Webhooks de status
├── Suppression list global
├── Monitor de qualidade
├── Handoff para Chatwoot
└── Auditoria e cobrança por mensagem entregue
```

A Meta cobra quando o template é efetivamente entregue; o revendedor pode adicionar mensalidade, margem operacional e cobrança por mensagem. [^8]

A diferença estratégica é simples:

```
Plataforma frágil:
lista fria + rotação de números + disparo indiscriminado

Plataforma defensável:
consentimento + WABA do cliente + templates + segmentação +
qualidade + auditoria + API oficial
```

A primeira escala como um castelo de cartas em uma turbina. A segunda pode virar SaaS.

Vale criar um monitor mensal das políticas, preços, limites e categorias da Meta, porque essas regras mudam com frequência.

[^1]: [developers.facebook.com](https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/get-started-for-tech-providers?utm_source=chatgpt.com)

[^2]: [business.whatsapp.com](https://business.whatsapp.com/policy?lang=pt_BR&utm_source=chatgpt.com)

[^3]: [developers.facebook.com](https://developers.facebook.com/documentation/business-messaging/whatsapp/marketing-messages/overview?utm_source=chatgpt.com)

[^4]: [developers.facebook.com](https://developers.facebook.com/documentation/business-messaging/whatsapp/throughput?utm_source=chatgpt.com)

[^5]: [developers.facebook.com](https://developers.facebook.com/documentation/business-messaging/whatsapp/messaging-limits?utm_source=chatgpt.com)

[^6]: [developers.facebook.com](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/marketing-templates/per-user-limits?utm_source=chatgpt.com)

[^7]: [developers.facebook.com](https://developers.facebook.com/documentation/business-messaging/whatsapp/policy-enforcement?utm_source=chatgpt.com)

[^8]: [developers.facebook.com](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing?utm_source=chatgpt.com)