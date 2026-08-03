---
title: "Ginkgo Core - Cérebro Externo AI"
source: "https://chatgpt.com/g/g-p-68e0a0b393cc8191a0f44ad743e1117d/c/69c085a8-e0dc-83e8-abe7-12360ca0e729"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
Sim, Imagine Ramificado nos três serviços: Atendimento(clientes, conversas, contato humano, tudo que englobe o universo de Brann), Conteúdo(criação de vídeos, posts, carroceis, roteiros de redes sociais, tudo que envolva o universo de Nyra), Ops(gestão de processos, delegações, plataformas para utilizar como meta ads, Tiktok ads, diretrizes, APIs, manual técnico de skills e maneiras de usar) ramifique assim o ginkgo brain

GINKGO\_BRAIN\_—\_System\_Prompt\_Completo.md

Arquivo

qua., 15 de abr. às 2:24

```markdown
# Guia Prático — Segundo Cérebro Automático com Obsidian + Claude

Este guia ensina a configurar **Obsidian + Claude** para que, **em toda nova sessão**, o Claude:
- recupere contexto automaticamente
- registre apenas o que importa
- organize conhecimento em Markdown
- evite duplicações
- evolua o cérebro ao longo do tempo  

Sem integrações complexas.  
Sem memória volátil.  
Apenas **filesystem + regras claras**.

---

## VISÃO GERAL

Claude **não se conecta ao Obsidian**.  
Claude **opera uma pasta Markdown**.  
O Obsidian apenas **visualiza e navega**.

\`\`\`text
Você
 ↓
Claude (chat ou Claude Code)
 ↓
Arquivos .md (cofre)
 ↓
Obsidian (grafo, backlinks, visual)
```

Toda persistência vem dos arquivos.

---

## ETAPA 1 — CRIAR O COFRE

### 1.1 Criar a pasta base

```markdown
mkdir -p ~/second-brain
cd ~/second-brain
```

### 1.2 Estrutura mínima

```markdown
second-brain/
├─ index.md
├─ SYSTEM.md
├─ USER.md
├─ STATE.md
├─ inbox/
├─ claims/
├─ methods/
├─ insights/
├─ logs/
├─ mocs/
```

Abra essa pasta como **Vault** no Obsidian.

---

## ETAPA 2 — ARQUIVOS-ÂNCORA (MEMÓRIA PERMANENTE)

Esses arquivos **sempre devem ser lidos pelo Claude** no início de qualquer sessão.

---

### SYSTEM.md — Regras imutáveis

```markdown
# SYSTEM — Regras do Segundo Cérebro

Este diretório é um sistema cognitivo persistente.

Regras absolutas:
- Nunca confiar em memória de chat
- Sempre ler index.md, SYSTEM.md, USER.md e STATE.md antes de agir
- Nunca salvar conversas completas
- Converter tudo em conhecimento reutilizável
- Usar apenas Markdown
- Evitar duplicação; atualizar notas existentes
- Priorizar clareza visual e wikilinks

Fluxo obrigatório:
Executar → Registrar → Conectar → Curar
```

---

### USER.md — Contexto do usuário

```markdown
# USER — Perfil

Nome: {{nome}}
Fuso horário: {{timezone}}

Características cognitivas:
- Alto volume de ideias
- Pensamento não linear
- Preferência por estrutura clara

Objetivo do sistema:
- Externalizar memória
- Evitar retrabalho
- Construir conhecimento acumulativo
```

---

### STATE.md — Estado vivo do sistema

```markdown
# STATE — Estado Atual

Última atualização: {{YYYY-MM-DD}}

Foco atual:
- {{tema ou projeto principal}}

Padrões recentes:
- {{insight recorrente}}
- {{decisão ativa}}

Pendências:
- Revisar inbox
- Consolidar notas similares
```

> Este arquivo **é atualizado pelo Claude** ao longo do tempo.

---

## ETAPA 3 — INDEX (PONTO DE ENTRADA)

```markdown
# Segundo Cérebro

Sistema de conhecimento persistente.

## Entrada
- [[inbox/]]

## Estrutura
- [[claims/]] — verdades e princípios
- [[methods/]] — como fazer
- [[insights/]] — aprendizados
- [[logs/]] — histórico factual
- [[mocs/]] — mapas de conteúdo
```

---

## ETAPA 4 — USAR O CLAUDE CODE (RECOMENDADO)

### 4.1 Instalar

```markdown
npm install -g @anthropic-ai/claude-code
```

