"""Tip Calculator."""

print("Welcome to the tip calculator.")
bill = int(input("How much was the bill? "))
guests = int(input("How many of you are there? "))
tip = int(input("What percentage tip would you like to leave? (5,10,etc): "))
share = (bill * (1 + tip / 100)) / guests
print(f"Each of you must pay ${round(share, 2)}")
