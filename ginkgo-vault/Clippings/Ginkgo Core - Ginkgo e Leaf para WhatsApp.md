---
title: "Ginkgo Core - Ginkgo e Leaf para WhatsApp"
source: "https://chatgpt.com/g/g-p-68e0a0b393cc8191a0f44ad743e1117d/c/69517b82-7c00-832f-9246-b47cef2a1ab6"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
dom., 28 de dez. às 22:27

Sim — uma hero nesse estilo é uma escolha forte para a Ginkgo/Leaf. É “premium SaaS” na veia e cria aquela sensação de produto vivo (o cérebro do usuário entende: *isso não é landing genérica*). Só precisa usar com disciplina: **1 hero animada + resto limpo**, senão vira parque de diversões e mata conversão.

Abaixo vai o guia completo pra integrar e usar isso no teu projeto (Next.js + shadcn + Tailwind + TypeScript).

---

## 1) Checagem rápida do codebase (shadcn + Tailwind + TS)

### Se já for um projeto Next.js com TS

- Confere se existem:
	- `tsconfig.json`
		- `tailwind.config.(js|ts)`
		- `postcss.config.js`
		- pasta `components/ui`

### Se NÃO tiver shadcn/tailwind/typescript

Use o caminho padrão e limpo:

**Criar Next.js com TS**

```markdown
npx create-next-app@latest ginkgo-leaf --ts --tailwind --eslint --app
cd ginkgo-leaf
```

**Inicializar shadcn/ui**

```markdown
npx shadcn@latest init
```

> O shadcn normalmente configura o alias `@/` e usa `components/ui` como casa dos componentes.

---

## 2) Caminhos padrão (componentes e estilos)

### Componentes

Padrão shadcn:

- `./components/ui`

Se seu projeto não tiver isso, crie:

```markdown
mkdir -p components/ui
```

**Por que é importante?**

- Mantém compatibilidade com exemplos/boilerplates shadcn
- Facilita upgrades e manutenção
- Evita espalhar UI primitives por `src/components` sem padrão
- O import do demo já assume: `@/components/ui/...`

### Estilos

Padrão comum em Next App Router:

- `app/globals.css`

(ou `src/app/globals.css` se você usa `src/`)

---

## 3) Copiar os arquivos para os lugares certos

### A) components/ui/container-scroll-animation.tsx

Crie o arquivo exatamente aqui:

- `components/ui/container-scroll-animation.tsx`

Cole o conteúdo fornecido.

> Observação: no seu código, o `Card` recebe `translate` no type mas não usa. Não quebra, mas dá warning. Se quiser limpar, eu já deixei um patch mais abaixo.

### B) Componente demo (onde você usa a hero)

Sugestão de path:

- `components/hero-scroll-demo.tsx` (ou `app/(marketing)/_components/hero-scroll-demo.tsx`)

---

## 4) Instalar dependências externas

### framer-motion

```markdown
npm i framer-motion
```

### lucide-react (se ainda não tiver no projeto)

```markdown
npm i lucide-react
```

---

## 5) Ajustar para Next/Image com assets reais (Unsplash)

Você pediu para usar imagens que “existem”. Unsplash é estável, mas o Next Image pode bloquear domínio.

### A) Adicionar domínio no next.config.js

```markdown
/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [
      { protocol: "https", hostname: "images.unsplash.com" },
    ],
  },
};

module.exports = nextConfig;
```

---

## 6) Implementação: Hero “Leaf no WhatsApp” nesse estilo

### components/hero-scroll-demo.tsx

