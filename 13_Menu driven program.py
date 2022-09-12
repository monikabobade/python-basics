
num1 = int(input("Please enter first number"))
num2 = int(input("Please enter second number"))
print("a. Addition")
print("s. Subtraction")
print("m. Multiplication")
print("d. Division")
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
else:
     print("Wrong choice enter")





