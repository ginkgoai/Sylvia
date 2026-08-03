# Prompt — Composer humano (envio real pelo atendente) · tronco ginkgo-tree

Cole no Claude Code (repo ginkgo-tree) DEPOIS do Kanban.

---
**Tarefa: habilitar o envio humano real no composer da Inbox.** Siga as skills `ginkgo`, `motion`,
`frontend`, `fastify`, `n8n`, `security-review`. Arquitetura §1.2; honest-data é lei.

1. **Branch:** `feat/composer-humano` a partir de `feat/polish-aa` (tip atual do tronco: já inclui
   Kanban + AA dos eyebrows + skills commitadas). **Exija working tree limpo antes** (`git status`
   sem modificações — ver nota de restauração no handoff). Local, sem push.

2. **Objetivo:** quando a conversa está em controle humano (após "Assumir", status=human) e o canal está
   conectado, o atendente digita no composer e a mensagem **vai de verdade pro cliente no WhatsApp**.

3. **Reusar o caminho de envio existente** (a Skill de reply do BRANN: n8n whatsapp-send + Evolution +
   confirmador independente). NÃO criar caminho novo. O envio humano é uma **Task governada** pelo
   Boundary (executor_ref assinado, evidência = confirmação do envio), `sender_type=human_agent`.
   **Sem LLM** (texto do humano) → não debitar GTK de modelo (só infra, se houver).

4. **Honest-data (crítico):** a bolha OUT só aparece como **enviada** após a confirmação do envio
   (Evidence/confirmer). Antes disso, estado "enviando"; em falha, estado de erro + retry. NUNCA
   sintetizar bolha "enviada" sem confirmação.

5. **Gating:** composer só habilita quando status=human E o número do tronco está pareado/conectado
   (checar via /channels/whatsapp/status). Se não pareado/conectado, composer fica desabilitado com
   microcopy honesta ("conecte o WhatsApp para responder"). Anexo/emoji/áudio seguem "em breve".

6. **Persistência:** gravar a mensagem (tabela messages, sender_type human_agent), atualizar
   last_message/atendimento da conversa. org sempre do JWT; 404 cross-tenant.

**Dependência do fundador:** parear o WhatsApp do tronco (Evolution :8081) escaneando o QR — sem isso o
envio não sai ao vivo, mas o código deve funcionar quando pareado (gated no status).

**Aceite:** com número pareado, digitar+enviar → mensagem sai pela Evolution, persiste, bolha confirma;
sem pareamento, composer desabilitado com nota honesta; tsc+build+lint verdes; honest-data; mantenha local.
---
