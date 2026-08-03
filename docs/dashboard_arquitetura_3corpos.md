# Ginkgo Dashboard — Arquitetura dos 3 corpos (Leaf · Pyre · Wave)

Cada produto é um **app segmentado** sob o mesmo shell; **sincronizados e interativos via agentes**
(eventos no mesmo banco). Design = `.claude/skills/ginkgo/`. Backend governado = ginkgo-tree.

## 0. Shell global (envolve todos os apps)
- **AppSwitcher** (topo-esq): Leaf(verde) · Pyre(âmbar) · Wave(azul) + áreas globais. Mostra app ativo.
- **GlobalBar** (topo): busca/⌘K · **saldo GTK** (com alerta 80%/100%) · "Dar uma tarefa ao time"
  (CTA → roteia pro agente certo) · notificações · conta/org · ajuda.
- **AppSidebar**: muda por app (seções abaixo). Colapsa em drawer no mobile.
- **Breadcrumb** + título de página. **CommandPalette ⌘K**: navegar, criar task, trocar app, buscar lead.
- Estados em tudo: skeleton / vazio / erro. Acento da rota colore item ativo, foco, gráfico primário.

## 0.1 Interação cruzada via agentes (o "sincronizado entre si")
- **Wave→Leaf**: clique no anúncio (UTM) cria/atualiza `lead` e abre conversa no Inbox.
- **Pyre→Leaf**: clipe/voz/avatar gerados viram `media_assets` → a Callima envia no chat.
- **Pyre→Wave**: peça aprovada vira criativo de anúncio.
- **Leaf→Wave**: lead "ganho" + pagamento = receita que o Wave atribui ao criativo (ROAS).
- **Delegação** (ADR 0003): Brann→Nyra→Alfred via Eventos, com aprovação (HITL) — nunca import direto.
- **Contato 360**: o mesmo lead/contato é visível nos 3 apps (origem Wave, conversa Leaf, conteúdo Pyre).
- Tudo passa por **Task governada** (orçamento GTK + Evidence + HITL quando R3).

## 0.2 Workflow do usuário (macro)
Signup → **Onboarding** (conectar WhatsApp · configurar Callima · subir base de conhecimento ·
1ª tarefa) → **Leaf ao vivo** → upsell Wave/Pyre. Dia a dia: abre → Visão geral → Inbox (atende/
revisa IA) → CRM (move funil) → aprova pendências (HITL) → fim. "Dar tarefa ao time" a qualquer hora.

---
## 1. LEAF — Atendimento + CRM (agente Brann · secretária Callima) · acento VERDE
Sidebar: Visão geral · Inbox · Funil/CRM · Callima · Conhecimento · Mídia · Agenda · Canais.

### 1.1 Visão geral
- **KPIs (MetricCards):** conversas abertas · tempo 1ª resposta · % resolvidas pela IA ·
  leads novos (hoje/7d) · taxa de conversão · agendamentos de hoje · saldo GTK.
- **Gráficos:** volume de conversas/dia (line) · funil de conversão por etapa (funnel/bar) ·
  distribuição por canal (donut) · IA vs humano ao longo do tempo (area).
- **Listas:** próximos agendamentos · pendências HITL ("aguardando você").
- Botões: "Dar tarefa ao time", "Conectar canal".

### 1.2 Inbox (3-pane) — coração operacional
- Esq: filas (Novos/Meus/Outros + contadores), busca, filtros (tag/canal/agente), cards de conversa
  (avatar, nome, etiquetas, snippet, hora, não-lidas, selo do agente).
- Centro: thread (bolhas entrada/IA/humano + nota de sistema "Card criado") · header com **Assumir**
  (HITL), **Concluir**, **Transferir** · composer (texto, anexo, emoji, **áudio**, enviar).
- Dir: **LeadPanel** (contato, etiquetas editáveis, etapa do funil, oportunidade, resumo da Callima,
  ações rápidas). Colapsável; drawer no mobile.
