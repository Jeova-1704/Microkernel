/**
 * Lista de plugins registrados no sistema
 */
import { Package, CheckCircle, Loader } from 'lucide-react';
import { usePlugins } from '../../hooks/usePlugins';
import PluginCard from './PluginCard';

const PluginList = () => {
  const { plugins, supportedFormats, loading, error } = usePlugins();

  if (loading) {
    return (
      <div className="flex items-center justify-center p-8">
        <Loader className="animate-spin text-blue-500" size={32} />
        <span className="ml-3 text-gray-600 dark:text-gray-400">
          Carregando plugins...
        </span>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-lg p-4">
        <p className="text-red-800 dark:text-red-300">
          Erro ao carregar plugins: {error}
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-4">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-gray-800 dark:text-white flex items-center gap-2">
            <Package size={28} />
            Plugins Registrados
          </h2>
          <p className="text-sm text-gray-600 dark:text-gray-400 mt-1">
            {plugins.length} plugin(s) disponível(is)
          </p>
        </div>

        <div className="flex items-center gap-2 bg-green-50 dark:bg-green-900/20 px-4 py-2 rounded-lg">
          <CheckCircle className="text-green-600" size={20} />
          <span className="text-sm font-semibold text-green-800 dark:text-green-300">
            Sistema Operacional
          </span>
        </div>
      </div>

      {/* Formatos suportados */}
      <div className="bg-blue-50 dark:bg-blue-900/20 border border-blue-200 dark:border-blue-800 rounded-lg p-4">
        <h3 className="font-semibold text-blue-900 dark:text-blue-300 mb-2">
          Formatos Suportados
        </h3>
        <div className="flex flex-wrap gap-2">
          {supportedFormats.map((format) => (
            <span
              key={format}
              className="px-3 py-1 bg-blue-100 dark:bg-blue-900/40 text-blue-800 dark:text-blue-300 rounded-full text-sm font-medium"
            >
              .{format}
            </span>
          ))}
        </div>
      </div>

      {/* Lista de plugins */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {plugins.map((plugin) => (
          <PluginCard key={plugin.name} plugin={plugin} />
        ))}
      </div>
    </div>
  );
};

export default PluginList;
