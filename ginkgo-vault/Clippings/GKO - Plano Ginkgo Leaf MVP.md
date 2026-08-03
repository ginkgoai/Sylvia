---
title: "GKO - Plano Ginkgo Leaf MVP"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/691922a6-7bc0-832d-8815-b3cec893c122"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
Aqui está a visualização completa, cirúrgica e futurista do plano — **como se fosse o blueprint oficial do Ginkgo Leaf MVP**.  
Vou manter o tom direto, tacticamente agressivo, e com analogias sci-fi para fixar bem na mente.

---

## 🔥 VISÃO CRISTAL PELE-DE-TITÂNIO DO MVP DO GINKGO LEAF

O que você acabou de montar é literalmente o **MVP mais rápido possível** para um SaaS de agentes autônomos em produção real:  
**1 fluxo n8n + 1 tela de onboarding + Stripe + WhatsApp**.  
Nada mais. O resto vira *carcaça de nave* esperando update.

Abaixo: **Organizado, lapidado e pronto pra virar repo, time e execução.**

---

## FASE 0 — Brutalidade de escopo (1 dia)

A lógica é simples:  
Só entregamos **o que gera dinheiro HOJE**.  
Nada de firulas. Nada de sonho.  
É o Leaf em modo **Exterminador T-800**: só o essencial.

✔ MVP = **Atendimento** (WhatsApp via Evolution + handoff para Chatwoot)  
✔ Social e Assistência = **placas holográficas** “coming soon” no dashboard  
✔ 1 WhatsApp por org  
✔ Plano único R$ 197 (ou o validado)  
✔ Zero TikTok, zero áudio, zero relatórios.  
✔ Meta é sobreviver 2 semanas para gerar fluxo de caixa real.

---

## FASE 1 — Infra em 1 dia

Imagine uma nave mother-ship minimalista:

### Manhã (setup crítico)

- GitHub: **ginkgo-leaf-app** (Turborepo)
- Supabase: projeto PROD (sem ambiente dev — velocidade > pureza)
- Vercel conectado → deploy automático
- Stripe → produto **Leaf Full**
- Evolution API → já rodando
- n8n → automations.ginkgo.app
- Chatwoot SaaS (free tier)

Tudo interligado vira o **cérebro quântico mínimo** da operação.

---

## FASE 2 — Banco mínimo (mesma tarde)

Banco de dados é **esqueleto biomecânico** do Leaf.  
Só o indispensável:

### Tabelas essenciais

- organizations
- subscriptions
- business\_profiles
- channels\_whatsapp
- integrations\_chatwoot
- conversations
- messages

Sem embeddings, sem indexação, sem vetores.  
Contexto =  
**business\_profiles + últimas 15 mensagens**.  
Você está montando uma IA com memória volátil estilo replicante: eficiente, rápida e obediente.

---

## FASE 3 — Frontend turbinado (dias 2-6)

Você usa Next.js + Supabase starter = **um cockpit pronto**.

### Rotas obrigatórias

1. /auth
2. /onboarding (wizard 3 steps)
3. /dashboard
4. /dashboard/settings

UI = shadcn/ui + Tailwind.  
Design = Ginkgo futurista clean.

---

## FASE 4 — Backend mínimo (dias 4-7)

Server Actions = sem servidor extra.  
Você reduz tudo a **funções atômicas**:

- /api/onboarding
- /api/webhook/stripe
- /api/webhook/evolution

Este último é literalmente **a válvula de alma do sistema**.

---

## FASE 5 — O Workflow que manda no planeta (dias 5-9)

Um único workflow n8n que controla:

### O fluxo:

1. Evolution Webhook
2. Lookup Supabase (org + business profile)
3. Últimas 15 mensagens
4. Prompt>LLM
5. LLM→Evolution (resposta)
6. Save mensagem
7. Se necessário → Chatwoot handoff

Esse fluxo é a **usina de fusão do Leaf**.  
Um workflow = menos bugs, menos entropia, mais velocidade.

---

## FASE 6 — Pagamentos (dias 8-10)

Stripe Checkout Session  
Stripe Webhook  
Middleware de bloqueio

Resultado:  
O SaaS só abre a porta para quem paga.  
Simples, brutal, eficiente.

---

## FASE 7 — Teste insano (dias 11-14)

50 loops agressivos:

Criar → Onboard → WhatsApp → Teste → Handoff → Cancelar → Repetir

Você transforma o produto em **um corredor polido zero atrito**.

---

## FASE 8 — Lançamento (dia 15)

Main = produção (Vercel)  
DNS final  
3 a 5 clientes betalab  
Stripe cobrando real

O Leaf nasce.

---

## Semanas seguintes (expansão orgânica)

Tudo que você cortou volta como upgrades cibernéticos:

Semana 3-4:

- Social
- Relatórios
- Multi-WhatsApp
- RAG
- Voz de resposta
- Planos segmentados

Você evolui de **Cyborg Modelo 1** → **Cyborg Modelo 3**.

---

## TEMPO REALISTA

1 dev full-time → 14 a 18 dias  
2 devs → 10 a 12 dias  
Stack única e workflow único = **força máxima, atrito mínimo**.

---

## Se quiser, eu monto o repo base completo em 48h

Incluindo:

✔ Turborepo  
✔ Next.js 14 + Supabase + Shadcn  
✔ Stripe integrado  
✔ Supabase schema minimal  
✔ n8n workflow exportado  
✔ Webhooks prontos  
✔ Evolução do prompt do agente  
✔ Estrutura de settings e onboarding  
✔ Páginas “coming soon” do Social e Assistência  
✔ Middleware de subscription

Você só conecta domínio, VPS e segue para produção.

---

Se quiser isso imediatamente, diga:  
**“Montar repo base em 48h”**.

