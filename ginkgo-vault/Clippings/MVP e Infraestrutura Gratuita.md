---
title: "MVP e Infraestrutura Gratuita"
source: "https://chatgpt.com/c/6a6628be-bf4c-83e9-8b88-b8a064d3a994"
author:
published:
created: 2026-07-26
description: "ChatGPT conversation with 2 messages"
tags:
  - "clippings"
---
**Você disse**

---

Esse Reel está **70% certo**. Ele mostra uma boa stack para lançar um MVP, mas vende a impressão de que infraestrutura gratuita equivale a negócio pronto. É como exibir o motor de uma nave e esquecer combustível, radar, tripulação e seguro contra meteoros.

## Onde a publicação simplifica demais

**Claude Max 20x não é o custo da IA do produto.**  
Ele serve principalmente para você desenvolver com Claude Code e usar o Claude intensivamente. As chamadas feitas pelo Leaf, Nyra ou outros agentes em produção continuam consumindo API, créditos ou OpenRouter separadamente. O plano Max oferece 5x ou 20x mais uso do aplicativo, enquanto cargas pesadas podem migrar para créditos de API. [^1]

**Vercel grátis não deve hospedar um SaaS comercial.**  
O plano Hobby é oficialmente destinado a uso pessoal e não comercial. Para Ginkgo, seria necessário Vercel Pro ou hospedar o Next.js na própria VPS. [^2]

**Supabase Free é desenvolvimento, não produção crítica.**  
O gratuito possui 500 MB de banco, não oferece backup automático, não oferece SLA e pode pausar após uma semana de baixa atividade. O Pro começa em US$ 25/mês e inclui backups diários. Isso é especialmente relevante para o Leaf, no qual perder conversas, clientes ou configurações seria um pequeno episódio de Black Mirror corporativo. [^3]

**OpenClaw e Hermes não deveriam ser dois “cérebros centrais”.**  
Eles possuem funções sobrepostas de agente, memória, skills e execução. O próprio Hermes oferece migração dos dados do OpenClaw, indicando que são alternativas ou camadas parcialmente concorrentes, não uma combinação obrigatória. [^4]  
Além disso, agentes persistentes com acesso a memória, arquivos, cron e shell ampliam bastante a superfície de ataque. Devem operar com permissões limitadas, aprovação humana e isolamento. [^5]

**Stripe não custa universalmente 2,9% no Brasil.**  
As tarifas dependem do método de pagamento, moeda, origem do cartão e configuração da conta. O número do vídeo provavelmente replica a tarifa americana como se fosse global. [^6]

## Stack correta para a Ginkgo

```
USUÁRIO
   ↓
Cloudflare
   ↓
Next.js / Vercel Pro ou VPS
   ↓
Fastify API Gateway
   ↓
Ginkgo Agent OS
   ├── Leaf
   ├── Pyre
   ├── Wave
   └── Nyra / Alfred / Brann
   ↓
PostgreSQL + Supabase
   ↓
Redis + BullMQ
   ↓
Workers / n8n / integrações externas
```

### Camada recomendada

| Função | Escolha para Ginkgo |
| --- | --- |
| DNS, proteção e cache | Cloudflare |
| Frontend | Next.js + Vercel Pro ou Docker na VPS |
| API principal | Node.js + Fastify |
| Banco | Supabase Pro/PostgreSQL com RLS |
| Autenticação | Supabase Auth inicialmente |
| Filas e jobs | Redis + BullMQ |
| Workflows determinísticos | n8n |
| Agente operacional | Hermes **ou** OpenClaw |
| WhatsApp | Evolution API + Chatwoot |
| IA em produção | OpenRouter/APIs diretas com roteamento |
| Desenvolvimento | Claude Code/Codex |
| E-mail transacional | Resend |
| Pagamentos | Stripe para SaaS |
| Analytics | PostHog |
| Erros | Sentry |
| Vetores | pgvector primeiro |
| Arquivos | Supabase Storage ou S3 compatível |
| Segredos | Vault/Doppler/Secrets do ambiente |
| Deploy | Docker Compose + Traefik |
| Backups | Snapshot diário externo e restauração testada |

## O que eu removeria

**Clerk**, inicialmente. Supabase Auth já cobre autenticação e reduz duplicação.

**Pinecone**, inicialmente. O `pgvector` dentro do PostgreSQL atende RAG e busca semântica no MVP. Pinecone só entra quando volume, latência ou isolamento justificarem outro serviço.

**Hotmart**, para o núcleo do SaaS. Faz sentido para cursos, mentorias, afiliados e produtos digitais. Para assinatura do Leaf, Stripe e faturamento próprio oferecem mais controle.

**OpenClaw + Hermes juntos no caminho crítico.** Escolha um deles para operações supervisionadas. O núcleo precisa continuar determinístico: API, banco, filas, políticas e evidências.

## Arquitetura ideal para o seu cenário

A melhor divisão seria:

```
Claude Code / Codex
→ constroem o software

Hermes ou OpenClaw
→ auxiliam operadores e executam missões supervisionadas

Ginkgo Agent OS
→ decide políticas, permissões, tenants e governança

BullMQ + n8n
→ executam tarefas previsíveis

Supabase/PostgreSQL
→ mantém o estado oficial e auditável
```

O ponto central: **agente não pode ser banco de dados, backend e administrador ao mesmo tempo**. Agente improvisa; infraestrutura precisa ser entediante, previsível e auditável. Quando o backend começa a “ter personalidade”, normalmente alguém esqueceu de implementar uma máquina de estados.

Para a Ginkgo, essa imagem deve ser tratada como uma lista de ingredientes. A receita de produção continua sendo a arquitetura que você já vem formando: **Fastify + Supabase/Postgres + Redis/BullMQ + n8n + Docker + Agent OS + produtos especializados**.

[^1]: [claude.com](https://claude.com/pricing)

[^2]: [vercel.com](https://vercel.com/pricing)

[^3]: [supabase.com](https://supabase.com/pricing)

[^4]: [github.com](https://github.com/hermes-agent-org/hermes)

[^5]: [arxiv.org](https://arxiv.org/abs/2605.13471?utm_source=chatgpt.com)

[^6]: [stripe.com](https://stripe.com/en-br/pricing)