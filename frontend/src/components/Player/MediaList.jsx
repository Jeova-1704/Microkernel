/**
 * Lista de arquivos de mídia disponíveis
 */
import { Play, Music, Film, Trash2 } from 'lucide-react';
import { usePlayer } from '../../context/PlayerContext';
import apiService from '../../services/api';
import { useState, useEffect } from 'react';

const MediaList = () => {
  const { playlist, currentMedia, playMedia, removeFromPlaylist } = usePlayer();
  const [allMedia, setAllMedia] = useState([]);
  const [loading, setLoading] = useState(true);

  // Carrega lista de arquivos do servidor
  useEffect(() => {
    loadMediaFiles();
  }, []);

  const loadMediaFiles = async () => {
    try {
      setLoading(true);
      const files = await apiService.listMediaFiles();
      setAllMedia(files);
    } catch (error) {
      console.error('Erro ao carregar arquivos:', error);
    } finally {
      setLoading(false);
    }
  };

  const handlePlay = async (file) => {
    try {
      // Analisa o arquivo para obter metadados completos
      const analysis = await apiService.analyzeMedia(file.filename);

      if (analysis.success) {
        playMedia({
          filename: file.filename,
          format: analysis.metadata.format,
          metadata: analysis.metadata,
          plugin_used: analysis.plugin_used,
        });
      }
    } catch (error) {
      console.error('Erro ao analisar arquivo:', error);
    }
  };

  const handleDelete = async (filename) => {
    if (confirm(`Deseja realmente excluir "${filename}"?`)) {
      try {
        await apiService.deleteMedia(filename);
        removeFromPlaylist(filename);
        loadMediaFiles(); // Recarrega lista
      } catch (error) {
        console.error('Erro ao excluir arquivo:', error);
      }
    }
  };

  const formatFileSize = (bytes) => {
    if (bytes < 1024) return bytes + ' B';
    if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
    return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
  };

  const getIcon = (file) => {
    const format = file.filename.split('.').pop().toLowerCase();
    if (['mp3', 'wav', 'flac'].includes(format)) {
      return <Music className="text-blue-400" size={24} />;
    }
    return <Film className="text-purple-400" size={24} />;
  };

  if (loading) {
    return (
      <div className="bg-gray-800 rounded-lg p-8 text-center">
        <p className="text-gray-400">Carregando arquivos...</p>
      </div>
    );
  }

  if (allMedia.length === 0) {
    return (
      <div className="bg-gray-800 rounded-lg p-8 text-center">
        <Music className="mx-auto mb-4 text-gray-600" size={48} />
        <p className="text-gray-400 text-lg">Nenhum arquivo encontrado</p>
        <p className="text-gray-500 mt-2">
          Faça upload de arquivos na aba "Upload"
        </p>
      </div>
    );
  }

  return (
    <div className="bg-gray-800 rounded-lg overflow-hidden">
      <div className="p-4 border-b border-gray-700">
        <h3 className="text-white font-semibold text-lg">
          Biblioteca de Mídia ({allMedia.length})
        </h3>
        <p className="text-gray-400 text-sm mt-1">
          Clique em um arquivo para reproduzir
        </p>
      </div>

      <div className="divide-y divide-gray-700">
        {allMedia.map((file) => {
          const isPlaying = currentMedia?.filename === file.filename;

          return (
            <div
              key={file.filename}
              className={`
                p-4 flex items-center gap-4 hover:bg-gray-700/50 transition-colors
                ${isPlaying ? 'bg-blue-900/30 border-l-4 border-blue-500' : ''}
              `}
            >
              {/* Ícone */}
              <div className="flex-shrink-0">
                {getIcon(file)}
              </div>

              {/* Informações */}
              <div className="flex-1 min-w-0">
                <h4 className={`font-medium truncate ${
                  isPlaying ? 'text-blue-400' : 'text-white'
                }`}>
                  {file.filename}
                </h4>
                <div className="flex gap-3 mt-1 text-xs text-gray-400">
                  <span>{formatFileSize(file.size)}</span>
                  {file.supported && file.plugin && (
                    <span className="text-green-400">• {file.plugin}</span>
                  )}
                  {!file.supported && (
                    <span className="text-red-400">• Formato não suportado</span>
                  )}
                </div>
              </div>

              {/* Ações */}
              <div className="flex gap-2 flex-shrink-0">
                {file.supported && (
                  <button
                    onClick={() => handlePlay(file)}
                    className={`
                      p-2 rounded-full transition-colors
                      ${isPlaying
                        ? 'bg-blue-600 text-white'
                        : 'bg-gray-700 text-gray-300 hover:bg-gray-600 hover:text-white'
                      }
                    `}
                    title="Reproduzir"
                  >
                    <Play size={16} fill={isPlaying ? 'white' : 'none'} />
                  </button>
                )}

                <button
                  onClick={() => handleDelete(file.filename)}
                  className="p-2 rounded-full bg-gray-700 text-gray-300 hover:bg-red-600 hover:text-white transition-colors"
                  title="Excluir"
                >
                  <Trash2 size={16} />
                </button>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default MediaList;
