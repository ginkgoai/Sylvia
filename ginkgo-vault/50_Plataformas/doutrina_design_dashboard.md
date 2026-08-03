# Doutrina de Design — Dashboard (adopt-list)

> 2026-07-01. A dashboard **warm/honest-data é o ATIVO** (identidade: Helena CRM + Chatwoot inbox + estados honestos, já lapidada e AA-auditada). Primitivos são **encanamento trocável** por baixo — mesma lógica do IA↔sistema. Claude Code (Fable) = produção; Lovable/V0/Figma = só exploração. Fontes: clipps de design (shadcn dashboard starter, react-bits, best-of-react, "Figma vs Lovable vs V0 vs Claude Code", CRM OSS 2025).

## Manter (não trocar)
- **DS de tokens** (theme.css v4 + global.css v2, warm verde/creme) — é a cara do produto. Twenty (DS+framework custom) prova o custo: "base enorme" + onboarding difícil; nós não pagamos esse imposto **nem** viramos genéricos.
- **Loop de produção:** Fable constrói o código real + lente de auditoria + QA-gate. (LogRocket: Claude #1 SWE-bench + único com análise de bundle/a11y; Lovable/v0 = "limitados" em a11y/performance.)

## Adotar seletivamente (own-the-code, sob NOSSOS tokens) — fatia FUTURA, pós-core
- **Radix/shadcn primitives** (via CLI, estilizados com nossos tokens): command palette, dropdown, dialog, popover, tooltip, combobox — a11y + teclado de graça (não é dependência; o código vive no nosso repo).
- **TanStack Table + Query + Nuqs:** CRM/inbox com filtro/busca no URL + cache de server-state → **mata o jank de polling**.
- **Recharts** (já adotado): KPIs honestos do dashboard.
- **Framer Motion** (já usamos) + **react-bits**: flourishes pontuais (empty-state/hero); shadcn-CLI, não briga com o DS.

## NÃO fazer
- Adotar o starter shadcn inteiro (Kiranism) ou **trocar o DS** → jogaria fora a lapidação e fragmentaria a identidade (o "AI slop" que a skill frontend-design alerta).
- Shippar código de protótipo (Lovable/V0) sem refino humano + marca + a11y.

## Padrões de UX a incorporar (batem em lacunas nossas)
notification center (badge→popover→página) · tabelas com estado no URL · **parallel routes** (isola loading por seção — o que nos mordeu no inbox-resilience) · theme switcher (dark #39) · org-switcher/plan-gating (já temos) · command palette (já temos).

> Vira uma **fatia de lapidação do Fable QUANDO o core (áudio/RAG/handoff/pix) fechar**. A dashboard atual já está demo-ready.
