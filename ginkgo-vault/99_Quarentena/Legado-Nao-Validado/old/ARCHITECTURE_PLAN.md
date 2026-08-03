# Ginkgo Platform - Arquitetura e Plano de Desenvolvimento (Fase 1)

## 1. Visão Geral
A **Ginkgo Platform** (anteriormente conhecida como Leaf Wave e Pyre) é um *AI Operating System* para empresas que utilizam agentes inteligentes. O objetivo desta fase é construir o frontend base (dashboard SaaS enterprise) com foco na experiência do usuário, estrutura visual, navegação e componentes reutilizáveis, utilizando dados mockados.

## 2. Stack Tecnológica (Imutável)
- **Framework:** Next.js 14 (App Router)
- **Linguagem:** TypeScript
- **Estilização:** TailwindCSS
- **Componentes UI:** shadcn/ui
- **Ícones:** lucide-react
- **Gráficos:** Recharts
- **Animações:** framer-motion

## 3. Identidade Visual
- **Estilo:** Dark futurista, Premium SaaS, Leve glassmorphism, Glow sutil (azul/roxo).
- **Cores Principais:**
  - Background: `#0B0F1A`
  - Cards: `#121826`
  - Border: `rgba(255,255,255,0.06)`
  - Texto primário: `#E5E7EB`
  - Texto secundário: `#9CA3AF`
  - Blue glow: `#3B82F6`
  - Indigo glow: `#6366F1`
- **Tipografia:** Geist (títulos fortes, textos curtos, visual limpo).

## 4. Estrutura de Pastas (Frontend - `apps/web`)
A estrutura seguirá o padrão do App Router do Next.js, organizada para escalabilidade:

```text
apps/web/
├── app/
│   ├── (auth)/
│   │   ├── login/page.tsx
│   │   └── register/page.tsx
│   ├── (dashboard)/
│   │   ├── layout.tsx          # AppSidebar + AppHeader + PageShell
│   │   ├── page.tsx            # Dashboard Principal
│   │   ├── chats/page.tsx
│   │   ├── contacts/page.tsx
│   │   ├── crm/page.tsx
│   │   ├── tasks/page.tsx
│   │   └── settings/page.tsx
│   ├── onboarding/page.tsx     # Já existente
│   ├── globals.css
│   └── layout.tsx              # Root layout
├── components/
│   ├── ui/                     # Componentes base (shadcn/ui)
│   ├── layout/                 # AppSidebar, AppHeader, PageShell
│   └── shared/                 # GlassCard, KpiCard, StatusBadge, MessagesChart, etc.
├── lib/
│   ├── utils.ts                # Utilitários (ex: cn para tailwind)
│   └── mocks/                  # Dados mockados para a Fase 1
└── public/
```

## 5. Componentes Reutilizáveis (Mandatórios)
- `AppSidebar`: Navegação lateral fixa, responsiva, com ícones Lucide.
- `AppHeader`: Cabeçalho superior (breadcrumbs, perfil do usuário).
- `PageShell`: Container padrão para as páginas do dashboard.
- `GlassCard`: Card base com efeito glassmorphism e bordas sutis.
- `KpiCard`: Card para exibição de métricas (Total de Contatos, Mensagens, etc).
- `StatusBadge`: Badge visual para status (online, offline, bot, human).
- `MessagesChart`: Gráfico central usando Recharts.
- `RecentActivity`: Lista de atividades recentes.
- `ConnectionStatus`: Indicador de status de conexões (ex: WhatsApp).
- `EmptyState`: Estado vazio padronizado para listas sem dados.

## 6. Plano de Execução (Passo a Passo)

### Passo 1: Configuração Inicial e Identidade Visual
- Instalar dependências necessárias (`shadcn/ui`, `lucide-react`, `recharts`, `framer-motion`).
- Configurar variáveis CSS no `globals.css` para refletir a paleta de cores dark futurista.
- Configurar a fonte Geist.

### Passo 2: Construção dos Componentes de Layout e UI Base
- Criar os componentes `GlassCard`, `KpiCard`, `StatusBadge`.
- Implementar o layout do dashboard (`AppSidebar`, `AppHeader`, `PageShell`).

### Passo 3: Telas de Autenticação
- Desenvolver a tela de Login (`/login`).
- Desenvolver a tela de Registro (`/register`).

### Passo 4: Dashboard Principal
- Construir a página inicial do dashboard (`/`).
- Integrar `KpiCard`s, `MessagesChart` e `RecentActivity`.

### Passo 5: Telas Internas
- **Chats:** Lista de conversas e janela de chat com diferenciação visual (usuário vs agente IA).
- **Contatos:** Grid de cards com avatares e status.
- **CRM:** Pipeline visual simples (Novo Lead, Qualificação, etc).
- **Tarefas:** Lista de tarefas com prioridade e status.
- **Configurações:** Gerenciamento de conexões simuladas.

## 7. Integração Futura (Motor n8n)
Os fluxos n8n analisados (ex: `Callima`, `Automated AI voice cloning`, `Process large documents with OCR`) servirão como o motor de backend na Fase 2. A arquitetura do frontend está sendo preparada para consumir essas APIs via o backend Node.js/Fastify já presente no monorepo (`apps/api`).

## 8. Critérios de Aceite (Fase 1)
- Navegação fluida entre todas as telas obrigatórias.
- Identidade visual estritamente aplicada (Dark futurista, Glassmorphism).
- Componentes reutilizáveis isolados e bem definidos.
- Dados mockados preenchendo as telas de forma realista.
- Responsividade adequada (foco desktop, mas funcional em telas menores).
