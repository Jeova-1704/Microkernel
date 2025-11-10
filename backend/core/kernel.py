"""
Microkernel - Core System
Núcleo mínimo do sistema que coordena plugins e operações essenciais
"""
import os
import logging
from typing import Optional, List, Dict, Any
from pathlib import Path

from core.plugin_manager import PluginManager
from core.interfaces import MediaMetadata, PluginMetadata
from plugins.mp3_plugin import MP3Plugin
from plugins.mp4_plugin import MP4Plugin
from plugins.avi_plugin import AVIPlugin

logger = logging.getLogger(__name__)


class MediaKernel:
    """
    Núcleo do sistema - Microkernel
    Responsabilidades mínimas:
    - Gerenciar ciclo de vida dos plugins
    - Delegar operações para plugins apropriados
    - Fornecer API de alto nível para a camada de aplicação
    """

    def __init__(self, storage_path: str = "./storage/uploads"):
        """
        Inicializa o Microkernel

        Args:
            storage_path: Diretório para armazenar arquivos de mídia
        """
        self.plugin_manager = PluginManager()
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)

        # Auto-carrega plugins disponíveis
        self._load_default_plugins()

        logger.info(f"MediaKernel inicializado (Storage: {self.storage_path})")

    def _load_default_plugins(self) -> None:
        """
        Carrega plugins padrão do sistema
        Em produção, isso poderia ser dinâmico (descoberta automática)
        """
        default_plugins = [
            MP3Plugin(),
            MP4Plugin(),
            AVIPlugin()
        ]

        for plugin in default_plugins:
            try:
                self.plugin_manager.register_plugin(plugin)
            except Exception as e:
                logger.error(f"Erro ao carregar plugin: {e}")

        logger.info(f"{self.plugin_manager.plugin_count()} plugins carregados")

    def register_plugin(self, plugin) -> Dict[str, Any]:
        """
        Registra um novo plugin no sistema

        Args:
            plugin: Instância do plugin

        Returns:
            Dicionário com resultado da operação
        """
        try:
            self.plugin_manager.register_plugin(plugin)
            return {
                "success": True,
                "message": f"Plugin '{plugin.get_metadata().name}' registrado com sucesso"
            }
        except Exception as e:
            logger.error(f"Erro ao registrar plugin: {e}")
            return {
                "success": False,
                "error": str(e)
            }

    def get_plugins(self) -> List[PluginMetadata]:
        """
        Lista todos os plugins registrados

        Returns:
            Lista de metadados dos plugins
        """
        return self.plugin_manager.list_plugins()

    def get_supported_formats(self) -> List[str]:
        """
        Retorna todos os formatos suportados

        Returns:
            Lista de extensões suportadas
        """
        return self.plugin_manager.get_all_supported_formats()

    def analyze_media(self, file_path: str) -> Dict[str, Any]:
        """
        Analisa um arquivo de mídia e extrai metadados

        Args:
            file_path: Caminho do arquivo

        Returns:
            Dicionário com metadados ou erro
        """
        try:
            # Encontra plugin apropriado
            plugin = self.plugin_manager.get_plugin_for_file(file_path)

            if not plugin:
                return {
                    "success": False,
                    "error": "Nenhum plugin disponível para este formato"
                }

            # Valida arquivo
            if not plugin.validate_file(file_path):
                return {
                    "success": False,
                    "error": "Arquivo inválido ou corrompido"
                }

            # Extrai metadados
            metadata = plugin.extract_metadata(file_path)

            return {
                "success": True,
                "metadata": metadata,
                "plugin_used": plugin.get_metadata().name,
                "stream_url": plugin.get_stream_url(file_path)
            }

        except Exception as e:
            logger.error(f"Erro ao analisar mídia: {e}")
            return {
                "success": False,
                "error": str(e)
            }

    def validate_media(self, file_path: str) -> Dict[str, Any]:
        """
        Valida se um arquivo pode ser processado

        Args:
            file_path: Caminho do arquivo

        Returns:
            Dicionário com resultado da validação
        """
        try:
            plugin = self.plugin_manager.get_plugin_for_file(file_path)

            if not plugin:
                return {
                    "valid": False,
                    "reason": "Formato não suportado"
                }

            is_valid = plugin.validate_file(file_path)

            return {
                "valid": is_valid,
                "plugin": plugin.get_metadata().name if is_valid else None,
                "reason": "OK" if is_valid else "Arquivo inválido"
            }

        except Exception as e:
            logger.error(f"Erro ao validar mídia: {e}")
            return {
                "valid": False,
                "reason": str(e)
            }

    def get_stream_url(self, file_path: str) -> Optional[str]:
        """
        Retorna URL para streaming de um arquivo

        Args:
            file_path: Caminho do arquivo

        Returns:
            URL de streaming ou None
        """
        try:
            plugin = self.plugin_manager.get_plugin_for_file(file_path)
            if plugin:
                return plugin.get_stream_url(file_path)
            return None
        except Exception as e:
            logger.error(f"Erro ao obter URL de streaming: {e}")
            return None

    def save_uploaded_file(self, filename: str, content: bytes) -> str:
        """
        Salva arquivo enviado no storage

        Args:
            filename: Nome do arquivo
            content: Conteúdo em bytes

        Returns:
            Caminho completo do arquivo salvo
        """
        file_path = self.storage_path / filename
        file_path.write_bytes(content)
        logger.info(f"Arquivo salvo: {file_path}")
        return str(file_path)

    def list_media_files(self) -> List[Dict[str, Any]]:
        """
        Lista todos os arquivos de mídia no storage

        Returns:
            Lista de informações dos arquivos
        """
        files = []
        for file_path in self.storage_path.iterdir():
            if file_path.is_file():
                plugin = self.plugin_manager.get_plugin_for_file(str(file_path))
                files.append({
                    "filename": file_path.name,
                    "size": file_path.stat().st_size,
                    "supported": plugin is not None,
                    "plugin": plugin.get_metadata().name if plugin else None
                })
        return files

    def delete_media(self, filename: str) -> bool:
        """
        Remove um arquivo de mídia

        Args:
            filename: Nome do arquivo

        Returns:
            True se removido com sucesso
        """
        try:
            file_path = self.storage_path / filename
            if file_path.exists():
                file_path.unlink()
                logger.info(f"Arquivo removido: {filename}")
                return True
            return False
        except Exception as e:
            logger.error(f"Erro ao remover arquivo: {e}")
            return False
