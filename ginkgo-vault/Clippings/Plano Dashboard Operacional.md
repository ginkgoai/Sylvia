---
title: "Plano Dashboard Operacional"
source: "https://chatgpt.com/c/6a665386-d920-83e9-aed2-4ae549fd0582"
author:
published:
created: 2026-07-26
description: "ChatGPT conversation with 2 messages"
tags:
  - "clippings"
---
**Você disse**

Segue um plano completo para esta dashboard de operção com multiagent alimentado por claude, construção via prompt no proprio claude code.

---

Consolidei o plano em uma arquitetura **local-first, auditável e construída incrementalmente pelo Claude Code**. A conversa identificou corretamente que a sessão do Claude não deve ser o banco: cada operação precisa de uma pasta independente, arquivos persistentes e dashboard iniciado em localhost.

**Versão:** 1.0  
**Produto:** Dashboard operacional multiagente  
**Ambiente:** Claude Code + aplicação local em localhost  
**Persistência:** arquivos da operação em disco  
**Usuário inicial:** operador individual  
**Modelo:** preparação automática + decisão humana  
**Status:** pronto para iniciar desenvolvimento

---

## 1\. Visão do produto

Construir uma central operacional local para controlar uma operação de vendas na Amazon com produtos provenientes de fornecedores externos.

O sistema funciona como uma torre de comando:

```markdown
Dados da operação
        ↓
Agentes especializados
        ↓
Cálculos determinísticos
        ↓
Fila operacional priorizada
        ↓
Dashboard localhost
        ↓
Decisão humana
```

Claude será responsável por:

- interpretar entradas;
- organizar informações;
- identificar pendências;
- comparar produtos;
- preparar fichas operacionais;
- elaborar respostas;
- produzir análises.

Claude não será responsável por:

- executar compras;
- realizar pagamentos;
- preencher rastreios automaticamente;
- enviar mensagens sem aprovação;
- inventar dados ausentes;
- operar múltiplas identidades;
- utilizar navegadores anti-detect.

---

## 2\. Decisão arquitetural central

## 2.1 O Claude não será o banco de dados

Conversas são contexto temporário. Não são uma fonte confiável de persistência operacional.

A fonte de verdade será a pasta da operação:

```markdown
operations-console/
├── CLAUDE.md
├── README.md
├── config/
├── dados/
├── scripts/
├── relatorios/
├── sop/
├── logs/
├── backups/
└── .claude/
```

Cada cliente ou operador recebe uma cópia isolada:

```markdown
operacoes/
├── operacao-gabriel/
├── operacao-cliente-a/
└── operacao-cliente-b/
```

Regra:

```markdown
Uma pasta = uma operação = um conjunto isolado de dados.
```

Não usar uma conversa Claude como tenant. Não compartilhar a mesma pasta `dados/` entre operadores.

## 2.2 Como o usuário utilizará

O operador abre o terminal dentro da pasta e inicia o Claude Code.

Exemplos de comandos:

```markdown
/painel
/pedido
/auditor
/comparar
/fechar-dia
/responder
/fornecedor
```

O comando `/painel` inicia a aplicação e devolve algo como:

```markdown
Dashboard disponível em:
http://127.0.0.1:8765
```

O servidor deve escutar apenas em `127.0.0.1` por padrão.

---

## 3\. Resultado esperado do MVP

O operador conseguirá:

1. Registrar uma nova venda.
2. Calcular automaticamente custo, taxas, lucro, margem e ROI.
3. Receber uma ficha de compra pronta.
4. Saber quais pedidos estão próximos do prazo.
5. Controlar pedidos sem rastreio real.
6. Visualizar fila operacional por prioridade.
7. Fechar o dia com indicadores financeiros.
8. Comparar produtos Amazon × fornecedor.
9. Preparar respostas de atendimento.
10. Consultar histórico e trilha de auditoria.
11. Abrir tudo em uma dashboard local.
12. Exportar relatórios em HTML, CSV, XLSX e Markdown.

A execução de compra continua humana.

---

## 4\. Escopo permanente

## 4.1 Dentro do escopo

- importação de pedidos;
- cadastro de pedidos;
- catálogo Amazon × fornecedor;
- cálculo financeiro;
- controle de prazo;
- ficha de compra;
- auditoria de pendências;
- comparação de produtos;
- análise de fornecedores;
- preparação de mensagens;
- relatórios;
- dashboard;
- histórico;
- backups;
- integrações oficiais futuras.

## 4.2 Fora do escopo

