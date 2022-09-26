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
# def pal():
#     n = input("Please enter the value")
#     n1 = (n[::-1])
#     if n==n1:
#         print("number is pal")
#     else:
#         print("number is not pal")
# pal()

# Write a python program using function to take input player name, runs, balls and display strike rate of that player
# def Strike_rate():
#     Player_name = input("Please enter player name")
#     Runs = int(input("Please enter runs"))
#     Balls = int(input("Please enter balls"))
#     n = Runs/Balls
#     n1 = n*100
#     print(f"Strike rate of {Player_name} is {n1}")
# Strike_rate()

# Write a python program using function to take
# runs scored in 5 matches, store it in list and display total runs scored in 5 matches

# def Total_run_score():
#     Player_runs = []
#     Sum_of_runs = 0
#     for i in range(1,6):
#         Match = int(input(f"Enter score of match {i}: "))
#         Player_runs.append(Match)
#     for j in Player_runs:
#         Sum_of_runs = Sum_of_runs + j
#     print(f"Total runs scored in 5 matches is {Sum_of_runs}")
# Total_run_score()

# Write a program to take player name and runs scored in 5 matches
# store it in a dictionary and display name and the score for all the players
#     having century
# ======================================================================
# for i in range(1,4):
#     Match = input(f"Please enter player name {i}")
# for j in range(1,4):
#     Match = int(input(f"Please enter run scored {j}"))
# ===================================================================
dict = {}
ply1 = input("Please enter 1st player name")
score1 = int(input("Please enter 1st score"))
ply2 = input("Please enter 1st player name")
score2 = int(input("Please enter 2nd score"))
ply3 = input("Please enter 1st player name")
score3 = int(input("Please enter 3rd score"))
Player = {ply1 : score1, ply2: score2, ply3: score3}
print(Player)
for i in Player:
    # print(f"{i}:{Player[i]}")
    if Player[i] > 100:
        print(f"{i}--->{Player[i]}")
