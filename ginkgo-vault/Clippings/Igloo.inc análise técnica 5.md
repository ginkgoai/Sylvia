---
title: "Igloo.inc análise técnica"
source: "https://chatgpt.com/c/6a59dd94-674c-83e9-9108-e94beb00634f"
author:
published:
created: 2026-07-17
description: "ChatGPT conversation with 9 messages"
tags:
  - "clippings"
---
**Você disse**

igloo.inc me de odos os detalhes e é a parte tecnica de desenvolvimento de um site como esse

---

![https://assets.awwwards.com/awards/element/2024/06/66799402d00b4333947986.jpg](https://tse1.mm.bing.net/th/id/OIP.1BB7Mn13ekfzlLSg3DWkBwHaFj?r=0&w=474&h=474&c=7&p=0)

O **Igloo.inc** é um site institucional imersivo da empresa controladora por trás de projetos como Pudgy Penguins e OverpassIP. Em vez de funcionar como uma landing page comum, ele apresenta o portfólio como uma experiência audiovisual 3D, guiada pelo scroll. O projeto foi criado pela **Abeto**, em colaboração com a **Bureaux**, e recebeu o prêmio Site of the Day da Awwwards em julho de 2024. [^1]

A lógica central é:

> transformar uma holding de projetos Web3 em um universo visual congelado, onde cada empresa aparece encapsulada em uma estrutura de gelo.

Não é apenas um site com elementos 3D. É praticamente uma pequena aplicação gráfica em tempo real rodando dentro do navegador.

---

## 1\. O que existe no site

## 1.1 Tela inicial cinematográfica

A abertura funciona como uma introdução de filme:

- fundo escuro e atmosférico;
- identidade tipográfica minimalista;
- textos técnicos e institucionais;
- ruído, partículas e distorções;
- transições lentas e controladas;
- câmera virtual movimentando-se em um ambiente 3D.

O usuário não “entra numa página”. Ele entra numa cena.

A experiência utiliza uma estética entre:

- laboratório criogênico;
- terminal militar futurista;
- documentário científico;
- interface de nave espacial;
- apresentação de marca de luxo.

O objetivo não é entregar informações imediatamente. O objetivo é construir percepção de valor.

---

## 1.2 Navegação orientada pelo scroll

O scroll vertical controla uma linha do tempo interna.

Em vez de simplesmente mover a página para baixo, ele pode controlar:

- posição da câmera;
- rotação dos objetos;
- intensidade dos shaders;
- transição entre cenários;
- aparecimento e desaparecimento dos textos;
- deformações;
- partículas;
- mudança do projeto exibido.

Tecnicamente, o scroll funciona como um controle remoto de uma animação 3D.

Exemplo conceitual:

```
Scroll 0%    → introdução
Scroll 15%   → aproximação do primeiro objeto
Scroll 30%   → apresentação do projeto
Scroll 45%   → dissolução da cena
Scroll 60%   → segundo projeto
Scroll 85%   → manifesto institucional
Scroll 100%  → footer interativo
```

Esse tipo de arquitetura costuma usar uma timeline central sincronizada com a posição normalizada do scroll.

---

## 1.3 Portfólio encapsulado em gelo

Cada projeto é exibido dentro de uma estrutura cristalina própria.

O site não depende apenas de modelos de gelo feitos manualmente. Há relatos técnicos de que os cristais foram criados com um processo procedural que simula crescimento dentro de diferentes volumes. Isso permite gerar novas variações quando outro projeto é adicionado ao portfólio. [^2]

Isso resolve um problema importante:

```
Modelo manual:
novo projeto → modelar novo gelo → texturizar → iluminar → exportar

Modelo procedural:
novo projeto → escolher volume → gerar cristal → exportar automaticamente
```

É uma arquitetura preparada para escala, não apenas uma peça artística isolada.

---

## 1.4 Textos integrados ao WebGL

Uma das características mais incomuns é que parte relevante da interface é renderizada dentro do próprio ambiente WebGL, em vez de usar apenas HTML sobreposto.

Segundo a análise técnica publicada sobre o projeto, o site utiliza:

- texto baseado em texturas SDF;
- efeitos de embaralhamento de letras;
- offsets em atlas de caracteres;
- shaders para glitches;
- animações sem recalcular o layout do navegador a cada frame. [^2]

### SDF

SDF significa **Signed Distance Field**.

Em vez de renderizar letras como imagens fixas, o sistema guarda uma representação matemática simplificada da distância até as bordas da letra.

Isso permite:

- texto nítido em diferentes tamanhos;
- distorções;
- brilho;
- dissolução;
- glitch;
- transições;
- animação por shader.

É como transformar a tipografia em matéria programável.

---

## 1.5 Footer com partículas interativas

No final da experiência, partículas formam diferentes objetos ou silhuetas dependendo do link que o usuário seleciona.

O comportamento envolve:

- nuvem de partículas;
- posições-alvo;
- interpolação entre formatos;
- velocidade individual;
- alteração visual conforme o movimento;
- resposta ao hover.

O projeto também teria utilizado um conversor próprio para trazer dados volumétricos VDB para um formato leve o suficiente para navegadores. [^2]

O footer deixa de ser uma área burocrática e vira o último ato da experiência.

---

## 2\. Identidade visual

A Awwwards registra uma paleta principal baseada em dois tons:

- `#B6BAC5`
- `#383E4E`

A linguagem é essencialmente azul-acinzentada, metálica e fria. [^1]

## Componentes visuais

### Tipografia

- fonte grotesca ou sans-serif técnica;
- títulos em caixa alta;
- letras espaçadas;
- blocos pequenos de informação;
- estética de terminal;
- hierarquia baseada mais em posição e movimento do que em tamanho.

### Materiais

- gelo fosco;
- vidro;
- metal;
- partículas;
- névoa;
- superfícies refrativas;
- distorção cromática.

### Pós-processamento

Provavelmente são utilizados vários efeitos de pós-processamento:

- bloom;
- chromatic aberration;
- film grain;
- vignette;
- blur direcional;
- depth of field;
- color grading;
- noise;
- frost distortion.

A Awwwards classifica o projeto como experiência 3D, com animações, transições e scroll contínuo. [^1]

---

## 3\. Stack técnica identificada

A stack relatada para o projeto inclui:

| Camada | Tecnologia |
| --- | --- |
| Framework frontend | Svelte |
| Renderização 3D | Three.js |
| Motor gráfico | WebGL |
| Animações | GSAP |
| Modelagem 3D | Blender |
| Procedural e simulação | Houdini |
| Shaders | GLSL |
| Volumes e partículas | Dados VDB convertidos |
| Interface tipográfica | SDF textures |
| Hospedagem | Possivelmente CDN/edge deployment |
| Backend | Praticamente desnecessário para a experiência principal |

A combinação **Three.js + Svelte + GSAP + Houdini + Blender** foi mencionada em uma análise técnica do projeto. [^2]

O fórum oficial do Three.js também classifica o projeto nas áreas de shaders e animação. [^3]

## O que é confirmado e o que é inferido

### Confirmado por fontes públicas

- Three.js;
- WebGL;
- Svelte;
- GSAP;
- Blender;
- Houdini;
- shaders;
- geração procedural de cristais;
- partículas;
- interface parcialmente renderizada em WebGL.

### Provável, mas não confirmado diretamente

- Vite como bundler;
- CDN como Cloudflare ou similar;
- armazenamento de assets em object storage;
- uso de KTX2 ou Basis para texturas comprimidas;
- Draco ou Meshopt para geometria;
- pipeline CI/CD;
- worker para decodificação de assets;
- sistema próprio de gerenciamento de cenas.

---

## 4\. Arquitetura recomendada para construir algo semelhante

Uma arquitetura moderna e reproduzível seria:

```
Usuário
   │
   ▼
CDN / Edge
   │
   ├── HTML mínimo
   ├── JavaScript
   ├── shaders
   ├── modelos 3D
   ├── texturas comprimidas
   └── áudio
   │
   ▼
Aplicação SvelteKit
   │
   ├── UI DOM acessível
   ├── controle de navegação
   ├── carregamento de assets
   ├── gerenciamento de estado
   └── integração com analytics
   │
   ▼
Motor WebGL / Three.js
   │
   ├── SceneManager
   ├── CameraController
   ├── ScrollTimeline
   ├── ShaderManager
   ├── ParticleSystem
   ├── AssetLoader
   ├── PostProcessing
   └── PerformanceManager
```

## Estrutura de projeto

```
src/
├── app.html
├── routes/
│   ├── +page.svelte
│   ├── +layout.svelte
│   └── portfolio/
│       └── [slug]/
│           └── +page.svelte
│
├── lib/
│   ├── webgl/
│   │   ├── Experience.ts
│   │   ├── Renderer.ts
│   │   ├── Camera.ts
│   │   ├── SceneManager.ts
│   │   ├── AssetLoader.ts
│   │   ├── ScrollController.ts
│   │   ├── PostProcessing.ts
│   │   └── PerformanceMonitor.ts
│   │
│   ├── scenes/
│   │   ├── IntroScene.ts
│   │   ├── PortfolioScene.ts
│   │   ├── ManifestoScene.ts
│   │   └── FooterScene.ts
│   │
│   ├── objects/
│   │   ├── IceCrystal.ts
│   │   ├── ProductObject.ts
│   │   ├── ParticleCloud.ts
│   │   └── WebGLText.ts
│   │
│   ├── shaders/
│   │   ├── ice.vert
│   │   ├── ice.frag
│   │   ├── frost.vert
│   │   ├── frost.frag
│   │   ├── particles.vert
│   │   └── particles.frag
│   │
│   ├── stores/
│   │   ├── loading.ts
│   │   ├── navigation.ts
│   │   ├── audio.ts
│   │   └── quality.ts
│   │
│   └── components/
│       ├── Loader.svelte
│       ├── Header.svelte
│       ├── Navigation.svelte
│       ├── AccessibilityLayer.svelte
│       └── RotateDevice.svelte
│
├── assets/
│   ├── models/
│   ├── textures/
│   ├── fonts/
│   ├── audio/
│   └── environment/
│
└── data/
    └── projects.json
```

---

## 5\. Componentes técnicos fundamentais

## 5.1 Experience Controller

Um controlador central inicializa toda a aplicação gráfica.

```typescript
export class Experience {
  private renderer: Renderer;
  private camera: CameraController;
  private scenes: SceneManager;
  private scroll: ScrollController;

  constructor(canvas: HTMLCanvasElement) {
    this.renderer = new Renderer(canvas);
    this.camera = new CameraController();
    this.scenes = new SceneManager();
    this.scroll = new ScrollController();

    this.tick();
  }

  private tick = (): void => {
    const progress = this.scroll.getProgress();

    this.scenes.update(progress);
    this.camera.update(progress);
    this.renderer.render(this.scenes.current, this.camera.instance);

    requestAnimationFrame(this.tick);
  };
}
```

Esse controlador deve ser responsável por:

- iniciar a cena;
- carregar recursos;
- manter o render loop;
- atualizar os objetos;
- responder ao resize;
- pausar quando a aba não estiver visível;
- ajustar qualidade conforme o dispositivo.

---

## 5.2 Scroll Controller

O scroll não deve controlar diretamente cada componente. Ele deve ser convertido em um valor previsível, normalmente de `0` a `1`.

```typescript
export class ScrollController {
  private current = 0;
  private target = 0;

  update(): void {
    const maxScroll =
      document.documentElement.scrollHeight - window.innerHeight;

    this.target = maxScroll > 0
      ? window.scrollY / maxScroll
      : 0;

    this.current += (this.target - this.current) * 0.08;
  }

  getProgress(): number {
    return this.current;
  }
}
```

Depois, cada cena recebe um intervalo:

```typescript
const phases = {
  intro: [0, 0.18],
  firstProject: [0.18, 0.40],
  secondProject: [0.40, 0.62],
  manifesto: [0.62, 0.82],
  footer: [0.82, 1]
};
```

Assim, o site funciona como uma timeline não linear.

---

## 5.3 Scene Manager

Não convém manter todas as cenas pesadas renderizando ao mesmo tempo.

O Scene Manager deve:

- ativar a cena atual;
- preparar a próxima cena;
- desativar objetos distantes;
- liberar texturas;
- controlar transições;
- reduzir draw calls.
```typescript
interface SceneModule {
  enter(): Promise<void>;
  update(progress: number, delta: number): void;
  exit(): Promise<void>;
  dispose(): void;
}
```

Cada seção torna-se um módulo independente.

---

## 5.4 Shader de gelo

Um material de gelo convincente normalmente mistura:

- transmissão;
- refração;
- Fresnel;
- normal maps;
- noise procedural;
- absorção por profundidade;
- reflexos de ambiente;
- irregularidade interna.

Conceitualmente:

```glsl
float fresnel = pow(
  1.0 - dot(normalize(viewDirection), normalize(normal)),
  3.0
);

vec3 refractedColor = textureCube(
  environmentMap,
  refract(viewDirection, normal, refractionRatio)
).rgb;

float frost = noise(worldPosition * frostScale);

vec3 finalColor = mix(
  refractedColor,
  frostColor,
  frost * frostIntensity
);

finalColor += fresnel * edgeColor;
```

O desafio não é apenas criar transparência. Gelo real precisa parecer:

- espesso;
- imperfeito;
- parcialmente translúcido;
- internamente fragmentado;
- com bordas iluminadas;
- diferente de vidro puro.

---

## 5.5 Sistema de partículas

Uma implementação eficiente deve usar `BufferGeometry` ou GPU computation.

Cada partícula pode possuir:

```typescript
position
targetPosition
velocity
randomSeed
size
life
colorFactor
```

No vertex shader:

```glsl
vec3 direction = targetPosition - position;
vec3 animatedPosition = position + direction * transitionProgress;

animatedPosition += noiseOffset * turbulence;

gl_Position =
  projectionMatrix *
  modelViewMatrix *
  vec4(animatedPosition, 1.0);
```

Para milhares de partículas, a regra é simples:

> a CPU organiza; a GPU dança.

Mover dez mil elementos HTML seria um pequeno apocalipse de performance. Mover dez mil vértices num shader é rotina.

---

## 6\. Pipeline de produção 3D

## Etapa 1 — Conceito e storyboard

Antes do código:

- definir narrativa;
- desenhar sequência de cenas;
- especificar duração;
- mapear interações;
- determinar quais elementos precisam ser 3D;
- produzir animatic simples.

Ferramentas:

- Figma;
- FigJam;
- Blender;
- After Effects;
- Premiere;
- Rive para protótipos menores.

## Etapa 2 — Greybox

Criar uma versão sem materiais sofisticados:

- blocos simples;
- câmera;
- iluminação básica;
- duração das cenas;
- posição dos textos;
- transições.

O greybox evita gastar três semanas criando um cristal lindo que depois não cabe no enquadramento.

## Etapa 3 — Modelagem

No Blender:

- objetos principais;
- produtos;
- logotipos;
- superfícies;
- UV mapping;
- versões low-poly.

No Houdini:

- crescimento procedural;
- fragmentação;
- cristais;
- volumes;
- partículas;
- variações automáticas.

## Etapa 4 — Bake e exportação

Exportar:

- modelos em GLB;
- animações;
- normal maps;
- roughness;
- ambient occlusion;
- displacement;
- dados de partículas;
- pontos volumétricos.

## Etapa 5 — Compressão

Utilizar:

- Draco ou Meshopt para geometria;
- KTX2/Basis para texturas;
- WebP/AVIF para imagens;
- áudio em AAC ou Opus;
- lazy loading por cena.

## Etapa 6 — Integração WebGL

- importar os modelos;
- recriar materiais;
- programar shaders;
- sincronizar animações;
- implementar pós-processamento;
- ajustar a câmera;
- conectar tudo ao scroll.

---

## 7\. Performance

Esse tipo de site pode facilmente virar um forno portátil. É necessário tratar performance como parte do design.

## Metas recomendadas

| Item | Meta |
| --- | --- |
| JavaScript inicial | abaixo de 500 KB comprimidos |
| Cena inicial | abaixo de 3–5 MB |
| Total carregado progressivamente | 15–35 MB |
| Draw calls desktop | abaixo de 150 |
| Draw calls mobile | abaixo de 70 |
| FPS desktop | 50–60 |
| FPS mobile | 30–45 |
| Textura máxima mobile | 1K |
| Textura máxima desktop | 2K–4K seletivamente |

## Qualidade adaptativa

```typescript
function detectQuality(): "low" | "medium" | "high" {
  const memory = navigator.deviceMemory ?? 4;
  const cores = navigator.hardwareConcurrency ?? 4;
  const pixelRatio = window.devicePixelRatio;

  if (memory <= 4 || cores <= 4) return "low";
  if (memory <= 8 || pixelRatio > 2) return "medium";

  return "high";
}
```

A qualidade pode alterar:

- número de partículas;
- resolução;
- sombras;
- bloom;
- refração;
- antialiasing;
- textura;
- frequência de atualização.

## Renderização sob demanda

Não renderizar quando:

- a aba estiver escondida;
- o canvas estiver fora da viewport;
- a animação estiver parada;
- o usuário tiver ativado redução de movimento.

---

## 8\. Responsividade

Um site 3D não deve apenas “encolher” no celular.

É necessário criar outra direção de arte.

## Desktop

- câmera mais aberta;
- partículas completas;
- maior profundidade;
- efeitos de pós-processamento;
- tipografia espalhada;
- navegação baseada em cursor.

## Mobile

- câmera mais próxima;
- menos partículas;
- materiais simplificados;
- textos maiores;
- menor quantidade de blur;
- navegação por toque;
- rotação de objetos limitada;
- assets específicos para mobile.

O projeto recebeu avaliação relativamente forte em responsividade, mas notas mais modestas em acessibilidade, semântica e metadata na avaliação técnica da Awwwards. [^1]

Isso mostra o principal risco desse estilo: visual excelente, estrutura tradicional comprometida.

---

## 9\. SEO e acessibilidade

O erro clássico seria colocar tudo dentro do canvas.

Para evitar isso, a versão recomendada deve possuir uma camada HTML paralela:

```html
<main>
  <section aria-labelledby="intro-title">
    <h1 id="intro-title">Nome da empresa</h1>
    <p>Descrição institucional.</p>
  </section>

  <section aria-labelledby="portfolio-title">
    <h2 id="portfolio-title">Portfólio</h2>
    <!-- projetos -->
  </section>
</main>

<canvas aria-hidden="true"></canvas>
```

O canvas entrega a experiência visual.

O HTML entrega:

- indexação;
- leitores de tela;
- teclado;
- estrutura semântica;
- compartilhamento;
- fallback;
- conteúdo para mecanismos de busca.

Também deve existir:

```
@media (prefers-reduced-motion: reduce) {
  .motion-heavy {
    animation: none;
    transition: none;
  }
}
```

Para usuários com redução de movimento:

- desativar câmera agressiva;
- diminuir partículas;
- remover parallax;
- permitir navegação convencional.

---

## 10\. Backend necessário

Para um site puramente institucional, o backend pode ser mínimo.

## Versão simples

```
SvelteKit estático
        │
        ├── JSON do portfólio
        ├── formulário externo
        ├── analytics
        └── CDN
```

## Versão escalável

```
SvelteKit
   │
   ├── Headless CMS
   │     ├── projetos
   │     ├── textos
   │     ├── equipe
   │     └── notícias
   │
   ├── API
   │     ├── contato
   │     ├── newsletter
   │     └── analytics
   │
   └── Object Storage
         ├── modelos
         ├── texturas
         ├── vídeos
         └── áudio
```

CMS recomendados:

- Sanity;
- Strapi;
- Directus;
- Payload CMS;
- Supabase com painel próprio.

Para a Ginkgo, eu usaria:

```
Frontend: SvelteKit ou Next.js
3D: Three.js + Threlte
Animação: GSAP
CMS: Directus ou Payload
Banco: Supabase/PostgreSQL
Storage: Cloudflare R2
Deploy frontend: Vercel ou Cloudflare Pages
Analytics: PostHog
Monitoramento: Sentry
Automação: n8n
```

**Threlte** seria particularmente interessante caso o frontend permaneça em Svelte, porque organiza cenas Three.js em componentes.

---

## 11\. Painel administrativo

O conteúdo dos projetos deveria ser configurável:

```json
{
  "slug": "leaf",
  "name": "Leaf",
  "category": "AI CRM",
  "description": "CRM operacional com agentes de IA.",
  "model": "/models/leaf.glb",
  "crystalPreset": "vertical-shard",
  "environment": "cold-lab",
  "accent": "#D4AF37",
  "camera": {
    "position": [0, 1.2, 6],
    "target": [0, 0, 0]
  },
  "timeline": {
    "start": 0.2,
    "end": 0.38
  }
}
```

Assim, um novo projeto poderia ser adicionado sem alterar a base do código.

O sistema leria os dados e criaria automaticamente:

- objeto;
- cristal;
- câmera;
- legenda;
- rota;
- sequência;
- CTA.

---

## 12\. Como criar uma versão inspirada para a Ginkgo

Não recomendaria copiar gelo, tipografia ou composição diretamente. A inspiração deve estar no sistema, não na fantasia visual.

## Conceito indicado

### Igloo

```
empresas encapsuladas em gelo
```

### Ginkgo

```
produtos como organismos digitais crescendo a partir de uma árvore neural
```

## Universo visual da Ginkgo

- ambiente escuro;
- árvore central biomecânica;
- folhas douradas representando produtos;
- raízes representando infraestrutura;
- fluxos luminosos representando automações;
- agentes como núcleos inteligentes;
- cada produto vivendo em um ramo;
- dados circulando como seiva.

### Jornada

```
Abertura
↓
Semente digital
↓
Raízes: infraestrutura, VPS, banco e RAG
↓
Tronco: Ginkgo AI Systems
↓
Ramos: Leaf, Wave, Pyre, Lexra, Nyra
↓
Copa: ecossistema de clientes e agentes
↓
CTA: construir seu sistema operacional empresarial
```

Isso manteria o impacto cinematográfico, mas com identidade própria.

---

## 13\. Roadmap de desenvolvimento

## Fase 1 — Estratégia e direção

Duração: 1–2 semanas.

Entregáveis:

- conceito;
- arquitetura narrativa;
- wireframes;
- storyboard;
- referências;
- roteiro;
- mapa de cenas;
- definição mobile e desktop.

## Fase 2 — Protótipo 3D

Duração: 2–3 semanas.

Entregáveis:

- câmera;
- scroll;
- objeto principal;
- iluminação;
- greybox;
- primeira transição;
- teste de performance.

## Fase 3 — Produção visual

Duração: 3–6 semanas.

Entregáveis:

- modelos;
- texturas;
- shaders;
- partículas;
- identidade;
- tipografia;
- áudio;
- cenas completas.

## Fase 4 — Desenvolvimento

Duração: 4–8 semanas.

Entregáveis:

- frontend;
- Scene Manager;
- timeline;
- navegação;
- CMS;
- SEO;
- analytics;
- responsividade;
- acessibilidade.

## Fase 5 — Otimização

Duração: 2–3 semanas.

Entregáveis:

- compressão;
- testes mobile;
- fallback;
- redução de movimento;
- monitoramento;
- Core Web Vitals;
- compatibilidade entre navegadores.

## Prazo total

| Nível | Prazo |
| --- | --- |
| Protótipo inspirado | 3–5 semanas |
| Site premium simplificado | 8–12 semanas |
| Experiência próxima ao nível Igloo | 14–24 semanas |
| Produção extremamente refinada | 6–9 meses |

---

## 14\. Equipe recomendada

## Equipe mínima funcional

- 1 diretor criativo/UI;
- 1 desenvolvedor WebGL;
- 1 desenvolvedor frontend;
- 1 artista 3D;
- 1 motion designer parcialmente alocado.

## Equipe premium

- diretor criativo;
- UX/UI designer;
- creative developer;
- technical artist;
- artista Houdini;
- artista Blender;
- frontend developer;
- sound designer;
- QA/performance;
- produtor.

Para uma operação enxuta, uma pessoa muito técnica pode acumular frontend e Three.js, enquanto IA auxilia em:

- geração de shaders-base;
- criação de texturas;
- documentação;
- testes;
- variações visuais;
- geração de código;
- otimização;
- produção de assets intermediários.

Ainda assim, direção artística e otimização gráfica não são tarefas que desaparecem apenas porque existe IA. O robô gera gelo; alguém ainda precisa impedir que ele pareça plástico de pote.

---

## 15\. Estimativa de custo

Valores aproximados para produção no Brasil:

| Versão | Faixa |
| --- | --- |
| Landing inspirada, 3D leve | R$ 15 mil–35 mil |
| Site 3D premium | R$ 40 mil–90 mil |
| Experiência WebGL avançada | R$ 100 mil–250 mil |
| Nível estúdio internacional | R$ 250 mil–600 mil+ |

Para a Ginkgo desenvolvendo internamente:

| Item | Custo provável |
| --- | --- |
| Direção e UI terceirizada | R$ 5 mil–15 mil |
| Artista 3D | R$ 8 mil–25 mil |
| Sound design | R$ 2 mil–8 mil |
| Infra e serviços | R$ 300–1.500/mês |
| Desenvolvimento | custo interno |
| Prazo realista | 10–16 semanas |

---

## 16\. Versão tecnicamente recomendada

Eu não começaria tentando reproduzir 100% do Igloo.

A estratégia correta seria:

## Versão 1

- SvelteKit;
- Three.js ou Threlte;
- uma cena principal;
- cinco produtos;
- scroll cinematográfico;
- partículas moderadas;
- interface HTML acessível;
- GLB comprimido;
- sem Houdini procedural inicialmente.

## Versão 2

- materiais customizados;
- shaders de dissolução;
- tipografia WebGL;
- transições avançadas;
- áudio reativo;
- qualidade adaptativa.

## Versão 3

- geração procedural;
- partículas volumétricas;
- painel para adicionar projetos;
- cenas criadas dinamicamente;
- WebGPU opcional;
- experiência personalizada conforme o visitante.

O Igloo é uma nave interestelar. Para começar, não precisamos construir a Estrela da Morte. Precisamos construir um caça rápido, bonito e que realmente decole.

## Stack final sugerida

```
SvelteKit
Threlte / Three.js
TypeScript
GSAP
GLSL
Blender
Rive para microinterações
Directus ou Payload CMS
Supabase/PostgreSQL
Cloudflare R2
Cloudflare Pages ou Vercel
PostHog
Sentry
n8n
GitHub Actions
```

Essa arquitetura mantém o impacto visual, permite crescimento e se conecta naturalmente ao ecossistema técnico da Ginkgo.

---

**Você disse**

sobre o projeto de codinome sexta-feira, rebatizamos de laplace ou damos outro nome. o prompt anterior eu fazia referencia ao aplicativo Pierre.

---

**Você disse**

Coloque como peça Ginkgo Learn, abaixo de leaf, wave e pyre e escolha um agente professor, lore.

---

Acho que existe uma oportunidade ainda maior do que apenas transformar isso em um book institucional.

O universo da Ginkgo já está deixando de ser apenas uma empresa. Está começando a se tornar uma **propriedade intelectual (IP)**, semelhante ao que empresas como Riot, Blizzard e Bungie construíram, mas aplicada ao mercado B2B e IA.

Ou seja, o marketing não deveria vender "automação".

Ele deveria vender o universo Ginkgo.

---

## A estratégia que eu adotaria

Criaria três níveis de conteúdo.

```
Nível 1
MARKETING

↓

Nível 2
LORE

↓

Nível 3
PRODUTO
```

O usuário entra pela curiosidade.

Permanece pela história.

Compra pela solução.

Isso faz toda diferença.

---

## Livro Institucional

Eu não chamaria de catálogo.

Chamaria de

## GINKGO

## The Living Intelligence Ecosystem

ou

## The Living Systems Book

Esse material seria um híbrido entre:

- Artbook
- Manual Corporativo
- Bíblia de Marca
- Pitch institucional

Visualmente próximo de:

Apple

Tesla

Nothing

Riot Forge

Arcane Artbook

---

## Estrutura

### Capítulo 1

Manifesto

Por que a Ginkgo existe.

---

### Capítulo 2

A Lore

Nascimento da árvore.

Laplace.

As raízes.

O ecossistema.

---

### Capítulo 3

O Universo

Mapa inteiro.

```
Ginkgo

↓

Laplace

↓

Organisms

↓

Sylvans

↓

Clientes

↓

Ecossistema
```

---

### Capítulo 4

Os Organismos

Leaf

Wave

Pyre

Learn

Cada um com

- propósito
- história
- conceito
- aplicações
- arquitetura
- cases

---

### Capítulo 5

Os Guardiões

Brann

Nyra

Atlas

Alfred

Lexra

Euclid

Sylvia

Cada um recebe uma página dupla.

Exemplo:

---

## EUCLID

Keeper of the Living Curriculum

Espécie

Sylvan Strigidae Sapientis

Habitat

Scholarium

Função

Transformar conhecimento em domínio.

Frase

> Understanding is cultivated.

---

### Capítulo 6

Tecnologia

Mostrar

Laplace

Hermes

LiteLLM

n8n

Supabase

RAG

Agent Memory

MCP

sem virar documentação.

Mais parecido com diagramas Apple.

---

### Capítulo 7

Visão

Onde a empresa quer chegar.

---

## Livro de Marketing

Outra peça.

Menor.

Algo entre 30 e 50 páginas.

Voltado para clientes.

Pouquíssimo texto.

Muito impacto visual.

Quase um coffee table book.

---

## Audiovisual

Aqui, na minha opinião, mora o diferencial.

Não faria vídeos explicando.

Faria trailers.

---

## Trailer 1

"Nascimento"

60 segundos

Tela preta.

Uma raiz.

Pulso.

Uma semente.

Narrador.

> Every system begins beneath the surface.

A árvore nasce.

Fim.

Logo.

---

## Trailer 2

Laplace

Nenhum rosto.

Nenhuma IA falando.

Somente memória.

Anéis.

Raízes.

Arquivos.

Luz.

Narrador.

> Memory is the beginning of intelligence.

---

## Trailer 3

Leaf

Cliente falando.

WhatsApp.

Agenda.

CRM.

Brann aparece discretamente.

---

## Trailer 4

Wave

Cidade.

Sinais.

Campanhas.

Atlas.

---

## Trailer 5

Pyre

Conteúdo.

Arte.

Vídeos.

Nyra.

---

## Trailer 6

Learn

Um estudante.

Livros.

Euclid.

Scholarium.

---

## Trailer 7

Sylvia

Apenas o fundador.

Escuro.

Orb.

Voz.

Pouquíssimos diálogos.

Nunca mostrar Sylvia inteira.

Ela sempre deve permanecer parcialmente abstrata.

---

## Shorts

Ao invés de fazer apenas vídeos educativos.

Misture.

### Série

## Fragments

20 segundos.

Exemplo.

Uma folha cai.

Texto.

> Every conversation becomes memory.

Logo.

Leaf.

---

Outro.

Atlas observando ondas.

Texto.

> Growth is controlled propagation.

---

Outro.

Euclid desenhando linhas luminosas.

Texto.

> Understanding is cultivated.

---

Outro.

Laplace.

Apenas raízes.

Texto.

> Nothing is forgotten.

---

## Série Documental

Nome.

## Inside Ginkgo

Episódios.

Como criamos Leaf.

Como nasceu Laplace.

Como pensamos os agentes.

Como funciona Sylvia.

Como treinamos nossos sistemas.

---

## Conteúdo Diário

Até postagens simples podem seguir o universo.

Ao invés de

> "Nova funcionalidade"

Postar

```
LOG ENTRY 0842

ORGANISM

LEAF

STATE

EVOLVING

NEW CAPABILITY

Voice qualification.

STATUS

Deployed.
```

Parece um registro do ecossistema.

---

## Até bugs viram lore

Exemplo.

Ao invés de

> Corrigimos um bug.

```
INCIDENT REPORT

Node

Pyre

Description

Unexpected content propagation.

Resolution

Nyra stabilized the creative engine.

Status

Resolved.
```

Isso cria consistência.

---

## O diferencial que eu vejo

A maioria das empresas de IA comunica como SaaS.

Você pode comunicar como uma **civilização tecnológica viva**.

Não no sentido de fantasia exagerada, mas de uma identidade consistente em todos os pontos de contato.

- O site conta a origem da árvore.
- O book aprofunda a filosofia e os organismos.
- Os trailers apresentam cada entidade.
- Os posts parecem registros do ecossistema.
- Os lançamentos de funcionalidades viram "eventos" dentro do universo.
- Os clientes deixam de comprar apenas um CRM ou um aplicativo de estudos; passam a entrar em um ecossistema reconhecível.

Essa consistência é rara no mercado B2B de IA e pode se tornar um dos principais diferenciais da marca Ginkgo.

---

**Você disse**

perfeito.

---

A direção fica consolidada assim:

**Ginkgo** — o ecossistema vivo  
**Laplace** — a inteligência e memória central  
**Sylvia** — a interface privada do fundador  
**Leaf, Wave, Pyre e Ginkgo Learn** — os organismos principais  
**Euclid** — professor e guardião do Learn  
**Sylvans** — agentes especializados do ecossistema

A linha editorial deve seguir três camadas:

**Lore → Produto → Prova prática**

E os principais ativos de marca passam a ser:

- **The Living Systems Book** — book institucional completo;
- **Marketing Book** — versão comercial curta;
- **Trailers cinematográficos** — apresentação da Ginkgo e dos organismos;
- **Fragments** — vídeos curtos de lore;
- **Inside Ginkgo** — conteúdo documental;
- **Log Entries** — posts recorrentes de produto, evolução e operação.

A marca deixa de parecer apenas uma empresa de automação e passa a operar como uma propriedade intelectual tecnológica coerente.

---

**Você disse**

oq acha do nome Flow, para o Ginkgo Learn

---

**Flow** funciona bem como nome de produto, mas eu não o usaria sozinho no lugar de **Ginkgo Learn**.

Ele comunica:

- fluidez;
- progresso contínuo;
- ritmo;
- estado de concentração;
- jornada adaptativa.

O problema é ser muito genérico. Existem muitos produtos, apps e empresas chamados Flow. Também comunica mais “produtividade” do que “aprendizado”.

Minha recomendação:

## Ginkgo Flow

Nome comercial do aplicativo.

## Ginkgo Learn

Nome da unidade ou categoria educacional do ecossistema.

Estrutura:

```
Ginkgo Learn
└── Flow
    Adaptive Learning System
```

Assim, no portfólio institucional:

```
Leaf
Wave
Pyre
Learn
```

E, para o público:

```
FLOW
by Ginkgo Learn
```

Isso preserva a lógica dos organismos e cria um nome mais simples para o aplicativo.

### Posicionamentos possíveis

> **Flow — Know exactly what to study next.**

> **Flow — Your adaptive path to mastery.**

> **Flow — Aprenda no seu ritmo. Evolua com direção.**

> **Enter the flow of learning.**

Na lore, Flow pode representar o **fluxo de conhecimento que percorre os galhos do Scholarium**. Euclid não entrega conteúdos isolados; ele controla esse fluxo, adaptando dificuldade, ritmo e revisão para cada estudante.

Minha avaliação:

- **Ginkgo Learn:** mais claro, institucional e explicativo.
- **Flow:** mais forte, curto e comercial.
- **Ginkgo Flow:** melhor equilíbrio para marca pública.
- **Flow by Ginkgo Learn:** melhor arquitetura de submarca.

[^1]: [awwwards.com](https://www.awwwards.com/sites/igloo-inc)

[^2]: [webgpu.com](https://www.webgpu.com/showcase/igloo-inc-procedural-crystals/)

[^3]: [discourse.threejs.org](https://discourse.threejs.org/t/landing-site-igloo-inc/67249)