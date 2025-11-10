# PowerShell script para iniciar o backend

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Iniciando Backend - Microkernel Media Player" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Set-Location backend

Write-Host "[1/3] Ativando ambiente virtual..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

Write-Host "[2/3] Verificando instalacao..." -ForegroundColor Yellow
$fastapi_check = python -c "import fastapi; print('OK')" 2>$null
if (-not $fastapi_check) {
    Write-Host "[!] FastAPI nao encontrado. Instalando dependencias..." -ForegroundColor Red
    pip install -r requirements.txt
}

Write-Host "[3/3] Iniciando servidor..." -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host " Backend rodando em: http://localhost:8000" -ForegroundColor Green
Write-Host " Documentacao: http://localhost:8000/docs" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Pressione Ctrl+C para parar o servidor" -ForegroundColor Gray
Write-Host ""

python main.py
