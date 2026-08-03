# Benchmark + Reverse — Mailerfind (2026-07-06)

> `app.mailerfind.com`. Fundador curtiu design/onboarding/funcionalidades. Teardown e engenharia-reversa pro cenário Ginkgo (Lead Finder + outbound + PYRE + WAVE + Callima). Sediada em Andorra; +200k empresas / +16k clientes; plano free sem cartão; afiliado 20%.

## 1. O que é
**Plataforma de geração de leads via Instagram + cold email.** "Get qualified leads from Instagram." Motion:
1. Escolhe uma **conta-alvo do IG** (concorrente / influencer / do nicho).
2. **Scan** dos seguidores (ou following/comentaristas/localização/hashtag) → extrai **dado público**: nome, email, telefone, localização.
3. **IA gera o email** personalizado com base no **seu site/negócio** (variantes + variáveis).
4. **Envia em escala** pelo email sender próprio (Gmail/Outlook/SendGrid/SMTP) com **warmup + tech de deliverability** (cair na inbox, não no spam).
5. Alternativa: **sobe a lista pro Meta Ads** (Custom/Lookalike audiences).
- **Âncora de venda matadora:** "lead a €0,10 vs €8–15 no Meta Ads." "sem tocar na sua conta, sem bots, sem risco de ban" (scraping da infra deles, sem login).
- Features nomeadas: **Instagram Scraper · Email Sender · Email Warmup.** Alvos: Followers · Following · Commenters · Location · Hashtag.
- Segmentos: Agency · eCommerce · Freelance · Infoproduto.

## 2. O onboarding (o que o fundador viu — steps 1→6, reconstruído)
Wizard curto, **done-for-you**, dopamina crescente:
1–2. Informa **seu negócio/site** (analisam `ginkgosystems.tech`) + a **conta-alvo** (`@notorius.ai`).
3. **Scan** → acham os contatos.
4. **Conecta seu email.**
5. **"Escolha o seu modelo de email"** — **3 variantes geradas por IA** com base no negócio, com Assunto + editor rich-text + **variáveis** (`{{first_name}}`, `{{username}}`) + **"Gerar novos"** + reassurance *"não se preocupe, pode editar depois."* (O modelo era um cold-email: "Vi seu Instagram e tive uma ideia rápida… montei um checklist… responda a este email.")
6. **"Excelente trabalho!"** — checklist do que **FIZERAM**: ✅ analisámos seu site ✅ analisámos seguidores de @notorius.ai ✅ **encontrámos 73 emails e 62 telefones** ✅ ligámos sua conta de email ✅ modelo pronto pra enviar.

## 3. O que ROUBAR (UX/produto — é ouro)
1. **Wizard de onboarding curto e "done-for-you":** cada passo faz o trabalho pesado POR você; fricção baixa ("edita depois").
2. **Tela "Excelente trabalho!" com números concretos** ("73 emails, 62 telefones") — é um momento **honest-data perfeito**: mostra trabalho **provado** antes de pedir compromisso. Nós fazemos igual **e com prova real** (Evidence) — fica mais honesto que o deles (que é marketing).
3. **Templates IA: 3 variantes + "gerar novos" + variáveis** — o "escrevi pra você, escolhe e ajusta". Encaixa direto no passo "aprovar campanha (modelo)" do nosso outbound + é PYRE.
4. **Personalização "lê seu site":** eles leem `ginkgosystems.tech` pra calibrar a copy → nós: o **Brann lê o AgentProfile/RAG** da org e calibra.
5. **Multi-source targeting** (followers/following/commenters/location/hashtag) = o mapa de fontes do **Lead Finder**.
6. **Canal = EMAIL** (com warmup + deliverability) — ver §5, é o insight que muda nosso spec.
7. **GDPR como badge na frente** ("GDPR compliant · no card required · +1.000 reviews") — confiança/segurança no hero (igual modo-Pierre).
8. **Âncora €0,10/lead vs Meta Ads** — posicionamento forte + gancho pro WAVE (subir lista pra lookalike).

## 4. 🔴 O que NÃO copiar cru (o risco — é o núcleo deles)
O core do Mailerfind = **scraping de IG + cold email a estranhos**. A defesa legal deles (só dado **público**, GDPR/CAN-SPAM permitem outreach B2B **com opt-out**, scraping da infra própria = sem ban) é **real mas contestada**:
- **Scraping do IG fere o ToS do Instagram** (mesmo "sem login"). Risco de bloqueio da fonte, não da conta do cliente.
- **Cold email a contato raspado** = corda-bamba no EU (GDPR: consentimento vs interesse-legítimo) e regulado nos EUA (CAN-SPAM: opt-out + sem engano). Funciona, mas é **compliance-tightrope**.
- Pra nossa doutrina **honest-data + governado + auditável**, não dá pra só colar "raspa + dispara". A **nossa versão tem que ser consent-aware, opt-out-enforced e auditável** — e isso vira **diferencial** (fazemos governado, eles no fio).

## 5. Reverse pro Ginkgo — o mapa (Mailerfind = 3 das nossas coisas fundidas)
Mailerfind é um **ponto-a-ponto de um canal só**. A versão Ginkgo é a **governada, multicanal e de funil completo**:

