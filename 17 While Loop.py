# WAP to print marks
# marks = [23, 45, 67, 5]
# i = 0
# while i< len(marks):
#    print(marks)
#    i += 1


# WAP to search if number 5 is available in the marks

marks = [2, 4, 5, 7]
i=0
found = False
while i < len(marks):
    if marks[i] == 5:
        found = True
        break
    i+=1

if found == True:
           print("number is found")
else:
          print("number not found")