O sistema nunca deve:

- criar rastreio provisório ou falso;
- inventar código de transportadora;
- criar ou gerenciar contas descartáveis;
- integrar Dolphin Anty, 1Browser ou anti-detect;
- escolher ou rotacionar contas;
- automatizar cupons em volume;
- executar checkout;
- realizar pagamento;
- enviar mensagens sem confirmação;
- ocultar a origem do fornecimento;
- gravar estimativa como valor comprovado;
- modificar silenciosamente parâmetros financeiros.

## 4.3 Substituições seguras

| Problema | Implementação proibida | Solução do sistema |
| --- | --- | --- |
| Prazo de despacho | Rastreio provisório | Alerta antecipado e fila crítica |
| Trabalho repetitivo | Compra automática | Ficha pronta com link e dados |
| Erro de margem | Alteração automática de preço | Simulação e aprovação humana |
| Mineração demorada | Publicação automática | Ranking de candidatos |
| Atendimento repetitivo | Envio automático irrestrito | Rascunho com aprovação |
| Escala logística | Contas adicionais | Fornecedor homologado |

---

## 5\. Arquitetura técnica recomendada

## 5.1 Stack do MVP

### Backend local

- Python 3.12
- FastAPI
- Uvicorn
- Pydantic
- Pandas
- Jinja2

### Interface

- HTML server-side
- HTMX para ações locais
- Tailwind CSS compilado ou CSS local
- Chart.js para gráficos
- JavaScript mínimo

### Dados

- CSV como fonte operacional inicial
- YAML para parâmetros
- JSONL para eventos e auditoria
- XLSX apenas para importação e exportação
- Git para versionamento estrutural
- backups locais compactados

### Testes

- pytest
- Ruff
- mypy
- testes de contrato dos CSV
- testes de segurança da renderização

## 5.2 Por que não iniciar com Next.js

O primeiro objetivo é matar trabalho operacional, não construir um SaaS.

FastAPI + HTML local oferece:

- menos dependências;
- instalação mais simples;
- inicialização com um comando;
- acesso direto aos arquivos;
- menor superfície de falha;
- fácil operação pelo Claude Code.

Next.js, autenticação e banco remoto entram apenas quando existir:

- segundo operador;
- acesso remoto;
- celular;
- múltiplos clientes;
- necessidade de disponibilidade contínua.

---

## 6\. Estrutura do repositório

```markdown
operations-console/
│
├── CLAUDE.md
├── README.md
├── pyproject.toml
├── .env.example
├── .gitignore
│
├── config/
│   ├── parametros.yaml
│   ├── categorias.yaml
│   └── regras.yaml
│
├── dados/
│   ├── pedidos.csv
│   ├── catalogo.csv
│   ├── fornecedores.csv
│   ├── candidatos.csv
│   ├── mensagens.csv
│   └── correcoes.csv
│
├── app/
│   ├── main.py
│   ├── dependencies.py
│   ├── routes/
│   ├── services/
│   ├── schemas/
│   ├── templates/
│   └── static/
│
├── agents/
│   ├── router.md
│   ├── intake.md
│   ├── scout.md
│   ├── pricing.md
│   ├── finance.md
│   ├── auditor.md
│   ├── support.md
│   ├── supplier.md
│   └── qa.md
│
├── scripts/
│   ├── calculo.py
│   ├── importar.py
│   ├── validar_dados.py
│   ├── backup.py
│   └── iniciar_painel.py
│
├── sop/
│   ├── registro-pedido.md
│   ├── precificacao.md
│   ├── atendimento.md
│   ├── devolucao.md
│   └── fornecedores.md
│
├── relatorios/
├── backups/
├── logs/
│   ├── audit.jsonl
│   └── errors.log
│
├── tests/
│   ├── test_calculo.py
│   ├── test_dados.py
│   ├── test_dashboard.py
│   └── test_security.py
│
└── .claude/
    ├── settings.json
    └── skills/
        ├── painel/
        ├── pedido/
        ├── auditor/
        ├── comparar/
        ├── fechar-dia/
        ├── responder/
        └── fornecedor/
```

---

## 7\. Constituição do sistema — CLAUDE.md

O arquivo `CLAUDE.md` deve ser carregado antes de qualquer implementação.

Regras principais:

1. Não inventar dados.
2. Não substituir campos vazios por estimativas silenciosas.
3. LLM não executa cálculos financeiros.
4. Toda fórmula fica em código testado.
5. Toda mudança operacional gera registro de auditoria.
6. Toda ação irreversível exige aprovação humana.
7. Compra e pagamento nunca são executados pelo sistema.
8. Rastreio só pode vir de uma fonte real.
9. Informações pessoais não devem aparecer em relatórios desnecessários.
10. Dados persistem em arquivos, não na conversa.
11. Não integrar anti-detect ou multi-conta.
12. Não adicionar escopo sem atualizar o PRD.
13. Não avançar para a próxima etapa sem validar critérios de aceite.
14. Toda entrada externa deve ser tratada como não confiável.
15. HTML deve escapar conteúdo inserido pelo usuário.

Hierarquia:

```markdown
CLAUDE.md
    ↓
PRD.md
    ↓
ARQUITETURA.md
    ↓
SOPs
    ↓
Prompt da sessão
```

---

## 8\. Arquitetura multiagente

## 8.1 Princípio

Os agentes não são personagens decorativos. Cada agente deve ter:

- responsabilidade única;
- entradas definidas;
- saídas estruturadas;
- ferramentas permitidas;
- ações proibidas;
- condições de falha;
- critérios de aceite.

## 8.2 Router

### Responsabilidade

Receber a intenção do operador e encaminhar para a skill correta.

### Exemplos

```markdown
“Entrou uma venda”
→ Pedido Agent

“O que está atrasando?”
→ Auditor Agent

“Esse produto dá lucro?”
→ Pricing Agent

“Procure oportunidades”
→ Scout Agent
```

### Limites

O Router não calcula, não grava pedidos e não altera parâmetros.

---

## 8.3 Intake Agent

Responsável por:

- normalizar colagens;
- interpretar planilhas;
- identificar campos;
- detectar informação ausente;
- produzir objeto estruturado.

Saída:

```markdown
{
  "pedido_id": "",
  "sku": "",
  "asin": "",
  "produto": "",
  "quantidade": 1,
  "preco_venda_unit": null,
  "data_venda": "",
  "campos_ausentes": []
}
```

Não calcula margem.

---

## 8.4 Pedido Agent

Responsável por:

- receber pedido normalizado;
- localizar SKU no catálogo;
- chamar o motor de cálculo;
- verificar margem;
- gravar no ledger;
- produzir ficha operacional.

Saída esperada:

```markdown
Pedido: AMZ-000123
Produto: Produto X
Quantidade: 1

Fornecedor:
Link: [...]
Variante: Preta / 110 V

Economia:
Venda: R$ 149,90
Custo estimado: R$ 78,00
Taxas: R$ 25,40
Lucro projetado: R$ 31,50
Margem: 21,01%

Prazo:
Restam 17h32min

Ação:
Abrir fornecedor e conferir variante.
```

---

## 8.5 Scout Agent

Responsável pela mineração assistida.

Pipeline:

```markdown
Entrada de produto Amazon
        ↓
Normalização de título
        ↓
Extração de atributos
        ↓
Busca em fonte permitida
        ↓
Geração de possíveis correspondências
        ↓
Comparação de identidade
        ↓
Cálculo financeiro
        ↓
Análise de risco
        ↓
Ranking
```

Critérios de identidade:

- marca;
- modelo;
- material;
- dimensões;
- quantidade;
- cor;
- voltagem;
- imagens;
- acessórios;
- GTIN/EAN quando disponível.

O título parecido não prova que os produtos são iguais.

Saída:

```markdown
{
  "amazon": {},
  "fornecedor": {},
  "identidade": {
    "score": 0,
    "atributos_confirmados": [],
    "divergencias": [],
    "confianca": "baixa"
  },
  "economia": {},
  "risco": {},
  "decisao_sugerida": "revisar"
}
```

O Scout nunca anuncia e nunca compra.

---

## 8.6 Pricing Agent

Responsável por:

- simular cenários;
- calcular preço mínimo;
- calcular preço alvo;
- apontar margem insuficiente;
- mostrar impacto de taxas e custos.

O agente chama `scripts/calculo.py`. Não realiza aritmética livre pelo LLM.

---

## 8.7 Finance Agent

Responsável por:

- consolidar vendas;
- custos;
- taxas;
- lucro;
- margem;
- ROI;
- devoluções;
- desempenho por SKU.

Não altera dados originais.

Correções devem ser registradas como eventos novos.

---

## 8.8 Auditor Agent

Responsável pela fila de risco.

Prioridades:

1. Prazo de despacho inferior a 6 horas.
2. Pedido sem custo informado.
3. Margem negativa.
4. Pedido despachado sem rastreio real há mais de 48 horas.
5. Pedido sem fornecedor associado.
6. Produto com custo acima do teto.
7. Campo financeiro incompleto.
8. Divergência de variante.
9. Pedido sem atualização recente.

Formato:

```markdown
CRÍTICO — 2 pedidos
ATENÇÃO — 4 pedidos
INFORMATIVO — 3 itens
```

Cada alerta deve incluir:

- problema;
- evidência;
- tempo restante;
- impacto;
- ação recomendada.

---

## 8.9 Support Agent

Responsável por elaborar rascunhos de atendimento usando:

- SOP;
- status real do pedido;
- rastreio real;
- política definida;
- histórico necessário.

Nunca deve afirmar:

```markdown
“Seu pedido foi enviado”
```

quando `data_despacho` estiver vazia.

Toda resposta permanece em estado:

```markdown
draft
```

até aprovação humana.

---

## 8.10 Supplier Agent

Responsável por avaliar fornecedores.

Indicadores:

- preço médio;
- prazo de postagem;
- cancelamentos;
- divergência de produto;
- qualidade;
- rastreio;
- capacidade de despachar em nome da loja;
- documentação;
- estabilidade de estoque.

Objetivo estratégico:

```markdown
Transformar marketplaces em radar de oportunidades
e fornecedores homologados em infraestrutura operacional.
```

---

## 8.11 QA Guardian

Responsável por revisar saídas dos demais agentes.

Verifica:

- presença de dados inventados;
- cálculo vindo do LLM;
- ausência de fonte;
- ação fora do escopo;
- mensagem inconsistente;
- dados pessoais desnecessários;
- baixa confiança tratada como certeza.

Pode reprovar a saída, mas não executar correções irreversíveis.

---

## 9\. Modelo de dados

## 9.1 pedidos.csv

Campos mínimos:

```markdown
event_id
event_type
pedido_id
marketplace
data_venda
limite_despacho
asin
sku
produto
quantidade
preco_venda_unit
receita_bruta
custo_fornecedor
frete_fornecedor
desconto_aplicado
comissao_amazon
outras_taxas
imposto
reserva_devolucao
custo_total
lucro_liquido
margem_pct
roi_pct
fornecedor_id
status
data_compra
data_despacho
rastreio
transportadora
fonte_rastreio
created_at
created_by
observacao
```

## 9.2 catalogo.csv

```markdown
sku
asin
titulo_amazon
categoria
marca
modelo
variante
fornecedor_id
fornecedor_url
custo_referencia
frete_referencia
preco_minimo
margem_alvo
ativo
updated_at
```

## 9.3 fornecedores.csv

```markdown
fornecedor_id
nome
plataforma
url
despacha_em_nome_da_loja
prazo_medio_dias
cancelamento_pct
divergencia_pct
avaliacao_interna
status
observacoes
```

## 9.4 candidatos.csv

```markdown
candidate_id
asin
amazon_title
amazon_price
supplier_title
supplier_url
supplier_price_min
supplier_price_max
identity_score
estimated_profit
estimated_margin
risk_ip
risk_variant
data_quality
status
rejection_reason
created_at
```

## 9.5 Procedência

Campos calculados ou obtidos externamente devem registrar origem:

```markdown
comprovado
informado_operador
calculado
estimado
ausente
```

Estimativa pode existir em `candidatos.csv`.

Em `pedidos.csv`, custo real deve permanecer vazio até ser informado ou comprovado.

---

## 10\. Motor financeiro

As fórmulas devem existir exclusivamente em `scripts/calculo.py`.

```markdown
receita_bruta =
    preco_venda_unit × quantidade

imposto =
    receita_bruta × imposto_pct

reserva_devolucao =
    receita_bruta × reserva_devolucao_pct

custo_total =
    custo_fornecedor
    + frete_fornecedor
    - desconto_aplicado
    + comissao_amazon
    + outras_taxas
    + imposto
    + reserva_devolucao

lucro_liquido =
    receita_bruta - custo_total

margem_pct =
    lucro_liquido / receita_bruta × 100

roi_pct =
    lucro_liquido /
    (custo_fornecedor + frete_fornecedor) × 100
```

Regras:

- divisão por zero deve retornar erro tratado;
- campo ausente não vira zero automaticamente;
- comissão desconhecida gera cálculo incompleto;
- margem abaixo do limite exige confirmação;
- valores monetários usam Decimal;
- arredondamento em duas casas apenas na apresentação.

