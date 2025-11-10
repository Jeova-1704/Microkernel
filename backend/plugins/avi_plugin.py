"""
Plugin para arquivos de vídeo AVI
Implementa processamento específico para formato AVI
"""
import os
import cv2
from core.interfaces import PluginMetadata, MediaMetadata
from plugins.base_plugin import BaseMediaPlugin


class AVIPlugin(BaseMediaPlugin):
    """Plugin para processamento de arquivos AVI"""

    def _create_metadata(self) -> PluginMetadata:
        """Cria metadados do plugin"""
        return PluginMetadata(
            name="AVI Video Plugin",
            version="1.0.0",
            author="Media Player Team",
            description="Plugin para reprodução de vídeos AVI com diversos codecs",
            supported_formats=["avi"]
        )

    def extract_metadata(self, file_path: str) -> MediaMetadata:
        """
        Extrai metadados detalhados de arquivos AVI

        Args:
            file_path: Caminho do arquivo AVI

        Returns:
            MediaMetadata com informações do arquivo
        """
        if not self.can_handle(file_path):
            raise ValueError(f"Plugin AVI não pode processar: {file_path}")

        try:
            # Usa OpenCV para informações de vídeo
            cap = cv2.VideoCapture(file_path)

            fps = cap.get(cv2.CAP_PROP_FPS)
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            duration = frame_count / fps if fps > 0 else 0
            fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))

            # Decodifica o codec FourCC
            codec = "".join([chr((fourcc >> 8 * i) & 0xFF) for i in range(4)])

            cap.release()

            extra_info = {
                "fps": fps,
                "frame_count": frame_count,
                "width": width,
                "height": height,
                "fourcc": codec
            }

            return MediaMetadata(
                filename=self._get_filename(file_path),
                format="avi",
                duration=duration,
                size=self._get_file_size(file_path),
                bitrate=None,  # AVI não tem bitrate facilmente acessível
                codec=codec,
                resolution=f"{width}x{height}",
                extra_info=extra_info
            )

        except Exception as e:
            raise ValueError(f"Erro ao extrair metadados AVI: {str(e)}")

    def validate_file(self, file_path: str) -> bool:
        """
        Validação específica para AVI
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
