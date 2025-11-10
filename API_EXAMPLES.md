# 📡 Exemplos de Uso da API

Exemplos práticos de como usar a API REST do Microkernel Media Player.

---

## 🔧 Configuração

**Base URL:** `http://localhost:8000/api`

**Headers comuns:**
```http
Content-Type: application/json
```

---

## 📋 Endpoints

### 1. System Information

Obtém informações gerais do sistema.

**Request:**
```bash
curl -X GET http://localhost:8000/api/
```

**Response:**
```json
{
  "plugins_count": 3,
  "supported_formats": ["mp3", "mp4", "m4v", "avi"],
  "plugins": [
    {
      "name": "MP3 Audio Plugin",
      "version": "1.0.0",
      "author": "Media Player Team",
      "description": "Plugin para reprodução de arquivos MP3 com suporte a tags ID3",
      "supported_formats": ["mp3"]
    },
    {
      "name": "MP4 Video Plugin",
      "version": "1.0.0",
      "author": "Media Player Team",
      "description": "Plugin para reprodução de vídeos MP4/M4V com suporte a codecs H.264 e HEVC",
      "supported_formats": ["mp4", "m4v"]
    },
    {
      "name": "AVI Video Plugin",
      "version": "1.0.0",
      "author": "Media Player Team",
      "description": "Plugin para reprodução de vídeos AVI com diversos codecs",
      "supported_formats": ["avi"]
    }
  ]
}
```

---

### 2. List Plugins

Lista todos os plugins registrados.

**Request:**
```bash
curl -X GET http://localhost:8000/api/plugins
```

**Response:**
```json
[
  {
    "name": "MP3 Audio Plugin",
    "version": "1.0.0",
    "author": "Media Player Team",
    "description": "Plugin para reprodução de arquivos MP3 com suporte a tags ID3",
    "supported_formats": ["mp3"]
  }
]
```

---

### 3. Get Supported Formats

Lista formatos suportados.

**Request:**
```bash
curl -X GET http://localhost:8000/api/formats
```

**Response:**
```json
["mp3", "mp4", "m4v", "avi"]
```

---

### 4. Upload Media File

Faz upload de arquivo de mídia.

**Request:**
```bash
curl -X POST http://localhost:8000/api/upload \
  -F "file=@/path/to/song.mp3"
```

**Response (MP3):**
```json
{
  "success": true,
  "filename": "song.mp3",
  "file_path": "./storage/uploads/song.mp3",
  "analysis": {
    "success": true,
    "metadata": {
      "filename": "song.mp3",
      "format": "mp3",
      "duration": 245.5,
      "size": 9830400,
      "bitrate": 320000,
      "codec": "MP3",
      "resolution": null,
      "extra_info": {
        "title": "Bohemian Rhapsody",
        "artist": "Queen",
        "album": "A Night at the Opera",
        "year": "1975",
        "genre": "Rock",
        "sample_rate": 44100,
        "channels": 2,
        "mode": "Stereo"
      }
    },
    "plugin_used": "MP3 Audio Plugin",
    "stream_url": "/api/media/stream/song.mp3"
  }
}
```

**Response (MP4):**
```json
{
  "success": true,
  "filename": "video.mp4",
  "file_path": "./storage/uploads/video.mp4",
  "analysis": {
    "success": true,
    "metadata": {
      "filename": "video.mp4",
      "format": "mp4",
      "duration": 3665.0,
      "size": 524288000,
      "bitrate": 5000000,
      "codec": "H.264",
      "resolution": "1920x1080",
      "extra_info": {
        "fps": 30.0,
        "frame_count": 109950,
        "width": 1920,
        "height": 1080
      }
    },
    "plugin_used": "MP4 Video Plugin",
    "stream_url": "/api/media/stream/video.mp4"
  }
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "Nenhum plugin disponível para este formato"
}
```

---

### 5. List Media Files

Lista todos os arquivos no storage.

**Request:**
```bash
curl -X GET http://localhost:8000/api/media
```

