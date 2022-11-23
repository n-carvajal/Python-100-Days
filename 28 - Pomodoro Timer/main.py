"""
Pomodoro Timer App
"""

# Imports
import math
import tkinter as tk

# Constants and Variables
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
rounds = 0
tick_column = 0
timer = ""


def set_countdown():
    """
    Function that sets the countdown timer.

    Takes in 'rounds' and 'tick_column' values from global scope.
    Adds 1 to 'rounds'.
    Sets the 'btn_start' state to 'DISABLED' thereby not allowing multiple instances of the timer.
    Gets input from 'ent_work', 'ent_short', and 'ent_long' as an integer and converts into seconds by multiplying each
    by 60.
    Names corresponding result 'work_sec', 'short_break_sec' and 'long_break_sec'.
    Converts the values for 'WORK_MIN', 'SHORT BREAK MIN', and 'LONG BREAK MIN' into seconds by multiplying them by 60
    and names them 'work_sec', 'short_break_sec' and 'long_break_sec'.
    Checks the value of 'rounds'.
    If 'rounds' can be evenly divided by the input in 'ent_rounds' as an integer multiplied by 2. Then calls function
    'timer_countdown()' and passes 'long_break_sec' as its argument then sets 'lbl_title' to 'Break' in 'RED'.
    Else if 'rounds' is even then calls function 'timer_countdown()' and passes 'short_break_sec' as its argument and
    sets 'lbl_title' to 'Break' in 'PINK'.
    Else calls function 'timer_countdown()' and passes 'work_sec' as its argument, sets 'lbl_title' to 'Work' in
    'GREEN', then creates a Label object called 'lbl_work_tick' within 'frm_ticks' and places it with '.grid()' using
    'tick_column' as the corresponding grid column value.
    Adds 1 to 'tick_column'.
    """
    global rounds
    global tick_column
    rounds += 1
    btn_start.config(state=tk.DISABLED)
    work_sec = int(ent_work.get()) * 60
    short_break_sec = int(ent_short.get()) * 60
    long_break_sec = int(ent_long.get()) * 60
    if rounds % (int(ent_rounds.get()) * 2) == 0:
        start_countdown(long_break_sec)
        lbl_title.config(text="Break", fg=RED)
    elif rounds % 2 == 0:
        start_countdown(short_break_sec)
        lbl_title.config(text="Break", fg=PINK)
    else:
        start_countdown(work_sec)
        lbl_title.config(text="Work", fg=GREEN)
        lbl_work_tick = tk.Label(frm_ticks, text="✓", fg=GREEN, font=(FONT_NAME, 15), bg=YELLOW)
        lbl_work_tick.grid(row=0, column=tick_column)
        tick_column += 1


def start_countdown(count):
    """
    Function that starts the countdown timer and takes as its 'count' argument the 'work_sec', 'short_break_sec', or
    'long_break_sec' values from 'set_countdown()'.

    Takes in 'timer' from global scope.
    Creates variable called 'count_min' that calculates the number of whole minutes in 'count'.  It does so by dividing
    'count' by 60 seconds and then rounding the result down to the nearest whole number.
    Creates variable called 'count_sec' that calculates the remaining seconds in 'count' once the minutes have been
    calculated.  It does so by using modulo (%) 60 on 'count'.
    Checks 'count_min'.
    If 'count_min' is less than 10, then it formats 'count_min' to have a leading '0'.
    Checks 'count_sec'.
    If 'count_sec' is less than 10, then it formats 'count_sec' to have a leading '0'.
    Checks 'count'.
    If 'count' is greater than 0, creates 'timer' using '.after()' that every 1000 milliseconds triggers the
    'start_countdown()' function using the value of 'count' minus 1 as its argument. Additionally, it configures the
    'text_timer' in 'canvas' to display the 'count_min:count_sec' formatted as required.
    Else triggers the 'set_countdown()' function and brings 'root' window to front.
    """
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count > -1:
        timer = root.after(1000, start_countdown, count - 1)
        canvas.itemconfig(text_timer, text=f"{count_min}:{count_sec}")
    else:
        set_countdown()
        bring_to_front()


