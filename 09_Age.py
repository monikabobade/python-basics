

# if Age < 18:
#     status = "Kid"
# else:
#     status = "Adult"
#     print("you are a", status)



# age = int(input("Please enter your age: "))         # hello     21hello     21hi: error
# print("Your age is ", age)   # int  str
#
# print(type(age))

# # if condition:
# if age < 18:            # syntax of if condition
#     status = "Kid"
# else:
#     status = "Adult"



# if else ladder:
# if age < 18:
#     status = "Kid"
# elif age < 60:
#     status = "Adult"
# else:
#     status = "Sr Citizen"
# age = int(input("please enter ur age'"))
# print("age:", age)
# print(type(age))
# if age < 18:
#     status = "Kid"
# elif age < 60:
#     status = "Adult"
# elif age < 90:
#     status = "Sr Citizen"
# else:
#     status = "Awesome"
#     print("Thanks for visiting")
#
# print("You are", status)

age = int(input("please enter your age"))
print("age:", age)
if 18 < age < 40:
    status = "Issue Driving License"
elif age < 18:
    status = "Come again"
else:
    status = "Health Certificate Require"
    print("Thanks for visiting")
print(status)



