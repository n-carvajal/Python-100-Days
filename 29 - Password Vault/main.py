"""
Simple local password vault that saves provided website and user data into a 'logins.txt' file.
"""

# Imports
import random
import tkinter as tk
from tkinter import messagebox

from data import letters, numbers, symbols

# Variables
BG_COLOUR = "White"
FNT_NAME = "Arial"
FNT_STYLE = "bold"


# Functions
def submit_details():
    """
    Function that writes the inputs from the website, url, username, and password entry boxes to the file 'logins.txt'.

    Retrieves the text in the website name, address, username, and password entry boxes with the '.get()' method.
    Checks to see if any of the retrieved values equals an empty string "".
    If yes then displays a message box informing the user that no field may be left blank.
    Else generates a message box confirming if all details entered are correct.
    Then it opens the logins.txt file and appends 'name', 'address', 'username' and 'password' in that order each on a
    new line.
    It then deletes any existing input across all the input fields and the 'txt_output' field.
    After which it sets the focus on the 'ent_name' entry box.
    Finally, it generates a message box confirming that the details have been successfully saved.
    """
    name = ent_name.get()
    address = ent_url.get()
    username = ent_username.get()
    password = ent_password.get()
    if name == "" or address == "" or username == "" or password == "":
        messagebox.showerror("Error", "No Blank Fields Allowed")
    else:
        messagebox.showinfo("Confirm", "Are ALL Details Correct")
        with open("29 - Password Vault/logins.txt", "a") as vault:
            vault.write(f"{name}\n{address}\n{username}\n{password}\n")
        ent_name.delete(0, tk.END)
        ent_url.delete(0, tk.END)
        ent_username.delete(0, tk.END)
        ent_password.delete(0, tk.END)
        ent_name.focus()
        ent_username_retrieve.delete(0, tk.END)
        messagebox.showinfo("Success", "Details Saved Successfully")


def password_generate():
    """
    Function that automatically generates a 10 letter complex password and places the result in the password entry box.

    First it deletes any input that might be present in the password entry box.
    Then it creates an empty list called 'password_list'.
    It then picks a 'letter' at random from the 'letters' list in 'data.py'.
    It checks if the chosen 'letter' is present in 'password_list'.
    If it is not, it appends the chosen 'letter' to 'password_list'.
    If the 'letter' is already present in 'password_list' it picks another at random from 'letters' and tries again.
    This process is repeated until 6 random unique letters have been added to the 'password_list'.
    It then proceeds to perform the exact same procedure for 'symbol' and 'number' using 'symbols' and 'numbers' from
    'data.py' respectively until 2 unique and random 'symbol' and 2 unique and random 'number' values have been added to
    the 'password_list'.
    It then takes the 'password_list' containing 10 unique values (5 letters, 2 symbols, 2 numbers) and shuffles it.
    It then joins the shuffled list into a string called 'password'.
    Once done it inserts the 'password' string into the password entry box.
    Finally, it clears the clipboard of any previous data and then appends 'password' to it.
    """
    ent_password.delete(0, tk.END)
    password_list = []
    for _ in range(6):
        letter = random.choice(letters)
        while letter in password_list:
            letter = random.choice(letters)
        password_list.append(letter)
    for _ in range(2):
        symbol = random.choice(symbols)
        number = random.choice(numbers)
        while symbol in password_list:
            symbol = random.choice(symbols)
        while number in password_list:
            number = random.choice(numbers)
        password_list.append(symbol)
        password_list.append(number)
    random.shuffle(password_list)
    password = "".join(password_list)
    ent_password.insert(0, password)
    root.clipboard_clear()
    root.clipboard_append(password)


