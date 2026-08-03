---
title: "Ginkgo Core - Comparação Flowise Agent Builder"
source: "https://chatgpt.com/g/g-p-68e0a0b393cc8191a0f44ad743e1117d/c/68ef16cc-9df8-8325-9907-e4ff60f88270"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
Arquitetura Ginkgo Leaf — Brann · Nyra · Alphie (mermaid)

## Arquitetura Ginkgo Leaf — Brann · Nyra · Alphie

> Diagrama técnico para um ecossistema de agentes LLM em produção, com foco em WhatsApp (Evolution API), n8n, Flowise/LangGraph, CrewAI, memória híbrida (Redis/Supabase), e ferramentas de criação/ops.

---

## 1) Mapa do Ecossistema (alto nível)

flowchart LR

%% Camada de Interface

subgraph UI\[Camada de Interface\]

U\[Cliente \\n (WhatsApp/IG/Site)\]

WA\[WhatsApp \\n Evolution API\]

ChatUI\[Web Chat/Widget \\n (ChatKit ou custom)\]

end

%% Camada de Orquestração

subgraph ORQ\[Camada de Orquestração\]

Router\[n8n Router \\n (entrada, autenticação, routing)\]

LG\[LangGraph / Flowise \\n (planejamento & controle)\]

Crew\[CrewAI \\n (multi-agentes coordenados)\]

end

%% Agentes

subgraph AG\[Agentes\]

Brann\[Brann \\n (Vendas/Atendimento)\]

Nyra\[Nyra \\n (Criação & Postagem)\]

Alphie\[Alphie \\n (Ops/Finance/CRM)\]

end

%% Ferramentas/Serviços

subgraph TOOLS\[Camada de Ferramentas\]

RAG\[RAG \\n (Supabase Vector / Postgres)\]

Redis\[(Redis)\\n Curta duração\]

KB\[Supabase Storage / Docs\]

CRM\[Pipefy/Notion/Pipedrive\]

Stripe\[Stripe/Hotmart \\n (Pagamentos)\]

IGAPI\[Instagram/TikTok/X API\]

TTS\[Kokoro (TTS)/ElevenLabs\]

IMG\[SynthMind/NanoBanana/Runway\]

Docs\[DocuSign/Contracts\]

Search\[Search/Web Crawler \\n (Firecrawl/Apify)\]

end

---

## 2) Sequência de Atendimento (exemplo realista)

sequenceDiagram

participant C as Cliente (WhatsApp)

participant E as Evolution API (WA)

participant N as n8n Router

participant O as Orquestrador (LangGraph/Flowise)

participant W as CrewAI (Coordenação)

participant B as Brann (Agente)

participant V as RAG (Supabase Vector)

participant P as CRM (Pipefy/Notion)

participant K as Kokoro (TTS)

participant S as Scheduler (n8n Jobs)

C->>E: Mensagem: "Quero orçamento"

E->>N: Webhook de mensagem

N->>O: Normaliza payload + credenciais

O->>W: Planejamento (definir agente principal)

W->>B: Delegação: Brann assume

B->>V: Consulta contexto (produtos/planos/FAQ)

V-->>B: Retorna trechos relevantes

B->>P: Busca dados do lead (histórico, estágio)

P-->>B: Dados do lead + tarefas pendentes

B->>B: Monta proposta (com regras/guardrails)

B->>S: Agenda follow-up (se necessário)

B->>K: Gera áudio de retorno amigável

K-->>B: URL/arquivo do áudio

B-->>O: Resposta final (texto + áudio + CTA)

O-->>N: Payload formatado

N-->>E: Envia mensagem no WhatsApp

E-->>C: Cliente recebe proposta

---

## 3) Orquestração Interna (camadas e responsabilidades)

flowchart TB

subgraph Interface

IN1\[WhatsApp via Evolution API\]

IN2\[Instagram/Forms/Site\]

end

subgraph Orquestracao\[Orquestração\]

Rtr\[n8n Router\]

LGF\[LangGraph/Flowise\]

CRW\[CrewAI\]

end

subgraph Agentes

B\[Brann\]

Nn\[Nyra\]

A\[Alphie\]

end

subgraph Memoria\[Memória\]

R\[(Redis) Curta\]

SV\[Supabase Vector\]

end

subgraph Ferramentas

CR\[CRM: Pipefy/Notion/Pipedrive\]

ST\[Stripe/Hotmart\]

TT\[Kokoro/ElevenLabs\]

IM\[SynthMind/NanoBanana/Runway\]

DS\[DocuSign/Contracts\]

SC\[Search/Firecrawl/Apify\]

KB\[Supabase Storage/Buckets\]

end

subgraph Ops\[Observabilidade & Segurança\]

OT\[OpenTelemetry/Logs\]

HC\[Healthchecks\]

---

## 4) Camadas & responsabilidades

- **Interface**: Evolution API (WhatsApp), webchat/ChatKit, formulários (onboarding).
- **Orquestração**: n8n faz roteamento/integração; LangGraph/Flowise planeja os passos/loops; CrewAI coordena conversas multi‑agentes.
- **Agentes**:
	- **Brann**: atendimento/vendas, RAG, CRM, contratos, voz (Kokoro), agendamentos.
		- **Nyra**: criação multimídia, calendário editorial, posting automatizado.
		- **Alphie**: operações/financeiro, relatórios, auditoria, Evals, métricas.
- **Memória**: Redis (curta duração/sessão), Supabase Vector & Storage (longo prazo, ativos/embeddings).
- **Ferramentas**: CRM (Pipefy/Notion/Pipedrive), pagamentos (Stripe/Hotmart), TTS (Kokoro), geração de imagem/vídeo (SynthMind/NanoBanana/Runway), contratos (DocuSign), busca/raspagem (Firecrawl/Apify).
- **Ops & Segurança**: Healthchecks, OpenTelemetry/Logs, Guardrails (PII/prevenção de prompt‑injection), Evals/QA automatizados.

---

## 5) Notas de deploy & boas práticas

- **EasyPanel + Docker**: isolar serviços (n8n, Evolution API, Flowise, Redis, Postgres/Supabase, Kokoro bridge, workers).
- **Segredos/ENV**: gerenciar via vault do provedor/secret manager; nunca commitar chaves.
- **Observabilidade**: rastrear *latência por etapa* (entrada → orquestração → ferramenta → resposta), taxas de erro, custo por conversa.
- **Guardrails**: sanitize de PII, timeouts, limites de tool‑use, políticas de segurança por agente.
- **Evals contínuos**: regressão de qualidade em prompts/flows; cenários críticos (billing, agendamentos, contratos) com testes automatizados.
- **Roteamento dinâmico**: fallback entre modelos, e entre ferramentas (ex.: se IG API cair, refile via buffer/post later).

---

## 6) Próximos passos rápidos

1. Exportar esses diagramas para documentação oficial (README do repositório infra).
2. Gerar um *boilerplate* (Docker Compose + env.example) com serviços mínimos.
3. Criar *templates* n8n (Router + Jobs) e Flowise (grafo-base) para clonagem por cliente.
4. Ligar Healthchecks e criar dashboards de custo/latência.
5. Definir *playbooks* de incidentes (ex.: API do WhatsApp fora, Stripe webhooks falhou, etc.).