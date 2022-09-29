def add_number(n1, n2, n3=5, *n):
    sum1 = n1 + n2 + n3 + sum(n)
    print(sum1)
    print(type(n))


add_number(2, 3, 10, 15, 20, 2)
