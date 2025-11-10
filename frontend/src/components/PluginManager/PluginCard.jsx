/**
 * Card individual de plugin
 */
import { Package, User, Hash, FileType } from 'lucide-react';

const PluginCard = ({ plugin }) => {
  return (
    <div className="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-lg p-4 hover:shadow-lg transition-shadow">
      {/* Header */}
      <div className="flex items-start gap-3 mb-3">
        <div className="p-2 bg-blue-100 dark:bg-blue-900/40 rounded-lg">
          <Package className="text-blue-600 dark:text-blue-400" size={24} />
        </div>
        <div className="flex-1">
          <h3 className="font-semibold text-gray-800 dark:text-white">
            {plugin.name}
          </h3>
          <p className="text-sm text-gray-500 dark:text-gray-400">
            v{plugin.version}
          </p>
        </div>
      </div>

      {/* Descrição */}
      <p className="text-sm text-gray-600 dark:text-gray-400 mb-4">
        {plugin.description}
      </p>

      {/* Metadados */}
      <div className="space-y-2 text-sm">
        <div className="flex items-center gap-2 text-gray-600 dark:text-gray-400">
          <User size={16} />
          <span>{plugin.author}</span>
        </div>

        <div className="flex items-center gap-2">
          <FileType size={16} className="text-gray-600 dark:text-gray-400" />
          <div className="flex flex-wrap gap-1">
            {plugin.supported_formats.map((format) => (
              <span
                key={format}
                className="px-2 py-0.5 bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded text-xs font-medium"
              >
                {format.toUpperCase()}
              </span>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default PluginCard;
