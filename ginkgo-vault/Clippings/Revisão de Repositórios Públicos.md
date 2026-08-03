---
title: "Revisão de Repositórios Públicos"
source: "https://chatgpt.com/c/6a6e23f3-16d4-83e9-9828-d20d88c9ad23"
author:
published:
created: 2026-08-02
description: "ChatGPT conversation with 5 messages"
tags:
  - "clippings"
---
**Confere parcialmente.** É tecnicamente possível fazer o Codex chamar o Claude Code, mas isso não deve ser o centro da arquitetura.

A composição mais econômica seria:

```
Orquestrador local
        │
        ├── Claude Code — 70–85% do trabalho pesado
        │   arquitetura, implementação longa, refactors e documentação
        │
        ├── Codex — 15–30% do trabalho crítico
        │   revisão independente, testes, CI, segurança e correções cirúrgicas
        │
        └── Git + CI — autoridade objetiva
```

## O que é possível

O Claude Code pode ser chamado de forma não interativa:

```bash
claude -p "Analise e implemente o épico E003" \
  --output-format json \
  --max-turns 20
```

Também existe SDK oficial em TypeScript e Python para executá-lo como subprocesso, controlar diretório, ferramentas permitidas, número de turnos e coletar saída estruturada. [^1]

Como o Codex local consegue trabalhar no terminal, executar comandos e usar ferramentas externas, ele poderia chamar um script como:

```bash
./tools/delegate-to-claude.sh E003
```

Esse script chamaria o Claude Code, salvaria o resultado e devolveria ao Codex apenas um relatório resumido.

## Limitação financeira importante

As assinaturas continuam separadas:

- Claude Max fornece uso do Claude Code autenticado pela conta Claude;
- esse uso compartilha os limites do Claude/Claude Code do plano Max;
- uso da Anthropic API é outro sistema de cobrança;
- Codex Plus possui seu próprio pool de uso agêntico e eventuais créditos adicionais. [^2]

Portanto, Claude Max **não é uma chave de API ilimitada**. Para automações oficiais via SDK/API, a documentação da Anthropic recomenda uma chave de API dedicada, cobrada separadamente. [^1]

Na prática, o modo econômico seria chamar o **Claude Code local autenticado pelo Max**, não a API Anthropic.

---

## Por que Codex → Claude não é sempre mais barato

Quando Codex orquestra Claude:

1. Codex lê o problema;
2. Codex prepara o prompt;
3. Codex chama Claude;
4. Claude lê novamente o contexto;
5. Claude implementa;
6. Codex lê toda a resposta;
7. Codex revisa o código.

Há consumo nos dois lados e duplicação de contexto.

O resultado pode ser pior quando:

- Codex envia contexto incompleto;
- Claude e Codex discordam da arquitetura;
- ambos modificam os mesmos arquivos;
- Claude produz uma resposta enorme que Codex precisa reler;
- o loop automático continua sem um gate humano;
- um agente aceita superficialmente o resultado do outro.

Por isso, não recomendo:

```
Codex conversa livremente com Claude
Claude responde livremente ao Codex
Ambos editam o mesmo branch
```

Recomendo uma comunicação por **artefatos versionados**.

---

## Arquitetura recomendada: Ginkgo Build Orchestrator

Crie um pequeno orquestrador independente dos dois modelos:

```
tools/ai-orchestrator/
├── orchestrator.ts
├── prompts/
│   ├── architect.md
│   ├── implement.md
│   ├── review.md
│   └── repair.md
├── schemas/
│   ├── implementation-plan.schema.json
│   ├── review.schema.json
│   └── handoff.schema.json
└── runs/
    └── E003/
        ├── request.md
        ├── claude-plan.json
        ├── claude-implementation.json
        ├── test-results.json
        ├── codex-review.md
        └── final-report.md
```

O orquestrador decide quem trabalha, não Codex ou Claude.

## Fluxo

```
1. Você define o épico
        ↓
2. Claude cria plano e contratos
        ↓
3. Claude implementa o trabalho pesado
        ↓
4. Testes locais são executados
        ↓
5. Codex revisa apenas diff + specs + resultados
        ↓
6. Claude recebe findings objetivos
        ↓
7. Claude corrige
        ↓
8. Codex valida regressões
        ↓
9. CI decide
```

Isso usa mais Claude e preserva Codex para tarefas de alto valor.

---

## Divisão de trabalho ideal

## Claude Max — principal executor

Use Claude para:

- mapear bases grandes;
- escrever ADRs;
- implementar épicos extensos;
- refatorar múltiplos packages;
- criar migrations;
- construir APIs;
- implementar UI;
- documentar arquitetura;
- investigar bugs complexos;
- corrigir findings do Codex.

Distribuição sugerida:

```
Claude Sonnet: 65%
Claude Opus:   20%
Codex:         15%
```

Opus entra somente em:

- arquitetura do Tree;
- segurança multi-tenant;
- secrets boundary;
- idempotência;
- billing;
- reconciliação;
- revisão pré-produção.

## Codex Plus — avaliador independente

Use Codex para:

- revisar o diff;
- procurar bugs concretos;
- escrever testes de regressão;
- verificar critérios de aceitação;
- corrigir CI;
- executar lint/typecheck/test/build;
- revisar isolamento de tenant;
- localizar mudanças fora do escopo;
- fazer patches pequenos;
- testar o golden path.

Evite gastar Codex com:

- leitura repetida de todo o monorepo;
- documentação extensa;
- implementação integral de épicos;
- discussões arquiteturais longas;
- geração de boilerplate que Claude já pode produzir.

---

## Integração local simples