| Mailerfind | Peça Ginkgo | Nota |
|---|---|---|
| IG scraper + enriquecimento (email/tel) | **Lead Finder** (sub-agente, dos decks) | sai de "futuro" pra "specar" — com o flag de ToS/scraping |
| IA gera o email (variantes) | **Nyra / PYRE** (copy) | o passo de template do outbound |
| Email Sender + Warmup + deliverability | **outbound engine** (`leaf.outbound.*`) | **canal EMAIL** (ver abaixo) + a cadência sequencial que specamos |
| "responda a este email" → conversa | **Callima / LEAF** (inbound assume) | nosso loop de conversão |
| sobe lista pro Meta Ads (lookalike) | **Alfred / WAVE** | retargeting/custom audiences |
| wizard + tela de resultado | **onboarding LEAF + wizard de campanha** | roubar o UX |

**A jogada:** Lead Finder (fonte) → Nyra (copy) → outbound (email primeiro, WhatsApp p/ opt-in/warm) → Callima (conversa+converte) → Alfred (lookalike no Meta) — **tudo governado, honest-data, auditável**, com o wizard bonito + a tela "achamos X, provado".

## 6. Impacto no spec de outbound (`leaf_feature_outbound.md`)
1. **🔑 Adicionar EMAIL como canal de cold primário.** Mailerfind prova: **email cold é mais defensável e menos "banível" que WhatsApp cold** (CAN-SPAM/opt-out vs ban de número). Regra Ginkgo: **cold = email** (com warmup + deliverability); **WhatsApp = só warm/opt-in** (a decisão que você já tomou). Isso amplia o spec de "WhatsApp opt-in" pra **"email cold + WhatsApp warm"**.
2. **Onboarding/campanha = wizard** (roubar o de 6 passos): analisar negócio → fonte de leads → **3 modelos IA** → conectar canal → **tela "Excelente! encontramos X, modelo pronto"** → **Aprovar** (o nosso HITL de campanha).
3. **Lead Finder** vira spec próprio (fonte da cartela além do CSV manual) — com o flag legal.
4. **Deliverability + warmup de email** = requisito de engenharia novo (inbox vs spam) — dependência a registrar.

## 7. Recomendação
- **Curto prazo (piloto):** dá pra usar o próprio Mailerfind (ou nosso Lead Finder futuro) como **fonte de cartela** — MAS respeitando a decisão de opt-in: lead raspado é **cold** → mandar por **email** (defensável), não por WhatsApp (ban). Se for WhatsApp, só com opt-in real.
- **Médio prazo:** o **wizard + tela-resultado** entram no design do Claude Design (onboarding LEAF e criação de campanha outbound). O **canal email** entra no spec.
- **Diferencial nosso vs Mailerfind:** eles param no "enviei". Nós **governamos o funil inteiro com prova** (quem foi abordado, resposta, conversão — auditável), multicanal, com a Callima fechando a venda na conversa. É o "Mailerfind + secretária que converte + honest-data".

## 8. Telas / UX (walkthrough completo — o que roubar no Claude Design)
- **Tour guiado de 14 passos** (coach-marks "X de 14" + Anterior/Seguinte): na 1ª vez, spotlights explicam cada área (campanha, remetente, origem, assunto, modelos, teste, enviar). **Roubar** pro onboarding do LEAF/outbound — ensina fazendo, fricção baixa.
- **IA da sidebar:** dois blocos — **LEADS** (Análises · Nova análise · Filtros · Prospetos · Contas) e **ENVIO DE EMAILS** (Campanhas · Caixa de entrada · Contas de email) + Recursos/Integrações. Separa **gerar lead** de **enviar** → mapeia direto no nosso **Lead Finder + outbound**.
- **Editor de campanha (anatomia = o nosso wizard):** Assunto + Corpo rich-text com **Variáveis** · **Email AI** (gera/reescreve) · **Modelos** ("com resultados comprovados") · **Pré-visualização/HTML**. Painel "Definições": título interno · **Origem = Análise \| Lista** (fonte: um scrape OU lista manual) · contas remetentes · **"Total de envios diários ~25 emails/dia"** = a **cadência/teto** que specamos, exposta na UI.
- **Job de scrape com progresso honesto:** "Seguidores de @notorius.ai · 88.662 introduzidos · 592 analisados · RUNNING 1%" — long-running com % real. Nosso Lead Finder mostra igual (honest-data).
- **Fontes de lead além do IG:** **Google Maps Leads** (empresas locais por categoria+localização → tel/email/morada). Amplia o Lead Finder (local business, não só social).
- **Caixa de Entrada Unificada:** todas as respostas de email num lugar. = nosso inbox, mas de email; quando o lead responde, **a Callima assume** (nosso loop).
- **Gamificação + créditos (≈GTK):** "Ganhe Créditos Gratuitos" (+250 treino, +250 feedback), "75 a resgatar", "0/1600 créditos", checklist "0 de 5". Ativação gamificada + **créditos = o nosso GTK**. (O banner regressivo "cupão expira em 14h" = urgência agressiva → **NÃO roubar**, fere honest-data.)
- **🎯 O "kanban inteligente":** o Mailerfind é lindo mas **baseado em LISTAS/tabelas** (Análises, Prospetos, Campanhas). O **nosso Kanban-pipeline** (não-abordado→conversando→frio→convertido) é **mais inteligente**: mostra a JORNADA do lead + estado **provado por Event** (honest-data), não tabela estática. **Combinar:** telas lindas do Mailerfind + kanban-como-pipeline + honest-data = versão superior.