```markdown
"use client";

import React from "react";
import Image from "next/image";
import { ContainerScroll } from "@/components/ui/container-scroll-animation";
import { Sparkles, MessageCircle, ShieldCheck } from "lucide-react";

export function HeroScrollDemo() {
  return (
    <section className="w-full">
      {/* Ajuste esses paddings conforme sua página.
         O demo original tinha pt-[1000px] e pb-[500px] pra testar scroll.
         Em site real, isso costuma ser exagerado. */}
      <div className="flex flex-col overflow-hidden pt-24 pb-24 md:pt-32 md:pb-32">
        <ContainerScroll
          titleComponent={
            <div className="px-4">
              <div className="mx-auto mb-4 inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm text-white/80 backdrop-blur">
                <Sparkles className="h-4 w-4" />
                LEAF • Agente de IA no WhatsApp
              </div>

              <h1 className="mx-auto max-w-4xl text-balance text-4xl font-semibold text-white md:text-6xl">
                LEAF: sua{" "}
                <span className="bg-gradient-to-r from-indigo-300 via-purple-300 to-cyan-200 bg-clip-text text-transparent">
                  SecretarIA
                </span>{" "}
                no WhatsApp que trabalha 24/7
              </h1>

              <p className="mx-auto mt-4 max-w-2xl text-pretty text-base text-white/70 md:text-lg">
                Atende, entende, qualifica e registra tudo automaticamente — sem
                perder leads, sem “deixa pra depois”.
              </p>

              <div className="mx-auto mt-7 flex flex-col items-center justify-center gap-3 sm:flex-row">
                <a
                  href="#whatsapp"
                  className="inline-flex w-full items-center justify-center gap-2 rounded-xl bg-indigo-500 px-6 py-3 text-sm font-semibold text-white shadow-lg shadow-indigo-500/20 hover:bg-indigo-400 sm:w-auto"
                >
                  <MessageCircle className="h-4 w-4" />
                  Falar no WhatsApp
                </a>

                <a
                  href="#como-funciona"
                  className="inline-flex w-full items-center justify-center gap-2 rounded-xl border border-white/15 bg-white/5 px-6 py-3 text-sm font-semibold text-white/90 hover:bg-white/10 sm:w-auto"
                >
                  <ShieldCheck className="h-4 w-4" />
                  Ver como funciona
                </a>
              </div>

              <div className="mx-auto mt-6 flex max-w-3xl flex-wrap items-center justify-center gap-3 text-xs text-white/60">
                <span className="rounded-full border border-white/10 bg-white/5 px-3 py-1">
                  Captação e qualificação
                </span>
                <span className="rounded-full border border-white/10 bg-white/5 px-3 py-1">
                  Agendamento automático
                </span>
                <span className="rounded-full border border-white/10 bg-white/5 px-3 py-1">
                  Relatórios e handoff humano
                </span>
              </div>
            </div>
          }
        >
          <div className="relative h-full w-full">
            <Image
              src="https://images.unsplash.com/photo-1555949963-aa79dcee981c?auto=format&fit=crop&w=2400&q=80"
              alt="Dashboard abstrato em tela"
              fill
              className="rounded-2xl object-cover"
              priority
              draggable={false}
            />

            {/* overlay para combinar com o tema escuro */}
            <div className="absolute inset-0 rounded-2xl bg-gradient-to-t from-black/60 via-black/20 to-black/10" />

            {/* “fake UI” minimalista (opcional) */}
            <div className="absolute bottom-6 left-6 right-6 rounded-2xl border border-white/10 bg-black/40 p-4 backdrop-blur">
              <div className="flex items-center justify-between">
                <div className="text-sm font-semibold text-white">
                  Atendimento • WhatsApp
                </div>
                <div className="text-xs text-white/70">24/7</div>
              </div>
              <div className="mt-3 grid grid-cols-3 gap-3">
                <div className="rounded-xl bg-white/5 p-3">
                  <div className="text-xs text-white/60">Leads hoje</div>
                  <div className="text-lg font-bold text-white">42</div>
                </div>
                <div className="rounded-xl bg-white/5 p-3">
                  <div className="text-xs text-white/60">Respondidos</div>
                  <div className="text-lg font-bold text-white">100%</div>
                </div>
                <div className="rounded-xl bg-white/5 p-3">
                  <div className="text-xs text-white/60">Qualificados</div>
                  <div className="text-lg font-bold text-white">18</div>
                </div>
              </div>
            </div>
          </div>
        </ContainerScroll>
      </div>
    </section>
  );
}
```

