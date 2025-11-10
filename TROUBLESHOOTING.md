# 🔧 Guia de Solução de Problemas

## ❌ Problemas Comuns e Soluções

---

## 🐍 Backend (Python/FastAPI)

### Problema 1: `pip: Fatal error in launcher`

**Erro:**
```
Fatal error in launcher: Unable to create process using '"C:\...\python.exe" "C:\...\pip.exe"'
```

**Causa:** Ambiente virtual não ativado corretamente

**Solução:**

```powershell
# PowerShell (Windows)
.\venv\Scripts\Activate.ps1

# Se der erro de permissão:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Depois ative novamente:
.\venv\Scripts\Activate.ps1

# Agora instale as dependências:
pip install -r requirements.txt
```

```bash
# CMD (Windows alternativo)
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

**Verificar se está ativado:**
Você deve ver `(venv)` no início da linha de comando:
```
(venv) PS C:\projetos\arquitetura\microkernel\backend>
```

---

### Problema 2: `ModuleNotFoundError: No module named 'fastapi'`

**Causa:** Dependências não instaladas ou ambiente virtual não ativado

**Solução:**
```bash
# 1. Ative o ambiente virtual
.\venv\Scripts\Activate.ps1  # PowerShell
# ou
venv\Scripts\activate  # CMD

# 2. Verifique se está ativo (deve mostrar (venv))
# 3. Reinstale as dependências
pip install -r requirements.txt
```

---

### Problema 3: `name 'MediaMetadataResponse' is not defined`

**Causa:** Import faltando em routes.py

**✅ JÁ CORRIGIDO!** O arquivo `backend/api/routes.py` foi atualizado com o import correto.

Se ainda ocorrer, reinicie o servidor:
```bash
# Pare o servidor (Ctrl+C)
# Inicie novamente
python main.py
```

---

### Problema 4: Porta 8000 já em uso

**Erro:**
```
Address already in use
```

**Solução:**

```powershell
# Windows - Encontrar o processo
netstat -ano | findstr :8000

# Matar o processo (substitua PID pelo número encontrado)
taskkill /PID <PID> /F
```

```bash
# Linux/Mac
lsof -i :8000
kill -9 <PID>
```

**Alternativa:** Usar outra porta

Edite `backend/main.py`:
```python
uvicorn.run(
    "main:app",
    host="0.0.0.0",
    port=8001,  # ← Mude para 8001
    reload=True
)
```

---

### Problema 5: `opencv-python` não instala

**Windows:**
```bash
pip install opencv-python==4.8.1.78 --no-cache-dir
```

**Linux:**
```bash
sudo apt-get update
sudo apt-get install python3-opencv
pip install opencv-python
```

---

### Problema 6: Storage directory não existe

**Erro:**
```
FileNotFoundError: [Errno 2] No such file or directory: './storage/uploads'
```

**Solução:**
```bash
# Windows (PowerShell)
New-Item -ItemType Directory -Path "storage\uploads" -Force

# Windows (CMD)
mkdir storage\uploads

