"""
Ponto de entrada da aplicação FastAPI
Configuração do servidor e middlewares
"""
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Criação da aplicação FastAPI
app = FastAPI(
    title="Microkernel Media Player API",
    description="API REST para sistema de media player baseado em arquitetura Microkernel",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configuração de CORS para permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especificar domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra as rotas
app.include_router(router, prefix="/api", tags=["media"])


@app.on_event("startup")
async def startup_event():
    """Evento executado na inicialização do servidor"""
    logger.info("=" * 60)
    logger.info("🚀 Microkernel Media Player API iniciada")
    logger.info("=" * 60)
    logger.info("📖 Documentação: http://localhost:8000/docs")
    logger.info("🔄 ReDoc: http://localhost:8000/redoc")
    logger.info("=" * 60)


@app.on_event("shutdown")
async def shutdown_event():
    """Evento executado no desligamento do servidor"""
    logger.info("🛑 Servidor encerrado")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Hot reload durante desenvolvimento
        log_level="info"
    )
