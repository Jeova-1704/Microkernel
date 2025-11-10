# PowerShell script para iniciar o frontend

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Iniciando Frontend - Microkernel Media Player" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Set-Location frontend

Write-Host "[1/2] Verificando node_modules..." -ForegroundColor Yellow
if (-not (Test-Path "node_modules")) {
    Write-Host "[!] node_modules nao encontrado. Instalando dependencias..." -ForegroundColor Red
    npm install
} else {
    Write-Host "[OK] node_modules encontrado" -ForegroundColor Green
}

Write-Host "[2/2] Iniciando servidor de desenvolvimento..." -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host " Frontend rodando em: http://localhost:3000" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Pressione Ctrl+C para parar o servidor" -ForegroundColor Gray
Write-Host ""

npm run dev
