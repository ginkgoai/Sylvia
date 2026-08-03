---
title: "GKO - Análise fluxo de vendas"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/68fee990-d37c-8330-8170-c82fb0008e6f"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
seg., 27 de out. às 0:39

![fce0be0b-c3bc-469d-b861-37d62a05c34b.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000170861f584a9b36578998193&ts=495692&p=fs&cid=1&sig=6bdbb78cba1fd956d007e5181e79996de009f2db1ece90ddbe07b3c0467bd75c&v=0)

de uma olhada no fluxo agora, analise, podemos montar ele assim? brann atendente conversacional da ginkgo atendendo e vendendo mostrando as funcionalidades de um agent de ia de atendimento, podendo conversar por audio quando quiser, se a pessoa se interessar entrar e assinar alguma das opções automaticamente brann aciona o mcp server e manda um email de confirmação para ela, agenda uma chamada, cadastra no supabase o novo cliente e seus dados e confirma o boleto no stripe, correto essas funções desse jeito?

Sim. A arquitetura bate. Para fechar o “assina → provisiona → confirma” faltam só os ganchos de compra, provisionamento e pós-venda. Resumo do que precisa + configs “copy/cola”.

## 1) Intenção de compra no BRANN

- BRANN já devolve JSON `out` e você já roteia por `out.type`. Acrescente IDs fixos para planos (`plano_basico`, `plano_futurista`) e um case “assinar”. O envio pelo Evolution segue os formatos já definidos.
	Visao-geral-do-fluxo

## 2) Router de cliques → criar checkout no Stripe (boleto)

Nó: **Switch** por `{{$json.buttonId}}` ou `{{$json.message?.selectedId}}`  
Cases: `plano_basico`, `plano_futurista` → **HTTP Request** (Stripe)

**HTTP Request (Stripe: Create Checkout Session)**

- Method: POST
- URL: `https://api.stripe.com/v1/checkout/sessions`
- Headers:
	- `Authorization: ={{'Bearer ' + $env.STRIPE_SECRET}}`
		- `Content-Type: application/x-www-form-urlencoded`
- Body (Form URL Encoded):
```markdown
success_url={{$env.APP_URL}}/success?sid={CHECKOUT_SESSION_ID}
cancel_url={{$env.APP_URL}}/cancel
mode=subscription
payment_method_types[0]=boleto
line_items[0][price]={{$json.price_id}}   // defina por plano
line_items[0][quantity]=1
customer_email={{$json.email}}
locale=pt-BR
```
- Output: pegue `url` → responda com botão “Pagar boleto / Cartão”.

Opcional BR: se preferir **Payment Links**, pule a criação de session e só envie a URL do link do produto.

## 3) Webhook Stripe → confirmar pagamento

Crie um **Webhook → HTTP Trigger** no n8n: `/stripe/webhook`

- Verifique assinatura com `$env.STRIPE_WEBHOOK_SECRET`.
- Eventos de interesse:
	- `checkout.session.completed` → status “pendente” se boleto.
		- `payment_intent.succeeded` → boleto pago. Marque “ativo”.

Fluxo:  
`Stripe Webhook` → **Switch** event →

- `payment_intent.succeeded` → **Upsert Supabase** (cliente + assinatura) → **MCP: provisionar\_cliente** → **E-mail confirmação** → **Mensagem Evolution**.

## 4) Supabase: cadastro/atualização do cliente

Use **HTTP Request** (ou nó Supabase).

- Method: POST (ou PATCH)
- URL: `={{$env.SUPABASE_URL}}/rest/v1/customers`
- Headers:
	- `apikey: ={{$env.SUPABASE_SERVICE_ROLE}}`
		- `Authorization: ={{'Bearer ' + $env.SUPABASE_SERVICE_ROLE}}`
		- `Content-Type: application/json`
- Body (JSON):
```markdown
{
  "email": "={{$json.customer_email}}",
  "phone": "={{$json.phone}}",
  "name": "={{$json.name}}",
  "plan_id": "={{$json.plan_id}}",
  "stripe_customer_id": "={{$json.customer}}",
  "stripe_subscription_id": "={{$json.subscription}}",
  "status": "active",
  "started_at": "={{$now}}"
}
```

## 5) MCP Server: provisionamento

**HTTP Request** para seu MCP:

- Method: POST
- URL: `={{$env.MCP_URL}}/provisionar_cliente`
- Headers: `Authorization: ={{'Bearer ' + $env.MCP_TOKEN}}`, `Content-Type: application/json`
- Body:
```markdown
{
  "email": "={{$json.customer_email}}",
  "phone": "={{$json.phone}}",
  "nome": "={{$json.name}}",
  "plano": "={{$json.plan_id}}",
  "fonte": "stripe",
  "datasets": ["brann_preset","faq_ginkgo"],
  "whatsapp_instance": "={{$env.EVOLUTION_INSTANCE}}"
}
```

## 6) E-mail de confirmação

Use **SMTP** ou **Resend API**.

- Assunto: “Ginkgo | Assinatura confirmada”
- Corpo: dados do plano, link de onboarding e link de agenda.

## 7) Agendamento da chamada

Mais rápido: enviar **link Cal.com/Calendly** já configurado por plano.  
Automático: **HTTP Request** → Cal.com/Calendly API para criar invite com `email` do cliente e retornar link.

## 8) Confirmação no WhatsApp

Reaproveite seu sender Evolution:

- Texto curto confirmando pagamento e enviando:
	- Link da área do cliente / onboarding
		- Link da agenda
		- Nota fiscal quando aplicável

O envio de mensagens por Evolution segue seus templates atuais de `text/button/list/image/audio`.

Visao-geral-do-fluxo

## 9) Variáveis de ambiente mínimas

```markdown
EVOLUTION_BASE_URL
EVOLUTION_TOKEN
EVOLUTION_INSTANCE

STRIPE_SECRET
STRIPE_WEBHOOK_SECRET
APP_URL

SUPABASE_URL
SUPABASE_SERVICE_ROLE

MCP_URL
MCP_TOKEN

SMTP_HOST / SMTP_PORT / SMTP_USER / SMTP_PASS   // ou RESEND_API_KEY
CAL_BASE_URL / CAL_API_KEY                      // se usar API
```

## 10) Controles essenciais

- Idempotência: header `Idempotency-Key` na criação da session Stripe.
- Retentativas: `Retry On Fail` nos HTTP.
- Logs: `traceId`, `latency_ms`, `event` em **Set** antes do BRANN e no pós-venda.
- Privacidade: nunca ecoar tokens em erros.
- Fallback: se download de mídia falhar, responda por texto, como no blueprint.
	Visao-geral-do-fluxo

## 11) Onde plugar no seu canvas

- Depois do bloco Agent: adicione **Switch de intenção** → **Stripe** → **Resposta com link**.
- Novo “buffer pós-pagamento”: **Webhook Stripe** à direita, alimentando Supabase, MCP, E-mail e Evolução.
- BRANN permanece igual para mídia/JSON de saída.
	Visao-geral-do-fluxo

Conclusão: sim, pode montar assim. Com os 5 conectores acima o Brann vende, cobra por boleto, provisiona via MCP, registra no Supabase, agenda a call e confirma por e-mail e WhatsApp de ponta a ponta.