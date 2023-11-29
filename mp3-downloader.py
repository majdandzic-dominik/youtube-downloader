from pytube import YouTube
import os


def download_mp3_from_link(url, destination):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download(output_path=destination)

    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)


if __name__ == "__main__":
    destination = input("Enter save folder: ")
    url = input("Enter YouTube video URL: ")

    download_mp3_from_link(url, destination)
