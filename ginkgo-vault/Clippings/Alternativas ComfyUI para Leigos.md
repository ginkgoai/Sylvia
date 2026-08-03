---
title: "Alternativas ComfyUI para Leigos"
source: "https://chatgpt.com/c/6a5ff9ce-3d5c-83e9-933a-fd12b6f2a3ff"
author:
published:
created: 2026-07-21
description: "ChatGPT conversation with 6 messages"
tags:
  - "clippings"
---
**Você disse**

nunca utilizei comfyui. como um leigo, posso passar para o work/codex configurar templates e rodar para mim, me explicando ativamente, com foco e proposito em criação de conteudo, influencer de ia, videos shorts reels, ou similiares, selfies, e influencer style, imagens=insta carroceis. visando que minha maquina provavelmente não aguente local, qual a alternativa?

---

Eu não consigo acessar diretamente `C:\dev\pyre` no seu computador por este chat.

Para eu analisar de verdade, use uma destas opções:

1. compacte `C:\dev\pyre` em `.zip` e envie aqui; ou
2. envie o link do repositório GitHub do Pyre.

Enquanto isso, abra o **Codex/Work** na pasta:

```powershell
cd C:\dev\pyre
codex
```

Cole este prompt:

```
Analise este projeto inteiro sem alterar nenhum arquivo inicialmente.

Contexto:
O projeto se chama Pyre e deve funcionar como uma plataforma de automação de conteúdo e social media com IA.

Quero que você me guie como iniciante, em português, explicando o projeto por etapas.

Primeira missão: diagnóstico completo.

1. Mapeie a estrutura de pastas e arquivos.
2. Identifique:
   - frontend;
   - backend;
   - banco de dados;
   - autenticação;
   - APIs;
   - integrações;
   - geração de imagens;
   - geração de vídeos;
   - calendário editorial;
   - publicação em redes sociais;
   - sistema de créditos ou billing;
   - filas, jobs e workers;
   - armazenamento de arquivos;
   - variáveis de ambiente;
   - deploy.
3. Leia os arquivos principais:
   - README;
   - package.json;
   - arquivos de configuração;
   - schema SQL;
   - migrations;
   - rotas;
   - services;
   - hooks;
   - componentes centrais.
4. Não instale nada e não modifique nada ainda.
5. Produza um relatório com:
   - arquitetura atual;
   - fluxo de funcionamento;
   - funcionalidades prontas;
   - funcionalidades incompletas;
   - erros prováveis;
   - riscos técnicos;
   - dívidas técnicas;
   - dependências críticas;
   - próximos passos recomendados.
6. Explique cada pasta como se eu fosse iniciante.
7. Crie um diagrama textual da arquitetura.
8. Classifique cada módulo como:
   - funcional;
   - parcial;
   - mockado;
   - ausente;
   - quebrado;
   - desconhecido.
9. Ao final, proponha uma ordem de trabalho:
   - etapa 1: projeto rodando;
   - etapa 2: banco e autenticação;
   - etapa 3: geração de conteúdo;
   - etapa 4: biblioteca de mídia;
   - etapa 5: calendário;
   - etapa 6: publicação;
   - etapa 7: billing;
   - etapa 8: produção e monitoramento.

Antes de executar qualquer alteração, aguarde minha aprovação.
```

## Primeira etapa que você deve entender

O Pyre provavelmente deve ser dividido mentalmente em seis motores:

```
Briefing
   ↓
Planejamento editorial
   ↓
Geração de texto/imagem/vídeo
   ↓
Revisão e aprovação
   ↓
Agendamento/publicação
   ↓
Métricas e aprendizado
```

Cada motor precisa funcionar isoladamente antes de virar uma esteira automática.

## Ordem correta de diagnóstico

### 1\. Descobrir a stack

Execute:

```powershell
Get-ChildItem
```

Depois:

```powershell
Get-Content package.json
```

Procure por tecnologias como:

```
Next.js
React
Vite
Supabase
Prisma
Drizzle
PostgreSQL
Stripe
Trigger.dev
Inngest
n8n
Cloudinary
S3
OpenAI
Replicate
Fal
Postiz
Blotato
```

