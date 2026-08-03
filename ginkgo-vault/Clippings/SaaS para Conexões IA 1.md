---
title: "SaaS para Conexões IA"
source: "https://chatgpt.com/c/6a684a46-8534-83e9-8567-50ff8822ffd8"
author:
published:
created: 2026-07-28
description: "ChatGPT conversation with 11 messages"
tags:
  - "clippings"
---
**Você disse**

---

**Você disse**

---

**Você disse**

---

**Você disse**

---

**Você disse**

---

**Você disse**

---

Escolha **1 — CSV/XLSX derivados**.

É o ponto correto para o MVP: entrega valor operacional sem transformar o Connect em uma suíte de documentos. PDF/PPTX adicionariam renderização, templates, fontes, filas pesadas e mais superfície de armazenamento antes de validarmos a função central.

Cole no Codex:

```
Escolha a opção 1 — exportações CSV/XLSX derivadas e governadas.

Decisão para o primeiro MVP:

O Ginkgo Connect poderá exportar somente o conjunto de dados derivado e autorizado produzido por uma Task concluída.

Não deve funcionar como mecanismo de exportação irrestrita do Power BI.

Fluxo canônico:

Task governada
→ consulta Power BI autorizada
→ limites aplicados
→ resultado normalizado
→ classificação de sensibilidade
→ Task VERIFIED e COMMITTED
→ solicitação de exportação
→ geração assíncrona do artefato
→ armazenamento temporário cifrado
→ URL assinada com expiração
→ auditoria de criação e download

Formatos incluídos:

1. CSV
- UTF-8 com BOM para compatibilidade com Excel em pt-BR.
- Delimitador configurável internamente, com padrão compatível com a localidade.
- Escapar fórmulas e valores iniciados por =, +, -, @ para impedir CSV injection.
- Preservar datas em formato inequívoco.
- Não aplicar formatação visual.

2. XLSX
- Uma planilha principal chamada “Dados”.
- Uma planilha “Contexto” com:
  - período consultado;
  - modelo semântico;
  - medidas e dimensões utilizadas;
  - horário da execução;
  - Task ID;
  - quantidade de linhas;
  - aviso de que os dados foram derivados pelo Ginkgo Connect.
- Cabeçalhos legíveis.
- Tipos de célula corretos.
- Sem macros.
- Sem fórmulas executáveis.
- Sem conteúdo externo vinculado.
- Sem imagens no MVP.

Restrições obrigatórias:

- Exportar somente resultados pertencentes à organização autenticada.
- A exportação deve referenciar uma Task COMMITTED.
- Não permitir DAX arbitrário no endpoint de exportação.
- Não reexecutar automaticamente a consulta durante o download.
- Não exportar o dataset bruto completo quando a Task utilizou agregação, amostragem ou redução.
- Não permitir ao usuário aumentar limites pela interface de exportação.
- Não incluir campos ocultos ou não utilizados no resultado aprovado.
- Não incluir access tokens, prompts internos, metadados privados ou Evidence interna completa.
- Não enviar o arquivo ao Claude.
- Não armazenar arquivos no PostgreSQL ou Redis.
- Não usar n8n para gerar o arquivo.

Aprovação:

- Exportações com dados classificados como R2 exigem aprovação humana.
- O envelope de aprovação deve congelar:
  - taskId;
  - formato;
  - colunas;
  - quantidade máxima de linhas;
  - classificação de sensibilidade;
  - prazo de retenção;
  - destinatário, quando houver entrega externa.
- Exportações R1 de resultados agregados podem ser automáticas.
- Dados R3 permanecem bloqueados.

Limites iniciais sugeridos:

CSV:
- até 50.000 linhas;
- até 50 colunas;
- até 25 MB após geração.

XLSX:
- até 20.000 linhas;
- até 50 colunas;
- até 20 MB.

Os limites devem ser definidos por configuração e plano, não hardcoded no domínio.

Armazenamento:

- Usar S3-compatible object storage.
- Criptografia em repouso.
- Bucket privado.
- URL assinada de uso temporário.
- TTL padrão de 24 horas.
- Exclusão automática após expiração.
- Permitir exclusão antecipada.
- Não tornar objetos públicos.
- O nome físico do objeto não deve revelar organização, usuário ou conteúdo.

Banco de dados:

Criar modelo ExportArtifact contendo:

- id;
- organizationId;
- taskId;
- requestedByUserId;
- format;
- status;
- sensitivityLevel;
- objectKey;
- contentHash;
- rowCount;
- columnCount;
- sizeBytes;
- expiresAt;
- createdAt;
- completedAt;
- deletedAt;
- failureCode;
- idempotencyKey.

Estados:

REQUESTED
APPROVAL_REQUIRED
QUEUED
GENERATING
READY
EXPIRED
DELETED
FAILED

Auditoria:

Registrar:

- solicitação;
- aprovação ou rejeição;
- início da geração;
- conclusão;
- hash do arquivo;
- criação de URL assinada;
- download;
- expiração;
- exclusão;
- falha sanitizada.

Segurança adicional:

- Neutralizar spreadsheet formula injection.
- Sanitizar nomes de colunas e abas.
- Impedir path traversal.
- Aplicar rate limit.
- Validar MIME type.
- Gerar o arquivo em worker isolado.
- Aplicar timeout e limite de memória.
- Nunca registrar conteúdo das células em logs.
- Verificar novamente tenant, Task, status e aprovação no momento de gerar e baixar.

Idempotência:

A mesma solicitação com o mesmo:
- taskId;
- formato;
- conjunto de colunas;
- versão do resultado;

deve reutilizar o artefato válido existente ou impedir geração duplicada.

PDF e PPTX:

Não entram no primeiro MVP.

Deixar apenas interfaces futuras, sem implementação ou botões falsos:

ReportRenderer
PresentationRenderer

PDF poderá entrar depois para relatórios executivos.
PPTX será considerado somente após validação de demanda empresarial.

Criar:

packages/exports/
apps/worker/src/jobs/generate-export.ts
apps/api/src/routes/exports.ts
packages/shared/src/schemas/export-artifact.ts

Rotas mínimas:

POST /v1/tasks/:taskId/exports
GET /v1/exports/:exportId
POST /v1/exports/:exportId/approve
POST /v1/exports/:exportId/reject
POST /v1/exports/:exportId/download-url
DELETE /v1/exports/:exportId

Documentar em:

docs/adr/0010-governed-derived-exports.md

Princípio canônico:

Export the governed result, not the underlying warehouse.
Files are temporary delivery artifacts, not a second database.
```

