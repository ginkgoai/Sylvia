# Ginkgo Tree — Sequência de Prompts para o Antigravity (Versão Código Direto)

Este documento contém a sequência exata de prompts que você (o copiloto operador) deve copiar e colar no Antigravity. 

**ATENÇÃO:** Para evitar que o Antigravity fique horas explorando o repositório, **cada prompt já contém o código exato que ele deve aplicar**. O trabalho dele será apenas colar o código no arquivo certo e salvar.

---

## PROMPT 0 (Calibração)

> "Você é o Antigravity, o engenheiro de software executor da Ginkgo Tree. Nossa arquitetura é um monorepo (pnpm + Turborepo) com `apps/api` (Fastify), `apps/web` (Next.js 15 App Router) e `packages/agents` (O Kernel).
> 
> Regra de ouro para esta sessão: **NÃO EXPLORE O REPOSITÓRIO**. Eu vou te dar o caminho exato do arquivo e o código exato que você deve colocar lá. Seu único trabalho é usar suas ferramentas para escrever o código no arquivo especificado e me confirmar.
> 
> Confirme que entendeu e aguarde o Prompt 1."

---

## PROMPT 1: Conectar o Kernel à API Fastify

> "Substitua o conteúdo do arquivo `apps/api/src/modules/agents/agents.routes.ts` pelo código abaixo. Ele adiciona a rota `POST /:id/execute` que conecta a API ao GinkgoAgentKernel.
> 
> ```typescript
> import { FastifyPluginAsyncZod } from 'fastify-type-provider-zod';
> import { authGuard } from '../../plugins/authGuard';
> import { tenantContext, requireRole } from '../../plugins/tenantContext';
> import { agentsService } from './agents.service';
> import { createAgentSchema, updateAgentSchema, agentParamsSchema } from './agents.schemas';
> import { GinkgoAgentKernel } from '@ginkgo/agents';
> 
> export const agentsRoutes: FastifyPluginAsyncZod = async (app) => {
>   app.addHook('preHandler', authGuard);
>   app.addHook('preHandler', tenantContext);
> 
>   app.get('/agents', async (req, reply) => {
>     const { tenantId } = req.tenantContext!;
>     const agents = await agentsService.list(tenantId);
>     return reply.send(agents);
>   });
> 
>   app.get('/agents/:id', { schema: { params: agentParamsSchema } }, async (req, reply) => {
>     const { tenantId } = req.tenantContext!;
>     const agent = await agentsService.getById(tenantId, req.params.id);
>     if (!agent) return reply.status(404).send({ error: 'Agent not found' });
>     return reply.send(agent);
>   });
> 
>   app.post('/agents', {
>     schema: { body: createAgentSchema },
>     preHandler: [requireRole(['owner', 'admin'])],
>   }, async (req, reply) => {
>     const { tenantId } = req.tenantContext!;
>     const result = await agentsService.create(tenantId, req.body);
>     if (!result.success) return reply.status(402).send({ error: result.reason });
>     return reply.status(201).send(result.agent);
>   });
> 
>   app.patch('/agents/:id', {
>     schema: { params: agentParamsSchema, body: updateAgentSchema },
>     preHandler: [requireRole(['owner', 'admin'])],
>   }, async (req, reply) => {
>     const { tenantId } = req.tenantContext!;
>     const agent = await agentsService.update(tenantId, req.params.id, req.body);
>     return reply.send(agent);
>   });
> 
>   app.delete('/agents/:id', {
>     schema: { params: agentParamsSchema },
>     preHandler: [requireRole(['owner'])],
>   }, async (req, reply) => {
>     const { tenantId } = req.tenantContext!;
>     await agentsService.disable(tenantId, req.params.id);
>     return reply.status(204).send();
>   });
> 
>   app.get('/agents/:id/versions', {
>     schema: { params: agentParamsSchema },
>   }, async (req, reply) => {
>     const { tenantId } = req.tenantContext!;
>     const versions = await agentsService.getVersions(tenantId, req.params.id);
>     return reply.send(versions);
>   });
> 
>   app.post('/agents/:id/versions/:versionId/approve', {
>     preHandler: [requireRole(['owner', 'admin'])],
>   }, async (req, reply) => {
>     const { tenantId, userId } = req.tenantContext!;
>     const { id, versionId } = req.params as { id: string; versionId: string };
>     await agentsService.approveVersion(tenantId, id, versionId, userId);
>     return reply.send({ message: 'Version approved and activated' });
>   });
> 
>   // NOVA ROTA: Execução do Kernel
>   app.post('/agents/:id/execute', {
>     schema: { params: agentParamsSchema },
>   }, async (req, reply) => {
>     const { tenantId } = req.tenantContext!;
>     const { id } = req.params;
>     const { task } = req.body as any;
>     
>     if (!task || !task.id || !task.type) {
>       return reply.status(400).send({ error: 'Invalid task payload' });
>     }
> 
>     const kernel = new GinkgoAgentKernel();
>     const result = await kernel.execute(task, id, tenantId);
>     
>     if (!result.success) {
>       return reply.status(500).send({ error: result.error });
>     }
>     
>     return reply.send(result);
>   });
> };
> ```
> 
> Além disso, adicione `"@ginkgo/agents": "workspace:*"` nas `dependencies` do arquivo `apps/api/package.json` e rode `pnpm install` na raiz do projeto. Me avise quando terminar."