### Como usar na página (ex.: app/page.tsx)

```markdown
import { HeroScrollDemo } from "@/components/hero-scroll-demo";

export default function Page() {
  return (
    <>
      <HeroScrollDemo />
      {/* resto do site */}
      <section id="como-funciona" className="min-h-[50vh]" />
      <section id="whatsapp" className="min-h-[50vh]" />
    </>
  );
}
```

---

## 7) Patch opcional (tirar warning do translate não usado)

Se quiser deixar perfeito: no `Card` remova `translate` do type e do destructuring.

**Antes**

```markdown
export const Card = ({
  rotate,
  scale,
  children,
}: {
  rotate: MotionValue<number>;
  scale: MotionValue<number>;
  translate: MotionValue<number>;
  children: React.ReactNode;
}) => {
```

**Depois**

```markdown
export const Card = ({
  rotate,
  scale,
  children,
}: {
  rotate: MotionValue<number>;
  scale: MotionValue<number>;
  children: React.ReactNode;
}) => {
```

E onde chama:

```markdown
<Card rotate={rotate} translate={translate} scale={scale}>
```

vira:

```markdown
<Card rotate={rotate} scale={scale}>
```

---

## 8) Respostas diretas às “perguntas que importam” (pra você decidir rápido)

- **Que props vão entrar?**  
	`titleComponent` (ReactNode) + `children` (qualquer coisa). Ótimo para “Hero + mock de UI”.
- **Precisa state management?**  
	Não. Só `useScroll` e um `isMobile` interno.
- **Assets?**  
	Só a imagem (Unsplash) ou um mock de dashboard. Dá pra trocar por screenshot do teu produto depois.
- **Responsivo?**  
	Sim, ele reduz o scale no mobile. Recomendo **limitar altura** e evitar padding absurdo do demo.
- **Melhor lugar pra usar?**  
	Topo da home, como **única seção “cinematográfica”**. O resto: clean, bullets, prova, CTA.

---

## Minha recomendação (de produto, sem romance)

Faz.  
Só troca a vibe “carinho/conexões reais” por **“operações / resposta / registro / conversão”**. O efeito é: você para de parecer “chatbot fofinho” e começa a parecer **infra de receita**.

Se você me mandar:

1. qual framework do site (Next App Router ou Vite?)
2. se a estrutura usa `src/` ou não  
	eu ajusto os caminhos exatamente no padrão do teu repo e já te devolvo os prompts “pronto-copia-cola” por seção do Lovable.

Ginkgo-AI-Systems (4).pdf

PDF

quero que voce reescreva essas ideias mais acertiva e focada em uma pagina de apresentação com o efeito home que te dissse, em prompt para usar na manus,

Perfeito. Vou te entregar **UM PROMPT ÚNICO, cirúrgico e pronto pra colar na MANUS**, já **reescrevendo TODAS as ideias** do PDF e das conversas, mas **adaptadas para uma página de apresentação com HERO animado (scroll effect)**.

Sem storytelling pessoal, sem “manifesto longo”.  
Aqui é **home page que converte**, com narrativa clara, direta e moderna.

---

## 🎯 PROMPT MASTER — HOME PAGE GINKGO AI SYSTEMS (LEAF)

> **Use este prompt na MANUS para gerar a página inteira (copy + estrutura), focada em uma HERO com efeito scroll animado e restante clean, orientado a conversão.**

---

## PROMPT

