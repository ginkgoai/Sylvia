---
title: "Ginkgo Core"
source: "https://chatgpt.com/g/g-p-68e0a0b393cc8191a0f44ad743e1117d/c/6a68252f-3b88-83e9-a0e1-780c28aed01c"
author:
published:
created: 2026-08-02
description: "Use o ChatGPT para responder a perguntas, escrever, criar imagens, realizar tarefas e programar — tudo em um só lugar. Comece gratuitamente ou baixe o aplicativo."
tags:
  - "clippings"
---
Correto. **Hermes e OpenClaw não são necessários na arquitetura principal do Ginkgo Workforce.**

## Arquitetura definitiva

```markdown
Callima e Eliza
        ↓
Runtime próprio Ginkgo
├── Fastify API
├── BullMQ Workers
├── Task/Skill Engine
├── Model Router
├── Approval Engine
├── Policy Engine
└── Audit/Evidence
        ↓
Serviços
├── n8n
├── Nango
├── PostgreSQL + pgvector
├── Redis
├── Evolution / Meta Cloud API
├── Stripe
└── provedores LLM, STT e TTS
```

### O runtime próprio já cobre

- contexto e memória;
- chamadas aos modelos;
- escolha de ferramentas;
- execução de skills;
- permissões;
- limites de autonomia;
- aprovações;
- filas e retries;
- RAG;
- registros e evidências;
- consumo de créditos;
- coordenação entre Callima e Eliza.

Adicionar Hermes ou OpenClaw criaria outra camada entre o produto e essas funções.

## Hermes

O Hermes existente era essencialmente um backend/agente intermediário. Na própria `ai-stack`, o serviço FastAPI antigo já foi registrado como aposentado e não é mais construído.

Manter Hermes causaria duplicação de:

- roteamento de modelos;
- prompts;
- memória;
- ferramentas;
- autenticação;
- logs;
- tratamento de falhas;
- configuração por organização.

O papel que ele exerceria será assumido diretamente pelo:

```markdown
apps/api
apps/worker
packages/core
packages/callima
packages/eliza
packages/integrations
```

Portanto:

> **Hermes não entra no produto novo.**

## OpenClaw

OpenClaw é mais adequado para um agente geral com acesso ao computador, terminal, arquivos e aplicações locais.

Esse tipo de autonomia não é necessário para Callima e Eliza no MVP e aumenta:

- superfície de ataque;
- dificuldade de isolamento por cliente;
- risco de execução arbitrária;
- consumo de recursos;
- complexidade de deploy;
- dificuldade de auditoria;
- comportamento não determinístico.

Callima e Eliza não precisam “controlar um computador”. Elas precisam executar capacidades bem definidas:

```markdown
consultar CRM
criar contato
agendar reunião
enviar mensagem
consultar conhecimento
gerar documento
solicitar aprovação
```

Cada uma dessas funções deve existir como **skill tipada, autorizada e auditável**, não como liberdade geral de máquina.

Portanto:

> **OpenClaw também não entra na arquitetura de produção.**

## Onde poderiam ser usados

Podem continuar fora do produto, em ambientes separados.

## OpenClaw opcionalmente

- operações internas da Ginkgo;
- automação do computador do fundador;
- testes de computer use;
- manutenção assistida;
- protótipos de agente pessoal.

## Hermes opcionalmente

Não há uma função clara que justifique mantê-lo. O código útil pode ser reaproveitado diretamente, mas o serviço em si deve ser aposentado.

## Regra arquitetural

```markdown
LLM decide dentro de limites
Código valida
Skill executa
Sistema confirma
Eliza explica
```

Não:

```markdown
Eliza
→ framework de agente
→ outro framework
→ n8n
→ API
→ resultado incerto
```

Quanto menos camadas cognitivas intermediárias, melhores serão:

- latência;
- previsibilidade;
- segurança;
- rastreabilidade;
- manutenção;
- custo;
- experiência do usuário.

## Stack enxuta final

```markdown
Frontend
Next.js

Backend
Fastify + TypeScript

Orquestração determinística
BullMQ + Redis

Automações
n8n

Dados
PostgreSQL + pgvector

Conexões
Nango

WhatsApp
Evolution inicialmente
Meta Cloud API oficialmente

IA
Model Router próprio

Conhecimento
RAG nativo

Voz
Groq/OpenAI STT + ElevenLabs/OpenAI TTS

Cobrança
Stripe
```

