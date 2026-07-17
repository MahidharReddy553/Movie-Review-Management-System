from utils import *
from movies import *

reviews_file = r'D:\MRS_Project\MRS_no_db\data\reviews.csv'
movies_file = r'D:\MRS_Project\MRS_no_db\data\movies.csv'

def add_review(u_id, m_id, m_rating, m_comment):
    reviews = read_csv(reviews_file)
    movie = get_movie_by_id(movies_file, m_id)
    if movie == "Movie not found":
        return "Movie is not found. So, unable to write a review"

    new_review = {
        'id': generate_id(reviews_file),
        'user_id': u_id,
        'movie_id': m_id,
        'rating': m_rating,
        'comment': m_comment
    }
    write_row(reviews_file, new_review)

def view_user_review(u_id):
    reviews = read_csv(reviews_file)
    found = False
    for r in reviews:
        if r['user_id'] == u_id:
            print("User ID:", r['user_id'], "||", "Movie ID:", r['movie_id'], "||", "Movie Rating:", r['rating'], "||", "Movie Comment: ", r['comment'])
            found = True

    if not found:
        print(f"No reviews found with user ID {u_id}")

# view_user_review('3')

def edit_review(review_id, new_rating, new_comment):
    reviews = read_csv(reviews_file)
    for r in reviews:
        if r['id'] == review_id:
            r['rating'] = new_rating
            r['comment'] = new_comment
            break
    write_rows(reviews_file, reviews)

# edit_review('2', '4', 'Excellent experience')