---

## 11\. Dashboard operacional

## 11.1 Navegação

```markdown
Visão Geral
Pedidos
Fila Operacional
Produtos
Scout
Financeiro
Fornecedores
Atendimento
Auditoria
Configurações
```

## 11.2 Home — quatro linhas executivas

### Prazo

```markdown
2 pedidos vencem em menos de 6 horas
```

### Cliente

```markdown
3 pedidos aguardam rastreio real
```

### Dinheiro

```markdown
Lucro hoje: R$ 684,20
Margem média: 18,4%
```

### Próxima ação

```markdown
Conferir pedido AMZ-00123 antes das 17h40
```

## 11.3 Fila operacional

Colunas:

- prioridade;
- tempo restante;
- pedido;
- produto;
- status;
- margem;
- pendência;
- próxima ação.

Filtros:

- crítico;
- hoje;
- sem custo;
- sem fornecedor;
- sem rastreio;
- margem negativa;
- concluído.

## 11.4 Drawer de pedido

Ao selecionar um pedido:

### Dados da venda

- pedido;
- produto;
- quantidade;
- data;
- prazo.

### Ficha de compra

- fornecedor;
- link;
- variante;
- quantidade;
- custo máximo;
- endereço formatado;
- itens que devem ser conferidos.

### Economia

- receita;
- custo;
- taxas;
- lucro;
- margem;
- ROI.

### Eventos

- registrado;
- custo informado;
- compra confirmada;
- despacho confirmado;
- rastreio informado;
- concluído.

## 11.5 Scout

Exibe cartões:

```markdown
Amazon → Fornecedor
```

Cada cartão mostra:

- imagens;
- títulos;
- atributos;
- divergências;
- score de identidade;
- preço Amazon;
- faixa de custo;
- lucro estimado;
- margem estimada;
- risco;
- evidência.

Ações:

```markdown
Aprovar para catálogo
Solicitar revisão
Reprovar com motivo
```

Aprovar não publica anúncio.

## 11.6 Financeiro

KPIs:

- receita;
- lucro;
- margem;
- ROI;
- pedidos;
- ticket médio;
- custo médio;
- devoluções;
- SKUs negativos;
- produtos sem custo real.

Gráficos:

- lucro por dia;
- margem por SKU;
- receita × custo;
- top produtos;
- piores produtos;
- pedidos por status.

## 11.7 Atendimento

Apresenta:

- mensagem recebida;
- contexto operacional;
- resposta sugerida;
- fonte utilizada;
- botão copiar;
- estado aprovado/rejeitado.

Não envia diretamente no MVP.

## 11.8 Auditoria

Exibe:

- data;
- ator;
- agente;
- ação;
- arquivo;
- valor anterior;
- valor novo;
- motivo;
- resultado.

---

## 12\. Comandos Claude Code

## /setup-operacao

- valida dependências;
- cria arquivos ausentes;
- solicita parâmetros;
- não inventa valores;
- gera relatório de prontidão.

## /pedido

- recebe pedido;
- normaliza;
- localiza catálogo;
- calcula;
- grava;
- apresenta ficha.

## /auditor

- lê dados;
- identifica pendências;
- ordena riscos;
- não corrige automaticamente.

## /painel

- valida dados;
- inicia FastAPI/Uvicorn;
- abre ou informa localhost;
- não expõe servidor na rede externa.

## /comparar

- analisa produto Amazon;
- recebe ou busca candidatos permitidos;
- compara identidade;
- calcula economia;
- registra aprovados e reprovados.

## /fechar-dia

- consolida indicadores;
- compara com últimos sete dias;
- gera Markdown, HTML e XLSX;
- lista decisões pendentes.

## /responder

- recebe mensagem;
- consulta pedido e SOP;
- produz rascunho;
- não envia.

## /fornecedor

- analisa histórico;
- calcula indicadores;
- classifica fornecedor;
- lista evidências.

## /backup

- valida integridade;
- gera arquivo compactado;
- registra checksum;
- mantém últimas cópias configuradas.

---

## 13\. Segurança

## 13.1 Renderização

Todo conteúdo vindo de CSV, planilha, formulário ou operador deve ser escapado.

Obrigatório:

- escaping HTML;
- proteção contra XSS;
- CSP;
- validação de esquema;
- allowlist de protocolos;
- links apenas `https://` e `http://`;
- bloquear `javascript:`;
- bloquear HTML em títulos;
- não usar `innerHTML` com entrada externa.

