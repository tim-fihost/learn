from pytube import YouTube
from pytube.exceptions import AgeRestrictedError
from pytube.exceptions import VideoUnavailable, RegexMatchError
import os
#MODEL IS READY TO GO!
class Downloader(YouTube):
    """
    A class for downloading YouTube videos and converting them to audio.
    Attributes:
    """
    #========================================================
    def convert(self,old_name):
        os.rename(f'audio/{old_name}', f'audio/{old_name.replace("mp4", "mp3")}')
        print(f"Renamed {old_name} to {old_name.replace('mp4', 'mp3')}")
    #========================================================
    def download_audio(self):
        download_path_audio = 'audio/'
        try:
            audio_streams = self.streams.filter(only_audio=True)
            audio_stream = audio_streams.first()
            saved_file_path = audio_stream.download(output_path=download_path_audio)
            saved_file_name = saved_file_path.split('/')[-1]
            print("Name of the saved file:", saved_file_name)
            return saved_file_name
        except AgeRestrictedError as e:
             return f"{e}"
    #=========================================================
    def download_mp4(self):
        self.streams.filter(adaptive=True)
        stream = self.streams.get_by_itag(22)
        stream.download(output_path='videos/')
    

def main():
    "TEST CASE"
    what = input("What do you want to donwlaod: ")
    yt = Downloader(what)
    yt.check_youtube_video()
    path = yt.download_audio()
    if path in os.listdir('audio/'):
        yt.convert(path)
        yt.download_mp4()
    else:
         print(path)
if __name__ == '__main__':
        main()

#TODO just use what u ve got!