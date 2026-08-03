---
title: "Efeito 3D em Landing Pages"
source: "https://chatgpt.com/c/6a5f958b-ea60-83e9-8b2c-88d401e26db3"
author:
published:
created: 2026-07-21
description: "ChatGPT conversation with 2 messages"
tags:
  - "clippings"
---
**Você disse**

---

Esse post resume um padrão que está se tornando dominante no desenvolvimento de landing pages premium. O efeito "3D" não é um objeto 3D real na maioria dos casos. É uma ilusão construída com dezenas ou centenas de frames renderizados previamente.

### Como realmente funciona

Imagine um vídeo de 300 frames.

Em vez de reproduzir o vídeo normalmente:

```
Frame 1
Frame 2
Frame 3
...
Frame 300
```

o scroll da página controla qual frame aparece.

```
Scroll 0%  → Frame 1
Scroll 25% → Frame 75
Scroll 50% → Frame 150
Scroll 75% → Frame 225
Scroll100% → Frame 300
```

Na prática o usuário "arrasta" o vídeo com o mouse.

Isso produz aquela sensação de objeto girando em tempo real.

---

## Pipeline profissional

```
Blender
      │
Render de 200~600 frames
      │
PNG / WebP Sequence
      │
Canvas WebGL
      │
GSAP ou Anime.js
      │
ScrollTrigger
      │
Site
```

Esse é o fluxo usado por muitas experiências premiadas.

---

## GSAP

É praticamente o padrão da indústria para animações web.

Ideal para:

- ScrollTrigger
- timelines
- parallax
- pin sections
- canvas
- SVG
- WebGL
- sincronização perfeita

É difícil superar a GSAP quando o projeto exige controle absoluto.

---

## Anime.js

Excelente alternativa.

Hoje ela evoluiu bastante.

Vantagens:

- API extremamente simples
- open source
- ótima documentação
- perfeita para micros interações
- performance excelente

Para a maioria dos sites comerciais ela já resolve praticamente tudo.

---

## 21st.dev

Na minha opinião, é uma das bibliotecas mais úteis para quem trabalha com IA e geração rápida de interfaces.

Ela entrega componentes prontos:

- Hero Sections
- Glassmorphism
- Gradientes
- Cards
- Scroll Effects
- Cursor Effects
- Animated Buttons
- Backgrounds
- Text Reveal
- Bento Grids

O diferencial é que muitos componentes já podem ser consumidos diretamente por IA (Claude, Cursor, Windsurf) via MCP, acelerando muito a prototipação.

---

## Para a Ginkgo

Esse tipo de stack combina diretamente com a identidade premium que você vem desenhando.

## Site institucional

- Scroll cinematográfico
- Árvore Ginkgo crescendo conforme o scroll
- Ramos formando os produtos (Leaf, Wave, Pyre)
- Fundo com partículas douradas
- Morphing entre seções
- Text Reveal sincronizado

---

## Dashboard Leaf

Use animações discretas:

- Cards entrando suavemente
- Contadores animados
- Timeline viva
- Estados de IA pulsando

Evite exageros.

---

## Sylvia

O avatar pode surgir conforme o usuário entra na página.

Pequeno movimento de respiração.

Olhos acompanhando o cursor.

Partículas de folhas.

Tudo extremamente leve.

---

## Laplace

Aqui vale investir em algo mais cinematográfico.

Imagine um grafo neural crescendo.

Cada novo nó representa conhecimento adquirido.

Ao scroll:

```
Raiz

↓

Tronco

↓

Galhos

↓

Folhas

↓

Produtos

↓

Clientes

↓

Ecossistema
```

A navegação literalmente conta a história da empresa.

---

## Stack que eu adotaria

### Interface

- React
- Next.js
- Tailwind CSS

### Animação

- GSAP
- Anime.js
- Motion (Framer Motion)

### Efeitos

- Three.js (quando realmente precisar de 3D)
- React Three Fiber
- Lenis (scroll suave)
- OGL (WebGL extremamente leve)

### Componentes

- 21st.dev
- Magic UI
- Aceternity UI
- Origin UI
- Shadcn/UI

### IA

- Claude Code
- Cursor
- Windsurf

---

## O ponto mais importante do post

A última imagem é a que mais merece atenção:

> "Bonito que não vende é enfeite caro."

Essa é uma regra valiosa. Animação deve reforçar a mensagem, destacar a proposta de valor e conduzir o olhar até a ação principal (cadastro, demonstração, contato ou compra). Se o efeito aumenta o tempo de carregamento, prejudica a navegação ou distrai do objetivo, ele deixa de ser um recurso de UX e passa a ser apenas decoração.

Para a Ginkgo, a estratégia ideal é construir uma identidade visual memorável com animações de alto impacto na página institucional e landing pages, enquanto mantém o produto (Leaf, Wave e Pyre) rápido, responsivo e orientado à produtividade.