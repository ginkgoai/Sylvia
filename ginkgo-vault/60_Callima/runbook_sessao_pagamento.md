# Runbook — Sessão Pagamento da Callima (executar em janela ESTÁVEL)

> Objetivo: a Callima passa a **mandar link de pagamento na conversa** e fechar venda.
> Pré-condições: conexão das ferramentas **sem flap** (não executar com DC piscando) · **backup da Callima antes de tudo** · pix_link já provada (`pixLink0GINKGO01`).
> Regra: **test-first**. A viva só muda depois de validado. Se quebrar → restaura backup.

## 0. Backup (sempre primeiro)
- `docker exec ai-stack-n8n n8n export:workflow --id=zo9FqQ9XVRcU8AJZ --output=/tmp/callima_bkp.json` → copiar pro host.

## 1. pix_link tool-ready
- Trocar **Manual Trigger → "When Executed by Another Workflow"** (executeWorkflowTrigger).
- Inputs declarados: `amount, name, cpf, email, phone, description`.
- (Config node já tem as creds SyncPay; o trigger passa a receber os campos do agente.)

## 2. Callima — adicionar a tool
- Nó **`@n8n/n8n-nodes-langchain.toolWorkflow`** `pix_link_tool`:
  - `workflowId = pixLink0GINKGO01`
  - input map: `amount,name,cpf,email,phone,description` ← do agente
  - **description (pro LLM):** "Gera link de pagamento Pix (copia-e-cola). Use SÓ quando o cliente confirmar que quer pagar/assinar. Requer nome completo, CPF, email, telefone e valor (R$). Devolve `pix_code`. NUNCA afirme que o pagamento foi confirmado — só envie o código."
  - conexão **ai_tool → agente Callima** (mesmo padrão de `base_conhecimento_callima`/MIDIA).

## 3. systemMessage — bloco "FLUXO DE PAGAMENTO"
- Plano pronto → link Stripe (quando existir). Projeto sob medida → sinal **R$100** via `pix_link`.
- Antes de chamar `pix_link`: garantir **nome + CPF + email + telefone** (pedir só o que faltar, 1 por vez, tom humano).
- Chamar `pix_link` → enviar o `pix_code` → "é só pagar que eu já começo 🌱".
- **honest-data (lei):** NUNCA "pagamento confirmado" sem o webhook real. Parabeniza só após confirmação.

## 4. Aplicar na viva (o "versioning dance")
1. Salvar no canvas → **`publish:workflow`** (ou publicar na UI).
2. `UPDATE workflow_history SET nodes=(SELECT nodes FROM workflow_entity WHERE id='zo9FqQ9XVRcU8AJZ') WHERE "versionId"=<activeVersionId>` (o main executa a versão publicada, não o draft).
3. **Restart** n8n.
4. **Testar:** POST manual no webhook OU WhatsApp real → "quero o projeto" → Callima pede os dados → gera `pix_code`.
5. Quebrou? → `import:workflow` do backup + publish + restart.

## 5. Webhook receiver (loop de confirmação)
- Novo workflow n8n: **Webhook trigger** (`/syncpay-cb`) → valida `identifier` + `status` → se `paid`: dispara a confirmação.
- **Precisa URL pública** (SyncPay chama de fora). Local não tem → expor via túnel OU na migração VPS. Estrutura pronta agora, exposição real depois.

## 6. Loop "pagou → parabeniza"
- webhook `paid` → registra → Callima **parabeniza + onboarding** (pede os dados pra começar). honest-data: só aqui.

---
### Notas
- Creds SyncPay já vivem no Config do `pix_link` (rotacionar = re-editar o Config; nunca ecoar).
- **Caveat de deploy do tronco** (achado na verificação 9b60994): rodar dedup `(org_id, phone)` **antes** do unique index em DB já populado.
- Bridge `Callima → POST /ingest/lead`: endpoint pronto e verificado (8/8). Fiar junto nesta mesma sessão (a Callima já está aberta) — token por-org via `scripts/put-ingest-token.ts`.

_Mantido pela Sexta-feira. Executar quando a conexão estiver firme._
