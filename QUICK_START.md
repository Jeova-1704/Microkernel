# 🚀 Quick Start Guide

Guia rápido para começar a usar o Microkernel Media Player.

## ⚡ Início Rápido (5 minutos)

### 1️⃣ Backend

```bash
# Navegue para o diretório backend
cd backend

# Crie ambiente virtual
python -m venv venv

# Ative o ambiente (Windows)
venv\Scripts\activate
# Ou no Linux/Mac:
# source venv/bin/activate

# Instale dependências
pip install -r requirements.txt

# Inicie o servidor
python main.py
```

✅ Backend rodando em: http://localhost:8000

### 2️⃣ Frontend

**Em outro terminal:**

```bash
# Navegue para o diretório frontend
cd frontend

# Instale dependências
npm install

# Inicie o servidor de desenvolvimento
npm run dev
```

✅ Frontend rodando em: http://localhost:3000

### 3️⃣ Testando

1. Acesse http://localhost:3000
2. Vá para a aba **"Plugins"** para ver os plugins disponíveis
3. Vá para a aba **"Upload"** e envie um arquivo MP3, MP4 ou AVI
4. Vá para a aba **"Player"** e reproduza o arquivo

## 🧪 Teste Rápido via API

```bash
# Verificar saúde do sistema
curl http://localhost:8000/api/health

# Listar plugins
curl http://localhost:8000/api/plugins

# Listar formatos suportados
curl http://localhost:8000/api/formats
```

## 📦 Estrutura Resumida

```
microkernel/
├── backend/              # Python + FastAPI
│   ├── core/            # Core System
│   ├── plugins/         # Plugins (MP3, MP4, AVI)
│   ├── api/             # REST API
│   └── main.py          # Entry point
│
└── frontend/            # React + Vite
    ├── src/
    │   ├── components/  # UI Components
    │   ├── services/    # API calls
    │   └── App.jsx      # Main app
    └── package.json
```

## 🎯 Próximos Passos

- 📖 Leia o [README completo](README.md)
- 🔌 Aprenda a [criar plugins](README.md#-desenvolvendo-plugins)
- 📡 Explore os [endpoints da API](README.md#-api-endpoints)
- 🏗️ Entenda a [arquitetura](README.md#-arquitetura)

## ⚠️ Problemas Comuns

### Backend não inicia

**Erro:** `ModuleNotFoundError`
**Solução:** Certifique-se de ter ativado o ambiente virtual e instalado as dependências

```bash
pip install -r requirements.txt
```

### Frontend não inicia

**Erro:** `ENOENT: no such file or directory`
**Solução:** Instale as dependências

```bash
npm install
```

### CORS Error

**Solução:** Certifique-se de que o backend está rodando na porta 8000

## 📞 Suporte

Se encontrar problemas, verifique:
- ✅ Python 3.9+ instalado
- ✅ Node.js 16+ instalado
- ✅ Portas 8000 e 3000 disponíveis
- ✅ Ambiente virtual ativado (backend)

---

**Pronto para começar! 🎉**
