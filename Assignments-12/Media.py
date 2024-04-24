import pytube

class Media:
    def __init__(self, name, director, imdb_score, url, duration, casts):
        self.name = name
        self.director = director
        self.imdb_score = imdb_score
        self.url = url
        self.duration = duration
        self.casts = casts

    def show_info(self):
        print("Name:", self.name)
        print("Director", self.director)
        print("IMDB Score", self.imdb_score)
        print("Duration", self.duration, "minutes")
        print("Casts: ", ', '.join([cast.name for cast in self.casts]))

    def download(self):
        try:
            yt = pytube.YouTube(self.url)
            stream = yt.streams.first()
            stream.download(output_path='F:/Python/Exercises/12', filename='test.mp4')
            print("Download completed successfully.")
        except Exception as e:
            print("An error occurred during the download:", str(e))
