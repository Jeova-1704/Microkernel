# 🎵 Como Usar o Microkernel Media Player

Guia completo de uso da aplicação.

---

## 🚀 Antes de começar

Certifique-se de que **Backend** e **Frontend** estão rodando:

**Terminal 1 - Backend:**
```powershell
.\start_backend.ps1
```
→ http://localhost:8000

**Terminal 2 - Frontend:**
```powershell
.\start_frontend.ps1
```
→ http://localhost:3000

---

## 📱 Interface da Aplicação

A aplicação possui **3 abas principais**:

### 1️⃣ Player - Reproduzir Mídia
### 2️⃣ Upload - Enviar Arquivos
### 3️⃣ Plugins - Ver Plugins Disponíveis

---

## 🎬 Como Reproduzir uma Música/Vídeo

### Passo 1: Faça Upload do Arquivo

1. Acesse http://localhost:3000
2. Clique na aba **"Upload"**
3. **Arraste e solte** um arquivo (MP3, MP4, AVI) ou **clique para selecionar**
4. Aguarde o upload (verá a barra de progresso)
5. Quando concluir, verá: ✅ "Upload realizado com sucesso!"

### Passo 2: Vá para o Player

1. Clique na aba **"Player"**
2. Você verá **duas seções**:

#### Seção Superior: Player
- Controles de reprodução (Play, Pause, Volume)
- Informações da música (título, artista, formato)
- Timeline (barra de progresso)

#### Seção Inferior: Biblioteca de Mídia
- Lista de **TODOS os arquivos** disponíveis
- Cada arquivo tem um botão ▶️ **Play**

### Passo 3: Reproduzir

**Opção A:** Se o arquivo foi adicionado após upload:
- Ele já estará na lista da biblioteca
- Clique no botão ▶️ **Play** ao lado do arquivo

**Opção B:** Selecionar arquivo da biblioteca:
- Role a lista e encontre o arquivo
- Clique no botão ▶️ **Play**

### Passo 4: Controlar a Reprodução

- **▶️ Play/Pause**: Controla a reprodução
- **Volume**: Arraste o controle de volume
- **Timeline**: Clique na barra para pular para outra parte
- **⏮ ⏭**: Botões de skip (ainda não implementados)

---

## 📤 Como Fazer Upload

### Método 1: Arrastar e Soltar

1. Vá para a aba **"Upload"**
2. Arraste um arquivo (MP3, MP4, AVI) para a área tracejada
3. O upload iniciará automaticamente

### Método 2: Selecionar Arquivo

1. Vá para a aba **"Upload"**
2. Clique na área tracejada "Clique ou arraste arquivos aqui"
3. Selecione o arquivo no explorador
4. O upload iniciará automaticamente

### Formatos Suportados

✅ **Áudio:**
- MP3 (com tags ID3)

✅ **Vídeo:**
- MP4 / M4V (H.264, HEVC)
- AVI (múltiplos codecs)

### Durante o Upload

Você verá:
- **Barra de progresso** mostrando o percentual
- "Fazendo upload... X%"

### Após o Upload

Você verá:
- ✅ Mensagem de sucesso verde
- Nome do arquivo
- Plugin usado (ex: "MP3 Audio Plugin")
- Formato

**Importante:** Após o upload, **vá para a aba "Player"** para reproduzir!

---

## 🔌 Como Ver Plugins Disponíveis

1. Clique na aba **"Plugins"**
2. Você verá:

### Informações do Sistema
- Quantidade de plugins carregados
- Status do sistema (verde = ativo)

### Formatos Suportados
- Lista de extensões aceitas (.mp3, .mp4, .avi)

### Cards dos Plugins

Cada plugin mostra:
- **Nome**: Ex: "MP3 Audio Plugin"
- **Versão**: Ex: "v1.0.0"
- **Descrição**: O que o plugin faz
- **Autor**: Quem desenvolveu
- **Formatos**: Extensões que processa

### Plugins Incluídos

1. **MP3 Audio Plugin** 🎵
   - Processa arquivos MP3
   - Extrai tags ID3 (título, artista, álbum)
   - Formatos: MP3

2. **MP4 Video Plugin** 🎬
   - Processa vídeos MP4/M4V
   - Suporta H.264 e HEVC
   - Formatos: MP4, M4V

3. **AVI Video Plugin** 📹
   - Processa vídeos AVI
   - Múltiplos codecs
   - Formatos: AVI

---

## 🎵 Gerenciando a Biblioteca

### Ver Todos os Arquivos

1. Vá para a aba **"Player"**
2. Role para baixo até **"Biblioteca de Mídia"**
3. Verá lista de todos os arquivos carregados

### Informações Exibidas

Para cada arquivo:
- **Ícone**: 🎵 (áudio) ou 🎬 (vídeo)
- **Nome do arquivo**
- **Tamanho** (em KB ou MB)
- **Plugin usado** (em verde)
- **Status** (suportado ou não)

