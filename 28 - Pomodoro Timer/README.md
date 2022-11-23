# 100 Days of Python Code

## Project 28: Pomodoro Timer

Create a pomodoro timer using the `tkinter` module that enables you to work in a series of work/break intervals.

### Execution

To run the program execute `python main.py` from a command prompt within the project directory.

### Program Setup

The user is free to set up the timer by inputting a relevant whole number in the appropriate field.  The available fields
are:

* `Work Time Minutes`: Sets the amount of WHOLE minutes that each work interval should consist of.
* `Long Break Interval`: Sets the number of WORK and SHORT BREAK intervals that should transpire before
a long break interval takes place.
* `Short Break Interval`: Sets the amount of WHOLE minutes that each short break interval should consist of.
* `Long Break Interval`: Sets the amount of WHOLE minutes that a long break interval should consist of.

### Operation

* The timer should start when the user presses the `start` button.
* The timer should provision a short break interval after each work interval until the long break interval is reached.
* When the long break interval value is reached, the timer should then allow for a long break interval.
* This pattern should repeat indefinitely until the user stops the timer using the `reset` button.

### GUI Feedback

* When the user presses `start` the timer should begin and the start button should become inactive.
* When a work interval is active, the program should display a 'Work' title in green.
* When a short break interval is active, the program should display a 'Break' title in pink.
* When a long break interval is active, the program should display a 'Break' title in red.
* Once a work/break interval has been completed, the program should display a green checkmark above the 'Work Rounds' title.
* When the user presses `reset` the GUI should return to its original composition.
