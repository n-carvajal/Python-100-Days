"""Guessing Game App"""

# Imports
from random import randint

# Functions


def game_number():
    """Generates random number with randint"""
    return randint(1, 100)


def game_difficulty():
    """Asks player to choose a difficulty ('Easy' or 'Hard') and returns lives to use."""
    valid_difficulty = False
    while not valid_difficulty:
        level = input("Would you like to play the 'Easy' or 'Hard' version: ").lower()
        if level == "easy":
            return 10
        elif level == "hard":
            return 5
        else:
            print("You did not type 'Easy' or 'Hard'. Try again.")


def player_choice():
    """Asks player to choose a number in range. Ensures value is numerical and in range."""
    valid_choice = False
    while not valid_choice:
        choice = input("Pick a number between 1 - 100: ")
        if not choice.isdigit():
            print("You did not type a numerical value. Try again.")
        else:
            choice = int(choice)
            if choice not in range(1, 101):
                print("You did not pick a number between 1 - 100. Try again.")
            else:
                valid_choice = True
    return choice


def replay_game():
    """Asks if player wants to play again."""
    valid_replay = False
    while not valid_replay:
        replay = input("Would you like to play again ('Yes' or 'No'): ")
        if replay == "yes":
            return True
        if replay == "no":
            return False
        else:
            print("You did not type either 'Yes' or 'No'. Try again.")


# Game
print("Welcome to the guessing game.")
print("I'm thinking of a number from 1 - 100.")
guesses = []
RESTART = True
while RESTART:
    number = game_number()
    # Testing
    print(f"For testing purposes the number I'm thinking of is {number}.")
    LIVES = game_difficulty()
    while LIVES > 0:
        guess = player_choice()
        guesses.append(guess)
        if guesses.count(guess) > 1:
            print("You have already guessed that number.")
            print("You did not loose any lives. Try again.")
        elif number == guess:
            print("You win.")
            break
        elif abs(number - guess) < 11:
            LIVES -= 1
            print("You are CLOSE. Within 10.")
            print(f"You have {LIVES} attempts left.")
        elif guess < number:
            LIVES -= 1
            print("Your guess is TOO LOW.")
            print(f"You have {LIVES} attempts left.")
        else:
            LIVES -= 1
            print("Your guess is TOO HIGH.")
            print(f"You have {LIVES} attempts left.")
    if LIVES == 0:
        print("Sorry. You are out of lives.")
    RESTART = replay_game()
print("Game Over")