O `package.json` é o raio-X inicial. Ele revela boa parte da anatomia do projeto.

### 2\. Verificar como iniciar

Normalmente:

```powershell
npm install
npm run dev
```

Ou:

```powershell
pnpm install
pnpm dev
```

Não misture `npm`, `pnpm` e `yarn`. Veja qual arquivo existe:

```
package-lock.json → npm
pnpm-lock.yaml → pnpm
yarn.lock → yarn
```

### 3\. Conferir variáveis de ambiente

Procure:

```
.env
.env.local
.env.example
```

Nunca envie o conteúdo real desses arquivos aqui sem apagar:

```
API keys
tokens
senhas
URLs privadas
service role keys
webhook secrets
```

Envie apenas os nomes das variáveis:

```
NEXT_PUBLIC_SUPABASE_URL=
SUPABASE_SERVICE_ROLE_KEY=
OPENAI_API_KEY=
STRIPE_SECRET_KEY=
```

### 4\. Identificar o estado real

Um botão bonito no frontend não significa uma funcionalidade pronta.

O Codex deve verificar:

```
Botão existe
→ chama uma função?
→ função chama uma API?
→ API grava no banco?
→ existe tratamento de erro?
→ retorna resultado real?
```

Sem isso, o sistema pode ser apenas um cenário de cinema: fachada de cidade, mas nada atrás das portas.

## Marco zero do Pyre

Antes de integrar ComfyUI, RunPod ou geração avançada, confirme:

```
[ ] Projeto abre localmente
[ ] Login funciona
[ ] Banco conecta
[ ] Usuário possui workspace
[ ] Briefing pode ser criado
[ ] Conteúdo pode ser salvo
[ ] Arquivos podem ser armazenados
[ ] Status do conteúdo pode mudar
[ ] Logs de erro são visíveis
```

Depois disso:

```
[ ] Geração de texto
[ ] Geração de imagem
[ ] Geração de vídeo
[ ] Aprovação
[ ] Calendário
[ ] Publicação
[ ] Métricas
```

Envie o `.zip` do projeto ou o repositório GitHub. Com isso, faço o diagnóstico arquivo por arquivo e transformo a análise em um plano de execução numerado.

---

**Você disse**

---

Analisei o `pyre.zip`. O ponto central é este:

## Diagnóstico direto

Essa pasta **ainda não é o Pyre como SaaS de social media**.

Ela é um **laboratório inicial de ComfyUI**, criado para gerar um retrato básico de uma influenciadora virtual.

Hoje o projeto possui:

```
Pyre atual
├── 1 personagem fictícia
├── 1 prompt-base
├── 1 prompt negativo
├── 1 workflow manual ComfyUI
├── 1 workflow para API
├── 1 script Python de envio
├── testes locais
└── documentação inicial
```

Ainda não existem:

```
frontend
backend de aplicação
login
Supabase
banco de dados
dashboard
calendário editorial
geração de carrosséis
geração de vídeo
biblioteca de mídia
aprovação de conteúdo
publicação em Instagram/TikTok
n8n
filas
billing
multiusuário
analytics
```

Ou seja: o Codex construiu corretamente a **primeira célula do motor visual**, mas não construiu ainda a nave inteira.

---

## 1\. Estado técnico real

## Estrutura encontrada

```
pyre/
├── api/
│   └── submit_comfy_cloud.py
├── characters/
│   └── virtual_creator_v01.md
├── deployment/
│   ├── docker/
│   └── runpod/
├── docs/
├── outputs/
├── prompts/
├── references/
├── scripts/
├── tests/
└── workflows/
    ├── campaigns/
    ├── carousel/
    ├── identity/
    ├── lifestyle/
    └── video/
```

As pastas `campaigns`, `carousel`, `lifestyle` e `video` estão praticamente vazias. Elas são apenas espaços reservados.

O único workflow funcional está em:

```
workflows/identity/
```

---

## 2\. O que já funciona

Executei os testes fornecidos pelo projeto.

Resultado:

