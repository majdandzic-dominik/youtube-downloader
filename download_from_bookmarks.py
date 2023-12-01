import mp3_downloader
from bs4 import BeautifulSoup
import requests
import pandas as pd

if __name__ == "__main__":
    destination = input("Enter save folder: ")
    # file_path = input("Enter bookmark file path: ")
    file_path = "D:\\PRACTICE\\Python\\GIT\\bookmarks.html"
    with open(file_path, encoding="utf-8") as f:
        content = f.read()
        soup = BeautifulSoup(content, features="html.parser")
        links = soup.find_all("a")

        songs_arr = [
            link["href"]
            for link in links
            if link["href"].startswith("https://www.youtube.com/watch?v")
        ]

        print("Downloading...")
        for song in songs_arr:
            mp3_downloader.download_mp3_from_link(song, destination)
        print("Finished")
