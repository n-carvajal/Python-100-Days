"""
A clone of the hungry snake game.
"""

# Imports
import time
from random import randint, randrange
from turtle import Screen, Turtle


# Functions
def game_start():
    """
    Asks player if they want to play Hungry Snake.
    Returns True if 'yes'.
    Returns False if 'no'.
    """
    while True:
        if GAMES_PLAYED < 1:
            play = screen.textinput("Want to play Hungry Snake?", "Type 'Yes' or 'No': ").lower()
            if play == "yes":
                return True
            if play == "no":
                return False
        else:
            play = screen.textinput("Want to play again?", "Type 'Yes' or 'No': ").lower()
            if play == "yes":
                return True
            if play == "no":
                return False


def create_scoreboard(position, points, text):
    """
    Creates score board at position and prints text reflecting showing points.

    'position' = user defined coordinate as a tuple.
    'points' = 'score'.
    'text' = user defined string of text to display.
    """
    x, y = position
    scoreboard.clear()
    scoreboard.penup()
    scoreboard.goto(x, y)
    scoreboard.pencolor("white")
    scoreboard.write(f"{text}: {points}", False, "center", ("arial", 12, "normal"))
    scoreboard.hideturtle()


def update_scoreboard(points, text):
    """
    Clears then re-writes and updates scoreboard.
    'points' = 'score'.
    """
    scoreboard.clear()
    scoreboard.write(f"{text}: {points}", False, "center", ("arial", 12, "normal"))


def random_colour():
    """
    Creates a random colour in RGB format by generating a random value from 100 - 200 for 'r', 'g', and 'b'.
    Returns 'r', 'g', 'b'.
    """
    r = randint(100, 200)
    g = randint(100, 200)
    b = randint(100, 200)
    return r, g, b


def create_snake(coordinates, length, growth_factor):
    """
    Creates the starting snake body.

    Creates 'length' quantity of Turtle() objects each called 'snake_segment'.
    Each 'snake_segment' is assigned a set of identical attributes (growth_factor, shape, color, penup).
    The first 'snake_segment' created is placed at 'coordinates' on the screen.
    Subsequent 'snake_segment' objects are moved left on the 'X' axis by default size * growth factor.
    Every created 'snake_segment' is appended to the list 'snake_segments'.

    'coordinates' = 'snake_starting_position'
    'length' = 'snake_length'
    'growth_factor' = 'snake_growth_factor'

    """
    x_pos, y_pos = coordinates
    for _ in range(length):
        snake_segment = Turtle()
        snake_segment.hideturtle()
        snake_segment.penup()
        snake_segment.goto(x_pos, y_pos)
        snake_segment.turtlesize(growth_factor)
        snake_segment.shape("square")
        snake_segment.color(random_colour())
        snake_segment.showturtle()
        snake_segments.append(snake_segment)
        x_pos -= SNAKE_SEGMENT_DEFAULT_SIZE * growth_factor


def move_snake(speed):
    """
    Moves the turtle objects in 'snake_segments' forward at 'speed'.

    It does so by moving the last object in snake_segments, to the second to last's position.
    The second to last object to the third to last's position.
    ....etc...
    The second object to the first object's position.
    Then it moves the first object forward by 20 (the size of itself).

    'speed' = user defined input 0 - 10.
    """
    snake_segments[0].speed(speed)
    for seg in range(len(snake_segments) - 1, 0, -1):
        position = snake_segments[seg - 1].pos()
        snake_segments[seg].goto(position)
    snake_segments[0].forward(20)


def snake_right():
    """
    Sets the first object in the snake_segments list to East.
    """
    if snake_segments[0].heading() != 180:
        snake_segments[0].setheading(0)


def snake_left():
    """
    Sets the first object in the snake_segments list to West.
    """
    if snake_segments[0].heading() != 0:
        snake_segments[0].setheading(180)


def snake_up():
    """
    Sets the first object in the snake_segments list to North.
    """
    if snake_segments[0].heading() != 270:
        snake_segments[0].setheading(90)


def snake_down():
    """
    Sets the first object in the snake_segments list to South.
    """
    if snake_segments[0].heading() != 90:
        snake_segments[0].setheading(270)


def snake_control():
    """
    Listens for an "Up", "Down", "Left", or "Right" arrow keypress and assigns the corresponding heading
    to the first item in the snake_segments list.
    """
    screen.onkey(snake_up, "Up")
    screen.onkey(snake_down, "Down")
    screen.onkey(snake_left, "Left")
    screen.onkey(snake_right, "Right")


def add_snake_segment(coordinates):
    """
    Adds a Turtle() snake_segment object to the back of the snake.

    Obtains the 'coordinates' of the last item in 'snake_segments'.
    Creates a new invisible Turtle() snake_segment.
    Sends the new 'snake_segment' to 'coordinates' and moves the 'x_pos' left by default size * growth factor.
    Adds the same attributes as the rest of the objects in 'snake_segments'.
    Appends the new snake_segment to 'snake_segments' list.
    Once object appended to 'snake_segment' list makes object visible.

    'coordinates' = snake_segments[-1].position()
    """
    x_pos, y_pos = coordinates
    snake_segment = Turtle()
    snake_segment.hideturtle()
    snake_segment.penup()
    snake_segment.goto(x_pos, y_pos)
    snake_segment.turtlesize(SNAKE_GROWTH_FACTOR)
    snake_segment.shape("square")
    snake_segment.color(random_colour())
    snake_segment.showturtle()
    snake_segments.append(snake_segment)


