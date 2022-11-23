"""Pong Game Clone"""

# Imports
from random import randint  # randint() generates a random number from a range of two numbers given
from time import sleep  # sleep() from time speeds up or slows down time.
from turtle import Screen  # Turtle Screen class

from pygame import mixer

from ball import Ball
from net import Net
from paddle import Paddle
from scoreboard import Scoreboard

# Initialize pygame mixer
mixer.init()

# Play background music as a loop.
mixer.music.load("22 - Pong Game/background.wav")
mixer.music.play(-1)

# Create a sound object for a paddle strike.
paddle_hit = mixer.Sound("22 - Pong Game/paddle_beep.wav")

# Setup screen.
screen = Screen()
screen.setup(width=1440, height=800)
screen.bgcolor("dark green")
screen.tracer(0)

# Create net.
net = Net()
net.setup_net(10, 380)  # Where (x, y) represents desired dash length, and y-coordinate for start of net.

# Instantiate scoreboards.
scoreboard = Scoreboard()
p1_scoreboard = Scoreboard()
p2_scoreboard = Scoreboard()

# Create score counters.
P1_SCORE = 0
P2_SCORE = 0

# Instantiate paddles.
p1 = Paddle("Nico", "orange")   # Where (x, y) are player name and paddle colour.
p2 = Paddle("Adri", "cyan")     # Where (x, y) are player name and paddle colour.

# Define scoreboard positions
p1_scoreboard_position = (-120, 340)    # x-coordinate and y-coordinate for position.
p2_scoreboard_position = (120, 340)     # x-coordinate and y-coordinate for position.
game_over_scoreboard_position = (0, -80)    # x-coordinate and y-coordinate for position.

# Display scoreboards.
p1_scoreboard.create(p1_scoreboard_position, p1, P1_SCORE)
p2_scoreboard.create(p2_scoreboard_position, p2, P2_SCORE)

# Draw paddles on screen.
p1.spawn((-700, 0))    # Where (x, y) is position for centre of paddle.
p2.spawn((700, 0))     # Where (x, y) is position for centre of paddle.

# Instantiate game ball.
ball = Ball()

# Update screen.
screen.update()

# Set game starting player as p1.
starting_player = p1

# Set score with which to win game.
SCORE_TO_WIN = 10

# Set rally length at which to speed up the ball.
SPEED_UP = 2

# Start listening for key presses.
screen.listen()
screen.onkeypress(p1.move_up, "q")  # 'q' key moves p1 paddle up.
screen.onkeypress(p1.move_down, "a")    # 'a' key moves p1 paddle up.
screen.onkeypress(p2.move_up, "p")  # 'p' key moves p1 paddle up.
screen.onkeypress(p2.move_down, "l")    # 'l' key moves p1 paddle up.

# Start game over loop.
GAME_OVER = False
while not GAME_OVER:

    # Start rally length counter.
    RALLY_LENGTH = 0

    # Check if either player's score is enough to win the game.
    if P1_SCORE == SCORE_TO_WIN:
        GAME_OVER = True
        break
    elif P2_SCORE == SCORE_TO_WIN:
        GAME_OVER = True
        break

    # Check which player is starting or has scored previous goal and set a random ball heading in opposite direction.
    if starting_player == p1:
        ball_heading = randint(0, 45)
    else:
        ball_heading = randint(135, 180)

    # Kick off ball.
    ball.kick_off(ball_heading)

    # Set starting match delay.
    TIME_DELAY = 0.05

    # Start goal loop.
    GOAL = False
    while not GOAL:

        # Edit game time.
        sleep(TIME_DELAY)
        screen.update()

        # Start ball moving.
        ball.move()

        # Detect wall collisions and bounce ball.  Walls set to -380 and 380 on the y-axis.
        if ball.ycor() >= 380 or ball.ycor() <= -380:
            ball.setheading(360 - ball.heading())

        # Detect paddle 1 collision by comparing xcor and ycor of ball and paddle.  Bounce ball if True.
        if p1.xcor() + 40 > ball.xcor() and abs(ball.ycor() - p1.ycor()) < 100:
            paddle_hit.play()
            ball.setheading(180 - ball.heading())
            RALLY_LENGTH += 1
            # Check if rally length speed up value reached.  Increase ball speed if True.
            if RALLY_LENGTH % SPEED_UP == 0:
                TIME_DELAY *= 0.75

        # Detect paddle 2 collision by comparing xcor and ycor of ball and paddle.  Bounce ball if True.
        if p2.xcor() - 40 < ball.xcor() and abs(ball.ycor() - p2.ycor()) < 100:
            paddle_hit.play()
            ball.setheading(180 - ball.heading())
            RALLY_LENGTH += 1
            # Check if rally length speed up value reached.  Increase ball speed if True.
            if RALLY_LENGTH % SPEED_UP == 0:
                TIME_DELAY *= 0.75

        # Detect if p1 has scored a goal by checking if ball x-coordinate is greater than 780.
        if ball.xcor() > 700:
            P1_SCORE += 1
            p1_scoreboard.clear()
            p1_scoreboard.create(p1_scoreboard_position, p1, P1_SCORE)
            starting_player = p1
            GOAL = True

        # Detect if p2 has scored a goal by checking if ball x-coordinate is less than -780.
        if ball.xcor() < -700:
            P2_SCORE += 1
            p2_scoreboard.clear()
            p2_scoreboard.create(p2_scoreboard_position, p2, P2_SCORE)
            starting_player = p2
            GOAL = True

# Clear net and scoreboards from screen.
net.clear()
p1_scoreboard.clear()
p2_scoreboard.clear()
# Write game over scoreboard.
scoreboard.game_over(game_over_scoreboard_position, p1, P1_SCORE, p2, P2_SCORE)
screen.exitonclick()
