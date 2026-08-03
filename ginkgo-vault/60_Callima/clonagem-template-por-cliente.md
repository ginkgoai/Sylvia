---
tipo: processo
agente: callima
status: ativo
atualizado: 2026-06-16
---

# Clonagem do Template LEAF (Callima) por cliente

Processo padrão para criar a secretária de um novo cliente a partir do **template-mestre**
(`Callima` + `AUDIO FEM`, pasta LEAF no n8n). Vale como processo **manual interino** — quando o
LEAF SaaS estiver pronto, isso vira **provisionamento automático** (assina → tudo nasce sozinho).

## Template-mestre (não editar direto p/ cliente)
- Workflow **Callima** (pasta LEAF) — recursos validados: debounce por token, memória de lead,
  bloco `[[AUDIO]]`, anti-silêncio, prompt refinado, `Ler` com instância dinâmica, loop de envio OK.
- Sub-fluxo de áudio **AUDIO FEM** (voz feminina). Para voz masculina, manter um **AUDIO MASC**.
- Convenção de nomes por cliente: `Callima — Cliente X`, `AUDIO FEM — Cliente X`, `AUDIO MASC — Cliente X`.
- Usar **etiqueta/tag do cliente** no n8n para organizar.

## Passo a passo
1. **Duplicar** o workflow `Callima` → renomear `Callima — Cliente X`; manter na pasta LEAF + etiqueta do cliente.
2. **Duplicar o sub-fluxo de áudio** da voz escolhida → `AUDIO FEM — Cliente X` (ou MASC). No nó de TTS
   do sub-fluxo, ajustar o **voice_id** conforme a voz do cliente.
3. No workflow do cliente, apontar os nós **`Send Audio`** e **`AUDIO`** (executeWorkflow) para o
   **id do sub-fluxo de áudio do cliente**.
4. **Instância Evolution:** criar a instância do cliente (número dele) e **parear o QR**. O template já
   usa `$('Dados').INSTANCIA` (dinâmico) no `Ler` e no envio — então basta a instância certa chegar no payload.
5. **Webhook:** cada cliente com seu **path único** de webhook (ou um webhook compartilhado que roteia
   por `instance`). Registrar o webhook na instância Evolution do cliente.
6. **RAG:** criar **workspace do cliente no AnythingLLM** (base de conhecimento dele) e apontar o nó
   `base_conhecimento_callima` para `/api/v1/workspace/<cliente>/chat`. Subir a base (preços, FAQ, políticas do cliente).
7. **Persona/config:** ajustar o `systemMessage` do agente com o tom/negócio do cliente (no futuro LEAF,
   isso vem de `agent_config` por tenant — não editar prompt à mão).
8. **Isolamento de leads:** a `callima_leads` é compartilhada. Para cliente novo, **separar**: tabela por
   cliente OU coluna `instancia`/`org` na tabela + filtro no `Get Lead`/`Save Lead`. (As chaves Redis
   `_ACC`/`_LAST` já são por número do lead — ok.)
9. **Credenciais:** reutilizar Evolution/Redis/Postgres/ElevenLabs do stack (ou isolar por cliente se exigido).
10. **Ativar** o workflow do cliente e **testar** o fluxo cadastro→QR→config→conversa.

## Checklist de QA (antes de entregar)
- [ ] Responde a 1 mensagem e agrupa rajada (debounce)
- [ ] Lembra do nome/empresa (memória de lead grava em `callima_leads`)
- [ ] Áudio sai com a **voz certa** e é distinto do texto (bloco `[[AUDIO]]`)
- [ ] Nunca fica em silêncio (fallback anti-silêncio)
- [ ] RAG responde com a base **do cliente** (preços/FAQ certos)
- [ ] Não cumprimenta nem pede o nome 2× na mesma conversa
- [ ] Handoff/limites: não fecha contrato nem dá desconto sozinha

## Notas
- **LLM:** hoje Gemini (free tem rate limit). Migrar para **OpenRouter (modelos pagos)** no nó
  `Gemini Brain` quando for escalar — troca de credencial/modelo, sem mexer no fluxo.
- **Features extras** (agenda, Pix, e-mail, mídia, STT) entram como módulos por cima do template, um a um.
- Quando o **LEAF SaaS** assumir, este processo manual é substituído por provisionamento automático.
