import mp3_downloader

if __name__ == "__main__":
    destination = input("Enter save folder: ")
    search_term = input("Enter search term: ")
    print("Downloading...")
    mp3_downloader.download_mp3_from_search_term(search_term, destination)
    print("Finished")