```markdown
Crie uma página de apresentação (landing page) para a empresa Ginkgo AI Systems, com foco principal no produto LEAF.

O objetivo da página é:
- Apresentar a Ginkgo como uma empresa de automação e agentes de IA
- Posicionar o LEAF como um agente de IA para WhatsApp
- Converter visitantes em conversas no WhatsApp ou pedidos de demonstração

A página deve ter tom:
- Profissional
- Direto
- Tecnológico
- Focado em resultado operacional
Evite linguagem emocional, pessoal ou motivacional demais.

Estruture a página seguindo este fluxo:

====================
HERO SECTION (com efeito scroll animado)
====================

Título principal (impacto imediato):
"LEAF: o agente de IA no WhatsApp que atende, organiza e converte 24/7"

Subtítulo:
"Atendimento inteligente via WhatsApp que conversa com clientes, entende intenções, registra dados e executa tarefas automaticamente."

Elementos de apoio no HERO:
- Destaque visual de um dashboard ou interface abstrata
- Sensação de produto vivo, tecnológico e premium
- Scroll animation suave (produto se revela conforme o usuário desce)

CTAs:
- Botão primário: "Falar com o LEAF no WhatsApp"
- Botão secundário: "Ver como funciona"

Micro-bullets abaixo do CTA:
- Atendimento automático 24/7
- Captação e qualificação de leads
- Agendamento e relatórios automáticos
- Handoff humano quando necessário

====================
O QUE É A GINKGO
====================

Título:
"Ginkgo AI Systems"

Texto curto:
"A Ginkgo AI Systems cria agentes de IA e fluxos automatizados para transformar operações manuais em sistemas inteligentes, escaláveis e confiáveis."

Complemento:
"Nosso foco é aplicar inteligência artificial de forma prática, integrada ao dia a dia das empresas."

====================
O QUE É O LEAF
====================

Título:
"O que é o LEAF?"

Texto:
"O LEAF é um agente de IA que opera diretamente no WhatsApp. Ele atende clientes, entende mensagens, coleta informações, registra dados e executa ações automaticamente."

Destaque:
"O LEAF não é um chatbot genérico. É um sistema de atendimento conectado à operação real do negócio."

====================
O QUE O LEAF FAZ (FUNCIONALIDADES)
====================

Liste em cards objetivos:

- Atendimento automático no WhatsApp 24/7
  Responde clientes instantaneamente, sem filas ou horários.

- Captação e qualificação de leads
  Faz perguntas inteligentes e identifica oportunidades reais.

- Agendamento automático
  Marca horários, confirma compromissos e envia lembretes.

- Envio de propostas e documentos
  Automatiza orçamentos, PDFs e mensagens importantes.

- Relatórios e histórico
  Registra conversas, leads e resultados em banco de dados.

- Handoff humano
  Encaminha a conversa para uma pessoa quando necessário, com todo o contexto.

====================
COMO FUNCIONA
====================

Título:
"Como funciona"

Passos claros:

1. Diagnóstico rápido  
   Entendimento do negócio e definição dos fluxos.

2. Implementação  
   Configuração do LEAF para o WhatsApp do cliente.

3. Testes controlados  
   Validação do atendimento em ambiente real.

4. Produção  
   Agente ativo com monitoramento e melhorias contínuas.

Frase de apoio:
"Implementação enxuta, sem burocracia e com prazos claros."

====================
PARA QUEM É
====================

Título:
"Para quem o LEAF é ideal"

Liste segmentos:
- Empresas de serviços
- Clínicas e profissionais da saúde
- Corretores e imobiliárias
- Lojas e restaurantes
- Gestores de tráfego e marketing
- Pequenas e médias empresas que usam WhatsApp como principal canal

====================
RESULTADOS QUE IMPORTAM
====================

Cards de resultado:

- Resposta imediata  
  Nenhum cliente fica sem retorno.

- Menos tarefas repetitivas  
  Menos trabalho manual, mais foco estratégico.

- Mais conversões  
  Leads atendidos rápido convertem mais.

- Controle e rastreio  
  Tudo registrado, organizado e acessível.

====================
POSICIONAMENTO E COMPARAÇÃO
====================

Texto curto:
"Em vez de depender de atendimento manual, o LEAF executa tarefas de forma contínua, sem pausas, atrasos ou perda de informação."

Complemento:
"Mais eficiência, menos custo fixo e mais previsibilidade operacional."

====================
CTA FINAL
====================

Título:
"Seu WhatsApp pode trabalhar por você."

Texto:
"Veja o LEAF atendendo clientes reais em tempo real."

CTA principal:
"Falar com o LEAF no WhatsApp"

====================
RODAPÉ
====================

Inclua:
- Ginkgo AI Systems
- Produtos: LEAF (disponível), WAVE (em breve), PYRE (em breve)
- Redes sociais
- Política de privacidade e termos

A página deve ser pensada como uma home moderna de SaaS B2B, com foco em clareza, conversão e percepção de produto robusto.
```

