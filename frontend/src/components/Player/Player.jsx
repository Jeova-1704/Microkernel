/**
 * Componente principal do player de mídia
 */
import { useRef, useEffect } from 'react';
import ReactPlayer from 'react-player';
import { usePlayer } from '../../context/PlayerContext';
import Controls from './Controls';
import apiService from '../../services/api';

const Player = () => {
  const playerRef = useRef(null);
  const { currentMedia, isPlaying, volume, setCurrentTime, setDuration } = usePlayer();

  const handleProgress = (state) => {
    setCurrentTime(state.playedSeconds);
  };

  const handleDuration = (duration) => {
    setDuration(duration);
  };

  if (!currentMedia) {
    return (
      <div className="bg-gray-800 rounded-lg p-12 text-center">
        <div className="text-gray-400 text-xl">
          Nenhuma mídia selecionada
        </div>
        <div className="text-gray-500 mt-2">
          Faça upload ou selecione um arquivo para reproduzir
        </div>
      </div>
    );
  }

  const streamUrl = apiService.getStreamUrl(currentMedia.filename);
  const isVideo = ['mp4', 'm4v', 'avi'].includes(currentMedia.format);

  return (
    <div className="bg-gray-800 rounded-lg overflow-hidden">
      {/* Player */}
      <div className={`relative ${isVideo ? 'aspect-video' : 'h-64'} bg-black flex items-center justify-center`}>
        {isVideo ? (
          <ReactPlayer
            ref={playerRef}
            url={streamUrl}
            playing={isPlaying}
            volume={volume}
            width="100%"
            height="100%"
            onProgress={handleProgress}
            onDuration={handleDuration}
            controls={false}
          />
        ) : (
          <div className="text-center">
            <div className="text-6xl mb-4">🎵</div>
            <div className="text-white text-xl font-semibold">
              {currentMedia.metadata?.extra_info?.title || currentMedia.filename}
            </div>
            <div className="text-gray-400 mt-2">
              {currentMedia.metadata?.extra_info?.artist || 'Artista Desconhecido'}
            </div>
            <ReactPlayer
              ref={playerRef}
              url={streamUrl}
              playing={isPlaying}
              volume={volume}
              width="0"
              height="0"
              onProgress={handleProgress}
              onDuration={handleDuration}
              controls={false}
            />
          </div>
        )}
      </div>

      {/* Informações da mídia */}
      <div className="p-4 border-b border-gray-700">
        <h3 className="text-white font-semibold text-lg truncate">
          {currentMedia.filename}
        </h3>
        <div className="flex gap-4 mt-2 text-sm text-gray-400">
          <span>Format: {currentMedia.format?.toUpperCase()}</span>
          {currentMedia.metadata?.codec && (
            <span>Codec: {currentMedia.metadata.codec}</span>
          )}
          {currentMedia.metadata?.resolution && (
            <span>Resolução: {currentMedia.metadata.resolution}</span>
          )}
          {currentMedia.plugin_used && (
            <span className="text-green-400">Plugin: {currentMedia.plugin_used}</span>
          )}
        </div>
      </div>

      {/* Controles */}
      <Controls playerRef={playerRef} />
    </div>
  );
};

export default Player;
