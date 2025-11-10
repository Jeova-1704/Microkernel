@echo off
echo ========================================
echo  Iniciando Frontend - Microkernel Media Player
echo ========================================
echo.

cd frontend

echo [1/2] Verificando node_modules...
if not exist "node_modules" (
    echo [!] node_modules nao encontrado. Instalando dependencias...
    npm install
) else (
    echo [OK] node_modules encontrado
)

echo [2/2] Iniciando servidor de desenvolvimento...
echo.
echo ========================================
echo  Frontend rodando em: http://localhost:3000
echo ========================================
echo.
echo Pressione Ctrl+C para parar o servidor
echo.

npm run dev