def check_snake_collision(snake_body):
    """
    Checks to see if the head of the snake has hit its own body.

    Takes the positions of the objects in 'snake_segments' from index [1] to end of list.
    Unpacks the tuple position of the objects in 'snake_segments' to x and y.
    Converts x, and y to integers and repacks into a tuple called 'integer_snake_body_position'.
    Appends 'integer_snake_body_position' to a list called 'snake_body_positions'.
    Takes the position of the object in 'snake_segments[0]'.
    Unpacks the tuple position of snake_segments[0] to a and b.
    Converts a and b to integers and repacks into a tuple called 'snake_head_position'
    Checks to see if the position of 'snake_head_position' is in the list 'snake_body_positions'.
    Returns True if condition is met.
    """
    snake_body_positions = []
    for index in range(1, len(snake_body)):
        x, y = snake_body[index].position()
        integer_snake_body_position = (int(x), int(y))
        snake_body_positions.append(integer_snake_body_position)
    a, b = snake_body[0].position()
    snake_head_position = (int(a), int(b))
    if snake_head_position in snake_body_positions:
        return True


def check_wall_collision():
    """
    Checks to see if snake hit a wall.

    Takes the position of the object at snake_segments[0].
    Checks to see if the position is outside the bounds of the screen (-390 < x < 390, -390 < y < 390).
    If yes, prints 'Ouch! You hit a wall.
    Returns True if condition met.
    """
    if (
        snake_segments[0].xcor() <= -390
        or snake_segments[0].xcor() >= 390
        or snake_segments[0].ycor() <= -390
        or snake_segments[0].ycor() >= 390
    ):
        return True


def create_random_food(growth_factor):
    """
    Creates a red and round food turtle object half the size of a 'snake_segment'.
    Places food object at a random position on screen at intervals of 20.
    Where values for randrange in random tuple are screensize bounds less 20.
    """
    food.shape("circle")
    food.penup()
    food.color("red")
    food.turtlesize(growth_factor)
    random_tuple = (randrange(-380, 380, 20), randrange(-380, 380, 20))
    food.setposition(random_tuple)


def check_food_collision():
    """
    Checks if the first object in snake_segments position is less than 15 away from the random food position.
    Returns True if condition met.
    """
    spawned_food = food.position()
    snake_head = snake_segments[0]
    if snake_head.distance(spawned_food) <= 10:
        return True


def food_eaten():
    """
    If there is a food collision, then the food object is hidden on screen.
    """
    food.hideturtle()


# Setup Screen.
screen = Screen()
screen.resetscreen()
screen.setup(width=800, height=800)
screen.colormode(255)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Hungry Snake")
# Create scoreboard.
scoreboard = Turtle()
SCORE = 0
create_scoreboard((0, 370), SCORE, "Current Score")
# Create game start prompt:
GAMES_PLAYED = 0
GAME_ON = game_start()
while GAME_ON:
    # Create snake body and start position.
    snake_starting_position = (0, 0)
    SNAKE_LENGTH = 3
    SNAKE_GROWTH_FACTOR = 1
    SNAKE_SEGMENT_DEFAULT_SIZE = 20
    snake_segments = []
    snake = Turtle()
    create_snake(snake_starting_position, SNAKE_LENGTH, SNAKE_GROWTH_FACTOR)
    screen.update()
    # Create and place random snake food.
    FOOD_GROWTH_FACTOR = SNAKE_GROWTH_FACTOR / 2
    food = Turtle()
    create_random_food(FOOD_GROWTH_FACTOR)
    # Set focus on screen for key-presses:
    screen.listen()
    # Start while loop for gameplay
    TIME_SPEED = 0.1
    GAME_OVER = False
    while not GAME_OVER:
        time.sleep(TIME_SPEED)
        SNAKE_SPEED = 5
        screen.update()
        # Move the snake segments.
        move_snake(SNAKE_SPEED)
        snake_control()
        # Detect collision with wall.
        if check_wall_collision():
            create_scoreboard((0, 0), SCORE, "Ouch! You hit a wall!\nGame Over.\nYour Final Score is ")
            GAMES_PLAYED += 1
            if game_start():
                create_scoreboard((0, 370), SCORE, "Current Score")
                food_eaten()
                for segment in snake_segments:
                    segment.hideturtle()
                GAME_ON = True
                break
            else:
                GAME_ON = False
                GAME_OVER = True
        # Detect collision with food.
        if check_food_collision():
            # Eat food.
            food_eaten()
            # Add point to scoreboard when food eaten.
            SCORE += 1
            update_scoreboard(SCORE, "Current Score")
            # Add snake_segment to tail when food eaten.
            add_snake_segment(snake_segments[-1].position())
            # Create and randomly place new food object after food eaten.
            food = Turtle()
            create_random_food(FOOD_GROWTH_FACTOR)
            # Increase snake speed every 'level_up' food items eaten.
            LEVEL_UP = 10
            if SCORE % LEVEL_UP == 0:
                TIME_SPEED -= 0.02
        # Detect collision with body.
        if check_snake_collision(snake_segments):
            create_scoreboard((0, 0), SCORE, "Oh no! You hit your own tail!\nGame Over.\nYour Final Score is ")
            GAMES_PLAYED += 1
            if game_start():
                create_scoreboard((0, 370), SCORE, "Current Score")
                food_eaten()
                for segment in snake_segments:
                    segment.hideturtle()
                GAME_ON = True
                break
            else:
                GAME_ON = False
                GAME_OVER = True
# End game:
print("Program Exited.")
screen.exitonclick()
