from db import Popcorn
class Credentials:
    def __init__(self):
        self.entry_ticket()
        self.welcome_ticket()
        self.data = Popcorn()
        self.home()
        
        
    def sign_up(self):
        print("Fasten your seat belts.. Signing in.. 3..2..1..")
        print("--------------------------------------------------")
        print("Welcome to the Movie Review System! Please sign up to continue.")
        print()

        username = input("🧑‍💻 Username : ")
        password = input("🔒 Password : ")
        email = input("📧 Email Address : ")

        self.data.upload(username,password,email)
        print()
        print("...Enter your credentials to login...")
        input("Press Enter to continue...")
        print()
        print("✅Sign up is completed.. What do you want to do now?")
        print("1. Log in\n2. Exit")
        inp = int(input("Choose an option: "))
        if inp == 1:
            self.login()
        elif inp == 2:
            print("Exiting the system...")
            print("-------------------------------------------")
            print("Thank you for signing up...")
            print("-------------------------------------------")
            exit()
        else:
            print("Please enter a valid choice...")
        

    def login(self):
        print("Enter the DRAGON 🐉 ...")
        username = input("🧑‍💻 Username : ")
        password = input("🔒 Password : ")
        self.data.logins(username,password)
    

    def entry_ticket(self):
        print("                                     ~ ~ ~ ~ ~ ~ ~ ~  WELCOME CINEPHILE ~ ~ ~ ~ ~ ~ ~ ~          ")
        print("------------------------------------------------------------------------------------------------------------------------------------")

    def welcome_ticket(self):
        input("Press Enter to continue...")
        print(" 🍿🎬  Step onto the silver screen—your perfect movie awaits!  🎬🍿 ")
        input("Press Enter to continue...")

    def home(self):
        print("                          📽️   📽️   📽️   📽️   📽️   WELCOME TO CINEMA BAZAAR  📽️   📽️   📽️   📽️   📽️")
        print("------------------------------------------------------------------------------------------------------------------------------------")
        print()
        print("1. SIGN UP (if you are a new CINEPHILE 🤓..)\n2. LOGIN (if you are already a CINEPHILE 😎..)")
        print("------------------------------------------------------------------------------------------------------------------------------------")
        n = int(input("Enter your option: "))
        if n == 1:
            self.sign_up()
            
        elif n == 2:
            self.login()

        else:
            print("🔑Please select a valid option....")

    def add(self):
        self.data.add_a_movie(title = input("🎬 Enter title: "),
                              genre = input("🎭 Enter the genre of the film: "),
                              release_year = int(input("📅 Enter the movie's year of release:")))        

    def write(self):
        movie_id = int(input("🎞️ Enter the movie ID you want to review: "))
        movie_name = self.data.get_movie_name(movie_id)
        if movie_name:
            print(f"📽️ You are reviewing the movie: {movie_name}")
            rating = int(input("⭐ Enter your rating (1-5): "))
            comments = input("💬 Enter your comments: ")
            self.data.write_review(movie_id,rating,comments)
        else:
            print("❌Movie Id is not found in the database.. Please verify your input...")

    def view(self):
        self.data.view_all()

    def update(self):
        self.data.update_review()

    def delete(self):
        movie_id = int(input("🎞️ Enter the movie ID you want to delete your review: "))
        self.data.delete_review(movie_id)


clap = Credentials()
print("-----------------------------------------------------------------")
print("- - - - - - - - WELCOME TO MOVIE REVIEW SYSTEM- - - - - - - - - -")
print("-----------------------------------------------------------------")

def main():
    while True:
        print('''
              1. 🎬 Add a Movie
              2. 🔍 Search for movies
              3. 📝 Write a review
              4. 📖 View all reviews
              5. 🌟 Top Rated Movies
              6. ✏️ Update my review
              7. 🗑️ Delete my review
              8. 🚪 Exit
              ''')
        print("-----------------------------------------------------------------")
        op = int(input("🔘 Enter your option: "))
        if op == 1:
            clap.add()
        elif op == 2:
            clap.data.search_a_movie()
        elif op == 3:
            clap.write()
        elif op == 4:
            clap.view()
        elif op == 5:
            clap.data.top_movies()
        elif op == 6:
            clap.update()
        elif op == 7:
            clap.delete()
        elif op == 8:
            print()
            print("-----------------------------------------------------------------------------")
            print("Thank you for visiting our page!! 😊 \nPlease visit again")
            break
        else:
            print("🧿 Please select a valid option....")
        print("-----------------------------------------------------------------")
        print()
if __name__=='__main__':
    main()