<#
.SYNOPSIS
Script para criar a arquitetura Ginkgo AI Systems no OneDrive local.

.DESCRIPTION
Este script cria a estrutura completa de pastas, templates e documentação
da Ginkgo AI Systems no diretório "Administração Interna" do OneDrive.
Ele é seguro e não sobrescreve arquivos existentes.

.AUTHOR
Manus AI - Arquiteto de Sistemas Digitais
#>

# Definir o caminho base
$BasePath = "$env:USERPROFILE\OneDrive\Área de Trabalho\G-Tech\Administração Interna"

Write-Host "=======================================================" -ForegroundColor Cyan
Write-Host "🚀 INICIANDO CRIAÇÃO DA ARQUITETURA GINKGO AI SYSTEMS" -ForegroundColor Cyan
Write-Host "=======================================================" -ForegroundColor Cyan
Write-Host "Caminho alvo: $BasePath" -ForegroundColor Yellow
Write-Host ""

# Verificar se o caminho base existe
if (-not (Test-Path -Path $BasePath)) {
    Write-Host "⚠️ O caminho base não foi encontrado. Criando..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Force -Path $BasePath | Out-Null
}

# Função auxiliar para criar diretórios
function Create-Dir {
    param([string]$Path)
    $FullPath = Join-Path -Path $BasePath -ChildPath $Path
    if (-not (Test-Path -Path $FullPath)) {
        New-Item -ItemType Directory -Force -Path $FullPath | Out-Null
        Write-Host "✅ Criado: $Path" -ForegroundColor Green
    } else {
        Write-Host "⏭️ Já existe: $Path" -ForegroundColor DarkGray
    }
}

# Função auxiliar para criar arquivos com conteúdo
function Create-File {
    param([string]$Path, [string]$Content)
    $FullPath = Join-Path -Path $BasePath -ChildPath $Path
    
    # Garantir que o diretório pai existe
    $ParentDir = Split-Path -Path $FullPath -Parent
    if (-not (Test-Path -Path $ParentDir)) {
        New-Item -ItemType Directory -Force -Path $ParentDir | Out-Null
    }
    
    if (-not (Test-Path -Path $FullPath)) {
        Set-Content -Path $FullPath -Value $Content -Encoding UTF8
        Write-Host "📄 Arquivo criado: $Path" -ForegroundColor Green
    } else {
        Write-Host "⏭️ Arquivo já existe: $Path" -ForegroundColor DarkGray
    }
}

# ==========================================
# 1. CRIAR ESTRUTURA DE DIRETÓRIOS
# ==========================================
Write-Host "`n[1/3] Criando estrutura de diretórios..." -ForegroundColor Cyan

$Directories = @(
    "00_SYSTEM\Templates",
    "02_GINKGO_AI_SYSTEMS\01_INTERNAL_PROJECTS",
    "02_GINKGO_AI_SYSTEMS\02_PRODUCTS",
    "02_GINKGO_AI_SYSTEMS\03_SAAS",
    "02_GINKGO_AI_SYSTEMS\04_AGENTS",
    "02_GINKGO_AI_SYSTEMS\05_DESIGN",
    "02_GINKGO_AI_SYSTEMS\06_DOCUMENTATION",
    "02_GINKGO_AI_SYSTEMS\07_MEDIA\Raw",
    "02_GINKGO_AI_SYSTEMS\07_MEDIA\Edited",
    "02_GINKGO_AI_SYSTEMS\07_MEDIA\Final",
    "02_GINKGO_AI_SYSTEMS\08_SITES",
    "02_GINKGO_AI_SYSTEMS\09_AUTOMATIONS\n8n",
    "02_GINKGO_AI_SYSTEMS\09_AUTOMATIONS\Make",
    "02_GINKGO_AI_SYSTEMS\09_AUTOMATIONS\Zapier",
    "02_GINKGO_AI_SYSTEMS\09_AUTOMATIONS\Scripts"
)

foreach ($Dir in $Directories) {
    Create-Dir -Path $Dir
}

# ==========================================
# 2. CRIAR DOCUMENTAÇÃO BASE
# ==========================================
Write-Host "`n[2/3] Criando documentação base..." -ForegroundColor Cyan

$NamingConventions = @"
# 🏷️ Convenções de Nomenclatura (Naming Conventions)

## 1. Produtos e Serviços
- **Regra Geral**: Todos os produtos do ecossistema Ginkgo devem usar a nomenclatura "leaf by ginkgo".
- **Nomes Obsoletos**: "wave" e "pyre" não devem mais ser utilizados.

## 2. Diretórios e Arquivos
- **Pastas Principais**: UPPERCASE com underscore (ex: `00_SYSTEM`, `01_PESSOAL`).
- **Subpastas**: PascalCase com underscore (ex: `Internal_Projects`, `Design_Systems`).
- **Arquivos Markdown**: PascalCase (ex: `Project_Name.md`, `Meeting_Notes.md`).

## 3. Agentes
- **Nomes**: Nomes próprios ou descritivos curtos (ex: `Brann`, `Nyra`).
- **Tags**: `#agent/sales`, `#agent/ops`, `#agent/engineering`.
"@

$OperatingPrinciples = @"
# ⚙️ Princípios Operacionais (Operating Principles)

## 1. Colaboração
- **Modelo Copiloto Operador**: O agente de IA (Manus/Ginkgo) atua como líder, ditando regras e passos. O usuário (Gabriel) executa tarefas que o agente não pode realizar diretamente.

## 2. Estrutura Operacional Core
- **Tríade**: Manus/Ginkgo + API "alfred" + Agente "Brann". Esta é a estrutura central de gestão do negócio.

