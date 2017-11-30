import webbrowser
class Movies():
    VALID_RATINGS=['G','PG','PG13','R','NC17']
    def __init__(self, movie_title, movie_storyline,movie_posterimage,movie_youtubetrailer):
        self.title = movie_title
        self.story = movie_storyline
        self.poster_image_url = movie_posterimage
        self.trailer_youtube_url = movie_youtubetrailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