Um wrapper poderia receber um pacote de trabalho:

```bash
#!/usr/bin/env bash
set -euo pipefail

EPIC="${1:?Informe o épico, por exemplo E003}"
RUN_DIR=".ai/runs/${EPIC}"
PROMPT_FILE="${RUN_DIR}/claude-prompt.md"
OUTPUT_FILE="${RUN_DIR}/claude-result.json"

mkdir -p "$RUN_DIR"

test -f "$PROMPT_FILE" || {
  echo "Prompt não encontrado: $PROMPT_FILE" >&2
  exit 1
}

claude -p "$(cat "$PROMPT_FILE")" \
  --output-format json \
  --max-turns 25 \
  > "$OUTPUT_FILE"

jq -e '.is_error == false' "$OUTPUT_FILE" >/dev/null

echo "Resultado salvo em $OUTPUT_FILE"
```

Codex não precisaria receber a conversa completa. Ele leria:

- especificação;
- `git diff`;
- testes;
- resumo do Claude;
- arquivos alterados.

Isso reduz bastante o consumo do Codex.

---

## MCP: alternativa mais integrada

Também seria possível expor Claude como uma ferramenta MCP local:

```
claude_delegate.plan
claude_delegate.implement
claude_delegate.review
claude_delegate.repair
```

Codex chamaria algo parecido com:

```
claude_delegate.implement({
  epic: "E003",
  repository: "ginkgo-connect",
  allowed_paths: [
    "packages/capabilities",
    "apps/api",
    "tests"
  ],
  max_turns: 20
})
```

Internamente, o servidor executaria `claude -p`.

Vantagens:

- entrada e saída estruturadas;
- limite de turnos;
- paths permitidos;
- logs;
- timeouts;
- registro de consumo;
- política por operação.

Riscos:

- Codex pode delegar demais;
- um prompt mal formulado pode gerar mudanças amplas;
- o Claude subprocesso recebe acesso ao repositório;
- credenciais locais precisam ficar isoladas;
- automação não supervisionada pode consumir rapidamente a cota Max.

Começaria pelo wrapper CLI. MCP entra após o fluxo estar estável.

---

## Onde essa integração funciona melhor

## Codex local + Claude Code local

É a configuração mais adequada:

```
Sua máquina
├── repositório Git
├── Claude Code autenticado pelo Max
├── Codex CLI/app autenticado pelo Plus
├── scripts de orquestração
└── Docker/testes locais
```

## Codex em ambiente remoto ou cloud

Não conte com o login local do Claude Max estando disponível dentro de outro sandbox.

Nesse cenário seria necessário, em geral:

- chave da API Anthropic;
- serviço remoto próprio;
- gateway;
- ou alguma forma explícita de autenticação.

Isso provavelmente adicionaria cobrança de API e eliminaria parte da economia pretendida. A documentação oficial separa claramente o uso da assinatura Max do uso pago da API. [^2]

---

## Modelo operacional para a Ginkgo

## Modo BUILD

Claude implementa.

```
Claude:
- lê o épico;
- cria plano;
- modifica código;
- executa testes;
- produz relatório.
```

## Modo REVIEW

Codex não implementa tudo novamente.

```
Codex:
- lê specs;
- lê diff;
- verifica testes;
- procura violações;
- produz findings.
```

## Modo REPAIR

Claude corrige somente os findings.

```
Claude:
- recebe lista fechada;
- corrige;
- cria testes de regressão;
- atualiza relatório.
```

## Modo RELEASE

Codex faz validação final.

```
Codex:
- executa gates;
- verifica golden path;
- confirma ausência de mudanças fora do escopo;
- emite READY ou BLOCKED.
```

---

## Economia esperada

Não é possível garantir um percentual exato sem medir tarefas reais, mas a configuração tende a reduzir o uso do Codex quando:

- Claude faz implementação extensa;
- Codex recebe apenas diff e resumo;
- revisões são limitadas por escopo;
- não há conversas duplicadas;
- o contexto é mantido em arquivos;
- Codex não relê o monorepo inteiro a cada rodada.

Meta inicial razoável:

| Recurso | Participação |
| --- | --- |
| Claude Max | 75–85% |
| Codex Plus | 15–25% |

## Conclusão

**Dá para integrar, mas o melhor desenho não é Codex como “chefe do Claude”.**

O mais eficiente é:

```
Orquestrador determinístico
        ↓
Claude faz o trabalho pesado
        ↓
Codex age como revisor independente e verificador
        ↓
Claude corrige
        ↓
CI libera
```

Assim você aproveita o volume maior do Claude Max, preserva o Codex Plus para os pontos em que uma segunda inteligência realmente agrega e evita pagar duas vezes para ambos manterem o mesmo contexto.

---

**Você disse**

Vamos seguir a recomendação, neste primeiro momento, até eu entender o processo de contrução, me guie leigamente, bem instrutivo e passo a passo para não perder detalhe e os resultados serem os esperados.

---

Sim. Neste primeiro momento, usaremos um processo **manual, sequencial e auditável**. Nada de MCP entre Claude e Codex, scripts automáticos ou dois agentes editando simultaneamente. O objetivo inicial é você entender exatamente o que está acontecendo.

## Modelo de trabalho inicial

```
Você define o objetivo
        ↓
Claude analisa e planeja
        ↓
Você confere o plano
        ↓
Claude implementa
        ↓
Codex revisa o resultado
        ↓
Claude corrige os problemas
        ↓
Codex executa a validação final
        ↓
Você autoriza o merge
```

Neste modelo:

