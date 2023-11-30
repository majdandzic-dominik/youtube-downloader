from pytube import YouTube
from youtube_search import YoutubeSearch
import os


def download_mp3_from_link(url, destination):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download(output_path=destination)

    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)


def download_mp3_from_search_term(search_term, destination):
    result = YoutubeSearch(search_terms=search_term, max_results=1).to_dict()
    url = "https://www.youtube.com" + result[0]["url_suffix"]

    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"

    if os.path.exists(new_file):
        os.remove(out_file)
    else:
        os.rename(out_file, new_file)


if __name__ == "__main__":
    destination = input("Enter save folder: ")
    search_term = input("Enter search term: ")

    download_mp3_from_search_term(search_term, destination)
