# 1. take two numbers from user.
# Show menu to user and ask for the choice, perform the operation as per choice.
# choice should also include Q. Quit
# choice = 'A'
# while True:
# use break when the choice entered is 'Q'

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

# 2. marks = [10, 45, 23, 10, 49, 10, 20, 10, 30, 40]
# print if the number 10 appears minimum 3 times in marks list
# marks = [10, 45, 23, 10, 49, 10, 20, 10, 30, 40]
# count = 0
# for mark in marks:
#     if mark == 10:
#         if count == 3:
#             break
#         count +=1
# if count ==3:
#     print(f"number 10 appears {count} times")
# else:
#     print(f"number 10 appears less than 3 times")



# 3. marks = [10, 45, 23, 10, 49, 10, 20, 10, 30, 40]
# print if the number 10 appears exactly 3 times in marks list

# marks = [10, 45, 23, 100, 49, 10, 20, 10, 30, 40]
# count = 0
# for mark in marks:
#     if mark == 10:
#         if count >= 3:
#             break
#         count +=1
# if count ==3:
#     print(f"number 10 appears {count} times")
# else:
#     print(f"number 10 appears less than 3 times")

           # OR

# marks = [10, 45, 23, 100, 49, 10, 20, 10, 30, 40]
# count = 0
# for mark in marks:
#     if mark == 10:
#           count +=1
# if count ==3:
#  print(f"number 10 appears {count} times")
# else:
#  print(f"number 10 appears less or greater than 3 times")

# 4. marks = [10, 45, 23, 10, 49, 10, 20, 10, 30, 40]
# print all the numbers from marks, other than 10
# Hint: use for loop and continue
# marks = [10, 45, 23, 10, 49, 10, 20, 10, 30, 40]
# for mark in marks:
#     if mark == 10:
#         continue
#     print(mark)


# 5. marks = [10, 45, 23, 10, 49, 10, 20, 10, 30, 40]
# count the marks which are less than 25
# Hint: continue

# marks = [10, 45, 23, 10, 49, 10, 20, 10, 30, 40]
# count = 0
# for mark in marks:
#     if mark > 25:
#         continue
#     count +=1
# print(count)


#
# 6. write a program to accept a number from user and print factorial of that number
# what is factorial:
# e.g. factorial of 3 is 1 * 2 * 3
# e.g. factorial of 4 is 1 * 2 * 3 * 4
# e.g. factorial of 5 is 1 * 2 * 3 * 4 * 5
# Hint: you can choose to use for loop or while loop.

num1 = int(input("Print the number"))
factorial = 1
for i in range(1,num1+1):
    factorial = factorial*i   # (n!=(n-1)! * n)
print(factorial)