- **Claude Code:** arquiteto e executor principal;
- **Codex:** revisor independente e testador;
- **GitHub:** registro oficial;
- **CI:** prova automática;
- **você:** aprova decisões e merges.

Claude Code pode ser usado com sua assinatura Max diretamente no terminal. O uso do Claude normal e do Claude Code compartilha os limites do plano, e você pode verificar o consumo com `/status`. [^3]

Codex está incluído no ChatGPT Plus e pode ser usado no terminal, IDE, aplicativo ou ambiente web; para este método, usaremos inicialmente o terminal ou a extensão da IDE. [^4]

---

## Fase 0 — Regras para não estragar os projetos

Durante o aprendizado, siga estas regras:

1. Claude e Codex nunca editam o mesmo repositório ao mesmo tempo.
2. Nunca trabalhe diretamente na branch `main`.
3. Nunca aceite mudanças sem ler o resumo.
4. Nunca use modo totalmente automático no início.
5. Nunca forneça senhas, tokens ou arquivos `.env`.
6. Cada tarefa possui um branch próprio.
7. Cada tarefa termina com testes e um relatório.
8. Codex revisa o trabalho de Claude; não refaz tudo.
9. Nenhum agente faz merge.
10. Você só avança quando o estado anterior estiver limpo.

A primeira meta não é construir o produto inteiro. É estabelecer uma **fábrica de desenvolvimento confiável**.

---

## Fase 1 — Preparar o computador

## 1\. Verifique as ferramentas básicas

Abra o terminal e execute:

```bash
git --version
node --version
npm --version
```

Resultados esperados:

```
git version ...
v20... ou superior
10... ou superior
```

Para os repositórios atuais, o mais seguro é trabalhar com Node 24 quando exigido pelo projeto, especialmente no Connect.

Também verifique:

```bash
docker --version
docker compose version
```

Não execute nenhum banco ou container ainda.

## 2\. Instale o Claude Code

O método documentado pela Anthropic é:

```bash
npm install -g @anthropic-ai/claude-code
```

Depois:

```bash
claude
```

Na autenticação, escolha sua conta Claude vinculada ao plano Max. A Anthropic recomenda executar `claude doctor` depois da instalação para validar o ambiente. [^5]

Execute:

```bash
claude doctor
```

Dentro do Claude Code, execute:

```
/status
```

Isso mostra modelo, conta e situação de uso.

No início, use **Sonnet** para leitura, planejamento e implementação comum. Use Opus apenas para arquitetura crítica, segurança e revisões difíceis. O modelo pode ser selecionado com `/model`. [^6]

## 3\. Instale o Codex CLI

Execute:

```bash
npm install -g @openai/codex
```

Depois:

```bash
codex
```

Faça login com sua conta ChatGPT quando solicitado. A documentação atual informa que o Codex CLI pode usar a autenticação do plano ChatGPT; instalações antigas configuradas com API key podem exigir logout e novo login. [^7]

## 4\. Confirme as instalações

Execute:

```bash
claude --version
codex --version
git --version
node --version
docker --version
```

Não prossiga enquanto algum desses comandos falhar.

---

## Fase 2 — Criar a pasta central

Crie uma pasta única para o ecossistema:

```bash
mkdir ginkgo-platform
cd ginkgo-platform
```

Clone os três repositórios:

```bash
git clone https://github.com/ginkgoai/ginkgo-tree.git
git clone https://github.com/ginkgoai/ginkgo-connect.git
git clone https://github.com/ginkgoai/ginkgo-workforce.git
```

A estrutura ficará assim:

```
ginkgo-platform/
├── ginkgo-tree/
├── ginkgo-connect/
└── ginkgo-workforce/
```

Não coloque um repositório dentro do outro.

## Confirme o estado

Em cada repositório:

```bash
cd ginkgo-tree
git status
git branch --show-current
git remote -v
cd ..
```

Repita para Connect e Workforce.

O resultado correto deve dizer algo equivalente a:

```
On branch main
nothing to commit, working tree clean
```

Se houver arquivos modificados, não comece a implementação até entender de onde vieram.

---

## Fase 3 — Nosso primeiro épico

O primeiro trabalho será:

> **E000 — Preparar os três repositórios para desenvolvimento guiado por Claude e Codex.**

E000 não adiciona funcionalidades comerciais. Ele cria:

- instruções para os agentes;
- constituição arquitetural;
- estrutura de especificações;
- comandos confiáveis;
- checklist de revisão;
- regras de segurança;
- padrão de PR;
- fronteiras entre Tree, Connect e Workforce.

## Ordem

Faremos nesta sequência:

```
E000-A — Ginkgo Tree
E000-B — Ginkgo Connect
E000-C — Ginkgo Workforce
```

Começaremos exclusivamente no **Ginkgo Tree**.

---

## Fase 4 — Criar o branch do Tree

Entre no repositório:

```bash
cd ginkgo-platform/ginkgo-tree
```

Atualize a referência da branch principal:

```bash
git checkout main
git pull --ff-only
```

Crie o branch:

```bash
git checkout -b chore/E000-agent-development-harness
```

Confirme:

```bash
git branch --show-current
git status
```

Resultado esperado:

```
chore/E000-agent-development-harness
nothing to commit, working tree clean
```

---

## Fase 5 — Claude apenas analisa

Abra Claude dentro do repositório:

```bash
claude
```

Não peça implementação ainda.

Copie este prompt:

Você é o arquiteto principal do ecossistema Ginkgo.

Estamos trabalhando exclusivamente no repositório ginkgo-tree.

Objetivo deste ciclo:  
Preparar o épico E000 — Development Harness, criando uma base segura para desenvolvimento posterior com Claude Code como implementador principal e Codex como revisor independente.