### 4.2 Iniciar no diretório do cofre

```markdown
cd ~/second-brain
claude
```

Claude agora **lê e escreve no cérebro**.

---

## ETAPA 5 — PROMPT PADRÃO DE INÍCIO (OBRIGATÓRIO)

Use **em toda nova sessão** (chat ou CLI):

```markdown
Antes de responder qualquer coisa:
1. Leia index.md, SYSTEM.md, USER.md e STATE.md
2. Atualize seu contexto a partir desses arquivos
3. Aplique as regras do sistema
```

Isso garante **continuidade entre sessões**, mesmo após longos intervalos.

---

## ETAPA 6 — TIPOS DE CONHECIMENTO (REGRA CENTRAL)

Claude **nunca salva texto cru**.  
Tudo deve virar **um dos quatro tipos**:

### Claim — Verdade recorrente

- princípios
- decisões técnicas
- padrões estáveis

### Method — Como fazer

- processos
- passo a passo
- playbooks

### Insight — Aprendizado

- conexão nova
- melhoria
- atalho mental

### Log — Registro factual

- evento
- ação
- histórico

---

## ETAPA 7 — INBOX (ENTRADA TEMPORÁRIA)

`inbox/` recebe material bruto **temporariamente**.

Exemplo:

```markdown
# Inbox — {{data}}

Conteúdo ainda não processado.
Nada aqui é definitivo.
```

Claude deve:

- mover conteúdo da inbox
- converter em claim/method/insight/log
- limpar a inbox

---

## ETAPA 8 — COMO O SALVAMENTO ACONTECE AUTOMATICAMENTE

Durante a conversa, o Claude deve:

1. Responder normalmente
2. Identificar o que é reutilizável
3. Verificar se algo similar já existe
4. Atualizar ou criar a nota adequada
5. Linkar com notas relacionadas

Você pode reforçar com comandos simples:

```markdown
Salve isso no cérebro.
Organize isso como conhecimento.
```

---

## ETAPA 9 — CURADORIA ENTRE SESSÕES

Em qualquer momento (ou início de um novo dia):

```markdown
Revise o cofre.
Consolide notas redundantes.
Melhore links fracos.
Atualize o STATE.md.
```

Claude age como **curador cognitivo**.

---

## ETAPA 10 — PRINCÍPIOS QUE GARANTEM FUNCIONAMENTO

- ❌ Nunca confiar em histórico de chat
- ❌ Nunca salvar conversa inteira
- ❌ Nunca duplicar ideias
- ✅ Sempre linkar
- ✅ Poucos arquivos, bem conectados
- ✅ Revisão periódica

---

## RESULTADO FINAL

Mesmo após dias ou meses:

- Claude relê o cérebro
- recupera decisões
- reconhece padrões
- evita repetição
- evolui o sistema

Não é memória artificial.  
É **memória arquitetada**.

---

## RESUMO EM UMA LINHA

> Claude pensa em sessões.  
> O Obsidian lembra para sempre.

```markdown
Se quiser, posso entregar **:contentReference[oaicite:0]{index=0}**, ou **:contentReference[oaicite:1]{index=1}**.
```

