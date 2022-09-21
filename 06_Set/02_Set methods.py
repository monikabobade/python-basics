# sets

s = {15, 10, 20, 30}
print(s)

s.add(40)  # new element would be added: unordered
print(s)

s.update([70, 80])  # adding multiple elements
print(s)

s.update((100, 200))
print(s)


print(len(s))

s.remove(15)    # 15 will be removed
print(s)

# s.remove(50)    # key error if the element is not available
# print(s)

s.discard(20)     # will remove element if available, else ignore. NO error
print(s)

s.discard(50)     # will remove element if available, else ignore. NO error
print(s)

print(s.pop())     #   an arbitrary element would be removed and returned
                    # key error, if the set is empty
print(s)

s.clear()       # it will remove all elements from set
print(s)