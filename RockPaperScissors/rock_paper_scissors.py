# The rules are as follows:

# Rock beats Scissors.
# Scissors beat Paper.
# Paper beats Rock.
# First, create a player and a computer variable.

# Prompt the player to select number between 1 and 3 with input() and store it in player:

# 1 is for '✊' (Rock). 
# 2 is for '✋' (Paper).
# 3 is for '✌️' (Scissors).
# Then, use the random.randint() method to assign a number to the computer variable (1 to 3).

#Lastly, use control flow to compare the user's choice and the computer's choice, determine the winner, and print out who won.

import random

computer = random.randint(1, 3)

print("===================")
print("Rock Paper Scissors")
print("===================")

print("1) ✊")
print("2) ✋")
print("3) ✌️")
user_input = int(input("Pick a number: "))

print("You choose: ", user_input)
print("CPU choose: ", computer)

if user_input == 1 and computer == 1:
    print("It's Tie")
elif user_input == 1 and computer == 2:
    print("The Computer Won!")
elif user_input == 1 and computer == 3:
    print("The Player Won!")
elif user_input == 2 and computer == 1:
    print("The Player Won!")
elif user_input == 2 and computer == 2:
    print("It's Tie")
elif user_input == 2 and computer == 3:
    print("The Computer Won!")
elif user_input == 3 and computer == 1:
    print("The Computer Won!")
elif user_input == 3 and computer == 2:
    print("The Player Won!")
elif user_input == 3 and computer == 3:
    print("It's Tie")
else:
    print("Invalid Option")