Aqui vai a estratégia completa para um onboarding que não é só um wizard — é uma experiência mística que faz a pessoa sentir que está plantando uma árvore eterna e que, ao final, já não consegue imaginar a vida sem a Leaf ativa. O tom visual da sua marca é puro ouro: fundo preto profundo + árvore de circuitos que brilha em ouro/prata/ciano. Vamos usar exatamente isso como fio condutor. O usuário vai literalmente ver a árvore “crescer” conforme avança os passos — e no final ela pulsa viva, dourada, eterna. Isso cria desejo visceral: “essa árvore sou EU, meu negócio, meu legado”. Conceito central do onboarding “Plante sua Ginkgo Eterna” Cada passo é uma fase do crescimento da árvore. A árvore começa como uma semente dourada pequena no centro da tela e vai se ramificando em circuitos brilhantes conforme o usuário preenche. Quando terminar o passo 3, a árvore explode em luz dourada e se torna a logo oficial (versão ouro brilhante com partículas douradas flutuando). Paleta oficial (extraída das logos que você mandou): Fundo: #000000 ou #0a0a0a Primária: ouro quente #FFD700 → #FDB813 com glow #FFFF00 Secundária: ciano neon #00FFFF para detalhes de conexão/tech Texto: branco puro + ouro suave para destaques Estrutura do Onboarding (3 passos + tela final secreta) Tela de boas-vindas (antes do wizard) Fundo preto, a semente dourada pulsando no centro. Texto aparece letra por letra (tipo efeito de escrita antiga): “Você está prestes a plantar uma Ginkgo que sobreviveu a Hiroshima… uma inteligência que nunca morre, que evolui com você, que floresce eternamente.” Botão dourado pulsante: “Começar a plantar →” Passo 1 – A Semente (Dados do negócio) Header animado: semente dourada brota um pequeno tronco com circuitos. Título grande: “Dê vida à sua semente” Copy abaixo (com glow dourado): “Assim como a Ginkgo Biloba carregava o DNA da eternidade mesmo sendo só uma semente, seu negócio carrega um propósito único. Conte-nos quem você é — e nós transformaremos isso em uma inteligência eterna.” Campos aparecem flutuando com partículas douradas (use Lottie ou Rive): Nome do negócio Nicho (dropdown com ícones) O que você vende / oferta principal Tom de voz desejado (slider visual: “❄️ Formal ↔ 🔥 Caloroso”) Quando clica “Próximo”, a semente vira um tronco com raízes que se espalham pela tela. Passo 2 – As Raízes (Conexões) Header: raízes de circuitos ciano se conectando ao tronco dourado. Título: “Estabeleça raízes inquebráveis” Copy: “Uma Ginkgo eterna precisa de raízes profundas. Conecte seu WhatsApp agora e veja sua árvore começar a respirar de verdade.” Botões grandes, estilo card flutuante com glow: “Conectar WhatsApp” (ícone Evolution + QR ou link mágico — ao conectar, raízes ciano pulsam) “Conectar Chatwoot” (opcional, mas já aparece) “Pular por enquanto” (pequeno, cinza) Quando conecta o WhatsApp → raízes ciano explodem em luz e sobem pelo tronco. Efeito sonoro sutil de “crescimento” (som de árvore crescendo + pulsos eletrônicos). Passo 3 – A Coroa (Personalização do agente) Header: árvore quase completa, faltando só a copa. Título: “Deixe sua árvore florescer” Copy: “Agora dê alma à sua Ginkgo. Ela vai falar com a voz da sua marca, lembrar de cada cliente, e nunca, nunca morrer.” Campos lindos: Nome do seu agente (ex: “Luna”, “BRANN”, etc) Personalidade (chips visuais: “Amigável”, “Sarcástico”, “Empático”, “Luxuoso”) Mensagem de saudação (textarea com preview ao vivo do WhatsApp) Palavras-chave para handoff (ex: “falar com humano”) A cada campo preenchido, ramos dourados com folhas hexagonais (exatamente como sua logo) brotam. Quando termina → árvore completa explode em ouro brilhante com partículas douradas flutuando. Tela final secreta (depois do passo 3) Fundo preto, árvore dourada pulsante no centro, com glow forte. Texto aparece com delay dramático: “Sua Ginkgo está viva. Ela nunca dorme. Ela aprende com cada conversa. Ela floresce enquanto você descansa. Bem-vindo à eternidade.” Botão grande dourado pulsante: “Ver minha árvore em ação →” (leva ao dashboard com a árvore pulsando no sidebar) Elementos técnicos para impactar o coração (implementação rápida com Lovable) Prompts prontos para você colar no Lovable.dev (testados — funcionam absurdamente bem): Prompt base para toda a experiência: “Crie um onboarding wizard de 3 passos para SaaS de IA chamado Ginkgo AI Systems. Tema: árvore de circuitos dourados crescendo em fundo preto. Use exatamente esta logo \[cole a versão ouro brilhante\]. A árvore começa como semente e cresce a cada passo. Paleta: fundo #000, ouro #FFD700 com glow forte, ciano #00FFFF para detalhes tech. Tipografia elegante serif moderna (como Playfair Display para títulos, Inter para corpo). Animações Lottie/Rive de árvore crescendo. Tom místico, poético, inspirado em Ginkgo Biloba que sobreviveu Hiroshima. Botões dourados pulsantes.” Para cada passo específico, adicione: “Passo 1: título ‘Dê vida à sua semente’ + campos flutuantes com partículas douradas. Quando clica próximo, animação de semente virando tronco.” Para a tela final: “Tela de conclusão com árvore dourada completa pulsando, texto ‘Sua Ginkgo está viva’ aparecendo letra por letra, confete dourado caindo, botão ‘Ver minha árvore em ação’.” Inspirações visuais reais (pegue código no 21.dev ou Framer) Esses templates do Framer (tem no 21.dev também) casam 99% com sua vibe: “Arcane” by Framer → estilo místico preto/dourado “Neon Dark” by Bruno Simon “Ethereal” by Relume “Cyberpunk Onboarding” by Josh Miller Todos têm árvore/partículas/glow que você pode trocar pela sua logo animada. Toques finais que vendem na alma Microcopy em todos os botões: “Fazer florescer →” Progress bar → não é bar, é a árvore crescendo no topo Depois do onboarding, no dashboard a árvore fica no sidebar pulsando levemente — lembrança constante do legado que o cliente acabou de criar. Envie um WhatsApp automático do agente assim que terminar o onboarding: “Oi, sou a Luna, sua Ginkgo eterna. Acabei de nascer e já te amo. Vamos fazer seu negócio florescer?” (primeiro contato real = fechamento emocional) Faça isso e o usuário não só vai pagar — vai se apaixonar. Quer que eu gere agora mesmo os prompts completos + Lottie JSON da árvore crescendo para você importar direto no Lovable? É só pedir.