**Response:**
```json
[
  {
    "filename": "song.mp3",
    "size": 9830400,
    "supported": true,
    "plugin": "MP3 Audio Plugin"
  },
  {
    "filename": "video.mp4",
    "size": 524288000,
    "supported": true,
    "plugin": "MP4 Video Plugin"
  }
]
```

---

### 6. Analyze Media

Analisa arquivo específico.

**Request:**
```bash
curl -X GET http://localhost:8000/api/media/song.mp3/analyze
```

**Response:**
```json
{
  "success": true,
  "metadata": {
    "filename": "song.mp3",
    "format": "mp3",
    "duration": 245.5,
    "size": 9830400,
    "bitrate": 320000,
    "codec": "MP3",
    "resolution": null,
    "extra_info": {
      "title": "Bohemian Rhapsody",
      "artist": "Queen",
      "album": "A Night at the Opera"
    }
  },
  "plugin_used": "MP3 Audio Plugin",
  "stream_url": "/api/media/stream/song.mp3"
}
```

---

### 7. Validate Media

Valida arquivo.

**Request:**
```bash
curl -X GET http://localhost:8000/api/media/song.mp3/validate
```

**Response (válido):**
```json
{
  "valid": true,
  "plugin": "MP3 Audio Plugin",
  "reason": "OK"
}
```

**Response (inválido):**
```json
{
  "valid": false,
  "plugin": null,
  "reason": "Arquivo inválido ou corrompido"
}
```

---

### 8. Stream Media

Retorna stream do arquivo.

**Request:**
```bash
curl -X GET http://localhost:8000/api/media/stream/song.mp3 --output song.mp3
```

**Headers da Response:**
```http
Content-Type: application/octet-stream
Content-Disposition: attachment; filename="song.mp3"
```

---

### 9. Delete Media

Remove arquivo.

**Request:**
```bash
curl -X DELETE http://localhost:8000/api/media/song.mp3
```

**Response:**
```json
{
  "success": true,
  "message": "Arquivo 'song.mp3' removido com sucesso"
}
```

**Error Response:**
```json
{
  "detail": "Arquivo não encontrado"
}
```

---

### 10. Health Check

Verifica status do sistema.

**Request:**
```bash
curl -X GET http://localhost:8000/api/health
```

**Response:**
```json
{
  "status": "healthy",
  "plugins_loaded": 3,
  "storage_path": "./storage/uploads"
}
```

---

## 🐍 Exemplos em Python

### Upload de Arquivo

```python
import requests

url = "http://localhost:8000/api/upload"
files = {"file": open("song.mp3", "rb")}

response = requests.post(url, files=files)
data = response.json()

if data["success"]:
    print(f"Upload realizado: {data['filename']}")
    print(f"Plugin usado: {data['analysis']['plugin_used']}")
    print(f"Duração: {data['analysis']['metadata']['duration']}s")
else:
    print(f"Erro: {data['error']}")
```

### Listar Plugins

```python
import requests

url = "http://localhost:8000/api/plugins"
response = requests.get(url)
plugins = response.json()

for plugin in plugins:
    print(f"{plugin['name']} v{plugin['version']}")
    print(f"  Formatos: {', '.join(plugin['supported_formats'])}")
```

### Analisar Mídia

```python
import requests

filename = "song.mp3"
url = f"http://localhost:8000/api/media/{filename}/analyze"

response = requests.get(url)
data = response.json()

if data["success"]:
    metadata = data["metadata"]
    print(f"Arquivo: {metadata['filename']}")
    print(f"Formato: {metadata['format']}")
    print(f"Duração: {metadata['duration']}s")
    print(f"Codec: {metadata['codec']}")
```

---

## 🟢 Exemplos em JavaScript/Node.js

### Upload de Arquivo

```javascript
const FormData = require('form-data');
const fs = require('fs');
const axios = require('axios');

async function uploadFile(filePath) {
  const form = new FormData();
  form.append('file', fs.createReadStream(filePath));

  try {
    const response = await axios.post(
      'http://localhost:8000/api/upload',
      form,
      { headers: form.getHeaders() }
    );

    console.log('Upload realizado:', response.data.filename);
    console.log('Plugin usado:', response.data.analysis.plugin_used);
  } catch (error) {
    console.error('Erro:', error.response.data);
  }
}

uploadFile('./song.mp3');
```