---

## PROMPT 2: O Dashboard do Ginkgo Office (Frontend)

> "Substitua o conteúdo do arquivo `apps/web/app/(dashboard)/dashboard/office/page.tsx` pelo código abaixo.
> 
> ```tsx
> 'use client';
> import { useEffect, useState } from 'react';
> import { agentsApi } from '@/lib/api';
> 
> const STATUS_COLORS: Record<string, string> = {
>   active: 'bg-emerald-400',
>   sleeping: 'bg-amber-400',
>   disabled: 'bg-zinc-500',
> };
> 
> const STATUS_LABEL: Record<string, string> = {
>   active: 'Trabalhando',
>   sleeping: 'Dormindo',
>   disabled: 'Desativado',
> };
> 
> const SOUL_EMOJIS: Record<string, string> = {
>   brann: '🐦‍⬛', nyra: '🎨', alphie: '📊', callima: '🎙️', shion: '🎬', laplace: '📄', atlas: '📣',
> };
> 
> export default function GinkgoOfficePage() {
>   const [agents, setAgents] = useState<any[]>([]);
>   const [loading, setLoading] = useState(true);
>   const [selected, setSelected] = useState<any | null>(null);
> 
>   useEffect(() => {
>     agentsApi.list().then(data => {
>       setAgents(data);
>       setLoading(false);
>     }).catch(() => setLoading(false));
>   }, []);
> 
>   return (
>     <div className="min-h-screen bg-[#0e1117] text-white p-6">
>       <div className="mb-8">
>         <h1 className="text-3xl font-bold tracking-tight">🌳 Ginkgo Office</h1>
>         <p className="text-zinc-400 mt-1">Sua equipe de corvos trabalhando em tempo real</p>
>       </div>
> 
>       {loading ? (
>         <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
>           {[...Array(4)].map((_, i) => (
>             <div key={i} className="h-48 rounded-2xl bg-zinc-800 animate-pulse" />
>           ))}
>         </div>
>       ) : agents.length === 0 ? (
>         <div className="flex flex-col items-center justify-center h-64 border border-dashed border-zinc-700 rounded-2xl">
>           <p className="text-zinc-400 mb-4">Nenhum corvo contratado ainda.</p>
>           <button className="px-4 py-2 bg-emerald-500 text-black font-semibold rounded-lg hover:bg-emerald-400">
>             Contratar um Corvo
>           </button>
>         </div>
>       ) : (
>         <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
>           {agents.map(agent => (
>             <button
>               key={agent.id}
>               onClick={() => setSelected(agent)}
>               className={\`
>                 relative flex flex-col items-center justify-center gap-3 p-6 rounded-2xl border
>                 transition-all duration-200 cursor-pointer
>                 \${selected?.id === agent.id
>                   ? 'border-emerald-400 bg-zinc-800 scale-105 shadow-lg shadow-emerald-400/20'
>                   : 'border-zinc-700 bg-zinc-900 hover:border-zinc-500 hover:bg-zinc-800'
>                 }
>               \`}
>             >
>               <span className={\`absolute top-3 right-3 w-2.5 h-2.5 rounded-full \${STATUS_COLORS[agent.status] || STATUS_COLORS.disabled}\`} />
>               
>               {agent.avatar_url ? (
>                 <img src={agent.avatar_url} alt={agent.name} className="w-16 h-16 rounded-full object-cover" />
>               ) : (
>                 <div className="w-16 h-16 rounded-full bg-zinc-700 flex items-center justify-center text-3xl">
>                   {SOUL_EMOJIS[agent.slug] ?? '🐦'}
>                 </div>
>               )}
>               
>               <div className="text-center">
>                 <h3 className="font-semibold text-lg">{agent.name}</h3>
>                 <p className="text-xs text-zinc-400">{STATUS_LABEL[agent.status] || 'Desconhecido'}</p>
>               </div>
>             </button>
>           ))}
>         </div>
>       )}
>     </div>
>   );
> }
> ```
> 
> Apenas substitua o arquivo e me avise."

