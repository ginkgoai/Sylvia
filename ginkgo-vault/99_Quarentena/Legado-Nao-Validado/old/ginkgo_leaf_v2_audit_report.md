# Auditoria de Atualização: `Ginkgo LEAF` (Versão 2)

**Autor:** Manus AI
**Data:** 30 de Abril de 2026

## 1. Sumário Executivo

Esta auditoria analisa as novas alterações fornecidas no arquivo `leaf-main(1).zip`. O projeto evoluiu significativamente de um "Platform Shell" para uma arquitetura de **SaaS de IA focado em Real Estate e Vendas**. 

A principal mudança é a introdução de uma camada de serviços robusta no backend (`apps/api/services`) para lidar com **HITL (Human-in-the-loop)**, **RAG (Knowledge Base)**, **Follow-ups** e **Agendamentos**. No entanto, existe um "descompasso" técnico: o código desses serviços já está presente, mas as tabelas de banco de dados necessárias ainda estão em fase de especificação (Migração 007).

## 2. O Que Temos (Novidades da V2)

### 2.1 Backend Refatorado (`apps/api`)
O backend foi reorganizado em módulos claros e serviços especializados:
*   **Módulos Core**: `assistant`, `auth`, `crm`, `onboarding`, `workspaces`.
*   **Serviços de Inteligência**:
    *   `llm/replyGenerator.ts`: Lógica completa de geração de resposta contextual, incluindo injeção de RAG e diretivas por estágio do CRM [1].
    *   `knowledgeBase/ragEngine.ts`: Motor de busca semântica e híbrida (pgvector + keyword) [2].
    *   `hitl/hitlManager.ts`: Sistema de escalação para humanos baseado em confiança e palavras-chave [2].
    *   `followup/followupManager.ts`: Orquestrador de seguimentos automáticos para leads inativos [2].
    *   `conversation/stateManager.ts`: Gerenciador de estado de conversas (AI pausada, mutex de processamento) [2].
    *   `scheduling/googleCalendarManager.ts`: Integração real com Google Calendar para agendamentos [2].

### 2.2 Banco de Dados e Migrações
*   **Migração 006 (Core LEAF)**: Implementa as tabelas fundamentais para o novo escopo: `whatsapp_instances`, `workspace_assistants`, `conversations`, `messages`, `appointments`, `payment_links`, `knowledge_files` e `automations` [3].
*   **RLS (Row Level Security)**: Arquivo `db/rls.sql` presente, garantindo o isolamento multi-tenant.

### 2.3 Agentes e Automações
*   **WhatsApp Agent**: Pasta `agents/whatsapp-agent` com `system.prompt.md` detalhado e definições de ferramentas (`tools.ts`) [4].
*   **n8n Workflows**: Placeholders criados em `automations/n8n/` para `whatsapp-inbound`, `follow-up`, `lead-enrichment`, `payments`, `scheduling` e `hitl` [5].

## 3. O Que Falta (Gaps Críticos)

### 3.1 Descompasso Schema vs. Código (O Maior Gap)
O arquivo `docs/MIGRATION_007_CORE_REFACTOR.md` descreve alterações vitais que **ainda não foram aplicadas** ao banco de dados, mas que o código dos serviços já tenta utilizar:
*   **Tabelas Faltantes**: `escalations`, `follow_ups`, `rag_documents`.
*   **Colunas Faltantes em `conversations`**: `ai_paused_until`, `pause_reason`, `processing_lock`.
*   **Colunas Faltantes em `agents`**: `hitl_config`, `rag_config`.
*   **Colunas Faltantes em `organizations`**: Tokens de OAuth do Google Calendar.

### 3.2 Implementações Pendentes (Arquivos Vazios)
Alguns arquivos críticos foram criados como placeholders, mas estão vazios:
*   **`apps/api/services/whatsapp/evolution.ts`**: A integração direta com a API da Evolution ainda não está codificada neste arquivo (embora o webhook handler use a lógica).
*   **`apps/api/services/billing/stripe.ts`**: Lógica de criação de links de pagamento e checkout via código ainda pendente.
*   **`automations/n8n/*.json`**: Os arquivos de exportação dos workflows n8n estão vazios. As automações existem como conceito, mas os arquivos `.json` para importação não contêm os nós e conexões.

### 3.3 Frontend (UI Shell)
Apesar da estrutura de pastas em `apps/web` estar alinhada (`inbox`, `crm`, `assistant`, `billing`), as páginas continuam sendo **placeholders de UI** com dados mockados:
*   **Inbox**: Apenas uma tela de "Em breve/Conecte seu WhatsApp" [6].
*   **CRM**: Visualização básica de lista, sem o pipeline visual de estágios (Kanban).
*   **Onboarding**: Fluxo de 5 passos ainda é um mockup visual no frontend.

## 4. Comparativo: Plano LEAF vs. Estado Atual

| Componente | Plano LEAF | Estado Atual (V2) |
|---|---|---|
| **CRM Unificado** | Pipeline de 6 estágios | ⚠️ Backend pronto (schema 006), Frontend mockado. |
| **Inbox WhatsApp** | Handoff Bot/Humano | ⚠️ Lógica de HITL pronta no backend, Frontend mockado. |
| **Assistente IA** | Gemma 4 + RAG | ✅ `aiGateway` e `ragEngine` prontos. |
| **Agendamentos** | Google Calendar | ✅ `googleCalendarManager` pronto no backend. |
| **Pagamentos** | Links Stripe via Chat | ⚠️ Schema pronto, serviço `stripe.ts` vazio. |
| **Tokens** | Faturamento por uso | ✅ `tokenRouter.ts` funcional. |
| **n8n Engine** | Workflows orquestradores | ⚠️ Estrutura pronta, arquivos `.json` vazios. |

## 5. Recomendações de Próximos Passos

1.  **Executar Migração 007**: Transformar o conteúdo de `MIGRATION_007_CORE_REFACTOR.md` em um script SQL real e aplicar no Supabase para destravar os serviços de HITL, RAG e Follow-up.
2.  **Codificar `evolution.ts` e `stripe.ts`**: Implementar as chamadas de API reais para a Evolution API (provisionamento e envio) e Stripe (geração de links).
3.  **Exportar Workflows n8n**: Preencher os arquivos `.json` em `automations/n8n/` com os workflows reais para que possam ser deployados.
4.  **Conectar Frontend à API**: Substituir os mocks nas páginas de `inbox`, `crm` e `billing` por chamadas reais aos novos módulos da API.
5.  **Refinar Onboarding**: Implementar a lógica real de criação de workspace + instância WhatsApp + assistente inicial durante o fluxo de onboarding.

## Referências

[1] `apps/api/services/llm/replyGenerator.ts`
[2] `apps/api/services/` (subpastas `knowledgeBase`, `hitl`, `followup`, `conversation`, `scheduling`)
[3] `db/migrations/006_leaf_core.sql`
[4] `agents/whatsapp-agent/`
[5] `automations/n8n/`
[6] `apps/web/inbox/page.tsx`
