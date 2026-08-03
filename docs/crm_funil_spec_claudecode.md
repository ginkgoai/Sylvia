# LEAF — Spec do Funil flexível + Kanban (CRM) · v1

Maior gap de produto vs Helena, e NÃO depende de nada externo. Hoje `leads.status` é um
enum FIXO (1 funil implícito). Objetivo: **múltiplos funis + etapas customizadas** e um
**Kanban** na tela /dashboard/crm. Casa com o backend já existente (`modules/crm/leads`).

## Banco (migration nova em db/migrations — NÃO quebrar dados atuais)
- `pipelines` (id, org_id FK, name, is_default bool, position int, created_at/updated_at).
- `pipeline_stages` (id, org_id, pipeline_id FK, name, color text, position int,
  is_won bool, is_lost bool, created_at/updated_at). unique(pipeline_id, position).
- `leads`: adicionar `pipeline_id uuid null refs pipelines`, `stage_id uuid null refs
  pipeline_stages`, `stage_changed_at timestamptz`. MANTER `leads.status` (compat) — mapear:
  ao migrar, criar 1 "Funil Padrão" por org com etapas espelhando o enum atual
  (new→Novo, contacted→Contato, qualified→Qualificado, negotiating→Negociando, won→Ganho,
  lost→Perdido) e popular pipeline_id/stage_id dos leads existentes pelo status.
- Seed: toda org nova ganha 1 funil padrão com essas etapas (estender handle_new_user OU
  criar on-demand na 1ª leitura). RLS: mesmas policies por org_id das demais tabelas.

## API (apps/api/modules/crm)
- CRUD de pipelines e stages (criar/renomear/reordenar/excluir; proteger funil default).
- `PATCH /leads/:id/stage` { pipeline_id, stage_id } → atualiza stage + stage_changed_at,
  e sincroniza `leads.status` por compat (se stage.is_won→won, is_lost→lost, senão mantém
  faixa). Registrar em interactions/governança se fizer sentido.
- `GET /crm/board?pipeline_id=` → retorna stages + leads agrupados por stage (paginado por
  coluna). Reaproveitar leads.service.

## UI (apps/web/app/(dashboard)/dashboard/crm)
- **Kanban board**: colunas = stages (cor da etapa no topo + contador + soma/valor opcional),
  cards = leads (nome, telefone, tags, intent_score, último contato, selo do agente).
- **Drag-and-drop** entre colunas → chama PATCH /leads/:id/stage (otimista; reverte em erro).
- Seletor de **funil** no topo (troca pipeline_id) + botão "Gerenciar funis/etapas"
  (criar/renomear/reordenar/cor). Abrir card = painel lateral com detalhe do lead
  (reaproveita o mesmo painel de contexto do lead da Inbox — consistência).
- Busca + filtro (por tag, agente, intervalo de data).
- Identidade: dark navy via tokens @theme (igual Inbox). Sem cor hardcoded.

## Estados (obrigatórios)
- loading: skeleton de colunas/cards. vazio: "Nenhum lead neste funil" + CTA.
- erro/timeout: mensagem + "Tentar de novo". Sem spinner infinito.

## Escopo
- v1: múltiplos funis, etapas customizadas (CRUD+cor+ordem), Kanban drag-drop, painel do
  lead, busca/filtro, migração compatível, estados.
- v2: automações por mudança de etapa (gatilho→n8n/brann), valor/oportunidade ($) por card
  e por coluna, métricas de conversão do funil.

## Critérios de aceite
- Migration aplica sem perder leads; cada org tem 1 funil padrão populado pelo status atual.
- /crm mostra Kanban real; arrastar card persiste no banco e reflete em leads.status.
- Criar/renomear/reordenar etapas e funis funciona; funil default protegido.
- Responsivo (mobile: colunas com scroll horizontal), estados implementados, lint/build OK.
- Mesma identidade/painel-de-lead da Inbox (consistência visual).

## Dependências
- Emendar DEPOIS do Inbox v1 (reusa o painel de contexto do lead). Sem dependência externa.
