# Validação da arquitetura e propósito (auditoria do todo)

> Loop de validação pedido pelo Gabriel (2026-06-27), depois de ligar a Sexta-feira e desenhar a hierarquia de capacidades. honest-data: o que é sólido, o que é nascente, o que é risco.

## 1. Propósito — claro e servido? ✅
**Ginkgo = empresa AI-native que vende agentes CONFIÁVEIS e AUDITÁVEIS pra B2B.** O produto âncora (LEAF/Callima) = secretária no WhatsApp que qualifica, agenda e **fecha venda — com prova e custo**. A Sexta-feira = o orquestrador pessoal do fundador.
- **O diferencial NÃO é o motor** (commodity: Nous Hermes, OpenClaw…) — é a **governança auditável (Laplace)** + o **produto vertical** + **honest-data**.
- A arquitetura serve isso: o motor é alugado (Hermes), o **moat é o Laplace**. ✔️ Propósito coerente com a arquitetura.

## 2. Coerência — as peças encaixam? ✅ (no desenho)
"Hermes pensa, Laplace governa" + "MCP percebe, Skill age" (ADR 0002) + a **escada de capacidades** (host→sandbox→MCP→integração→dockerizado) + **profile-per-tenant** + contenção por herança (ADR 0004). É um sistema fechado e consistente. As 3 faces (Brann/Nyra/Alfred) + Sexta-feira = personas de um motor. ✔️

## 3. REAL vs CONCEITUAL — o estado verdadeiro (honest-data)
| | REAL (funciona hoje) | NASCENTE / CONCEITUAL |
|---|---|---|
| Vende | **Callima (n8n) fecha venda no WhatsApp** ✓ | — |
| Produto | dashboard LEAF (Inbox/CRM/Agenda/Ofertas/Planos) ✓ · billing (Payment Links) ✓ | PYRE/WAVE (não existem) |
| Cérebro | Brann-delegate (tronco) responde via OpenRouter ✓ · **Sexta-feira (Hermes) viva** via OpenRouter + bridges ✓ | — |
| Governança | Kernel/Boundary/Tasks/lineage REAIS ✓ | envelope de autonomia, gatilhos |
| **Convergência** | — | **Brann = Hermes governado (fatia #30) — NÃO plugado** · profile-per-tenant — não codado |
**Verdade nua:** o **produto VENDÁVEL está real**; o **motor unificado (Hermes governado, multi-tenant) está nascendo**. As duas metades **ainda não convergiram** — e essa convergência é a próxima fronteira.

## 4. Tensões / riscos (o que a validação levanta)
1. 🔴 **GRANDE: o Brann-produto NÃO pode morar no Windows nativo do fundador.** Os buracos POSIX (`/bin/bash`, chat-PTY WSL2-only) + ser SPOF na máquina pessoal + falta de isolamento provam: pra **clientes**, o motor Hermes-produto precisa de **infra dedicada (Docker/Linux)**, não o `C:\sexta-feira` pessoal. → **Reframe:** "Brann = Hermes" = o *software* Nous, deployado **dockerizado/Linux, profile-per-tenant, governado por Laplace** — uma instância SEPARADA da Sexta-feira pessoal.
2. 🟡 **`terminal.backend = docker` (aplicado):** certo pro **produto** (já é container). Pra **Sexta-feira pessoal** complica (o sandbox não enxerga `localhost` dos serviços do host) — pra ela, talvez bundled Git Bash. **A escolha de backend depende do deployment.**
3. 🟡 **Callima tem 3 encarnações:** o workflow n8n (vende), o conceito no tronco (face do LEAF), a pasta `sexta-feira/callima`. Reconciliar qual é a fonte da verdade antes da convergência.
4. 🟡 **OpenRouter = SPOF de créditos.** Mitigar com `hermes fallback` (cadeia de providers).

## 5. Veredito + próximos passos validados
**A arquitetura é sólida e o propósito é claro.** O gap real não é conceitual — é **executar a convergência** (motor↔produto) **na infra certa**.
1. Sexta-feira pessoal: lapidada e viva (✓). Backend dela = decidir (docker vs bundled-bash).
2. **Brann-produto = deployment Hermes dockerizado/Linux** (não o host do fundador) + profile-per-tenant + Laplace. ← isso reescreve a fatia #30.
3. Reconciliar as 3 Callimas.
4. Fallback de provider no Hermes.

_Auditado pela Sexta-feira. A convergência certa = Hermes dockerizado governado, não o agente pessoal no Windows._
