import mp3_downloader

if __name__ == "__main__":
    destination = input("Enter save folder: ")
    file_path = input("Enter text file path: ")
    songs_arr = []
    with open(file_path) as f:
        for line in f:
            if line.strip() != "":
                songs_arr.append(line.strip())
    print("Downloading...")
    for song in songs_arr:
        mp3_downloader.download_mp3_from_search_term(song, destination)

    print("Finished")