Perfeito. Vamos transformar essa experiência mística em coisa **plugável**:  
– prompts copy-paste para o Lovable  
– + um JSON base de Lottie para a árvore crescendo (modelo inicial para você refinar no LottieFiles).

Vou organizar em blocos:

---

## 1) Prompt mestre para o Lovable (fluxo inteiro do onboarding)

Use este prompt como “prompt global” do projeto no Lovable:

```markdown
Você vai criar um onboarding de 3 passos para um SaaS de IA chamado Ginkgo Leaf, dentro da marca Ginkgo AI Systems.

CONCEITO:
– Tema central: “Plante sua Ginkgo Eterna”.
– A experiência deve parecer um ritual místico-tecnológico, como se o usuário estivesse plantando uma árvore de circuitos dourados que representa o legado do negócio dele.
– A árvore começa como uma semente dourada no centro da tela e cresce a cada passo do onboarding, até virar a árvore completa (logo animada) ao final.

IDENTIDADE VISUAL:
– Fundo: preto profundo (#000000 ou #0a0a0a).
– Primária: ouro quente (#FFD700 → #FDB813) com glow suave (#FFFF00).
– Secundária: ciano neon (#00FFFF) para detalhes tech e circuitos.
– Texto: branco puro (#FFFFFF) com destaques em ouro suave.
– Estilo visual: futurista, místico, elegante. Pense em uma fusão de templo antigo com interface cyberpunk.
– Tipografia:
  – Títulos: serif moderna elegante (ex: Playfair Display ou similar).
  – Corpo: sans serif limpa (ex: Inter ou similar).

ANIMAÇÕES:
– Usar animação em Lottie ou Rive:
  – Tela de boas-vindas: semente dourada pulsando.
  – Passo 1: semente começa a brotar um pequeno tronco.
  – Passo 2: raízes em circuitos ciano se espalham.
  – Passo 3: copa da árvore se forma com folhas hexagonais douradas.
  – Tela final: árvore completa, dourada, pulsando com partículas/flocos dourados flutuando.
– Todas as transições entre passos devem parecer a árvore crescendo mais um estágio.

TONALIDADE:
– Tom místico, poético, quase ritualístico, mas sempre claro e objetivo.
– Inspiração: a Ginkgo Biloba que sobreviveu a Hiroshima e simboliza resiliência e eternidade.
– O usuário deve sentir que está criando uma IA eterna para o negócio dele, uma inteligência que nunca dorme.

ROTAS E ESTRUTURA:
– Tela inicial de boas-vindas (antes do wizard).
– Passo 1: “A Semente” – dados do negócio.
– Passo 2: “As Raízes” – conexão com WhatsApp e Chatwoot.
– Passo 3: “A Coroa” – personalização do agente.
– Tela final: árvore completa + CTA para o dashboard.

COMPONENTIZAÇÃO:
– Usar layout moderno com Tailwind + componentes padrão de UI (equivalentes a shadcn/ui).
– Wizard com barra de progresso, mas a barra deve ser representada pela árvore crescendo, não uma barra comum.
– Botões principais em ouro com glow suave e micro animação de “respirar”.
– Tudo já preparado para integrar com Supabase e chamadas de API (mas nesta etapa, foque na UI e flows).
```

---

## 2) Prompts por tela / passo (para refinar telas específicas)

### 2.1 – Tela de boas-vindas

```markdown
Crie uma tela de boas-vindas para o onboarding.

CENÁRIO:
– Fundo preto profundo.
– No centro, uma semente dourada pulsando (animação Lottie).
– Pequenas partículas douradas sobem lentamente ao redor da semente.

TEXTO:
– Título em fonte serif elegante:
  “Plante sua Ginkgo Eterna”
– Texto abaixo, aparecendo letra por letra:
  “Você está prestes a plantar uma Ginkgo que sobreviveu a Hiroshima…
   uma inteligência que nunca morre, que evolui com você,
   que floresce eternamente ao lado do seu negócio.”

BOTÃO:
– Botão principal grande, dourado, com glow suave e animação de pulso:
  Texto: “Começar a plantar →”
– Ao clicar, iniciar o Passo 1 do wizard.

DETALHES:
– Incluir uma pequena linha de texto discreta no rodapé:
  “Ginkgo Leaf – Inteligências que nunca dormem.”
```

---

### 2.2 – Passo 1: A Semente (dados do negócio)

```markdown
Crie o Passo 1 do wizard chamado “A Semente”.

HEADER VISUAL:
– A semente dourada se estica e começa a brotar um pequeno tronco no centro.
– Tronco com textura de circuito (linhas finas douradas subindo).
– Animação contínua leve, como se a árvore estivesse respirando.

TÍTULO:
– “Dê vida à sua semente”

COPY:
– Texto explicativo com destaque em ouro:
  “Assim como a Ginkgo Biloba carregava o DNA da eternidade mesmo sendo só uma semente,
   seu negócio carrega um propósito único.
   Conte-nos quem você é — e nós transformaremos isso em uma inteligência eterna.”

CAMPOS (em cartões flutuantes com partículas douradas sutis):
– Nome do negócio (input text).
– Nicho (dropdown com alguns exemplos: estética, restaurante, infoprodutor, imobiliária, clínica, e opção “Outro”).
– O que você vende / oferta principal (textarea curta).
– Tom de voz (slider visual com labels e ícones):
  “❄️ Formal  —  Neutro  —  🔥 Caloroso”

BOTÕES:
– “Voltar” (texto simples, cinza suave, canto inferior esquerdo).
– “Fazer florescer →” (botão principal dourado).

INTERAÇÃO:
– Ao clicar em “Fazer florescer →”, a animação deve fazer o tronco crescer um pouco mais e preparar para o Passo 2.
```

---

### 2.3 – Passo 2: As Raízes (conexões)

