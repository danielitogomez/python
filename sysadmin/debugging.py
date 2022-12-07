username = input("Enter username: ")
password = input("Enter your password: ")


def login_info():
    if username == 'lala' and password == '1234':
        print(f"Your username is {username} and you are logged now!!!")
    else:
        print("Incorrect username or password")
        exit()


login_info()
