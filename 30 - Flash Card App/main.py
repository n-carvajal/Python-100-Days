"""French Language Vocabulary Flash Card App"""

# Imports
import random
import tkinter as tk
import pandas as pd

# Read in 'DATA' from csv file. If 'data/unknown_word_pairs.csv' exists use that, else use 'data/all_word_pairs.csv'.
try:
    DATA = pd.read_csv("30 - Flash Card App/data/unknown_word_pairs.csv")
except FileNotFoundError:
    DATA = pd.read_csv("30 - Flash Card App/data/all_word_pairs.csv")

# Constants
BACKGROUND_COLOR = "#B1DDC6"
FLIP_TIMER = None
WORD_PAIRS = DATA.to_dict(orient="records")
WORD_PAIR = {}
known_word_pairs = []
DISPLAY_TIME = 5000


def next_card():
    """
    Picks a 'WORD_PAIR' at random from 'WORD_PAIRS', then displays the foreign word from the pair followed by its
    native equivalent 'DISPLAY_TIME' later. If 'WORD_PAIRS' is empty, states all words have been learnt.

    Takes the global variables 'FLIP_TIMER' and 'WORD_PAIR'. Tries to take random choice from 'WORD_PAIRS' and assign
    result to 'WORD_PAIR'. If an 'IndexError' is encountered, it configures 'card_language_lbl' and 'card_word_lbl' to
    display 'Finished' and 'No More Words To Learn' respectively as well as sets the value of 'FLIP_TIMER' to
    'None'. If no error is encountered, it calls 'foreign_word()' and checks 'FLIP_TIMER'. If 'FLIP_TIMER' is not 'None'
    it sets 'FLIP_TIMER' to 'None' then sets 'FLIP_TIMER' to call 'native_word()' after 'DISPLAY_TIME'.
    """
    def foreign_word():
        """
        Displays the foreign word on the front of the card.

        Extracts the value with key 'French' from 'WORD_PAIR' and saves it as 'fgn_word'. It then configures
        'card_language_lbl', 'card_word_lbl', and 'card_image' to display 'French', 'fgn_word', and 'card_front'
        respectively. Additionally, it sets the 'fill' in 'card_language_lbl', 'card_word_lbl', and 'card_image' to
        'black'.
        """
        fgn_word = WORD_PAIR["French"]
        card_cnv.itemconfig(card_language_lbl, text="French", fill="black")
        card_cnv.itemconfig(card_word_lbl, text=fgn_word, fill="black")
        card_cnv.itemconfig(card_image, image=card_front)

    def native_word():
        """
        Displays the equivalent native word on the back of the card.

        Extracts the value with key 'English' from 'WORD_PAIR' and saves it as 'ntv_word'. It then configures
        'card_language_lbl', 'card_word_lbl', and 'card_image' to display 'English', 'ntv_word', and 'card_back'
        respectively. Additionally, it sets the 'fill' in 'card_language_lbl', 'card_word_lbl', and 'card_image' to
        'white'.
        """
        ntv_word = WORD_PAIR["English"]
        card_cnv.itemconfig(card_language_lbl, text="English", fill="white")
        card_cnv.itemconfig(card_word_lbl, text=ntv_word, fill="white")
        card_cnv.itemconfig(card_image, image=card_back)

    global FLIP_TIMER, WORD_PAIR
    try:
        WORD_PAIR = random.choice(WORD_PAIRS)
    except IndexError:
        card_cnv.itemconfig(card_language_lbl, text="Finished", fill="black")
        card_cnv.itemconfig(card_word_lbl, text="No More Words To Learn", fill="black", font=('arial', 30, 'normal'))
        card_cnv.itemconfig(card_image, image=card_front)
        card_cnv.after_cancel(FLIP_TIMER)
    else:
        foreign_word()
        if FLIP_TIMER:
            card_cnv.after_cancel(FLIP_TIMER)
        FLIP_TIMER = card_cnv.after(DISPLAY_TIME, native_word)


def remove_card():
    """
    Removes 'WORD_PAIR' from 'WORD_PAIRS' and writes revised 'WORD_PAIRS' to 'data/unknown_word_pairs.csv'. In addition,
    it writes the removed 'WORD_PAIR' to 'data/known_word_pairs.csv'.

    Takes the global variables 'FLIP_TIMER' and 'WORD_PAIR'. Tries to remove 'WORD_PAIR' from 'WORD_PAIRS'. If a
    'ValueError' is encountered, it configures 'card_language_lbl', 'card_word_lbl', and 'card_image' to display
    'Finished', 'No More Words To Learn', and 'card_front' respectively as well as cancelling the 'FLIP_TIMER'.  If no
    'ValueError' is encountered it converts 'WORD_PAIRS' into 'unknown_word_pairs' dataframe and writes it to
    'data/unknown_word_pairs.csv'. It also appends 'WORD_PAIR' to 'known_word_pairs' list and converts it to dataframe
    'learnt_words' which is then written to 'data/known_word_pairs.csv'. It then calls 'next_card()'.
    """
    try:
        WORD_PAIRS.remove(WORD_PAIR)
    except ValueError:
        card_cnv.itemconfig(card_language_lbl, text="Finished", fill="black")
        card_cnv.itemconfig(card_word_lbl, text="No More Words To Learn", fill="black", font=('arial', 30, 'normal'))
        card_cnv.itemconfig(card_image, image=card_front)
        card_cnv.after_cancel(FLIP_TIMER)
    else:
        unknown_word_pairs = pd.DataFrame.from_dict(WORD_PAIRS)
        unknown_word_pairs.to_csv("30 - Flash Card App/data/unknown_word_pairs.csv", index=False)
        known_word_pairs.append(WORD_PAIR)
        learnt_words = pd.DataFrame.from_dict(known_word_pairs)
        learnt_words.to_csv("30 - Flash Card App/data/known_word_pairs.csv", index=False)
        next_card()


# Main GUI

# Root Window
root = tk.Tk()
root.title("french Vocabulary Flash Cards")
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Card and Button Frames in Root
card_frm = tk.Frame(root, bg=BACKGROUND_COLOR)
button_frm = tk.Frame(root, bg=BACKGROUND_COLOR)
card_frm.pack()
button_frm.pack()

# Canvas in Card Frame.
card_cnv = tk.Canvas(card_frm, width=800, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tk.PhotoImage(file="30 - Flash Card App/images/card_front.png")
card_back = tk.PhotoImage(file="30 - Flash Card App/images/card_back.png")
card_image = card_cnv.create_image(0, 0, image=card_front, anchor='nw')
card_language_lbl = card_cnv.create_text(400, 175, text="", anchor='center', font=('arial', 40, 'normal'))
card_word_lbl = card_cnv.create_text(400, 300, text="", anchor='center', font=('arial', 60, 'bold'))
card_cnv.pack()

# Start Card Display
next_card()

# Buttons in Button Frame.
correct_image = tk.PhotoImage(file="30 - Flash Card App/images/correct.png")
incorrect_image = tk.PhotoImage(file="30 - Flash Card App/images/incorrect.png")
answer_correct_btn = tk.Button(button_frm, image=correct_image, borderwidth=0, highlightthickness=0,
                               activebackground=BACKGROUND_COLOR, command=remove_card)
answer_incorrect_btn = tk.Button(button_frm, image=incorrect_image, borderwidth=0, highlightthickness=0,
                                 activebackground=BACKGROUND_COLOR, command=next_card)
answer_correct_btn.grid(row=0, column=0, padx=25)
answer_incorrect_btn.grid(row=0, column=1, padx=25)

root.mainloop()
