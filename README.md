# 🎵 Microkernel Media Player

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18.2+-61dafb.svg)](https://reactjs.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Sistema de reprodução de mídia baseado no **padrão arquitetural Microkernel** (Plugin Architecture), implementado com **FastAPI** (backend) e **React** (frontend).

---

## 📚 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Arquitetura](#-arquitetura)
- [Padrão Microkernel](#-padrão-microkernel)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Instalação](#-instalação)
- [Como Usar](#-como-usar)
- [API Endpoints](#-api-endpoints)
- [Desenvolvendo Plugins](#-desenvolvendo-plugins)
- [Screenshots](#-screenshots)
- [Contribuindo](#-contribuindo)

---

## 🎯 Sobre o Projeto

Este projeto demonstra a implementação do **padrão arquitetural Microkernel**, também conhecido como **Plugin Architecture**, através de um sistema de media player similar ao VLC.

### Objetivos

✅ Demonstrar arquitetura extensível e desacoplada
✅ Permitir adição de novos formatos sem modificar o core
✅ Separação clara entre core system e módulos externos
✅ API REST para comunicação frontend-backend
✅ Interface moderna e responsiva

---

## 🏗️ Arquitetura

### Visão Geral

```
┌─────────────────────────────────────────────────────────────┐
│                     FRONTEND (React)                        │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────┐   │
│  │  Player  │  │ Uploader │  │ Plugin   │  │  UI     │   │
│  │Component │  │Component │  │ Manager  │  │ Utils   │   │
│  └─────┬────┘  └────┬─────┘  └────┬─────┘  └────┬────┘   │
│        │            │             │             │         │
│        └────────────┴─────────────┴─────────────┘         │
│                          │                                 │
│                   Context API / Hooks                      │
│                          │                                 │
└──────────────────────────┼─────────────────────────────────┘
                           │
                      HTTP / REST
                           │
┌──────────────────────────▼─────────────────────────────────┐
│                  API LAYER (FastAPI)                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                │
│  │  Routes  │  │  Models  │  │   CORS   │                │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘                │
│       │             │             │                        │
│       └─────────────┴─────────────┘                        │
│                     │                                      │
└─────────────────────┼──────────────────────────────────────┘
                      │
┌─────────────────────▼──────────────────────────────────────┐
│              CORE SYSTEM (Microkernel)                     │
│  ┌───────────────────────────────────────────────────┐    │
│  │            MediaKernel (Core)                     │    │
│  │  • Minimal core functionality                     │    │
│  │  • Plugin lifecycle management                    │    │
│  │  • Delegation to appropriate plugins              │    │
│  └──────────────────┬────────────────────────────────┘    │
│                     │                                      │
│  ┌──────────────────▼────────────────────────────────┐    │
│  │         PluginManager (Registry)                  │    │
│  │  • Plugin registration/unregistration             │    │
│  │  • Plugin discovery                               │    │
│  │  • Format-to-plugin mapping                       │    │
│  └──────────────────┬────────────────────────────────┘    │
│                     │                                      │
│  ┌──────────────────▼────────────────────────────────┐    │
│  │         IMediaPlugin (Interface)                  │    │
│  │  • Plugin contract definition                     │    │
│  │  • Abstract methods                               │    │
│  └───────────────────────────────────────────────────┘    │
└────────────────────────┬───────────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
┌────────▼────────┐ ┌───▼────────┐ ┌───▼────────┐
│   MP3 Plugin    │ │ MP4 Plugin │ │ AVI Plugin │
│  • MP3 parsing  │ │ • MP4      │ │ • AVI      │
│  • ID3 tags     │ │ • M4V      │ │ • Multiple │
│  • Audio stream │ │ • H.264    │ │   codecs   │
└─────────────────┘ └────────────┘ └────────────┘
```

### Fluxo de Dados

```
┌──────────┐
│  User    │
└────┬─────┘
     │ 1. Upload file
     ▼
┌──────────────┐
│   Frontend   │
└────┬─────────┘
     │ 2. POST /api/upload
     ▼
┌──────────────┐
│   FastAPI    │
└────┬─────────┘
     │ 3. Save file
     ▼
┌──────────────┐
│ MediaKernel  │
└────┬─────────┘
     │ 4. Request plugin
     ▼
┌──────────────┐
│PluginManager │
└────┬─────────┘
     │ 5. Return plugin
     ▼
┌──────────────┐
│ MP3Plugin    │ (example)
└────┬─────────┘
     │ 6. Extract metadata
     ▼
┌──────────────┐
│  Response    │ ──► Frontend displays data
└──────────────┘
```

---

## 🔧 Padrão Microkernel

### Conceito

O padrão **Microkernel** (ou **Plugin Architecture**) divide o sistema em:

1. **Core System (Microkernel)**: Funcionalidades mínimas essenciais
2. **Plugins**: Módulos externos que estendem o sistema

### Componentes

#### 1. Core System (Microkernel)

**Responsabilidades:**
- ✅ Gerenciar ciclo de vida dos plugins
- ✅ Fornecer interface de registro
- ✅ Delegar operações para plugins apropriados
- ✅ Manter funcionalidades mínimas

**Implementação:** `backend/core/kernel.py`

```python
class MediaKernel:
    """
    Núcleo mínimo do sistema
    Coordena plugins e fornece API de alto nível
    """
    def __init__(self):
        self.plugin_manager = PluginManager()
        self._load_default_plugins()

    def analyze_media(self, file_path: str):
        plugin = self.plugin_manager.get_plugin_for_file(file_path)
        return plugin.extract_metadata(file_path)
```

#### 2. Plugin Manager (Registry)

**Responsabilidades:**
- ✅ Registrar/desregistrar plugins
- ✅ Descobrir plugins disponíveis
- ✅ Mapear formatos para plugins
- ✅ Fornecer plugin apropriado sob demanda

**Implementação:** `backend/core/plugin_manager.py`

```python
class PluginManager:
    def register_plugin(self, plugin: IMediaPlugin):
        """Registra plugin no sistema"""

    def get_plugin_for_file(self, file_path: str):
        """Retorna plugin capaz de processar o arquivo"""
```

#### 3. Plugin Interface (Contract)

**Responsabilidades:**
- ✅ Definir contrato que todos os plugins devem seguir
- ✅ Garantir consistência entre plugins
- ✅ Permitir polimorfismo

**Implementação:** `backend/core/interfaces.py`

```python
class IMediaPlugin(ABC):
    @abstractmethod
    def get_metadata(self) -> PluginMetadata:
        pass

    @abstractmethod
    def extract_metadata(self, file_path: str) -> MediaMetadata:
        pass

    @abstractmethod
    def can_handle(self, file_path: str) -> bool:
        pass
```

#### 4. Concrete Plugins

**Responsabilidades:**
- ✅ Implementar interface de plugin
- ✅ Processar formatos específicos
- ✅ Extrair metadados
- ✅ Validar arquivos

**Plugins Disponíveis:**
- 🎵 **MP3Plugin**: Áudio MP3 com tags ID3
- 🎬 **MP4Plugin**: Vídeo MP4/M4V (H.264, HEVC)
- 📹 **AVIPlugin**: Vídeo AVI (múltiplos codecs)

---

## 🛠️ Tecnologias Utilizadas

### Backend

| Tecnologia | Versão | Propósito |
|------------|--------|-----------|
| **Python** | 3.9+ | Linguagem principal |
| **FastAPI** | 0.104+ | Framework web assíncrono |
| **Uvicorn** | 0.24+ | Servidor ASGI |
| **Pydantic** | 2.5+ | Validação de dados |
| **Mutagen** | 1.47+ | Extração de metadados de áudio |
| **OpenCV** | 4.8+ | Processamento de vídeo |

### Frontend

| Tecnologia | Versão | Propósito |
|------------|--------|-----------|
| **React** | 18.2+ | Biblioteca UI |
| **Vite** | 5.0+ | Build tool e dev server |
| **TailwindCSS** | 3.3+ | Framework CSS utilitário |
| **Axios** | 1.6+ | Cliente HTTP |
| **React Player** | 2.13+ | Componente de player |
| **Lucide React** | 0.294+ | Ícones |

---

## 📁 Estrutura do Projeto

```
microkernel/
│
├── backend/                      # Backend Python/FastAPI
│   ├── core/                     # Core System (Microkernel)
│   │   ├── __init__.py
│   │   ├── interfaces.py         # 🔷 Plugin Interface (Contract)
│   │   ├── plugin_manager.py    # 🔷 Plugin Registry
│   │   └── kernel.py             # 🔷 Microkernel Core
│   │
│   ├── plugins/                  # 🔌 External Plugins
│   │   ├── __init__.py
│   │   ├── base_plugin.py        # Base class for plugins
│   │   ├── mp3_plugin.py         # 🎵 MP3 Plugin
│   │   ├── mp4_plugin.py         # 🎬 MP4 Plugin
│   │   └── avi_plugin.py         # 📹 AVI Plugin
│   │
│   ├── api/                      # API Layer
│   │   ├── __init__.py
│   │   ├── routes.py             # REST endpoints
│   │   └── models.py             # Pydantic models
│   │
│   ├── storage/                  # File storage
│   │   └── uploads/              # Uploaded media files
│   │
│   ├── main.py                   # Application entry point
│   ├── config.py                 # Configuration
│   └── requirements.txt          # Python dependencies
│
├── frontend/                     # Frontend React
│   ├── src/
│   │   ├── components/           # React Components
│   │   │   ├── Player/
│   │   │   │   ├── Player.jsx
│   │   │   │   └── Controls.jsx
│   │   │   ├── FileUploader/
│   │   │   │   └── FileUploader.jsx
│   │   │   └── PluginManager/
│   │   │       ├── PluginList.jsx
│   │   │       └── PluginCard.jsx
│   │   │
│   │   ├── context/              # React Context
│   │   │   └── PlayerContext.jsx
│   │   │
│   │   ├── hooks/                # Custom Hooks
│   │   │   └── usePlugins.js
│   │   │
│   │   ├── services/             # API Services
│   │   │   └── api.js
│   │   │
│   │   ├── App.jsx               # Main component
│   │   ├── main.jsx              # Entry point
│   │   └── index.css             # Global styles
│   │
│   ├── public/                   # Static assets
│   ├── index.html                # HTML template
│   ├── package.json              # Node dependencies
│   ├── vite.config.js            # Vite configuration
│   └── tailwind.config.js        # Tailwind configuration
│
└── README.md                     # 📖 This file
```

---

## 🚀 Instalação

### Pré-requisitos

- **Python** 3.9 ou superior
- **Node.js** 16+ e npm/yarn
- **Git**

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/microkernel-media-player.git
cd microkernel-media-player
```

### 2. Backend Setup

```bash
cd backend

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 3. Frontend Setup

```bash
cd frontend

# Instalar dependências
npm install
# ou
yarn install
```

---

## ▶️ Como Usar

### Iniciar Backend

```bash
cd backend
python main.py
```

O servidor estará disponível em:
- **API**: http://localhost:8000
- **Documentação**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Iniciar Frontend

```bash
cd frontend
npm run dev
# ou
yarn dev
```

O frontend estará disponível em: http://localhost:3000

### Fluxo de Uso

1. **Acesse** http://localhost:3000
2. **Visualize** plugins disponíveis na aba "Plugins"
3. **Faça upload** de arquivos na aba "Upload"
4. **Reproduza** mídia na aba "Player"

---

## 📡 API Endpoints

### System Information

```http
GET /api/
```

Retorna informações do sistema e plugins carregados.

**Response:**
```json
{
  "plugins_count": 3,
  "supported_formats": ["mp3", "mp4", "m4v", "avi"],
  "plugins": [...]
}
```

### List Plugins

```http
GET /api/plugins
```

Lista todos os plugins registrados.

### Get Supported Formats

```http
GET /api/formats
```

Retorna formatos suportados.

### Upload Media

```http
POST /api/upload
Content-Type: multipart/form-data
```

Faz upload de arquivo de mídia.

**Response:**
```json
{
  "success": true,
  "filename": "song.mp3",
  "file_path": "/storage/uploads/song.mp3",
  "analysis": {
    "success": true,
    "metadata": {
      "filename": "song.mp3",
      "format": "mp3",
      "duration": 245.5,
      "size": 4096000,
      "bitrate": 320000,
      "codec": "MP3",
      "extra_info": {...}
    },
    "plugin_used": "MP3 Audio Plugin",
    "stream_url": "/api/media/stream/song.mp3"
  }
}
```

### List Media Files

```http
GET /api/media
```

Lista arquivos no storage.

### Analyze Media

```http
GET /api/media/{filename}/analyze
```

Analisa arquivo específico.

### Validate Media

```http
GET /api/media/{filename}/validate
```

Valida arquivo.

### Stream Media

```http
GET /api/media/stream/{filename}
```

Retorna stream do arquivo.

### Delete Media

```http
DELETE /api/media/{filename}
```

Remove arquivo.

### Health Check

```http
GET /api/health
```

Verifica status do sistema.

---

## 🔌 Desenvolvendo Plugins

### Criar Novo Plugin

#### 1. Crie o arquivo do plugin

```python
# backend/plugins/wav_plugin.py

from core.interfaces import PluginMetadata, MediaMetadata
from plugins.base_plugin import BaseMediaPlugin

class WAVPlugin(BaseMediaPlugin):
    """Plugin para arquivos WAV"""

    def _create_metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="WAV Audio Plugin",
            version="1.0.0",
            author="Seu Nome",
            description="Plugin para arquivos WAV",
            supported_formats=["wav"]
        )

    def extract_metadata(self, file_path: str) -> MediaMetadata:
        # Implementar extração de metadados
        # ...

        return MediaMetadata(
            filename=self._get_filename(file_path),
            format="wav",
            duration=duration,
            size=self._get_file_size(file_path),
            bitrate=bitrate,
            codec="PCM",
            resolution=None,
            extra_info={}
        )
```

#### 2. Registre o plugin no kernel

```python
# backend/core/kernel.py

from plugins.wav_plugin import WAVPlugin

class MediaKernel:
    def _load_default_plugins(self):
        default_plugins = [
            MP3Plugin(),
            MP4Plugin(),
            AVIPlugin(),
            WAVPlugin(),  # ← Novo plugin
        ]
        # ...
```

#### 3. Pronto!

O plugin será automaticamente carregado e disponibilizado pelo sistema.

### Interface Obrigatória

Todo plugin deve implementar:

- ✅ `get_metadata()` - Metadados do plugin
- ✅ `get_supported_formats()` - Formatos suportados
- ✅ `can_handle(file_path)` - Verifica se pode processar
- ✅ `extract_metadata(file_path)` - Extrai metadados do arquivo
- ✅ `validate_file(file_path)` - Valida arquivo
- ✅ `get_stream_url(file_path)` - URL de streaming

---

## 📸 Screenshots

### 1. Player Interface
```
┌────────────────────────────────────────────────┐
│  🎵 Microkernel Media Player                   │
│  ┌────────────────────────────────────────┐   │
│  │                                        │   │
│  │         🎵 Song Title                  │   │
│  │         Artist Name                    │   │
│  │                                        │   │
│  └────────────────────────────────────────┘   │
│  ▐▬▬▬▬▬▬▬▬▬▬▬▶▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌  │
│  2:34                              3:45        │
│  ⏮  ▶  ⏭                            🔊 ▬▬▬▶   │
└────────────────────────────────────────────────┘
```

### 2. Plugin Manager
```
┌────────────────────────────────────────────────┐
│  📦 Plugins Registrados (3 plugins)            │
│  ┌──────────────┐ ┌──────────────┐ ┌─────────┐│
│  │ MP3 Plugin   │ │ MP4 Plugin   │ │ AVI     ││
│  │ v1.0.0       │ │ v1.0.0       │ │ Plugin  ││
│  │ 🎵 MP3       │ │ 🎬 MP4, M4V  │ │ 📹 AVI  ││
│  └──────────────┘ └──────────────┘ └─────────┘│
└────────────────────────────────────────────────┘
```

---

## 🎓 Conceitos de Arquitetura

### Princípios SOLID Aplicados

#### 1. **Single Responsibility Principle (SRP)**
- Cada plugin tem uma única responsabilidade: processar um formato específico
- Core System apenas coordena, não processa

#### 2. **Open/Closed Principle (OCP)**
- Sistema aberto para extensão (novos plugins)
- Fechado para modificação (core não muda)

#### 3. **Liskov Substitution Principle (LSP)**
- Qualquer plugin pode substituir outro que implemente `IMediaPlugin`

#### 4. **Interface Segregation Principle (ISP)**
- Interface `IMediaPlugin` contém apenas métodos necessários

#### 5. **Dependency Inversion Principle (DIP)**
- Core depende de abstrações (`IMediaPlugin`), não de implementações concretas

### Padrões de Projeto

- **Strategy**: Plugins são estratégias intercambiáveis
- **Registry**: Plugin Manager mantém registro de plugins
- **Factory**: Core cria/fornece plugins apropriados
- **Facade**: API fornece interface simplificada para o sistema

---

## 🧪 Testando o Sistema

### Testar Backend

```bash
cd backend
python -c "from core.kernel import MediaKernel; k = MediaKernel(); print(f'Plugins: {len(k.get_plugins())}')"
```

### Testar API

```bash
# Health check
curl http://localhost:8000/api/health

# Listar plugins
curl http://localhost:8000/api/plugins

# Upload (usando form-data)
curl -X POST http://localhost:8000/api/upload \
  -F "file=@/path/to/audio.mp3"
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovoPlugin`)
3. Commit suas mudanças (`git commit -m 'Add: WAV plugin'`)
4. Push para a branch (`git push origin feature/NovoPlugin`)
5. Abra um Pull Request

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Autor

**Carlos Melo**
Projeto desenvolvido para estudo de Arquitetura de Software

---

## 📚 Referências

- [Pattern-Oriented Software Architecture (POSA)](https://www.amazon.com/Pattern-Oriented-Software-Architecture-System-Patterns/dp/0471958697)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://reactjs.org/)
- [Plugin Architecture Pattern](https://www.oreilly.com/library/view/software-architecture-patterns/9781491971437/ch03.html)

---

## ⭐ Features Futuras

- [ ] Suporte a mais formatos (WAV, FLAC, MKV, WebM)
- [ ] Playlist persistente
- [ ] Hot-reload de plugins em runtime
- [ ] Sistema de permissões para plugins
- [ ] Cache de metadados
- [ ] Thumbnails para vídeos
- [ ] Equalizer
- [ ] Plugin marketplace

---

<div align="center">

**Desenvolvido com ❤️ usando Arquitetura Microkernel**

⭐ Se este projeto foi útil, considere dar uma estrela!

</div>
