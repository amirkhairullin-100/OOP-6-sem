from abc import ABC, abstractmethod

class AudioPlayable(ABC):
    @abstractmethod
    def play_audio(self, file: str):
        pass

class VideoPlayable(ABC):
    @abstractmethod
    def play_video(self, file: str):
        pass

class SubtitlesSupport(ABC):
    @abstractmethod
    def show_subtitles(self, file: str):
        pass

class VideoPlayer(AudioPlayable, VideoPlayable, SubtitlesSupport):
    def play_audio(self, file: str):
        print(f"Воспроизведение аудио: {file}")

    def play_video(self, file: str):
        print(f"Воспроизведение видео: {file}")

    def show_subtitles(self, file: str):
        print(f"Показ субтитров: {file}")

class AudioPlayer(AudioPlayable):
    def play_audio(self, file: str):
        print(f"Воспроизведение аудио: {file}")

player_audio = AudioPlayer()
player_audio.play_audio("song.mp3")

video_player = VideoPlayer()
video_player.play_audio("music.mp3")
video_player.play_video("movie.mp4")
video_player.show_subtitles("subtitles.srt")