Resumo da decisão:

```
CSV/XLSX derivados → MVP
PDF executivo       → fase seguinte
PPTX                → depois de demanda validada
Exportação bruta    → proibida
```

O Connect deve entregar a bandeja pronta, não permitir que alguém leve a cozinha inteira embora.

---

**Você disse**

---

Escolha **1 — MCP remoto opcional**, usando uma arquitetura híbrida.

O servidor MCP remoto do Power BI é hoje o caminho oficial mais direto para obter o schema abrangente: tabelas, colunas, medidas, relacionamentos, tipos, hierarquias e metadados preparados para IA. Porém, ele continua em **preview**, pode mudar e depende de habilitação no tenant. [^1]

O endpoint XMLA também fornece metadados e schema em modo somente leitura, mas depende de workspace em capacidade Premium, PPU ou Power BI Embedded. Portanto, deve entrar como opção Enterprise, não como requisito do MVP. [^2]

Cole no Codex:

```
Escolha a opção 1 — MCP remoto opcional, com REST como plano de controle estável.

Decisão arquitetural:

O Ginkgo Connect deve separar descoberta, schema e execução em capacidades independentes.

1. REST API — plano de controle obrigatório

Usar Power BI REST para:

- autenticação e validação da conexão;
- listar workspaces;
- listar relatórios;
- listar modelos semânticos;
- obter IDs dos recursos;
- executar healthchecks;
- verificar permissões conhecidas;
- executar consultas read-only quando aplicável;
- manter o onboarding funcional sem depender do MCP.

REST é obrigatório em toda conexão Power BI.

2. MCP remoto — provedor preferencial de schema completo

Usar o servidor MCP remoto do Power BI, quando habilitado, exclusivamente através de um adapter governado.

Capacidades permitidas inicialmente:

- get_semantic_model_schema;
- get_report_metadata;
- execute_query, quando aprovado pela política.

A capacidade de schema deve recuperar:

- tabelas;
- colunas;
- medidas;
- relacionamentos;
- tipos;
- hierarquias;
- metadados otimizados para IA, quando existentes.

Não permitir descoberta livre de ferramentas pelo LLM em produção.

O ConnectorRegistry deve possuir uma allowlist fixa das ferramentas MCP aceitas e schemas versionados localmente.

3. MCP é opcional por conexão

Durante o onboarding, executar capability negotiation:

- verificar se o endpoint MCP está habilitado no tenant;
- verificar autenticação delegada;
- verificar Build Permission;
- tentar obter o schema;
- validar o formato retornado;
- registrar a versão observada;
- calcular hash do schema normalizado.

Estados possíveis:

FULL_SCHEMA_MCP
LIMITED_REST
FULL_SCHEMA_XMLA
DEGRADED
DISCONNECTED

Nunca mostrar a conexão como plenamente funcional quando apenas LIMITED_REST estiver disponível.

4. Comportamento sem MCP

Caso o MCP remoto esteja desabilitado, indisponível ou incompatível:

- manter conexão REST ativa;
- permitir descoberta de workspaces, relatórios e modelos;
- permitir healthchecks;
- bloquear tarefas que dependam de schema completo;
- não inventar colunas, medidas ou relacionamentos;
- não pedir ao Claude para gerar DAX sem contexto estrutural suficiente;
- mostrar ao usuário que a organização precisa habilitar o Power BI MCP para análises completas.

Mensagem de produto sugerida:

“Seu Power BI está conectado, mas o acesso ao esquema completo ainda não foi habilitado pela organização. Algumas análises permanecerão indisponíveis.”

5. XMLA read-only — adapter futuro e opcional

Preparar interface:

PowerBISchemaProvider
  ├── RemoteMcpSchemaProvider
  ├── XmlaReadOnlySchemaProvider
  └── LimitedRestSchemaProvider

Não implementar XMLA como requisito do primeiro release.

XMLA será destinado a organizações com:

- Power BI Premium;
- Premium Per User;
- Power BI Embedded;
- endpoint XMLA read-only habilitado;
- Build Permission.

Nunca solicitar XMLA read-write no MVP.

6. Segurança

Todas as chamadas devem ocorrer:

Worker
→ TaskRunner
→ Security Boundary
→ PowerBIConnector
→ transporte escolhido

Regras:

- autenticação delegada do usuário;
- RLS preservado;
- tokens somente dentro da Boundary;
- nenhuma credencial enviada ao Claude;
- nenhuma credencial enviada ao n8n;
- nenhuma ferramenta MCP de escrita;
- nenhuma operação de modelagem;
- nenhuma ferramenta desconhecida;
- nenhum endpoint MCP fornecido pelo usuário ou pelo LLM;
- egress fixado aos domínios oficiais configurados;
- timeout e limite de resposta;
- validação estrita de output.

7. Normalização de schema

Criar um modelo interno independente do formato MCP:

interface SemanticModelSchema {
  modelId: string;
  modelName?: string;
  tables: SemanticTable[];
  relationships: SemanticRelationship[];
  hierarchies: SemanticHierarchy[];
  source: "POWERBI_REMOTE_MCP" | "POWERBI_XMLA" | "LIMITED_REST";
  completeness: "FULL" | "PARTIAL";
  schemaHash: string;
  fetchedAt: string;
}

interface SemanticTable {
  name: string;
  description?: string;
  hidden: boolean;
  columns: SemanticColumn[];
  measures: SemanticMeasure[];
}

A aplicação nunca deve acoplar suas regras ao JSON bruto retornado pelo MCP.

8. Cache do schema

O schema é metadata empresarial, não resultado bruto de consulta.

Pode ser persistido como snapshot tenant-scoped:

- cifrado em repouso;
- organizationId;
- connectionId;
- semanticModelId;
- source;
- schemaHash;
- schemaVersion;
- completeness;
- fetchedAt;
- expiresAt.

TTL inicial sugerido: 24 horas.

Permitir atualização manual e refresh automático quando o snapshot expirar.

Não armazenar access tokens ou dados de linhas junto ao schema.

9. Resistência a mudanças do preview

Como o MCP remoto está em preview:

- encapsular todo acesso em RemoteMcpSchemaProvider;
- validar cada resposta com Zod;
- manter fixtures de contrato;
- registrar incompatibilidade como capability degradation;
- não quebrar a conexão REST se o MCP mudar;
- implementar feature flag para desligar o adapter MCP;
- registrar métricas de falha por versão;
- nunca aceitar silenciosamente um schema incompleto como FULL.

10. Evidence

A obtenção do schema deve registrar:

- organizationId;
- connectionId;
- semanticModelId;
- provider utilizado;
- capability;
- schemaHash;
- quantidade de tabelas;
- quantidade de colunas;
- quantidade de medidas;
- quantidade de relacionamentos;
- status;
- duração;
- timestamp;
- request ID, quando disponível.

Não incluir o schema completo na Evidence append-only.

Criar:

packages/connectors/src/powerbi/schema/schema-provider.ts
packages/connectors/src/powerbi/schema/remote-mcp-schema-provider.ts
packages/connectors/src/powerbi/schema/limited-rest-schema-provider.ts
packages/connectors/src/powerbi/schema/schema-normalizer.ts
packages/connectors/src/powerbi/schema/schema-capabilities.ts
packages/shared/src/schemas/semantic-model-schema.ts

Preparar, sem implementar:

packages/connectors/src/powerbi/schema/xmla-readonly-schema-provider.ts

Documentar em:

docs/adr/0011-powerbi-schema-provider-strategy.md

Princípio canônico:

REST keeps the connection alive.
Remote MCP provides the complete schema when available.
XMLA is an enterprise fallback.
Capability status must always be honest.
```