def retrieve_details():
    """
    Searches through logins.txt file for matching website name and username and displays the corresponding login details
    in the black output box.

    Retrieves inputted text in 'ent_name_retrieve' and 'ent_username_retrieve'.
    Deletes the text in 'ent_name_retrieve', 'ent_username_retrieve' and 'txt_output' if any.
    Creates two empty lists 'vault_list' and 'found_item'.
    It then opens 'logins.txt' as 'vault'.
    Loops through vault_lines in 'vault' and appends 'vault_line' to 'vault_list' stripping the new line ('\n') symbol.
    Creates a variable called 'index' and sets its value to 0.
    Loops through 'vault_list' checking if 'vault_list[index]' and 'vault_list[index + 2]' equal 'name' and
    'username' respectively.
    If true, it appends 'vault_list[index]' plus the following 3 values '[index + 1]', '[.. + 2]', '[.. + 3]' to
    'found_item'.
    Else it increases the index by 1.
    Does this until list completed.
    Then it checks the contents of found_item.
    If 'found_item' is not empty then a matching 'name' and 'username' have been found and the resulting details are
    inserted into the 'txt_output'.
    Else if empty it determines the 'name' and 'username' where not found at index relationship [index] and [index + 2]
    therefore no entry matches the search criteria and a messagebox is provided with the appropriate feedback.
    """
    name = ent_name_retrieve.get()
    username = ent_username_retrieve.get()
    ent_name_retrieve.delete(0, tk.END)
    ent_username_retrieve.delete(0, tk.END)
    txt_output.delete("1.0", tk.END)
    vault_list = []
    found_item = []
    with open("29 - Password Vault/logins.txt") as vault:
        for vault_lines in vault:
            vault_list.append(vault_lines.rstrip("\n"))
    index = 0
    for _ in vault_list:
        if vault_list[index] == name and vault_list[index + 2] == username:
            for i in range(4):
                found_item.append(vault_list[index + i])
        else:
            index += 1
    if found_item:
        txt_output.insert(
            "1.0",
            f"Website: {found_item[0]}\nURL: {found_item[1]}\nUsername: {found_item[2]}\n" f"Password: {found_item[3]}",
        )
    else:
        messagebox.showerror("Not Found", "Wrong Combination of Name and Username.")


# Create window 'root'.
root = tk.Tk()
root.title("Password Vault")
root.geometry("600x750")
root.config(bg=BG_COLOUR)

# Create Frame 'frm_logo'.
frm_logo = tk.Frame(root)
frm_logo.pack(fill=tk.X)

# Create Frame 'frm_sinfo'.
frm_sinfo = tk.Frame(root, bg=BG_COLOUR)
frm_sinfo.pack()

# Create Frame 'frm_submit'.
frm_submit = tk.Frame(root, bg=BG_COLOUR)
frm_submit.pack()

# Create Frame 'frm_rinfo'.
frm_rinfo = tk.Frame(root, bg=BG_COLOUR)
frm_rinfo.pack()

# Create Frame 'frm_retrieve'.
frm_retrieve = tk.Frame(root, bg=BG_COLOUR)
frm_retrieve.pack()

# Create Frame 'frm_output'.
frm_output = tk.Frame(root, bg=BG_COLOUR)
frm_output.pack()

# Create Canvas 'canvas' in 'frm_logo'.
canvas = tk.Canvas(frm_logo, highlightthickness=0, bg=BG_COLOUR)
img_logo = tk.PhotoImage(file="29 - Password Vault/logo.png")
canvas.create_image(300, 150, image=img_logo)
canvas.pack(fill=tk.X)

# Create 'frm_save' Label object 'lbl_save'.
lbl_save = tk.Label(frm_sinfo, text="Details To Save", font=(FNT_NAME, 15, FNT_STYLE), bg=BG_COLOUR)
lbl_save.grid(row=0, column=0, columnspan=2, pady=10, sticky="nesw")

# Create 'frm_sinfo' Label object 'lbl_name'.
lbl_name = tk.Label(frm_sinfo, text="Website Name:", font=(FNT_NAME, 13, FNT_STYLE), bg=BG_COLOUR)
lbl_name.grid(row=1, column=0, sticky="e", pady=5)

# Create 'frm_info' Label object 'lbl_url'.
lbl_url = tk.Label(frm_sinfo, text="Website Address:", font=(FNT_NAME, 13, FNT_STYLE), bg=BG_COLOUR)
lbl_url.grid(row=2, column=0, sticky="e", pady=5)

# Create 'frm_info' Label object 'lbl_username'.
lbl_username = tk.Label(frm_sinfo, text="User Name:", font=(FNT_NAME, 13, FNT_STYLE), bg=BG_COLOUR)
lbl_username.grid(row=3, column=0, sticky="e", pady=5)

