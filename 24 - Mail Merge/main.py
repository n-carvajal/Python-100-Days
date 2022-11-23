"""Mail Merge Application"""


with open("24 - Mail Merge/Input/Names/invited_names.txt") as name_file:
    for name in name_file.readlines():
        stripped_name = name.strip()
        greeting = f"Dear {stripped_name},\n"
        with open("24 - Mail Merge/Input/Letters/starting_letter.txt") as text_file:
            text_list = text_file.readlines()
            text_list[0] = greeting
            with open(
                f"24 - Mail Merge/Output/ReadyToSend/letter_to_{stripped_name}.txt", mode="w"
            ) as letter_personalised:
                letter_personalised.writelines(text_list)