---

## 🔥 Por que esse prompt está “no ponto”

- Condensa **10 páginas do PDF** em **1 narrativa clara**
- Elimina excesso de pessoalidade
- Alinha com **hero animado + SaaS moderno**
- Posiciona LEAF como **infraestrutura de operação**, não “robô fofo”
- Pronto para:
	- Lovable
		- Manus
		- V0
		- Qualquer gerador de UI

---

Se quiser, próximo passo eu posso:

- Ajustar esse prompt para **versão internacional (EN)**
- Criar um **prompt exclusivo só para o HERO (motion-first)**
- Ou quebrar em **prompts por seção** pra refinar uma a uma na Manus

Você decide o próximo movimento.

Ginkgo AI Systems Produto Planos Para quem é FAQ WhatsApp Falar com Agente LEAF Produto LEAF LEAF: seu agente de IA no WhatsApp que atende, organiza e converte 24/7 Atendimento inteligente via WhatsApp que conversa, entende, registra dados e executa tarefas automaticamente — enquanto você foca no crescimento do negócio. Falar com o LEAF no WhatsApp Ver como funciona Ver Planos → Ginkgo AI Systems A Ginkgo AI Systems cria agentes de IA e fluxos automatizados para transformar operações manuais em sistemas inteligentes, escaláveis e confiáveis. Nosso foco é aplicar inteligência artificial de forma prática, integrada ao dia a dia das empresas. O que é o LEAF? O LEAF é um agente de IA que opera diretamente no WhatsApp. Ele atende clientes, entende mensagens, coleta informações, registra dados e executa ações automaticamente. O LEAF não é um chatbot genérico. É um sistema de atendimento conectado à operação real do negócio. O que o LEAF faz Atendimento automático no WhatsApp 24/7 Responde clientes instantaneamente, sem filas ou horários. Captação e qualificação de leads Faz perguntas inteligentes e identifica oportunidades reais. Agendamento automático Marca horários, confirma compromissos e envia lembretes. Envio de propostas e documentos Automatiza orçamentos, PDFs e mensagens importantes. Relatórios e histórico Registra conversas, leads e resultados em banco de dados. Handoff humano Encaminha a conversa para uma pessoa quando necessário, com todo o contexto. Processo Como funciona Implementação enxuta, sem burocracia e com prazos claros. 01 Diagnóstico rápido (1–2 dias) Analisamos seu WhatsApp e identificamos oportunidades de automação. 02 Implementação do LEAF Configuração personalizada do agente para o seu negócio. 03 Testes reais no WhatsApp Validação com clientes reais em ambiente controlado. 04 Produção com monitoramento Ativação completa com acompanhamento contínuo e ajustes. Resultados Resultados que importam Métricas reais que impactam diretamente o seu negócio. Resposta imediata Clientes atendidos na hora, sem perder oportunidades. Menos tarefas repetitivas Menos mensagens manuais, mais tempo para decisões estratégicas. Mais conversões Leads respondidos rápido convertem mais. Controle e rastreio Todas as conversas registradas e organizadas automaticamente. Para quem o LEAF é ideal Empresas de serviços Clínicas e profissionais da saúde Corretores e imobiliárias Lojas e restaurantes Gestores de tráfego e marketing Pequenas e médias empresas que usam WhatsApp como principal canal Em vez de depender de atendimento manual, o LEAF executa tarefas de forma contínua, sem pausas, atrasos ou perda de informação. Mais eficiência, menos custo fixo e mais previsibilidade operacional. Casos de Uso Como empresas usam o LEAF na prática Cenários reais de aplicação em diferentes segmentos. "Antes: demora no atendimento e leads perdidos. Depois: respostas imediatas e leads organizados automaticamente." Empresa de serviços Consultoria e manutenção "Antes: mensagens perdidas e desorganização. Depois: clientes qualificados automaticamente e agendas sincronizadas." Imobiliária Venda e locação de imóveis "Antes: equipe sobrecarregada com tarefas repetitivas. Depois: atendimento 24/7 e time focado em casos complexos." Clínica de estética Agendamentos e consultas Planos Escolha sua plataforma Comece com LEAF ou aguarde o lançamento de WAVE e PYRE. Todas as plataformas trabalham 24/7 sem férias. DISPONÍVEL LEAF LEAF Atendimento e operação inteligente via WhatsApp, 24/7 R$ 449/mês Focado exclusivamente em WhatsApp para máxima eficiência Atendimento 24/7 Captação & Qualificação de leads Agendamento automático Propostas & Documentos Relatórios & Insights Handoff humano Operação exclusiva no WhatsApp ROI Equivale a menos de 1h de atendente/mês — trabalha 720h Começar Agora EM BREVE WAVE WAVE Gestor de Tráfego IA R$ 749/mês Campanhas otimizadas automaticamente Otimização automática de campanhas Análise de ROI em tempo real Criação de anúncios A/B testing automático Relatórios de performance Integração com Meta Ads e Google Ads ROI Gestor de tráfego: R$ 3.000+/mês — economize 95% Entrar na fila de espera EM BREVE PYRE PYRE Social Media IA R$ 1.199/mês Conteúdo diário no piloto automático Posts automáticos diários Vídeos curtos (Reels/Shorts) gerados por IA Calendário editorial de 30 dias Copys alinhadas ao nicho Templates da marca Análise de engajamento ROI Social media profissional: R$ 2.500+/mês — economize 96% Entrar na fila de espera PERSONALIZADO Enterprise A Ginkgo é especialista em criar qualquer solução digital sob medida: sites, plataformas, aplicativos, sistemas, dashboards, integrações complexas. Imagine, e nós criamos. Sites e landing pages de alta conversão Plataformas web e aplicativos mobile customizados Sistemas de gestão e dashboards inteligentes Integrações com ERPs, APIs e sistemas legados LEAF + WAVE + PYRE + qualquer outra solução que você imaginar Consultoria estratégica e suporte dedicado 24/7 Sob consulta Falar com especialista Investimento que se paga sozinho: Compare o custo de uma plataforma Ginkgo com o valor de contratar um profissional especializado. Nossa IA trabalha 24/7, não tira férias e está sempre atualizada com as melhores práticas do mercado. Perguntas Frequentes O que exatamente é o LEAF? O LEAF é só um chatbot? O LEAF substitui pessoas? Quanto tempo leva para implementar o LEAF? Preciso ter conhecimento técnico? Posso integrar com meu CRM atual? A IA responde qualquer coisa sozinha? Existe handoff para atendimento humano? Posso começar no plano básico e fazer upgrade depois? O LEAF funciona 24/7 mesmo? Meus dados ficam seguros? Pronto para começar? Seu WhatsApp pode trabalhar por você. Veja o LEAF atendendo clientes reais em tempo real. Conversar com um Agente Falar no WhatsApp Ginkgo AI Systems Ginkgo AI Systems Transformando empresas em máquinas enxutas com inteligência artificial. Menos fricção, mais execução. Produtos LEAF - Atendimento IA WAVE - Tráfego IA (em breve) PYRE - Social Media IA (em breve) Enterprise Redes Sociais Instagram TikTok YouTube X (Twitter) Comunidade Discord LinkedIn Facebook WhatsApp © 2025 Ginkgo AI Systems. Todos os direitos reservados. Política de Privacidade Termos de Uso LGPD esse e o texto inteiro, ajuste para o padrao ginkgo

