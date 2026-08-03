# Auditoria do Repositório `ginkgo-platform` para `Ginkgo LEAF`

**Autor:** Manus AI
**Data:** 30 de Abril de 2026

## 1. Sumário Executivo

O repositório `ginkgo-platform` foi auditado com o objetivo de comparar sua implementação atual com a visão do **Ginkgo LEAF**, um CRM + Sistema Operacional de Vendas e Suporte via WhatsApp com inteligência artificial. A auditoria focou em identificar componentes existentes e lacunas de implementação para a transição do escopo mais amplo do "Ginkgo Platform" para o produto focado "Ginkgo LEAF".

Em resumo, a base do monorepo, a estrutura da API Fastify e o frontend Next.js estão bem estabelecidos. O core de faturamento por tokens e a integração básica com Evolution API e Stripe já existem. No entanto, a maior parte da lógica de negócio específica do LEAF, como o CRM unificado, o inbox de conversas, o assistente de IA e os fluxos de automação n8n, ainda está em estágios iniciais ou é representada por mockups no frontend.

## 2. Avaliação do Estado Atual vs. Plano LEAF

A tabela a seguir detalha o estado atual dos componentes do `ginkgo-platform` em comparação com o plano de transformação para `Ginkgo LEAF`.

| Dimensão | Status Atual (Ginkgo Platform) | Status Desejado (Ginkgo LEAF) | Observações da Auditoria |
|---|---|---|---|
| Estrutura Monorepo (Turborepo + pnpm) | ✅ Sólida | ✅ Manter | Estrutura `apps/` e `packages/` bem definida. |
| API Fastify com rotas modulares | ✅ Boa base | ✅ Refatorar módulos | Rotas para `auth`, `tenants`, `onboarding`, `leads`, `leaf`, `agents`, `provisioning`, `webhooks` existem. | 
| Web app Next.js 16 com dashboard | ✅ Shell de UI | ✅ Simplificar páginas | Dashboard com `Overview`, `Inbox`, `CRM`, `Assistant`, `Automations`, `Billing`, `Settings` (alguns com mockups). | 
| DB Supabase multi-tenant com RLS | ✅ Forte | ✅ Estender para LEAF | `profiles`, `tenants`, `memberships`, `module_entitlements`, `customers_billing`, `subscriptions` implementados. Migrações `001` a `005` presentes. | 
| Token Engine (faturamento) | ✅ Funcional | ✅ Manter e adaptar | `tokenRouter.ts` e `001_token_engine_schema.sql` confirmam implementação de débito/crédito de tokens. | 
| Agent Kernel (@ginkgo/agents) | ⚠️ Esqueleto | ✅ Reconstruir para Gemma 4 | `packages/agents/src/kernel.ts` e `soulsManager.ts` mostram uma arquitetura de kernel e "souls" (agentes) existente, mas ainda genérica e com foco em `gpt-4o` ou `claude`. | 
| Integração WhatsApp (Evolution API) | ⚠️ Webhook existe | ✅ Implementação completa | `webhooks.routes.ts` tem rota `/evolution` que processa mensagens, resolve leads e gera respostas via `replyGenerator.ts`. O `leaf.service.ts` para canais está mockado [1]. | 
| Orquestração n8n | ⚠️ Referências | ✅ Workflows reais | `webhooks.routes.ts` tem rotas para `n8n/incoming`, `n8n/leads/shadow-create`, `n8n/leads/:phone/smart-update`, `n8n/interactions`. `n8nExecutor.ts` é um executor genérico de webhook [2]. | 
| Integração Stripe | ⚠️ Webhook handler | ✅ Connect + links de pagamento | `webhooks.routes.ts` tem rota `/stripe` para `checkout.session.completed`, `invoice.payment_succeeded`, `customer.subscription.deleted`. Falta a geração de links de pagamento personalizados [3]. | 
| 7 Agentes Soul (Brann–Atlas) | ❌ Remover | ✅ 1 assistente configurável | A arquitetura de `agents` ainda suporta múltiplos agentes, mas o plano é simplificar para um assistente por workspace. | 
| Módulos de Conteúdo/Ads | ❌ Remover | ❌ Remover | `content_posts` e `ad_campaigns` existem na migração `004_agents_leads_files_rag.sql`, mas o plano é removê-los. | 
| Gamificação | ❌ Remover | ❌ Remover | Não há evidência direta de gamificação no código atual, mas o plano sugere remoção. | 
| DocuSign, HeyGen, Gamma, Apify | ❌ Remover | ❌ Remover | Não há evidência direta dessas integrações no código atual. | 