## 13.2 Dados pessoais

- evitar mostrar endereço na home;
- endereço completo apenas dentro do pedido;
- não incluir PII em relatórios financeiros;
- não gravar PII em prompts ou memória permanente;
- mascarar dados em screenshots e logs;
- não enviar dados completos para modelo quando não forem necessários.

## 13.3 Arquivos

- escrita atômica;
- backup antes de migração;
- lock durante alteração;
- validação posterior à escrita;
- `.env` no `.gitignore`;
- nenhum segredo em log;
- nenhuma credencial no frontend.

---

## 14\. Parâmetros que precisam ser coletados

```markdown
moeda: BRL
timezone: America/Sao_Paulo
prazo_despacho_horas: 24

margem_minima_pct: PENDENTE
margem_alvo_pct: PENDENTE
imposto_pct: PENDENTE
reserva_devolucao_pct: PENDENTE

categorias_principais: []
comissao_por_categoria: {}

alerta_critico_horas: 6
alerta_rastreio_horas: 48
```

O sistema deve iniciar mesmo com parâmetros incompletos, mas bloquear cálculos dependentes e mostrar:

```markdown
Cálculo financeiro incompleto:
comissão da categoria não configurada.
```

---

## 15\. Ordem de desenvolvimento

## Fase 0 — Governança

Entregas:

- CLAUDE.md;
- PRD.md;
- README;
- estrutura;
- git;
- regras de segurança.

Aceite:

```markdown
Nenhum código funcional antes de os limites estarem documentados.
```

## Fase 1 — Contratos de dados

Entregas:

- schemas;
- CSVs vazios;
- validação;
- exemplos separados dos dados reais;
- importador de planilhas.

Aceite:

```markdown
Dados de demonstração nunca aparecem no ledger real.
```

## Fase 2 — Motor financeiro

Entregas:

- `calculo.py`;
- Decimal;
- validações;
- testes.

Aceite:

```markdown
Três cenários manuais coincidem com o código.
```

## Fase 3 — Pedido Agent

Entregas:

- skill `/pedido`;
- registro append-only;
- associação ao catálogo;
- ficha operacional.

Aceite:

```markdown
Dois pedidos registrados sem cálculo manual.
```

## Fase 4 — Auditor Agent

Entregas:

- regras;
- prioridades;
- countdown;
- alertas.

Aceite:

```markdown
Pedido com prazo inferior a seis horas aparece primeiro.
```

## Fase 5 — Dashboard

Entregas:

- servidor localhost;
- home;
- fila;
- pedido;
- financeiro básico;
- auditoria.

Aceite:

```markdown
/painel inicia o servidor e retorna uma URL funcional.
```

## Fase 6 — Fechamento

Entregas:

- `/fechar-dia`;
- relatórios;
- tendências;
- top e piores produtos.

## Fase 7 — Scout

Entregas:

- comparação estruturada;
- score de identidade;
- ranking;
- razões de reprovação.

## Fase 8 — Atendimento

Entregas:

- SOP;
- `/responder`;
- rascunho;
- validação de status real.

## Fase 9 — Fornecedores

Entregas:

- scorecard;
- histórico;
- homologação;
- recomendações.

## Fase 10 — Integrações oficiais

Somente depois do MVP estável:

- Amazon SP-API;
- APIs autorizadas de catálogo;
- SMTP;
- importações programadas.

---

## 16\. Testes obrigatórios

## Financeiro

- margem positiva;
- margem negativa;
- custo ausente;
- comissão ausente;
- quantidade maior que um;
- desconto maior que frete;
- divisão por zero.

## Dados

- CSV vazio;
- coluna ausente;
- duplicidade;
- caracteres especiais;
- vírgula decimal;
- planilha corrompida.

## Segurança

Entradas:

```markdown
<script>alert(1)</script>
```
```markdown
<img src=x onerror=alert(1)>
```
```markdown
javascript:alert(1)
```

Nenhuma pode executar no dashboard.

## Operação

- pedido crítico;
- pedido sem custo;
- pedido sem fornecedor;
- pedido sem rastreio;
- mensagem com status inconsistente;
- candidato com baixa confiança;
- correção append-only.

---

## 17\. Indicadores de sucesso

## Operacionais

- tempo de registro por pedido;
- tempo até identificar item crítico;
- pedidos sem custo;
- pedidos sem fornecedor;
- pedidos próximos do prazo;
- percentual de dados completos.

## Financeiros