Neste momento, trabalhe somente em modo de análise. Não altere arquivos, não execute migrations, não instale dependências e não faça commits.

Primeiro:

1. Leia o README e os documentos arquiteturais.
2. Analise package.json, estrutura de packages, testes e workflows.
3. Verifique o estado atual do Git.
4. Identifique instruções existentes para agentes.
5. Identifique riscos de duplicação, documentação conflitante ou arquivos desatualizados.
6. Separe claramente o que pertence ao Ginkgo Tree, Connect e Workforce.
7. Proponha o conteúdo de:
	- CLAUDE.md
		- AGENTS.md
		- docs/AI-CONSTITUTION.md
		- docs/SECURITY-INVARIANTS.md
		- docs/DEVELOPMENT-WORKFLOW.md
		- specs/E000-development-harness/
8. Liste exatamente quais arquivos seriam criados ou alterados.
9. Liste os comandos que deverão validar o resultado.
10. Informe qualquer risco antes de propor implementação.

Regras arquiteturais:

- Ginkgo Tree governa tenancy, identidade, políticas, autonomia, orçamento, auditoria, evidências, segredos e Laplace.
- Connect conecta APIs, MCPs, ferramentas e canais.
- Workforce organiza funcionários de IA, cargos, equipes, tarefas e supervisão.
- Nenhum produto deve duplicar o kernel.
- Nenhuma credencial real pode ser lida ou registrada.
- Nenhuma mudança deve ser feita diretamente na main.
- Nenhum merge deve ser realizado por um agente.

Entregue um plano numerado e termine com:

STATUS: PLAN\_READY

Não implemente enquanto eu não autorizar.

## O que Claude deve fazer

Ele poderá:

- ler arquivos;
- executar `git status`;
- executar buscas;
- entender o repositório;
- apresentar plano.

Ele não deve:

- editar arquivos;
- instalar pacotes;
- executar Docker;
- fazer commit;
- criar PR.

## O que você confere no resultado

Não precisa entender todo o código. Verifique apenas:

- Claude respeitou o escopo?
- Ele não tentou implementar produto?
- Tree, Connect e Workforce foram separados?
- Há uma lista clara de arquivos?
- Há comandos de validação?
- Terminou com `STATUS: PLAN_READY`?

Caso ele comece a modificar arquivos, interrompa:

```
Pare. Reverta qualquer alteração feita nesta sessão e retorne somente ao planejamento.
```

---

## Fase 6 — Salvar o plano

Depois que o plano estiver correto, peça ao Claude:

```
Salve exatamente este plano em:

specs/E000-development-harness/plan.md

Não crie nenhum outro arquivo.
Depois execute git diff --check e git status.
Não faça commit.
```

Ao terminar, saia do Claude:

```
/exit
```

Confira manualmente:

```bash
git status
git diff --check
git diff
```

Você deverá ver apenas:

```
specs/E000-development-harness/plan.md
```

Essa é a primeira passagem formal:

```
Claude → plan.md → Codex
```

---

## Fase 7 — Codex revisa o plano

Ainda dentro do mesmo repositório, execute:

```bash
codex
```

Use inicialmente o modo mais supervisionado disponível. Não libere alterações automáticas.

Copie este prompt:

Atue como revisor independente do plano E000.

Não altere arquivos, não execute instalações, não faça commit e não implemente o plano.

Leia:

- README.md
- package.json
- docs/
- specs/E000-development-harness/plan.md
- workflows existentes
- estrutura atual do repositório

Revise o plano segundo estes critérios:

1. Está compatível com o código existente?
2. Algum arquivo proposto já existe ou conflita com documentação atual?
3. O plano preserva a separação entre Ginkgo Tree, Connect e Workforce?
4. Há risco de mudança fora do escopo?
5. Os comandos de validação realmente existem?
6. Faltam testes, lint, typecheck ou validações de segurança?
7. O plano poderia apagar, substituir ou contradizer decisões existentes?
8. Há qualquer risco de segredo, credencial ou dado operacional?
9. O plano é pequeno o suficiente para um único PR?
10. Quais correções são obrigatórias antes da implementação?

Classifique cada problema como:

- BLOCKER
- HIGH
- MEDIUM
- LOW

Não modifique o repositório.

Entregue somente a revisão e termine com:

REVIEW\_STATUS: APPROVED

ou

REVIEW\_STATUS: CHANGES\_REQUIRED

## Interpretação

### APPROVED

O plano pode voltar para Claude para implementação.

### CHANGES\_REQUIRED

Não peça ao Codex para corrigir o plano.

Copie os findings e entregue ao Claude:

```
O Codex revisou o plano e encontrou os seguintes problemas:

[cole os findings]

Atualize apenas:
specs/E000-development-harness/plan.md

Não implemente ainda.
Depois execute git diff --check.
```

Repita a revisão até o Codex emitir `APPROVED`.

---

## Fase 8 — Claude implementa o E000

Depois da aprovação do plano, abra novamente:

```bash
claude
```

Copie:

Implemente o plano aprovado em:

specs/E000-development-harness/plan.md

Escopo:  
Somente o épico E000 — Development Harness do ginkgo-tree.

Regras:

1. Leia novamente o plano antes de alterar arquivos.
2. Trabalhe apenas nos arquivos autorizados pelo plano.
3. Não implemente funcionalidades comerciais.
4. Não altere schemas, migrations ou contratos de runtime, salvo se o plano aprovado exigir explicitamente.
5. Não instale novas dependências sem necessidade documentada.
6. Não leia arquivos.env nem credenciais.
7. Não altere a licença.
8. Não faça merge.
9. Não faça push.
10. Não faça commit antes de concluir as validações.

