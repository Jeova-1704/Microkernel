"""
Plugin para arquivos de áudio MP3
Implementa processamento específico para formato MP3
"""
import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from core.interfaces import PluginMetadata, MediaMetadata
from plugins.base_plugin import BaseMediaPlugin


class MP3Plugin(BaseMediaPlugin):
    """Plugin para processamento de arquivos MP3"""

    def _create_metadata(self) -> PluginMetadata:
        """Cria metadados do plugin"""
        return PluginMetadata(
            name="MP3 Audio Plugin",
            version="1.0.0",
            author="Media Player Team",
            description="Plugin para reprodução de arquivos MP3 com suporte a tags ID3",
            supported_formats=["mp3"]
        )

    def extract_metadata(self, file_path: str) -> MediaMetadata:
        """
        Extrai metadados detalhados de arquivos MP3

        Args:
            file_path: Caminho do arquivo MP3

        Returns:
            MediaMetadata com informações do arquivo
        """
        if not self.can_handle(file_path):
            raise ValueError(f"Plugin MP3 não pode processar: {file_path}")

        try:
            audio = MP3(file_path)

            # Extrai informações básicas
            duration = audio.info.length
            bitrate = audio.info.bitrate
            sample_rate = audio.info.sample_rate

            # Tenta extrair tags ID3
            extra_info = {}
            try:
                tags = ID3(file_path)
                extra_info = {
                    "title": str(tags.get("TIT2", "Unknown")),
                    "artist": str(tags.get("TPE1", "Unknown")),
                    "album": str(tags.get("TALB", "Unknown")),
                    "year": str(tags.get("TDRC", "Unknown")),
                    "genre": str(tags.get("TCON", "Unknown")),
                    "sample_rate": sample_rate,
                    "channels": audio.info.channels,
                    "mode": audio.info.mode
                }
            except Exception:
                extra_info = {
                    "sample_rate": sample_rate,
                    "channels": audio.info.channels
                }

            return MediaMetadata(
                filename=self._get_filename(file_path),
                format="mp3",
                duration=duration,
                size=self._get_file_size(file_path),
                bitrate=bitrate,
                codec="MP3",
                resolution=None,
                extra_info=extra_info
            )

        except Exception as e:
            raise ValueError(f"Erro ao extrair metadados MP3: {str(e)}")

    def validate_file(self, file_path: str) -> bool:
        """
        Validação específica para MP3
        """
        if not super().validate_file(file_path):
            return False

        try:
            audio = MP3(file_path)
            # Verifica se tem duração válida
            return audio.info.length > 0
        except Exception:
            return False
