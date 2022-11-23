"""
Application that breaks a word into it's corresponding letters and then spells it out in the console using the NATO
phonetic alphabet.
"""

import pandas as pd

print("NATO alphabet mapper")
nato_df = pd.read_csv("26 - Nato Alphabet Mapper/nato_phonetic_alphabet.csv")
nato = nato_df.set_index("letter")

while True:
    word = input("Enter a word and I will provide the NATO phonetic spelling: ").upper()
    try:
        nato_list = [nato.loc[letter, "code"] for letter in word]
        print(f"Your word is spelled as follows: {nato_list}")
        break
    except KeyError:
        print("The word must solely consist of letters from the alphabet.")
