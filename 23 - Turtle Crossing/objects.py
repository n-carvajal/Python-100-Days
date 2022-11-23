"""
Module holding the Player, Car, and Scoreboard classes.
"""

# Imports
from random import choice, randrange
from turtle import Turtle

from pygame import mixer

# Initialize mixer.
mixer.init()

# Create sound object for player movement.
player_movement = mixer.Sound("23 - Turtle Crossing/player_move.wav")


class Background(Turtle):
    """
    Background class that inherits from the Turtle class.
    """
    def __init__(self):
        """
        Upon instantiation Background object has the penup() and is in the shape of a "square".
        """
        super().__init__()
        self.penup()
        self.shape("square")

    def grass(self):
        """
        Method to create the two grass verges on the screen.

        It does so by setting color() and turtlesize() attributes.
        It then sends the turtle to a y position of 350 and creates a stamp().
        Then it moves down to a y position of -350 anc creates a stamp().
        """
        self.color("forest green")
        self.turtlesize(5, 40)
        y_pos = 350
        for _ in range(2):
            self.goto(0, y_pos)
            self.stamp()
            y_pos -= 700

    def lines(self):
        """
        Method to create the 5 lane dividers on the screen to simulate a road.

        It does so by setting color() and turtlesize() attributes.
        It then sends the turtle to an x and y position of (0, 300) and creates a stamp().
        Then it moves down to a y position of that is 150 less than the previous one and creates a stamp().
        It does this 5 times in total.
        """
        self.color("white")
        self.turtlesize(0.25, 40)
        x_cor, y_cor = (0, 300)
        for _ in range(5):
            self.goto(x_cor, y_cor)
            self.stamp()
            y_cor -= 150

    def dashes(self):
        """
        Method to create the 4 central road markings on the screen.

        It does so by setting color() and turtlesize() attributes.
        It then sends the turtle to an x and y position of (360, 255).
        It creates a stamp() at the position and then moves -80 on the x-axis where it creates another stamp().
        It repeats the x-axis subtraction and stamp() 10 times.
        Once the 10 stamp() manoeuvres have been completed on the x-axis it moves down on the y-axis by 150.
        Once done it repeats the entire procedure.
        It does so for a total of 4 times.
        """
        self.color("white")
        self.turtlesize(0.25, 2)
        x_cor, y_cor = (360, 225)
        for _ in range(4):
            self.goto(x_cor, y_cor)
            y_cor -= 150
            for _ in range(10):
                self.stamp()
                self.forward(-80)
        self.hideturtle()


class Player(Turtle):
    """
    Player class that inherits from the Turtle class.
    """
    def __init__(self):
        """
        Upon instantiation the Player object is given penup(), shape(), color(), setheading() and goto() attributes.
        """
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("black", "orange")
        self.setheading(90)
        self.goto(0, -337)

    def upwards(self):
        """
        Method that moves the Player object upwards on screen which is the game upper bounds limit.

        It first checks if the object's ycor() is < 338.
        If true it moves the object up on the y-axis by 75.
        75 is the distance interval required for the Player object to land in the center of a road lane every time.
        """
        y_pos = int(self.ycor())
        if y_pos < 338:
            x_pos, y_pos = self.position()
            self.goto(x_pos, y_pos + 75)
            player_movement.play()

    def downwards(self):
        """
        Method that moves the Player object downwards on screen.

        It first checks if the object's ycor() is < -337 which is the game lower bounds limit.
        If true it moves the object down on the y-axis by 75.
        75 is the distance interval required for the Player object to land in the center of a road lane every time.
        """
        y_pos = int(self.ycor())
        if y_pos > -337:
            x_pos, y_pos = self.position()
            self.goto(x_pos, y_pos - 75)
            player_movement.play()

    def leftwards(self):
        """
        Method that moves the Player object leftwards on screen.

        It first checks if the object's xcor() is < -380 which is the game left bounds limit.
        If true it moves the object left on the x-axis by 20.
        20 is the default width of a Turtle object from which this class inherits.
        """
        x_pos = int(self.xcor())
        if x_pos > -380:
            x_pos, y_pos = self.position()
            self.goto(x_pos - 20, y_pos)
            player_movement.play()

    def rightwards(self):
        """
        Method that moves the Player object rightwards on screen.

        It first checks if the object's xcor() is < 380 which is the game right bounds limit.
        If true it moves the object right on the x-axis by 20.
        20 is the default width of a Turtle object from which this class inherits.
        """
        x_pos = int(self.xcor())
        if x_pos < 380:
            x_pos, y_pos = self.position()
            self.goto(x_pos + 20, y_pos)
            player_movement.play()


class Car(Turtle):
    """
    Car class that inherits from the Turtle class.
    """
    def __init__(self):
        """
        Upon instantiation the Car object is assigned penup(), shape(), and setheading() attributes.
        """
        super().__init__()
        self.penup()
        self.shape("square")
        self.setheading(0)

    def spawn(self):
        """
        Method that assigns a random color to a car object and sends it to a random location on the right or left
        of the screen.

        A colour is picked from colours list with choice() and assigned to color() attribute of the car object.
        An x position of either -400 or 400 is picked with choice().
        The values of 400 and -400 correspond to the left and right edges of the screen.
        Random y values are generated with randrange() for positions on the left of the screen.
        Random y values are generated with randrange() for position on the right of the screen.
        The start, stop, and step values for left randrange() and right randrange() ensures the cars are placed in the
        centre of alternating road lanes on either side of the screen.
        If the x position chosen is -400 this is packed into a tuple with the left randrange() value.
        If the x position chosen is 400 this is packed into a tuple with the right randrange() value.
        The resulting position is used in goto() to send the object to that position.

        Returns True if the x position chosen is -400.
        Returns False if the x position chosen is 400.
        """
        colours = ["red", "orange", "yellow", "blue", "purple", "cyan", "magenta"]
        self.color(choice(colours))
        x_pos = choice([-400, 400])
        left_y_pos = randrange(-262, 338, 150)
        right_y_pos = randrange(-187, 337, 150)
        if x_pos == -400:
            self.goto(x_pos, left_y_pos)
        else:
            self.goto(x_pos, right_y_pos)
        if x_pos == -400:
            return True
        else:
            return False


class Scoreboard(Turtle):
    """
    Player class that inherits from the Turtle class.
    """
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def display(self, text, level, position, font_size):
        """Sets up scoreboard display"""
        self.goto(position)
        self.color("black")
        self.write(f"{text}: {level}", False, "center", ('Arial', font_size, 'bold'))
