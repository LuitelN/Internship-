stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random 
import csv 
# import pandas as pd ###to be used later when the words data is improved.(remove the words consisting of letters less than 3)

def get_word():
    with open("Words.csv") as f:
        words1 = f.read().splitlines()   
    return random.choice(words1)
name = input("Enter your name to continue: ")
print("Welcome " + name + ", Let's begin")

def hangman():
    chosen_word = get_word()
    
    display = []
    # why using underscore
    for b in chosen_word: #In the chosen word, adds the blank spaces to put the letters 
        display += "a"
    
    end_of_loop = False #Boolean
    lives = 7

    print("\nWelcome to Hangman\n")
    print("Guess the word:-      ", end=" ") 
    print(f"{' '.join(display)}")
    print(f"Lives: {lives}")

    while not end_of_loop:
        guess = input("Guess a Letter: ").lower()
        if not (guess in chosen_word):
            lives -= 1
        index = 0 #yo point bata start garera word check garne 
        for c in chosen_word: #c-> character 
            if c == guess:
                display[index] = guess
            index += 1

        print(f"{' '.join(display)}") #duita values bich ma space jodeko list maa join garda 
        print(f"Lives: {lives}")
        print(stages[lives-1])

        if "_" not in display:
            print("You Win")
            end_of_loop = True

        if lives == 0:
            print("You Lose")
            print(f"The word was: {chosen_word}")
            end_of_loop = True

end_of_game = False

while not end_of_game: #true
    ask = input("Do you want to play Hangman? (y/n): ").lower()
    # import pdb;pdb.set_trace()
    if ask == 'y' or ask == 'yes':
        hangman()
    
    elif ask == 'n' or ask == 'no':
        print("Program Exit Successful")
        end_of_game = True
    else:
        print("Your given input could not be processed.")
        print("Please enter a correct input.")