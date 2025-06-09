# The rules follow the classic “Rock Paper Scissors” game, but with two new choices – “Lizard” and “Spock”:

# Scissors cut Paper.
# Paper covers Rock.
# Rock crushes Lizard.
# Lizard poisons Spock.
# Spock smashes Scissors.
# Scissors beat Lizard.
# Lizard eats Paper.
# Paper disproves Spock.
# Spock vaporizes Rock.
# Rock breaks Scissors.

import random

print("================================")
print("Rock Paper Scissors Lizard Spock")
print("================================")

print("1) ✊")
print("2) ✋")
print("3) ✌️")
print("4) 🦎")
print("5) 🖖")

user_input = int(input("Pick a number: "))
computer = random.randint(1, 5)

print("You Choose: ", user_input)
print("CPU Choose: ", computer)

if user_input == 1 and computer == 1:
    print("It's a Tie")
elif user_input == 1 and computer == 2:
    print("The Computer Won!")
elif user_input == 1 and computer == 3:
    print("The Player Won!")
elif user_input == 1 and computer == 4:
    print("The Player Won!")
elif user_input == 1 and computer == 5:
    print("The Computer Won!")
elif user_input == 2 and computer == 1:
    print("The Player Won!")
elif user_input == 2 and computer == 2:
    print("It's a Tie")
elif user_input == 2 and computer == 3:
    print("The Computer Won!")
elif user_input == 2 and computer == 4:
    print("The Computer Won!")
elif user_input == 2 and computer == 5:
    print("The Player Won!")
elif user_input == 3 and computer == 1:
    print("The Computer Won!")
elif user_input == 3 and computer == 2:
    print("The Player Won!")
elif user_input == 3 and computer == 3:
    print("It's a Tie")
elif user_input == 3 and computer == 4:
    print("The Player Won!")
elif user_input == 3 and computer == 5:
    print("The Computer Won!")
elif user_input == 4 and computer == 1:
    print("The Computer Won!")
elif user_input == 4 and computer == 2:
    print("The Player Won!")
elif user_input == 4 and computer == 3:
    print("The Computer Won!")
elif user_input == 4 and computer == 4:
    print("It's a Tie")
elif user_input == 4 and computer == 5:
    print("The Player Won!")
elif user_input == 5 and computer == 1:
    print("The Player Won!")
elif user_input == 5 and computer == 2:
    print("The Computer Won!")
elif user_input == 5 and computer == 3:
    print("The Player Won!")
elif user_input == 5 and computer == 4:
    print("The Computer Won!")
elif user_input == 5 and computer == 5:
    print("It's a Tie")
else:
    print("Invalid Option")
    