- lucro líquido;
- margem média;
- ROI;
- ticket médio;
- lucro por SKU;
- produtos negativos;
- devoluções.

## Qualidade dos agentes

- saídas aceitas sem edição;
- reprovações do QA;
- informações ausentes corretamente detectadas;
- falsos positivos do Scout;
- divergências encontradas antes da compra.

---

## 18\. Cronograma estimado do MVP

| Etapa | Estimativa |
| --- | --- |
| Governança e estrutura | 0,5–1 dia |
| Dados e importadores | 1–2 dias |
| Motor financeiro | 1 dia |
| Pedido + ficha | 1–2 dias |
| Auditor | 1 dia |
| Dashboard localhost | 2–3 dias |
| Fechamento diário | 1 dia |
| Testes e segurança | 1–2 dias |
| **Total** | **8–13 dias úteis** |

O Scout completo deve ser tratado como módulo posterior, pois depende de dados, fontes e validação de identidade mais complexos.

---

## 19\. Definição de pronto do MVP

O MVP está pronto quando:

- `/painel` sobe localhost;
- pedido pode ser registrado;
- fórmulas passam nos testes;
- fila é ordenada por risco;
- ficha de compra aparece;
- margem incompleta é sinalizada;
- relatório diário é gerado;
- nenhum HTML externo executa;
- nenhum dado de teste aparece na operação real;
- nenhuma compra é executada pelo sistema;
- nenhum rastreio é inventado;
- logs e backups funcionam;
- operador não precisa editar código para usar o fluxo básico.

---

## 20\. Prompt 00 — Inicialização no Claude Code

Cole este prompt primeiro:

```markdown
Você atuará como Arquiteto Principal e Product Engineer do projeto
Operations Console.

Leia integralmente o PRD.md antes de modificar qualquer arquivo.

MISSÃO

Construir uma dashboard operacional local-first para uma operação Amazon
com fornecedores externos, alimentada por agentes Claude e utilizada através
do Claude Code.

O sistema deve:

- persistir dados em arquivos dentro da pasta do projeto;
- iniciar uma aplicação em localhost;
- oferecer comandos Claude Code como /pedido, /auditor e /painel;
- calcular custos, taxas, lucro, margem e ROI por código determinístico;
- preparar fichas operacionais;
- mostrar filas, riscos, pendências e indicadores;
- manter ações irreversíveis sob controle humano.

REGRAS INVIOLÁVEIS

- Não automatizar compras ou pagamentos.
- Não criar ou preencher rastreio que não seja real.
- Não criar ou gerenciar múltiplas contas.
- Não integrar navegadores anti-detect.
- Não enviar mensagens sem aprovação humana.
- Não inventar valores ausentes.
- Não usar a conversa como banco de dados.
- Não implementar cálculo financeiro dentro do LLM.
- Não adicionar escopo não solicitado.
- Não modificar arquivos antes de apresentar o diagnóstico inicial.

PRIMEIRA TAREFA

1. Inspecione todo o repositório.
2. Informe o que já existe.
3. Compare o estado atual com o PRD.
4. Liste lacunas, conflitos e riscos.
5. Proponha a árvore final de arquivos.
6. Crie um plano de execução dividido em commits pequenos.
7. Não implemente ainda.

FORMATO DA RESPOSTA

- Estado encontrado
- Lacunas
- Decisões técnicas
- Arquivos a criar ou alterar
- Ordem dos commits
- Critérios de aceite da Fase 0

Não avance além do planejamento nesta execução.
```

---

## 21\. Prompt 01 — Fundação

Executar somente após validar o diagnóstico:

```markdown
Implemente exclusivamente a Fase 0 do PRD.

OBJETIVO

Criar a fundação documental, estrutural e de segurança do projeto.

ENTREGAS

- CLAUDE.md
- README.md
- PRD.md preservado
- pyproject.toml
- .gitignore
- .env.example sem valores
- estrutura de diretórios
- config/parametros.yaml com campos PENDENTE
- arquivos CSV vazios com cabeçalhos
- logs/audit.jsonl vazio
- documentação de como iniciar o projeto

REGRAS

- Não criar dashboard ainda.
- Não implementar agentes ainda.
- Não instalar integrações externas.
- Não adicionar dados de demonstração nos arquivos reais.
- Exemplos devem ficar em tests/fixtures/.
- Validar encoding dos CSV.
- Registrar todas as decisões em docs/decisions/.

VALIDAÇÃO

- mostrar árvore criada;
- executar validadores;
- confirmar que nenhum segredo foi gravado;
- confirmar que dados reais e fixtures estão separados;
- gerar commit local: chore: initialize operations console foundation.

Pare após concluir e validar a Fase 0.
```

