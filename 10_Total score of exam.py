# score = int(input("please enter your score"))
# print("score:", score)
# if score > 90:
#     status = "merit"
# elif score > 70:
#     status = "distinction"
# elif score > 60:
#     status = "first class"
# elif score > 35:
#     status = "pass"
# else:
#     status = "try again"
# print(status)

score = int(input("please enter your score"))
print("score:", score)
if score < 100 and score >= 90:
    status = "merit"
elif score < 90 and score >= 70:
    status = "distinction"
elif score < 70 and score >= 60:
    status = "first class"
elif score < 60 and score >= 35:
    status = "pass"
else:
    status = "try again"
print(status)