def reset_countdown():
    """
    Function that resets the countdown timer.

    Takes in 'rounds', 'tick_column' and 'timer' from global scope.
    Sets 'rounds' and 'tick_column' to 0.
    Sets 'btn_start' state to 'NORMAL' thereby allowing a timer restart.
    Cancels 'timer' using '.after_cancel()'.
    Configures 'lbl_title' to display 'Timer' in 'GREEN'.
    Configures 'text_timer' in 'canvas' to display '00:00'.
    Loops through all the children widgets in 'frm_ticks' and destroys them using '.destroy()'.
    """
    global rounds
    global tick_column
    global timer
    rounds = 0
    tick_column = 0
    btn_start.config(state=tk.NORMAL)
    root.after_cancel(timer)
    lbl_title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(text_timer, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    for widget in frm_ticks.winfo_children():
        widget.destroy()


def bring_to_front():
    """
    Function that brings the 'root' window to the front of all windows.

    It sets 'root' state to 'normal' therefore expanding if the window is minimised.
    It then configures the root attribute '-topmost' as True to make 'root' a top level window.
    It then sets the 'root' attribute '-topmost' as False to allow for other windows to be top level again.
    """
    root.state("normal")
    # Bring to top level above all windows
    root.attributes("-topmost", True)
    # Allows other windows to top level again
    root.attributes("-topmost", False)


# Create 'root' window.
root = tk.Tk()
# Set 'root' title.
root.title("Pomodoro Timer")
# Configure 'root' size and background.
root.config(padx=100, pady=50, bg=YELLOW)

# Create a 'Timer' title called 'lbl_title' in 'root'.
lbl_title = tk.Label(root, text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
# Place 'lbl_title' in 'root' with '.grid()'.
lbl_title.grid(row=0, column=1)

# Create a Canvas object called 'canvas' in 'root' and set its attributes.
canvas = tk.Canvas(root, width=200, height=224, bg=YELLOW, highlightthickness=0)
# Convert 'tomato.png' to a tkinter image called 'tomato_image'.
tomato_image = tk.PhotoImage(file="28 - Pomodoro Timer/tomato.png")
# Place image on canvas.
canvas.create_image(100, 112, image=tomato_image)
# Create '00:00' text on canvas and name 'text_timer'.
text_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# Place 'canvas' in 'root' with '.grid()'.
canvas.grid(row=1, column=1, pady=15)

# Create Label object called lbl_work:
lbl_work = tk.Label(root, text="Work Time\nMinutes", font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
# Place 'lbl_work' with '.grid()'.
lbl_work.grid(row=2, column=0)
# Create Entry object called 'ent_work'.
ent_work = tk.Entry(root, width=10)
# Place 'ent_work' with '.grid()'.
ent_work.grid(row=3, column=0, pady=15)

# Create Label object called lbl_rounds:
lbl_rounds = tk.Label(root, text="Long Break\nInterval", font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=PINK)
# Place 'lbl_rounds' with '.grid()'.
lbl_rounds.grid(row=2, column=2)
# Create Entry object called 'ent_rounds'.
ent_rounds = tk.Entry(root, width=10)
# Place 'ent_rounds' with '.grid()'.
ent_rounds.grid(row=3, column=2, pady=15)


# Create Label object called lbl_short:
lbl_short = tk.Label(root, text="Short Break\nMinutes", font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
# Place 'lbl_short' with '.grid()'.
lbl_short.grid(row=4, column=0)
# Create Entry object called 'ent_short'.
ent_short = tk.Entry(root, width=10)
# Place 'ent_short' with '.grid()'.
ent_short.grid(row=5, column=0, pady=15)

# Create Label object called lbl_long:
lbl_long = tk.Label(root, text="Long Break\nMinutes", font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
# Place 'lbl_long' with '.grid()'.
lbl_long.grid(row=4, column=2)
# Create Entry object called 'ent_long'.
ent_long = tk.Entry(root, width=10)
# Place 'ent_long' with '.grid()'.
ent_long.grid(row=5, column=2, pady=15)

# Create Button object called 'btn_start' in 'root'.
btn_start = tk.Button(root, text='Start', font=(FONT_NAME, 15), command=set_countdown)
# Place 'btn_start' in 'root' with '.grid()'
btn_start.grid(row=6, column=0)

# Create Frame object called 'frm_ticks' in 'root'.
frm_ticks = tk.Frame(root, bg=YELLOW)
# Place 'frm_ticks' in 'root' with '.grid()'.
frm_ticks.grid(row=7, columnspan=3)

# Create Label object called lbl_ticks in 'frm_ticks'.
lbl_ticks = tk.Label(frm_ticks, text="Work Rounds", font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
# Place lbl_ticks in frm_ticks with .grid().
lbl_ticks.grid(row=1, column=0)

# Create Button object called 'btn_reset' in 'root'.
btn_reset = tk.Button(root, text='Reset', font=(FONT_NAME, 15), command=reset_countdown)
# Place 'btn_reset' in 'root.
btn_reset.grid(row=6, column=2)

# Start listening loop.
root.mainloop()
