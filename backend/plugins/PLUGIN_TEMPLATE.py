"""
Template para criação de novos plugins
Copie este arquivo e implemente os métodos necessários

INSTRUÇÕES:
1. Copie este arquivo para um novo arquivo (ex: wav_plugin.py)
2. Renomeie a classe (ex: WAVPlugin)
3. Implemente os métodos abstratos
4. Registre o plugin em kernel.py
"""
from core.interfaces import PluginMetadata, MediaMetadata
from plugins.base_plugin import BaseMediaPlugin
from typing import Dict, Any


class TemplatePlugin(BaseMediaPlugin):
    """
    Template para novo plugin
    Substitua 'Template' pelo nome do seu formato
    """

    def _create_metadata(self) -> PluginMetadata:
        """
        Define metadados do plugin

        PREENCHA:
        - name: Nome do plugin (ex: "WAV Audio Plugin")
        - version: Versão (ex: "1.0.0")
        - author: Seu nome
        - description: Descrição breve
        - supported_formats: Lista de extensões (ex: ["wav", "wave"])
        """
        return PluginMetadata(
            name="Template Plugin",  # ← MUDE AQUI
            version="1.0.0",
            author="Your Name",  # ← MUDE AQUI
            description="Description of what this plugin does",  # ← MUDE AQUI
            supported_formats=["ext1", "ext2"]  # ← MUDE AQUI
        )

    def extract_metadata(self, file_path: str) -> MediaMetadata:
        """
        Extrai metadados do arquivo

        IMPLEMENTE:
        1. Abra o arquivo
        2. Extraia informações usando biblioteca apropriada
        3. Retorne MediaMetadata com as informações

        EXEMPLO DE BIBLIOTECAS:
        - Áudio: mutagen, pydub, wave
        - Vídeo: opencv-python, ffmpeg-python
        - Imagem: Pillow
        """
        # Validação básica
        if not self.can_handle(file_path):
            raise ValueError(f"Plugin não pode processar: {file_path}")

        try:
            # ========================================
            # IMPLEMENTE SUA LÓGICA AQUI
            # ========================================

            # Exemplo para áudio:
            # import wave
            # with wave.open(file_path, 'rb') as audio:
            #     duration = audio.getnframes() / audio.getframerate()
            #     channels = audio.getnchannels()
            #     sample_rate = audio.getframerate()

            # Exemplo para vídeo:
            # import cv2
            # cap = cv2.VideoCapture(file_path)
            # fps = cap.get(cv2.CAP_PROP_FPS)
            # width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            # height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            # cap.release()

            # ========================================
            # Valores de exemplo - SUBSTITUA!
            # ========================================
            duration = 0.0  # ← Calcule a duração real
            bitrate = None  # ← Extraia o bitrate se disponível
            codec = "Unknown"  # ← Identifique o codec
            resolution = None  # ← Para vídeo: "1920x1080"

            extra_info: Dict[str, Any] = {
                # Adicione informações extras aqui
                # Ex: sample_rate, channels, fps, etc
            }

            # ========================================
            # Retorne os metadados
            # ========================================
            return MediaMetadata(
                filename=self._get_filename(file_path),
                format=self._get_format(file_path),
                duration=duration,
                size=self._get_file_size(file_path),
                bitrate=bitrate,
                codec=codec,
                resolution=resolution,
                extra_info=extra_info
            )

        except Exception as e:
            raise ValueError(f"Erro ao extrair metadados: {str(e)}")

    def validate_file(self, file_path: str) -> bool:
        """
        Valida se o arquivo está íntegro e pode ser processado

        IMPLEMENTE:
        - Validação básica já implementada em BaseMediaPlugin
        - Adicione validação específica do formato se necessário

        EXEMPLO:
        - Áudio: Verificar se tem frames válidos
        - Vídeo: Verificar se consegue abrir e ler frames
        """
        # Validação básica (arquivo existe e tem tamanho > 0)
        if not super().validate_file(file_path):
            return False

        try:
            # ========================================
            # ADICIONE VALIDAÇÃO ESPECÍFICA AQUI
            # ========================================

            # Exemplo:
            # import wave
            # with wave.open(file_path, 'rb') as audio:
            #     return audio.getnframes() > 0

            return True  # ← Retorne resultado da validação

        except Exception:
            return False


# ============================================
# COMO REGISTRAR O PLUGIN
# ============================================
"""
1. Abra: backend/core/kernel.py

2. Adicione o import:
   from plugins.seu_plugin import SeuPlugin

3. Adicione na lista de plugins:
   def _load_default_plugins(self):
       default_plugins = [
           MP3Plugin(),
           MP4Plugin(),
           AVIPlugin(),
           SeuPlugin(),  # ← ADICIONE AQUI
       ]
"""

# ============================================
# EXEMPLO COMPLETO: WAV PLUGIN
# ============================================
"""
import wave
from core.interfaces import PluginMetadata, MediaMetadata
from plugins.base_plugin import BaseMediaPlugin


class WAVPlugin(BaseMediaPlugin):
    def _create_metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="WAV Audio Plugin",
            version="1.0.0",
            author="Your Name",
            description="Plugin para arquivos WAV PCM",
            supported_formats=["wav"]
        )

    def extract_metadata(self, file_path: str) -> MediaMetadata:
        if not self.can_handle(file_path):
            raise ValueError(f"Cannot handle: {file_path}")

        with wave.open(file_path, 'rb') as audio:
            n_frames = audio.getnframes()
            framerate = audio.getframerate()
            duration = n_frames / framerate

            extra_info = {
                "sample_rate": framerate,
                "channels": audio.getnchannels(),
                "sample_width": audio.getsampwidth(),
                "compression_type": audio.getcomptype()
            }

            return MediaMetadata(
                filename=self._get_filename(file_path),
                format="wav",
                duration=duration,
                size=self._get_file_size(file_path),
                bitrate=framerate * audio.getnchannels() * audio.getsampwidth() * 8,
                codec="PCM",
                resolution=None,
                extra_info=extra_info
            )

    def validate_file(self, file_path: str) -> bool:
        if not super().validate_file(file_path):
            return False

        try:
            with wave.open(file_path, 'rb') as audio:
                return audio.getnframes() > 0
        except:
            return False
"""

# ============================================
# BIBLIOTECAS RECOMENDADAS
# ============================================
"""
ÁUDIO:
- mutagen: MP3, MP4, FLAC, OGG, etc (mais completo)
- pydub: Manipulação de áudio
- wave: WAV nativo do Python
- audioread: Leitura universal

VÍDEO:
- opencv-python (cv2): Análise de vídeo
- ffmpeg-python: Wrapper do FFmpeg
- moviepy: Edição de vídeo

IMAGEM:
- Pillow (PIL): Imagens em geral
- imageio: Leitura de múltiplos formatos

DOCUMENTOS:
- PyPDF2: PDF
- python-docx: Word
- openpyxl: Excel

INSTALAÇÃO:
pip install mutagen opencv-python pillow
"""
