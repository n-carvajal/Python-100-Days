"""
Clone of road crossing game.
"""

# Imports
from time import sleep  # Speeds up or slows down time.
from turtle import Screen  # To set up the screen.

from pygame import mixer  # Allows music to be played in game.

from objects import Background, Car, Player, Scoreboard

# Setup screen.
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("grey25")

# Initialise mixer.
mixer.init()

# Play background music as a loop.
mixer.music.load("23 - Turtle Crossing/background.wav")
mixer.music.play(-1)

# Create sound objects for player movement and game over.
car_crash = mixer.Sound("23 - Turtle Crossing/game_over.wav")
crossing_success = mixer.Sound("23 - Turtle Crossing/success.wav")

# Instantiate Scoreboard object.
scoreboard = Scoreboard()

# Turn off auto update and set screen to listen for key presses.
screen.tracer(0)
screen.listen()

# Instantiate Background object and set up background.
background = Background()
background.grass()
background.lines()
background.dashes()

# Instantiate Player object 'onyx'.
onyx = Player()

# Create car lists to house future instantiated car objects.
cars_all_created = []
cars_starting_right = []
cars_starting_left = []

# Watch for "-" arrow key presses and perform corresponding 'onyx' method if detected.
screen.onkeypress(onyx.upwards, "Up")
screen.onkeypress(onyx.downwards, "Down")
screen.onkeypress(onyx.leftwards, "Left")
screen.onkeypress(onyx.rightwards, "Right")

# Create variable to track game level.
level = 1

# Variable showing initial sleep() value for the game.
time_delay = 0.15

# Create game over while loop.
game_over = False
while not game_over:

    # Print scoreboard showing level.
    scoreboard.clear()
    scoreboard.display("Current Level", level, (0, 370), 15)

    # Set game sleep() and update the screen.
    sleep(time_delay)
    screen.update()

    # Instantiate Car object 'car'.
    car = Car()

    # Spawn car and if method returns True.
    if car.spawn():
        # Append car to cars_starting_left and cars_all_created lists.
        cars_starting_left.append(car)
        cars_all_created.append(car)
    # If method returns False.
    else:
        # Append car to cars_starting_right and cars_all_created lists.
        cars_starting_right.append(car)
        cars_all_created.append(car)

    # For every car in cars_starting_left list move car forward by 20.
    for car in cars_starting_left:
        car.forward(20)     # 20 is the standard turtle length and width value.

    # For every car in cars_starting_right list move car backwards by 20.
    for car in cars_starting_right:
        car.backward(20)    # 20 is the standard turtle length and width value.

    # Detect collision by checking if 'onyx' is within 20 of 'car' object.
    for car in cars_all_created:
        if onyx.distance(car.position()) < 5:  # 20 is the standard turtle length and width value.
            car_crash.play()    # Play car crash sound.
            game_over = True

    # Detect road crossed successfully if 'onyx' ycor() is equal to 338. Send 'onyx' back to start position.
    if onyx.ycor() == 338:  # 338 is the end y-coordinate position for 'onyx' on the screen.
        crossing_success.play()     # Play successful crossing sound.
        onyx.goto(0, -337)  # -337 is the start y-coordinate position for 'onyx' on the screen.
        time_delay *= 0.9   # 0.9 is a user defined value by which to decrease time delay.
        level += 1   # Increase level counter by 1.

# Clear turtle objects and display game over scoreboard.
background.clear()
scoreboard.display("GAME OVER\nReached Level", level, (0, 0), 30)
screen.exitonclick()
