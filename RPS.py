#Rock, Paper, Scissors 

import random 
computer = ["Rock", "Paper", "Scissors"]

user = input("Rock, Paper, Scissors?\n").strip()
print("User chose: ", user)

#Conditions 
if user not in computer: 
    print("Invalid input. Please choose : Rock, Paper or Scissors")
else:
    computer_choice = random.choice(computer)
    print("Computer chose: ", computer_choice)

    if user == "Rock" and computer_choice == "Scissors":
        print("Result: User Wins!")
    elif user == "Rock" and computer_choice == "Paper":
        print("Result: Computer Wins!")
    elif user == "Paper" and computer_choice == "Rock":
        print("Result: User Wins!")
    elif user == "Paper" and computer_choice == "Scissors":
        print("Result: Computer Wins!")
    elif user == "Scissors" and computer_choice == "Paper":
        print("Result: User Wins!")
    elif user == "Scissors" and computer_choice == "Rock":
        print("Result: Computer Wins!")
    else: 
        print("Result: Draw")
    