\# 🧠 Segundo Cérebro Automático — Obsidian + Claude > Arquitetura passo a passo para um sistema cognitivo persistente operado por Claude --- ## Visão Geral Claude \*\*não se conecta ao Obsidian\*\*. Claude \*\*opera uma pasta Markdown\*\*. O Obsidian apenas \*\*visualiza e navega\*\*.
```
Você
 ↓
Claude (Claude Code ou chat)
 ↓
Arquivos .md (cofre local)
 ↓
Obsidian (grafo, backlinks, visualização)
```
Toda persistência vem dos arquivos. Sem banco de dados. Sem integrações complexas. Apenas \*\*filesystem + regras claras\*\*. --- ## Etapa 1 — Criar o Cofre ### 1.1 Criar a pasta base
```
bash
mkdir -p ~/second-brain
cd ~/second-brain
```
\### 1.2 Estrutura mínima de pastas
```
second-brain/
├─ index.md          ← ponto de entrada do sistema
├─ SYSTEM.md         ← regras imutáveis do cérebro
├─ USER.md           ← perfil e contexto do usuário
├─ STATE.md          ← estado vivo e foco atual
├─ inbox/            ← entrada temporária de ideias brutas
├─ claims/           ← verdades, princípios, decisões estáveis
├─ methods/          ← processos, playbooks, passo a passos
├─ insights/         ← aprendizados e conexões novas
├─ logs/             ← histórico factual de eventos e ações
└─ mocs/             ← mapas de conteúdo por tema
```
\> Abra essa pasta como \*\*Vault\*\* no Obsidian. --- ## Etapa 2 — Arquivos-Âncora (Memória Permanente) Esses quatro arquivos são a \*\*memória estrutural\*\* do sistema. Claude deve lê-los \*\*obrigatoriamente\*\* no início de toda sessão. --- ### `SYSTEM.md` — Regras Imutáveis
```
markdown
# SYSTEM — Regras do Segundo Cérebro

Este diretório é um sistema cognitivo persistente.

## Regras absolutas
- Nunca confiar em memória de chat
- Sempre ler index.md, SYSTEM.md, USER.md e STATE.md antes de agir
- Nunca salvar conversas completas
- Converter tudo em conhecimento reutilizável
- Usar apenas Markdown
- Evitar duplicação; atualizar notas existentes
- Priorizar clareza visual e wikilinks [[link]]

## Fluxo obrigatório
Executar → Registrar → Conectar → Curar
```
\--- ### `USER.md` — Contexto do Usuário
```
markdown
# USER — Perfil

Nome: {{seu nome}}
Fuso horário: {{America/Sao_Paulo}}

## Características cognitivas
- Alto volume de ideias simultâneas
- Pensamento não linear
- Preferência por estrutura visual clara

## Objetivo do sistema
- Externalizar memória de longo prazo
- Evitar retrabalho entre sessões
- Construir conhecimento acumulativo e consultável
```
\--- ### `STATE.md` — Estado Vivo do Sistema
```
markdown
# STATE — Estado Atual

Última atualização: {{YYYY-MM-DD}}

## Foco atual
- {{tema ou projeto principal em andamento}}

## Padrões recentes
- {{insight recorrente das últimas sessões}}
- {{decisão ativa relevante}}

## Pendências
- Revisar inbox/
- Consolidar notas similares em claims/ ou methods/
```
\> Este arquivo é \*\*atualizado pelo Claude\*\* ao longo do tempo, não pelo usuário. --- ### `index.md` — Ponto de Entrada
```
markdown
# Segundo Cérebro

Sistema de conhecimento persistente operado por Claude.

## Entrada
- [[inbox/]] — ideias brutas aguardando processamento

## Estrutura de conhecimento
- [[claims/]]   — verdades e princípios
- [[methods/]]  — como fazer coisas
- [[insights/]] — aprendizados e conexões
- [[logs/]]     — histórico factual
- [[mocs/]]     — mapas de conteúdo por área
```
\--- ## Etapa 3 — Instalar e Iniciar o Claude Code O \*\*Claude Code\*\* é o modo recomendado porque acessa o filesystem diretamente. ### 3.1 Instalar
```
bash
npm install -g @anthropic-ai/claude-code
```
\### 3.2 Iniciar dentro do cofre
```
bash
cd ~/second-brain
claude
```
\> Claude agora lê e escreve no cérebro com acesso completo ao diretório. --- ## Etapa 4 — Prompt Padrão de Início de Sessão Use este prompt \*\*em toda nova sessão\*\* (chat ou CLI):
```
Antes de responder qualquer coisa:
1. Leia index.md, SYSTEM.md, USER.md e STATE.md
2. Atualize seu contexto interno com base nesses arquivos
3. Aplique todas as regras do sistema durante esta sessão
```
\> Isso garante \*\*continuidade cognitiva\*\* entre sessões, mesmo após longos intervalos. --- ## Etapa 5 — Os Quatro Tipos de Conhecimento Claude \*\*nunca salva texto bruto\*\*. Tudo o que vale ser guardado deve ser convertido em um dos quatro tipos: | Tipo | Pasta | O que é | Exemplos | |------|-------|---------|----------| | \*\*Claim\*\* | `claims/` | Verdade recorrente e estável | Princípios, decisões técnicas, padrões | | \*\*Method\*\* | `methods/` | Como fazer algo | Processos, playbooks, passo a passos | | \*\*Insight\*\* | `insights/` | Aprendizado ou conexão nova | Melhorias, atalhos mentais, epifanias | | \*\*Log\*\* | `logs/` | Registro factual de evento | Ação tomada, histórico, decisão datada | ### Exemplos de notas bem formadas \*\* `claims/agentes-precisam-de-contexto-explicito.md` \*\*
```
markdown
# Claim — Agentes precisam de contexto explícito

Sem contexto injetado, agentes LLM repetem erros entre sessões.

## Por que isso é verdade
- Modelos não têm memória persistente nativa
- O filesystem é a única forma confiável de persistência

## Onde isso se aplica
- [[methods/prompt-inicio-sessao]]
- [[logs/2024-01-10-sessao-ginkgo]]
```
\*\* `methods/criar-agente-n8n.md` \*\*
```
markdown
# Method — Criar agente no n8n

## Passos
1. Criar workflow base com trigger HTTP
2. Adicionar nó AI Agent com memory buffer
3. Conectar ao Evolution API
4. Configurar system prompt com [[claims/]]

## Relacionado
- [[insights/memory-buffer-vs-session-memory]]
```
\--- ## Etapa 6 — Inbox: Entrada Temporária A pasta `inbox/` recebe \*\*material bruto\*\* que ainda não foi processado. \*\*Exemplo de nota de inbox:\*\*
```
markdown
# Inbox — 2024-01-15

Ideia sobre usar Redis para cache de sessões no Lexra.
Pode ser útil para acelerar autenticação no eProc.

> ⚠️ Não processado. Mover para claims/ ou methods/ na próxima sessão.
```
\*\*Claude deve:\*\* 1. Ler a inbox no início da sessão 2. Converter cada item em `claim/method/insight/log` 3. Criar os links (`[[wikilinks]]`) adequados 4. Limpar ou arquivar o item da inbox --- ## Etapa 7 — Como o Salvamento Acontece Automaticamente Durante a conversa, o Claude executa este loop internamente:
```
1. Responder ao usuário normalmente
2. Identificar o que é conhecimento reutilizável
3. Verificar se algo similar já existe no cofre
4. Atualizar nota existente OU criar nova nota no tipo correto
5. Adicionar wikilinks para notas relacionadas
6. Atualizar STATE.md se necessário
```
\*\*Comandos que você pode usar para reforçar:\*\*
```
Salve isso no cérebro.
Organize isso como conhecimento.
Isso é um novo claim ou atualiza um existente?
Registre no log de hoje.
```
\--- ## Etapa 8 — Curadoria Entre Sessões Em qualquer momento (ou no início de um novo dia), use:
```
Revise o cofre.
Consolide notas redundantes.
Melhore links fracos.
Atualize o STATE.md com o foco atual.
```
\> Claude age como \*\*curador cognitivo\*\* — não apenas executor de tarefas. --- ## Etapa 9 — Princípios que Garantem o Funcionamento | ❌ Nunca | ✅ Sempre | |----------|----------| | Confiar no histórico de chat | Ler os arquivos-âncora no início | | Salvar conversa inteira | Extrair apenas o que é reutilizável | | Duplicar ideias | Atualizar notas existentes | | Deixar inbox acumular | Processar e mover para o tipo correto | | Criar nota sem links | Linkar com notas relacionadas | --- ## Etapa 10 — Manutenção Periódica (Opcional mas Recomendado) \*\*Semanal:\*\*
```
Revise claims/ e elimine duplicatas.
Atualize methods/ com melhorias aprendidas.
Consolide insights/ em claims/ quando confirmados.
```
\*\*Mensal:\*\*
```
Gere um MOC (Mapa de Conteúdo) novo se um tema cresceu muito.
Arquive logs/ antigos em pasta logs/archive/YYYY/.
Revise USER.md se seu perfil ou objetivos mudaram.
```
\--- ## Resultado Final Mesmo após dias, semanas ou meses sem sessão ativa: - Claude relê o cérebro e \*\*recupera o contexto completo\*\* - Reconhece decisões passadas e \*\*evita contradições\*\* - Identifica padrões e \*\*evolui o sistema\*\* - Não repete trabalho já feito > Não é memória artificial. > É \*\*memória arquitetada\*\*. --- ## Resumo em Uma Linha > \*\*Claude pensa em sessões. O Obsidian lembra para sempre.\*\* --- \*Arquitetura gerada para uso com Claude Code + Obsidian como vault local.\* \*Compatível com qualquer projeto: Ginkgo AI, Lexra, Deriva Estelar, ou qualquer outro contexto.\*

