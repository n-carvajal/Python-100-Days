# 100 Days of Python Code

## Project 25: Name The State Game

Create a game where you can guess all 50 States in the United States and see their labels being populated on a map.

### Notes

* Upon starting the game, the game looks in `states_guessed.csv` to see if there are any previous instances of the
game that are unfinished.  
* If there are no previous guesses stored in `states_guessed.csv` the game will start from scratch.
* Otherwise, the game asks the user if they want to continue with the previous game or start new one.
* If the player chooses to start fresh, the data in `states_guessed.csv` and `missing_states.csv` will be deleted and the game will start from scratch.
* If the player chooses to continue with the previous game instance then the game will continue from where it was previously closed.
* Given the amount of states to guess, every 10 guesses the player is asked if the wish to continue or exit the game.
* Upon game exit, the `states_guessed.csv` and `missing_states.csv` files will be repopulated.

In order to play the game run `main.py`
