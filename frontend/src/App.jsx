/**
 * Componente principal da aplicação
 */
import { useState } from 'react';
import { PlayerProvider } from './context/PlayerContext';
import Player from './components/Player/Player';
import FileUploader from './components/FileUploader/FileUploader';
import PluginList from './components/PluginManager/PluginList';
import { Music, Upload, Package } from 'lucide-react';

function App() {
  const [activeTab, setActiveTab] = useState('player');

  const tabs = [
    { id: 'player', label: 'Player', icon: Music },
    { id: 'upload', label: 'Upload', icon: Upload },
    { id: 'plugins', label: 'Plugins', icon: Package },
  ];

  return (
    <PlayerProvider>
      <div className="min-h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900">
        {/* Header */}
        <header className="bg-gray-900/50 backdrop-blur-sm border-b border-gray-700">
          <div className="container mx-auto px-4 py-6">
            <div className="flex items-center justify-between">
              <div>
                <h1 className="text-3xl font-bold text-white flex items-center gap-3">
                  🎵 Microkernel Media Player
                </h1>
                <p className="text-gray-400 mt-1">
                  Arquitetura baseada em plugins
                </p>
              </div>

              <div className="bg-green-500/20 text-green-400 px-4 py-2 rounded-lg border border-green-500/30">
                <span className="text-sm font-semibold">Sistema Ativo</span>
              </div>
            </div>
          </div>
        </header>

        {/* Navigation */}
        <nav className="bg-gray-800/50 backdrop-blur-sm border-b border-gray-700">
          <div className="container mx-auto px-4">
            <div className="flex gap-1">
              {tabs.map((tab) => {
                const Icon = tab.icon;
                return (
                  <button
                    key={tab.id}
                    onClick={() => setActiveTab(tab.id)}
                    className={`
                      flex items-center gap-2 px-6 py-3 font-semibold transition-all
                      ${activeTab === tab.id
                        ? 'bg-gray-900 text-white border-b-2 border-blue-500'
                        : 'text-gray-400 hover:text-white hover:bg-gray-800/50'
                      }
                    `}
                  >
                    <Icon size={20} />
                    {tab.label}
                  </button>
                );
              })}
            </div>
          </div>
        </nav>

        {/* Main Content */}
        <main className="container mx-auto px-4 py-8">
          <div className="max-w-6xl mx-auto">
            {activeTab === 'player' && (
              <div className="space-y-6">
                <div>
                  <h2 className="text-2xl font-bold text-white mb-2">
                    Reprodutor de Mídia
                  </h2>
                  <p className="text-gray-400">
                    Reproduza seus arquivos de áudio e vídeo
                  </p>
                </div>
                <Player />
              </div>
            )}

            {activeTab === 'upload' && (
              <div className="space-y-6">
                <div>
                  <h2 className="text-2xl font-bold text-white mb-2">
                    Upload de Arquivos
                  </h2>
                  <p className="text-gray-400">
                    Envie arquivos de mídia para o sistema
                  </p>
                </div>
                <div className="bg-gray-800 rounded-lg p-6">
                  <FileUploader
                    onUploadSuccess={() => {
                      // Poderia atualizar lista de arquivos aqui
                    }}
                  />
                </div>
              </div>
            )}

            {activeTab === 'plugins' && (
              <div className="space-y-6">
                <PluginList />
              </div>
            )}
          </div>
        </main>

        {/* Footer */}
        <footer className="bg-gray-900/50 backdrop-blur-sm border-t border-gray-700 mt-12">
          <div className="container mx-auto px-4 py-6">
            <div className="text-center text-gray-400 text-sm">
              <p>
                Microkernel Media Player - Arquitetura de Software
              </p>
              <p className="mt-1">
                Desenvolvido com React + FastAPI + Padrão Microkernel
              </p>
            </div>
          </div>
        </footer>
      </div>
    </PlayerProvider>
  );
}

export default App;