## 3. Integração de Ferramentas
- **Nativas vs Externas**: Priorizar ferramentas nativas do Manus em detrimento de externas (ex: substituir SerpAPI por ferramentas nativas).
- **Banco de Dados**: Supabase é o banco de dados primário para os dados da empresa.

## 4. Fluxo de Desenvolvimento
- **Organização Primeiro**: Todo repositório e ambiente de desenvolvimento deve ser completamente organizado e confirmado antes de iniciar a codificação passo a passo.
"@

Create-File -Path "00_SYSTEM\Naming_Conventions.md" -Content $NamingConventions
Create-File -Path "00_SYSTEM\Operating_Principles.md" -Content $OperatingPrinciples

# ==========================================
# 3. CRIAR TEMPLATES
# ==========================================
Write-Host "`n[3/3] Criando templates..." -ForegroundColor Cyan

$TemplateProject = @"
# 📝 Template de Projeto (R&D)

## 1. Visão Geral
- **Nome do Projeto**: [Nome]
- **Status**: [Ideação | Em Andamento | Congelado | Concluído]
- **Data de Início**: [Data]
- **Responsável**: [Nome]

## 2. Hipóteses
- [Hipótese 1]
- [Hipótese 2]

## 3. Experimentos
- [Experimento 1]
- [Experimento 2]

## 4. Descobertas (Findings)
- [Descoberta 1]

## 5. Decisão (Kill or Scale)
- [Decisão final sobre o projeto]
"@

$TemplateProduct = @"
# 📦 Template de Produto

## 1. Visão (Vision)
- **Nome do Produto**: [Nome]
- **Propósito**: [O que ele faz e por que existe]

## 2. Problema (Problem)
- [Qual problema estamos resolvendo?]

## 3. Solução (Solution)
- [Como resolvemos o problema?]

## 4. Usuário Alvo (Target User)
- [Quem vai usar?]

## 5. Proposta de Valor (Value Prop)
- [Por que escolher este produto?]

## 6. Métricas (Metrics)
- [KPI 1]
- [KPI 2]
"@

$TemplateAgent = @"
# 🤖 Template de Agente

## 1. Identidade Core (Core Identity)
- **Nome**: [Nome do Agente]
- **Propósito**: [Missão principal]
- **Personalidade**: [Traços de personalidade]

## 2. Habilidades (Skills)
- **Token Skills (Como pensa)**: [Raciocínio, análise]
- **Tool Skills (Como age)**: [Ferramentas que utiliza]

## 3. Alma (Soul)
- **Voz e Tom**: [Como se comunica]
- **Regras de Memória**: [O que deve lembrar]

## 4. Casos de Uso (Use Cases)
- [Caso 1]
- [Caso 2]
"@

$TemplateSaaS = @"
# 🌐 Template de SaaS

## 1. Resumo Executivo
- **Nome do SaaS**: [Nome]
- **Modelo de Negócio**: [B2B, B2C, etc]

## 2. Arquitetura
- **Frontend**: [Stack]
- **Backend**: [Stack]
- **Infra/Cloud**: [Stack]

## 3. Automações
- [Automação 1]
- [Automação 2]

## 4. Roadmap
- [Fase 1]
- [Fase 2]
"@

# Criar templates na pasta base
Create-File -Path "00_SYSTEM\Templates\Project.md" -Content $TemplateProject
Create-File -Path "00_SYSTEM\Templates\Product.md" -Content $TemplateProduct
Create-File -Path "00_SYSTEM\Templates\Agent.md" -Content $TemplateAgent
Create-File -Path "00_SYSTEM\Templates\SaaS.md" -Content $TemplateSaaS

# Criar templates nas pastas específicas
Create-File -Path "02_GINKGO_AI_SYSTEMS\01_INTERNAL_PROJECTS\Template_Projeto.md" -Content $TemplateProject
Create-File -Path "02_GINKGO_AI_SYSTEMS\02_PRODUCTS\Template_Produto.md" -Content $TemplateProduct
Create-File -Path "02_GINKGO_AI_SYSTEMS\03_SAAS\Template_SaaS.md" -Content $TemplateSaaS
Create-File -Path "02_GINKGO_AI_SYSTEMS\04_AGENTS\Template_Agente.md" -Content $TemplateAgent

# Criar READMEs para cada módulo
$Modules = @(
    "01_INTERNAL_PROJECTS", "02_PRODUCTS", "03_SAAS", "04_AGENTS", 
    "05_DESIGN", "06_DOCUMENTATION", "07_MEDIA\Raw", "07_MEDIA\Edited", 
    "07_MEDIA\Final", "08_SITES", "09_AUTOMATIONS\n8n", 
    "09_AUTOMATIONS\Make", "09_AUTOMATIONS\Zapier", "09_AUTOMATIONS\Scripts"
)

foreach ($Mod in $Modules) {
    $ModName = ($Mod -split "\\")[-1]
    $ReadmeContent = "# 📁 Módulo: $ModName`n`nParte da arquitetura Ginkgo AI Systems."
    Create-File -Path "02_GINKGO_AI_SYSTEMS\$Mod\README.md" -Content $ReadmeContent
}

Write-Host "`n=======================================================" -ForegroundColor Cyan
Write-Host "🎉 CONCLUÍDO COM SUCESSO!" -ForegroundColor Green
Write-Host "A estrutura Ginkgo AI Systems foi criada no seu OneDrive." -ForegroundColor White
Write-Host "Pressione qualquer tecla para sair..." -ForegroundColor DarkGray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