Perfeito. O guia que você trouxe **já está correto, completo e operacional**.  
A única coisa que faltava para fechar o ciclo “automático e natural” é **um mecanismo explícito de auto-hidratação em TODA nova sessão**, sem depender de você lembrar de colar prompt.

Abaixo está **um complemento enxuto**, em **Markdown**, para você **anexar ao final do guia** ou salvar como `README-AUTO.md`.

---

```markdown
# Anexo — Continuidade Automática entre Sessões

Este anexo define como garantir que **toda nova sessão do Claude**
— independentemente do tempo decorrido —
recupere, consolide e evolua o Segundo Cérebro automaticamente.

---

## Regra de Ouro da Continuidade

Claude **não deve confiar em memória de chat anterior**.

Toda sessão começa assumindo:
> “Nada foi lembrado. Tudo precisa ser relido.”

A persistência é **100% delegada ao filesystem**.

---

## Ritual Obrigatório de Início de Sessão

Em **toda nova sessão**, Claude deve executar este ritual **antes de responder**:
```

RITUAL-DE-INÍCIO:

1. Ler SYSTEM.md
2. Ler USER.md
3. Ler STATE.md
4. Ler index.md
5. Verificar inbox/
```markdown
Esse ritual **não é opcional**.

---

## Prompt de Auto-Hidratação (Sessão Zero)

Use este prompt como **primeira mensagem de qualquer sessão**:
```

