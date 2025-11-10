/**
 * Componente de upload de arquivos
 */
import { useState, useRef } from 'react';
import { Upload, File, X, CheckCircle, AlertCircle } from 'lucide-react';
import apiService from '../../services/api';
import { usePlayer } from '../../context/PlayerContext';

const FileUploader = ({ onUploadSuccess }) => {
  const [isDragging, setIsDragging] = useState(false);
  const [uploading, setUploading] = useState(false);
  const [uploadProgress, setUploadProgress] = useState(0);
  const [uploadStatus, setUploadStatus] = useState(null);
  const fileInputRef = useRef(null);
  const { addToPlaylist } = usePlayer();

  const handleDragOver = (e) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = (e) => {
    e.preventDefault();
    setIsDragging(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);

    const files = Array.from(e.dataTransfer.files);
    if (files.length > 0) {
      handleFileUpload(files[0]);
    }
  };

  const handleFileSelect = (e) => {
    const files = Array.from(e.target.files);
    if (files.length > 0) {
      handleFileUpload(files[0]);
    }
  };

  const handleFileUpload = async (file) => {
    setUploading(true);
    setUploadProgress(0);
    setUploadStatus(null);

    try {
      const result = await apiService.uploadMedia(file, (progress) => {
        setUploadProgress(progress);
      });

      if (result.success) {
        setUploadStatus({
          type: 'success',
          message: `Upload realizado com sucesso!`,
          data: result,
        });

        // Adiciona à playlist
        addToPlaylist({
          filename: result.filename,
          format: result.analysis.metadata.format,
          metadata: result.analysis.metadata,
          plugin_used: result.analysis.plugin_used,
        });

        if (onUploadSuccess) {
          onUploadSuccess(result);
        }

        // Limpa após 3 segundos
        setTimeout(() => {
          setUploadStatus(null);
          setUploadProgress(0);
        }, 3000);
      } else {
        setUploadStatus({
          type: 'error',
          message: result.error || 'Erro no upload',
        });
      }
    } catch (error) {
      setUploadStatus({
        type: 'error',
        message: error.message || 'Erro ao fazer upload',
      });
    } finally {
      setUploading(false);
      if (fileInputRef.current) {
        fileInputRef.current.value = '';
      }
    }
  };

  return (
    <div className="space-y-4">
      {/* Área de drop */}
      <div
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
        onClick={() => fileInputRef.current?.click()}
        className={`
          border-2 border-dashed rounded-lg p-8 text-center cursor-pointer
          transition-all duration-200
          ${isDragging
            ? 'border-blue-500 bg-blue-50 dark:bg-blue-900/20'
            : 'border-gray-300 dark:border-gray-700 hover:border-blue-400'
          }
          ${uploading ? 'pointer-events-none opacity-50' : ''}
        `}
      >
        <input
          ref={fileInputRef}
          type="file"
          className="hidden"
          onChange={handleFileSelect}
          accept=".mp3,.mp4,.m4v,.avi"
        />

        <Upload className="mx-auto mb-4 text-gray-400" size={48} />

        <p className="text-lg font-semibold text-gray-700 dark:text-gray-300 mb-2">
          Clique ou arraste arquivos aqui
        </p>

        <p className="text-sm text-gray-500 dark:text-gray-400">
          Formatos suportados: MP3, MP4, M4V, AVI
        </p>
      </div>

      {/* Barra de progresso */}
      {uploading && (
        <div className="space-y-2">
          <div className="flex justify-between text-sm text-gray-600 dark:text-gray-400">
            <span>Fazendo upload...</span>
            <span>{uploadProgress}%</span>
          </div>
          <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2">
            <div
              className="bg-blue-600 h-2 rounded-full transition-all duration-300"
              style={{ width: `${uploadProgress}%` }}
            />
          </div>
        </div>
      )}

      {/* Status do upload */}
      {uploadStatus && (
        <div
          className={`
            flex items-start gap-3 p-4 rounded-lg
            ${uploadStatus.type === 'success'
              ? 'bg-green-50 dark:bg-green-900/20 border border-green-200 dark:border-green-800'
              : 'bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800'
            }
          `}
        >
          {uploadStatus.type === 'success' ? (
            <CheckCircle className="text-green-600 flex-shrink-0" size={20} />
          ) : (
            <AlertCircle className="text-red-600 flex-shrink-0" size={20} />
          )}

          <div className="flex-1">
            <p className={`font-semibold ${
              uploadStatus.type === 'success' ? 'text-green-800 dark:text-green-300' : 'text-red-800 dark:text-red-300'
            }`}>
              {uploadStatus.message}
            </p>

            {uploadStatus.data && (
              <div className="mt-2 text-sm text-gray-600 dark:text-gray-400">
                <p>Arquivo: {uploadStatus.data.filename}</p>
                <p>Plugin usado: {uploadStatus.data.analysis.plugin_used}</p>
                <p>Formato: {uploadStatus.data.analysis.metadata.format.toUpperCase()}</p>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default FileUploader;