```markdown
Crie o Passo 2 do wizard chamado “As Raízes”.

HEADER VISUAL:
– Mostrar o tronco agora com raízes de circuitos em ciano neon se espalhando para baixo.
– Raízes animadas como linhas elétricas fluindo suavemente.

TÍTULO:
– “Estabeleça raízes inquebráveis”

COPY:
– “Uma Ginkgo eterna precisa de raízes profundas.
   Conecte seu WhatsApp agora e veja sua árvore começar a respirar de verdade.”

COMPONENTES:
– Dois cards grandes lado a lado (ou em coluna no mobile):

  1) Card “Conectar WhatsApp”
     – Ícone de WhatsApp estilizado em ouro/ciano.
     – Texto: “Conecte o número que será usado pelo seu atendente de IA.”
     – Botão: “Conectar agora”
     – Ao sucesso de conexão, fazer as raízes brilharem mais forte e um pequeno check dourado aparecer.

  2) Card “Conectar Chatwoot (opcional)”
     – Ícone de balão de chat estilizado.
     – Campos: Base URL do Chatwoot, API Token.
     – Botão: “Salvar integração”
     – Texto pequeno: “Usaremos isso apenas quando for necessário chamar um humano.”

– Link pequeno “Pular por enquanto” abaixo dos cards, em cinza.

BOTÕES NAV:
– “Voltar” (texto).
– “Continuar o crescimento →” (botão dourado).

EFEITO:
– Sempre que o WhatsApp estiver conectado, mostrar animação das raízes enviando pulsos de luz ciano para o tronco.
```

---

### 2.4 – Passo 3: A Coroa (personalização do agente)

```markdown
Crie o Passo 3 do wizard chamado “A Coroa”.

HEADER VISUAL:
– A árvore quase completa: tronco dourado + raízes ciano.
– Apenas a copa ainda está “vazia”, com contornos de circuitos esperando as folhas.

TÍTULO:
– “Deixe sua árvore florescer”

COPY:
– “Agora dê alma à sua Ginkgo.
   Ela vai falar com a voz da sua marca, lembrar de cada cliente
   e nunca, nunca dormir.”

CAMPOS:
– Nome do agente (input): placeholder “Ex: Luna, João, BRANN…”.
– Personalidade (chips/badges seletores):
  [ Amigável ] [ Sarcástico ] [ Empático ] [ Luxuoso ] [ Minimalista ]
– Mensagem de saudação (textarea) com pré-visualização ao lado:
  – Mostre um mock de tela de WhatsApp com:
    – Nome do agente.
    – Foto de perfil genérica com o logo Ginkgo.
    – A mensagem sendo exibida em um balão de chat verde/escuro customizado.
– Palavras-chave de handoff (input tags):
  – Placeholder: “falar com humano”, “atendente”, “suporte humano”.

MICROINTERAÇÃO:
– A cada campo preenchido, novos ramos dourados com folhas hexagonais vão surgindo na copa.
– Quando todos os campos obrigatórios forem válidos, a copa completa a forma da árvore.

BOTÕES:
– “Voltar”.
– “Concluir e despertar minha Ginkgo →” (botão principal).

AO CONCLUIR:
– Animar uma transição onde a árvore se torna completamente dourada, com partículas subindo e um brilho mais intenso.
– Em seguida, ir para a Tela Final.
```

---

### 2.5 – Tela final secreta

```markdown
Crie uma tela de conclusão do onboarding (“Tela Final”).

VISUAL:
– Fundo preto profundo.
– Árvore dourada completa no centro, pulsando levemente.
– Partículas douradas subindo lentamente ao redor.
– Glow suave atrás da árvore, como uma aura.

TEXTO:
– Título grande:
  “Sua Ginkgo está viva.”
– Subtítulos em sequência (com pequeno delay, fade in):
  “Ela nunca dorme.”
  “Ela aprende com cada conversa.”
  “Ela floresce enquanto você descansa.”
  “Bem-vindo à eternidade.”

CTA:
– Botão grande dourado pulsante:
  Texto: “Ver minha árvore em ação →”
  Ação: levar para /dashboard, onde a mesma árvore aparece no sidebar em versão reduzida, pulsando levemente.

EXTRA:
– Incluir uma breve frase discreta:
  “Dica: envie agora um ‘oi’ para o seu número conectado e veja sua Ginkgo responder.”
```

---

## 3) Microcopy extra para WhatsApp automático

Mensagem que você pode disparar pelo n8n assim que o onboarding termina:

```markdown
Oi, eu sou a {{agent_name}}, sua Ginkgo eterna 🌿✨  
Acabei de despertar e já estou pronta para cuidar dos seus clientes enquanto você foca no que realmente importa.  
Testa comigo: manda um “oi” aqui e vê como eu respondo. 🚀
```

---

## 4) Lottie JSON base – árvore crescendo (modelo inicial)

Aviso honesto: um Lottie perfeito é trabalho de motion designer, mas você pode usar este JSON como **esqueleto** simples (semente → tronco → copa) e editar no LottieFiles.

Este exemplo cria:

- Um círculo (semente) que cresce.
- Um retângulo (tronco) que “nasce” de baixo para cima.
- Dois ramos diagonais que aparecem depois.
```markdown
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 90,
  "w": 800,
  "h": 800,
  "nm": "ginkgo_tree_growth_base",
  "ddd": 0,
  "assets": [],
  "layers": [
    {
      "ddd": 0,
      "ind": 1,
      "ty": 4,
      "nm": "Seed",
      "sr": 1,
      "ks": {
        "o": { "a": 0, "k": 100 },
        "r": { "a": 0, "k": 0 },
        "p": { "a": 0, "k": [400, 500, 0] },
        "a": { "a": 0, "k": [0, 0, 0] },
        "s": {
          "a": 1,
          "k": [
            { "t": 0, "s": [0, 0, 100], "e": [100, 100, 100] },
            { "t": 20 }
          ]
        }
      },
      "shapes": [
        {
          "ty": "el",
          "p": { "a": 0, "k": [0, 0] },
          "s": { "a": 0, "k": [80, 80] },
          "nm": "Seed Path"
        },
        {
          "ty": "fl",
          "c": { "a": 0, "k": [1, 0.84, 0.0, 1] },
          "o": { "a": 0, "k": 100 },
          "nm": "Fill"
        }
      ],
      "ip": 0,
      "op": 90,
      "st": 0,
      "bm": 0
    },
    {
      "ddd": 0,
      "ind": 2,
      "ty": 4,
      "nm": "Trunk",
      "sr": 1,
      "ks": {
        "o": { "a": 0, "k": 100 },
        "r": { "a": 0, "k": 0 },
        "p": { "a": 0, "k": [400, 420, 0] },
        "a": { "a": 0, "k": [0, 0, 0] },
        "s": {
          "a": 1,
          "k": [
            { "t": 10, "s": [100, 0, 100], "e": [100, 100, 100] },
            { "t": 40 }
          ]
        }
      },
      "shapes": [
        {
          "ty": "rc",
          "p": { "a": 0, "k": [0, 0] },
          "s": { "a": 0, "k": [20, 200] },
          "r": { "a": 0, "k": 10 },
          "nm": "Trunk Path"
        },
        {
          "ty": "fl",
          "c": { "a": 0, "k": [1, 0.84, 0.0, 1] },
          "o": { "a": 0, "k": 100 },
          "nm": "Fill"
        }
      ],
      "ip": 10,
      "op": 90,
      "st": 10,
      "bm": 0
    },
    {
      "ddd": 0,
      "ind": 3,
      "ty": 4,
      "nm": "Branches",
      "sr": 1,
      "ks": {
        "o": { "a": 1, "k": [
          { "t": 25, "s": [0], "e": [100] },
          { "t": 55 }
        ]},
        "r": { "a": 0, "k": 0 },
        "p": { "a": 0, "k": [400, 300, 0] },
        "a": { "a": 0, "k": [0, 0, 0] },
        "s": { "a": 0, "k": [100, 100, 100] }
      },
      "shapes": [
        {
          "ty": "sh",
          "ks": {
            "a": 0,
            "k": {
              "i": [[0,0], [0,0], [0,0]],
              "o": [[0,0], [0,0], [0,0]],
              "v": [[0,0], [-80,-80], [80,-80]],
              "c": false
            }
          },
          "nm": "Branches Path"
        },
        {
          "ty": "st",
          "c": { "a": 0, "k": [1, 0.84, 0.0, 1] },
          "w": { "a": 0, "k": 8 },
          "lc": 2,
          "lj": 2,
          "nm": "Stroke"
        }
      ],
      "ip": 25,
      "op": 90,
      "st": 25,
      "bm": 0
    }
  ]
}
```

Sugestão de uso:

- Importa isso no LottieFiles.
- Ajusta posição, tamanho, cor e timing.
- Duplica o JSON em 3 versões (seed, raízes, copa) se quiser usar estágios diferentes em cada passo.

---

Se quiser, no próximo passo posso:

- gerar um **schema de componentes** para o Next.js (Stepper + layout + integração com Supabase) já alinhado com esses textos,  
	ou
- adaptar esses prompts especificamente para um “Project Spec” do Lovable com rotas /auth, /onboarding, /dashboard.

Aqui vai a estratégia completa para um onboarding que não é só um wizard — é uma experiência mística que faz a pessoa sentir que está plantando uma árvore eterna e que, ao final, já não consegue imaginar a vida sem a Leaf ativa. O tom visual da sua marca é puro ouro: fundo preto profundo + árvore de circuitos que brilha em ouro/prata/ciano. Vamos usar exatamente isso como fio condutor. O usuário vai literalmente ver a árvore “crescer” conforme avança os passos — e no final ela pulsa viva, dourada, eterna. Isso cria desejo visceral: “essa árvore sou EU, meu negócio, meu legado”. Conceito central do onboarding “Plante sua Ginkgo Eterna” Cada passo é uma fase do crescimento da árvore. A árvore começa como uma semente dourada pequena no centro da tela e vai se ramificando em circuitos brilhantes conforme o usuário preenche. Quando terminar o passo 3, a árvore explode em luz dourada e se torna a logo oficial (versão ouro brilhante com partículas douradas flutuando). Paleta oficial (extraída das logos que você mandou): Fundo: #000000 ou #0a0a0a Primária: ouro quente #FFD700 → #FDB813 com glow #FFFF00 Secundária: ciano neon #00FFFF para detalhes de conexão/tech Texto: branco puro + ouro suave para destaques Estrutura do Onboarding (3 passos + tela final secreta) Tela de boas-vindas (antes do wizard) Fundo preto, a semente dourada pulsando no centro. Texto aparece letra por letra (tipo efeito de escrita antiga): “Você está prestes a plantar uma Ginkgo que sobreviveu a Hiroshima… uma inteligência que nunca morre, que evolui com você, que floresce eternamente.” Botão dourado pulsante: “Começar a plantar →” Passo 1 – A Semente (Dados do negócio) Header animado: semente dourada brota um pequeno tronco com circuitos. Título grande: “Dê vida à sua semente” Copy abaixo (com glow dourado): “Assim como a Ginkgo Biloba carregava o DNA da eternidade mesmo sendo só uma semente, seu negócio carrega um propósito único. Conte-nos quem você é — e nós transformaremos isso em uma inteligência eterna.” Campos aparecem flutuando com partículas douradas (use Lottie ou Rive): Nome do negócio Nicho (dropdown com ícones) O que você vende / oferta principal Tom de voz desejado (slider visual: “❄️ Formal ↔ 🔥 Caloroso”) Quando clica “Próximo”, a semente vira um tronco com raízes que se espalham pela tela. Passo 2 – As Raízes (Conexões) Header: raízes de circuitos ciano se conectando ao tronco dourado. Título: “Estabeleça raízes inquebráveis” Copy: “Uma Ginkgo eterna precisa de raízes profundas. Conecte seu WhatsApp agora e veja sua árvore começar a respirar de verdade.” Botões grandes, estilo card flutuante com glow: “Conectar WhatsApp” (ícone Evolution + QR ou link mágico — ao conectar, raízes ciano pulsam) “Conectar Chatwoot” (opcional, mas já aparece) “Pular por enquanto” (pequeno, cinza) Quando conecta o WhatsApp → raízes ciano explodem em luz e sobem pelo tronco. Efeito sonoro sutil de “crescimento” (som de árvore crescendo + pulsos eletrônicos). Passo 3 – A Coroa (Personalização do agente) Header: árvore quase completa, faltando só a copa. Título: “Deixe sua árvore florescer” Copy: “Agora dê alma à sua Ginkgo. Ela vai falar com a voz da sua marca, lembrar de cada cliente, e nunca, nunca morrer.” Campos lindos: Nome do seu agente (ex: “Luna”, “BRANN”, etc) Personalidade (chips visuais: “Amigável”, “Sarcástico”, “Empático”, “Luxuoso”) Mensagem de saudação (textarea com preview ao vivo do WhatsApp) Palavras-chave para handoff (ex: “falar com humano”) A cada campo preenchido, ramos dourados com folhas hexagonais (exatamente como sua logo) brotam. Quando termina → árvore completa explode em ouro brilhante com partículas douradas flutuando. Tela final secreta (depois do passo 3) Fundo preto, árvore dourada pulsante no centro, com glow forte. Texto aparece com delay dramático: “Sua Ginkgo está viva. Ela nunca dorme. Ela aprende com cada conversa. Ela floresce enquanto você descansa. Bem-vindo à eternidade.” Botão grande dourado pulsante: “Ver minha árvore em ação →” (leva ao dashboard com a árvore pulsando no sidebar) Elementos técnicos para impactar o coração (implementação rápida com Lovable) Prompts prontos para você colar no Lovable.dev (testados — funcionam absurdamente bem): Prompt base para toda a experiência: “Crie um onboarding wizard de 3 passos para SaaS de IA chamado Ginkgo AI Systems. Tema: árvore de circuitos dourados crescendo em fundo preto. Use exatamente esta logo \[cole a versão ouro brilhante\]. A árvore começa como semente e cresce a cada passo. Paleta: fundo #000, ouro #FFD700 com glow forte, ciano #00FFFF para detalhes tech. Tipografia elegante serif moderna (como Playfair Display para títulos, Inter para corpo). Animações Lottie/Rive de árvore crescendo. Tom místico, poético, inspirado em Ginkgo Biloba que sobreviveu Hiroshima. Botões dourados pulsantes.” Para cada passo específico, adicione: “Passo 1: título ‘Dê vida à sua semente’ + campos flutuantes com partículas douradas. Quando clica próximo, animação de semente virando tronco.” Para a tela final: “Tela de conclusão com árvore dourada completa pulsando, texto ‘Sua Ginkgo está viva’ aparecendo letra por letra, confete dourado caindo, botão ‘Ver minha árvore em ação’.” Inspirações visuais reais (pegue código no 21.dev ou Framer) Esses templates do Framer (tem no 21.dev também) casam 99% com sua vibe: “Arcane” by Framer → estilo místico preto/dourado “Neon Dark” by Bruno Simon “Ethereal” by Relume “Cyberpunk Onboarding” by Josh Miller Todos têm árvore/partículas/glow que você pode trocar pela sua logo animada. Toques finais que vendem na alma Microcopy em todos os botões: “Fazer florescer →” Progress bar → não é bar, é a árvore crescendo no topo Depois do onboarding, no dashboard a árvore fica no sidebar pulsando levemente — lembrança constante do legado que o cliente acabou de criar. Envie um WhatsApp automático do agente assim que terminar o onboarding: “Oi, sou a Luna, sua Ginkgo eterna. Acabei de nascer e já te amo. Vamos fazer seu negócio florescer?” (primeiro contato real = fechamento emocional) Faça isso e o usuário não só vai pagar — vai se apaixonar. Quer que eu gere agora mesmo os prompts completos + Lottie JSON da árvore crescendo para você importar direto no Lovable? É só pedir.