Ao implementar:

- crie arquivos em passos pequenos;
- preserve documentação existente;
- execute os comandos de validação previstos;
- corrija erros causados por suas mudanças;
- não esconda testes falhando;
- não remova testes;
- não reduza regras de segurança.

No final, crie:

specs/E000-development-harness/implementation-report.md

O relatório deve conter:

- arquivos criados;
- arquivos alterados;
- decisões tomadas;
- comandos executados;
- resultados;
- problemas encontrados;
- riscos pendentes;
- qualquer desvio do plano.

Termine mostrando:

1. git status
2. git diff --stat
3. resultados das validações
4. lista de riscos restantes

Não faça commit.

---

## Fase 9 — Conferência humana básica

Quando Claude terminar, execute:

```bash
git status
git diff --stat
git diff --check
```

Depois, dependendo dos scripts existentes:

```bash
pnpm install --frozen-lockfile
pnpm lint
pnpm typecheck
pnpm test
pnpm build
```

Não execute todos cegamente. Consulte primeiro o `package.json`. No Ginkgo Tree atual existem scripts próprios para build, lint, typecheck, testes unitários e testes de integração; utilize exatamente os comandos declarados pelo repositório.

## Sinais de problema

Pare se acontecer:

- Claude alterou muitos arquivos de runtime;
- um lockfile mudou sem justificativa;
- arquivos `.env` apareceram;
- testes foram removidos;
- README inteiro foi substituído;
- uma licença foi modificada;
- mais de um produto foi alterado;
- migrations apareceram no E000;
- o diff ficou muito maior que o plano.

---

## Fase 10 — Codex revisa a implementação

Abra Codex:

```bash
codex
```

Peça:

```
Revise a implementação do E000.

Leia:

- specs/E000-development-harness/plan.md
- specs/E000-development-harness/implementation-report.md
- git diff
- arquivos alterados
- package.json
- workflows relevantes

Não altere arquivos nesta primeira revisão.

Procure:

1. divergências do plano;
2. documentação conflitante;
3. instruções inseguras para agentes;
4. permissões excessivas;
5. comandos inexistentes;
6. referências a arquivos inexistentes;
7. mudanças fora do escopo;
8. vazamento de segredo ou informação operacional;
9. violação da separação Tree/Connect/Workforce;
10. falta de validação.

Classifique findings como BLOCKER, HIGH, MEDIUM ou LOW.

Para cada finding, informe:

- arquivo;
- trecho;
- problema;
- impacto;
- correção esperada;
- validação necessária.

Não implemente correções.
```

---

## Fase 11 — Claude corrige

Entregue apenas os findings ao Claude:

```
Corrija exclusivamente os findings abaixo:

[cole os findings]

Não faça refactors adicionais.
Não altere arquivos fora do escopo do E000.
Adicione validação quando necessária.
Atualize implementation-report.md.
Execute novamente os comandos afetados.
Não faça commit.
```

Depois, Codex revisa novamente.

O ciclo termina apenas quando:

```
Nenhum BLOCKER
Nenhum HIGH
Nenhum MEDIUM injustificado
Lint aprovado
Typecheck aprovado
Testes aprovados
Build aprovado
git diff --check aprovado
```

---

## Fase 12 — Commit e PR

Quando tudo estiver validado:

```bash
git status
git diff --check
git add .
git commit -m "chore: establish agent development harness"
```

Confira:

```bash
git status
git log -1 --oneline
```

Envie o branch:

```bash
git push -u origin chore/E000-agent-development-harness
```

Abra um **draft PR**.

O PR deve informar:

```
Objetivo:
Preparar o Ginkgo Tree para desenvolvimento guiado por Claude e revisão por Codex.

Incluído:
- instruções dos agentes;
- constituição;
- invariantes de segurança;
- fluxo de desenvolvimento;
- estrutura de specs;
- relatório de implementação.

Não incluído:
- funcionalidades de produto;
- migrations;
- mudanças de runtime;
- deploy.

Validação:
- lint;
- typecheck;
- testes;
- build;
- diff check.

Revisão:
- plano revisado por Codex;
- implementação revisada por Codex;
- findings corrigidos por Claude.
```

Não faça merge imediatamente. Verifique primeiro o CI do GitHub.

---

## Fase 13 — Repetir em Connect e Workforce

Após o Tree:

## Connect

Branch:

```bash
chore/E000-agent-development-harness
```

O documento do Connect deve reforçar:

```
Connect conecta APIs, MCPs, ferramentas e canais.
Connect não governa agentes.
Connect não substitui o CRM.
Connect não armazena segredos diretamente.
Connect executa somente sob política do Tree.
```

## Workforce

O documento do Workforce deve reforçar:

```
Workforce gerencia funcionários, cargos, equipes e tarefas.
Workforce não implementa conectores.
Workforce não cria seu próprio kernel.
Workforce usa Connect para ferramentas e canais.
Workforce usa Tree para políticas e auditoria.
```

---

## O primeiro resultado esperado

Depois do E000 nos três repositórios, você ainda não terá funcionalidades novas. Terá algo mais importante:

```
Um processo repetível
+
responsabilidades claras
+
instruções persistentes
+
revisão independente
+
histórico no Git
+
gates de qualidade
```

Somente depois começaremos o **E001 — Contratos compartilhados do Ginkgo Tree**.

## Sua tarefa imediata

Execute somente esta sequência:

```bash
git --version
node --version
npm --version
docker --version
docker compose version
claude --version
codex --version
```

Em seguida:

