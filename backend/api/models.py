"""
Modelos Pydantic para validação de dados da API
"""
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any


class PluginMetadataResponse(BaseModel):
    """Resposta com metadados de um plugin"""
    name: str
    version: str
    author: str
    description: str
    supported_formats: List[str]


class MediaMetadataResponse(BaseModel):
    """Resposta com metadados de arquivo de mídia"""
    filename: str
    format: str
    duration: Optional[float]
    size: int
    bitrate: Optional[int]
    codec: Optional[str]
    resolution: Optional[str]
    extra_info: Dict[str, Any]


class MediaAnalysisResponse(BaseModel):
    """Resposta completa de análise de mídia"""
    success: bool
    metadata: Optional[MediaMetadataResponse] = None
    plugin_used: Optional[str] = None
    stream_url: Optional[str] = None
    error: Optional[str] = None


class MediaValidationResponse(BaseModel):
    """Resposta de validação de arquivo"""
    valid: bool
    plugin: Optional[str] = None
    reason: str


class MediaFileInfo(BaseModel):
    """Informações de arquivo no storage"""
    filename: str
    size: int
    supported: bool
    plugin: Optional[str] = None


class UploadResponse(BaseModel):
    """Resposta de upload de arquivo"""
    success: bool
    filename: Optional[str] = None
    file_path: Optional[str] = None
    analysis: Optional[MediaAnalysisResponse] = None
    error: Optional[str] = None


class SystemInfoResponse(BaseModel):
    """Informações do sistema"""
    plugins_count: int
    supported_formats: List[str]
    plugins: List[PluginMetadataResponse]


class ErrorResponse(BaseModel):
    """Resposta de erro padrão"""
    error: str
    detail: Optional[str] = None


class SuccessResponse(BaseModel):
    """Resposta de sucesso genérica"""
    success: bool
    message: str