Execute o ritual de início.  
Reidrate completamente o contexto a partir do cofre.  
Depois disso, confirme que está pronto para operar.

```markdown
Resultado esperado:
- Claude entende quem é o usuário
- Claude entende as regras
- Claude entende o foco atual
- Claude detecta pendências
- Claude evita repetir decisões

---

## Consolidação Automática de Sessões Passadas

Após o ritual de início, Claude deve executar mentalmente:
```

CHECK-DE-CONSISTÊNCIA:

- Existem claims similares que deveriam ser consolidados?
- Algum insight recente deveria virar claim?
- O STATE.md reflete o foco real atual?
```markdown
Se sim:
- Atualizar arquivos existentes
- Nunca criar duplicações
- Registrar ajustes em logs/

---

## Salvamento Implícito (Modo Padrão)

Durante a sessão, Claude deve assumir:

> “Se algo for repetível, aplicável no futuro ou decisivo,
> isso não pode morrer no chat.”

Portanto:
- Responder ao usuário
- Extrair conhecimento
- Atualizar o cofre silenciosamente
- Manter o fluxo natural da conversa

---

## Atualização do STATE.md

O \`STATE.md\` deve ser atualizado sempre que ocorrer:

- Mudança de foco
- Nova decisão ativa
- Encerramento de um tema
- Abertura de um novo projeto mental

Formato esperado:
- Curto
- Objetivo
- Sem histórico excessivo

---

## Encerramento de Sessão (Opcional)

Se a sessão estiver terminando, Claude pode executar:
```

Encerrar sessão.  
Garantir que tudo relevante foi salvo.  
Estado do sistema consistente.

```markdown
Nenhum output é necessário — apenas consistência interna.

---

## Garantia de Evolução ao Longo do Tempo

Se este protocolo for seguido:

- O cofre cresce, mas não incha
- O conhecimento se consolida
- Decisões deixam de ser rediscutidas
- O Claude parece “lembrar”, mas está apenas lendo bem

---

## Princípio Final

> Sessões são descartáveis.  
> Arquivos são soberanos.

Se o arquivo está correto, o sistema está correto.
```

---

### Status final da arquitetura

- ✅ Persistência real (filesystem)
- ✅ Continuidade entre sessões
- ✅ Zero dependência de memória volátil
- ✅ Escalável para meses ou anos
- ✅ Compatível com CLI ou chat
- ✅ Visualmente navegável no Obsidian

Se quiser, o próximo passo possível é:

- um **checklist de auditoria semanal automática**
- ou um **prompt ultra-curto (3 linhas) para uso diário**
- ou uma **versão “somente leitura + escrita silenciosa”**

Você decide.

Abaixo está o **passo a passo 100% por CLI**, do zero até o sistema funcionando de forma contínua.  
Sem teoria. Só comandos + o que cada um faz.

---

```markdown
# 0) PRÉ-REQUISITOS
# - Node.js 18+ instalado
# - Obsidian já instalado (GUI)
# - Conta Claude ativa
```

---

## 1) Criar o cofre (filesystem = memória)

```markdown
mkdir -p ~/second-brain
cd ~/second-brain
```
```markdown
mkdir inbox claims methods insights logs mocs
```

---

## 2) Criar arquivos-âncora (memória estrutural)