**Conclusão:** Hermes e OpenClaw ficam fora. O Ginkgo Workforce terá runtime próprio, menor, controlável e construído especificamente para Callima e Eliza.

Okay, perfeito. Qual o próximo passo ideal, vizando utilizar os tokens restante do Codex e depois passar para Fable quando acabar.

## Próximo passo ideal

**Usar os tokens restantes do Codex para entregar uma vertical funcional do RAG nativo, conectada à Callima existente em modo de comparação.**

Não começaria agora:

- Eliza completa;
- Nango;
- billing;
- refinamento visual do dashboard;
- Meta Cloud API;
- múltiplos agentes.

Essas frentes dependem da qualidade do núcleo cognitivo. O RAG é o componente de maior impacto sobre respostas, decisões, contexto e confiança.

A ordem correta é:

```markdown
Callima atual funcionando
        ↓
Congelar comportamento e criar testes
        ↓
Construir RAG nativo
        ↓
Executar em shadow mode
        ↓
Comparar com AnythingLLM
        ↓
Superar a referência atual
        ↓
Migrar a Callima
        ↓
Construir onboarding, Eliza e Nango
```

## Como usar os tokens restantes do Codex

## 70% — Implementação do RAG vertical

O Codex deve construir uma única linha completa:

```markdown
Upload
→ Storage
→ Extração
→ Chunking
→ Embedding
→ pgvector + FTS
→ Busca híbrida
→ Reranking
→ Contexto
→ Resposta com citações
```

É melhor concluir uma vertical utilizável do que iniciar cinco módulos incompletos.

## 20% — Testes e comparação

- conjunto dourado;
- testes de isolamento;
- benchmark contra AnythingLLM;
- testes de idioma;
- recuperação de códigos, preços e produtos;
- citações;
- respostas sem evidência;
- CI.

## 10% — Preparação para o Fable

O último trabalho do Codex deve ser criar um pacote de continuidade:

```markdown
AGENTS.md
docs/CURRENT_STATE.md
docs/DECISIONS.md
docs/RAG_ARCHITECTURE.md
docs/RAG_EVALUATION.md
docs/HANDOFF_FABLE.md
docs/RUNBOOK_LOCAL.md
```

