"""
Plugin para arquivos de vídeo MP4
Implementa processamento específico para formato MP4
"""
import os
import cv2
from mutagen.mp4 import MP4
from core.interfaces import PluginMetadata, MediaMetadata
from plugins.base_plugin import BaseMediaPlugin


class MP4Plugin(BaseMediaPlugin):
    """Plugin para processamento de arquivos MP4"""

    def _create_metadata(self) -> PluginMetadata:
        """Cria metadados do plugin"""
        return PluginMetadata(
            name="MP4 Video Plugin",
            version="1.0.0",
            author="Media Player Team",
            description="Plugin para reprodução de vídeos MP4/M4V com suporte a codecs H.264 e HEVC",
            supported_formats=["mp4", "m4v"]
        )

    def extract_metadata(self, file_path: str) -> MediaMetadata:
        """
        Extrai metadados detalhados de arquivos MP4

        Args:
            file_path: Caminho do arquivo MP4

        Returns:
            MediaMetadata com informações do arquivo
        """
        if not self.can_handle(file_path):
            raise ValueError(f"Plugin MP4 não pode processar: {file_path}")

        try:
            # Usa OpenCV para informações de vídeo
            cap = cv2.VideoCapture(file_path)

            fps = cap.get(cv2.CAP_PROP_FPS)
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            duration = frame_count / fps if fps > 0 else 0

            cap.release()

            # Tenta extrair metadados adicionais com mutagen
            extra_info = {
                "fps": fps,
                "frame_count": frame_count,
                "width": width,
                "height": height
            }

            try:
                audio = MP4(file_path)
                if audio.info:
                    extra_info["bitrate"] = audio.info.bitrate
                    extra_info["codec"] = getattr(audio.info, 'codec', 'Unknown')
            except Exception:
                pass

            return MediaMetadata(
                filename=self._get_filename(file_path),
                format="mp4",
                duration=duration,
                size=self._get_file_size(file_path),
                bitrate=extra_info.get("bitrate"),
                codec=extra_info.get("codec", "H.264"),
                resolution=f"{width}x{height}",
                extra_info=extra_info
            )

        except Exception as e:
            raise ValueError(f"Erro ao extrair metadados MP4: {str(e)}")

    def validate_file(self, file_path: str) -> bool:
        """
        Validação específica para MP4
        """
        if not super().validate_file(file_path):
            return False

        try:
            cap = cv2.VideoCapture(file_path)
            is_valid = cap.isOpened()
            cap.release()
            return is_valid
        except Exception:
            return False