## 3. O Que Será Removido

### 3.1 Código Morto / Overengineering (Ações de DELETE)

Conforme o plano, os seguintes itens devem ser removidos. A auditoria confirma a existência de alguns deles no código ou no esquema do banco de dados:

*   **Páginas de UI:**
    *   `apps/web/app/(dashboard)/dashboard/office/`: Não encontrada diretamente, mas o conceito de "Office" não está presente na navegação atual [4].
    *   `apps/web/app/(dashboard)/dashboard/files/`: Não encontrada na navegação atual [4].
    *   `apps/web/app/(dashboard)/dashboard/tasks/`: Não encontrada na navegação atual [4].
    *   `apps/web/app/(dashboard)/dashboard/contacts/`: Não encontrada na navegação atual [4].
*   **Módulos API:**
    *   `apps/api/src/modules/files/`: Não encontrado. O `filesApi` no frontend (`apps/web/lib/api.ts`) aponta para `/files`, mas o módulo backend não existe, indicando que já foi removido ou nunca foi implementado [5].
*   **Tabelas do Banco de Dados (da migração `004_agents_leads_files_rag.sql`):**
    *   `content_posts`: **Existe**. Deve ser removida.
    *   `ad_campaigns`: **Existe**. Deve ser removida.
    *   `rag_documents`: **Existe**. O plano sugere simplificar para uma base de conhecimento do agente. Atualmente, é uma tabela separada para RAG.
    *   `agent_templates`: **Existe**. O plano sugere substituir por geração de persona baseada em nicho.
*   **Constantes Compartilhadas:**
    *   `packages/shared/src/modules.ts`: Já refatorado para conter apenas `CRM`, `INBOX`, `ASSISTANT`, `SCHEDULING`, `PAYMENTS` [6]. As constantes `WAVE`, `PYRE`, `BRAIN`, `N8N_INTEGRATION`, `EMAIL_MARKETING` já foram removidas deste arquivo.

### 3.2 Documentação para Arquivar (Ações de DEPRECATE)

Os seguintes documentos na pasta `docs/` devem ser arquivados, pois refletem a arquitetura anterior ou conceitos descontinuados:

*   `docs/AI_CRUD_ARCHITECTURE.md`
*   `docs/PLATFORM_SPEC.md`
*   `docs/PROMPT_AI_CRUD.md`
*   `docs/ECOSYSTEM_MAP.md`
*   `docs/TOKEN_ENGINE_ARCHITECTURE.md`
*   `docs/GUIDED_CODING_MANUAL.md`
*   `docs/DEPLOYMENT_AND_HANDOVER.md`
*   `docs/RESPONSABILIDADES_E_MULTITENANT.md`

### 3.3 Variáveis de Ambiente para Remover

As seguintes variáveis de ambiente, mencionadas no plano, não foram encontradas em uso direto nos arquivos `aiGateway.ts` ou `webhooks.routes.ts` para as integrações principais, indicando que já foram removidas ou não são mais relevantes para o escopo LEAF:

*   `ELEVENLABS_API_KEY`, `NANO_BANANA_API_KEY`, `HEYGEN_API_KEY`
*   `DOCUSIGN_*`
*   `META_APP_ID`, `META_APP_SECRET`, `META_WHATSAPP_TOKEN`, `META_INSTAGRAM_TOKEN`
*   `ANTHROPIC_API_KEY`, `OPENAI_API_KEY` (substituídas por `AI_API_KEY` genérico no `aiGateway.ts` [7]).

## 4. Arquitetura Final do Ginkgo LEAF (Status de Implementação)

### 4.1 Estrutura do Monorepo (Simplificada)

A estrutura do monorepo está alinhada com o plano, com as seguintes observações:

*   **`apps/api/src/modules/`**: 
    *   `auth/`, `tenants/`: **EXISTEM** e estão funcionais.
    *   `onboarding/`: **EXISTE**, mas a lógica de steps (`onboarding.service.ts`) ainda usa um mock de 6 passos genéricos, não o wizard de 5 passos baseado em nicho [8].
    *   `crm/`: **NÃO EXISTE** como módulo API separado. A funcionalidade de leads está em `apps/api/src/modules/leads/` e precisa ser unificada e estendida para o CRM completo.
    *   `inbox/`: **NÃO EXISTE** como módulo API separado. A funcionalidade de WhatsApp está em `apps/api/src/modules/leaf/` e `webhooks.routes.ts`, mas o `leaf.service.ts` está amplamente mockado [1].
    *   `assistant/`: **NÃO EXISTE** como módulo API separado. A lógica de agentes está em `apps/api/src/modules/agents/` e `packages/agents/`.
    *   `scheduling/`: **NÃO EXISTE**.
    *   `payments/`: **NÃO EXISTE** como módulo API separado. A integração Stripe está em `webhooks.routes.ts`.
    *   `webhooks/`: **EXISTE** e contém handlers para Evolution, Stripe e n8n [3].
    *   `billing/`: **NÃO EXISTE** como módulo API separado. A lógica de faturamento está em `tokenRouter.ts` e migrações SQL [9].
*   **`apps/web/`**: 
    *   `(auth)/`, `onboarding/`: **EXISTEM**. O onboarding no frontend (`apps/web/app/onboarding/page.tsx`) é um mockup com estado local [10].
    *   `(dashboard)/dashboard/`: 
        *   `page.tsx` (Overview): **EXISTE** com KPIs mockados [11].
        *   `inbox/`: **EXISTE** como placeholder de UI [12].
        *   `crm/`: **EXISTE** e faz chamadas reais para a API de leads, mas agrupa por `status` genérico, não por `stage` do pipeline LEAF [13].
        *   `assistant/`: **EXISTE** como placeholder de UI [4].
        *   `automations/`: **EXISTE** como placeholder de UI com workflows hardcoded [14].
        *   `billing/`: **EXISTE** como placeholder de UI com dados mockados [15].
        *   `settings/`: **EXISTE** com conexões mockadas [16].
*   **`packages/`**: 
    *   `db/`, `config/`, `ui/`: **EXISTEM** e estão funcionais.
    *   `shared/`: **EXISTE** e já foi refatorado para as constantes do LEAF [6].
    *   `agents/`: **EXISTE** e contém o `GinkgoAgentKernel`, `LLMRouter`, `SoulsManager`, `N8nToolExecutor` e `MemoryManager` [17].
*   **`docs/`**: Precisa ser reescrito para documentação específica do LEAF.

### 4.2 Esquema de Dados de Alto Nível (Status de Implementação)

O esquema de dados atual (`schema.sql` e migrações) já possui uma base sólida, mas requer extensões e refatorações para o LEAF:

*   **CORE MULTI-TENANT**: `profiles`, `tenants`, `memberships` **EXISTEM** e estão funcionais [18].
*   **BILLING**: `plans`, `subscriptions`, `customers_billing`, `token_wallets`, `token_ledger` **EXISTEM** e estão funcionais [9] [19].
*   **CRM**: A tabela `leads` **EXISTE** (`004_agents_leads_files_rag.sql`), mas o campo `status` é genérico. Precisa ser refatorado para o `stage` do pipeline LEAF (`new`, `qualified`, `scheduled`, `negotiating`, `closed`, `lost`) e incluir campos como `ai_next_action`, `assigned_agent_id`, `stripe_payment_link_id`, `payment_status` [20].
*   **CONVERSATIONS**: As tabelas `conversations` e `messages` **NÃO EXISTEM**. Atualmente, as interações são registradas na tabela `interactions` (`004_agents_leads_files_rag.sql`) [20].
*   **WHATSAPP CHANNELS**: A tabela `whatsapp_instances` **NÃO EXISTE**. A integração atual usa `leaf_channels` (mencionada em `webhooks.routes.ts` [3]), que precisa ser refatorada para `whatsapp_instances` com `evolution_instance_id` e `config JSONB`.
*   **SCHEDULING**: A tabela `appointments` **NÃO EXISTE**.
*   **PAYMENTS**: A tabela `payment_links` **NÃO EXISTE**. O `stripe_payment_link_id` está previsto no `leads` mas a tabela de links não existe [20].
*   **ASSISTANT**: A tabela `workspace_assistants` **NÃO EXISTE**. Atualmente, a configuração de agentes está na tabela `agents` (`004_agents_leads_files_rag.sql`) [20].
*   **AUTOMATION STATUS**: A tabela `automations` **NÃO EXISTE**.

## 5. Módulos Core e Responsabilidades (Status de Implementação)