## Resultado da decisão

```
REST            → obrigatório e estável
MCP remoto      → schema completo preferencial
XMLA read-only  → futuro fallback Enterprise
MCP indisponível→ modo limitado, nunca schema inventado
```

Consultas feitas pelo MCP no contexto do usuário exigem permissão Build e preservam RLS; a Microsoft alerta que RLS não é suportado atualmente com autenticação por service principal nesse cenário. [^3]

O Codex identificou corretamente a bifurcação: REST sozinho mantém a nave ligada, mas não entrega todo o mapa estelar. O MCP fornece o mapa; a abstração impede que o produto caia junto caso o mapa em preview seja redesenhado.

---

**Você disse**

---

**Não mande implementar o plano inteiro em uma única execução.** O planejamento está sólido, mas ele descreve praticamente o MVP completo: Kernel, banco, OAuth, Power BI, Claude, exports, MCP interno, n8n e frontend.

Selecione **“Sim, implementar este plano”**, mas antes ou imediatamente depois cole esta trava:

```
Implemente este plano, porém apenas a primeira fatia vertical de fundação.

Não tente construir o MVP completo nesta execução.

ESCOPO DESTA EXECUÇÃO — FOUNDATION 001

1. Criar ou inicializar o repositório dedicado:
   ginkgoai/ginkgo-connect

2. Criar a branch:
   feat/foundation-001

3. Registrar os repositórios doadores e SHAs em:
   docs/extraction-manifest.md

4. Criar o monorepo:

apps/
  api/
  web/
  worker/

packages/
  core/
  db/
  boundary/
  connectors/
  llm/
  exports/
  shared/
  ui/

infra/
  docker/
  n8n/

docs/
  adr/
  architecture/
  operations/

5. Configurar:
- pnpm workspace;
- Turborepo;
- ESM;
- TypeScript strict;
- lint;
- formatting;
- Vitest;
- scripts de build, lint, typecheck e test;
- GitHub Actions;
- dependency constraints;
- .gitignore;
- .env.example sem segredos;
- AGENTS.md;
- README.md.

6. Subir somente a infraestrutura básica local:
- PostgreSQL;
- Redis;
- MinIO;
- healthchecks;
- redes privadas;
- volumes persistentes.

Não adicionar n8n nesta fatia.
Não adicionar Power BI.
Não adicionar Claude.
Não implementar OAuth.
Não implementar billing.
Não construir telas funcionais.
Não criar models Prisma definitivos ainda.
Não copiar código de domínio dos repositórios doadores.

7. Criar apenas contratos vazios e compiláveis para os pacotes:

@connect/core
@connect/db
@connect/boundary
@connect/connectors
@connect/llm
@connect/exports
@connect/shared
@connect/ui

Os pacotes devem respeitar estas regras de dependência:

core:
- não importa Prisma;
- não importa Fastify;
- não importa BullMQ;
- não importa Claude;
- não importa Power BI;
- não acessa process.env.

boundary:
- depende apenas de contratos/portas;
- não depende diretamente de Prisma.

apps:
- funcionam como composition roots;
- são responsáveis pelo wiring concreto.

8. Criar os ADRs iniciais:

docs/adr/0001-monorepo-boundaries-and-runtime-baseline.md
docs/adr/0002-task-lifecycle-frozen-decision-and-append-only-truth.md
docs/adr/0003-postgresql-source-of-truth-outbox-and-redis-ephemerality.md
docs/adr/0004-connect-credits-ledger-reservation-and-settlement.md

Nesta fatia, os ADRs podem registrar decisões aprovadas, mas não devem alegar que recursos ainda não implementados estão funcionais.

9. Compatibilidade TypeScript

Node.js 24 LTS pode ser usado como runtime.

TypeScript 7 deve ser adotado somente após validar compatibilidade real com:
- ESLint;
- typescript-eslint;
- Next.js;
- Vitest;
- Prisma;
- Turborepo.

Como TypeScript 7.0 não possui API programática estável, não presuma que ele é substituto direto para ferramentas que importam a API do TypeScript.

Caso typescript-eslint ou outra ferramenta ainda dependa da API anterior:
- usar TypeScript 7 para o tsc;
- manter @typescript/typescript6 para compatibilidade das ferramentas;
- ou usar TypeScript 6 como baseline temporário;
- documentar a decisão no ADR 0001.

Não contornar incompatibilidades desativando lint ou typecheck.

10. Proveniência

Não copiar diretórios inteiros nesta fatia.

Criar a estrutura do manifesto com:

- repository;
- sourceCommit;
- sourcePath;
- destinationPath;
- treatment: copied | adapted | rewritten;
- reason;
- verification.

Nenhum arquivo doador deve ser importado sem aparecer nesse manifesto.

11. Gates obrigatórios

Antes de concluir:

pnpm install
pnpm lint
pnpm typecheck
pnpm test
pnpm build
docker compose config
docker compose up -d
docker compose ps

Validar healthchecks de PostgreSQL, Redis e MinIO.

12. Entrega

Ao terminar:
- mostrar a árvore criada;
- listar arquivos alterados;
- listar versões efetivamente instaladas;
- mostrar resultados dos gates;
- registrar limitações;
- registrar decisões pendentes;
- não iniciar a próxima fase automaticamente.

Somente criar commit se todos os gates estiverem verdes.

Commit:

chore: bootstrap ginkgo connect foundation

Pare após esta fatia e aguarde revisão.
```

