"""
Rotas da API FastAPI
Expõe funcionalidades do Microkernel via REST
"""
import os
from fastapi import APIRouter, UploadFile, File, HTTPException, Path as PathParam
from fastapi.responses import FileResponse, StreamingResponse
from typing import List

from api.models import (
    PluginMetadataResponse,
    MediaMetadataResponse,
    MediaAnalysisResponse,
    MediaValidationResponse,
    MediaFileInfo,
    UploadResponse,
    SystemInfoResponse,
    SuccessResponse
)
from core.kernel import MediaKernel

# Inicializa o router
router = APIRouter()

# Instância global do kernel (em produção, usar dependency injection)
kernel = MediaKernel(storage_path="./storage/uploads")


@router.get("/", response_model=SystemInfoResponse)
async def get_system_info():
    """
    Retorna informações do sistema e plugins carregados
    """
    plugins = kernel.get_plugins()

    return SystemInfoResponse(
        plugins_count=len(plugins),
        supported_formats=kernel.get_supported_formats(),
        plugins=[
            PluginMetadataResponse(**plugin.__dict__)
            for plugin in plugins
        ]
    )


@router.get("/plugins", response_model=List[PluginMetadataResponse])
async def list_plugins():
    """
    Lista todos os plugins registrados
    """
    plugins = kernel.get_plugins()
    return [
        PluginMetadataResponse(**plugin.__dict__)
        for plugin in plugins
    ]


@router.get("/formats", response_model=List[str])
async def get_supported_formats():
    """
    Lista todos os formatos de mídia suportados
    """
    return kernel.get_supported_formats()


@router.post("/upload", response_model=UploadResponse)
async def upload_media(file: UploadFile = File(...)):
    """
    Upload de arquivo de mídia

    Args:
        file: Arquivo enviado

    Returns:
        Informações do upload e análise do arquivo
    """
    try:
        # Lê conteúdo do arquivo
        content = await file.read()

        # Salva no storage
        file_path = kernel.save_uploaded_file(file.filename, content)

        # Analisa o arquivo
        analysis_result = kernel.analyze_media(file_path)

        if not analysis_result["success"]:
            return UploadResponse(
                success=False,
                error=analysis_result.get("error", "Erro ao analisar arquivo")
            )

        # Converte metadata para o modelo de resposta
        metadata = analysis_result["metadata"]
        metadata_response = MediaMetadataResponse(
            filename=metadata.filename,
            format=metadata.format,
            duration=metadata.duration,
            size=metadata.size,
            bitrate=metadata.bitrate,
            codec=metadata.codec,
            resolution=metadata.resolution,
            extra_info=metadata.extra_info
        )

        analysis_response = MediaAnalysisResponse(
            success=True,
            metadata=metadata_response,
            plugin_used=analysis_result["plugin_used"],
            stream_url=analysis_result["stream_url"]
        )

        return UploadResponse(
            success=True,
            filename=file.filename,
            file_path=file_path,
            analysis=analysis_response
        )

    except Exception as e:
        return UploadResponse(
            success=False,
            error=f"Erro no upload: {str(e)}"
        )


@router.get("/media", response_model=List[MediaFileInfo])
async def list_media_files():
    """
    Lista todos os arquivos de mídia no storage
    """
    files = kernel.list_media_files()
    return [MediaFileInfo(**file_info) for file_info in files]


@router.get("/media/{filename}/analyze", response_model=MediaAnalysisResponse)
async def analyze_media(filename: str = PathParam(..., description="Nome do arquivo")):
    """
    Analisa um arquivo de mídia existente

    Args:
        filename: Nome do arquivo no storage

    Returns:
        Metadados completos do arquivo
    """
    file_path = os.path.join("./storage/uploads", filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Arquivo não encontrado")

    result = kernel.analyze_media(file_path)

    if not result["success"]:
        raise HTTPException(status_code=400, detail=result.get("error", "Erro ao analisar"))

    metadata = result["metadata"]
    metadata_response = MediaMetadataResponse(
        filename=metadata.filename,
        format=metadata.format,
        duration=metadata.duration,
        size=metadata.size,
        bitrate=metadata.bitrate,
        codec=metadata.codec,
        resolution=metadata.resolution,
        extra_info=metadata.extra_info
    )

    return MediaAnalysisResponse(
        success=True,
        metadata=metadata_response,
        plugin_used=result["plugin_used"],
        stream_url=result["stream_url"]
    )


@router.get("/media/{filename}/validate", response_model=MediaValidationResponse)
async def validate_media(filename: str = PathParam(..., description="Nome do arquivo")):
    """
    Valida se um arquivo pode ser processado

    Args:
        filename: Nome do arquivo no storage

    Returns:
        Resultado da validação
    """
    file_path = os.path.join("./storage/uploads", filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Arquivo não encontrado")

    result = kernel.validate_media(file_path)
    return MediaValidationResponse(**result)


@router.get("/media/stream/{filename}")
async def stream_media(filename: str = PathParam(..., description="Nome do arquivo")):
    """
    Stream de arquivo de mídia

    Args:
        filename: Nome do arquivo

    Returns:
        Stream do arquivo
    """
    file_path = os.path.join("./storage/uploads", filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Arquivo não encontrado")

    return FileResponse(
        file_path,
        media_type="application/octet-stream",
        filename=filename
    )


@router.delete("/media/{filename}", response_model=SuccessResponse)
async def delete_media(filename: str = PathParam(..., description="Nome do arquivo")):
    """
    Remove um arquivo de mídia

    Args:
        filename: Nome do arquivo

    Returns:
        Resultado da operação
    """
    success = kernel.delete_media(filename)

    if not success:
        raise HTTPException(status_code=404, detail="Arquivo não encontrado")

    return SuccessResponse(
        success=True,
        message=f"Arquivo '{filename}' removido com sucesso"
    )


@router.get("/health")
async def health_check():
    """
    Endpoint de health check

    Returns:
        Status do sistema
    """
    return {
        "status": "healthy",
        "plugins_loaded": kernel.plugin_manager.plugin_count(),
        "storage_path": str(kernel.storage_path)
    }
