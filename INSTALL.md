# 📦 Guia de Instalação Detalhado

Instruções passo a passo para instalar e configurar o Microkernel Media Player.

---

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

### Obrigatórios

- ✅ **Python 3.9 ou superior**
  - Download: https://www.python.org/downloads/
  - Verificar: `python --version`

- ✅ **Node.js 16 ou superior**
  - Download: https://nodejs.org/
  - Verificar: `node --version`

- ✅ **npm** (vem com Node.js)
  - Verificar: `npm --version`

- ✅ **Git**
  - Download: https://git-scm.com/
  - Verificar: `git --version`

### Recomendados

- ⭐ **VS Code** ou editor de código preferido
- ⭐ **Postman** ou **Insomnia** para testar API

---

## 🚀 Instalação

### 1️⃣ Clone o Repositório

```bash
# HTTPS
git clone https://github.com/seu-usuario/microkernel-media-player.git

# SSH
git clone git@github.com:seu-usuario/microkernel-media-player.git

# Ou baixe o ZIP e extraia
```

### 2️⃣ Navegue até o diretório

```bash
cd microkernel-media-player
```

---

## 🐍 Configuração do Backend

### 1. Navegue para o diretório backend

```bash
cd backend
```

### 2. Crie um ambiente virtual

#### Windows

```bash
python -m venv venv
```

#### Linux/Mac

```bash
python3 -m venv venv
```

### 3. Ative o ambiente virtual

#### Windows (CMD)

```bash
venv\Scripts\activate
```

#### Windows (PowerShell)

```bash
venv\Scripts\Activate.ps1
```

**Nota:** Se encontrar erro de permissão no PowerShell:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### 4. Verifique se o ambiente está ativo

Você deve ver `(venv)` no início da linha de comando:

```bash
(venv) C:\projetos\arquitetura\microkernel\backend>
```

### 5. Atualize pip (recomendado)

```bash
python -m pip install --upgrade pip
```

### 6. Instale as dependências

```bash
pip install -r requirements.txt
```

**Dependências instaladas:**
- FastAPI 0.104.1
- Uvicorn 0.24.0
- Pydantic 2.5.0
- Mutagen 1.47.0
- OpenCV-Python 4.8.1.78
- Python-magic-bin 0.4.14
- Aiofiles 23.2.1

### 7. Verifique a instalação

```bash
python -c "import fastapi; print(f'FastAPI {fastapi.__version__} instalado com sucesso!')"
```

### 8. Crie o diretório de storage (se não existir)

```bash
# Windows
mkdir storage\uploads

# Linux/Mac
mkdir -p storage/uploads
```

### 9. Teste o backend

```bash
python main.py
```

**Saída esperada:**
```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### 10. Acesse a documentação

Abra no navegador:
- http://localhost:8000/docs (Swagger)
- http://localhost:8000/redoc (ReDoc)

### 11. Pare o servidor

Pressione `Ctrl+C`

---

## ⚛️ Configuração do Frontend

### 1. Navegue para o diretório frontend

**Em um NOVO terminal** (mantenha o backend rodando se quiser):

```bash
cd frontend
```

### 2. Instale as dependências

#### Usando npm

```bash
npm install
```

#### Usando yarn (alternativa)

```bash
yarn install
```

**Dependências instaladas:**
- React 18.2.0
- React DOM 18.2.0
- Vite 5.0.0
- TailwindCSS 3.3.5
- Axios 1.6.0
- React Player 2.13.0
- Lucide React 0.294.0

### 3. Verifique a instalação

```bash
npm list react
```

### 4. Teste o frontend

```bash
npm run dev
```

**Saída esperada:**
```
  VITE v5.0.0  ready in 1234 ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
```

### 5. Acesse a aplicação

Abra no navegador: http://localhost:3000

---

## ✅ Verificação Completa

Execute este checklist para garantir que tudo está funcionando:

### Backend

- [ ] Ambiente virtual ativado
- [ ] Dependências instaladas
- [ ] Servidor iniciando sem erros
- [ ] Acesso a http://localhost:8000/docs
- [ ] API respondendo em http://localhost:8000/api/health

**Teste:**
```bash
curl http://localhost:8000/api/health
```

**Resposta esperada:**
```json
{
  "status": "healthy",
  "plugins_loaded": 3,
  "storage_path": "./storage/uploads"
}
```

### Frontend

- [ ] Node modules instalados
- [ ] Servidor dev rodando
- [ ] Acesso a http://localhost:3000
- [ ] Página carregando sem erros
- [ ] Console do navegador sem erros

---

## 🔧 Resolução de Problemas

### Backend

#### Erro: `ModuleNotFoundError: No module named 'fastapi'`

**Causa:** Ambiente virtual não ativado ou dependências não instaladas

**Solução:**
```bash
# Ative o ambiente virtual
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Reinstale dependências
pip install -r requirements.txt
```

#### Erro: `Address already in use`

**Causa:** Porta 8000 já está em uso

**Solução:**
```bash
# Encontre o processo usando a porta
netstat -ano | findstr :8000  # Windows
lsof -i :8000  # Linux/Mac

