"""Blind Auction"""

# Imports
import os
from art import logo


def clear_screen():
    """Clears the console."""
    os.system("cls" if os.name == "nt" else "clear")


# Variables:
AUCTION = True
BIDDING = True
bids = {}
MAX_BID = 0
MAX_BIDDER = ""
# Code
print(logo)
print("Do you want to start the auction?")
while AUCTION:
    take_part = input("Type 'yes' or 'no': ").lower()
    if take_part == "yes":
        while BIDDING:
            name = input("Enter bidders name: ")
            bid = int(input("Enter bid amount: $"))
            bids[name] = bid
            print("Does anyone else want to bid?")
            another_bid = input("Type 'yes' or 'no': ").lower()
            clear_screen()
            if another_bid == "yes":
                continue
            else:
                BIDDING = False
        for bidder in bids:
            if bids[bidder] > MAX_BID:
                MAX_BIDDER = bidder
                MAX_BID = bids[bidder]
        print(f"The auction winner is {MAX_BIDDER} with a bid of ${MAX_BID}")
        print("Auction ended")
        print(logo)
        AUCTION = False
    elif take_part == "no":
        AUCTION = False
        print("OK. Goodbye.")
    else:
        print("That is not a valid input.")
        print("Try again.")
