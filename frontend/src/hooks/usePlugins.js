/**
 * Hook customizado para gerenciar plugins
 */
import { useState, useEffect } from 'react';
import apiService from '../services/api';

export const usePlugins = () => {
  const [plugins, setPlugins] = useState([]);
  const [supportedFormats, setSupportedFormats] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchPlugins = async () => {
    try {
      setLoading(true);
      const [pluginsData, formatsData] = await Promise.all([
        apiService.getPlugins(),
        apiService.getSupportedFormats(),
      ]);
      setPlugins(pluginsData);
      setSupportedFormats(formatsData);
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchPlugins();
  }, []);

  return {
    plugins,
    supportedFormats,
    loading,
    error,
    refetch: fetchPlugins,
  };
};
