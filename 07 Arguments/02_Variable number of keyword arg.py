#  variable Number of arg + variable number of keyword arg
def add_number(n1, n2, n3=5, *n, **num):
    sum1 = n1 + n2 + n3 + sum(n) + sum(num.values())
    print(sum1)
    print(type(n))
    print(type(num))


add_number(2, 3, 1, 1, 20, 2, a=2, b=3)