```bash
mkdir ginkgo-platform
cd ginkgo-platform
git clone https://github.com/ginkgoai/ginkgo-tree.git
git clone https://github.com/ginkgoai/ginkgo-connect.git
git clone https://github.com/ginkgoai/ginkgo-workforce.git
```

Depois inicie apenas o planejamento E000 do Ginkgo Tree conforme o prompt acima. Não avance para implementação antes da revisão do plano pelo Codex.

---

**Você disse**

Antes, me dê um prompt descritivo de cada repositório, focado em ensinar um sócio comercial, sem muita tecnialidade.

---

Abaixo estão prompts individuais, prontos para copiar e colar. Eles foram escritos para ensinar um sócio comercial sobre produto, mercado, proposta de valor e relação entre os repositórios, evitando excesso de linguagem técnica.

## 1\. Ginkgo Tree

Explique o Ginkgo Tree para um sócio comercial que não possui formação técnica.

Apresente o Ginkgo Tree como o sistema central que governa todos os produtos e funcionários de inteligência artificial da Ginkgo.

Explique de forma simples:

- qual problema empresarial ele resolve;
- por que empresas não podem simplesmente liberar uma IA para agir sem limites;
- como ele controla permissões, autonomia, orçamento, memória, segurança e aprovação humana;
- como registra tudo que os agentes fizeram;
- como permite desligar, limitar ou supervisionar uma IA;
- por que ele é a infraestrutura invisível por trás dos demais produtos;
- como o Laplace funciona dentro dele como memória e base de conhecimento;
- por que o cliente normalmente não compra o Ginkgo Tree isoladamente;
- como ele aumenta a confiança comercial dos produtos Ginkgo.

Use exemplos cotidianos, como um funcionário que precisa pedir autorização antes de gastar dinheiro, enviar uma proposta ou alterar informações importantes.

Finalize com:

1. proposta de valor em uma frase;
2. cliente ideal;
3. principais benefícios comerciais;
4. riscos que ele reduz;
5. como explicá-lo em uma reunião de vendas;
6. um pitch de 30 segundos.

Evite linguagem de programação, arquitetura de software e termos técnicos desnecessários.

---

## 2\. Ginkgo Connect

Explique o Ginkgo Connect para um sócio comercial sem formação técnica.

Apresente o Connect como a ponte que permite que qualquer inteligência artificial se conecte a ferramentas, canais de comunicação e sistemas empresariais.

Explique de forma simples:

- como ele conecta IAs a WhatsApp, Telegram, Instagram, Facebook, e-mail, web chat e outros canais;
- como conecta também Gmail, Google Calendar, Drive, CRMs, ERPs, bancos de dados, APIs e ferramentas internas;
- como o usuário descreve o que deseja fazer e o Connect identifica a conexão necessária;
- como ele testa se a conexão realmente funciona;
- como diferencia operações de leitura e operações que alteram informações;
- como ações sensíveis podem exigir aprovação;
- como ele evita que cada produto da Ginkgo precise desenvolver todas as integrações novamente;
- como ele funciona junto com Ginkgo Tree e Workforce;
- por que ele pode ser vendido como infraestrutura de conectividade ou fazer parte de outros produtos.

Use exemplos como:

- conectar um funcionário de IA ao Gmail;
- permitir que uma IA consulte a agenda;
- receber clientes pelo WhatsApp;
- publicar ou responder mensagens em redes sociais;
- consultar dados de um sistema existente.

Finalize com:

1. proposta de valor em uma frase;
2. cliente ideal;
3. principais casos de uso;
4. diferenciais comerciais;
5. modelo de oferta;
6. pitch de 30 segundos.

Evite aprofundamento em APIs, protocolos ou programação.

---

## 3\. Ginkgo Workforce

Explique o Ginkgo Workforce para um sócio comercial sem formação técnica.

Apresente o Workforce como uma plataforma para criar, contratar, organizar e supervisionar funcionários de inteligência artificial.

Explique de forma simples:

- o que é um funcionário de IA;
- como cada funcionário pode ter nome, cargo, responsabilidades, personalidade e limites;
- como uma empresa pode montar uma equipe de agentes;
- como tarefas são delegadas e acompanhadas;
- como o proprietário conversa com esses funcionários pelo painel, WhatsApp, Telegram ou web;
- como os agentes podem atender clientes ou executar trabalhos internos;
- como o Workforce mostra tarefas, aprovações, custos, resultados e histórico;
- como o Connect fornece as ferramentas e canais;
- como o Ginkgo Tree controla segurança, autonomia e orçamento;
- como o Laplace fornece memória e conhecimento.

Use exemplos de funcionários como:

- assistente administrativo;
- secretária;
- atendente;
- coordenador;
- pesquisador;
- analista de conteúdo;
- operador de vendas.

Explique também por que o produto deve começar com poucos cargos bem definidos, em vez de prometer uma empresa totalmente autônoma.

Finalize com:

1. proposta de valor em uma frase;
2. cliente ideal;
3. primeiros cargos comercializáveis;
4. formato de cobrança;
5. benefícios para pequenas e médias empresas;
6. pitch de 30 segundos.

---

## 4\. Ginkgo Leaf

Explique o Ginkgo Leaf para um sócio comercial sem formação técnica.

Apresente o Leaf como um CRM com inteligência artificial, criado para organizar clientes, leads, oportunidades, conversas e vendas.

Explique de forma simples:

- o que é um CRM;
- por que empresas perdem vendas quando contatos ficam espalhados;
- como o Leaf centraliza clientes, histórico, conversas, agenda e pipeline;
- como agentes de IA podem atender, qualificar, organizar e acompanhar leads;
- como o sistema pode receber contatos por WhatsApp, Instagram, web e outros canais;
- como diferencia atendimento automático e atendimento humano;
- como cria lembretes e follow-ups;
- como pode ajudar clínicas, imobiliárias, escritórios, prestadores de serviços e comércio;
- como o Connect fornece os canais;
- como o Tree controla as ações dos agentes;
- como o Workforce pode fornecer funcionários de IA especializados.

Deixe claro que o Leaf não é apenas um chatbot. Ele é o sistema onde a empresa acompanha todo o relacionamento comercial.

Finalize com:

1. proposta de valor em uma frase;
2. público ideal;
3. principais dores resolvidas;
4. módulos que podem ser vendidos;
5. possibilidades de upsell;
6. pitch de 30 segundos.

---

## 5\. Ginkgo Pyre

Explique o Ginkgo Pyre para um sócio comercial sem formação técnica.

Apresente o Pyre como um estúdio multimodal de criação com inteligência artificial.

Explique de forma simples:

- o que significa criação multimodal;
- como o usuário pode produzir texto, imagens, vídeos, áudio, roteiros e cenas no mesmo ambiente;
- como ele pode organizar projetos criativos;
- como ajuda a criar campanhas, personagens, anúncios, vídeos e conteúdos;
- como mantém consistência visual e narrativa;
- como pode trabalhar com roteiros, storyboard, cenas, versões e arquivos;
- como se diferencia de um simples gerador de imagem;
- como publicação em redes sociais pode existir como etapa posterior, mas não é o produto inteiro;
- como pode atender agências, criadores, empresas, produtoras e equipes de marketing;
- como Ginkgo Tree controla custos, acesso e geração;
- como Connect pode integrar ferramentas e destinos de publicação.

Use exemplos como:

- criar uma campanha completa;
- desenvolver um personagem virtual;
- montar um vídeo publicitário;
- produzir variações de criativos;
- criar uma sequência de cenas.

Finalize com:

1. proposta de valor em uma frase;
2. cliente ideal;
3. principais entregas;
4. diferenciais;
5. possíveis planos comerciais;
6. pitch de 30 segundos.

---

## 6\. Ginkgo Wave

Explique o Ginkgo Wave para um sócio comercial sem formação técnica.

Apresente o Wave como um painel simplificado para criação, acompanhamento e gestão de anúncios com assistência de inteligência artificial.

Explique de forma simples:

- por que pequenos negócios têm dificuldade para entender plataformas de anúncios;
- como o Wave reúne dados de Meta, Google, TikTok e outras plataformas;
- como apresenta métricas de forma simples;
- como ajuda a criar campanhas;
- como identifica anúncios fracos, custos altos e possíveis oportunidades;
- como sugere ajustes de orçamento;
- como alerta sobre fadiga de criativos;
- como diferencia sugestão, aprovação e execução;
- por que a IA não deve gastar dinheiro livremente;
- como o Connect realiza as integrações;
- como o Tree controla orçamento, aprovação e ações sensíveis.

Use exemplos como:

- campanha com custo por lead alto;
- anúncio que parou de funcionar;
- sugestão de novo criativo;
- redistribuição de orçamento;
- relatório automático para o cliente.

Finalize com:

1. proposta de valor em uma frase;
2. cliente ideal;
3. principais benefícios;
4. riscos que o produto reduz;
5. formato de comercialização;
6. pitch de 30 segundos.

---

## 7\. Ginkgo Aegis

Explique o Ginkgo Aegis para um sócio comercial sem formação técnica.

Apresente o Aegis como uma solução de segurança que utiliza inteligência artificial para verificar falhas, riscos e vulnerabilidades em ambientes autorizados.

Explique de forma simples:

- o que é um AI Red Team;
- por que empresas precisam testar a própria segurança;
- como o Aegis trabalha somente com autorização;
- como identifica possíveis falhas;
- como organiza evidências e relatórios;
- como diferencia simulação, validação e ação real;
- como evita atividades destrutivas;
- como mantém aprovação humana;
- por que ele não deve ser apresentado como um “hacker autônomo”;
- como pode ser oferecido como serviço recorrente de validação;
- como Ginkgo Tree controla escopo, autorização e auditoria.

Use exemplos como:

- verificar uma aplicação antes do lançamento;
- revisar exposição de serviços;
- validar configurações;
- produzir relatório de risco;
- acompanhar correções.

Finalize com:

1. proposta de valor em uma frase;
2. cliente ideal;
3. limites éticos e comerciais;
4. formato de serviço;
5. diferenciais;
6. pitch de 30 segundos.

---

## 8\. Ginkgo Lexra

Explique o Ginkgo Lexra para um sócio comercial sem formação técnica.

Apresente o Lexra como uma funcionária de inteligência artificial oferecida como serviço para escritórios de advocacia.

Explique de forma simples:

- como ela ajuda a organizar clientes, processos, documentos e tarefas;
- como pode receber informações iniciais;
- como acompanha eventos autorizados;
- como transforma informações técnicas em resumos;
- como cria pendências e lembretes;
- como solicita documentos;
- como auxilia na comunicação com clientes;
- como ajuda na agenda e no acompanhamento;
- como pode assumir diferentes cargos operacionais;
- por que decisões jurídicas e responsabilidade profissional permanecem humanas;
- como o Workforce organiza a funcionária;
- como Connect conecta sistemas e canais;
- como Tree controla acesso, segurança e auditoria;
- como Laplace fornece a base de conhecimento.

Apresente possíveis ofertas:

- recepcionista jurídica;
- assistente de processos;
- assistente de operações;
- persona personalizada.