# Create 'frm_info' Label object 'lbl_password'.
lbl_password = tk.Label(frm_sinfo, text="Password:", font=(FNT_NAME, 13, FNT_STYLE), bg=BG_COLOUR)
lbl_password.grid(row=4, column=0, sticky="e", pady=5)

# Create 'frm_info' Entry object 'ent_name'.
ent_name = tk.Entry(frm_sinfo, width=30, borderwidth=1.5, font=(FNT_NAME, 12, FNT_STYLE))
ent_name.focus()
ent_name.grid(row=1, column=1, columnspan=2, pady=5)

# Create 'frm_info' Entry object 'ent_url'.
ent_url = tk.Entry(frm_sinfo, width=30, borderwidth=1.5, font=(FNT_NAME, 12, FNT_STYLE))
ent_url.grid(row=2, column=1, columnspan=2, pady=5)

# Create 'frm_info' Entry object 'ent_username'.
ent_username = tk.Entry(frm_sinfo, width=30, borderwidth=1.5, font=(FNT_NAME, 12, FNT_STYLE))
ent_username.grid(row=3, column=1, columnspan=2, pady=5)

# Create 'frm_info' Entry object 'ent_password'.
ent_password = tk.Entry(frm_sinfo, width=18, borderwidth=1.5, font=(FNT_NAME, 12, FNT_STYLE))
ent_password.grid(row=4, column=1, sticky="w", pady=5)

# Create 'frm_info' Button object 'btn_generate_pwd'.
btn_generate_pwd = tk.Button(frm_sinfo, text="Auto Generate", font=(FNT_NAME, 9, FNT_STYLE), command=password_generate)
btn_generate_pwd.grid(row=4, column=2, sticky="nesw", pady=5)

# Create 'frm_submit' Button object 'btn_submit'.
btn_submit = tk.Button(
    frm_submit, text="Submit Details", font=(FNT_NAME, 10, FNT_STYLE), bg="Black", fg="White", command=submit_details
)
btn_submit.pack()

# Create 'frm_retrieve' Label object 'lbl_retrieve_logo'.
lbl_retrieve_logo = tk.Label(frm_rinfo, text="Details To Retrieve", font=(FNT_NAME, 15, FNT_STYLE), bg=BG_COLOUR)
lbl_retrieve_logo.grid(row=0, column=0, columnspan=2, pady=10, sticky="nesw")

# Create 'frm_retrieve' Label object 'lbl_name_retrieve'.
lbl_name_retrieve = tk.Label(frm_rinfo, text="Website To Retrieve:", font=(FNT_NAME, 13, FNT_STYLE), bg=BG_COLOUR)
lbl_name_retrieve.grid(row=1, column=0, sticky="e", pady=5)

# Create 'frm_retrieve' Label object 'lbl_username_retrieve'.
lbl_username_retrieve = tk.Label(frm_rinfo, text="Username To Retrieve:", font=(FNT_NAME, 13, FNT_STYLE), bg=BG_COLOUR)
lbl_username_retrieve.grid(row=2, column=0, sticky="e", pady=5)

# Create 'frm_retrieve' Entry object 'ent_name_retrieve'.
ent_name_retrieve = tk.Entry(frm_rinfo, width=30, borderwidth=1.5, font=(FNT_NAME, 12, FNT_STYLE))
ent_name_retrieve.grid(row=1, column=1, pady=5)

# Create 'frm_retrieve' Entry object 'ent_username_retrieve'.
ent_username_retrieve = tk.Entry(frm_rinfo, width=30, borderwidth=1.5, font=(FNT_NAME, 12, FNT_STYLE))
ent_username_retrieve.grid(row=2, column=1, pady=5)

# Create 'frm_retrieve' Button object 'btn_retrieve'.
btn_retrieve = tk.Button(
    frm_retrieve,
    text="Retrieve Details",
    font=(FNT_NAME, 10, FNT_STYLE),
    bg="Black",
    fg="White",
    command=retrieve_details,
)
btn_retrieve.pack()

# Create 'frm_output' Textbox object 'txt_output'.
txt_output = tk.Text(
    frm_output, height=4, width=30, borderwidth=1, bg="Black", fg="White", font=(FNT_NAME, 12, FNT_STYLE)
)
txt_output.pack(pady=5)

# Create 'mainloop' for 'root'.
root.mainloop()
