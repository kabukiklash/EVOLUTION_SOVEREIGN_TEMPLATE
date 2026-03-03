# Revert.ps1 - Protocolo Militar de Instalação (MIP)
# Compliance: ISO 27002, NIST SP 800-160

$ErrorActionPreference = "Stop"

Write-Host "⚠️ [MIP] Iniciando Reversão Soberana..." -ForegroundColor Yellow

# 1. Remover Marcador de Operação
if (Test-Path "00_GOVERNANCE/deployment.ok") {
    Remove-Item "00_GOVERNANCE/deployment.ok"
    Write-Host " [+] Marcador de operação removido."
}

# 2. Restaurar Sistema (Opcional - Requer interação ou script de confirmação)
Write-Host "[!] Recomendado: Usar o Ponto de Restauração 'Evolution-MIP-Gold' via GUI do Windows se houver falhas críticas." -ForegroundColor Cyan

# 3. Limpeza de Slag
$slag = Get-ChildItem -Recurse -Include .log, .pyc, __pycache__ -ErrorAction SilentlyContinue
if ($slag) {
    $slag | Remove-Item -Force -Recurse
    Write-Host " [+] Lixo operacional removido."
}

Write-Host "Reversão concluída. O diretório está em modo 'Safe-State'." -ForegroundColor Green
