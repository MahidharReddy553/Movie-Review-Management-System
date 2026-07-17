from utils import *


movies_file = r'D:\MRS_Project\MRS_no_db\data\movies.csv'

def view_all_movies():
    movie_data = read_csv(movies_file)
    # Handling empty data
    if not movie_data:
        return "No movies found"

    print(f"{'Movie ID':<10} {'Movie Title':<50} {'Movie Genre':<20} {'Release Year':<15}")
    print("-" * 90)
    for m in movie_data:
        print(f"{m['id']:<10} {m['title']:<50} {m['genre']:<20} {m['release_year']:<15}")

def add_movie(movie_title, movie_genre, movie_release_year):
    movie_data = read_csv(movies_file)
    new_movie = {
        'id': generate_id(movies_file),
        'title': movie_title,
        'genre': movie_genre,
        'release_year': movie_release_year
    }
    write_row(movies_file, new_movie)

def get_movie_by_id(movies_file, movie_id):
    movie_data = read_csv(movies_file)
    for m in movie_data:
        if m['id'] == movie_id:
            return m
    return "Movie not found"
# print(get_movie_by_id(movies_file, '2'))

def get_movie_by_title(movies_file, movie_title):
    movie_data = read_csv(movies_file)
    for m in movie_data:
        if m['title'].lower().strip() == movie_title.lower().strip():
            return m 
    return "Movie not found"
# print(get_movie_by_title(movies_file, 'godavari'))