### Listar Plugins

```javascript
const axios = require('axios');

async function listPlugins() {
  try {
    const response = await axios.get('http://localhost:8000/api/plugins');

    response.data.forEach(plugin => {
      console.log(`${plugin.name} v${plugin.version}`);
      console.log(`  Formatos: ${plugin.supported_formats.join(', ')}`);
    });
  } catch (error) {
    console.error('Erro:', error.message);
  }
}

listPlugins();
```

---

## 📱 Exemplos em React (Frontend)

### Upload com Progress

```jsx
import axios from 'axios';
import { useState } from 'react';

function FileUploader() {
  const [progress, setProgress] = useState(0);

  const handleUpload = async (file) => {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post(
        'http://localhost:8000/api/upload',
        formData,
        {
          onUploadProgress: (progressEvent) => {
            const percent = Math.round(
              (progressEvent.loaded * 100) / progressEvent.total
            );
            setProgress(percent);
          }
        }
      );

      console.log('Upload completo:', response.data);
    } catch (error) {
      console.error('Erro no upload:', error);
    }
  };

  return (
    <div>
      <input
        type="file"
        onChange={(e) => handleUpload(e.target.files[0])}
      />
      <div>Progresso: {progress}%</div>
    </div>
  );
}
```

### Buscar Plugins

```jsx
import { useEffect, useState } from 'react';
import axios from 'axios';

function PluginList() {
  const [plugins, setPlugins] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/plugins')
      .then(response => setPlugins(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      {plugins.map(plugin => (
        <div key={plugin.name}>
          <h3>{plugin.name}</h3>
          <p>{plugin.description}</p>
          <p>Formatos: {plugin.supported_formats.join(', ')}</p>
        </div>
      ))}
    </div>
  );
}
```

---

## 🧪 Testando com cURL

### Script Completo de Teste

```bash
#!/bin/bash

BASE_URL="http://localhost:8000/api"

echo "1. Health Check"
curl -X GET $BASE_URL/health
echo -e "\n"

echo "2. Listar Plugins"
curl -X GET $BASE_URL/plugins
echo -e "\n"

echo "3. Formatos Suportados"
curl -X GET $BASE_URL/formats
echo -e "\n"

echo "4. Upload de Arquivo"
curl -X POST $BASE_URL/upload -F "file=@song.mp3"
echo -e "\n"

echo "5. Listar Arquivos"
curl -X GET $BASE_URL/media
echo -e "\n"

echo "6. Analisar Arquivo"
curl -X GET $BASE_URL/media/song.mp3/analyze
echo -e "\n"

echo "7. Validar Arquivo"
curl -X GET $BASE_URL/media/song.mp3/validate
echo -e "\n"
```

---

## 🔍 Códigos de Status HTTP

| Código | Significado | Quando ocorre |
|--------|-------------|---------------|
| 200 | OK | Requisição bem-sucedida |
| 404 | Not Found | Arquivo/recurso não encontrado |
| 400 | Bad Request | Dados inválidos ou erro de validação |
| 500 | Internal Server Error | Erro no servidor |

---

## 🛠️ Ferramentas Recomendadas

- **Postman**: Cliente API com interface gráfica
- **Insomnia**: Alternativa ao Postman
- **httpie**: Cliente HTTP CLI moderno
- **Thunder Client**: Extensão para VS Code

---

## 📚 Documentação Interativa

Acesse a documentação interativa gerada automaticamente pelo FastAPI:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

Nessas interfaces você pode:
- ✅ Ver todos os endpoints
- ✅ Testar requisições
- ✅ Ver schemas de dados
- ✅ Baixar especificação OpenAPI

---

## 💡 Dicas

1. **Use a documentação interativa** para testes rápidos
2. **Valide arquivos antes** de fazer upload
3. **Verifique o health check** se algo não funcionar
4. **Use progress callbacks** em uploads grandes
5. **Implemente retry logic** para requisições que podem falhar

---

<div align="center">

**Para mais informações, consulte o [README.md](README.md)**

</div>