Perfeito. O conteúdo está **completo e bem estruturado** — agora o ajuste é **refinar linguagem, padronizar tom Ginkgo e deixar tudo ainda mais assertivo, técnico e premium**, sem perder clareza.

Abaixo está o **TEXTO INTEGRAL REESCRITO NO PADRÃO GINKGO AI SYSTEMS**, pronto para substituir o atual **sem mudar a estrutura da página** (hero, seções, planos, FAQ etc.).

Use exatamente como copy final.

---

## Ginkgo AI Systems

**Automação inteligente para operações que precisam escalar.**

Produto  
Planos  
Para quem é  
FAQ  
WhatsApp  
Falar com Agente

---

## LEAF — Produto

### LEAF: o agente de IA no WhatsApp que atende, organiza e converte 24/7

Atendimento inteligente via WhatsApp que conversa com clientes, entende intenções, registra dados e executa tarefas automaticamente — enquanto sua operação ganha velocidade, organização e previsibilidade.

**Falar com o LEAF no WhatsApp**  
**Ver como funciona**  
Ver Planos →

---

## Ginkgo AI Systems

A **Ginkgo AI Systems** desenvolve agentes de IA e fluxos automatizados para transformar operações manuais em sistemas inteligentes, escaláveis e confiáveis.

Aplicamos inteligência artificial de forma prática, integrada ao dia a dia das empresas, com foco em eficiência operacional, redução de custos e aumento de conversão.

