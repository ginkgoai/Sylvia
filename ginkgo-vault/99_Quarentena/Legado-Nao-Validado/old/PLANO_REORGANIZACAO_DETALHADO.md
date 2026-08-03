# 🧠 Plano Detalhado de Reorganização: Sistema Operacional Ginkgo

**Versão**: 1.0  
**Data**: 21 de Abril de 2026  
**Escopo**: Reorganização completa de `/home/ubuntu` em arquitetura Ginkgo AI Systems + Obsidian  
**Status**: ⏳ Aguardando aprovação para execução

---

## 📋 Sumário Executivo

Este plano transforma seu computador em um **Data Center Cognitivo** com separação absoluta entre vida pessoal e operações Ginkgo. A reorganização é **não-destrutiva** (nenhum arquivo será deletado) e será executada apenas após sua aprovação explícita.

| Métrica | Valor |
|---------|-------|
| Total de Itens | 492 |
| Itens GINKGO_CORE | 56 (95% confiança) |
| Itens PESSOAL | 3 (90% confiança) |
| Itens SISTEMA | 423 (95% confiança) |
| Itens AMBÍGUOS | 10 (requerem decisão manual) |
| Universos Principais | 4 + 1 temporária |

---

## 🏗️ Arquitetura Final Proposta

### Estrutura de Raiz

```
/home/ubuntu/
├── 00_SYSTEM/                          # Kernel do cérebro
│   ├── Templates/
│   ├── Prompts/
│   ├── Frameworks/
│   ├── Configs/
│   ├── Snippets/
│   └── Naming_Conventions/
│
├── 01_PESSOAL/                         # Universo pessoal isolado
│   ├── Documentos/
│   │   └── Contexto_Arquitetura/       # (upload/ será movido aqui)
│   ├── Estudos/
│   ├── Financas/
│   ├── Projetos_Criativos/
│   └── Downloads_Temporarios/          # (Downloads/ será movido aqui)
│
├── 02_GINKGO_AI_SYSTEMS/               # Core executivo
│   ├── 01_INTERNAL_PROJECTS/           # R&D e incubação
│   ├── 02_PRODUCTS/                    # Produtos digitais
│   ├── 03_SAAS/                        # Máquinas de renda
│   ├── 04_AGENTS/                      # Entidades autônomas
│   │   └── Skills/                     # (skills/ será movido aqui)
│   ├── 05_DESIGN/                      # Linguagem visual
│   ├── 06_DOCUMENTATION/               # Memória de longo prazo
│   ├── 07_MEDIA/                       # Mídia organizada
│   │   ├── Raw/
│   │   ├── Edited/
│   │   └── Final/
│   ├── 08_SITES/                       # Agentes silenciosos 24/7
│   └── 09_AUTOMATIONS/                 # Sistema nervoso
│       ├── n8n/
│       ├── Make/
│       ├── Zapier/
│       └── Scripts/
│
├── 99_ARCHIVE/                         # Cemitério de aprendizado
│   └── [Projetos finalizados/congelados]
│
├── 00_REVISAO_MANUAL/                  # Pasta temporária (NOVO)
│   └── [Itens ambíguos aguardando decisão]
│
└── [Arquivos de Sistema - Mantidos na Raiz]
    ├── .bashrc, .profile, .zshrc       # Configuração shell
    ├── .browser_data_dir/              # Cache Chromium
    ├── .env, .user_env                 # Variáveis de ambiente
    ├── .logs/                          # Logs do sistema
    ├── .secrets/                       # Tokens sensíveis
    └── [Outros arquivos de SO]
```

---

## 📊 Classificação Semântica Completa

### 1. GINKGO_CORE (56 itens | Confiança: 95%)

**Destino**: `02_GINKGO_AI_SYSTEMS/04_AGENTS/Skills/`

**Conteúdo**:
- `/home/ubuntu/skills/` e todo seu conteúdo
  - `bgm-prompter/` - Skill para geração de música
  - `canva-mcp/` - Integração Canva
  - `excel-generator/` - Gerador de planilhas
  - `github-gem-seeker/` - Busca em GitHub
  - `gws-best-practices/` - Google Workspace
  - `internet-skill-finder/` - Descoberta de skills
  - `meta-ads-analyzer/` - Análise de anúncios Meta
  - `n8n-manus-api/` - API n8n
  - `similarweb-analytics/` - Análise SimilarWeb
  - `skill-creator/` - Criador de skills

**Ação**: ✅ Mover para `02_GINKGO_AI_SYSTEMS/04_AGENTS/Skills/`

---

### 2. PESSOAL (3 itens | Confiança: 90%)

**Destino**: `01_PESSOAL/`