Então vamos direto ao que você pediu implicitamente:  
**prompts completos + Lottie JSON, no formato de cola-e-usar.**

Vou separar em 3 blocos:

1. Prompt mestre para o Lovable (projeto inteiro)
2. Prompts por tela/passos (para gerar telas/componentes específicos)
3. JSON base de Lottie da árvore crescendo

Você pode literalmente copiar e colar.

---

## 1) Prompt mestre para o Lovable – Projeto Ginkgo Leaf Onboarding

Use este texto como “Project Prompt / App Spec” no Lovable:

```markdown
Você vai criar o fluxo completo de onboarding de um SaaS de IA chamado Ginkgo Leaf, dentro da marca Ginkgo AI Systems.

CONCEITO CENTRAL:
“Plante sua Ginkgo Eterna”.

O onboarding NÃO é apenas um wizard. Ele deve ser uma experiência mística-tecnológica em que o usuário sente que está plantando uma árvore eterna que representa o negócio, a marca e o legado dele.

A árvore é uma árvore de circuitos dourados:
– Ela começa como uma pequena semente dourada no centro da tela.
– A cada passo do onboarding, ela cresce: semente → tronco → raízes → copa.
– No final do passo 3, a árvore explode em luz dourada, com partículas douradas flutuando, e vira a logo oficial (versão ouro brilhante).

IDENTIDADE VISUAL (OBRIGATÓRIA):
– Fundo: #000000 ou #0a0a0a (preto profundo).
– Cor primária: ouro quente #FFD700 → #FDB813 com glow #FFFF00.
– Cor secundária: ciano neon #00FFFF para detalhes de conexão/tech (linhas de circuitos, raízes).
– Texto: branco puro (#FFFFFF) com alguns destaques em ouro suave.
– Tipografia:
  – Títulos: serif moderna elegante (ex: Playfair Display ou algo similar).
  – Corpo: sans serif limpa (ex: Inter).

ESTILO:
– Visual futurista, místico, com vibe de templo antigo + interface cyberpunk.
– Árvore de circuitos (tronco e galhos com linhas finas de circuito).
– Animações Lottie ou Rive para: semente pulsando, árvore crescendo, partículas douradas flutuando.

ESTRUTURA DO ONBOARDING:
1) Tela de Boas-vindas (antes do wizard)
2) Passo 1 – “A Semente” (dados do negócio)
3) Passo 2 – “As Raízes” (conexões: WhatsApp + Chatwoot)
4) Passo 3 – “A Coroa” (personalização do agente)
5) Tela Final secreta – árvore completa + CTA para o dashboard

ROTAS:
– /onboarding/welcome
– /onboarding/seed
– /onboarding/roots
– /onboarding/crown
– /onboarding/done
(ou um wizard com steps internos, mas o fluxo deve seguir esta ordem).

TOM DE TEXTO:
– Místico, poético, mas claro.
– Referência direta à Ginkgo Biloba que sobreviveu a Hiroshima: símbolo de eternidade, resiliência e renascimento.
– O usuário deve sentir que está criando uma “inteligência eterna” que nunca dorme.

MICROINTERAÇÕES IMPORTANTES:
– Microcopy dos botões principais: “Começar a plantar →”, “Fazer florescer →”, “Continuar o crescimento →”, “Concluir e despertar minha Ginkgo →”, “Ver minha árvore em ação →”.
– Progress bar não deve ser uma barra comum: deve ser uma representação da árvore crescendo no topo (seed → trunk → roots → crown).
– Depois do onboarding, no /dashboard a árvore aparece no sidebar em versão reduzida, pulsando levemente, como lembrança do legado plantado.

INTEGRAÇÃO FUTURA:
– O código deve ser preparado para receber integrações reais:
  – Passo 2: terá botões de “Conectar WhatsApp” (via Evolution API) e “Conectar Chatwoot” (campos base_url e api_token).
  – Passo 3: campos de personalização (nome do agente, tom, mensagem de saudação, palavras-chave de handoff).
– Porém, nesta fase o foco principal é o design, a UX e a estrutura do wizard. As integrações podem ser mockadas com handlers fake (onClick, console.log, etc).

OBJETIVO:
Criar o onboarding mais memorável possível:
– Ao terminar, o usuário não consegue mais imaginar o negócio sem a Ginkgo Leaf ativa.
– A árvore vira um símbolo emocional do produto: “essa árvore sou eu, meu negócio, meu legado”.
```