---

## O que é o LEAF?

O **LEAF** é um agente de IA que opera diretamente no WhatsApp.  
Ele atende clientes, entende mensagens, coleta informações, registra dados e executa ações automaticamente.

O LEAF **não é um chatbot genérico**.  
É um sistema de atendimento conectado à operação real do negócio, desenhado para funcionar em produção.

---

## O que o LEAF faz

**Atendimento automático no WhatsApp 24/7**  
Responde clientes instantaneamente, sem filas, horários ou atrasos.

**Captação e qualificação de leads**  
Faz perguntas inteligentes e identifica oportunidades reais de negócio.

**Agendamento automático**  
Marca horários, confirma compromissos e envia lembretes sem intervenção manual.

**Envio de propostas e documentos**  
Automatiza orçamentos, PDFs e mensagens estratégicas.

**Relatórios e histórico**  
Registra conversas, leads e resultados de forma organizada e rastreável.

**Handoff humano**  
Encaminha a conversa para uma pessoa quando necessário, com todo o contexto.

---

## Processo

### Como funciona

Implementação enxuta, sem burocracia e com prazos claros.

**01 — Diagnóstico rápido (1–2 dias)**  
Análise do WhatsApp e identificação das oportunidades de automação.

**02 — Implementação do LEAF**  
Configuração personalizada do agente para o seu negócio.

**03 — Testes reais no WhatsApp**  
Validação com clientes reais em ambiente controlado.

**04 — Produção com monitoramento**  
Ativação completa com acompanhamento contínuo e ajustes.

---

## Resultados

### Resultados que importam

Métricas reais que impactam diretamente o negócio.

**Resposta imediata**  
Clientes atendidos na hora, sem perder oportunidades.

**Menos tarefas repetitivas**  
Menos mensagens manuais, mais foco estratégico.

**Mais conversões**  
Leads respondidos rápido convertem mais.

**Controle e rastreio**  
Conversas organizadas, registradas e acessíveis.

---

## Para quem o LEAF é ideal

- Empresas de serviços
- Clínicas e profissionais da saúde
- Corretores e imobiliárias
- Lojas e restaurantes
- Gestores de tráfego e marketing
- Pequenas e médias empresas que usam WhatsApp como principal canal

Em vez de depender de atendimento manual, o LEAF executa tarefas de forma contínua, sem pausas, atrasos ou perda de informação.

Mais eficiência, menos custo fixo e mais previsibilidade operacional.

---

## Casos de Uso

### Como empresas usam o LEAF na prática

Cenários reais de aplicação em diferentes segmentos.

