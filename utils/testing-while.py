not_finish = False


while not not_finish:

    username = input("Enter username: ")

    def names():
        if username == 'daniel':
            print(f"So, your username is {username}")

        elif username == 'dani':
            print(f"So, your username is {username}")
        else:
            print("Incorrect input")
            exit()
        return
    names()

    should_continue = input("Do you want to continue with the questions? Type 'yes or 'no'.\n")
    if should_continue == "yes":
        names()
    elif should_continue == "no":
        not_finish = True
        print("Bye!")
        exit()
