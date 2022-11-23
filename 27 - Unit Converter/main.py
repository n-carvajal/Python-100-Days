"""
Unit converter application using the tkinter built-in module
"""

import tkinter as tk


def check_selection():
    """
    Loops with 'num' through values 1 to 5.
    Obtains value from 'radio_button_selection' with '.get()'.
    Checks if the obtained value is equal to 'num'.
    If yes it configures the text attribute of 'label_user_prompt' with the value at
    'units_imperial' indexed at [num].
    If not repeats the loop.
    """
    for number in range(1, 5):
        if radio_button_selection.get() == number:
            label_user_prompt.config(text=f"Enter {units_imperial[number - 1]}:")


def convert_entry():
    """
    Gets the value of the text attribute from 'label_user_prompt' and names it 'choice'.
    Checks the slice 'choice[6:-1]' against the values in 'units_imperial' list.
    Depending on result applies appropriate conversion formula to obtain a value in
    the corresponding unit of measure.
    It does so by obtaining the value in 'entry_user_input' with '.get()'.
    Converting the text string to a flat with `float()`.
    Applying the appropriate formula depending on the resulting unit desired.
    Rounds result to two decimal palaces.
    Configures the text attribute of 'label_conversion_output' with result value and metric
    unit from 'units_metric'.
    """
    choice = label_user_prompt.cget("text")
    if choice[6:-1] == units_imperial[0]:
        label_conversion_output.config(
            text=f"{round(float(entry_user_input.get()) * 1.6, 2)} {units_metric[0]}",
            font=("arial", 14, "bold")
        )
    elif choice[6:-1] == units_imperial[1]:
        label_conversion_output.config(
            text=f"{round(float(entry_user_input.get()) * 0.3048, 2)} {units_metric[1]}",
            font=("arial", 14, "bold")
        )
    elif choice[6:-1] == units_imperial[2]:
        label_conversion_output.config(
            text=f"{round(float(entry_user_input.get()) * 0.453592, 2)} {units_metric[2]}",
            font=("arial", 14, "bold")
        )
    elif choice[6:-1] == units_imperial[3]:
        label_conversion_output.config(
            text=f"{round((float(entry_user_input.get()) - 32) * 5 / 9, 2)} {units_metric[3]}",
            font=("arial", 14, "bold")
        )


# List of imperial units to convert from.
units_imperial = ["Miles", "Feet", "Pounds", "Fahrenheit"]

# List of metric units to convert to.
units_metric = ["Kilometres", "Metres", "Kilograms", "Celsius"]

# Instantiate tkinter root window.
root = tk.Tk()
root.title("Unit Converter")
root.geometry("250x300")

# Frames List
frames = []

# Instantiate 6 'Frame' objects and append to 'Frames' list.
for num in range(6):
    frame = tk.Frame(root, pady=5)
    frame.pack()
    frames.append(frame)

# Instantiate and pack 'label_choice_prompt'.
label_choice_prompt = tk.Label(frames[0], text="Choose Conversion")
label_choice_prompt.pack(fill=tk.X)

# Instantiate 'radio_button_selection' variable.
radio_button_selection = tk.IntVar()

# Instantiate and pack 4 'radio_button' objects.
RADIO_BUTTON_VALUE = 1
for i in range(4):
    radio_button = tk.Radiobutton(
        master=frames[1],
        text=f"{units_imperial[i]} to {units_metric[i]}",
        variable=radio_button_selection,
        value=RADIO_BUTTON_VALUE,
        command=check_selection)
    RADIO_BUTTON_VALUE += 1
    radio_button.pack(anchor="w")

# Instantiate and pack 'label_user_prompt' object.
label_user_prompt = tk.Label(frames[2], text="-----")
label_user_prompt.pack()

# Instantiate and pack 'entry_user_input' object.
entry_user_input = tk.Entry(frames[3])
entry_user_input.pack()

# Instantiate and pack 'button_covert' object.
button_convert = tk.Button(frames[4], text="Convert", command=convert_entry)
button_convert.pack()

# Instantiate and pack 'label_conversion_output' object.
label_conversion_output = tk.Label(frames[5], text="Your Result")
label_conversion_output.pack()

root.mainloop()
