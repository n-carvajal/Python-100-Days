"""
A clone of the Hungry Snake Game using OOP.
"""

# Imports.
from time import sleep
from turtle import Screen

from pygame import mixer

from food import Food
from scoreboard import Scoreboard
from snake import Snake


# Functions.
def play_game():
    """
    Asks player if they want to play Hungry Snake.
    Returns True if 'yes'.
    Returns False if 'no'.
    """
    while True:
        if GAMES_PLAYED < 1:
            play = screen.textinput("Want to play Hungry Snake?", "Type 'Yes' or 'No': ")
            if play.lower() == "yes":
                return True
            elif play.lower() == "no":
                return False
        else:
            play = screen.textinput("Want to play again?", "Type 'Yes' or 'No': ")
            if play.lower() == "yes":
                return True
            elif play.lower() == "no":
                return False


def wall_collision():
    """
    Checks to see if snake hit a wall.

    Takes the position of the object at snake.segments[0].
    Checks to see if the position is outside the bounds of the screen (-390 < x < 390, -390 < y < 390).
    Returns True if condition met.
    """
    if (
        snake.segments[0].xcor() <= -390
        or snake.segments[0].xcor() >= 390
        or snake.segments[0].ycor() <= -390
        or snake.segments[0].ycor() >= 390
    ):
        return True


def food_collision():
    """
    Checks if 'snake.segments[0]' is less than 10 away from 'food.position()'.
    Returns True if condition met.
    """
    if snake.segments[0].distance(food.position()) <= 10:
        return True


def body_collision():
    """
    Checks to see if 'snake.segments[0]' has hit its own body.

    Loops through the segment objects in 'snake.segments' from index[1] to end of list.
    Takes the position of each segment and checks if snake.segments[0] is at distance within 10 of that position.
    Returns True if condition is met.
    """
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment.position()) < 10:
            return True


# Instantiate Screen object.
screen = Screen()

# Initiate pygame mixer
mixer.init()

# Setup Screen Parameters.
screen.setup(width=800, height=800)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Hungry Snake")
screen.tracer(0)

# Create counter for games played.
GAMES_PLAYED = 0

# Instantiate Scoreboard object.
scoreboard = Scoreboard()

# Start a while loop for 'game_start'.
GAME_START = play_game()
while GAME_START:

    # Play background music.
    mixer.music.load("21 - Snake Game (OOP)/background.wav")
    mixer.music.play(-1)

    # Create a sound object for eaten food and collisions.
    food_eaten = mixer.Sound("21 - Snake Game (OOP)/eaten_food.wav")
    collision_occurred = mixer.Sound("21 - Snake Game (OOP)/crash.wav")

    # Set game variables.
    scoreboard.score = 0
    NUMBER_SEGMENTS = 2  # Number of segments by which to extend snake when food collision occurs.
    LEVEL_UP = 5  # Number of food items after which to double the 'number_segments'.
    MULTIPLIER = 2  # Number by which to multiply 'number_segments' every 'level_up'
    SLEEP_DELAY = 0.1  # Starting sleep delay with which to start the game.
    SLEEP_MULTIPLIER = 0.98  # Number by which to multiply the time delay to speed up the game.

    # Open 'history.txt' and read the score contents. Convert to integer and assign to 'scoreboard.high_score'.
    with open("21 - Snake Game (OOP)/walls_kill/history.txt", mode="r") as score_history:
        scoreboard.high_score = int(score_history.read())

    # Instantiate a snake and food object.
    snake = Snake()
    food = Food()

    # Add 1 game to 'games_played'.
    GAMES_PLAYED += 1

    # Start listening for key presses.
    screen.listen()
    screen.onkeypress(snake.move_up, "Up")
    screen.onkeypress(snake.move_down, "Down")
    screen.onkeypress(snake.move_left, "Left")
    screen.onkeypress(snake.move_right, "Right")

    # Call spawn() method for snake and food objects. Call create() method for scoreboard object.
    snake.spawn()
    food.spawn()
    scoreboard.create((0, 350), "Current Score", "High Score")

    # Time controller.
    sleep(SLEEP_DELAY)

    # Start a while loop for 'game_over'.
    GAME_OVER = False
    while not GAME_OVER:

        # Set screen.update() and sleep() time delay.
        screen.update()
        sleep(SLEEP_DELAY)

        # Call the move() method on the snake object.
        snake.move()

        # Check for wall collision and provide feedback.
        if wall_collision():
            collision_occurred.play()
            scoreboard.clear()
            scoreboard.create((0, 0), "Ouch you hit a wall!\nGAME OVER\nFinal Score", "\nHigh Score")
            # Take 'scoreboard.high_score' convert to a string and write high score into 'history.txt'.
            with open("21 - Snake Game (OOP)/walls_kill/history.txt", mode="w") as score_history:
                score_history.write(f"{scoreboard.high_score}")
            GAME_OVER = True
            GAME_START = play_game()
            screen.resetscreen()
            break

        # Check for food collision and every 'level_up' increase 'number_segments' to extend by 'multiplier'.
        if food_collision():
            food_eaten.play()
            SLEEP_DELAY *= SLEEP_MULTIPLIER
            scoreboard.score += 1
            food.spawn()
            snake.extend(NUMBER_SEGMENTS)
            scoreboard.clear()
            scoreboard.create((0, 350), "Current Score", "High Score")
            if scoreboard.score % LEVEL_UP == 0:
                NUMBER_SEGMENTS *= MULTIPLIER

        # Check for body collision and provide feedback.
        if body_collision():
            collision_occurred.play()
            scoreboard.clear()
            scoreboard.create((0, 0), "Try not to eat yourself!\nGAME OVER\nFinal Score", "\nHigh Score")
            # Take 'scoreboard.high_score' convert to a string and write high score into 'history.txt'.
            with open("21 - Snake Game (OOP)/walls_kill/history.txt", mode="w") as score_history:
                score_history.write(f"{scoreboard.high_score}")
            GAME_OVER = True
            GAME_START = play_game()
            screen.resetscreen()
            break

# Close game_start while loop with feedback.
scoreboard.clear()
scoreboard.create((0, 0), "\nGAME OVER\nFinal Score", "\nHigh Score")
screen.exitonclick()
