#WAP to print factorial

# def factorial():
#     num1 = int(input("Print the number"))
#     factorial = 1
#     for i in range(1,num1+1):
#         factorial = factorial*i   # (n!=(n-1)! * n)
# print(factorial)
#
# factorial()


# Reverse MADAM

# def rev():
#     n = "MADAM"
#     print(n[::-1])
# pal()

# def rev():
#     n =input("Please enter a number")
#     print(n[::-1])
# rev()


# Palindrom MADAM
def pal():
    n = input("Please enter the value")
    n1 = (n[::-1])
    if n==n1:
        print("number is pal")
    else:
        print("number is not pal")
pal()