### Reproduzir da Biblioteca

- Clique no botão **▶️ Play** ao lado do arquivo
- O player acima carregará o arquivo automaticamente

### Excluir Arquivo

- Clique no botão **🗑️ Trash** ao lado do arquivo
- Confirme a exclusão
- O arquivo será removido do servidor

### Arquivo em Reprodução

O arquivo atualmente tocando terá:
- **Borda azul** à esquerda
- **Fundo azul claro**
- **Botão Play preenchido** em azul

---

## 🎨 Interface do Player

### Player de Áudio (MP3)

Quando reproduzindo áudio:
- 🎵 **Ícone grande** de música
- **Título** da música (se disponível nas tags ID3)
- **Artista** (se disponível)
- Controles na parte inferior

### Player de Vídeo (MP4, AVI)

Quando reproduzindo vídeo:
- **Vídeo** exibido em tela cheia
- Controles na parte inferior

### Informações da Mídia

Abaixo do player, você vê:
- **Nome do arquivo**
- **Formato** (MP3, MP4, AVI)
- **Codec** (MP3, H.264, etc)
- **Resolução** (para vídeos: 1920x1080)
- **Plugin usado** (em verde)

### Controles

#### Timeline (Barra de Progresso)
- Mostra tempo atual vs. tempo total
- Clique para pular para outra parte

#### Botões
- **⏮**: Voltar (ainda não implementado)
- **▶️/⏸**: Play/Pause
- **⏭**: Avançar (ainda não implementado)

#### Volume
- **🔊**: Ícone de volume
- **Barra deslizante**: Arraste para ajustar (0% a 100%)

---

## ❓ Perguntas Frequentes

### P: Upload concluiu, mas não aparece no player?

**R:** Vá para a aba **"Player"** e role até **"Biblioteca de Mídia"**. Clique no botão ▶️ Play ao lado do arquivo.

---

### P: Arquivo está na lista mas não toca?

**R:** Verifique se:
1. Backend está rodando (http://localhost:8000)
2. Formato é suportado (MP3, MP4, AVI)
3. Arquivo não está corrompido

---

### P: Vídeo não reproduz no navegador?

**R:** Alguns codecs podem não ser suportados pelo navegador:
- **MP4 (H.264)**: ✅ Todos os navegadores
- **MP4 (HEVC/H.265)**: ⚠️ Apenas Safari
- **AVI**: ⚠️ Depende do codec interno

---

### P: Como voltar ao início da música?

**R:** Clique no início da barra de progresso (timeline).

---

### P: Posso adicionar mais formatos?

**R:** Sim! Consulte o arquivo `backend/plugins/PLUGIN_TEMPLATE.py` para criar novos plugins.

---

### P: Onde os arquivos são armazenados?

**R:** No servidor, em `backend/storage/uploads/`

---

### P: Como remover um arquivo?

**R:** Na aba "Player", na lista de arquivos, clique no botão 🗑️ ao lado do arquivo.

---

## 🔧 Atalhos de Teclado

Atualmente não implementados, mas planejados:
- `Espaço`: Play/Pause
- `←/→`: Voltar/Avançar 5 segundos
- `↑/↓`: Aumentar/Diminuir volume

---

## 🐛 Resolução de Problemas

### Arquivo não aparece após upload?

1. Verifique se o upload foi concluído (mensagem verde)
2. Vá para a aba "Player"
3. Role até "Biblioteca de Mídia"
4. Atualize a página se necessário (F5)

### Player mostra "Nenhuma mídia selecionada"?

Isso é normal! Significa que você ainda não clicou em nenhum arquivo. Vá até a "Biblioteca de Mídia" abaixo e clique em um arquivo.

### Erro CORS ou Network Error?

Backend não está rodando. Inicie:
```powershell
.\start_backend.ps1
```

### Música não toca?

1. Abra o Console do navegador (F12)
2. Veja se há erros em vermelho
3. Verifique se a URL de streaming está correta

---

## 📱 Fluxo Completo de Uso

```
1. Inicie Backend e Frontend
   ↓
2. Acesse http://localhost:3000
   ↓
3. Vá para aba "Upload"
   ↓
4. Envie um arquivo MP3/MP4/AVI
   ↓
5. Aguarde upload completar
   ↓
6. Vá para aba "Player"
   ↓
7. Role até "Biblioteca de Mídia"
   ↓
8. Clique no botão ▶️ Play do arquivo
   ↓
9. Controle a reprodução!
```

---

## 🎓 Recursos Adicionais

- **API Docs**: http://localhost:8000/docs
- **Documentação**: [README.md](README.md)
- **Problemas**: [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

---

<div align="center">

**Divirta-se usando o Microkernel Media Player! 🎵**

</div>
