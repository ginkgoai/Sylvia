# Portfólio de Agent Skills — curadoria pro Ginkgo

Garimpado de awesome-skills.com + coleções GitHub (anthropics/skills [oficial], ComposioHQ,
travisvn, heilcheng, sickn33/antigravity = agregador de 1.555). [O]=oficial Anthropic · [C]=comunidade.
Padrão de uso: como a skill `ginkgo` que criamos — colocar SKILL.md em `.claude/skills/` do tronco.

## Top 8 pra adotar primeiro
1. **n8n Workflow Skills + n8n-MCP** [C] — backbone da Callima/Brann (n8n). Endurece a automação.
2. **stripe-best-practices** [C] — destrava o billing tokenizado (GTK) — casa com o pricing.
3. **frontend-design** [O] — salto de qualidade de UI nos 3 apps (anti "AI-slop").
4. **next-best-practices + mcollina (Fastify/Node)** [C] — exatamente nosso stack (apps/web + api).
5. **Security Review** [O] (claude-code-security-review) — gate de segurança no CI (governança/Laplace).
6. **remotion** [C] — motor de vídeo/clipes do Pyre (React → vídeo).
7. **claude-d3js / d3** [C] — gráficos do Wave (atribuição) e dashboards do Leaf.
8. **firecrawl** [C] — scraping/pesquisa pra Trends do Pyre e intel de concorrente do Wave.

## Por bucket (relevantes)
- **Leaf/WhatsApp:** n8n-skills, n8n-MCP, courier (notificações multicanal), claude-memory (memória de lead).
- **Pyre:** remotion (vídeo), fal-generate/upscale (imagem/vídeo via fal.ai), openai sora/speech (ref TTS/clip), typefully/social-content (agendamento), frontend-slides.
- **Wave:** agent-gtm-skills (18 skills GTM/ads), ai-seo/page-cro/copywriting (criativo+CRO).
- **Governança/Segurança:** Security Review [O], Trail of Bits static-analysis, Better Auth (2FA), Karpathy guidelines (guardrail de edição).
- **Dev/Qualidade:** next/react-best-practices, mcollina (Fastify), webapp-testing [O] (Playwright), getsentry (review/bugs).
- **Design/Front:** frontend-design [O], shadcn skills, web-artifacts-builder [O], Interface Design (memória de design).
- **Office/Docs:** docx/pptx/xlsx/pdf [O], doc-coauthoring [O].
- **Data:** claude-d3js, duckdb, tinybird (analytics realtime — padrão p/ uso tokenizado/ads).
- **SEO/Research:** Claude SEO (19 sub-skills), sanity seo-aeo, firecrawl.
- **Payments/Ops:** stripe-best-practices, composio (1000+ apps com auth gerenciada).

## Já temos (não readotar) — built-ins Anthropic
docx · pptx · xlsx · pdf · mcp-builder · skill-creator · canvas-design · web-artifacts-builder.

## Riscos (vetar antes de instalar) — comunidade ≠ confiável por padrão
- **Claude SEO** lê credenciais Google/Moz/GA4. **firecrawl/notebooklm** fazem chamadas externas/cookies.
- **antigravity-awesome-skills** (1.555) é AGREGADOR — autor diz "não seguro por padrão"; usar como
  índice de descoberta, cherry-pick, nunca bulk-install.
- Regra Ginkgo: skill de terceiro que toca segredo/efeito externo entra só revisada e, idealmente,
  atrás do nosso Boundary (ADR 0002: MCP percebe, Skill age).

## Como agregar (recomendação)
Não instalar em massa. Escolher 4–6 do Top 8, revisar o SKILL.md, e colocar em `.claude/skills/`
do tronco (como a skill `ginkgo`). Começar pelas que destravam o que já está em obra:
n8n-skills (Callima), frontend-design + next/Fastify (repaginação do tronco), stripe (billing).


---
## Lote 2 — verificação (repos do fundador)
ADOTADOS como skill no tronco:
- **wave-ads** (`.claude/skills/wave-ads`) — auditoria+estratégia+execução de ads, governada.
  Minera: claude-ads (auditoria, MIT, limpa), ai-ads-claude (estratégia), ads-mcp (design de execução).
- (já antes) **motion** (LottieFiles) e **pyre-avatar** (HeyGen, governado).

REFERÊNCIAS de arquitetura (NÃO rodar — têm loop/efeito próprio, conflitam com nosso Kernel/Boundary):
- **SalesGPT** [MIT] — máquina de estados de venda (intro→qualify→close) p/ Leaf/Callima. Gera Stripe
  sozinho → só referência.
- **ViMax** [MIT, ~8k★] — pipeline de vídeo (script→storyboard→consistência) p/ Pyre. Chama Veo pago +
  orquestra sozinho → referência; se adotar, embrulhar cada passo como Task com GTK.
- **CrewAI** [MIT] — orquestrador concorrente; já temos o runtime do ginkgo-tree → só referência de padrões.

MINERAR templates: ai-marketing-claude (email/calendário/copy → Pyre), ai-ads-claude (personas/funil/budget → Wave).
ÍNDICE: awesome-ai-agents-2026 (CC0, manter como sourcing). PULAR: e2b/awesome-ai-agents (fora de domínio).

Regra reforçada: efeito externo/pago/segredo ou loop de agente próprio = NÃO adotar como skill solta;
ou vira referência, ou entra como Skill governada atrás do Boundary (Task+GTK+Evidence).
