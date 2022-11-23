"""Etch A Sketch Simulator"""

from turtle import Turtle, Screen


def move_forward():
    """
    Moves turtle forward by 10 when 'w' pressed.
    """
    onyx.forward(10)


def move_backwards():
    """
    Moves turtle backwards by 10 when 's' pressed.
    """
    onyx.backward(10)


def move_right():
    """
    Moves turtle clockwise by 10 when 'd' is pressed.
    """
    onyx.right(10)


def move_left():
    """
    Moves turtle clockwise by 10 when 'a' is pressed.
    """
    onyx.left(10)


def clear_screen():
    """
    Clears the screen of turtle drawing when 'c' is pressed.
    """
    onyx.clear()
    onyx.penup()
    onyx.setposition(0.0, 0.0)
    onyx.setheading(0)
    onyx.pendown()


screen = Screen()
onyx = Turtle()
onyx.shape("triangle")
onyx.pensize(5)
onyx.pencolor("black")
screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
screen.onkey(clear_screen, "c")
screen.listen()
screen.exitonclick()
