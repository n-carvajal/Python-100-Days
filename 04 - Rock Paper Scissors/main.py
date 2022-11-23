"""Rock Paper Scissors Simulator"""

# import randint from random
from random import randint
from hand_art import responses

# Intro:
print("Welcome to ROCK PAPER SCISSORS!")
print("Would you like to play?")

# While game_over:
GAME_OVER = True
ASKED_TO_PLAY = 0
while GAME_OVER:
    play = input("Type 'Yes' or 'No': ")
    ASKED_TO_PLAY += 1
    if play.lower() != "yes" and play.lower() != "no":
        print("That is not a valid input.")
        print("Let's try again...")
        continue
    elif play.lower() == "no" and ASKED_TO_PLAY == 1:
        print("Are you sure?")
        print("It's a lot of fun.")
        continue
    elif play.lower() == "no":
        print("Understood.")
        print("Maybe some other time...")
        break
    else:
        print("Great! Let's play...")
        print("Best out of 5")
        GAME_OVER = False
# Win counters:
P1_WINS = 0
CPU_WINS = 0
# While game not won:
while P1_WINS + CPU_WINS < 5:
    p1_choice = int(input("Type 0 for 'Rock', 1 for 'Paper', or 2 for 'Scissors': "))
    cpu_choice = randint(0, 2)
    # If player out of bounds:
    if p1_choice < 0 or p1_choice >= 3:
        print("Invalid input")
        continue
    # Else player in bounds:
    else:
        print(f"You chose {responses[p1_choice]}")
        print(f"I chose {responses[cpu_choice]}")
    # If both players and cpu pick same response:
    if p1_choice == cpu_choice:
        print("It's a DRAW")
        print(f"The current score is {P1_WINS} to you and {CPU_WINS} to me.")
        continue
    # If player chooses scissors and cpu chooses rock:
    if p1_choice == 2 and cpu_choice == 0:
        CPU_WINS += 1
        print("You LOSE!")
        print(f"The current score is {P1_WINS} to you and {CPU_WINS} to me.")
        continue
    # If cpu chooses scissors and player chooses rock:
    if cpu_choice == 2 and p1_choice == 0:
        P1_WINS += 1
        print("You WIN!")
        print(f"The current score is {P1_WINS} to you and {CPU_WINS} to me.")
        continue
    # If player chooses higher value than cpu:
    if p1_choice > cpu_choice:
        P1_WINS += 1
        print("You WIN!")
        print(f"The current score is {P1_WINS} to you and {CPU_WINS} to me.")
        continue
    # If cpu chooses higher value than player:
    if cpu_choice > p1_choice:
        CPU_WINS += 1
        print("You LOSE!")
        print(f"The current score is {P1_WINS} to you and {CPU_WINS} to me.")
        continue
if CPU_WINS > P1_WINS:
    print("\nGame Over.")
    print(f"You lost {P1_WINS} to {CPU_WINS}")
else:
    print("\nGame Over.")
    print(f"You won {P1_WINS} to {CPU_WINS}")
