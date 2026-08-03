# subir_github.ps1 — publica C:\sexta-feira no GitHub como repo privado "sylvia"
# Uso: clique-direito > Executar com PowerShell (ou: powershell -ExecutionPolicy Bypass -File .\subir_github.ps1)
# O token é pedido na hora e NUNCA fica gravado em arquivo ou no remote.

$ErrorActionPreference = "Continue"
$repoPath = "C:\sexta-feira"
$repoName = "sylvia"

Write-Host "== Sylvia -> GitHub ==" -ForegroundColor Cyan
$token = Read-Host "Cole seu GitHub PAT (com permissao de criar repositorio e push)"
if (-not $token) { Write-Host "Token vazio. Abortando."; exit 1 }

$headers = @{ Authorization = "Bearer $token"; Accept = "application/vnd.github+json"; "User-Agent" = "sylvia-setup" }

# 1) Identificar usuário
try {
    $user  = Invoke-RestMethod -Uri "https://api.github.com/user" -Headers $headers
    $login = $user.login
    Write-Host "Autenticado como: $login" -ForegroundColor Green
} catch {
    Write-Host "Token invalido ou sem acesso a API ($($_.Exception.Message)). Abortando." -ForegroundColor Red
    exit 1
}

# 2) Criar repo privado (se ainda não existir)
$created = $false
try {
    $body = @{ name = $repoName; private = $true; description = "Cognicao da Sylvia - inteligencia executiva da holding (Ginkgo + Scale Group)" } | ConvertTo-Json
    Invoke-RestMethod -Method Post -Uri "https://api.github.com/user/repos" -Headers $headers -Body $body -ContentType "application/json" | Out-Null
    $created = $true
    Write-Host "Repositorio PRIVADO '$repoName' criado." -ForegroundColor Green
} catch {
    $detail = ""
    try { $detail = $_.ErrorDetails.Message } catch {}
    if ($detail -match "already exists") {
        Write-Host "Repositorio ja existe - seguindo para o push." -ForegroundColor Yellow
    } else {
        Write-Host "Nao consegui criar via API (provavel permissao do PAT)." -ForegroundColor Yellow
        Write-Host "Crie manualmente: https://github.com/new  -> nome: $repoName, visibilidade: PRIVADO, sem README."
        Read-Host "Depois de criar, pressione Enter para continuar"
    }
}

# 3) Push (auth via header; token nao fica no .git/config)
Set-Location $repoPath
if (-not (git config user.name))  { git config user.name  "Gabriel" }
if (-not (git config user.email)) { git config user.email "bocaoamazon@gmail.com" }

$pair = "x-access-token:" + $token
$b64  = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes($pair))

git remote remove origin 2>&1 | Out-Null
git remote add origin "https://github.com/$login/$repoName.git"
git -c http.extraHeader="Authorization: Basic $b64" push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "Publicado: https://github.com/$login/$repoName" -ForegroundColor Green
    Write-Host "IMPORTANTE: revogue o PAT usado (https://github.com/settings/tokens) e crie" -ForegroundColor Yellow
    Write-Host "uma credencial normal (Git Credential Manager) para os proximos pushes." -ForegroundColor Yellow
} else {
    Write-Host "Push falhou. Verifique se o repo existe e se o PAT tem permissao de conteudo (write)." -ForegroundColor Red
}