---

## 22\. Prompt 02 — Dados e cálculos

```markdown
Implemente as Fases 1 e 2 do PRD.

ENTREGAS

- schemas Pydantic para pedidos, catálogo, fornecedores e candidatos;
- leitor e escritor CSV com escrita atômica;
- append-only para pedidos;
- scripts/validar_dados.py;
- scripts/calculo.py usando Decimal;
- testes de fórmula;
- testes de campos ausentes;
- testes de duplicidade;
- relatório de validação.

REGRAS

- Campo ausente não pode virar zero silenciosamente.
- Comissão ausente deve produzir cálculo incompleto.
- LLM não participa dos cálculos.
- Correção gera evento novo.
- Não criar interface.
- Não importar dados reais ainda.

CRITÉRIO DE ACEITE

- todos os testes passam;
- três cálculos manuais estão documentados e coincidem;
- um pedido incompleto não é gravado como financeiramente completo;
- escrita interrompida não corrompe o CSV.

Gere commit:
feat: add validated data contracts and financial engine

Pare após a validação.
```

---

## 23\. Prompt 03 — Pedido e Auditor

```markdown
Implemente as skills /pedido e /auditor.

A skill /pedido deve:

- receber texto ou objeto;
- normalizar campos;
- localizar SKU no catálogo;
- chamar o motor financeiro;
- solicitar somente o campo indispensável que estiver faltando;
- gravar evento append-only;
- produzir ficha operacional;
- nunca comprar ou abrir checkout automaticamente.

A skill /auditor deve:

- ler pedidos;
- identificar prazos críticos;
- identificar custos ausentes;
- identificar margem negativa;
- identificar fornecedor ausente;
- identificar despacho sem rastreio real;
- ordenar por criticidade;
- produzir ação recomendada.

Crie testes end-to-end com fixtures.

CRITÉRIO DE ACEITE

- dois pedidos de teste são registrados;
- pedido crítico aparece primeiro;
- campos ausentes são mostrados;
- nenhuma informação é inventada.

Gere commit:
feat: add order intake and operational auditor

Pare após validar.
```

---

## 24\. Prompt 04 — Dashboard localhost

```markdown
Implemente a primeira versão da dashboard local.

STACK

- FastAPI
- Uvicorn
- Jinja2
- HTMX
- Chart.js
- CSS local

ROTAS

- /
- /pedidos
- /pedidos/{pedido_id}
- /fila
- /financeiro
- /auditoria
- /health

COMANDO

Criar /painel e scripts/iniciar_painel.py.

FUNCIONAMENTO

- validar dados antes de iniciar;
- usar 127.0.0.1 por padrão;
- encontrar porta livre a partir de 8765;
- devolver a URL;
- não abrir rede externa;
- mostrar estado vazio corretamente.

BLOCOS DA HOME

- Prazo
- Cliente
- Dinheiro
- Próxima ação
- Fila crítica
- Pendências
- Últimos eventos

SEGURANÇA

- escapar todo conteúdo;
- bloquear javascript: em links;
- aceitar apenas http e https;
- adicionar CSP;
- não utilizar innerHTML com dados externos;
- incluir testes anti-XSS.

CRITÉRIO DE ACEITE

- /painel inicia o servidor;
- /health responde;
- dashboard abre;
- fixture maliciosa aparece como texto;
- nenhum script é executado;
- dados de fixture não contaminam dados/.

Gere commit:
feat: add secure localhost operations dashboard

Pare após validar.
```

---

## 25\. Sequência posterior

Depois dos quatro prompts iniciais:

```markdown
Prompt 05 → Fechamento diário
Prompt 06 → Atendimento
Prompt 07 → Fornecedores
Prompt 08 → Scout e comparação
Prompt 09 → Importação das planilhas reais
Prompt 10 → Hardening e operação assistida
Prompt 11 → Integrações oficiais
```

Cada prompt deve:

1. implementar apenas uma fase;
2. executar testes;
3. atualizar documentação;
4. gerar commit próprio;
5. parar para revisão.

Nunca pedir ao Claude Code para construir tudo em uma única execução. Um prompt monolítico produz uma nave espacial com painel bonito e parafusos esquecidos.

O ponto de partida é o **Prompt 00**. Ele força o Claude Code a inspecionar o estado atual antes de sair construindo sobre suposições.