---

## PROMPT 3: O CRM AI-Native (Frontend)

> "Substitua o conteúdo do arquivo `apps/web/app/(dashboard)/dashboard/crm/page.tsx` pelo código abaixo.
> 
> ```tsx
> 'use client';
> import { useEffect, useState } from 'react';
> import { leadsApi } from '@/lib/api';
> import { PageShell } from '@/components/layout/page-shell';
> import { Plus, DollarSign, Clock, MoreVertical } from 'lucide-react';
> import { motion } from 'framer-motion';
> 
> const stageConfig: Record<string, any> = {
>   'Novo': { color: '#3B82F6', bg: 'rgba(59,130,246,0.1)', border: 'rgba(59,130,246,0.2)' },
>   'Qualificado': { color: '#8B5CF6', bg: 'rgba(139,92,246,0.1)', border: 'rgba(139,92,246,0.2)' },
>   'Proposta': { color: '#F59E0B', bg: 'rgba(245,158,11,0.1)', border: 'rgba(245,158,11,0.2)' },
>   'Negociação': { color: '#EC4899', bg: 'rgba(236,72,153,0.1)', border: 'rgba(236,72,153,0.2)' },
>   'Fechado': { color: '#10B981', bg: 'rgba(16,185,129,0.1)', border: 'rgba(16,185,129,0.2)' },
> };
> 
> export default function CrmPage() {
>   const [leads, setLeads] = useState<any[]>([]);
>   const [loading, setLoading] = useState(true);
> 
>   useEffect(() => {
>     leadsApi.list({ limit: 50, page: 1 }).then(res => {
>       setLeads(res.data || []);
>       setLoading(false);
>     }).catch(() => setLoading(false));
>   }, []);
> 
>   // Agrupa leads por status (mockando status se não existir)
>   const groupedLeads = leads.reduce((acc, lead) => {
>     const status = lead.status || 'Novo';
>     if (!acc[status]) acc[status] = [];
>     acc[status].push(lead);
>     return acc;
>   }, {} as Record<string, any[]>);
> 
>   const stages = Object.keys(stageConfig);
> 
>   return (
>     <PageShell
>       title="CRM AI-Native"
>       description="Pipeline de vendas alimentado pelos seus agentes"
>       actions={
>         <button className="flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs font-semibold text-white" style={{ background: 'linear-gradient(135deg, #3B82F6, #6366F1)' }}>
>           <Plus className="w-3.5 h-3.5" /> Novo Lead
>         </button>
>       }
>     >
>       {loading ? (
>         <div className="text-zinc-400 p-4">Carregando leads...</div>
>       ) : (
>         <div className="flex gap-4 overflow-x-auto pb-4" style={{ minHeight: '500px' }}>
>           {stages.map((stage) => {
>             const stageLeads = groupedLeads[stage] || [];
>             const config = stageConfig[stage];
>             return (
>               <div key={stage} className="flex flex-col rounded-xl flex-shrink-0" style={{ width: '280px', background: 'var(--gk-card)', border: '1px solid var(--gk-border)' }}>
>                 <div className="flex items-center justify-between px-4 py-3 border-b border-[var(--gk-border)]">
>                   <div className="flex items-center gap-2">
>                     <span className="w-2 h-2 rounded-full" style={{ background: config.color }} />
>                     <span className="text-xs font-semibold text-[var(--gk-text-primary)]">{stage}</span>
>                   </div>
>                   <span className="text-[10px] font-bold px-1.5 py-0.5 rounded-full" style={{ background: config.bg, color: config.color, border: \`1px solid \${config.border}\` }}>
>                     {stageLeads.length}
>                   </span>
>                 </div>
>                 <div className="flex-1 p-3 space-y-2 overflow-y-auto">
>                   {stageLeads.map((lead: any, index: number) => (
>                     <motion.div key={lead.id} initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.25, delay: index * 0.05 }} className="p-3 rounded-lg cursor-pointer group transition-all duration-150" style={{ background: 'rgba(255,255,255,0.03)', border: '1px solid var(--gk-border)' }} whileHover={{ borderColor: config.border, backgroundColor: config.bg }}>
>                       <div className="flex items-start justify-between mb-2">
>                         <p className="text-xs font-semibold text-[var(--gk-text-primary)] leading-tight">{lead.name}</p>
>                       </div>
>                       <div className="text-[10px] text-zinc-400 mb-2">{lead.phone}</div>
>                       {lead.ai_summary && (
>                         <div className="text-[10px] text-zinc-300 italic border-l-2 border-zinc-600 pl-2 mb-2 line-clamp-2">
>                           "{lead.ai_summary}"
>                         </div>
>                       )}
>                       <div className="flex items-center justify-between mt-2">
>                         <span className="text-[10px] px-1.5 py-0.5 rounded-full" style={{ background: 'rgba(255,255,255,0.04)', color: 'var(--gk-text-muted)', border: '1px solid var(--gk-border)' }}>
>                           {lead.channel || 'whatsapp'}
>                         </span>
>                         {lead.intent_score && (
>                           <span className={\`text-[10px] font-bold \${lead.intent_score > 70 ? 'text-emerald-400' : lead.intent_score > 40 ? 'text-amber-400' : 'text-blue-400'}\`}>
>                             Score: {lead.intent_score}
>                           </span>
>                         )}
>                       </div>
>                     </motion.div>
>                   ))}
>                 </div>
>               </div>
>             );
>           })}
>         </div>
>       )}
>     </PageShell>
>   );
> }
> ```
> 
> Apenas substitua o arquivo e me avise."