```
OK: os workflows manual e API são JSON válidos
```

Também executei a simulação de envio:

```json
{
  "mode": "dry-run",
  "endpoint": "https://cloud.comfy.org/api/prompt",
  "checkpoint": "sd_xl_base_1.0.safetensors",
  "seed": 2407202601,
  "dimensions": {
    "width": 1024,
    "height": 1024,
    "batch_size": 1
  },
  "node_count": 7
}
```

Isso confirma que:

- os arquivos JSON são estruturalmente válidos;
- o workflow tem conexões coerentes;
- o script Python consegue carregar o workflow;
- as variáveis podem ser substituídas;
- nenhuma chave foi exposta;
- o modo de simulação funciona.

Mas isso **não confirma que uma imagem foi realmente gerada no Comfy Cloud**.

Ainda falta testar:

```
workflow válido
→ modelo disponível na sua conta
→ API aceita a chave
→ geração entra na fila
→ imagem é produzida
→ imagem é recuperada
```

O projeto chega até a porta da fábrica. Ainda não entrou na linha de produção.

---

## 3\. O workflow atual, explicado como leigo

Ele possui sete nodes:

```
1. Load Checkpoint
        ↓
2. Prompt positivo
3. Prompt negativo
        ↓
4. Tela vazia 1024 × 1024
        ↓
5. KSampler
        ↓
6. VAE Decode
        ↓
7. Save Image
```

## Node 1 — Checkpoint

```
CheckpointLoaderSimple
```

Carrega o modelo de geração.

Está configurado para:

```
sd_xl_base_1.0.safetensors
```

Esse é o “cérebro visual” atual.

Problema possível: esse nome precisa existir exatamente no ambiente Comfy Cloud. O projeto pressupõe que ele estará disponível, mas isso ainda não foi validado.

---

## Nodes 2 e 3 — Prompts

O prompt positivo descreve:

- mulher adulta fictícia;
- brasileira;
- 28 anos;
- estilo lifestyle;
- roupa de linho;
- iluminação editorial;
- aparência fotográfica.

O prompt negativo tenta evitar:

- menores;
- texto;
- marca d’água;
- baixa resolução;
- anatomia ruim;
- rosto deformado.

Isso é aceitável como teste inicial.

Porém, apenas o prompt textual não garante consistência facial. A personagem pode mudar entre uma geração e outra.

---

## Node 4 — Canvas

Cria uma imagem latente de:

```
1024 × 1024
batch: 1
```

É uma resolução adequada para teste de retrato.

Para Instagram, posteriormente precisaremos de formatos diferentes:

```
Feed vertical: 1080 × 1350
Story/Reel: 1080 × 1920
Quadrado: 1080 × 1080
Capa vertical: 1080 × 1920
```

---

## Node 5 — KSampler

É onde a geração ocorre de fato.

Ele combina:

```
modelo
+ prompt positivo
+ prompt negativo
+ seed
+ configurações de amostragem
```

A seed atual é:

```
2407202601
```

Seed é como um ponto de partida matemático. Mantendo modelo, prompt e configurações iguais, tende a reproduzir resultado semelhante no mesmo ambiente.

Mas seed não é identidade.

```
Seed fixa ≠ personagem fixa
```

---

## Node 6 — VAE Decode

Transforma o resultado interno do modelo em uma imagem visível.

É como converter o código bruto da Matrix em pixels.

---

## Node 7 — Save Image

Salva o arquivo gerado.

Na execução manual, isso ocorre dentro do ambiente do ComfyUI. Na execução via API, ainda será necessário implementar a recuperação e o armazenamento dessa imagem.

---

## 4\. O que o script Python faz

Arquivo:

```
api/submit_comfy_cloud.py
```

Ele permite:

- carregar o workflow JSON;
- alterar prompt;
- alterar seed;
- alterar checkpoint;
- validar o workflow;
- executar em modo simulado;
- enviar para o endpoint do Comfy Cloud.

Exemplo atual:

```powershell
python api\submit_comfy_cloud.py --dry-run
```

O modo `--dry-run` não consome créditos nem gera imagem.

