"""US States Game"""

# Imports
from turtle import Screen, Turtle

import pandas as pd


# Class
class Label(Turtle):
    """
    Label class that inherits from Turtle class.
    """
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()


# Functions
def new_game():
    """
    Function that asks the user if they want to start a new game or continue with old one and validates their input
    to ensure it is either "new" or "continue".

    Returns True if "new"
    Returns False if "continue"
    """
    while True:
        new_start = screen.textinput("Continue Previous?", "Yes or No: ").lower()
        if new_start == "yes":
            return False
        elif new_start == "no":
            return True
        else:
            continue


def end_game():
    """
    Function that asks the user if they want to quit the game or keep going and validates their input
    to ensure it is either "yes" or "no".

    Returns True if "no"
    Returns False if "yes"
    """
    while True:
        quit_game = screen.textinput("Want To Keep Going?", "Yes or No: ").lower()
        if quit_game == "yes":
            return False
        elif quit_game == "no":
            return True
        else:
            continue


# Setup Screen
screen = Screen()
screen.setup(width=725, height=500)
screen.bgpic("25 - US States Game/background.gif")
screen.title("U.S. States Game")
screen.tracer(0)

# Instantiate label object
label = Label()

# Use pandas to read corresponding csv files.
all_states_df = pd.read_csv("25 - US States Game/50_states.csv")
states_guessed_df = pd.read_csv("25 - US States Game/states_guessed.csv")
states_remaining_df = pd.read_csv("25 - US States Game/missing_states.csv")

# Use pandas to generate lists from 'state' Series for each file.
states_list = all_states_df["state"].to_list()
states_guessed = states_guessed_df["state"].to_list()
states_remaining = states_remaining_df["state"].to_list()

# Draw previous game map state.
for state in states_guessed:
    x_pos = int(all_states_df.loc[all_states_df["state"] == state, "x"])
    y_pos = int(all_states_df.loc[all_states_df["state"] == state, "y"])
    position = (x_pos, y_pos)
    label.goto(position)
    label.write(state, True, "center", ("Arial", 8, "normal"))

# Check length of states guessed and if equal to zero start a new game otherwise ask if player wishes to continue.
if len(states_guessed) == 0:
    label.clear()
    states_guessed = []
    states_remaining_df = pd.read_csv("25 - US States Game/50_states.csv")
    states_remaining = states_remaining_df["state"].to_list()
else:
    if new_game():
        label.clear()
        states_guessed = []
        states_remaining_df = pd.read_csv("25 - US States Game/50_states.csv")
        states_remaining = states_remaining_df["state"].to_list()

# Set input box labels and guess attempt counter.
box_title = "Name the State"
box_text = "Guess a state: "
guess_attempts = 0

# Game while loop that continues until guess list length is equal to state list length.
while len(states_guessed) < len(states_list):

    # Update screen, ask for a guess, and update guess counter.
    screen.update()
    state = screen.textinput(box_title, box_text).title()
    guess_attempts += 1

    # If guess is not in 'states_list'.
    if state not in states_list:
        box_title = "Not a State"
        box_text = "Try Again: "
    # Else if guess is in 'states_guessed'.
    elif state in states_guessed:
        box_title = "Already Guessed That"
        box_text = "Guess Another: "
    # Else if guess is in 'states_list'.
    elif state in states_list:
        # Append guess to 'states_guessed'.
        states_guessed.append(state)
        # Pop state guessed from 'states_remaining' list by determining index within list with '.index()` method.
        states_remaining.pop(states_remaining.index(state))
        # Grab the 'x' and 'y' values from all_states DataFrame with Pandas filtering.
        x_pos = int(all_states_df.loc[all_states_df["state"] == state, "x"])
        y_pos = int(all_states_df.loc[all_states_df["state"] == state, "y"])
        # Send label to position and write the guessed state's name in place.
        position = (x_pos, y_pos)
        label.goto(position)
        label.write(state, True, "center", ("Arial", 8, "normal"))
        # Provide correct guess feedback in input box.
        box_title = f"{len(states_guessed)} / {len(states_list)} correct."
        box_text = "Guess a state: "

    # Ask the user if they want to continue with the game or exit every 10 guesses.
    if guess_attempts % 10 == 0:
        # If user wants to end the game.
        if end_game():
            # Clear the screen and write label providing feedback on correct and missing states.
            screen.clear()
            label.goto(0, 40)
            label.write(f"You guessed {len(states_guessed)} states!\n\nYou missed {len(states_remaining)} states.\n\n"
                        f"The missing states have been saved to the file 'missing_states.csv'",
                        True, "center", ("Arial", 10, "normal"))
            # Convert 'states_guessed' and 'missing_states' to Pandas Series' with 'state' as the column label.
            states_guessed = pd.Series(states_guessed, name="state")
            missing_states = pd.Series(states_remaining, name="state")
            # Write Pandas Series' 'states_guessed' and 'missing_states' to csv file.
            states_guessed.to_csv("25 - US States Game/states_guessed.csv")
            missing_states.to_csv("25 - US States Game/missing_states.csv")
            # End Game.
            break

screen.exitonclick()
