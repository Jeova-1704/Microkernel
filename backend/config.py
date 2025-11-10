"""
Configurações da aplicação
"""
import os
from pathlib import Path

# Diretórios
BASE_DIR = Path(__file__).parent
STORAGE_DIR = BASE_DIR / "storage" / "uploads"

# Criar diretórios necessários
STORAGE_DIR.mkdir(parents=True, exist_ok=True)

# Configurações de upload
MAX_UPLOAD_SIZE = 500 * 1024 * 1024  # 500 MB
ALLOWED_EXTENSIONS = ["mp3", "mp4", "avi", "m4v"]

# Configurações de API
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8000"))
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# Configurações de CORS
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")