## Correção técnica relevante

Node.js 24 já está em LTS, Next.js 16 e Prisma 7 são releases estáveis. [^4]

O ponto delicado é **TypeScript 7**. Ele foi lançado como estável em julho de 2026, mas não inclui ainda uma API programática estável. A própria equipe recomenda compatibilidade paralela com TypeScript 6 para ferramentas que importam essa API, incluindo cenários ligados ao `typescript-eslint`. [^5]

Portanto:

```
Clique: Sim, implementar este plano
Execução real: somente Foundation 001
Depois: auditoria
Em seguida: Kernel + banco, em uma nova tarefa
```

Deixar o Codex executar as quinze fases de uma vez produziria um castelo funcional no README e uma favela distribuída no runtime. Aqui, cada módulo só ganha oxigênio depois de passar no próprio teste.

[^1]: [learn.microsoft.com](https://learn.microsoft.com/en-us/power-bi/developer/mcp/remote-mcp-server-get-started?utm_source=chatgpt.com)

[^2]: [learn.microsoft.com](https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-connect-tools?utm_source=chatgpt.com)

[^3]: [learn.microsoft.com](https://learn.microsoft.com/en-us/power-bi/developer/mcp/remote-mcp-server-tools?utm_source=chatgpt.com)

[^4]: [nodejs.org](https://nodejs.org/pt-br/about/previous-releases?utm_source=chatgpt.com)

[^5]: [devblogs.microsoft.com](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/?utm_source=chatgpt.com)