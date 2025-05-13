#Rock, Paper, Scissors 

import random 
Computer = ["Rock", "Paper", "Scissors"]

User = input("Rock, Paper, Scissor?: ")
print(User)
print(random.choice(Computer))

#Conditions 

if User == "Rock" and Computer == "Scissor":
    print("User Wins!")
elif User == "Rock" and Computer == "Paper":
    print("Computer Wins!")
elif User == "Paper" and Computer == "Rock":
    print("User Wins!")
elif User == "Paper" and Computer == "Scissor":
    print("Computer Wins!")
if User == "Scissor" and Computer == "Paper":
    print("User Wins!")
elif User == "Scissor" and Computer == "Rock":
    print("Computer Wins!")
else: 
    print("Draw")
    