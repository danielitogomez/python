# functions
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def operations():
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid input")
    return


finish_calculate = False

while not finish_calculate:

    # take input from the user
    print("Select operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    choice = input("Enter choice(1 2 3 or 4):")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    operations()

    should_continue = input("Do you want to do more calculations? Type 'yes or 'no'.\n")
    if should_continue == "yes":
        operations()
    elif should_continue == "no":
        finish_calculate = True
        print("Bye!")
        exit()