# Linux/Mac
mkdir -p storage/uploads
```

---

## ⚛️ Frontend (React/Node)

### Problema 7: `npm: command not found`

**Causa:** Node.js não instalado

**Solução:**
1. Baixe e instale Node.js: https://nodejs.org/
2. Reinicie o terminal
3. Verifique: `node --version`

---

### Problema 8: `EACCES: permission denied` (npm)

**Linux/Mac:**
```bash
sudo chown -R $USER:$GROUP ~/.npm
sudo chown -R $USER:$GROUP ~/.config
```

**Windows:** Execute PowerShell como Administrador

---

### Problema 9: Porta 3000 já em uso

**Vite automaticamente usa outra porta** (3001, 3002, etc)

Ou defina manualmente em `frontend/vite.config.js`:
```javascript
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3001,  // ← Mude aqui
    // ...
  }
})
```

---

### Problema 10: CORS Error

**Erro no console do navegador:**
```
Access to XMLHttpRequest at 'http://localhost:8000/api/...' from origin
'http://localhost:3000' has been blocked by CORS policy
```

**Causa:** Backend não está rodando ou CORS mal configurado

**Solução:**

1. **Certifique-se que o backend está rodando:**
   ```bash
   # Em outro terminal
   cd backend
   .\venv\Scripts\Activate.ps1
   python main.py
   ```

2. **Verifique a configuração de CORS em `backend/main.py`:**
   ```python
   app.add_middleware(
       CORSMiddleware,
       allow_origins=["*"],  # Deve estar assim em desenvolvimento
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

---

### Problema 11: `Failed to resolve import`

**Causa:** node_modules corrompido

**Solução:**
```bash
# Windows (PowerShell)
Remove-Item -Recurse -Force node_modules
Remove-Item package-lock.json
npm install

# Linux/Mac
rm -rf node_modules package-lock.json
npm install
```

---

### Problema 12: Upload falha no frontend

**Erro:** "Erro no upload: ..."

**Soluções:**

1. **Backend está rodando?**
   ```bash
   curl http://localhost:8000/api/health
   ```

2. **Arquivo muito grande?**
   - Limite padrão: 500MB
   - Para mudar, edite `backend/config.py`

3. **Formato não suportado?**
   - Apenas: MP3, MP4, M4V, AVI
   - Verifique: `curl http://localhost:8000/api/formats`

4. **Arquivo corrompido?**
   - Tente outro arquivo

---

### Problema 13: Player não reproduz

**Soluções:**

1. **Verifique o console do navegador** (F12)

2. **Codec não suportado pelo navegador:**
   - MP3: ✅ Todos os navegadores
   - MP4 (H.264): ✅ Todos os navegadores
   - MP4 (HEVC): ❌ Apenas Safari
   - AVI: ⚠️ Depende do codec

3. **URL de streaming incorreta:**
   - Deve ser: `http://localhost:8000/api/media/stream/filename.mp3`

---

## 🔍 Verificação Rápida

### Backend

```bash
# 1. Ambiente virtual ativo?
# Deve mostrar (venv) no prompt

# 2. Dependências instaladas?
pip list | grep fastapi

# 3. Servidor rodando?
curl http://localhost:8000/api/health

# Resposta esperada:
# {
#   "status": "healthy",
#   "plugins_loaded": 3,
#   "storage_path": "./storage/uploads"
# }
```

### Frontend

```bash
# 1. Node instalado?
node --version
npm --version

# 2. Dependências instaladas?
ls node_modules | wc -l
# Deve mostrar número > 0

# 3. Servidor rodando?
# Acesse: http://localhost:3000
# Deve abrir a aplicação
```

---

## 🧪 Testes Rápidos

### Teste 1: Backend funcionando

```bash
# Health check
curl http://localhost:8000/api/health

# Listar plugins
curl http://localhost:8000/api/plugins

# Formatos suportados
curl http://localhost:8000/api/formats
```

### Teste 2: Upload via curl

```bash
# Substitua /path/to/file.mp3 por um arquivo real
curl -X POST http://localhost:8000/api/upload \
  -F "file=@/path/to/file.mp3"
```

### Teste 3: Frontend funcionando

1. Abra http://localhost:3000
2. Vá para aba "Plugins"
3. Deve mostrar 3 plugins (MP3, MP4, AVI)
4. Vá para aba "Upload"
5. Faça upload de um MP3
6. Deve aparecer mensagem de sucesso

---

## 📞 Ainda com Problemas?

### Logs do Backend

Verifique os logs no terminal onde o backend está rodando:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Plugin registrado: MP3 Audio Plugin
ERROR:    Erro ao extrair metadados: ...
```

### Logs do Frontend

Abra o Console do Navegador (F12):
- Erros aparecem em vermelho
- Requisições de rede na aba "Network"

### Verificar Versões

```bash
# Python
python --version
# Deve ser 3.9+

# Node
node --version
# Deve ser 16+

# Pip
pip --version
```

---

## 🔄 Reset Completo

Se nada funcionar, reset completo:

### Backend

```bash
cd backend

# Remove ambiente virtual
rm -rf venv  # Linux/Mac
Remove-Item -Recurse -Force venv  # Windows PowerShell

# Remove cache Python
rm -rf __pycache__
rm -rf */__pycache__

# Recria tudo
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
python main.py
```

### Frontend

```bash
cd frontend

# Remove node_modules
rm -rf node_modules package-lock.json  # Linux/Mac
Remove-Item -Recurse -Force node_modules, package-lock.json  # Windows

# Reinstala
npm install
npm run dev
```

---

## ✅ Checklist de Verificação

Backend:
- [ ] Python 3.9+ instalado
- [ ] Ambiente virtual criado
- [ ] Ambiente virtual ativado (mostra `(venv)`)
- [ ] Dependências instaladas
- [ ] Diretório `storage/uploads` existe
- [ ] Servidor rodando na porta 8000
- [ ] `curl http://localhost:8000/api/health` funciona

Frontend:
- [ ] Node.js 16+ instalado
- [ ] npm instalado
- [ ] Dependências instaladas (`node_modules` existe)
- [ ] Servidor rodando na porta 3000
- [ ] Navegador abre http://localhost:3000
- [ ] Sem erros no console (F12)

---

## 📚 Documentação Adicional

- **Instalação Detalhada:** [INSTALL.md](INSTALL.md)
- **Início Rápido:** [QUICK_START.md](QUICK_START.md)
- **Exemplos de API:** [API_EXAMPLES.md](API_EXAMPLES.md)

---

<div align="center">

**Problema não listado aqui?**

Verifique os logs detalhados e consulte a documentação das bibliotecas.

</div>
