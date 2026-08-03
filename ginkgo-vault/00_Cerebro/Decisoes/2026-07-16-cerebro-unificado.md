# Decisão — cérebro unificado da Sexta-feira

- **Data:** 2026-07-16
- **Status:** confirmado pelo fundador
- **Decisão:** `C:\sexta-feira\ginkgo-vault\00_Cerebro\` é a fonte canônica da memória pessoal e operacional da Sexta-feira.

## Consequências

1. Checkpoint, handoff, conversas resumidas, decisões, insights e ledger vivem no cofre.
2. `C:\sexta-feira\memory\` permanece apenas para compatibilidade do Hermes/runtime até migração deliberada; não é mais a fonte de decisão nova.
3. Clippings entram como evidência externa, são destilados e movidos para temas; duplicatas, legado e material sensível não entram no contexto ativo.
4. Dados detalhados de cliente ficam na respectiva pasta de cliente, com leitura no escopo da tarefa. O cérebro e o RAG globais recebem apenas sínteses minimizadas; PII, chaves, tokens e segredos ficam fora do contexto global.
5. `75_Studio/` é a frente ativa de agenciamento, incluindo clientes, Ginkgo Motor e redes da Ginkgo; não deve ser tratado como arquivo de projetos paralelos.

## Critério de revisão

Rever esta decisão somente se uma migração do runtime Hermes exigir outra estrutura e houver plano de compatibilidade, backup e validação de leitura/escrita.
