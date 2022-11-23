"""Random Turtle Racing"""

from random import choice
from turtle import Screen, Turtle

# Setup Screen:
screen = Screen()
screen.setup(width=500, height=400)
# Create turtles:
turtles = []
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
# Turtle 0 starting position:
POS_X = -250
POS_Y = 150
for i in range(6):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(colours[i])
    turtle.penup()
    turtle.setposition(POS_X, POS_Y)
    POS_Y -= 60
    turtles.append(turtle)
# Prompt user for a bet:
bet = (screen.textinput(title="Random Turtle Racing", prompt="Type the colour of the turtle you think will "
                                                             "win: ")).lower()
# While loop running game:
GAME_OVER = False
while not GAME_OVER:
    jockey = choice(turtles)
    jockey.forward(10)
    if jockey.xcor() == 230:
        if bet == jockey.fillcolor():
            print(f"You bet {bet} and the {jockey.fillcolor()} turtle won!")
            print("You win.")
            GAME_OVER = True
        else:
            print(f"You bet {bet} and the {jockey.fillcolor()} turtle won!")
            print("You lose.")
            GAME_OVER = True
print("Game Over")
# Exit screen on click
screen.exitonclick()
