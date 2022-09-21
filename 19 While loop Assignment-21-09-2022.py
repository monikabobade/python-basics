# 1. take two numbers from user.
# Show menu to user and ask for the choice, perform the operation as per choice.
# choice should also include Q. Quit
# choice = 'A'
# while True:
# use break when the choice entered is 'Q'

while True:

    num1 = int(input("Please enter first number"))
    num2 = int(input("Please enter second number"))
    print("a. Addition")
    print("s. Subtraction")
    print("m. Multiplication")
    print("d. Division")
    print("q. Quit")
    Choice = input("Please enter the menu: ")
    if Choice == "a":
        Addition = num1 + num2
        print(Addition)
    elif Choice == "s":
        Subtraction = num1 - num2
        print(Subtraction)
    elif Choice == "m":
        Multiplication = num1 * num2
        print(Multiplication)
    elif Choice == "d":
        Division = num1 / num2
        print(Division)
    elif Choice == "q":
         print("Quit")
         break
    else:
         print("Wrong choice enter")

marks = [10, 45, 23, 10, 49, 10, 20, 10, 30, 40]
print if the
number
10
appears
minimum
3
times in marks
list