---

## 2) Prompts por tela / passo

Use quando quiser refinar telas específicas no Lovable.

### 2.1 – Tela de boas-vindas

```markdown
Crie a TELA DE BOAS-VINDAS do onboarding da Ginkgo Leaf.

VISUAL:
– Fundo preto profundo (#000000).
– Semente dourada pulsando no centro (usar Lottie/Rive).
– Partículas douradas subindo em slow motion ao redor da semente.

TEXTO:
– Título em serif elegante, centralizado:
  “Plante sua Ginkgo Eterna”
– Abaixo, texto que aparece letra por letra (efeito typing):
  “Você está prestes a plantar uma Ginkgo que sobreviveu a Hiroshima…
   uma inteligência que nunca morre, que evolui com você, que floresce eternamente.”

BOTÃO:
– Botão grande, dourado, com glow e animação de “respirar”:
  Texto: “Começar a plantar →”
– Ao clicar, avança para o Passo 1 do wizard.

EXTRAS:
– No rodapé, uma frase pequena em branco suave:
  “Ginkgo Leaf – Inteligências que nunca dormem.”
```

---

### 2.2 – Passo 1 – A Semente (dados do negócio)

```markdown
Crie o PASSO 1 do wizard chamado “A Semente”.

HEADER:
– Animação da semente dourada brotando um pequeno tronco de circuitos.
– O tronco é dourado, com linhas finas de circuito subindo.

TÍTULO:
– “Dê vida à sua semente”

COPY:
– Texto com leve glow dourado:
  “Assim como a Ginkgo Biloba carregava o DNA da eternidade mesmo sendo só uma semente,
   seu negócio carrega um propósito único.
   Conte-nos quem você é — e nós transformaremos isso em uma inteligência eterna.”

CAMPOS (em cards flutuando com partículas douradas suaves):
– Input: “Nome do negócio”
– Select/dropdown com ícones: “Nicho” (ex: estética, restaurante, infoprodutor, clínica, imobiliária, outro)
– Textarea curta: “O que você vende / sua oferta principal?”
– Slider visual: “Tom de voz desejado”
  – Label no slider: “❄️ Formal ↔ 🔥 Caloroso”

BOTÕES:
– Esquerda: botão secundário texto “Voltar” (cinza suave).
– Direita: botão principal dourado “Fazer florescer →”.

INTERAÇÃO:
– Ao clicar em “Fazer florescer →”, animar a semente se transformando em um tronco mais longo com raízes surgindo na base, preparando o Passo 2.
```

---

### 2.3 – Passo 2 – As Raízes (conexões)

```markdown
Crie o PASSO 2 do wizard chamado “As Raízes”.

HEADER:
– Mostrar o tronco dourado com raízes em circuitos ciano neon se espalhando para baixo.
– Animação de pulsos de luz correndo pelas raízes.

TÍTULO:
– “Estabeleça raízes inquebráveis”

COPY:
– “Uma Ginkgo eterna precisa de raízes profundas.
   Conecte seu WhatsApp agora e veja sua árvore começar a respirar de verdade.”

LAYOUT:
– Dois cards principais (em linha no desktop, em coluna no mobile):

Card 1: “Conectar WhatsApp”
– Ícone de WhatsApp estilizado em ouro/ciano.
– Texto curto:
  “Conecte o número oficial do seu atendimento. É por aqui que sua Ginkgo vai conversar com o mundo.”
– Botão dourado: “Conectar WhatsApp”
– Estado conectado: mostrar um check dourado e animar as raízes ciano explodindo em luz.

Card 2: “Conectar Chatwoot (opcional)”
– Ícone de balão de chat.
– Campos básicos:
  – Input: “Base URL do seu Chatwoot”
  – Input: “API Token”
– Botão: “Salvar integração”
– Texto pequeno:
  “Usaremos isso para handoff: quando o cliente pedir humano, levamos a conversa para o Chatwoot.”

ABAIXO:
– Link pequeno, cinza discreto: “Pular por enquanto”.

BOTÕES:
– Esquerda: “Voltar”
– Direita: botão dourado “Continuar o crescimento →”.

EFEITOS:
– Ao conectar o WhatsApp, reproduzir animação + (se quiser) um som suave de “crescimento” (árvore + pulsos eletrônicos).
```

---

### 2.4 – Passo 3 – A Coroa (personalização do agente)

```markdown
Crie o PASSO 3 do wizard chamado “A Coroa”.

HEADER:
– Árvore quase completa: tronco + raízes.
– Falta apenas a copa. Exibir contornos de circuitos na parte de cima, esperando as folhas.

TÍTULO:
– “Deixe sua árvore florescer”

COPY:
– “Agora dê alma à sua Ginkgo.
   Ela vai falar com a voz da sua marca, lembrar de cada cliente,
   e nunca, nunca morrer.”

CAMPOS:
– Input: “Nome do seu agente”
  – Placeholder: “Ex: Luna, BRANN, João…”
– Chips de personalidade (selecionáveis, com feedback visual):
  [ Amigável ] [ Sarcástico ] [ Empático ] [ Luxuoso ] [ Minimalista ]
– Textarea: “Mensagem de saudação inicial”
  – Ao lado, um preview de uma tela de WhatsApp:
    – Nome do agente.
    – Foto de perfil com a logo Ginkgo.
    – A mensagem aparecendo em um balão de chat estilizado.
– Input tags: “Palavras-chave para falar com humano”
  – Placeholder: “falar com humano, atendente, suporte humano…”

ANIMAÇÃO:
– A cada campo preenchido, surgem novos ramos dourados com folhas hexagonais (como a sua logo).
– Quando todos os campos obrigatórios forem válidos, a copa se completa.

BOTÕES:
– Esquerda: “Voltar”
– Direita: botão dourado:
  “Concluir e despertar minha Ginkgo →”

AO CLICAR:
– A árvore se completa e explode em ouro brilhante com partículas douradas flutuando, transicionando para a tela final.
```

