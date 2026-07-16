from utils import *

path = r'D:\MRS_Project\MRS_no_db\data\reviews.csv'

def get_user_reviews(user_id):
    data = read_csv(path)
    reviews = [r for r in data if r.get('user_id') == user_id]
    return reviews


def add_review(u_id, m_id, m_rating, m_comment):
    reviews = read_csv(path)

    new_review = {
        'id': generate_id(path),
        'user_id': u_id,
        'movie_id': m_id,
        'rating': m_rating,
        'comment': m_comment
    }

    write_row(path, new_review)
# get_user_reviews('1')