- Transições: abrir thread = slide; assumir = some o badge "IA", muda o header; toasts de envio.

### 1.3 Funil / CRM (Kanban)
- Colunas = etapas (cor + contador + soma de valor opcional); cards = leads; **DnD** otimista →
  PATCH stage. Seletor de funil + "Gerenciar funis/etapas" (CRUD, cor, ordem). Abrir card = LeadPanel.
- Busca + filtro. Índices: conversão por etapa, tempo médio por etapa, leads parados.

### 1.4 Callima (config da secretária)
- Formulário: persona/nicho/descrição · skills (agendar/cobrar/qualificar/follow-up, toggles) ·
  **voz** (on/off + voice_id + botão "testar voz") · handoff (limiar/keywords) · horário · filtros
  (allow/block, ignorar grupos) · resposta (split, delay, read-receipt). **Kill-switch** (ativo/pausado).
- Settings/esquema: tudo persiste em `workspace_assistants`; mudanças com toast + estado salvo.

### 1.5 Conhecimento (RAG) · 1.6 Mídia · 1.7 Agenda · 1.8 Canais
- **Conhecimento:** upload (PDF/txt/url/faq) + status de processamento + ativar/excluir.
- **Mídia:** biblioteca (grid com preview) + upload + "enviar via Callima"; recebe peças do Pyre.
- **Agenda:** calendário/lista de `appointments` (confirmar/cancelar), filtro por dia.
- **Canais:** conectar WhatsApp (QR + estado + quality rating/tier) · card "Cloud API em breve" ·
  IG/Messenger "em breve".

---
## 2. PYRE — Estúdio de Conteúdo (agente Nyra) · acento ÂMBAR
Sidebar: Visão geral · Voz · Trends · Clips · Avatar · Radar · Content Engine · Projetos.

### 2.1 Visão geral
- KPIs: posts agendados · posts publicados (7/30d) · taxa de aprovação HITL · saldo GTK · projetos ativos.
- Gráficos: produção/dia (bar) · desempenho do conteúdo publicado (alcance/engajamento, line) ·
  score de tendências em alta (lista com sparkline).
- Atalhos pros módulos + "Novo projeto".

### 2.2 Módulos (cada um: input → preview → consome GTK → salva no projeto → exporta/enviar)
- **Voz** (ElevenLabs): roteiro → áudio; voz/idioma/tom; player; "usar na Callima".
- **Trends**: cards de tendência por nicho/keyword + **score de viralidade** + "gerar pauta".
- **Clips**: upload vídeo longo → cortes 9:16 com legenda (highlights por IA); timeline; export.
- **Avatar (HeyGen)**: roteiro da Nyra → vídeo de avatar vertical; preview; export.
- **Radar**: outliers de concorrentes (vídeos acima da média) — tabela + "inspirar conteúdo".
- **Content Engine**: calendário editorial + geração de posts/legendas + **HITL (aprovar antes de
  publicar)** + agendamento via Postiz. Estados de aprovação visíveis.
- **Projetos**: histórico/outputs por projeto, export em qualquer formato, reuso na Mídia do Leaf.

---
## 3. WAVE — Tráfego / Atribuição (agente Alfred) · acento AZUL
Sidebar: Visão geral · Campanhas · Atribuição · Otimização · CAPI · Conexões.

### 3.1 Visão geral
- KPIs: gasto · receita atribuída · **ROAS** · ROI · CPA · lucro · % do orçamento usado.
- Gráficos: ROAS por campanha (bar) · gasto vs receita (line dupla) · CPA no tempo (line) ·
  atribuição anúncio→lead→venda (funnel/sankey).

### 3.2 Seções
- **Campanhas:** tabela (campanha/conjunto/anúncio) com métricas + venda atribuída por criativo;
  drill no criativo; filtros rede/período.