### SYSTEM.md

```markdown
cat << 'EOF' > SYSTEM.md
# SYSTEM — Regras do Segundo Cérebro

Este diretório é um sistema cognitivo persistente.

Regras absolutas:
- Nunca confiar em memória de chat
- Sempre ler index.md, SYSTEM.md, USER.md e STATE.md antes de agir
- Nunca salvar conversas completas
- Converter tudo em conhecimento reutilizável
- Usar apenas Markdown
- Evitar duplicação; atualizar notas existentes
- Priorizar clareza visual e wikilinks [[link]]

Fluxo obrigatório:
Executar → Registrar → Conectar → Curar
EOF
```

### USER.md

```markdown
cat << 'EOF' > USER.md
# USER — Perfil

Nome: SEU_NOME
Fuso horário: America/Sao_Paulo

Características:
- Alto volume de ideias
- Pensamento não linear
- Preferência por estrutura clara

Objetivo:
- Externalizar memória
- Evitar retrabalho
- Construir conhecimento acumulativo
EOF
```

### STATE.md

```markdown
cat << 'EOF' > STATE.md
# STATE — Estado Atual

Última atualização: $(date +%F)

Foco atual:
- indefinido

Padrões recentes:
- nenhum

Pendências:
- Revisar inbox/
EOF
```

### index.md

```markdown
cat << 'EOF' > index.md
# Segundo Cérebro

Sistema de conhecimento persistente.

## Entrada
- [[inbox/]]

## Estrutura
- [[claims/]]
- [[methods/]]
- [[insights/]]
- [[logs/]]
- [[mocs/]]
EOF
```

---

## 3) Abrir no Obsidian (uma vez)

```markdown
# Não é CLI, mas é só isso:
# Obsidian → Open Folder as Vault → ~/second-brain
```

Depois disso, **nunca mais mexe por aqui**.  
O Obsidian só observa.

---

## 4) Instalar o Claude Code

```markdown
npm install -g @anthropic-ai/claude-code
```

Verificar:

```markdown
claude --version
```

---

## 5) Iniciar o Claude dentro do cérebro

```markdown
cd ~/second-brain
claude
```

A partir daqui, Claude **vê e escreve** no cofre.

---

## 6) Comando obrigatório de início de sessão

Sempre que abrir o Claude (CLI ou chat):

```markdown
Antes de responder qualquer coisa:
1. Leia SYSTEM.md, USER.md, STATE.md e index.md
2. Reidrate totalmente o contexto
3. Aplique as regras do sistema
```

(cole isso como primeira mensagem)

---

## 7) Uso normal (durante a sessão)

Você conversa normalmente.

Quando algo for importante, use **comandos naturais**:

```markdown
Salve isso como claim.
Isso vira um method.
Registre isso no log de hoje.
Organize isso no cérebro.
```

Claude cria/atualiza arquivos automaticamente.

---

## 8) Inbox via CLI (entrada rápida)

Adicionar ideia crua:

```markdown
cat << 'EOF' >> inbox/$(date +%F).md
- Ideia sobre X
- Possível melhoria em Y
EOF
```

Claude processa isso na próxima sessão.

---

## 9) Curadoria manual (quando quiser)

```markdown
Revise o cofre.
Consolide duplicações.
Atualize o STATE.md.
```

---

## 10) Rotina automática opcional (cron)

Criar script:

```markdown
mkdir -p scripts
cat << 'EOF' > scripts/revisao.sh
#!/bin/bash
claude << 'PROMPT'
Leia SYSTEM.md, USER.md, STATE.md e index.md.
Revise o cofre.
Consolide notas redundantes.
Atualize o STATE.md.
PROMPT
EOF
```

Permissão:

```markdown
chmod +x scripts/revisao.sh
```

Agendar semanal:

```markdown
crontab -e
```

Adicionar:

```markdown
0 9 * * 1 cd ~/second-brain && ./scripts/revisao.sh
```

---

## 11) Resultado prático

- Nova sessão → Claude lê tudo
- Claude não “lembra”, **ele consulta**
- Nada se perde
- Nada se repete
- O grafo fica mais inteligente com o tempo

---

## Regra final (grave isso)

```markdown
Sessões morrem.
Arquivos sobrevivem.
```

Se quiser, próximo passo possível:

- versão **minimal (3 comandos só)**
- ou **modo 100% automático sem prompts manuais**
- ou **integração com voz (ElevenLabs)**