O script de envio possui uma estrutura razoável:

```
carrega .env
→ lê JSON
→ aplica parâmetros
→ valida nodes
→ cria requisição
→ envia para /api/prompt
→ retorna prompt_id
```

## O que falta no cliente API

Ainda faltam funções essenciais:

```
consultar status da geração
esperar conclusão
identificar arquivos de saída
baixar imagem
salvar em outputs/
registrar metadados
lidar com timeout prolongado
retry
controle de custo
logs estruturados
```

No momento, ele apenas envia o pedido. É como fazer um pedido no restaurante e ir embora antes de a comida chegar.

---

## 5\. Problemas e inconsistências encontrados

## 5.1 Nome incorreto no README

O README orienta importar:

```
workflows/identity/portrait_consistent_manual.json
```

Mas o arquivo existente é:

```
portrait_consistent_manual_v01.json
```

Isso pode confundir você ou o Codex.

O README deve ser corrigido.

---

## 5.2 O projeto não possui commits

O repositório Git está inicializado, mas aparece como:

```
No commits yet on main
```

Todos os arquivos estão sem versionamento.

Antes da próxima alteração, deve ser criado um commit-base:

```
chore: establish initial comfy content studio baseline
```

Isso cria um ponto seguro de retorno.

---

## 5.3 Diagnóstico afirma fatos da sua máquina

O arquivo:

```
docs/00-diagnostico.md
```

declara que encontrou:

```
RTX 4060 com 8 GB
Docker Desktop 29.6.1
Python 3.13
Comfy Desktop em execução
```

Isso parece ter sido produzido pelo Codex operando localmente em sua máquina. É coerente, mas deve ser tratado como fotografia daquele momento, não como configuração garantida para sempre.

---

## 5.4 A API ainda não foi validada ao vivo

O projeto presume:

```
POST https://cloud.comfy.org/api/prompt
X-API-Key
```

Mas ainda não houve teste real com sua conta.

Antes de construir em cima disso, o Codex deve verificar a documentação atual e o comportamento real da conta.

---

## 5.5 Consistência da influenciadora ainda é fraca

O projeto usa:

```
prompt textual + seed
```

Isso serve para descobrir uma aparência inicial, mas não para manter a mesma influenciadora durante dezenas de posts.

Para consistência real, posteriormente serão necessários mecanismos como:

```
imagem de referência aprovada
FaceID/IP-Adapter equivalente
LoRA da personagem
controle de pose
controle de composição
dataset versionado
```

Não precisa começar por LoRA. Mas precisa saber que o workflow atual é uma prova de conceito, não uma identidade de produção.

---

## 5.6 O nome “Pyre” está sendo usado para algo menor

Atualmente a pasta `C:\dev\pyre` contém apenas o laboratório ComfyUI.

Estratégicamente, eu separaria:

```
C:\dev\pyre
    aplicação principal

C:\dev\pyre-comfy-worker
    workflows visuais e integração ComfyUI
```

Ou dentro de um monorepo:

```
pyre/
├── apps/
│   ├── web/
│   └── api/
├── services/
│   ├── content-engine/
│   ├── comfy-worker/
│   └── publisher/
├── packages/
│   ├── database/
│   ├── ui/
│   └── shared/
└── infrastructure/
```

O motor ComfyUI é um órgão do Pyre. Não deve ser confundido com o corpo inteiro.

---

## 6\. Classificação dos módulos

| Módulo | Estado |
| --- | --- |
| Documentação inicial | Funcional |
| Ficha da personagem | Funcional como especificação |
| Prompt-base | Funcional como rascunho |
| Workflow manual | Estruturalmente funcional |
| Workflow API | Estruturalmente funcional |
| Validação local | Funcional |
| Envio Comfy Cloud | Parcial |
| Recuperação da imagem | Ausente |
| Armazenamento de resultados | Ausente |
| Consistência facial avançada | Ausente |
| Lifestyle | Ausente |
| Campanhas | Ausente |
| Carrosséis | Ausente |
| Vídeos | Ausente |
| Produção em lote | Ausente |
| Frontend Pyre | Ausente |
| Backend Pyre | Ausente |
| Banco de dados | Ausente |
| Autenticação | Ausente |
| Calendário | Ausente |
| Publicação social | Ausente |
| Métricas | Ausente |
| Billing | Ausente |
| Integração n8n | Ausente |
| RunPod | Apenas documentado |
| Docker | Apenas documentado |

