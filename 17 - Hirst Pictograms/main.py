"""Application that places multicoloured dots on a Turtle canvas"""

import random
import turtle

import colorgram


def paint_line(start, x_dots, x_dist):
    """Paints a line."""
    for _ in range(x_dots):
        random_colour = random.choice(colours)
        onyx.pencolor(random_colour.rgb)
        onyx.dot()
        onyx.forward(x_dist)
    onyx.setx(start)


def move_line(y_dist):
    """Moves a line."""
    onyx.left(90)
    onyx.forward(y_dist)
    onyx.right(90)


def paint_dots(start, x_dots, x_dist, y_dots, y_dist):
    """Paints dots."""
    for _ in range(y_dots):
        paint_line(start, x_dots, x_dist)
        move_line(y_dist)


screen = turtle.Screen()
screen.screensize(900, 900)
screen.colormode(255)
colours = colorgram.extract("17 - Hirst Painting/colour_palette.jpg", 32)
onyx = turtle.Turtle()
onyx.hideturtle()
DOTS_HORIZONTAL = 16
SPACING_HORIZONTAL = 50
DOTS_VERTICAL = 16
SPACING_VERTICAL = 50
onyx.speed(0)
onyx.penup()
onyx.pensize(20)
onyx.setposition(
    (((DOTS_HORIZONTAL - 1) * SPACING_HORIZONTAL) / 2) * -1, (((DOTS_VERTICAL - 1) * SPACING_VERTICAL) / 2) * -1
)
x_start = onyx.xcor()
y_start = onyx.ycor()
paint_dots(x_start, DOTS_HORIZONTAL, SPACING_HORIZONTAL, DOTS_VERTICAL, SPACING_VERTICAL)
onyx.setposition(x_start, y_start)

screen.exitonclick()