# Mate o processo ou use outra porta
# Em main.py, mude: uvicorn.run(..., port=8001)
```

#### Erro: `opencv-python` não instala

**Solução Windows:**
```bash
pip install opencv-python --no-cache-dir
```

**Solução Linux:**
```bash
sudo apt-get install python3-opencv
pip install opencv-python
```

#### Erro: `python-magic-bin` não encontrado

**Solução Windows:**
```bash
pip install python-magic-bin==0.4.14
```

**Solução Linux:**
```bash
sudo apt-get install libmagic1
pip install python-magic
```

### Frontend

#### Erro: `npm: command not found`

**Causa:** Node.js não instalado ou não está no PATH

**Solução:** Reinstale Node.js de https://nodejs.org/

#### Erro: `EACCES: permission denied`

**Solução Linux/Mac:**
```bash
sudo chown -R $USER:$GROUP ~/.npm
sudo chown -R $USER:$GROUP ~/.config
```

#### Erro: `network timeout`

**Solução:** Use outro registry do npm
```bash
npm config set registry https://registry.npmjs.org/
npm install
```

#### Erro: Port 3000 já em uso

**Solução:**
```bash
# Vite irá automaticamente usar outra porta (3001, 3002, etc)
# Ou defina manualmente em vite.config.js:
# server: { port: 3001 }
```

#### Erro: `Failed to resolve import`

**Causa:** node_modules corrompido

**Solução:**
```bash
rm -rf node_modules package-lock.json  # Linux/Mac
# ou
rmdir /s node_modules & del package-lock.json  # Windows

npm install
```

---

## 🐳 Instalação com Docker (Opcional)

### Dockerfile Backend

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
```

### Dockerfile Frontend

```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json .
RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev", "--", "--host"]
```

### Docker Compose

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/app
      - ./backend/storage:/app/storage

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend
    environment:
      - VITE_API_URL=http://localhost:8000
```

**Executar:**
```bash
docker-compose up
```

---

## 📝 Variáveis de Ambiente (Opcional)

### Backend

Crie `.env` em `backend/`:

```env
# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True

# Storage
STORAGE_PATH=./storage/uploads
MAX_UPLOAD_SIZE=524288000  # 500MB

# CORS
CORS_ORIGINS=http://localhost:3000,http://localhost:5173
```

### Frontend

Crie `.env` em `frontend/`:

```env
VITE_API_URL=http://localhost:8000/api
VITE_APP_NAME=Microkernel Media Player
```

---

## 🎯 Próximos Passos

Após instalação completa:

1. ✅ Leia o [README.md](README.md) para entender a arquitetura
2. ✅ Teste a aplicação seguindo [QUICK_START.md](QUICK_START.md)
3. ✅ Explore a [API](API_EXAMPLES.md)
4. ✅ Crie seu próprio plugin usando [PLUGIN_TEMPLATE.py](backend/plugins/PLUGIN_TEMPLATE.py)

---

## 📦 Comandos Úteis

### Backend

```bash
# Ativar ambiente virtual
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Desativar ambiente virtual
deactivate

# Instalar nova dependência
pip install nome-do-pacote
pip freeze > requirements.txt  # Atualizar requirements

# Limpar cache
pip cache purge

# Verificar dependências
pip list
```

### Frontend

```bash
# Instalar dependência
npm install nome-do-pacote

# Instalar dependência de desenvolvimento
npm install -D nome-do-pacote

# Remover dependência
npm uninstall nome-do-pacote

# Limpar cache
npm cache clean --force

# Verificar dependências
npm list

# Build para produção
npm run build

# Preview do build
npm run preview
```

---

## 🔐 Segurança

### Produção

Antes de fazer deploy em produção:

1. **Mude `DEBUG=False`** em config.py
2. **Configure CORS** adequadamente (não use `*`)
3. **Use HTTPS**
4. **Configure limites de upload**
5. **Implemente autenticação**
6. **Use variáveis de ambiente** para secrets
7. **Configure firewall**
8. **Use gunicorn** ao invés de uvicorn direto

---

## 📞 Suporte

Se continuar tendo problemas:

1. Verifique os **logs** de erro
2. Consulte a **documentação** das bibliotecas
3. Procure no **Stack Overflow**
4. Abra uma **issue** no GitHub

---

<div align="center">

**Instalação completa! 🎉**

Consulte [QUICK_START.md](QUICK_START.md) para começar a usar.

</div>
