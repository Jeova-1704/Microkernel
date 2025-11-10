/**
 * Context API para gerenciar estado global do player
 */
import { createContext, useContext, useState } from 'react';

const PlayerContext = createContext();

export const usePlayer = () => {
  const context = useContext(PlayerContext);
  if (!context) {
    throw new Error('usePlayer deve ser usado dentro de PlayerProvider');
  }
  return context;
};

export const PlayerProvider = ({ children }) => {
  const [currentMedia, setCurrentMedia] = useState(null);
  const [playlist, setPlaylist] = useState([]);
  const [isPlaying, setIsPlaying] = useState(false);
  const [volume, setVolume] = useState(0.5);
  const [currentTime, setCurrentTime] = useState(0);
  const [duration, setDuration] = useState(0);

  const playMedia = (media) => {
    setCurrentMedia(media);
    setIsPlaying(true);
  };

  const pauseMedia = () => {
    setIsPlaying(false);
  };

  const stopMedia = () => {
    setCurrentMedia(null);
    setIsPlaying(false);
    setCurrentTime(0);
  };

  const addToPlaylist = (media) => {
    setPlaylist((prev) => [...prev, media]);
  };

  const removeFromPlaylist = (filename) => {
    setPlaylist((prev) => prev.filter((m) => m.filename !== filename));
    if (currentMedia?.filename === filename) {
      stopMedia();
    }
  };

  const clearPlaylist = () => {
    setPlaylist([]);
    stopMedia();
  };

  const value = {
    currentMedia,
    playlist,
    isPlaying,
    volume,
    currentTime,
    duration,
    playMedia,
    pauseMedia,
    stopMedia,
    addToPlaylist,
    removeFromPlaylist,
    clearPlaylist,
    setVolume,
    setCurrentTime,
    setDuration,
  };

  return (
    <PlayerContext.Provider value={value}>
      {children}
    </PlayerContext.Provider>
  );
};
