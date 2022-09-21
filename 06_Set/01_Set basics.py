# sets
# 1. {}
# 2. unordered
# 3. duplicates are ignored
# 4. no indexing, no slicing
# 5. membership can be checked
# 6. mutable
# 7. mathematical operations: union, intersection, etc.

s = {15, 10, 20, 30}
print(s)

print(15 in s)   # membership supported

s.add(40)  # new element would be added: unordered
print(s)

s.add(20)  # duplicate ignored
print(s)

print(type(s))
# -----------------------------------
# Empty set
s2 = {}  # it's dict
print(s2)
print(type(s2))  # dict

# s2.add(40)  # not allowed

s3 = set()  # empty set
print(s3)
print(type(s3))
