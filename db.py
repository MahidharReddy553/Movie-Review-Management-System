import mysql.connector
class Popcorn:
    def __init__(self):
        self.connect()
    def connect(self):
        self.con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "Cinebase"
            )
        self.cur = self.con.cursor()


    def upload(self,username,password,email):
        self.connect() #Connect to the database
        print("🚀 Uploading user details... Please wait! 📂")

        self.cur.execute("insert into users(username,password,email) values (%s,%s,%s)",(username,password,email)) #Insert user details into the users table
        self.con.commit() #Commit the changes to the database

        print("\n✅ Details uploaded successfully!!! ")
        print("🔓 You are now **FREE** to LOGIN and explore! ")
        self.cur.close() #Close the cursor
        self.con.close() #Close the connection
        

    def logins(self,username,password):
        self.connect()
        self.cur.execute("select username from users where username = %s and password = %s",(username,password)) #Login as existing user
        result = self.cur.fetchone() #Fetch that user details from the database
        if result:
            self.logged_in_user = username  # Store the logged-in username for later use
            print(f"✅ Login successful!! Welcome {username}!!")
        else:
            print("❌ Invalid username or password.. Please Try again!!")
          
        self.cur.close()
        self.con.close()

    def fetch_user_id(self,username): #Fetch user id from the database
        self.connect()
        self.cur.execute("select user_id from users where username = %s",(username,))
        data = self.cur.fetchone()
        print(data, type(data[0]))
        


    def add_a_movie(self,title,genre,release_year): #Add a movie to the database
        if not title or not genre or not release_year:
            print("❌ Please provide all movie details.")
            return
        self.connect()
        self.cur.execute("insert into movies(title,genre,release_year) values (%s,%s,%s)",(title,genre,release_year))
        self.con.commit()
        print(f"Your movie details 🎬 🍿\n title : {title} \n genre : {genre} \n year_of_release = {release_year} \n have been successfully stored! 🎬 🍿")
        self.cur.close()
        self.con.close()

    def search_a_movie(self): #Search a movie in the database
        self.connect()
        while True:
                print("\n🎬 Movie Search Options 🎬")
                print('''
                      1. Search by year
                      2. Search by Movie name
                      3. Search by Genre
                      4. Quit Search
                      ''')

                opt = int(input("Select your choice: "))
                if opt == 1:
                    year = int(input("Enter year of release:  "))
                    self.cur.execute("select * from movies where release_year = %s",(year,))
                    data = self.cur.fetchall()
                    print("----------------------------------------------------------------------")
                    print("ID\tTitle\t\t\tGenre\t\tYear of Release")
                    print("----------------------------------------------------------------------")
                    for row in data:
                        print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}")
                elif opt == 2:
                    name = input("🎬 Enter title of the film:  ")
                    self.cur.execute("select * from movies where title = %s",(name,))
                    data = self.cur.fetchall()
                    print(data)
                elif opt == 3:
                    movie_genre = input("🎭 Enter the genre of the film:  ")
                    self.cur.execute("select * from movies where genre = %s",(movie_genre,))
                    data = self.cur.fetchall()
                    print(data)
                elif opt == 4:
                    break
                else:
                    print("❌ Please select valid choice...")
    

    def view_all(self): #View all movies and reviews in the database
        self.connect()
        
        self.cur.execute("SELECT * FROM movies")
        d = self.cur.fetchall()
        print("------------------------------------------------------------------")
        print("ID\tTitle\t\t\t\tGenre\t\tYear of Release")
        print("------------------------------------------------------------------")
        for row in d:
            print(f"{row[0]}\t{row[1]}\t\t\t\t\t{row[2]}\t{row[3]}")
        print("------------------------------------------------------------------")
       
        self.cur.execute("SELECT rating,comments from reviews join movies on reviews.movie_id = movies.movie_id")
        data = self.cur.fetchall()
        if not data:
            print("🚫 No reviews found.")
            return 
        else:
            print("----------------------------------------------------")
            print("Rating\t\t\t\t\tComments")
            print("----------------------------------------------------")
            for mov in data:
                print(f"{mov[0]}\t\t\t{mov[1]}")
                print("------------------------------------------------------")
        
    def top_movies(self): #View top rated movies in the database
        self.connect()
        self.cur.execute('''
                        SELECT 
                            movies.title, 
                            movies.genre,
                            reviews.rating,
                            movies.release_year 
                        FROM 
                            reviews 
                        INNER JOIN 
                            movies 
                        ON 
                            reviews.movie_id = movies.movie_id 
                        ORDER BY 
                            reviews.rating DESC''')
        data = self.cur.fetchall()
        print('--------------------------------------------------')
        print("----------------TOP RATED MOVIES------------------")
        print('--------------------------------------------------')
        print("--------------------------------------------------")
        print("Title\t\t\tGenre\t\tYear of Release")
        print("--------------------------------------------------")
        for row in data:
            print(f"{row[0]}\t{row[1]}\t{row[2]}")


    def write_review(self, movie_id, rating, comments): #Write a review for a movie in the database
        self.connect()

        # Check if user is logged in
        if self.logged_in_user == "":
            print("You must be logged in to write a review.")
            return

        # Show available movies
        self.cur.execute("SELECT movie_id, title, genre FROM movies")
        movies = self.cur.fetchall()
        print("------------------------------------------------------------------")
        print("ID\tTitle\t\t\t\tGenre")
        print("------------------------------------------------------------------")
        for row in movies:
            print(f"{row[0]}\t{row[1]}\t\t\t\t{row[2]}")
        print("--------------------------------------------------")

        # Get user_id from username
        self.cur.execute("SELECT user_id FROM users WHERE username = %s", (self.logged_in_user,))
        user_data = self.cur.fetchone()
        if user_data is None:
            print("User not found in the database.")
            return

        user_id = user_data[0]   # Insert review with user_id
        self.cur.execute(
            "INSERT INTO reviews (movie_id, rating, comments, user_id) VALUES (%s, %s, %s, %s)",
            (movie_id, rating, comments, user_id)
        )
        self.con.commit()

        print("Your review is added successfully!")
        self.cur.close()
        self.con.close()

    
    def get_movie_name(self, movie_id): #Get movie name by movie id
        self.connect()
        self.cur.execute("select title from movies where movie_id = %s",(movie_id,))
        moviename = self.cur.fetchone()
        if not moviename:
            print("Movie not found..")
            return None
        return moviename[0]
    
    
    
    def update_review(self): #Update a review in the database
        self.connect()  
        # Check if a user is logged in
        if not self.logged_in_user:
            print("Access denied: No user is logged in.")
            return
        # Fetch reviews only for the logged-in user
        self.cur.execute("""
            SELECT reviews.review_id, reviews.movie_id, movies.title, reviews.rating, reviews.comments 
            FROM reviews
            JOIN movies ON reviews.movie_id = movies.movie_id
            WHERE reviews.user_id = (SELECT user_id FROM users WHERE username = %s);
        """, (self.logged_in_user,))

        reviews = self.cur.fetchall()

        if not reviews:
            print()
            print("🔎 You haven't submitted any reviews yet.")
            return

        # Displaying the previous reviews given by the user(if there are any)
        print("\n-------------------Your Reviews:--------------------")
        for review in reviews:
            print(f" 🆔 Review ID: {review[0]}, 🎬 Movie: {review[2]},  ⭐ Rating: {review[3]}, 💬 Comments: {review[4]}")

        # which review to update
        review_id = int(input("🆔 Enter the Review ID of the review you want to update: "))

        # Make sure the selected Review ID belongs to the logged-in user
        review_exists = any(review[0] == review_id for review in reviews)
        if not review_exists:
            print()
            print("🚫 Access restricted: You can only update your own reviews.")
            return

        # Get new rating and comments
        print()
        print("🔄 Updating your review...")
        new_rating = float(input("⭐ Enter new rating: "))
        new_comments = input("💬 Enter new comments: ")

        # Update review only for the logged-in user
        self.cur.execute("""
            UPDATE reviews 
            SET rating = %s, comments = %s 
            WHERE review_id = %s;
        """, (new_rating, new_comments, review_id))

        self.con.commit()
        print("✔ Your review has been updated successfully!")
        self.cur.close()
        self.con.close()


    def delete_review(self,movie_id): #Delete a review in the database
        self.connect()  
        # Check if a user is logged in
        if not self.logged_in_user:
            print("🚫 Access denied: No user is logged in.")
            return

        # Fetch reviews only for the logged-in user
        self.cur.execute("""
            SELECT reviews.review_id, reviews.movie_id, movies.title, reviews.rating, reviews.comments 
            FROM reviews
            JOIN movies ON reviews.movie_id = movies.movie_id
            WHERE reviews.user_id = (SELECT user_id FROM users WHERE username = %s);
        """, (self.logged_in_user,))

        reviews = self.cur.fetchall()

        if not reviews:
            print()
            print("📭 You haven't submitted any reviews yet.")
            return

        # Displaying the previous reviews given by the user(if there are any)
        print("\n-------------------Your Reviews:--------------------")
        for review in reviews:
            print(f"Review ID: {review[0]}, Movie: {review[2]}, Rating: {review[3]}, Comments: {review[4]}")

        # which review to delete
        review_id = int(input("🆔 Enter the Review ID of the review you want to delete: "))

        # Make sure the selected Review ID belongs to the logged-in user
        review_exists = any(review[0] == review_id for review in reviews)
        if not review_exists:
            print("🚫 Access restricted: You can only delete your own reviews.")
            return

        # Delete review only for the logged-in user
        self.cur.execute("""
            DELETE FROM reviews 
            WHERE review_id = %s;
        """, (review_id,))  #Main query to delete the review

        self.con.commit()
        print("🗑️ Your review has been deleted successfully!")
        self.cur.close()
        self.con.close()