import mp3_downloader

if __name__ == "__main__":
    destination = input("Enter save folder: ")
    url = input("Enter YouTube video URL: ")
    print("Downloading...")
    mp3_downloader.download_mp3_from_link(url, destination)
    print("Finished")