**Empresa de serviços — consultoria e manutenção**  
Antes: demora no atendimento e leads perdidos.  
Depois: respostas imediatas e leads organizados automaticamente.

**Imobiliária — venda e locação**  
Antes: mensagens perdidas e desorganização.  
Depois: clientes qualificados e agendas sincronizadas.

**Clínica de estética — agendamentos**  
Antes: equipe sobrecarregada com tarefas repetitivas.  
Depois: atendimento 24/7 e equipe focada em casos complexos.

---

## Planos

### Escolha sua plataforma

Comece com LEAF ou aguarde o lançamento de WAVE e PYRE.  
Todas as plataformas trabalham 24/7, sem férias.

---

### DISPONÍVEL — LEAF

**Atendimento e operação inteligente via WhatsApp**

**R$ 449/mês**

Focado exclusivamente em WhatsApp para máxima eficiência.

- Atendimento 24/7
- Captação e qualificação de leads
- Agendamento automático
- Propostas e documentos
- Relatórios e insights
- Handoff humano
- Operação exclusiva no WhatsApp

**ROI**  
Equivale a menos de 1h de atendente/mês — opera 720h.

**Começar agora**

---

### EM BREVE — WAVE

**Gestor de Tráfego com IA**

**R$ 749/mês**

Campanhas otimizadas automaticamente.

- Otimização automática de campanhas
- Análise de ROI em tempo real
- Criação de anúncios
- A/B testing automático
- Relatórios de performance
- Integração com Meta Ads e Google Ads

**ROI**  
Gestor de tráfego: R$ 3.000+/mês — economia de até 95%.

**Entrar na fila de espera**

---

### EM BREVE — PYRE

**Social Media com IA**

**R$ 1.199/mês**

Conteúdo diário no piloto automático.

- Posts automáticos
- Vídeos curtos (Reels/Shorts) por IA
- Calendário editorial de 30 dias
- Copys alinhadas ao nicho
- Templates da marca
- Análise de engajamento

**ROI**  
Social media profissional: R$ 2.500+/mês — economia de até 96%.

**Entrar na fila de espera**

---

### PERSONALIZADO — Enterprise

A Ginkgo cria soluções digitais sob medida: sistemas, plataformas, aplicativos, integrações e operações completas com IA.

- Sites e landing pages de alta conversão
- Plataformas web e aplicativos mobile
- Sistemas de gestão e dashboards inteligentes
- Integrações com ERPs, APIs e sistemas legados
- LEAF + WAVE + PYRE + soluções customizadas
- Consultoria estratégica e suporte dedicado 24/7

**Sob consulta**  
**Falar com especialista**

> Investimento que se paga sozinho: compare o custo de uma plataforma Ginkgo com a contratação de profissionais especializados. A IA opera 24/7, sem férias, com atualização contínua.

---

## Perguntas Frequentes

- O que exatamente é o LEAF?
- O LEAF é só um chatbot?
- O LEAF substitui pessoas?
- Quanto tempo leva para implementar o LEAF?
- Preciso ter conhecimento técnico?
- Posso integrar com meu CRM atual?
- A IA responde qualquer coisa sozinha?
- Existe handoff para atendimento humano?
- Posso começar no plano básico e fazer upgrade depois?
- O LEAF funciona 24/7 mesmo?
- Meus dados ficam seguros?

---

## Pronto para começar?

### Seu WhatsApp pode trabalhar por você.

Veja o LEAF atendendo clientes reais em tempo real.

**Conversar com um agente**  
**Falar no WhatsApp**

---

## Rodapé

**Ginkgo AI Systems**  
Transformando empresas em operações enxutas com inteligência artificial.  
Menos fricção. Mais execução.

**Produtos**  
LEAF — Atendimento IA  
WAVE — Tráfego IA (em breve)  
PYRE — Social Media IA (em breve)  
Enterprise

**Redes Sociais**  
Instagram · TikTok · YouTube · X (Twitter)

**Comunidade**  
Discord · LinkedIn · Facebook · WhatsApp