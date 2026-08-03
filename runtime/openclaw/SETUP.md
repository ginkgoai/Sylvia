# OpenClaw — runtime da Sylvia (setup verificado)

> Atualizado em 2026-08-03 com comandos confirmados na doc oficial (docs.openclaw.ai). O workspace do OpenClaw usa exatamente os arquivos que este repo já tem na raiz: `AGENTS.md`, `SOUL.md`, `IDENTITY.md`, `USER.md`, `MEMORY.md`, `BOOT.md`, `memory/`. **C:\sylvia-brain é o workspace.**

## 1. Pré-requisitos

- **Node 22.22.3+ / 24.15+ / 25.9+** (26 recomendado) — conferir: `node --version`.
- **ANTHROPIC_API_KEY** (Claude) — o onboarding pede.
- Windows: o caminho mais fácil é o **app nativo (Windows Hub)**; o instalador PowerShell e o gateway em WSL2 também são suportados.

## 2. Instalar e onboardar

```powershell
# Windows (PowerShell)
iwr -useb https://openclaw.ai/install.ps1 | iex

# Onboarding completo (provider + API key + gateway + daemon)
openclaw onboard --install-daemon
```

No wizard: provider **Anthropic**, colar a API key ("env de LLM" fica guardada em `~/.openclaw/`, fora do workspace/repo — nunca commitada). Pulou algo? `openclaw configure` volta ao wizard; `openclaw doctor` diagnostica.

## 3. Apontar o workspace para este repo

Editar `~/.openclaw/openclaw.json`:

```json5
{
  agents: {
    defaults: {
      workspace: "C:\\sylvia-brain",   // no WSL2: "/mnt/c/sylvia-brain"
      skipBootstrap: true,             // nós gerimos os arquivos; não semear defaults
    },
  },
}
```

O OpenClaw carrega automaticamente por sessão: `AGENTS.md` (instruções) → `SOUL.md` (persona) → `IDENTITY.md` (nome/vibe) → `USER.md` (modelo do fundador, orçamento 4k chars) → `MEMORY.md` (memória curada, só na sessão principal) → diários `memory/AAAA-MM-DD.md`. `BOOT.md` roda como checklist no restart do gateway (com hooks internos habilitados).

## 4. Canais

**Web (imediato):**

```bash
openclaw gateway status    # deve escutar na porta 18789
openclaw dashboard         # abre o Control UI no navegador → chat pronto
```

**Telegram (o mais rápido para o celular):**

1. Falar com **@BotFather** → `/newbot` → guardar o token (ex.: bot `SylviaExecBot`). Não reaproveitar o bot "Friday" do Hermes.
2. Configurar em `~/.openclaw/openclaw.json` (ou env `TELEGRAM_BOT_TOKEN`):

```json5
{
  channels: {
    telegram: {
      enabled: true,
      botToken: "SEU_TOKEN_AQUI",   // fica fora do repo
      dmPolicy: "pairing",           // ninguém fala com a Sylvia sem aprovação
    },
  },
}
```

3. Ativar e aprovar a si mesmo (código de pareamento expira em 1h):

```bash
openclaw gateway
openclaw pairing list telegram
openclaw pairing approve telegram <CODE>
```

**WhatsApp:** depois da rotina Telegram estável; número dedicado, nunca o comercial do Leaf.

## 5. Segurança (inegociável)

- `dmPolicy: "pairing"` + aprovar somente o fundador; sem grupos abertos.
- Gateway local (não expor 18789 na internet).
- Segredos vivem em `~/.openclaw/` e variáveis de ambiente — **jamais** no workspace (repo).
- Para isolamento de execução: `agents.defaults.sandbox` (ver doc "Sandboxing").
- Ações A3 continuam regidas por `cognicao/AUTONOMIA.md` — o runtime não altera os gates.

## 6. Memória e git

- Diário: a Sylvia escreve `memory/AAAA-MM-DD.md`; consolidação semanal para o vault (`cognicao/MEMORIA.md`).
- Backup: este repo já é privado (`ginkgoai/Sylvia`). Rotina: `git add . && git commit -m "memoria: ..." && git push` (a própria Sylvia pode propor o commit; push com aprovação).

## 7. Poderes plugáveis

Arsenal (n8n, Postgres, Redis, RAG, APIs, MCPs) e o padrão de disparo determinístico: `cognicao/PODERES.md`. Skills de workspace ficam em `skills/` (maior precedência no OpenClaw).

## 8. Migração do Hermes (legado)

| Item | Destino |
|---|---|
| Bot Telegram "Friday" | Desativar após Sylvia estável no bot novo. |
| `runtime/hermes/config/SOUL.md` | Substituído pelo `SOUL.md` da raiz. |
| Skills `sexta-*` | Recriar como skills de workspace usando `runtime/bridges/` (ver `cognicao/PODERES.md`). |
| `runtime/hermes-memory-compat/` | Congelado; memória canônica é o vault. |
| Instalação `%LOCALAPPDATA%\hermes` | Remover quando a migração for confirmada. |

## 9. Critério de pronto (Fase 1)

1. Sylvia responde no Control UI e no Telegram com persona e boot corretos.
2. Lê e escreve memória conforme protocolo (diário + vault).
3. Heartbeat diário entrega briefing executivo real (ou `HEARTBEAT_OK` silencioso).
4. Nenhuma ação A3 sem aprovação registrada.