Finalize com:

1. proposta de valor em uma frase;
2. cliente ideal;
3. atividades que ela pode executar;
4. atividades que permanecem humanas;
5. modelo comercial;
6. pitch de 30 segundos.

---

## 9\. Ginkgo Commerce OS

Explique o Ginkgo Commerce OS para um sócio comercial sem formação técnica.

Apresente o Commerce OS como um sistema completo para criar, operar e otimizar negócios de comércio eletrônico com inteligência artificial.

Explique de forma simples:

- como ele pode ajudar a pesquisar produtos;
- como compara preços, avaliações, margem, prazo e disponibilidade;
- como organiza fornecedores;
- como cria catálogo e descrições;
- como ajuda em preço, estoque e pedidos;
- como pode integrar marketplaces e lojas próprias;
- como auxilia atendimento e pós-venda;
- como acompanha métricas;
- como pode apoiar operações de social commerce;
- como utiliza fontes autorizadas, APIs e programas de afiliados;
- por que não deve depender de práticas que burlem bloqueios ou regras de plataformas;
- como Connect realiza integrações;
- como Tree controla ações, custos e permissões;
- como Leaf pode organizar relacionamento com clientes.

Use exemplos como:

- comparar um produto entre marketplaces;
- identificar oportunidade de margem;
- cadastrar produtos;
- gerar descrição e anúncio;
- atualizar estoque;
- acompanhar pedidos.

Finalize com:

1. proposta de valor em uma frase;
2. cliente ideal;
3. principais módulos;
4. possibilidades de receita;
5. riscos operacionais;
6. pitch de 30 segundos.

---

## 10\. Ginkgo AI Stack

Explique o Ginkgo AI Stack para um sócio comercial sem formação técnica.

Apresente o AI Stack como o laboratório aberto da Ginkgo para testar, estudar e criar tecnologias de inteligência artificial.

Explique de forma simples:

- por que uma empresa de IA precisa de um laboratório;
- como ele reúne ferramentas abertas para agentes, automações, memória, comunicação e criação de protótipos;
- como permite testar ideias antes de colocá-las nos produtos comerciais;
- como ajuda a comunidade e desenvolvedores;
- como pode atrair colaboradores;
- como demonstra capacidade técnica;
- como pode gerar componentes que posteriormente são reconstruídos ou incorporados aos produtos;
- por que ele não é a versão gratuita do Ginkgo Tree;
- por que não deve conter dados de clientes, segredos ou código proprietário;
- por que o AI Stack não é necessariamente vendido como SaaS.

Use uma analogia simples: o AI Stack é o laboratório e a oficina; os produtos comerciais são os veículos prontos para o cliente.

Finalize com:

1. função estratégica em uma frase;
2. público principal;
3. benefícios para a marca;
4. benefícios para desenvolvimento;
5. limites entre laboratório e produtos;
6. pitch de 30 segundos.

---

## 11\. Visão completa do ecossistema

Explique todo o ecossistema Ginkgo para um sócio comercial sem formação técnica.

Use esta divisão:

- Ginkgo Tree governa e controla.
- Laplace fornece memória e conhecimento dentro do Tree.
- Connect conecta ferramentas, sistemas e canais.
- Workforce organiza os funcionários de IA.
- Leaf organiza clientes e vendas.
- Pyre produz conteúdo multimodal.
- Wave gerencia anúncios.
- Aegis verifica segurança.
- Lexra atende operações jurídicas.
- Commerce OS opera comércio eletrônico.
- AI Stack é o laboratório aberto.

Apresente o ecossistema como uma empresa de infraestrutura e produtos de inteligência operacional, e não como um conjunto desconectado de aplicativos.

Explique:

- o papel de cada produto;
- como eles trabalham juntos;
- quais produtos o cliente enxerga;
- quais componentes ficam nos bastidores;
- como um cliente pode começar com um produto e adicionar outros;
- como ocorre cross-sell;
- como evitar confusão comercial;
- como vender resultados e funcionários, e não apenas tecnologia.

Inclua três exemplos completos:

1. uma clínica;
2. um escritório de advocacia;
3. uma empresa de comércio eletrônico.

Para cada exemplo, mostre quais produtos seriam utilizados e qual resultado comercial seria entregue.

Finalize com:

1. posicionamento da Ginkgo;
2. proposta de valor central;
3. mapa simples do ecossistema;
4. modelo de entrada;
5. possibilidades de expansão;
6. pitch institucional de 60 segundos.

O prompt mais importante para iniciar o treinamento comercial é o último, porque apresenta primeiro a visão completa e depois permite aprofundar cada produto individualmente.

[^1]: [docs.anthropic.com](https://docs.anthropic.com/pt/docs/claude-code/sdk?utm_source=chatgpt.com)

[^2]: [support.anthropic.com](https://support.anthropic.com/en/articles/11145838-using-claude-code-with-your-max-plan?utm_source=chatgpt.com)

[^3]: [support.anthropic.com](https://support.anthropic.com/pt/articles/11145838-usando-o-claude-code-com-seu-plano-max?utm_source=chatgpt.com)

[^4]: [help.openai.com](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan%28.pdf?utm_source=chatgpt.com)

[^5]: [docs.anthropic.com](https://docs.anthropic.com/en/docs/claude-code/getting-started?utm_source=chatgpt.com)

[^6]: [support.anthropic.com](https://support.anthropic.com/en/articles/11940350-claude-code-model-configuration?utm_source=chatgpt.com)

[^7]: [help.openai.com](https://help.openai.com/en/articles/11096431?utm_source=chatgpt.com)