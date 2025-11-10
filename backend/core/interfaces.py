"""
Interfaces e contratos para o padrão Microkernel
Define o contrato que todos os plugins devem seguir
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from dataclasses import dataclass


@dataclass
class PluginMetadata:
    """Metadados do plugin"""
    name: str
    version: str
    author: str
    description: str
    supported_formats: List[str]


@dataclass
class MediaMetadata:
    """Metadados de arquivos de mídia"""
    filename: str
    format: str
    duration: Optional[float]
    size: int
    bitrate: Optional[int]
    codec: Optional[str]
    resolution: Optional[str]
    extra_info: Dict[str, Any]


class IMediaPlugin(ABC):
    """
    Interface base para todos os plugins de mídia
    Implementa o padrão Strategy + Plugin Architecture
    """

    @abstractmethod
    def get_metadata(self) -> PluginMetadata:
        """
        Retorna os metadados do plugin

        Returns:
            PluginMetadata: Informações sobre o plugin
        """
        pass

    @abstractmethod
    def get_supported_formats(self) -> List[str]:
        """
        Retorna lista de formatos suportados pelo plugin

        Returns:
            List[str]: Lista de extensões (ex: ['mp3', 'wav'])
        """
        pass

    @abstractmethod
    def can_handle(self, file_path: str) -> bool:
        """
        Verifica se o plugin pode processar o arquivo

        Args:
            file_path: Caminho do arquivo

        Returns:
            bool: True se pode processar, False caso contrário
        """
        pass

    @abstractmethod
    def extract_metadata(self, file_path: str) -> MediaMetadata:
        """
        Extrai metadados do arquivo de mídia

        Args:
            file_path: Caminho do arquivo

        Returns:
            MediaMetadata: Metadados extraídos

        Raises:
            ValueError: Se o arquivo não puder ser processado
        """
        pass

    @abstractmethod
    def validate_file(self, file_path: str) -> bool:
        """
        Valida se o arquivo está íntegro e pode ser reproduzido

        Args:
            file_path: Caminho do arquivo

        Returns:
            bool: True se válido, False caso contrário
        """
        pass

    @abstractmethod
    def get_stream_url(self, file_path: str) -> str:
        """
        Retorna URL para streaming do arquivo

        Args:
            file_path: Caminho do arquivo

        Returns:
            str: URL para streaming
        """
        pass


class IPluginManager(ABC):
    """Interface para o gerenciador de plugins"""

    @abstractmethod
    def register_plugin(self, plugin: IMediaPlugin) -> None:
        """Registra um plugin no sistema"""
        pass

    @abstractmethod
    def unregister_plugin(self, plugin_name: str) -> None:
        """Remove um plugin do sistema"""
        pass

    @abstractmethod
    def get_plugin_for_file(self, file_path: str) -> Optional[IMediaPlugin]:
        """Retorna o plugin apropriado para o arquivo"""
        pass

    @abstractmethod
    def list_plugins(self) -> List[PluginMetadata]:
        """Lista todos os plugins registrados"""
        pass

    @abstractmethod
    def get_all_supported_formats(self) -> List[str]:
        """Lista todos os formatos suportados por todos os plugins"""
        pass
