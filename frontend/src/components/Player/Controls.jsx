/**
 * Controles do player (play, pause, volume, timeline)
 */
import { Play, Pause, SkipBack, SkipForward, Volume2, VolumeX } from 'lucide-react';
import { usePlayer } from '../../context/PlayerContext';
import { useState } from 'react';

const Controls = ({ playerRef }) => {
  const {
    isPlaying,
    volume,
    currentTime,
    duration,
    playMedia,
    pauseMedia,
    setVolume,
    currentMedia,
  } = usePlayer();

  const [isMuted, setIsMuted] = useState(false);

  const formatTime = (seconds) => {
    if (!seconds) return '0:00';
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  };

  const handleSeek = (e) => {
    const newTime = parseFloat(e.target.value);
    if (playerRef.current) {
      playerRef.current.seekTo(newTime, 'seconds');
    }
  };

  const handleVolumeChange = (e) => {
    const newVolume = parseFloat(e.target.value);
    setVolume(newVolume);
    setIsMuted(newVolume === 0);
  };

  const toggleMute = () => {
    if (isMuted) {
      setVolume(0.5);
      setIsMuted(false);
    } else {
      setVolume(0);
      setIsMuted(true);
    }
  };

  const handlePlayPause = () => {
    if (isPlaying) {
      pauseMedia();
    } else {
      if (currentMedia) {
        playMedia(currentMedia);
      }
    }
  };

  return (
    <div className="p-4 bg-gray-900">
      {/* Timeline */}
      <div className="mb-4">
        <input
          type="range"
          min="0"
          max={duration || 0}
          value={currentTime || 0}
          onChange={handleSeek}
          className="w-full h-2 bg-gray-700 rounded-lg appearance-none cursor-pointer slider"
        />
        <div className="flex justify-between text-xs text-gray-400 mt-1">
          <span>{formatTime(currentTime)}</span>
          <span>{formatTime(duration)}</span>
        </div>
      </div>

      {/* Botões de controle */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <button
            className="p-2 rounded-full hover:bg-gray-800 text-gray-400 hover:text-white transition"
            disabled
          >
            <SkipBack size={20} />
          </button>

          <button
            onClick={handlePlayPause}
            className="p-3 rounded-full bg-blue-600 hover:bg-blue-700 text-white transition"
            disabled={!currentMedia}
          >
            {isPlaying ? <Pause size={24} /> : <Play size={24} />}
          </button>

          <button
            className="p-2 rounded-full hover:bg-gray-800 text-gray-400 hover:text-white transition"
            disabled
          >
            <SkipForward size={20} />
          </button>
        </div>

        {/* Controle de volume */}
        <div className="flex items-center gap-2">
          <button
            onClick={toggleMute}
            className="p-2 rounded-full hover:bg-gray-800 text-gray-400 hover:text-white transition"
          >
            {isMuted ? <VolumeX size={20} /> : <Volume2 size={20} />}
          </button>
          <input
            type="range"
            min="0"
            max="1"
            step="0.01"
            value={volume}
            onChange={handleVolumeChange}
            className="w-24 h-2 bg-gray-700 rounded-lg appearance-none cursor-pointer slider"
          />
        </div>
      </div>
    </div>
  );
};

export default Controls;
