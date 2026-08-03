# LEAF — Spec da Central de Atendimento (Inbox) · v1

Objetivo: implementar a tela mais crítica do dashboard — a Inbox de atendimento
WhatsApp — no padrão "Helena-grade", com identidade Ginkgo. Aprovada pelo founder.

## Rota e navegação
- Rota: `apps/web/app/(dashboard)/inbox/page.tsx` (ou a rota já apontada no item
  "Inbox" da sidebar — reaproveitar a existente, não duplicar).
- Item da sidebar "Inbox/Atendimentos" deve levar aqui e ficar ativo.

## Layout (3-pane, desktop)
1. Topbar da tela: título "Atendimentos" + selo "Callima online" (dot verde) + sino + avatar.
2. Coluna ESQUERDA (~280px) — lista de conversas:
   - Abas/filtros: Novos / Meus / Outros (com contadores).
   - Busca (input "Buscar atendimento").
   - Cards de conversa: avatar(iniciais), nome, etiquetas (Lead/Suporte/Prioridade/
     Atendimento humano), snippet da última msg, horário relativo, badge de não-lidas,
     selo do agente atuando (ex.: "Leaf/Callima"). Card ativo com borda-esquerda roxa.
3. Coluna CENTRAL (flex) — thread:
   - Header: avatar+nome+telefone(whatsapp), selo "Callima atendendo", botões
     **Assumir** (primário) e **Concluir** (outline). "Transferir" no menu.
   - Mensagens: bolhas entrada (esq) e saída (dir); bolha da IA marcada "Callima (IA)";
     nota de sistema "Card criado no CRM pela Callima — etapa X".
   - Composer: anexo, emoji, input, microfone, enviar.
4. Coluna DIREITA (~300px, colapsável) — contexto do lead/CRM:
   - Dados do contato, etiquetas editáveis, card do CRM (etapa/funil), oportunidade,
     ações rápidas (mudar etapa, atribuir, marcar prioridade).

## Identidade (tokens já existentes no projeto)
- Tema dark navy (v1). bg #0B0F1C, surfaces #0E1422/#121a2b, borda #1e2740,
  texto #fff / #8a93a8 / #5f6b85, primário #6d5efc, Leaf verde #22c55e,
  Wave azul, Pyre laranja #f97316. Fontes Space Grotesk (títulos) + Inter (corpo).
- Usar os tokens do design system do projeto (Tailwind v4 @theme). NÃO hardcodar
  cores avulsas — mapear pros tokens. Modo claro (azul/branco) fica pro v2.
- Mobile-first: <768px colapsa pra 1 painel (lista → abre thread; contexto vira drawer).

## Dados (wire no que já existe — NÃO inventar схема)
- Listar conversas, mensagens, lead/CRM a partir da API real (`apps/api`) /
  Supabase. Inspecionar o módulo de inbox/conversations já existente e usar os
  endpoints/tabelas reais. Se faltar endpoint, criar mínimo no `apps/api`.
- Botão "Assumir" = ação HITL: muda o controle da conversa de IA→humano
  (registrar em brann_actions/governança e pausar respostas automáticas da Callima).
- "Concluir" fecha o atendimento (status). Etiquetas e etapa do CRM persistem.

## Estados (obrigatórios — sem spinner infinito)
- loading: skeletons nas 3 colunas.
- vazio: "Nenhum atendimento ainda" + dica.
- erro/timeout: mensagem + botão "Tentar de novo" (sem travar).

## Escopo
- v1 (AGORA): as 3 colunas, wire real, Assumir/Concluir, etiquetas, estados, responsivo.
- v2 (depois): modo claro; resumo da conversa pela IA; sugestão de resposta; busca avançada.

## Critérios de aceite
- Abre em /inbox, sidebar ativa, sem 404.
- Lista real de conversas; clicar abre a thread real; enviar mensagem funciona.
- "Assumir" pausa a IA e marca controle humano (verificável no banco/governança).
- Responsivo no mobile; loading/empty/error implementados; lint/build passam.
- Visual coerente com o mock aprovado (dark navy + selos de agente + HITL visível).