---

## 7\. Etapa correta agora

Não avance imediatamente para vídeo, LoRA, RunPod ou automação em massa.

A próxima etapa deve ser:

## Etapa 1 — Primeira imagem real

Objetivo:

```
executar o workflow manual
→ gerar uma imagem real
→ confirmar que o modelo existe
→ salvar o resultado
→ avaliar qualidade
```

## Procedimento

Na sua tela do Comfy Desktop, abra o cartão:

```
Comfy Cloud
```

Depois procure a opção de importar workflow.

Importe:

```
C:\dev\pyre\workflows\identity\portrait_consistent_manual_v01.json
```

Ao abrir, verifique o node:

```
Load Checkpoint
```

Confirme se existe:

```
sd_xl_base_1.0.safetensors
```

Caso não exista, selecione um modelo SDXL disponível, mas não altere outros parâmetros ainda.

Execute uma única imagem.

---

## 8\. Como avaliar a primeira geração

Não julgue apenas “bonita ou feia”. Use critérios objetivos:

```
Identidade
├── rosto natural
├── olhos coerentes
├── cabelo coerente
└── idade adulta clara

Fotografia
├── iluminação
├── pele
├── enquadramento
└── profundidade

Aplicação
├── parece criadora de conteúdo?
├── funcionaria no Instagram?
├── possui aparência genérica?
└── permite criar variações?
```

Crie uma escala:

```
0 = inutilizável
1 = fraco
2 = aceitável
3 = bom
4 = muito bom
5 = identidade candidata
```

---

## 9\. Prompt para o Codex executar a próxima etapa

Abra o Codex em:

```powershell
cd C:\dev\pyre
codex
```

Use:

```
Analise o estado atual deste repositório e execute somente a Etapa 1 de validação.

Objetivo:
Preparar o projeto para a primeira geração real no Comfy Cloud, sem instalar modelos, custom nodes, RunPod ou LoRA.

Antes de alterar:
1. Execute os testes existentes.
2. Leia README.md, AGENTS.md e os workflows de identity.
3. Verifique inconsistências de caminhos e nomes de arquivos.
4. Mostre o plano de alterações.

Alterações autorizadas:
1. Corrigir no README o nome do workflow manual para:
   workflows/identity/portrait_consistent_manual_v01.json
2. Criar um checklist chamado:
   docs/06-primeira-geracao-real.md
3. Adicionar instruções claras para:
   - importar o workflow;
   - confirmar o checkpoint;
   - gerar uma imagem;
   - localizar a saída;
   - registrar seed, modelo e data;
   - avaliar qualidade de 0 a 5.
4. Criar:
   outputs/generated/.gitkeep
5. Criar um arquivo:
   outputs/README.md
   explicando como nomear as imagens.
6. Não enviar nenhuma requisição real.
7. Não utilizar credenciais.
8. Não instalar dependências.
9. Não alterar o prompt ou a seed.
10. Executar novamente os testes ao final.

Depois:
- informe arquivos alterados;
- explique cada alteração;
- mostre como testar;
- mostre como desfazer;
- aguarde aprovação antes de qualquer etapa adicional.
```

---

## 10\. Padrão de nome das imagens

Use algo assim:

```
creator_v01_s2407202601_sdxl_2026-07-21_001.png
```

Significado:

```
creator_v01       personagem
s2407202601       seed
sdxl              modelo
2026-07-21        data
001               versão da execução
```

Isso parece detalhe burocrático, mas em geração de IA sem rastreabilidade tudo vira um multiverso de imagens sem origem conhecida.

---

## 11\. Ordem recomendada das próximas fases