| Item | Origem | Destino | Motivo |
|------|--------|---------|--------|
| `pasted_content.txt` | `/upload/` | `01_PESSOAL/Documentos/Contexto_Arquitetura/` | Contexto arquitetural pessoal |
| `pasted_content_2.txt` | `/upload/` | `01_PESSOAL/Documentos/Contexto_Arquitetura/` | Mapa mental do sistema |
| `.tmp/` | `/Downloads/` | `01_PESSOAL/Downloads_Temporarios/` | Pasta temporária |

**Ação**: ✅ Mover para `01_PESSOAL/`

---

### 3. SISTEMA (423 itens | Confiança: 95%)

**Destino**: **[MANTER NA RAIZ - NÃO MOVER]**

**Conteúdo**:
- `.browser_data_dir/` - Cache e dados Chromium
- `.logs/` - Logs do sistema
- `.secrets/` - Tokens de autenticação
- `.config/`, `.cache/`, `.local/` - Configurações do SO
- Arquivos de shell (`.bashrc`, `.profile`, `.zshrc`)
- Variáveis de ambiente (`.env`, `.user_env`)

**Justificativa**: Mover estes arquivos pode quebrar referências de caminhos em scripts, variáveis de ambiente e sessões do navegador.

**Ação**: ⛔ NÃO MOVER

---

### 4. MEDIA (0 itens | Confiança: N/A)

**Destino**: `02_GINKGO_AI_SYSTEMS/07_MEDIA/`

**Status**: Nenhum arquivo de mídia encontrado atualmente.

**Ação**: Estrutura criada, aguardando conteúdo futuro.

---

### 5. AMBÍGUO (10 itens | Confiança: 0-40%)

**Destino**: `00_REVISAO_MANUAL/` (Pasta Temporária)

| Item | Tipo | Tamanho | Confiança | Recomendação |
|------|------|---------|-----------|--------------|
| `.bash_logout` | File | 220B | 0% | ⛔ MANTER NA RAIZ (Shell config) |
| `.bashrc` | File | 4.2KB | 0% | ⛔ MANTER NA RAIZ (Shell config) |
| `.gdrive-rclone.ini` | File | 395B | 0% | ⛔ MANTER NA RAIZ (Config crítica) |
| `.profile` | File | 807B | 0% | ⛔ MANTER NA RAIZ (Shell config) |
| `.user_env` | File | 18.7KB | 20% | ⛔ MANTER NA RAIZ (Env vars) |
| `.zshrc` | File | 218B | 0% | ⛔ MANTER NA RAIZ (Shell config) |
| `Downloads` | Dir | N/A | 40% | ✅ MOVER para `01_PESSOAL/Downloads_Temporarios/` |
| `sandbox.txt` | File | 19B | 30% | ❓ REVISAR (Propósito desconhecido) |
| `skills` | Dir | N/A | 10% | ✅ MOVER para `02_GINKGO_AI_SYSTEMS/04_AGENTS/Skills/` |
| `upload` | Dir | N/A | 40% | ✅ MOVER para `01_PESSOAL/Documentos/Contexto_Arquitetura/` |

---

## ⚠️ Análise de Riscos

### Risco Alto (R001, R002)

| ID | Item | Risco | Mitigação | Ação |
|----|------|-------|-----------|------|
| **R001** | `.bashrc`, `.profile`, `.zshrc` | Mover pode quebrar shell do usuário | MANTER NA RAIZ | ⛔ NÃO MOVER |
| **R002** | `.browser_data_dir/` | Mover pode quebrar Chromium e perder dados de sessão | MANTER NA RAIZ | ⛔ NÃO MOVER |

### Risco Médio (R003, R004)

| ID | Item | Risco | Mitigação | Ação |
|----|------|-------|-----------|------|
| **R003** | `.logs/` | Logs do sistema podem referenciar caminhos absolutos | MANTER NA RAIZ | ⛔ NÃO MOVER |
| **R004** | `.secrets/` | Tokens sensíveis podem quebrar autenticação | MANTER NA RAIZ | ⛔ NÃO MOVER |

### Risco Baixo (R005, R006)

| ID | Item | Risco | Mitigação | Ação |
|----|------|-------|-----------|------|
| **R005** | `.env` | Scripts podem referenciar `/home/ubuntu/.env` | MANTER NA RAIZ | ⛔ NÃO MOVER |
| **R006** | `terminal_full_output/` | Propósito desconhecido | Revisar manualmente | ❓ REVISÃO MANUAL |

---

## 🔄 Conflitos Potenciais e Resoluções

### C001: Ambiguidade de Diretórios Raiz

