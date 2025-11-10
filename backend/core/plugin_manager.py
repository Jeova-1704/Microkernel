"""
Gerenciador de Plugins - Implementação do padrão Registry
Responsável por registrar, descobrir e gerenciar plugins
"""
from typing import Dict, List, Optional
from core.interfaces import IMediaPlugin, IPluginManager, PluginMetadata
import logging

logger = logging.getLogger(__name__)


class PluginManager(IPluginManager):
    """
    Gerenciador central de plugins do sistema Microkernel
    Implementa o padrão Registry para gerenciar plugins dinâmicos
    """

    def __init__(self):
        self._plugins: Dict[str, IMediaPlugin] = {}
        self._format_to_plugin: Dict[str, IMediaPlugin] = {}
        logger.info("Plugin Manager inicializado")

    def register_plugin(self, plugin: IMediaPlugin) -> None:
        """
        Registra um novo plugin no sistema

        Args:
            plugin: Instância do plugin a ser registrado

        Raises:
            ValueError: Se já existe plugin com o mesmo nome
        """
        metadata = plugin.get_metadata()
        plugin_name = metadata.name

        if plugin_name in self._plugins:
            logger.warning(f"Plugin '{plugin_name}' já registrado. Substituindo...")

        self._plugins[plugin_name] = plugin

        # Mapeia formatos para o plugin
        for fmt in plugin.get_supported_formats():
            self._format_to_plugin[fmt.lower()] = plugin

        logger.info(
            f"Plugin registrado: {plugin_name} "
            f"(Formatos: {', '.join(metadata.supported_formats)})"
        )

    def unregister_plugin(self, plugin_name: str) -> None:
        """
        Remove um plugin do sistema

        Args:
            plugin_name: Nome do plugin a ser removido

        Raises:
            KeyError: Se o plugin não estiver registrado
        """
        if plugin_name not in self._plugins:
            raise KeyError(f"Plugin '{plugin_name}' não encontrado")

        plugin = self._plugins[plugin_name]

        # Remove mapeamentos de formato
        for fmt in plugin.get_supported_formats():
            if fmt.lower() in self._format_to_plugin:
                del self._format_to_plugin[fmt.lower()]

        del self._plugins[plugin_name]
        logger.info(f"Plugin removido: {plugin_name}")

    def get_plugin_for_file(self, file_path: str) -> Optional[IMediaPlugin]:
        """
        Retorna o plugin apropriado para processar um arquivo

        Args:
            file_path: Caminho do arquivo

        Returns:
            Plugin capaz de processar o arquivo ou None
        """
        # Tenta por extensão primeiro
        extension = file_path.split('.')[-1].lower()
        if extension in self._format_to_plugin:
            plugin = self._format_to_plugin[extension]
            if plugin.can_handle(file_path):
                logger.debug(f"Plugin encontrado por extensão '{extension}': {plugin.get_metadata().name}")
                return plugin

        # Fallback: tenta todos os plugins
        for plugin in self._plugins.values():
            if plugin.can_handle(file_path):
                logger.debug(f"Plugin encontrado por can_handle: {plugin.get_metadata().name}")
                return plugin

        logger.warning(f"Nenhum plugin encontrado para: {file_path}")
        return None

    def list_plugins(self) -> List[PluginMetadata]:
        """
        Lista todos os plugins registrados

        Returns:
            Lista de metadados dos plugins
        """
        return [plugin.get_metadata() for plugin in self._plugins.values()]

    def get_all_supported_formats(self) -> List[str]:
        """
        Lista todos os formatos suportados por todos os plugins

        Returns:
            Lista única de formatos
        """
        formats = set()
        for plugin in self._plugins.values():
            formats.update(plugin.get_supported_formats())
        return sorted(list(formats))

    def get_plugin_by_name(self, name: str) -> Optional[IMediaPlugin]:
        """
        Busca um plugin pelo nome

        Args:
            name: Nome do plugin

        Returns:
            Plugin ou None se não encontrado
        """
        return self._plugins.get(name)

    def plugin_count(self) -> int:
        """Retorna quantidade de plugins registrados"""
        return len(self._plugins)

    def clear_plugins(self) -> None:
        """Remove todos os plugins (útil para testes)"""
        self._plugins.clear()
        self._format_to_plugin.clear()
        logger.info("Todos os plugins foram removidos")