```
Fase 1
Primeira imagem real

Fase 2
Gerar cinco candidatas mudando somente a seed

Fase 3
Escolher e congelar uma identidade-base

Fase 4
Criar workflow lifestyle com referência

Fase 5
Criar formatos Instagram

Fase 6
Criar geração em lote

Fase 7
Criar recuperação automática por API

Fase 8
Conectar ao n8n e Pyre

Fase 9
Vídeos verticais

Fase 10
RunPod ou Serverless
```

A ação correta agora é validar uma única imagem no Comfy Cloud. Sem isso, qualquer automação posterior estará industrializando uma hipótese.

---

**Você disse**

output do work

---

O output do Work está correto e confirma o diagnóstico: o repositório atual é um **POC de geração de retrato via ComfyUI/Comfy Cloud**, não o Pyre completo. O Work fez uma análise somente leitura, executou os testes seguros e não alterou arquivos nem consumiu créditos.

## O que o Work descobriu de mais importante

O estado real é:

```
Pyre atual
  └── laboratório ComfyUI
       ├── personagem em Markdown
       ├── prompts
       ├── workflow manual
       ├── workflow API
       ├── cliente Python
       └── testes estruturais
```

Ainda faltam duas camadas diferentes:

```
Camada 1 — Motor de conteúdo
ComfyUI + modelos + workflows + armazenamento + jobs

Camada 2 — Produto Pyre
Dashboard + usuários + calendário + campanhas + publicação + billing
```

Misturar as duas agora seria como tentar construir o aeroporto enquanto ainda estamos testando o motor do primeiro avião.

## Pontos críticos confirmados

### 1\. O fluxo da API termina cedo demais

Hoje:

```
envia workflow
→ recebe prompt_id
→ encerra
```

O ciclo correto precisa ser:

```
envia workflow
→ recebe prompt_id
→ acompanha processamento
→ detecta sucesso ou erro
→ identifica outputs
→ baixa a imagem
→ salva metadados
→ registra custo e duração
```

O cliente Python atual faz apenas a submissão.

### 2\. O README possui um caminho quebrado

Ele aponta para:

```
portrait_consistent_manual.json
```

Mas o arquivo real é:

```
portrait_consistent_manual_v01.json
```

É uma correção pequena, mas necessária antes de você seguir as instruções manualmente.

### 3\. O checkpoint não foi confirmado

O workflow usa:

```
sd_xl_base_1.0.safetensors
```

Isso não significa que esse modelo esteja disponível na sua instância do Comfy Cloud. O nome precisa ser confirmado na interface antes da geração real.

### 4\. Não existe versionamento seguro

O Git foi inicializado, mas não há commits nem remoto. Portanto, ainda não existe um ponto real de restauração.

Antes de o Work começar a editar, o ideal é criar o primeiro commit.

### 5\. O dry-run não prova geração

Os testes confirmam:

```
JSON válido
workflow estruturalmente coerente
script Python funcionando
variáveis substituíveis
```

Eles não confirmam:

```
API key válida
plano com acesso
checkpoint existente
job processado
imagem gerada
download funcionando
```

A fundação passou no teste elétrico, mas ainda não ligamos o reator.

## Decisão recomendada

Não comece agora frontend, Supabase, Stripe ou calendário editorial.

A etapa seguinte deve ser dividida em dois pequenos marcos.

## Marco 1 — Organizar a fundação

Autorize o Work a:

1. corrigir o README;
2. criar o commit inicial;
3. melhorar a validação do cliente;
4. criar o checklist da primeira geração;
5. preparar a pasta de outputs;
6. não fazer chamada real ainda.

## Marco 2 — Primeira geração controlada

Depois:

1. abrir o workflow no Comfy Cloud;
2. verificar o checkpoint;
3. gerar uma única imagem;
4. registrar o resultado;
5. avaliar qualidade;
6. só então testar a API.

Essa ordem reduz a quantidade de variáveis. Caso a geração falhe, saberemos se o problema está no workflow, no modelo, na conta ou na API.

## Prompt para enviar agora ao Work