O Codex possui suporte a `AGENTS.md`, e o comando `/init` pode gerar uma estrutura inicial para orientar o agente dentro do projeto. [OpenAI Help Center](https://help.openai.com/pt-br/articles/11369540-como-usar-o-codex-com-seu-plano-do-chatgpt?utm_source=chatgpt.com)

## Sprint Codex recomendada

## Etapa 1 — Congelar a Callima atual

Antes de alterar qualquer coisa, registrar a versão funcional.

### Exportar da ai-stack

- workflow principal ativo;
- subworkflows acionados;
- prompts;
- ferramentas;
- contratos dos webhooks;
- estruturas de entrada e saída;
- configurações de memória;
- modelo usado;
- formato retornado pelo AnythingLLM;
- agendamento;
- envio de texto;
- envio de imagem;
- recebimento e envio de áudio.

Não copiar:

- tokens;
- chaves;
- credenciais;
- IDs privados;
- dados reais de clientes.

### Criar fixtures anônimas

```markdown
fixtures/
├── conversations/
│   ├── basic-text.json
│   ├── contextual-follow-up.json
│   ├── audio-request.json
│   ├── image-request.json
│   └── appointment-request.json
│
├── knowledge/
│   ├── catalog.md
│   ├── faq.md
│   ├── pricing.csv
│   └── policies.md
│
└── expected/
    ├── retrieval.json
    └── decisions.json
```

O objetivo é transformar “já testei e funciona” em uma referência repetível.

---

## Etapa 2 — Criar packages/knowledge

Responsabilidades:

```markdown
packages/knowledge/
├── contracts/
├── ingestion/
├── extraction/
├── chunking/
├── embeddings/
├── retrieval/
├── reranking/
├── context-builder/
├── citations/
└── evaluation/
```

Não deve gerar a resposta final. Ele apenas entrega evidências de qualidade para Callima ou Eliza.

Contrato principal:

```markdown
export interface KnowledgeService {
  ingest(input: IngestKnowledgeInput): Promise<IngestionResult>;

  retrieve(input: RetrieveKnowledgeInput): Promise<KnowledgeContext>;

  remove(input: RemoveKnowledgeInput): Promise<void>;

  evaluate(input: EvaluationInput): Promise<EvaluationResult>;
}
```

---

## Etapa 3 — Construir o banco

Adicionar:

```markdown
knowledge_documents
knowledge_document_versions
knowledge_chunks
knowledge_ingestion_jobs
knowledge_queries
knowledge_retrieval_results
knowledge_feedback
knowledge_eval_cases
knowledge_eval_runs
```

Obrigatório em todas as entidades:

```markdown
org_id
created_at
updated_at
```

Nos chunks:

```markdown
content
embedding
search_vector
locale
document_type
title
section
page
valid_from
valid_until
priority
permissions
checksum
version
status
```

---

## Etapa 4 — Knowledge Worker

Criar:

```markdown
apps/knowledge-worker
```

Responsável por:

1. receber um job;
2. buscar o arquivo;
3. extrair conteúdo;
4. estruturar o documento;
5. escolher a estratégia de chunking;
6. gerar metadados;
7. criar embeddings;
8. construir o `tsvector`;
9. persistir os chunks;
10. executar consultas de validação;
11. publicar a versão.

A ingestão não deve acontecer dentro de uma requisição HTTP longa.

---

## Etapa 5 — Retrieval V1

Implementar nesta ordem:

### Busca vetorial

Recupera similaridade semântica.

### Busca lexical

Recupera:

- nomes;
- códigos;
- SKUs;
- números;
- termos exatos;
- nomes próprios;
- cláusulas.

### Fusão

Usar Reciprocal Rank Fusion.

### Reranking

Reordenar os candidatos com um reranker multilíngue.

### Context Builder

- remover duplicados;
- priorizar fontes vigentes;
- limitar conteúdo repetido;
- diversificar documentos;
- respeitar orçamento;
- incluir citações;
- sinalizar conflitos.

---

## Etapa 6 — Shadow mode

Não cortar o AnythingLLM imediatamente.

Adicionar um modo temporário:

```markdown
KNOWLEDGE_MODE=legacy
KNOWLEDGE_MODE=shadow
KNOWLEDGE_MODE=native
```

### legacy

A Callima usa apenas o sistema atual.

### shadow

A resposta ao cliente continua usando o sistema atual, mas a consulta também passa pelo RAG nativo.

Registrar:

```markdown
Pergunta
Resultados AnythingLLM
Resultados pgvector
Posições dos documentos corretos
Latência
Chunks irrelevantes
Citações
Resposta potencial
```

### native

A Callima utiliza o RAG próprio.

O código do adaptador legado deve ficar em:

```markdown
tools/migration/anythingllm-benchmark
```

Não em `packages/knowledge`.

---

## Critério para migrar

O novo sistema não deve ser ativado apenas porque “está pronto”.

## Retrieval

- recupera os documentos corretos;
- localiza informações exatas;
- respeita validade;
- não cruza organizações;
- funciona em português e inglês;
- melhora a posição do conteúdo relevante;
- reduz chunks irrelevantes.

## Resposta

- não inventa;
- utiliza a fonte correta;
- responde de forma mais limpa;
- cita o documento;
- distingue ausência de informação;
- resolve conflitos;
- mantém contexto.

## Produto

- texto continua funcionando;
- áudio continua funcionando;
- imagem continua funcionando;
- agenda continua funcionando;
- latência permanece aceitável;
- consumo é registrado;
- falhas possuem fallback.

## Onde o Codex termina

O Codex deve concluir com:

```markdown
✓ banco e migrations
✓ Knowledge Worker
✓ ingestão de Markdown, PDF e CSV
✓ embeddings
✓ busca vetorial
✓ busca textual
✓ RRF
✓ reranking
✓ Context Builder
✓ citações
✓ API de retrieval
✓ golden dataset
✓ shadow comparator
✓ testes multi-tenant
✓ CI verde
✓ documentação
```

Não pedir ao Codex para “construir o produto inteiro”. Como o uso do Codex passou a ser contabilizado com base no consumo, tarefas delimitadas, verificáveis e orientadas por testes utilizam melhor o orçamento disponível. [OpenAI Help Center+1](https://help.openai.com/en/articles/20001106?utm_source=chatgpt.com)

## Onde o Fable entra

Depois que a vertical estiver funcional, o Fable recebe o repositório e assume trabalhos mais longos:

1. auditoria integral do RAG;
2. análise de arquitetura;
3. revisão da qualidade do chunking;
4. otimização do retrieval;
5. avaliação das respostas;
6. integração definitiva com Callima;
7. desenho cognitivo da Eliza;
8. onboarding conversacional;
9. revisão completa da experiência;
10. coordenação dos próximos épicos.

A Anthropic posiciona o Fable 5 para trabalhos ambiciosos e projetos de agentes de longo horizonte, incluindo planejamento em múltiplos estágios e verificação do próprio trabalho. [Anthropic](https://www.anthropic.com/claude/fable?utm_source=chatgpt.com)

Portanto, a divisão ideal é:

```markdown
Codex
→ construir a fundação concreta e testada

Fable
→ auditar, integrar, evoluir e conduzir os ciclos longos
```

## Prompt inicial para o Codex

Você está trabalhando no repositório privado `ginkgoai/ginkgo-workforce`.

## Missão

Implementar a primeira vertical funcional do Knowledge Engine nativo do Ginkgo Workforce usando PostgreSQL + pgvector, busca textual, busca híbrida, reranking e avaliações próprias.

Este trabalho substitui o AnythingLLM na arquitetura-alvo, mas não deve quebrar nem modificar prematuramente a Callima funcional que atualmente roda na `ai-stack`.

A Callima existente é a referência de comportamento. O novo RAG deve ser comparado contra ela em shadow mode antes do corte.

## Princípios obrigatórios

1. Não construir o produto inteiro.
2. Trabalhar exclusivamente no núcleo de conhecimento e na comparação com o sistema atual.
3. Não copiar segredos, tokens, dados reais ou IDs privados.
4. Não adicionar Hermes ou OpenClaw.
5. Não colocar lógica de produto no n8n.
6. O PostgreSQL é a fonte de verdade.
7. Todo dado de negócio deve possuir `org_id`.
8. Nenhuma consulta vetorial pode acontecer sem escopo de organização.
9. Respostas sem evidência suficiente devem falhar honestamente.
10. Toda alteração deve ter testes e documentação.
11. Não remover AnythingLLM da `ai-stack` antes da validação de paridade.
12. O adaptador legado deve existir apenas em `tools/migration`, nunca como dependência permanente do runtime.

## Primeira ação

Antes de editar código:

1. leia `README.md`;
2. leia `CLAUDE.md`;
3. leia toda a pasta `docs`;
4. leia o schema Prisma;
5. leia os packages atuais;
6. leia as issues relacionadas a Callima e RAG;
7. produza um plano de implementação;
8. identifique conflitos entre documentação e código;
9. não faça alterações até concluir o diagnóstico.

## Entregáveis

### 1\. Contratos

Criar `packages/knowledge` com contratos tipados para:

- documentos;
- versões;
- chunks;
- ingestão;
- retrieval;
- citações;
- feedback;
- avaliações;
- contexto retornado aos agentes.

### 2\. Banco

Adicionar modelos e migrations para:

- `knowledge_documents`;
- `knowledge_document_versions`;
- `knowledge_chunks`;
- `knowledge_ingestion_jobs`;
- `knowledge_queries`;
- `knowledge_retrieval_results`;
- `knowledge_feedback`;
- `knowledge_eval_cases`;
- `knowledge_eval_runs`.

Ativar:

- extensão `vector`;
- full-text search;
- índices adequados;
- isolamento por organização;
- versionamento;
- soft delete quando necessário.

### 3\. Worker

Criar `apps/knowledge-worker` com BullMQ para:

- extração;
- limpeza;
- chunking;
- embeddings;
- indexação;
- reindexação;
- exclusão;
- validação posterior à ingestão.

### 4\. Ingestão inicial

Suportar:

- Markdown;
- texto;
- PDF;
- CSV.

Preservar:

- títulos;
- seções;
- páginas;
- linhas;
- produtos;
- preços;
- códigos;
- tabelas;
- origem;
- checksum.

### 5\. Chunking

Criar estratégias distintas para:

- FAQ;
- catálogo;
- documento longo;
- política;
- CSV;
- texto livre.

Não utilizar um único tamanho fixo para todos os documentos.

### 6\. Retrieval

Implementar:

- busca vetorial;
- PostgreSQL full-text search;
- filtros obrigatórios;
- RRF;
- reranking multilíngue;
- deduplicação;
- diversidade de fontes;
- prioridade por vigência;
- Context Builder;
- citações rastreáveis.

### 7\. API

Criar endpoints internos para:

- upload;
- ingestão;
- status;
- consulta;
- remoção;
- reindexação;
- feedback;
- execução de avaliações.

### 8\. Shadow mode

Criar ferramenta de migração que compare:

- AnythingLLM atual;
- Knowledge Engine nativo.

Modos temporários:

- `legacy`;
- `shadow`;
- `native`.

O adaptador do AnythingLLM deve ficar em:

`tools/migration/anythingllm-benchmark`

### 9\. Avaliações

Criar conjunto dourado com casos em pt-BR e en-US:

- pergunta direta;
- sinônimo;
- código exato;
- preço;
- produto;
- política;
- informação ausente;
- informação desatualizada;
- conflito entre fontes;
- tentativa de acessar dados de outra organização.

Medir:

- Recall@K;
- MRR;
- nDCG;
- precisão de citações;
- groundedness;
- latência;
- taxa de resposta sem evidência.

### 10\. Documentação

Criar ou atualizar:

- `AGENTS.md`;
- `docs/CURRENT_STATE.md`;
- `docs/DECISIONS.md`;
- `docs/RAG_ARCHITECTURE.md`;
- `docs/RAG_EVALUATION.md`;
- `docs/RUNBOOK_LOCAL.md`;
- `docs/HANDOFF_FABLE.md`.

## Critérios de aceite

- Prisma Generate passa.
- TypeScript passa.
- Build passa.
- Testes passam.
- Docker Compose é válido.
- Uma organização não recupera chunks de outra.
- Documentos podem ser versionados e removidos.
- Busca vetorial e lexical funcionam.
- RRF e reranking estão ativos.
- Respostas possuem citações.
- Informação ausente não é inventada.
- O shadow mode produz comparação auditável.
- A Callima funcional não sofre regressão.
- A documentação permite que outro agente continue o trabalho sem depender do histórico desta conversa.

## Estratégia de commits

Faça commits pequenos e semânticos:

1. contratos;
2. schema e migrations;
3. worker;
4. ingestão;
5. retrieval;
6. reranking;
7. API;
8. avaliações;
9. shadow mode;
10. documentação.

Ao final, apresente:

- arquivos alterados;
- decisões tomadas;
- testes executados;
- resultados;
- limitações;
- riscos;
- próxima ação recomendada.

Esse prompt usa o Codex onde ele gera mais valor agora: implementação concreta, validação automática e preparação de uma transição sem perda de contexto.

quinta-feira 20:03

deep-research-report.md

Arquivo

deep-research-report (3).md

Arquivo

deep-research-report (2).md

Arquivo

deep-research-report (1).md

Arquivo

Documentação LangChain.md

Arquivo

GitHub ginkgo-workforce vamos iniciar a construção no claude code prompt a prompt

## Ponto de partida

O repositório possui duas linhas paralelas:

- **PR #1 / `bootstrap/workforce-foundation`**: base executável com Fastify, Next.js, BullMQ, Prisma, PostgreSQL/pgvector, Redis, n8n e Evolution. É a branch correta para iniciar código.
- **PR #10 / `agent/refine-workforce-architecture`**: documentação e contratos mais completos, mas reintroduz Hermes e amplia o escopo para serviços que já decidimos não usar.

O schema existente já fornece organizações, assistentes, skills, tarefas, aprovações, ledger e isolamento por `org_id`, mas o conhecimento ainda está reduzido a uma única tabela `KnowledgeSource`.

A arquitetura de pesquisa sustenta PostgreSQL + pgvector, Redis, object storage, worker de ingestão, retrieval híbrido e Laplace como Evidence Kernel. O material histórico também possui contratos úteis de personas, memória, Agent Package e respostas independentes do canal, que devem ser aproveitados seletivamente.

Documentação LangChain

Registrei no **Epic #9** as decisões canônicas e a ordem da construção. A primeira execução será de consolidação, antes de implementar o Laplace.

## Prompt 1 — Consolidar a baseline canônica

Você está trabalhando no repositório privado:

`ginkgoai/ginkgo-workforce`

Sua função nesta etapa é atuar como Principal Engineer responsável por consolidar uma baseline executável e arquiteturalmente coerente antes da implementação do Laplace.

## Objetivo desta execução

Criar uma branch limpa de implementação a partir da fundação executável, consolidar apenas os documentos e contratos úteis da arquitetura refinada e remover referências que contradizem as decisões atuais.

Esta execução ainda não deve implementar o Knowledge Engine completo.

O resultado esperado é uma baseline:

- compilável;
- documentada;
- sem conflitos arquiteturais;
- sem AnythingLLM na stack do produto novo;
- sem Hermes;
- sem OpenClaw;
- pronta para receber o Laplace no próximo prompt.

---

## 1\. Segurança Git

Antes de alterar qualquer arquivo:

```markdown
git status
git remote -v
git fetch --all --prune
```

Confirme que o repositório é exatamente:

```markdown
ginkgoai/ginkgo-workforce
```

A base executável obrigatória é:

```markdown
origin/bootstrap/workforce-foundation
```

Crie a branch:

```markdown
git switch --create build/laplace-foundation origin/bootstrap/workforce-foundation
```

Caso a branch local já exista:

```markdown
git switch build/laplace-foundation
git rebase origin/bootstrap/workforce-foundation
```

Não desenvolva em:

- `main`;
- `bootstrap/workforce-foundation`;
- `agent/refine-workforce-architecture`.

Não faça merge integral da PR #1 ou da PR #10.

Não force push.

Não altere ou feche pull requests existentes.

Não abra uma nova pull request nesta execução.

---

## 2\. Fontes de verdade

Leia, nesta ordem:

1. GitHub Issue #9 e todos os seus comentários;
2. `CLAUDE.md` da branch atual;
3. `README.md`;
4. `docs/PRD.md`;
5. `docs/ARCHITECTURE.md`;
6. `docs/MIGRATION_INVENTORY.md`;
7. `docs/SECURITY.md`;
8. `docs/ROADMAP.md`;
9. `packages/db/prisma/schema.prisma`;
10. todos os packages e apps existentes;
11. documentação da branch `origin/agent/refine-workforce-architecture`.

Para ler um arquivo da branch de arquitetura sem fazer checkout:

```markdown
git show origin/agent/refine-workforce-architecture:<caminho>
```

Exemplo:

```markdown
git show origin/agent/refine-workforce-architecture:docs/AGENT-PACKAGE-SPEC.md
```

A branch `agent/refine-workforce-architecture` é apenas uma biblioteca seletiva de ideias. Ela não é a fonte arquitetural definitiva.

---

## 3\. Decisões canônicas obrigatórias

Estas decisões prevalecem sobre qualquer documento antigo.

## Produto

- Callima atende clientes.
- Eliza supervisiona e orienta o proprietário.
- O dashboard é um control plane, não um CRM visual.
- O usuário deve supervisionar exceções, não operar automações manualmente.
- Nyra, Alfred, Brann, Pyre, Wave e outros componentes ficam fora do primeiro vertical funcional.

## Runtime

- Hermes não faz parte da arquitetura.
- OpenClaw não faz parte da arquitetura.
- Não existe agente com shell, Docker, browser ou acesso irrestrito à máquina.
- Fastify, BullMQ, Redis, PostgreSQL e skills tipadas formam o runtime inicial.
- n8n é executor de workflows e integrações, nunca policy engine ou fonte de verdade.
- LangGraph pode ser estudado posteriormente mediante ADR; não adicione a dependência nesta execução.

## Conhecimento

- Laplace será o Knowledge and Evidence Kernel.
- PostgreSQL é a fonte canônica.
- pgvector é o backend vetorial inicial.
- PostgreSQL Full-Text Search fornece busca lexical.
- Retrieval será dense + lexical + RRF + reranking.
- Qdrant não entra no MVP.
- AnythingLLM não entra na arquitetura do produto novo.
- A instalação antiga do AnythingLLM na `ai-stack` existe somente como benchmark temporário.
- Nenhum adaptador legado do AnythingLLM deve ser criado nesta execução.

## Dados

- Toda entidade de negócio possui `org_id`.
- Redis não guarda conhecimento canônico.
- Arquivos originais ficam em object storage.
- Documentos, versões, chunks, embeddings, procedência e avaliações ficam no PostgreSQL.
- Conteúdo recuperado é dado não confiável e nunca pode conceder permissões ou redefinir políticas.

## Operações

- Preço, saldo, pagamento, estoque, disponibilidade e agenda devem consultar fontes estruturadas atuais.
- RAG documental serve para políticas, produtos, procedimentos, explicações e contexto.
- Toda ação externa exige contrato, validação, autorização, idempotência e evidência.
- Nenhuma execução pode ser declarada concluída sem confirmação do sistema externo.
- Falta de evidência deve resultar em abstention ou handoff, não invenção.

---

## 4\. Diagnóstico obrigatório

Antes de editar, produza internamente uma tabela com:

```markdown
Arquivo
Estado atual
Conflito encontrado
Ação recomendada
Origem da decisão
```

Procure especificamente por referências a:

```markdown
AnythingLLM
Hermes
OpenClaw
Qdrant
ChatbotX
Postiz
Pyre
Wave
Atlas
Nyra
Alfred
CRM visual
```

Classifique cada ocorrência como:

- remover;
- substituir;
- manter apenas como futuro;
- manter no escopo atual;
- mover para documentação histórica.

Não interrompa o trabalho para me perguntar sobre ocorrências já cobertas pelas decisões canônicas acima.

---

## 5\. Consolidação seletiva da PR #10

Avalie e aproveite seletivamente conceitos úteis destes arquivos:

```markdown
docs/AGENT-PACKAGE-SPEC.md
docs/AGENT-LIFECYCLE-AND-EVALUATION.md
docs/MEMORY-ARCHITECTURE.md
docs/ONBOARDING-AND-LEARNING.md
docs/RESPONSE-AND-DELIVERY-CONTRACTS.md
docs/GOVERNANCE.md
docs/PROMPT-CONTRACTS.md
docs/NAMING-TAXONOMY.md
config/personas/callima.yaml
config/personas/eliza.yaml
config/policies/action-risk-levels.yaml
```

Não copie cegamente os arquivos.

Ao portar conteúdo:

- remova Hermes;
- remova OpenClaw;
- remova ChatbotX;
- remova Postiz;
- remova AnythingLLM;
- mantenha Nyra, Alfred e demais personas apenas como evolução futura quando necessário para explicar a taxonomia;
- adapte `tenant_id` e `org_id` para uma convenção única;
- não duplique conceitos já presentes;
- não transforme YAML declarativo em comportamento executável nesta etapa;
- preserve procedência das ideias no documento de decisões.

A convenção inicial do código é:

```markdown
org_id = isolamento comercial principal
workspace_id = subdivisão opcional futura
```

Não introduza `tenant_id` como um terceiro identificador equivalente.

---

## 6\. Arquivos obrigatórios

## 6.1 Atualizar README.md

O README deve explicar:

- tese do produto;
- Callima e Eliza;
- arquitetura resumida;
- stack atual;
- como executar localmente;
- estado real do projeto;
- limites do MVP;
- que AnythingLLM, Hermes e OpenClaw não fazem parte da arquitetura;
- que Laplace será construído sobre PostgreSQL + pgvector.

Remova a recomendação de iniciar o serviço AnythingLLM.

Remova referências ao nome antigo `GKO`.

## 6.2 Atualizar CLAUDE.md

Transforme-o em regra operacional clara para Claude Code:

- hierarquia das fontes;
- limites do produto;
- convenção de branches;
- segurança multi-tenant;
- regras de banco;
- critérios de conclusão;
- proibição de alegar testes não executados;
- proibição de ampliar o escopo sem ADR;
- instrução para ler `AGENTS.md`.

## 6.3 Criar AGENTS.md

O arquivo deve orientar qualquer agente de código sobre:

- mapa do monorepo;
- comandos principais;
- regras de arquitetura;
- responsabilidades de cada app/package;
- arquivos que são fonte de verdade;
- estratégia de testes;
- modelo de commits;
- áreas proibidas;
- como registrar decisões;
- como realizar handoff.

## 6.4 Criar docs/CURRENT\_STATE.md

Registrar objetivamente:

- o que existe;
- o que compila;
- o que é apenas contrato;
- o que é skeleton;
- o que ainda não foi testado em runtime;
- PRs e branches relevantes;
- serviços externos ainda não conectados;
- dívida técnica conhecida.

Não declare que algo funciona sem evidência executada nesta sessão.

## 6.5 Criar docs/DECISIONS.md

Registrar decisões com:

```markdown
ID
Data
Status
Contexto
Decisão
Consequências
Alternativas rejeitadas
```

Incluir pelo menos:

- Callima e Eliza como escopo inicial;
- exclusão de Hermes;
- exclusão de OpenClaw;
- runtime próprio;
- n8n como executor;
- Laplace nativo;
- pgvector como backend inicial;
- Qdrant somente mediante gatilhos;
- AnythingLLM somente como benchmark externo temporário;
- fonte estruturada antes de RAG para fatos operacionais;
- `org_id` como isolamento principal.

## 6.6 Criar ADRs

Criar:

```markdown
docs/adr/0004-agent-runtime-boundary.md
docs/adr/0005-laplace-knowledge-kernel.md
docs/adr/0006-organization-isolation.md
```

### ADR 0004

Deve definir:

```markdown
Fastify + BullMQ + Skill Engine + código determinístico
```

e rejeitar:

```markdown
Hermes
OpenClaw
computer-use irrestrito
framework dentro de framework
```

LangGraph deve permanecer uma decisão futura, não uma dependência atual.

### ADR 0005

Deve definir:

```markdown
PostgreSQL + pgvector
PostgreSQL FTS
RRF
reranker
object storage
worker de ingestão
Evidence Pack
abstention
avaliações
```

AnythingLLM e Qdrant ficam fora do runtime do MVP.

### ADR 0006

Deve definir:

```markdown
org_id obrigatório
filtro server-side
RLS quando aplicável
testes negativos cross-org
namespaces de arquivos
jobs e callbacks com organização resolvida no servidor
```

## 6.7 Atualizar arquitetura e roadmap

Atualizar:

```markdown
docs/ARCHITECTURE.md
docs/PRD.md
docs/ROADMAP.md
docs/SECURITY.md
docs/MIGRATION_INVENTORY.md
```

Remover contradições e transformar o próximo marco em:

```markdown
Laplace Foundation
```

Não iniciar Eliza completa, Nango, billing ou Meta Cloud API antes do vertical de conhecimento.

---

## 7\. Docker e ambiente

Atualize:

```markdown
docker-compose.yml
.env.example
README.md
```

Remova da stack do Workforce:

```markdown
anythingllm
anythingllm_data
ANYTHINGLLM_IMAGE
ANYTHINGLLM_PORT
ANYTHINGLLM_AUTH_TOKEN
```

Não remova nada da `ai-stack`, pois ela é outro repositório e serve como referência funcional.

A stack local desta branch deve manter:

```markdown
postgres com pgvector
redis
n8n
n8n-worker
evolution-api
api
worker
web
```

Não adicione novos serviços stateful.

Não adicione Qdrant.

Não adicione MinIO nesta execução. Apenas documente a futura interface de object storage.

---

## 8\. Schema Prisma

Nesta execução, não implemente ainda todas as tabelas do Laplace.

Faça somente uma auditoria do schema atual e documente:

- tabelas reutilizáveis;
- campos inconsistentes;
- entidades que precisarão de migração;
- diferenças entre `KnowledgeSource` atual e o domínio completo planejado;
- riscos de usar `String` onde enums serão necessários;
- tabelas sem relação explícita de organização;
- índices ausentes;
- campos financeiros e de idempotência que precisam de revisão.

Não altere modelos de banco nesta execução, exceto para corrigir um erro que impeça Prisma Generate ou build. Documente qualquer correção emergencial.

O schema completo será tratado no Prompt 2.

---

## 9\. Validação

Execute, nesta ordem:

```markdown
corepack enable
pnpm install
pnpm db:generate
pnpm typecheck
pnpm build
docker compose config
```

Execute também os testes existentes, caso haja script configurado:

```markdown
pnpm test
```

Caso não exista script de teste:

- não invente resultado;
- registre explicitamente a ausência;
- adicione isso a `docs/CURRENT_STATE.md`.

Não adicione dependências apenas para satisfazer documentação.

Não ignore erros.

Corrija erros relacionados às alterações desta execução.

Registre erros preexistentes separadamente.

---

## 10\. Commit

Após todos os gates possíveis passarem:

```markdown
git status
git diff --check
git diff --stat
```

Crie um único commit:

```markdown
chore: consolidate canonical workforce baseline
```

Não faça push nesta execução.

---

## 11\. Relatório final obrigatório

Ao concluir, responda com:

## Branch

- branch base;
- branch criada;
- commit SHA.

## Diagnóstico

- conflitos encontrados;
- decisões aplicadas;
- conteúdo seletivamente aproveitado da PR #10;
- conteúdo rejeitado.

## Arquivos

- criados;
- atualizados;
- removidos.

## Validação

Para cada comando:

```markdown
comando
resultado
evidência resumida
```

## Estado do repositório

- `git status`;
- divergência em relação à branch base;
- alterações não commitadas, caso existam.

## Riscos restantes

- conflitos arquiteturais não resolvidos;
- dependências externas;
- limitações da baseline;
- pontos que precisam entrar no Prompt 2.

## Próxima ação recomendada

A próxima ação deve ser limitada a:

```markdown
Prompt 2 — contratos, schema e migrations do Laplace
```

Não comece o Prompt 2 automaticamente.

Cole esse prompt no Claude Code dentro do repositório. Ao concluir, envie o relatório integral gerado por ele; o próximo prompt será construído sobre o diff e os testes reais, não sobre suposições.