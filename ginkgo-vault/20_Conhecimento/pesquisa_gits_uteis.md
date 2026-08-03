# Pesquisa de GitHubs úteis — onboarding-tour + stack outbound/CRM (2026-07-06)

> Garimpo pro cenário Ginkgo (Next 14 + React). Foco: o "tutorial que escurece e centraliza a tela" que o fundador lembrava + libs/refs úteis pro Lead Finder, kanban, editor de campanha, envio e inbox. ⚠️ Licenças verificadas onde possível — **confirmar antes de embutir** (AGPL contamina produto fechado; alguns exigem licença comercial).

## A. Onboarding "tour" (escurece + spotlight no elemento) — O QUE VOCÊ LEMBRAVA
| Lib | Repo | ⭐ | Licença | Nota |
|---|---|---|---|---|
| **Driver.js** ✅ | `kamranahmedse/driver.js` | ~25,5k | **MIT** | **5KB**, vanilla (roda em React), spotlight + overlay escuro + popover. O mais leve. **É provavelmente o que você viu — e o que eu recomendo** (MIT, sem pegadinha). |
| **Intro.js** ⚠️ | `usablica/intro.js` | ~23,6k | **AGPL + licença COMERCIAL paga** | O "padrão da indústria" (o clássico escurece-e-centraliza). **Pegadinha: uso comercial exige licença paga.** Evitar a menos que compre. |
| **react-joyride** | `gilbarbara/react-joyride` | ~7,7k | **MIT** | O mais popular em React (~340k installs/semana). Mais pesado (~34KB). Nativo React. |
| **Onborda** | `uixmat/onborda` | menor | MIT | **Next.js + Tailwind + Framer Motion** — casa com o "modo Pierre" (motion). Bom se quiser tour animado on-brand. |
| **NextStep** | `nextstepjs/nextstep` | menor | MIT | Idem, Next.js App Router + Framer. Alternativa ao Onborda. |
> **Recomendação:** **Driver.js** (MIT, 5KB, exatamente o efeito) pro genérico; ou **Onborda/NextStep** se quiser o tour animado no registro modo-Pierre. **Fugir do Intro.js** (licença comercial). Obs.: benchmark aponta que várias dessas têm violações ARIA (WCAG) — cuidar acessibilidade.

## B. Kanban / drag-and-drop (o board da CRM)
| Lib | Licença | Nota |
|---|---|---|
| **dnd-kit** (`clauderic/dnd-kit`) | MIT | Padrão moderno de DnD em React (leve, acessível). Provável base do nosso `KanbanBoard` atual. |
| **@hello-pangea/dnd** | Apache-2.0 | Fork MANTIDO do `react-beautiful-dnd` (que foi arquivado). Kanban "estilo Trello" pronto. |
| **@caldwell619/react-kanban** | MIT | Board kanban quase pronto (colunas+cards). Bom pra protótipo rápido. |

## C. Editor de e-mail da campanha (corpo + variáveis) — o do print do Mailerfind
| Lib | Repo | Licença | Nota |
|---|---|---|---|
| **Maily.to** ⭐ | `arikchakma/maily.to` | Open-source (MIT) | **Bingo:** editor de e-mail WYSIWYG em **Next.js + Tiptap + React Email**, com **variáveis**, componentes prontos, render cross-client. É literalmente o "corpo do email + {{variáveis}} + modelos" que vimos. **Melhor ref pro nosso editor de campanha.** |
| **React Email** | `resend/react-email` | MIT | Componentes de e-mail + Editor novo. Casa com o **Resend** (que já usamos). |
| **Tiptap** | `ueberdosis/tiptap` | MIT (core) | O rich-text por baixo do Maily; mentions/variáveis, extensível. |

## D. Motor de envio / newsletter (referência p/ o outbound-email)
| Lib | Licença | Nota |
|---|---|---|
| **Listmonk** ⭐ (`knadh/listmonk`) | AGPL | Self-hosted, **1 binário Go**, dashboard moderno, 100k+ contatos num VPS de $10. **Melhor ref** de motor de listas/envio + painel. (AGPL: usar como serviço/ref, não copiar código pro nosso fechado.) |
| **Keila** | AGPL | Newsletter em Elixir, foco privacidade/EU. |
| **Mautic** | GPL | Automação de marketing completa (pesada) — CRM + landing + workflow visual. "Quando o Listmonk não basta". |
| ⚠️ **Entrega:** todos precisam de **SMTP relay** (Amazon SES / Postmark / Mailgun) pra caixa de entrada + **warmup**. É o requisito de deliverability que registramos no spec outbound. |

## E. Inbox unificada / IA de e-mail (a "Caixa de Entrada Unificada" do Mailerfind)
| Lib | Licença | Nota |
|---|---|---|
| **Inbox Zero** (`elie222/inbox-zero`) | AGPL (confirmar) | Assistente de IA pra Gmail/Outlook: automações, unsubscribe em massa, **bloqueia cold email**, analytics. Ótima ref de **inbox + IA de triagem** (e de como o "outro lado" barra cold — bom pra calibrar deliverability). |

## F. CRM open-source de referência (produto inteiro + kanban) — OURO
| Lib | Repo | ⭐ | Licença | Nota |
|---|---|---|---|---|
| **Twenty** ⭐⭐ | `twentyhq/twenty` | ~44k | AGPL | "O CRM open-source #1, feito pra IA." React + NestJS/GraphQL, **cada objeto vira tabela OU kanban de pipeline**, workflows, self-host Docker. **Melhor referência viva** de UX de CRM + kanban + "designed for AI". (AGPL: referência/estudo, não fork no produto fechado.) |
| **Atomic CRM** | `marmelab/atomic-crm` | — | MIT | React + **shadcn/ui + Supabase** (nosso stack antigo do leaf), pipeline kanban, import/export. Mais leve; MIT = pode reusar código. |

## Alerta de licença (governança)
- **Embutir no nosso produto (fechado):** só **MIT/Apache** (Driver.js, react-joyride, dnd-kit, hello-pangea, Maily, React Email, Tiptap, Atomic CRM, Onborda, NextStep).
- **AGPL/GPL (Twenty, Listmonk, Keila, Mautic, Inbox Zero):** ótimos como **referência de UX/arquitetura** e como serviço self-hosted separado, mas **NÃO copiar código pro trunk fechado** (copyleft contamina). 
- **Intro.js:** uso comercial = **licença paga** → preferir Driver.js.

## Fontes
- React tour benchmark 2026 — usertourkit.com/blog/react-tour-library-benchmark-2026
- npmtrends: driver.js vs intro.js vs react-joyride
- Twenty CRM — github.com/twentyhq/twenty
- Atomic CRM — github.com/marmelab/atomic-crm
- Maily.to — github.com/arikchakma/maily.to
- Listmonk — github.com/knadh/listmonk · listmonk.app
- Inbox Zero — getinboxzero.com
