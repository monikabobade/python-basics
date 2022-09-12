# marks = 45, 48, 44, 46   # another way to define a tuple
# Recommended way of defining a tuple is using ()

# marks = 45, 48, 44, 46   # packing
#
# print(marks)
# print(type(marks))

# t1 = (30, 40, 20, 50)
# m1, m2, m3, m4 = t1    # unpacking
# # m1, m2, m3 = t1           # ValueError: too many values to unpack (expected 3)
# # m1, m2, m3, m4, m5 = t1   # ValueError: not enough values to unpack (expected 5, got 4)
# print(m1)
# print(m2)
# print(m3)
# print(m4)

# a = 5
# b = 10
# c = 20
# t = 5, 10, 15  # packing > tuple
# a, b, c = t   # tuple > unpacking
a, b, c = 5, 10, 15    # packing > tuple > unpacking
# a, b, c = (5, 10, 15)
print(a, type(a))
print(b, type(b))
print(c, type(c))