**Itens**: `Downloads/`, `upload/`  
**Problema**: Ambos são diretórios raiz sem extensão. Classificação baixa (40%).  
**Resolução Proposta**:
- `Downloads/` → `01_PESSOAL/Downloads_Temporarios/`
- `upload/` → `01_PESSOAL/Documentos/Contexto_Arquitetura/`

**Status**: ✅ Recomendação clara

---

### C002: Confiança Baixa em Diretório com Conteúdo Claro

**Item**: `skills/`  
**Problema**: Diretório raiz tem confiança baixa (10%), mas análise de conteúdo revela 95% de confiança GINKGO_CORE.  
**Resolução Proposta**: Mover para `02_GINKGO_AI_SYSTEMS/04_AGENTS/Skills/`  
**Status**: ✅ Recomendação clara

---

### C003: Arquivo Genérico sem Contexto

**Item**: `sandbox.txt`  
**Problema**: Arquivo de texto genérico (19B). Propósito desconhecido.  
**Resolução Proposta**: Mover para `00_REVISAO_MANUAL/` para você decidir  
**Status**: ❓ Requer sua decisão

---

### C004: Dependência de Configuração

**Itens**: `.env`, `.user_env`, `.gdrive-rclone.ini`  
**Problema**: Arquivos de configuração que podem ser referenciados por scripts em caminhos absolutos.  
**Resolução Proposta**: MANTER NA RAIZ  
**Status**: ✅ Recomendação clara

---

## 📋 Plano de Execução (Não Iniciado)

### Fase 1: Preparação (Pré-Execução)

1. ✅ Análise completa do sistema
2. ✅ Classificação semântica
3. ✅ Identificação de riscos
4. ⏳ **SUA APROVAÇÃO EXPLÍCITA** (Aguardando)

### Fase 2: Criação de Estrutura

Quando aprovado, executarei:

1. Criar estrutura de diretórios vazios
2. Gerar log de todas as operações
3. Criar backups de referência

### Fase 3: Movimentação de Arquivos

1. Mover `skills/` → `02_GINKGO_AI_SYSTEMS/04_AGENTS/Skills/`
2. Mover `upload/` → `01_PESSOAL/Documentos/Contexto_Arquitetura/`
3. Mover `Downloads/` → `01_PESSOAL/Downloads_Temporarios/`
4. Mover `sandbox.txt` → `00_REVISAO_MANUAL/` (se você confirmar)

### Fase 4: Validação

1. Verificar integridade de todos os arquivos
2. Gerar relatório final de movimentações
3. Documentar qualquer anomalia

---

## 🎯 Decisões Requeridas de Você

Antes de prosseguir, confirme:

### ✅ Decisão 1: Arquivos de Sistema

**Pergunta**: Concordo em manter na raiz os seguintes arquivos de sistema?

- `.bashrc`, `.profile`, `.zshrc`
- `.browser_data_dir/`
- `.env`, `.user_env`
- `.logs/`, `.secrets/`
- `.gdrive-rclone.ini`

**Opções**: SIM / NÃO / REVISAR

---

### ✅ Decisão 2: Diretórios Pessoais

**Pergunta**: Concordo em mover para `01_PESSOAL/`?

- `Downloads/` → `01_PESSOAL/Downloads_Temporarios/`
- `upload/` → `01_PESSOAL/Documentos/Contexto_Arquitetura/`

**Opções**: SIM / NÃO / REVISAR

---

### ✅ Decisão 3: Skills para Ginkgo

**Pergunta**: Concordo em mover `skills/` para `02_GINKGO_AI_SYSTEMS/04_AGENTS/Skills/`?

**Opções**: SIM / NÃO / REVISAR

---

### ✅ Decisão 4: Arquivo Ambíguo

**Pergunta**: O que fazer com `sandbox.txt`?

**Opções**:
- A) Mover para `00_REVISAO_MANUAL/`
- B) Manter na raiz
- C) Deletar
- D) Outro

---

### ✅ Decisão 5: Diretório Desconhecido

**Pergunta**: Encontrei um diretório `terminal_full_output/`. Devo:

**Opções**:
- A) Mover para `00_REVISAO_MANUAL/`
- B) Manter na raiz
- C) Deletar
- D) Outro

---

## 📝 Próximos Passos

1. **Revise este plano** em detalhes
2. **Responda as 5 decisões** acima
3. **Aprove explicitamente** ou solicite ajustes
4. Após aprovação, executarei a reorganização automática

---

## 📌 Notas Importantes

- **Nenhum arquivo será deletado** sem sua confirmação explícita
- **Nenhuma movimentação será executada** sem sua aprovação
- **Todos os arquivos serão preservados** em suas novas localizações
- **Um log detalhado** será gerado durante a execução
- **Você pode reverter** qualquer movimentação manualmente

---

**Aguardando sua aprovação para prosseguir! 🚀**