| Módulo | API Prefix | Responsabilidade | Status de Implementação | Lacunas / Próximos Passos |
|---|---|---|---|---|
| **Auth** | `/auth` | Login, signup, JWT, Google OAuth | ✅ Implementado | Completo. |
| **Tenants** | `/tenants` | CRUD de Workspace | ✅ Implementado | Completo. |
| **Onboarding** | `/onboarding` | Wizard de 5 passos baseado em nicho | ⚠️ Parcialmente implementado | API existe, mas a lógica de steps é genérica e o frontend é mockado. Precisa de refatoração para o fluxo LEAF [8] [10]. |
| **CRM** | `/crm` | Leads, pipeline, contatos | ⚠️ Parcialmente implementado | API de `leads` existe, mas precisa ser unificada e estender o schema para `stage` e campos específicos do LEAF [20]. Frontend faz chamadas reais, mas a visualização do pipeline é baseada em `status` genérico [13]. |
| **Inbox** | `/inbox` | Conversas WhatsApp | ❌ Não implementado | A API `leaf` está mockada [1]. O frontend é um placeholder [12]. Necessita de implementação completa das tabelas `conversations` e `messages` e lógica de negócio. |
| **Assistant** | `/assistant` | Assistente de IA do CRM | ⚠️ Parcialmente implementado | A lógica de agentes (`packages/agents/`) existe, mas precisa ser adaptada para um único assistente configurável por workspace e integrada ao frontend [17]. |
| **Scheduling** | `/scheduling` | Agendamentos e Calendário | ❌ Não implementado | Necessita de API e tabelas (`appointments`) [20]. |
| **Payments** | `/payments` | Stripe Connect + links de pagamento | ⚠️ Parcialmente implementado | Webhooks Stripe existem [3]. Falta API para geração de links de pagamento personalizados e a tabela `payment_links` [20]. |
| **Webhooks** | `/webhooks` | Evolution + Stripe + n8n | ✅ Implementado | Handlers para Evolution, Stripe e n8n estão presentes e funcionais [3]. |
| **Billing** | `/billing` | Assinaturas + uso de tokens | ✅ Implementado | A lógica de débito/crédito de tokens (`tokenRouter.ts`) e o esquema de planos/limites (`005_plan_limits_enforcement.sql`) estão implementados [9] [19]. O frontend é mockado [15]. |

## 6. Perguntas Abertas (Conforme o Plano)

1.  **Acesso à API Gemma 4**: O `aiGateway.ts` já possui suporte para provedores `google` (que inclui Gemma 4) e `openai`, configurável via variáveis de ambiente `AI_PROVIDER`, `AI_MODEL`, `AI_API_KEY` [7]. Portanto, a arquitetura já está preparada para Gemma 4. A questão é se a chave de API (`AI_API_KEY`) está disponível e configurada para o ambiente de produção.
2.  **Stripe Connect vs. Simple Links**: A implementação atual do Stripe via webhook (`webhooks.routes.ts`) lida com eventos de `checkout.session.completed`, `invoice.payment_succeeded` e `customer.subscription.deleted` [3]. Isso sugere que a integração é mais voltada para o faturamento da plataforma (assinaturas). A geração de links de pagamento personalizados para leads, conforme o plano LEAF, **ainda não está implementada** e exigiria uma extensão da API e do esquema de dados (`payment_links`). A sugestão de usar links simples gerados pela plataforma no Phase 1 e adiar o Stripe Connect completo para o Phase 2 é uma abordagem pragmática e alinhada com o estado atual.
3.  **Modelo de Autenticação Evolution API**: O `webhooks.routes.ts` resolve o `org_id` a partir do `instanceName` da Evolution API, buscando na tabela `leaf_channels` [3]. Para o LEAF, onde cada workspace precisa de sua própria instância Evolution, é crucial que a Evolution API suporte a criação multi-instância via API ou que haja um processo de provisionamento automatizado (possivelmente via n8n). O `provisioning.service.ts` existe, mas é um mockup simulado [21]. Esta é uma **lacuna crítica** que precisa de uma solução real de provisionamento de instâncias da Evolution API.
4.  **Templates de Workflow n8n**: O plano prevê a criação automática de workflows n8n durante o onboarding. O `n8nExecutor.ts` é um executor genérico de webhooks n8n [2]. O `provisioning.service.ts` é um mockup [21]. A capacidade de criar ou clonar workflows n8n via API é **essencial e não implementada** no código atual. Isso exigiria integração com a API do n8n para gerenciamento de workflows.
5.  **Idioma**: O código e a UI atuais estão em Português (pt-BR). O plano não especifica internacionalização, mas o `AppSidebar.tsx` e `page.tsx` do dashboard confirmam o uso de textos em português [4] [11]. Manter o Português como idioma principal é o caminho de menor resistência, mas a internacionalização (`i18n`) desde o início é uma boa prática para produtos SaaS escaláveis.