```
Aprovo a próxima etapa de organização da fundação do projeto.

Execute somente as alterações abaixo. Não faça geração real, não envie chamadas à API, não consuma créditos, não instale modelos e não altere a arquitetura do produto.

ETAPA A — CRIAR BASE SEGURA DE VERSIONAMENTO

1. Confirme novamente o estado atual do Git.
2. Verifique se .env, outputs gerados, caches Python e arquivos sensíveis estão corretamente ignorados.
3. Caso estejam seguros, crie o primeiro commit do projeto com a mensagem:

chore: establish initial comfy content studio baseline

4. Não configure repositório remoto.
5. Mostre o hash e o conteúdo resumido do commit.

ETAPA B — CORREÇÕES DOCUMENTAIS

1. Corrija no README o caminho incorreto:

de:
workflows/identity/portrait_consistent_manual.json

para:
workflows/identity/portrait_consistent_manual_v01.json

2. Atualize qualquer menção desatualizada aos planos compatíveis com a API do Comfy Cloud, citando a data da verificação na documentação.

3. Deixe explícito que outputs/ é apenas um destino planejado e que o cliente atual ainda não baixa imagens.

ETAPA C — CHECKLIST DA PRIMEIRA GERAÇÃO

Crie:

docs/06-primeira-geracao-real.md

O documento deve explicar de forma didática:

1. Como abrir a instância Comfy Cloud.
2. Como importar:
   workflows/identity/portrait_consistent_manual_v01.json
3. Como verificar se todos os sete nodes carregaram.
4. Como identificar nodes ausentes ou inválidos.
5. Como verificar o checkpoint disponível.
6. O que fazer caso sd_xl_base_1.0.safetensors não exista.
7. Como executar apenas uma imagem.
8. Como localizar a imagem gerada.
9. Como registrar:
   - data;
   - modelo;
   - seed;
   - prompt;
   - resolução;
   - duração;
   - avaliação.
10. Como avaliar a imagem de 0 a 5 nos critérios:
   - identidade;
   - naturalidade;
   - anatomia;
   - iluminação;
   - qualidade fotográfica;
   - adequação para redes sociais.

ETAPA D — ORGANIZAÇÃO DOS OUTPUTS

Crie:

outputs/generated/.gitkeep
outputs/README.md
outputs/generation_log.example.json

O arquivo de exemplo deve conter:

- generation_id;
- character_id;
- workflow_version;
- provider;
- checkpoint;
- seed;
- prompt;
- negative_prompt;
- width;
- height;
- status;
- started_at;
- completed_at;
- duration_seconds;
- estimated_cost;
- output_filename;
- quality_scores;
- notes.

Não crie dados reais nem credenciais.

ETAPA E — ROBUSTEZ LOCAL

Melhore somente as validações locais do cliente Python:

1. Detectar workflow JSON inválido.
2. Detectar nodes obrigatórios ausentes.
3. Detectar campos internos obrigatórios ausentes.
4. Na execução real, considerar erro quando prompt_id não existir ou for null.
5. Impedir envio da API key para um host diferente de cloud.comfy.org por padrão.
6. Permitir host diferente apenas com uma flag explícita:
   --allow-custom-host
7. Manter compatibilidade com o dry-run atual.
8. Não implementar polling ou download nesta etapa.

ETAPA F — TESTES

Adicione testes para:

1. workflow válido;
2. node ausente;
3. campo interno ausente;
4. resposta sem prompt_id;
5. bloqueio de host não autorizado;
6. dry-run sem rede.

Execute todos os testes ao final.

ENTREGA

Ao terminar, apresente:

1. arquivos criados;
2. arquivos alterados;
3. testes executados;
4. resultados;
5. novo estado do Git;
6. como desfazer as alterações;
7. comando exato para abrir o checklist.

Não avance para frontend, banco, RunPod, LoRA, vídeo, n8n ou geração real.
```

## Após essa etapa

O próximo prompt não deve pedir “construa o Pyre”. Deve pedir apenas:

```
Guie-me interativamente pela primeira geração manual.
Pare depois de cada ação e aguarde minha confirmação.
```

Isso força o Work a agir como instrutor, não como uma escavadeira autônoma soltando dependências pela pasta inteira.