- **Atribuição:** funil clique(UTM)→lead→conversa→card→pagamento; origem de cada venda.
- **Otimização (Alfred):** recomendações da IA (pausar/escalar/realocar) com **HITL** (aprovar/recusar).
- **CAPI:** config de eventos server-side (Meta/Google/TikTok).
- **Conexões:** conectar contas de anúncio (Meta Marketing API primeiro; verba = conta do cliente, Modelo A).
- Estado atual no produto: **"em breve"** honesto até as APIs de ads entrarem (depende do portfólio Meta).

---
## 4. Áreas globais (fora dos apps · acento roxo de marca)
- **Atividade** (glass-box): lista de Tasks com lineage (events/evidence/ledger), filtros, "ao vivo".
- **Financeiro / Planos:** carteira GTK (saldo + breakdown plano/top-up) · histórico (ledger) ·
  recarga (top-up Stripe) · plano atual + upgrade · faturas. Gráfico de consumo de GTK/dia.
- **Equipe / Admin:** membros, papéis (owner/admin/manager/operator/viewer), permissões, convites.
- **Configurações:** conta/perfil · org · segurança · notificações · idioma (pt/en) · tema (dark) ·
  toggles de agente por tenant · kill-switch global.
- **Onboarding:** wizard (conectar WhatsApp → configurar Callima → subir KB → 1ª tarefa) com progresso.

## 5. Componentes (inventário compartilhado) — construir 1x, reusar
AppShell · AppSwitcher · GlobalBar · AppSidebar · CommandPalette(⌘K) · Button(4 variantes) ·
Input/Select/Textarea/Toggle/Slider · Badge/Tag · Card · MetricCard · Table · Kanban(Board/Column/Card) ·
Chat(Thread/Bubble/Composer) · LeadPanel · Modal · Drawer · Toast · Tabs · Skeleton · EmptyState ·
ErrorState · Avatar · AgentBadge · Charts(Line/Bar/Donut/Sparkline/Funnel) · TaskLineage · HITLApprovalCard.

## 6. Transições & micro-interações
Troca de rota = fade 150ms · drawer/modal = slide+fade · DnD = otimista com spring · skeleton→conteúdo =
fade · toasts (sucesso/erro) · hover/active em botões (scale 0.98) · paleta ⌘K (fade+scale).
Tudo ≤200ms, respeitando reduced-motion. framer-motion (já no projeto).

## 7. Settings / esquemas
Tema dark (claro=v2) · densidade (confortável/compacta) · idioma pt/en · notificações (canais/eventos) ·
preferências por agente (ativar/pausar, voz on/off) · kill-switch · sessão/segurança (logout, tokens).
Persistir por usuário/org; honest-data (refletir estado real do banco).

## 8. Dados · gráficos · índices (resumo)
- **Leaf:** conversas/dia, funil de conversão, canal (donut), IA-vs-humano; índices: 1ª resposta,
  %IA, conversão, leads por origem, GTK/dia.
- **Pyre:** produção/dia, desempenho publicado, score de trends; índices: agendados, %aprovação HITL.
- **Wave:** ROAS por campanha, gasto×receita, CPA, atribuição (funnel); índices: ROAS/ROI/CPA/%budget.
- **Global:** consumo GTK/dia, tasks por estado, pendências HITL.
- Libs: recharts/Chart.js. Sempre com EmptyState quando sem dados (nunca número inventado).

## 9. Ordem de construção (no tronco, guiado pela skill ginkgo)
1) Aplicar a skill `ginkgo` + repaginar o Shell/GlobalBar/Sidebar existentes ao token novo.
2) Leaf: Visão geral → Inbox (repaginar) → Kanban (novo) → Callima/KB/Mídia/Agenda/Canais.
3) Globais: Financeiro/Planos (GTK) → Atividade → Settings → Admin → Onboarding.
4) Pyre e Wave: cascas "em breve" já no padrão; encher quando as APIs entrarem.
