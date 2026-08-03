# Spec — fatia `feat/ui-consistency` (clash de tema / contraste)

> Diagnóstico medido ao vivo no browser (WCAG sweep + `elementsFromPoint` pro fundo visual real), 2026-06-27. Vira a spec da fatia. honest-data: medido, não chutado.

## Sintoma
"UI estranha e não funcional" — texto **ilegível** em vários pontos, pior no **balão do Brann** (resposta quase invisível).

## Causa raiz (medida)
A app renderiza num **`body` CLARO** (`rgb(246,245,242)` / `#f6f5f2`) com várias **superfícies claras órfãs** (`.card`≈`rgb(240,240,240)`, bolha do Brann≈bege `rgb(232,230,225)`, chips de filtro), **mas o texto é BRANCO** (`#fff`) — herança do tema escuro. Onde um container **escuro** cobre (chrome, item selecionado = `rgb(14,20,34)`), funciona; onde a superfície clara vaza, vira **branco-em-claro = invisível.**
→ É o clash dos **dois sistemas de estilo**: `global.css` (claro: `.card/.btn/.pill`) × Tailwind+tokens (escuro). O tema pretendido é **ESCURO** (o chrome e o selecionado já são).

## Confirmados quebrados (fundo visual real, não DOM-walk)
| Onde | Texto (fg) | Fundo real (bg) | Ratio | AA? |
|---|---|---|---|---|
| **Balão do Brann** (a resposta "Olá! Sou o Brann…") | `255,255,255` | bege `232,230,225` | **1.25** | ✗ (precisa 4.5) |
| `Brann` / `oi` (labels no balão) | `255,255,255` | `255,255,255` | **1.0** | ✗ |
| Cards de inbox **não-selecionados** (Dr. Paulo, Ricardo) | `255,255,255` | `240,240,240` | **1.14** | ✗ |
| Chips de filtro (`Novos/Meus/IA/Resolvidas`) | `138,147,168` | `240,240,240` | **2.7** | ✗ |
| Preview "IA: …" nos cards | `138,147,168` | `240,240,240` | **2.7** | ✗ |
| `Nyra · em breve` / `Alfred · em breve` / rodapé "Conteúdo gerado por IA" | `154,163,172` | claro `255` | **2.56** | ✗ |
| *(controle) Item selecionado / chrome / "Caixa de entrada"* | `255,255,255` | escuro `14,20,34` | *ok* | ✅ |

Sweep total: **36 combinações** abaixo de AA. As de cima são as reais de alto impacto.

## Fix (direção)
**Consolidar TUDO no tema escuro que já domina** — não inventar tema novo.
- Eliminar os `#f6f5f2` / `#f0f0f0` / bege **órfãos**; alinhar `body`, `.card`, `.pill`, **`AgentBubble` (balão do Brann)**, chips de filtro e rótulos "em breve"/rodapé aos **tokens escuros existentes**.
- Texto claro em superfície escura, **AA ≥ 4.5:1** em todas as telas (Visão geral · Inbox · CRM · Agenda · Ofertas · Planos · balão).
- Balão: bolha Brann × usuário **distintas mas ambas legíveis**; `N tokens · ver tarefa →` clicável e legível.

## Aceite
- Zero texto < AA nas 6 telas + balão (re-rodar o sweep).
- **Gate de contraste no CI** (trava regressão futura).
- Render tests verdes · honest-data intacto · branch `feat/ui-consistency` → CI verde → merge.

## Nota
O **backend do Brann está perfeito** (resposta real via OpenRouter, estado real percebido, tarefa auditável). Isto é 100% camada de tinta — não tocar na lógica.

_Medido e mantido pela Sexta-feira._
