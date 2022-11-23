"""Caesar Cypher"""

# Variables:
alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


# Function definitions:
def caesar(string, number, code_direction):
    """
    Encrypts word by mapping to alphabet and applying a shift of number to every letter
    Decrypts by mapping to alphabet and applying a negative shift of number to every letter
    """
    output_string = ""
    if code_direction == "decrypt":
        number *= -1
    for char in string:
        if char.isalpha():
            char_index = alphabet.index(char)
            char_shifted_index = char_index + number
            if char_shifted_index >= len(alphabet) or char_shifted_index < 0:
                output_string += alphabet[char_shifted_index % len(alphabet)]
            else:
                output_string += alphabet[char_shifted_index]
        else:
            output_string += char
    print(f"\nThe {direction}ed message is: {output_string}\n")


# Prompt user to encrypt or decrypt:
print("Do you have a message to encrypt/decrypt?")
ENCRYPTING = True
while ENCRYPTING:
    have_message = input("Type 'yes' or 'no': ").lower()
    if have_message == "yes":
        direction = input("\nType 'encrypt' to encrypt, or 'decrypt' to decrypt: ")
        text = input("Type your message: ").lower()
        shift = int(input("Type the shift number: "))
        caesar(string=text, number=shift, code_direction=direction)
        print("Do you want to encrypt/decrypt another message?")
    elif have_message == "no":
        ENCRYPTING = False
        print("\nOK. Goodbye.")
    else:
        print("\nThat is not a valid entry.")
