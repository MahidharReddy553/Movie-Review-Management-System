from utils import *
from users import *
from movies import *
from reviews import *

# User Dashboard
def dashboard(user):
    while True:
        print("Select a choice(0-5):")
        print("0. Logout\n1. Add a movie\n2. List all movies\n3. Add a review\n4. View all reviews by a user\n5. Edit a review\n6. Delete a review")

        c = input("Enter the choice: ")
        
        if c == '0':
            print("You have logged out successfully...")
            exit()

        elif c == '1':
            movie_title = input("Enter the movie title: ")
            movie_genre = input("Enter the movie genre: ")
            movie_release_year = input("Enter the movie's release year: ")

            add_movie(movie_title, movie_genre, movie_release_year)
            print('Movie has been added successfully..')

        elif c == '2':
            print("--------------- LIST OF MOVIES ---------------")
            view_all_movies()

        elif c == '3':
            u_id = input("Enter the user ID: ")
            m_id = input("Enter the movie ID: ")
            m_rating = input("Enter the rating of the movie: ")
            m_comment = input("Enter your comment on the movie: ")

            add_review(u_id, m_id, m_rating, m_comment)
            print("Your review has been added successfully..")

        elif c == '4':
            u_id = input("Enter the user ID: ")
            print(f"Reviews by the user with User ID: {u_id}")
            view_user_review(u_id)

        elif c == '5':
            review_id = input("Enter the review id you want to edit: ")
            new_rating = input("Enter the edited rating: ")
            new_comment = input("Enter the new comment: ")

            print(f"Review ID entered by the user: {review_id}")
            edit_review(review_id, new_rating, new_comment)

        elif c == '6':
            pass

        else:
            print("Invalid Choice. Please enter your choice between 0-5")


while True:
    print("----------- WELCOME TO MOVIE REVIEW SYSTEM -----------")
    print("0. Exit\n1. Register\n2. Login")

    ch = input("Please enter a choice (0/1/2): ")

    if ch == '0':
        break

    elif ch == '1':
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        email = input("Enter the email: ")

        register_user = register(username, password, email)
        print("User has been registered successfully..")

    elif ch == '2':
        print("Enter your details to login")
        credential = input("Enter your credential(username or email): ")
        log_password = input("Enter your password: ")

        output = login(credential, log_password)
        if output[0] == 'Login successful.':
            user = output[1]
            dashboard(user)
        else:
            print("Login failed..", output[0])
        
    else:
        print("Wrong Choice...")