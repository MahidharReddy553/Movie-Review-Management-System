from users import *

def dashboard(user):
    while True:
        print('Select a choice')
        print('0. Logout')
        print('1. Add a movie')
        print('2. List all movies')
        print('3. Add a review')
        print('4. Edit a review')
        print('5. Delete a review')

        ch = input('Enter your choice (0 - 5) : ').strip()
        if ch == '0':
            print('You have logged out successfully...')
            exit()

        if ch == '1':
            pass

        elif ch == '2':
            pass

        elif ch == '3':
            pass

        elif ch == '4':
            pass

        elif ch == '5':
            pass

        else:
            print('Invalid Choice. Please enter between (0 - 5)')
        pass


while True:
    print('0. exit')
    print('1. Register')
    print('2. Login')
    c = input('Enter your choice (0/1/2): ').strip()

    if c == '0':
        print("Thanks for your interest in movies. Byee!!")
        break

    elif c == '1':
        username = input("Enter the uesrname : ")
        password = input("Enter your password : ")
        email = input("Enter your email : ")
        print(register(username, password, email))

    elif c == '2':
        credential = input("Enter your username or email : ")
        l_password = input("Enter your password : ")
        output = login(credential, l_password)
        if output[0] == 'Login successful.':
            user = output[1]
            print(user)
            dashboard(user)
        else:
            print("Login failed!!", output)