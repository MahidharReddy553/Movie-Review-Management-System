from movies import *
from reviews import *

class MovieReviewSystem:
    def __init__(self, user):
        self.user = user
    
    def add_a_movie(self, movie_title, movie_genre, movie_release_year):
        add_movie(movie_title, movie_genre, movie_release_year)
    
    def view_my_reviews(self):
        get_user_reviews(self.user.get('id'))


