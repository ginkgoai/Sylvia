# 🏗️ BRIEFING TÉCNICO: Auditoria e Roadmap de Execução — Ginkgo LEAF v2

**DE:** Engenheiro-Chefe de Automação e IA
**PARA:** Arquiteto de Sistemas / Lead Developer
**ASSUNTO:** Auditoria de Integridade e Plano de Sincronização Schema-Service

---

## 1. DIAGNÓSTICO DE ESTADO ATUAL

A auditoria da versão `leaf-main(2.0)` revela uma evolução significativa na camada de serviços, mas com um **descompasso crítico de sincronização** entre o código-fonte e a persistência. Temos uma arquitetura "Service-First" onde a lógica de negócio avançou além da infraestrutura de dados disponível.

### ⚠️ GAPS CRÍTICOS (BLOCKERS)
1.  **Schema Drift (Migração 007)**: Os serviços de `HITLManager`, `RAGEngine`, `FollowupManager` e `ConversationStateManager` estão instanciados, mas são inoperantes. Eles referenciam tabelas (`escalations`, `follow_ups`, `rag_documents`) e colunas de estado (`ai_paused_until`, `processing_lock`) que existem apenas no documento de especificação `MIGRATION_007_CORE_REFACTOR.md`.
2.  **Integrações "Ghost"**: Os arquivos `evolution.ts` (WhatsApp) e `stripe.ts` (Payments) são placeholders vazios (`0 bytes`). A lógica de envio e cobrança está desacoplada ou pendente de implementação.
3.  **Orquestração Vazia**: A pasta `automations/n8n/` contém a estrutura correta, mas os arquivos `.json` estão sem os metadados dos workflows. O motor está montado, mas sem o combustível (lógica n8n).

---

## 2. ARQUITETURA DE DADOS (STATUS CHECK)

| Entidade | Status | Ação Necessária |
| :--- | :--- | :--- |
| **WhatsApp Instances** | ✅ Schema 006 OK | Implementar provisionamento real em `evolution.ts`. |
| **CRM Leads** | ⚠️ Parcial | Refatorar `status` para `stage` (Pipeline LEAF). |
| **Conversations** | ⚠️ Incompleto | Aplicar colunas de State Management (Migração 007). |
| **HITL / Escalations** | ❌ Missing | Criar tabela `escalations` e colunas de config em `agents`. |
| **RAG / Knowledge** | ❌ Missing | Criar tabela `rag_documents` (pgvector) e config em `orgs`. |
| **Follow-ups** | ❌ Missing | Criar tabela `follow_ups` e lógica de mutex. |
| **Scheduling** | ✅ Schema 006 OK | Validar integração OAuth Google em `organizations`. |

---

## 3. DIRETRIZES DE EXECUÇÃO (ROADMAP)

### FASE 1: ESTABILIZAÇÃO DA INFRA (IMEDIATO)
*   **Ação 1.1**: Consolidar e aplicar o script SQL da **Migração 007**. Sem isso, o backend atual lançará exceções de `column not found` em 80% das rotas de webhook.
*   **Ação 1.2**: Implementar o `evolution.ts` utilizando o SDK da Evolution API para garantir que o `whatsapp_instances` reflita o estado real da conexão.

### FASE 2: INTELIGÊNCIA E CONTEXTO
*   **Ação 2.1**: Ativar o `RAGEngine`. Garantir que o `knowledge_files` (Schema 006) alimente corretamente o `rag_documents` (Schema 007) via embeddings (Ollama 768 dims conforme padrão).
*   **Ação 2.2**: Refinar o `replyGenerator.ts`. A lógica de injeção de contexto está sólida, mas precisa de validação de tokens em tempo real para evitar estouro de contexto no Gemma 4.

### FASE 3: FRONTEND E UX (CONEXÃO)
*   **Ação 3.1**: Mapear os endpoints de `inbox` e `crm` para os novos serviços. O frontend deve parar de consumir mocks e passar a refletir o `ConversationState`.
*   **Ação 3.2**: Implementar o Kanban de Vendas no CRM, utilizando o campo `stage` do lead para movimentação de pipeline.

---

## 4. CONCLUSÃO DA AUDITORIA

O sistema está **70% pronto no backend** e **30% pronto no frontend**. A fundação multi-tenant e o motor de tokens são o ponto mais forte. O ponto mais fraco é a dependência de migrações manuais e arquivos de integração vazios.

**Próximo passo sugerido:** "Arquiteto, sua prioridade zero é a execução da Migração 007 e a codificação do serviço de integração com a Evolution API. O sistema precisa 'falar' com o WhatsApp antes de refinarmos a IA."

---
*Relatório gerado por Manus AI — Chief Engineer Mode.*
