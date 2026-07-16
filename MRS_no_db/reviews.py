from utils import *

path = r'D:\MRS_Project\MRS_no_db\data\reviews.csv'

def get_user_reviews(user_id):
    data = read_csv(path)
    reviews = [r for r in data if r.get('user_id') == user_id]
    return reviews

# get_user_reviews('1')