# Auditoria Codex — 2026-07-15

Escopo: `C:\sexta-feira` e `C:\dev`, com foco em Sexta-feira, Ginkgo Tree, LEAF, Callima/ai-stack e landing `ginkgo-sale`.

## Resumo executivo

1. Tenho acesso local a `C:\sexta-feira` e `C:\dev`.
2. O tronco canônico do produto é `C:\dev\ginkgo-tree`. Ele está saudável em código: `pnpm test` passou `381/381`, `pnpm typecheck` passou, `pnpm build` passou.
3. O produto Ginkgo/Leaf está em estado de quase MVP técnico, mas não em produção completa. O que falta é prova operacional ao vivo: domínio/env final, e-mail transacional, Stripe live coerente, pareamento/uso real do WhatsApp no tronco, e alguns gates de acesso.
4. A Callima protótipo em `ai-stack` está viva: Docker rodando, n8n health OK, AnythingLLM OK, Evolution com uma instância `open`, workflows ativos incluindo Callima, áudio, mídia, Pix e Brann Actions Consumer.
5. `C:\dev\leaf` é doador/legado. Os próprios docs dizem que o schema/migrations eram incoerentes e que o alvo atual deve ser `ginkgo-tree`.
6. `C:\dev\ginkgo-sale` builda e tem teste mínimo verde, mas lint falha e `npm audit` acusa 20 vulnerabilidades, sendo 12 high e 1 critical.
7. Risco crítico de segredo: há exports JSON em `C:\sexta-feira\callima\leaf_dump` com credenciais hardcoded. Não estão necessariamente versionados, mas devem ser rotacionados e limpos.

## Inventário local

### `C:\sexta-feira`

Papel: memória, vault, specs, bridges e persona da Sexta-feira.

Principais partes:

- `README.md`: define Sexta-feira como orquestrador pessoal autônomo sobre Hermes Agent.
- `memory/`: estado/roadmap/learnings/env. Está desatualizado: `STATE.md` é de 2026-06-10.
- `docs/`: especificações de Ginkgo/Leaf/Pyre/Wave, handoffs, pricing e arquitetura.
- `hermes/skills`: skills customizadas para status, n8n e RAG.
- `bridges/n8n` e `bridges/rag`: clientes simples para n8n e AnythingLLM.
- `callima/`: scripts e dumps de workflows n8n.
- `ginkgo-vault/`: vault de conhecimento/branding/operação.

Estado honesto:

- Sexta-feira é mais "sistema cognitivo/memória/orquestração" do que produto runtime.
- A Fase 1 descrita no README ainda tem pendências: Hermes/provider/Telegram, n8n read-only, RAG, ponte Claude+MCP e Dashboard Orb.
- O handoff local diz que `ginkgo-tree` é o tronco canônico e `leaf` deve ser aposentado após portar UX.

### `C:\dev\ginkgo-tree`

Papel: tronco canônico do produto Ginkgo/Leaf.

Stack:

- Monorepo pnpm.
- `apps/api`: Fastify.
- `apps/web`: Next.js 14.
- `apps/worker`: BullMQ.
- `packages/core`: Kernel puro.
- `packages/boundary`: Security Boundary.
- `packages/db`: Prisma/Postgres.
- `packages/leaf`: skills e lógica de produto Leaf.

Git:

- Branch atual: `feat/whatsapp-connect-surface`.
- HEAD: `ba819ec`.
- `main` e `origin/main`: `194061c`, M5 activation self-serve.
- Branch atual parece local sem upstream direto.
- Working tree sem mudanças rastreadas; só artefatos ignorados (`.next`, `dist`, `node_modules`, `.env`, backups).

Verificação executada:

- `pnpm test`: passou `381/381`.
- `pnpm typecheck`: passou em todos os pacotes.
- `pnpm build`: passou, incluindo Next build de 59 páginas.
- `pnpm lint`: falhou.

Lint:

- Falha principal após build: `eslint .` varre `apps/web/.next`.
- Fonte-only ainda falha por plugins/regras ausentes (`@next/next/no-img-element`, `react-hooks/exhaustive-deps`) e alguns unused vars.
- Isso é dívida de DX/CI. Não bloqueou build/test, mas precisa ser arrumado.

Config:

- `.env` existe e está ignorado.
- `.env.example` tem variáveis ausentes localmente, incluindo `LEAF_DOMAIN`, `WEB_BASE_URL`, `RESEND_API_KEY`, `EMAIL_FROM`, `TUNNEL_TOKEN`, configs AnythingLLM e defaults.
- `docker-compose.prod.yml` não interpola hoje sem `LEAF_DOMAIN`.
- Supabase keys locais estão vazias no `.env`.

Riscos de produto/código:

- Gate de acesso para `subscriptionStatus` `suspended`/`canceled` está marcado como TODO em `packages/db/src/store.ts`.
- Ofertas aceitam qualquer URL `https://`, não apenas Stripe; o próprio comentário em `apps/api/src/routes/offers.ts` diz que validar "é Stripe" ficou para fatia futura.
- Billing tem código forte e idempotente, mas docs ainda registram prova-pendente de Stripe live/Payment Links/env.
- CI cobre build/typecheck/test e integração Postgres/Redis, mas não cobre n8n/Evolution/WhatsApp live nem lint.
- Observabilidade/realtime ainda é polling; SSE está ausente.
- ChannelPort/Cloud API oficial ainda pendente; risco Baileys continua existencial.

### `C:\dev\ai-stack`

Papel: runtime local/protótipo vivo da Callima e serviços adjacentes.

Serviços Docker ativos:

- `ai-stack-n8n`: health OK em `/healthz`.
- `ai-stack-evolution`: Evolution API v2.3.7, uma instância aberta.
- `ai-stack-anythingllm`: `/api/ping` OK.
- `ai-stack-postgres`, `ai-stack-redis`: healthy.
- `ai-stack-postiz`, `ai-stack-temporal`.

n8n:

- Logs mostram cinco workflows ativos: Callima, Pix, envio de mídia, áudio feminino e Brann Actions Consumer.
- Compose local está modificado: n8n main mudou de queue para regular, com worker ainda presente.
- Imagem no container é `n8nio/n8n:latest` e log mostra versão 2.23.4, enquanto alguns docs antigos falam em outra versão.
- API n8n via chave configurada falhou nesta auditoria; health do serviço está OK.

Git:

- `docker-compose.yml` modificado.
- Muitas deleções rastreadas em `ginkgo-vault/*`.
- Antes de qualquer push neste repo, revisar com cuidado: há risco de perda acidental de vault.

Riscos:

- `latest` em n8n aumenta risco de drift.
- Worker n8n roda, mas main está em modo regular; documentação e runtime divergem.
- Logs mostram erros temporários de banco no boot, depois recuperação.
- `.env` tem chaves reais e backups `.env.bak-*` ignorados. Precisa higiene/rotação.

### `C:\dev\leaf`

Papel: repo LEAF separado, hoje legado/doador.

Git:

- Branch atual: `feat/pricing-gtk`.
- Tem `.claude/` untracked.
- Sem `node_modules`.

Estado:

- Docs do próprio repo dizem que o DB nunca foi integrado de forma coerente, migrations antigas foram quebradas e conceitos de tenant/org estavam misturados.
- Isso confirma que não deve ser tratado como tronco de produção.
- Valor atual: doador de UX, páginas, specs e ideias que ainda não foram portadas.

### `C:\dev\ginkgo-sale`

Papel: landing/site Ginkgo.

Verificação executada:

- `npm ci`: passou, mas acusou 20 vulnerabilidades.
- `npm run build`: passou.
- `npm run test`: passou 1 teste.
- `npm run lint`: falhou com 4 erros e 9 warnings.

Riscos:

- `npm audit`: 1 critical e 12 high. Critical em `vitest`; high em Vite, React Router, Rollup, lodash, minimatch/picomatch, form-data, etc.
- README ainda é template Lovable e não documenta o projeto real.
- Cobertura de teste é praticamente simbólica.

## Achados priorizados

### P0 — antes de expor para cliente/pagante

1. Rotacionar credenciais hardcoded em exports da Callima.
   - Encontrado em `C:\sexta-feira\callima\leaf_dump\pix_link.json`.
   - Encontrado em `C:\sexta-feira\callima\leaf_dump\Callima.json`.
   - Ação: revogar/rotacionar no provedor, mover para credencial n8n/cofre, reexportar sem valores.

2. Fechar configuração mínima de produção do `ginkgo-tree`.
   - Faltam `LEAF_DOMAIN`, `WEB_BASE_URL`, `RESEND_API_KEY`, `EMAIL_FROM`, `TUNNEL_TOKEN` e configs relacionadas.
   - `docker-compose.prod.yml` não sobe sem isso.

3. Provar o caminho vivo do tronco, não só do protótipo.
   - Hoje `ai-stack` está vivo, mas `ginkgo-tree` não está rodando.
   - Rodar compose de `ginkgo-tree`, provisionar secrets, testar health, signup, connect, webhook, Stripe webhook e fluxo Leaf.

4. Implementar gate de acesso para assinatura suspensa/cancelada.
   - Código marca `subscriptionStatus='suspended'`, mas o TODO diz que preHandlers/middleware ainda não restringem o workspace.

5. Resolver higiene do `ai-stack` antes de qualquer commit/push.
   - `docker-compose.yml` alterado.
   - Deleções rastreadas no vault.
   - Decidir se o compose regular-mode é intencional e documentar.

### P1 — MVP sólido

1. Arrumar lint do `ginkgo-tree`.
   - Ignorar `.next/dist`.
   - Instalar/configurar plugins de Next/React Hooks ou remover regras inválidas.
   - Limpar unused vars.

2. Provar Stripe live.
   - Alinhar Payment Links live, webhook live, `STRIPE_WEBHOOK_SECRET`, domínio público e Resend.
   - Rodar assinatura -> webhook -> tenant -> magic link -> grant GTK.

3. Validar ofertas.
   - Hoje qualquer `https://` entra como payment link.
   - Validar domínio/padrão Stripe ou separar "paymentLink" provider-specific.

4. Fixar versões no `ai-stack`.
   - Trocar `n8nio/n8n:latest` por versão pinada.
   - Atualizar README/compose para o modo real.

5. Criar smoke e2e versionado do `ai-stack`.
   - Health, workflows ativos, Evolution open, AnythingLLM OK, execução Callima controlada.

### P2 — limpeza/organização

1. Arquivar ou congelar `C:\dev\leaf` como doador legado.
2. Atualizar `C:\sexta-feira\memory\STATE.md` e handoffs, que estão datados.
3. Corrigir README do `ginkgo-sale`.
4. Resolver lint e audit do `ginkgo-sale`.
5. Criar mapa oficial: `ginkgo-tree` = produto, `ai-stack` = runtime/protótipo, `sexta-feira` = cognição/memória, `leaf` = legado, `ginkgo-sale` = site.

## Conclusão

O estado é melhor do que "caos de MVP": existe um tronco tecnicamente forte (`ginkgo-tree`) com Kernel/Boundary/billing/Leaf bem testados, e existe uma Callima viva no `ai-stack`.

O gargalo não é mais "construir a ideia". O gargalo é convergir operação: segredos, domínio, live payments, prova do tronco rodando, limpeza de repos legados e remoção de riscos óbvios antes de cliente pagar depender disso.

