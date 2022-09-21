s = {100, 70, 40, 200, 10, 15, 80, 20, 30}

# del s
# print(s)  # not accessible any more
# NameError: name 's' is not defined

print(s)

s2 = {100, 200, 500, 300, 400}
print(s.union(s2))   # values from both sets, ignoring the duplicates

print(s.intersection(s2))  # common values

# set can contain multiple data types but only mutable
s3 = {100, 200, 500, 300, 400, "MS", "Rahul"}
print(s3)

s4 = {100, 200, 500, 300, 400, "MS", "Rahul", (10, 20, 30)}
print(s4)

# TypeError: unhashable type: 'list'
# s5 = {100, 200, 500, 300, 400, "MS", "Rahul", [10, 20, 30]}
# print(s5)