## 7. Conclusão e Próximos Passos

O `ginkgo-platform` possui uma base técnica robusta e bem estruturada, com um monorepo organizado, API Fastify e frontend Next.js. O core de autenticação, multi-tenancy e faturamento por tokens está funcional. As integrações com Evolution API e Stripe estão presentes via webhooks, mas focadas em aspectos específicos (recebimento de mensagens e eventos de faturamento, respectivamente).

As principais lacunas para a visão do `Ginkgo LEAF` residem na **implementação completa dos módulos de negócio**: CRM unificado com pipeline de vendas, inbox de conversas WhatsApp, assistente de IA configurável, agendamentos e a geração de links de pagamento personalizados. Além disso, o **provisionamento automatizado de instâncias da Evolution API e de workflows n8n** são pontos críticos que atualmente são mockups ou não implementados.

**Próximos Passos Recomendados:**

1.  **Refatorar e Estender o CRM**: Unificar o módulo `leads` para o `crm` e estender o esquema de dados para incluir os campos de `stage` e `ai_next_action` conforme o plano LEAF.
2.  **Implementar Módulo Inbox**: Criar as tabelas `conversations` e `messages` e desenvolver a lógica de negócio para o inbox de WhatsApp, incluindo o fluxo de bot para agente humano.
3.  **Desenvolver Módulo de Agendamentos**: Implementar a API e o esquema de dados para `appointments`.
4.  **Implementar Geração de Links de Pagamento**: Desenvolver a API para criar `payment_links` personalizados via Stripe e integrar com o CRM.
5.  **Provisionamento Automatizado**: Investigar e implementar a integração com a API da Evolution API para provisionamento de instâncias e com a API do n8n para criação/clonagem de workflows.
6.  **Refatorar Onboarding**: Atualizar a lógica do onboarding para o wizard de 5 passos baseado em nicho, integrando com o provisionamento real de canais e assistentes.
7.  **Simplificar Agentes**: Adaptar a arquitetura de `agents` para suportar um único assistente configurável por workspace, conforme a visão LEAF.
8.  **Remover Código Morto**: Excluir as tabelas `content_posts`, `ad_campaigns`, `rag_documents` (ou refatorar para o novo modelo de KB do assistente) e `agent_templates`.

Este relatório serve como um guia para as próximas fases de desenvolvimento, priorizando as funcionalidades essenciais para o lançamento do Ginkgo LEAF.

## Referências

[1] `apps/api/src/modules/leaf/leaf.service.ts`
[2] `packages/agents/src/tools/n8nExecutor.ts`
[3] `apps/api/src/modules/webhooks/webhooks.routes.ts`
[4] `apps/web/components/layout/AppSidebar.tsx`
[5] `apps/web/lib/api.ts`
[6] `packages/shared/src/modules.ts`
[7] `apps/api/src/services/aiGateway.ts`
[8] `apps/api/src/modules/onboarding/onboarding.service.ts`
[9] `apps/api/src/services/tokenRouter.ts`
[10] `apps/web/app/onboarding/page.tsx`
[11] `apps/web/app/(dashboard)/dashboard/page.tsx`
[12] `apps/web/app/(dashboard)/dashboard/inbox/page.tsx`
[13] `apps/web/app/(dashboard)/dashboard/crm/page.tsx`
[14] `apps/web/app/(dashboard)/dashboard/automations/page.tsx`
[15] `apps/web/app/(dashboard)/dashboard/billing/page.tsx`
[16] `apps/web/app/(dashboard)/dashboard/settings/page.tsx`
[17] `packages/agents/src/kernel.ts`
[18] `packages/db/schema.sql`
[19] `apps/api/migrations/005_plan_limits_enforcement.sql`
[20] `apps/api/migrations/004_agents_leads_files_rag.sql`
[21] `apps/api/src/modules/provisioning/provisioning.service.ts`
