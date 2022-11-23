"""Higher Lower Game"""

# Imports
from random import randint
from game_data import data
import art


# Function Definitions
def pick_item():
    """Picks random item from data."""
    random_index = randint(0, 49)
    item = data[random_index]
    return item


def display_item(item):
    """Prints item as a formatted string."""
    print(f"{item['name']}: {item['description']} from {item['country']}.")


def choice():
    """Asks the user to select between 'A' or 'B' and validates input."""
    while True:
        answer_given = input("Enter Choice: ").lower()
        if answer_given == "a" or answer_given == "b":
            return answer_given
        else:
            print("You did not enter 'A' or 'B', try again.")


# Set Variables.
SCORE = 0
WINNING = True
# Pick 'item_a' from 'game_data.py'
item_a = pick_item()
# While answering correctly.
while WINNING:
    # Pick 'item_b' from 'game_data.py'.
    item_b = pick_item()
    # Index 'follower_count' for each item.
    followers_a = item_a["follower_count"]
    followers_b = item_b["follower_count"]
    # While 'followers_a' and 'followers_b' are equal.
    while followers_a == followers_b:
        # Re-pick 'item_b' and get corresponding 'follower_count'.
        item_b = pick_item()
        followers_b = item_b["follower_count"]
    # If 'followers_a' is greater than 'followers_b'.
    if followers_a > followers_b:
        ANSWER = "a"
    else:
        ANSWER = "b"
    # Start game by creating space and printing logo.
    print("\n" * 50)
    print(art.logo)
    # If score is greater than 0.
    if SCORE > 0:
        print(f"Correct. Your current score is: {SCORE}. Let's try another.")
    # Print formatted string of 'item_a'.
    display_item(item_a)
    # For testing print follower_a.
    print(followers_a)
    # Print VS logo.
    print(art.vs)
    # Print formatted string of 'item_b'
    display_item(item_b)
    # For testing print 'followers_b'.
    print(followers_b)
    print(f"Who has more followers? A: {item_a['name']} or B: {item_b['name']}")
    # Ask user for a guess.
    guess = choice()
    # If guess is equal to answer.
    if guess == ANSWER:
        SCORE += 1
        # If answer is equal to 'b'.
        if ANSWER == "b":
            item_a = item_b
    else:
        print(f"That was incorrect. Your final score is {SCORE}")
        break
print("Game Over")
