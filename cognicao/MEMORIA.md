# Protocolo de memória da Sylvia

> A memória canônica vive em `ginkgo-vault/00_Cerebro/`. Este protocolo define como ela cresce sem virar ruído.

## Camadas

| Camada | Onde | O que guarda |
|---|---|---|
| Sessão | contexto do runtime | Trabalho em andamento. Volátil. |
| Estado vivo | `00_Cerebro/CHECKPOINT.md` + `HANDOFF.md` | Onde paramos, próxima ação, pendências. |
| Diário | `00_Cerebro/CONTEXT_LOG.md` | Uma linha por evento relevante, com data. |
| Decisões | `00_Cerebro/Decisoes/AAAA-MM-DD-titulo.md` | Decisões confirmadas pelo fundador. Imutáveis; revogar = nova decisão. |
| Insights | `00_Cerebro/Insights/` | Teses reutilizáveis destiladas de evidência ou clippings. |
| Conversas | `00_Cerebro/Conversas/` | Resumos sanitizados de conversas importantes. |
| Ledger | `00_Cerebro/LEDGER.jsonl` | Trilha append-only: `observation`, `learning_candidate`, `confirmed_learning`, `action`. |
| Biblioteca | demais pastas do vault | Conhecimento temático refinado e material de trabalho. |

## Regras de escrita

1. **Fonte, data e escopo sempre.** Registro sem fonte é hipótese e deve ser marcado como tal.
2. **Estados**: `Comprovado` (fonte verificável atual), `Relatado` (dito, não verificado nesta sessão), `Hipótese` (interpretação a validar), `Arquivado` (não guia mais ação).
3. **Promoção, nunca teleporte.** Clipping/conversa → hipótese → (evidência ou confirmação do fundador) → decisão ou insight canônico. Ver `TRIAGEM_CLIPPINGS.md`.
4. **Sanitização.** Nada de segredos, tokens, PII ou transcrição bruta de cliente na memória global — só síntese operacional: decisão, status, risco, próxima ação.
5. **Fechamento de sessão** relevante: atualizar `CHECKPOINT.md` e `HANDOFF.md`; registrar no `CONTEXT_LOG.md`; decisões novas em `Decisoes/` + `confirmed_learning` no ledger.
6. **Legado**: `runtime/hermes/memory-compat/` (ex-`memory/`) é compatibilidade do Hermes. Não escrever memória nova lá.

## Consolidação (anti-entropia)

No heartbeat semanal: fundir duplicatas, marcar `Arquivado` o que envelheceu, atualizar índices (`00_INDEX.md`), verificar que decisões recentes têm registro e que o CHECKPOINT reflete a realidade. Memória que contradiz evidência atual é corrigida com nota, nunca apagada silenciosamente.