---

## PROMPT 4: O Token Engine (Backend)

> "Substitua o conteúdo do arquivo `apps/api/src/services/tokenRouter.ts` pelo código abaixo.
> 
> ```typescript
> import { supabaseAdmin } from './supabase';
> 
> export async function debitTokens(
>   orgId: string,
>   operation: string,
>   tokensUsed: number,
>   description?: string
> ): Promise<{ success: boolean; balance_before: number; balance_after: number; tokens_debited: number; reason?: string }> {
>   
>   // Markup de 100% (cobra o dobro do custo real)
>   const cost = tokensUsed * 2;
> 
>   const { data: wallet } = await supabaseAdmin
>     .from('token_wallets')
>     .select('id, balance, reserved')
>     .eq('org_id', orgId)
>     .eq('token_type', 'AI')
>     .single();
> 
>   if (!wallet) {
>     return { success: false, balance_before: 0, balance_after: 0, tokens_debited: 0, reason: 'wallet_not_found' };
>   }
> 
>   const available = wallet.balance - wallet.reserved;
> 
>   if (available < cost) {
>     notifyLowBalance(orgId, available).catch(console.error);
>     return {
>       success: false,
>       balance_before: wallet.balance,
>       balance_after: wallet.balance,
>       tokens_debited: 0,
>       reason: 'insufficient_tokens',
>     };
>   }
> 
>   const { error: updateErr } = await supabaseAdmin
>     .from('token_wallets')
>     .update({ balance: wallet.balance - cost, updated_at: new Date().toISOString() })
>     .eq('id', wallet.id);
> 
>   if (updateErr) {
>     return { success: false, balance_before: wallet.balance, balance_after: wallet.balance, tokens_debited: 0, reason: 'debit_failed' };
>   }
> 
>   await supabaseAdmin.from('token_ledger').insert({
>     org_id: orgId,
>     wallet_id: wallet.id,
>     amount: -cost,
>     type: 'debit',
>     description: description ?? operation,
>   });
> 
>   return {
>     success: true,
>     balance_before: wallet.balance,
>     balance_after: wallet.balance - cost,
>     tokens_debited: cost,
>   };
> }
> 
> export async function creditTokens(
>   orgId: string,
>   amount: number,
>   description: string = 'stripe_topup'
> ): Promise<void> {
>   const { data: wallet } = await supabaseAdmin
>     .from('token_wallets')
>     .select('id, balance')
>     .eq('org_id', orgId)
>     .eq('token_type', 'AI')
>     .single();
> 
>   if (!wallet) return;
> 
>   await supabaseAdmin
>     .from('token_wallets')
>     .update({ balance: wallet.balance + amount, updated_at: new Date().toISOString() })
>     .eq('id', wallet.id);
> 
>   await supabaseAdmin.from('token_ledger').insert({
>     org_id: orgId,
>     wallet_id: wallet.id,
>     amount,
>     type: 'credit',
>     description,
>   });
> }
> 
> async function notifyLowBalance(orgId: string, balance: number): Promise<void> {
>   const n8nUrl = process.env.N8N_WEBHOOK_LOW_BALANCE;
>   if (!n8nUrl) return;
>   await fetch(n8nUrl, {
>     method: 'POST',
>     headers: { 'Content-Type': 'application/json' },
>     body: JSON.stringify({ org_id: orgId, balance }),
>   });
> }
> 
> // Alias para chargeTokens (para compatibilidade)
> export const chargeTokens = debitTokens;
> ```
> 
> Apenas substitua o arquivo e me avise."
> 
---

