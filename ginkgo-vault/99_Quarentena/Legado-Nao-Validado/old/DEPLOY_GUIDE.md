# Ginkgo Platform — Guia de Deploy

## Stack de Hospedagem

| Camada | Serviço | Função |
|---|---|---|
| CDN / DNS | Cloudflare | Proxy, SSL, cache, proteção DDoS |
| Frontend | Cloudflare Pages | Deploy do Next.js (`apps/web`) |
| Backend API | VPS Hostinger (Easypanel) | `apps/api` (Fastify) em container Docker |
| Banco de dados | Supabase | PostgreSQL gerenciado |
| Motor de automação | n8n (VPS) | Fluxos de IA e integrações |

---

## 1. Deploy do Frontend — Cloudflare Pages

### Opção A: Deploy via GitHub (Recomendado)

1. Acesse [dash.cloudflare.com](https://dash.cloudflare.com) → **Pages** → **Create a project**
2. Conecte o repositório `gingkosystems/ginkgo-platform`
3. Configure o build:

```
Framework preset: Next.js
Root directory: apps/web
Build command: pnpm build
Build output directory: .next
Node.js version: 20
```

4. Adicione as variáveis de ambiente:

```env
NEXT_PUBLIC_API_URL=https://api.ginkgosystems.tech
NEXT_PUBLIC_SUPABASE_URL=<sua-url-supabase>
NEXT_PUBLIC_SUPABASE_ANON_KEY=<sua-chave-anon>
```

5. Clique em **Save and Deploy**

### Opção B: Deploy via Wrangler CLI

```bash
# Na raiz do projeto
cd apps/web
pnpm build
npx wrangler pages deploy .next --project-name ginkgo-platform
```

### Configurar domínio customizado

1. No painel Cloudflare Pages → **Custom domains** → Adicionar `app.ginkgosystems.tech`
2. O registro DNS será criado automaticamente (CNAME → `ginkgo-platform.pages.dev`)
3. SSL automático via Cloudflare

---

## 2. Deploy da API — VPS Hostinger (Easypanel)

### Dockerfile para `apps/api`

```dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN corepack enable && pnpm install --frozen-lockfile
COPY . .
RUN pnpm build

FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

### No Easypanel

1. Crie um novo **App** → tipo **Docker**
2. Conecte ao repositório GitHub → branch `main`
3. Configure o **Root Directory** como `apps/api`
4. Adicione variáveis de ambiente:

```env
DATABASE_URL=postgresql://...supabase...
JWT_SECRET=<gere-com-openssl-rand-base64-32>
EVOLUTION_API_URL=http://localhost:8080
EVOLUTION_API_KEY=<sua-chave>
N8N_WEBHOOK_URL=https://studio.ginkgosystems.tech
PORT=3000
```

5. Configure o domínio: `api.ginkgosystems.tech`
6. Ative SSL via Let's Encrypt no Easypanel

---

## 3. Configuração DNS no Cloudflare

| Tipo | Nome | Valor | Proxy |
|---|---|---|---|
| CNAME | app | ginkgo-platform.pages.dev | ✅ Proxied |
| A | api | `<IP-VPS-Hostinger>` | ✅ Proxied |
| A | studio | `<IP-VPS-Hostinger>` | ✅ Proxied |
| A | @ | `<IP-VPS-Hostinger>` | ✅ Proxied |

### Regras de Page Rules recomendadas

```
app.ginkgosystems.tech/*
  → Cache Level: Bypass (para rotas dinâmicas)
  → SSL: Full (strict)

api.ginkgosystems.tech/*
  → Cache Level: Bypass
  → SSL: Full (strict)
```

---

## 4. Variáveis de Ambiente — Resumo

### Frontend (`apps/web/.env.local`)

```env
NEXT_PUBLIC_API_URL=https://api.ginkgosystems.tech
NEXT_PUBLIC_SUPABASE_URL=https://xxxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...
NEXT_PUBLIC_APP_URL=https://app.ginkgosystems.tech
```

### Backend (`apps/api/.env`)

```env
DATABASE_URL=postgresql://postgres:senha@db.xxxx.supabase.co:5432/postgres
JWT_SECRET=<32-bytes-random>
JWT_EXPIRES_IN=7d
EVOLUTION_API_URL=http://localhost:8080
EVOLUTION_API_KEY=<chave>
N8N_WEBHOOK_BASE=https://studio.ginkgosystems.tech/webhook
OPENAI_API_KEY=<chave>
ELEVENLABS_API_KEY=<chave>
PORT=3000
NODE_ENV=production
```

---

## 5. Próximas Fases de Desenvolvimento

### Fase 2 — Autenticação Real (Supabase Auth)
- Substituir mock de login por `supabase.auth.signInWithPassword()`
- Middleware Next.js para proteção de rotas
- Refresh token automático

### Fase 3 — Integração Evolution API
- Endpoint `POST /api/connections` → provisiona instância Evolution
- Webhook Evolution → n8n → Supabase (armazenar mensagens)
- Real-time no Chats via Supabase Realtime

### Fase 4 — CRM Real
- CRUD de leads no Supabase
- Drag-and-drop no kanban (dnd-kit)
- Histórico de interações por lead

### Fase 5 — Agente IA (Callima)
- Widget de chat com Callima no dashboard
- Integração com fluxo n8n `Callima` via webhook
- Histórico de conversas com IA

### Fase 6 — Billing (Stripe)
- Planos: Starter / Pro / Enterprise
- Webhook Stripe → atualiza `subscription_status` no Supabase
- Controle de uso de tokens de IA

---

## 6. Arquivos Criados nesta Fase

```
apps/web/
├── app/
│   ├── (auth)/
│   │   ├── login/page.tsx          ← Tela de login
│   │   └── register/page.tsx       ← Tela de cadastro
│   ├── (dashboard)/
│   │   ├── layout.tsx              ← Layout com Sidebar + Header
│   │   └── dashboard/
│   │       ├── page.tsx            ← Dashboard principal
│   │       ├── chats/page.tsx      ← Chat split-panel
│   │       ├── contacts/page.tsx   ← Grid de contatos
│   │       ├── crm/page.tsx        ← Kanban pipeline
│   │       ├── tasks/page.tsx      ← Gestão de tarefas
│   │       └── settings/page.tsx   ← Configurações + conexões
│   ├── globals.css                 ← Design system tokens
│   └── layout.tsx                  ← Root layout
├── components/
│   ├── layout/
│   │   ├── AppSidebar.tsx
│   │   ├── AppHeader.tsx
│   │   └── PageShell.tsx
│   └── shared/
│       ├── GlassCard.tsx
│       ├── KpiCard.tsx
│       ├── StatusBadge.tsx
│       ├── MessagesChart.tsx
│       ├── RecentActivity.tsx
│       ├── ConnectionStatus.tsx
│       └── EmptyState.tsx
└── lib/
    ├── utils.ts                    ← cn() helper
    └── mocks/data.ts               ← Dados mock para todas as telas
```
