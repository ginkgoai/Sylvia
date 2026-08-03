# Checkpoint da Sylvia

> Atualizado em 2026-08-03. Leia depois de `00_INDEX.md` e antes de executar trabalho novo. A assistente foi renomeada: **Sexta-feira → Sylvia** (constituição nova em `../../SYLVIA.md`).

## Estado vivo

- **Papel da Sylvia:** inteligência executiva da holding (Ginkgo + Scale Group) — pensa e dirige como CEO; o fundador opera e decide como dono, com gates de autonomia (`cognicao/AUTONOMIA.md`). Assistente pessoal completa do fundador — estrategista, gestora e operadora privada da Ginkgo, com acesso contextual às ferramentas, serviços e à biblioteca de trabalho autorizados. Acesso não elimina confirmação para efeitos externos, gastos, publicação, deleção ou ação sobre cliente.
- **Topologia operacional:** `C:\sexta-feira` é o centro de comando e memória; `75_Studio` é agenciamento ativo de clientes, Ginkgo Motor e redes da Ginkgo; `C:\dev` é desenvolvimento, testes e produção.
- **Foco de produto:** LEAF é o produto recorrente; agência manual valida operações antes de PYRE/WAVE virarem SaaS.
- **Saída do LEAF:** o produto está no caminho de sair de testes para produção e receber usuários. Só considerar a transição concluída com prova de fluxo crítico, isolamento, observabilidade e operação de suporte.
- **LEAF/WhatsApp:** a cadeia QR → pareamento → mensagem → inbox → CRM ainda exige prova ponta a ponta com organização e número de teste. Não tratar botão, workflow publicado ou instância criada como sucesso.
- **Gabbih:** relatado como bot existente/online e SyncPay vinculado; fluxo de venda, webhook, acesso VIP, renovação e expiração continuam sem prova E2E. Operar manualmente, com conta de teste e evidência por etapa.
- **PYRE:** benchmark de referência StudioBanana foi salvo em `50_Plataformas/benchmark_studiobanana_pyre.md`. Aplicar somente princípios adaptados: job real, ativo versionado, aprovação humana e handoff verificável ao WAVE.
- **InfraNodus:** hipótese de integração futura somente como análise opt-in de lacunas de conhecimento/PYRE. Não substitui o RAG factual do LEAF nem recebe conversas brutas de tenants.

## Consolidação desta sessão (2026-08-03 — fundação da Sylvia)

- **Renomeação e constituição**: Sexta-feira → Sylvia. Constituição em `SYLVIA.md` (raiz) + adaptadores `AGENTS.md`/`SOUL.md`/`CLAUDE.md` + protocolos em `cognicao/` (memória, triagem de clippings, autonomia A0–A3, heartbeat).
- **Reorganização**: runtime legado (hermes, bridges, callima, db, dashboard-orb, memory) movido para `runtime/`; camada de negócio criada em `empresas/` (ecossistema Ginkgo + 10 perfis de produto + briefs fonte + Scale Group) e `operacao/` (contas/canais, financeiro). Mapa completo em `MIGRATION.md`.
- **Runtime alvo decidido**: OpenClaw (canais, heartbeat, skills); Claude Cowork/Code como oficina; n8n como automação determinística; Hermes em desativação (`runtime/openclaw/SETUP.md`).
- **Repo git `sylvia` criado** no centro de comando (commit de nascimento, ~1,5 mil arquivos, sem segredos; vip-gabi e zavan-landing seguem como repos independentes fora do índice). Push ao GitHub privado via `subir_github.ps1` (executar no Windows).
- Decisão registrada em `Decisoes/2026-08-03-sylvia-constituicao-e-repo.md`.

## Próxima sequência de maior retorno

1. Executar `subir_github.ps1`, confirmar o repo privado `sylvia` no GitHub e **revogar o PAT** usado (foi colado em chat).
2. Instalar OpenClaw e cumprir a Fase 1 da Sylvia (Telegram + boot + memória + heartbeat) — critério de pronto em `runtime/openclaw/SETUP.md`.
3. Gerar os dossiês comerciais a partir de `empresas/*/briefs_fonte/` (um por produto + ecossistema + Scale Group), com revisão do fundador.
4. Preparar a saída do LEAF para usuários: provar o QR ponta a ponta, isolamento por organização, suporte manual, logs e rollback antes de abrir acesso.
5. Triagem do backlog de clippings até zerar `00_Inbox` e depurar `20_Conhecimento/Referencias`; preencher `operacao/CONTAS_E_CANAIS.md`.

## Regras de atualização

- Atualize este arquivo ao final de uma sessão relevante.
- Diferencie sempre `comprovado`, `relatado` e `hipótese`.
- Não registre segredos, PII, links de pagamento, códigos de acesso ou dados de cliente.