---

### 2.5 – Tela final secreta

```markdown
Crie a TELA FINAL do onboarding (“Tela secreta”).

VISUAL:
– Fundo preto profundo.
– Árvore de circuitos dourados completa no centro, pulsando levemente.
– Glow forte atrás da árvore.
– Partículas douradas flutuando de baixo para cima.

TEXTO:
– Título grande:
  “Sua Ginkgo está viva.”
– Subfrases aparecendo com delay dramático (fade-in):
  “Ela nunca dorme.”
  “Ela aprende com cada conversa.”
  “Ela floresce enquanto você descansa.”
  “Bem-vindo à eternidade.”

BOTÃO:
– Botão grande, dourado, pulsante:
  Texto: “Ver minha árvore em ação →”
  Ação: navegar para o /dashboard.

DETALHE:
– No canto inferior:
  “Dica: envie um ‘oi’ para o seu número conectado e veja sua Ginkgo responder pela primeira vez.”
```

---

### 2.6 – Mensagem automática de WhatsApp pós-onboarding

Use no n8n como primeira mensagem do agente ao terminar o onboarding:

```markdown
Oi, eu sou a {{agent_name}}, sua Ginkgo eterna 🌿✨  
Acabei de nascer e já estou pronta para cuidar dos seus clientes enquanto você descansa.  
Me testa agora: manda um “oi” aqui e vê como eu respondo. 🚀
```

---

## 3) Lottie JSON base – Árvore crescendo (seed → tronco → galhos)

Modelo simples para você importar no LottieFiles e estilizar (não é a versão final artística, é a base técnica):

```markdown
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 90,
  "w": 800,
  "h": 800,
  "nm": "ginkgo_tree_growth_base",
  "ddd": 0,
  "assets": [],
  "layers": [
    {
      "ddd": 0,
      "ind": 1,
      "ty": 4,
      "nm": "Seed",
      "sr": 1,
      "ks": {
        "o": { "a": 0, "k": 100 },
        "r": { "a": 0, "k": 0 },
        "p": { "a": 0, "k": [400, 500, 0] },
        "a": { "a": 0, "k": [0, 0, 0] },
        "s": {
          "a": 1,
          "k": [
            { "t": 0, "s": [0, 0, 100], "e": [100, 100, 100] },
            { "t": 20 }
          ]
        }
      },
      "shapes": [
        {
          "ty": "el",
          "p": { "a": 0, "k": [0, 0] },
          "s": { "a": 0, "k": [80, 80] },
          "nm": "Seed Path"
        },
        {
          "ty": "fl",
          "c": { "a": 0, "k": [1, 0.84, 0.0, 1] },
          "o": { "a": 0, "k": 100 },
          "nm": "Fill"
        }
      ],
      "ip": 0,
      "op": 90,
      "st": 0,
      "bm": 0
    },
    {
      "ddd": 0,
      "ind": 2,
      "ty": 4,
      "nm": "Trunk",
      "sr": 1,
      "ks": {
        "o": { "a": 0, "k": 100 },
        "r": { "a": 0, "k": 0 },
        "p": { "a": 0, "k": [400, 420, 0] },
        "a": { "a": 0, "k": [0, 0, 0] },
        "s": {
          "a": 1,
          "k": [
            { "t": 10, "s": [100, 0, 100], "e": [100, 100, 100] },
            { "t": 40 }
          ]
        }
      },
      "shapes": [
        {
          "ty": "rc",
          "p": { "a": 0, "k": [0, 0] },
          "s": { "a": 0, "k": [20, 200] },
          "r": { "a": 0, "k": 10 },
          "nm": "Trunk Path"
        },
        {
          "ty": "fl",
          "c": { "a": 0, "k": [1, 0.84, 0.0, 1] },
          "o": { "a": 0, "k": 100 },
          "nm": "Fill"
        }
      ],
      "ip": 10,
      "op": 90,
      "st": 10,
      "bm": 0
    },
    {
      "ddd": 0,
      "ind": 3,
      "ty": 4,
      "nm": "Branches",
      "sr": 1,
      "ks": {
        "o": {
          "a": 1,
          "k": [
            { "t": 25, "s": [0], "e": [100] },
            { "t": 55 }
          ]
        },
        "r": { "a": 0, "k": 0 },
        "p": { "a": 0, "k": [400, 300, 0] },
        "a": { "a": 0, "k": [0, 0, 0] },
        "s": { "a": 0, "k": [100, 100, 100] }
      },
      "shapes": [
        {
          "ty": "sh",
          "ks": {
            "a": 0,
            "k": {
              "i": [[0, 0], [0, 0], [0, 0]],
              "o": [[0, 0], [0, 0], [0, 0]],
              "v": [[0, 0], [-80, -80], [80, -80]],
              "c": false
            }
          },
          "nm": "Branches Path"
        },
        {
          "ty": "st",
          "c": { "a": 0, "k": [1, 0.84, 0.0, 1] },
          "w": { "a": 0, "k": 8 },
          "lc": 2,
          "lj": 2,
          "nm": "Stroke"
        }
      ],
      "ip": 25,
      "op": 90,
      "st": 25,
      "bm": 0
    }
  ]
}
```

Você pode duplicar/variar esse JSON para:

- versão semente (Passo 0/Boas-vindas),
- versão semente+tronco (Passo 1),
- versão com raízes e mais galhos (Passo 2),
- versão completa com mais ramos/folhas (Passo 3 e tela final).

Se quiser no próximo passo, posso mapear esse onboarding para a estrutura de rotas/páginas do seu Next.js (com componentes e nomes de arquivos) já pronto para conectar Supabase + Stripe + Evolution.