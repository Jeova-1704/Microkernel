@echo off
echo ========================================
echo  Iniciando Backend - Microkernel Media Player
echo ========================================
echo.

cd backend

echo [1/3] Ativando ambiente virtual...
call venv\Scripts\activate.bat

echo [2/3] Verificando instalacao...
python -c "import fastapi; print('FastAPI OK')" 2>nul
if errorlevel 1 (
    echo [!] FastAPI nao encontrado. Instalando dependencias...
    pip install -r requirements.txt
)

echo [3/3] Iniciando servidor...
echo.
echo ========================================
echo  Backend rodando em: http://localhost:8000
echo  Documentacao: http://localhost:8000/docs
echo ========================================
echo.
echo Pressione Ctrl+C para parar o servidor
echo.

python main.py
