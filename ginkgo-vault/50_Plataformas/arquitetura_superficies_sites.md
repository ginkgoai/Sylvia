# Arquitetura de superfícies — sites + app (plano — 04/07)

> Como dividir as telas: **site institucional** + **3 produtos divididos** (LEAF/PYRE/WAVE), cada um com formato + CTA. Estilo-alvo = `estilo_pierre_diretriz.md`. Eles **só cruzam** em: **cadastro/conta · tarefas · comunicação intra-agente**.

## O ajuste (o "correto, mas...")
- **SITES/marketing: DIVIDIDOS** ✓ — institucional + leaf + pyre + wave, cada um com posicionamento, formato e CTA próprios (SEO, clareza, funil).
- **APP: UNIFICADO** (recomendação) — **um** workspace "Ginkgo OS", **uma conta, uma carteira (GTK)**, com **módulos** LEAF/PYRE/WAVE (é o que já está construído: `/app/leaf/*`, e pyre/wave "em breve"). Cliente assina à la carte → o módulo comprado **acende**; os outros viram upsell. Um login, inbox/tasks/carteira unificados, e o **funil PYRE→WAVE→LEAF** flui sem troca de app. Mais simples e melhor UX que 3 apps separados — e casa com "uma conta, uma carteira, três mundos".
- Resumo: **superfícies de marca divididas; produto num app-com-módulos.**

## Onde cruzam (o backbone compartilhado — o que faz ser SUÍTE, não 3 ferramentas)
1. **Cadastro / conta:** um signup, uma identidade, uma **carteira GTK**, um billing (à la carte). (M5 já entrega o self-serve.)
2. **Tarefas:** o motor governado — **Task + budget + Evidence + honest-data**. Todo produto emite tasks na mesma esteira; a aba Atividade é compartilhada.
3. **Comunicação intra-agente:** agentes se falam **só por Events** (invariante). **Brann orquestra**; o funil passa o bastão: **PYRE cria → WAVE distribui/mede → LEAF converte**. Esse cruzamento é o diferencial vs concorrentes de produto único.

## Formato + CTA por superfície (estilo modo-Pierre: dark-elegante, chips de mascote, cards honest-data, voz 1ª pessoa)

| Superfície | Público | Formato | CTA |
|---|---|---|---|
| **Institucional** (ginkgosystems.tech) | leads + parceiros | marca-mãe: quem é (ginkgo/honest-data), os 3 mundos, o funil, IMAGINE/enterprise | "Conheça cada mundo" (roteia) + **"Contratar a Ginkgo" (IMAGINE)** |
| **LEAF** | SMB atendimento/vendas | Callima (chip de luz) + cards honest-data ("agendamento ✓ com prova") + voz 1ª pessoa | **"Conectar meu WhatsApp"** → trial → signup → app |
| **PYRE** | quem cria conteúdo | Nyra (chip) + galeria de criativos + calendário 30d + banco de hooks | **"Criar meu 1º conteúdo grátis"** → trial → signup |
| **WAVE** | quem roda tráfego | Alfred (chip) + painel de **métricas honestas** + funil + verba governada | **"Escalar meu tráfego"** → trial → signup |

- Cada CTA leva ao **mesmo cadastro** (uma conta) e acende o módulo certo no app.
- Honest-data no CTA: **teste grátis**, "cada ação vira tarefa auditável, com prova".

## Ordem de construção (marketing = Claude Design; produto = Fable, pós-core)
1. **Institucional** (o guarda-chuva + roteamento). 2. **LEAF** (é o que está vivo → converte já). 3. **PYRE / WAVE** (quando os módulos abrirem). Todos herdam o DS do Claude Design (2 registros + modo Pierre).
