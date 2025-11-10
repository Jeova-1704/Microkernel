/**
 * Serviço de comunicação com a API Backend
 * Encapsula todas as chamadas HTTP
 */
import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

/**
 * Serviço de API
 */
export const apiService = {
  /**
   * Obtém informações do sistema
   */
  async getSystemInfo() {
    const response = await api.get('/');
    return response.data;
  },

  /**
   * Lista todos os plugins registrados
   */
  async getPlugins() {
    const response = await api.get('/plugins');
    return response.data;
  },

  /**
   * Lista formatos suportados
   */
  async getSupportedFormats() {
    const response = await api.get('/formats');
    return response.data;
  },

  /**
   * Faz upload de arquivo de mídia
   */
  async uploadMedia(file, onProgress) {
    const formData = new FormData();
    formData.append('file', file);

    const response = await api.post('/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      onUploadProgress: (progressEvent) => {
        if (onProgress) {
          const percentCompleted = Math.round(
            (progressEvent.loaded * 100) / progressEvent.total
          );
          onProgress(percentCompleted);
        }
      },
    });

    return response.data;
  },

  /**
   * Lista arquivos de mídia
   */
  async listMediaFiles() {
    const response = await api.get('/media');
    return response.data;
  },

  /**
   * Analisa um arquivo específico
   */
  async analyzeMedia(filename) {
    const response = await api.get(`/media/${filename}/analyze`);
    return response.data;
  },

  /**
   * Valida um arquivo
   */
  async validateMedia(filename) {
    const response = await api.get(`/media/${filename}/validate`);
    return response.data;
  },

  /**
   * Obtém URL de streaming
   */
  getStreamUrl(filename) {
    return `${API_BASE_URL}/media/stream/${filename}`;
  },

  /**
   * Remove arquivo de mídia
   */
  async deleteMedia(filename) {
    const response = await api.delete(`/media/${filename}`);
    return response.data;
  },

  /**
   * Health check
   */
  async healthCheck() {
    const response = await api.get('/health');
    return response.data;
  },
};

export default apiService;
