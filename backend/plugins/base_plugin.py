"""
Classe base abstrata para plugins
Fornece implementação padrão de métodos comuns
"""
import os
from pathlib import Path
from typing import List
from core.interfaces import IMediaPlugin, PluginMetadata


class BaseMediaPlugin(IMediaPlugin):
    """
    Classe base que fornece funcionalidades comuns para todos os plugins
    """

    def __init__(self):
        self._metadata = self._create_metadata()

    def _create_metadata(self) -> PluginMetadata:
        """
        Método a ser sobrescrito pelas subclasses para definir metadados
        """
        raise NotImplementedError("Subclasses devem implementar _create_metadata()")

    def get_metadata(self) -> PluginMetadata:
        """Retorna os metadados do plugin"""
        return self._metadata

    def get_supported_formats(self) -> List[str]:
        """Retorna formatos suportados dos metadados"""
        return self._metadata.supported_formats

    def can_handle(self, file_path: str) -> bool:
        """
        Verifica se pode processar baseado na extensão do arquivo
        """
        if not os.path.exists(file_path):
            return False

        extension = Path(file_path).suffix.lower().replace('.', '')
        return extension in self.get_supported_formats()

    def validate_file(self, file_path: str) -> bool:
        """
        Validação básica: verifica se arquivo existe e tem tamanho > 0
        Subclasses podem sobrescrever para validação mais específica
        """
        if not os.path.exists(file_path):
            return False

        return os.path.getsize(file_path) > 0

    def get_stream_url(self, file_path: str) -> str:
        """
        Retorna URL relativa para streaming
        Pode ser sobrescrito para lógica customizada
        """
        filename = os.path.basename(file_path)
        return f"/api/media/stream/{filename}"

    def _get_file_size(self, file_path: str) -> int:
        """Retorna tamanho do arquivo em bytes"""
        return os.path.getsize(file_path)

    def _get_filename(self, file_path: str) -> str:
        """Retorna nome do arquivo"""
        return os.path.basename(file_path)

    def _get_format(self, file_path: str) -> str:
        """Retorna formato/extensão do arquivo"""
        return Path(file_path).suffix.lower().replace('.', '')
