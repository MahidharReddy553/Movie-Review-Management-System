from users import *

def dashboard(user):
    pass

while True:
    print('0. exit')
    print('1. Register')
    print('2. Login')
    c = input('Enter your choice (0/1/2): ')

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
            print("Login failed", output[0])