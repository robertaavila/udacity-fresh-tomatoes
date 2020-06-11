# coding: UTF-8
import webbrowser

#cria a classe Movie com as instancias titulo, titulo original, duracao, genero, sinopse, imagem do poster e trailer.  
class Movie():
    # This class provides a way to store movie related information
    def __init__(self, movie_title, movie_original_title, movie_duration, movie_type, movie_storyline, poster_image, trailer_youtube):
    # initialize instance of class Movie
        self.title = movie_title
        self.original_title = movie_original_title
        self.duration = movie_duration
        self.type = movie_type
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