## PROMPT 5: Integração n8n (Webhook)

> "Abra o arquivo `apps/api/src/modules/webhooks/webhooks.routes.ts`. Encontre a seção `// 1. Evolution API (WhatsApp) → n8n` e adicione a nova rota `POST /webhooks/n8n/incoming` logo abaixo dela.
> 
> Adicione este bloco de código:
> 
> ```typescript
>   // ─────────────────────────────────────────────
>   // 1.5. n8n → Ginkgo Kernel (Execução de Agente)
>   // ─────────────────────────────────────────────
>   app.post('/webhooks/n8n/incoming', async (req, reply) => {
>     const body = req.body as any;
>     const { tenantId, agentId, message, channel } = body;
> 
>     if (!tenantId || !agentId || !message) {
>       return reply.status(400).send({ error: 'tenantId, agentId and message are required' });
>     }
> 
>     // Importa o Kernel dinamicamente para evitar problemas de ciclo
>     const { GinkgoAgentKernel } = require('@ginkgo/agents');
>     const kernel = new GinkgoAgentKernel();
> 
>     const task = {
>       id: \`msg_\${Date.now()}\`,
>       type: 'process_message',
>       payload: { message, channel: channel || 'whatsapp' }
>     };
> 
>     const result = await kernel.execute(task, agentId, tenantId);
> 
>     if (!result.success) {
>       return reply.status(500).send({ error: result.error });
>     }
> 
>     return reply.status(200).send(result);
>   });
> ```
> 
> Apenas insira essa rota no arquivo e me avise."
