# Conversas recentes da Sexta-feira — resumo preservado

> Fonte: conversas Codex no diretório `C:\sexta-feira`, consultadas em 2026-07-16. Isto é um resumo de decisões e evidências, não uma cópia de transcrições.

## Auditoria Sexta-feira e dev

- A prioridade separa **Sexta-feira** (cognição/operação) de **Ginkgo Tree** (produto e testes em `C:\dev`).
- O LEAF deve ser tratado como CRM operacional, sem estados falsos, texto técnico na interface ou automação não provada.
- Critério de sucesso do canal: preparar, aprovar, QR real, parear número de teste, receber mensagem, refletir na inbox e criar/atualizar o lead certo com rastreabilidade e sem expor segredo.

## Operação manual Gabbih

- Diretriz: validar manualmente receita, entrega e suporte antes de criar SaaS ou automação nova.
- Estado relatado: bot Gabbih existe/está online, bot é administrador dos canais e SyncPay foi vinculado; isto não prova checkout, webhook ou acesso VIP.
- Ordem válida: fluxo `start` → planos → checkout → webhooks → teste de baixo risco → conciliação → renovação/expiração → tratamento manual de falha.
- Victoria permanece separada até o fluxo Gabbih estar provado.

## Engenharia reversa PYRE

- O benchmark StudioBanana foi armazenado em `50_Plataformas/benchmark_studiobanana_pyre.md`.
- Princípio adotável: PYRE cria e versiona ativos; o humano aprova; WAVE recebe somente um handoff rastreável. PYRE não publica nem mede mídia por conta própria.

## Regra de memória

- Conversas passam a ser reduzidas a decisões, fatos observados, pendências e fontes; transcrições integrais só devem ser mantidas quando houver necessidade explícita e forem seguras.
