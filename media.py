class Movie():
    # Create a movie object that saves titles, poster images, and movie trailer URLs
    def __init__(self, title, poster_img, trailer_url):
        self.title = title
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_url
