"""Simple Password Generator App"""

# Imports
from random import randint, shuffle
from data import letters, symbols, numbers

print("Welcome to the PyPassword Generator.")
# Prompt user for number of letters, symbols, and numbers:
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))
# Create strings to store chosen letters, symbols, and numbers:
CHOSEN_LETTERS = ""
CHOSEN_SYMBOLS = ""
CHOSEN_NUMBERS = ""
# Iterate through letters list as many times as nr_letters.
# Generate a random index each time and add letters[index] to chosen_letters:
for letter in range(nr_letters):
    index = randint(0, len(letters) - 1)
    CHOSEN_LETTERS += letters[index]
# Iterate through symbols list as many times as nr_symbols.
# Generate a random index each time and add symbols[index] to chosen_symbols:
for symbol in range(nr_symbols):
    index = randint(0, len(symbols) - 1)
    CHOSEN_SYMBOLS += symbols[index]
# Iterate through numbers list as many times as nr_numbers.
# Generate a random index each time and add numbers[index] to chosen_numbers:
for number in range(nr_numbers):
    index = randint(0, len(numbers) - 1)
    CHOSEN_NUMBERS += numbers[index]
# Return a concatenation of chosen_letters, chosen_symbols, chosen_strings:
simple_password = CHOSEN_LETTERS + CHOSEN_SYMBOLS + CHOSEN_NUMBERS
print(f"Your simple secure password is: {simple_password}")
# Cast simple password to a list, shuffle the list, and rejoin to create a complex password:
password_list = list(simple_password)
shuffle(password_list)
COMPLEX_PASSWORD = "".join(password_list)
print(f"Your more secure shuffled password is: {COMPLEX_PASSWORD}")
