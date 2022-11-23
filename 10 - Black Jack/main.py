"""Black Jack Simulator"""

# Imports
from random import choice
from cards import deck


# Functions
def deal_card():
    """
    Issues a random card to a player X.
    """
    card = choice(list(deck))
    value = deck[card]
    return card, value


def score_check(x_hand, x_score, x_ace_reductions):
    """
    Checks a hand for presence of As.
    If present and over 21 subtracts 10 from score.
    """
    if "A" in x_hand:
        for _ in range(0, x_hand.count("A")):
            if x_score > 21 and x_ace_reductions < x_hand.count("A"):
                x_score -= 10
                x_ace_reductions += 1
    return x_hand, x_score, x_ace_reductions


# Welcome
print("Welcome to 21 Black Jack\n")
# Get username:
player = input("What is your name: ")
print(f"{player}, would you like to play some 21 Black Jack?")
GAME_REPLAY = True
while GAME_REPLAY:
    replay = input("\nType 'Yes' or 'No': ").lower()
    if replay == "yes":
        print("\n" * 20)
        player_hand = []
        house_hand = []
        PLAYER_SCORE = 0
        HOUSE_SCORE = 0
        PLAYER_ACE_REDUCTIONS = 0
        HOUSE_ACE_REDUCTIONS = 0
        GAME_OVER = False
        # Issue first two cards to player 1 show both:
        for i in range(2):
            random_card, random_value = deal_card()
            player_hand.append(random_card)
            PLAYER_SCORE += random_value
        player_hand, PLAYER_SCORE, PLAYER_ACE_REDUCTIONS = score_check(player_hand, PLAYER_SCORE, PLAYER_ACE_REDUCTIONS)
        print(f"\n{player} your hand is {player_hand}")
        print(f"Your hand score is {PLAYER_SCORE}")
        # Issue first two cards to house show only first:
        for i in range(2):
            random_card, random_value = deal_card()
            house_hand.append(random_card)
            HOUSE_SCORE += random_value
        house_hand, HOUSE_SCORE, HOUSE_ACE_REDUCTIONS = score_check(house_hand, HOUSE_SCORE, HOUSE_ACE_REDUCTIONS)
        print(f"\nThe house has {house_hand[0]}")
        # print(f"\nThe house has {house_hand}") --------- Testing
        # print(f"The house hand score is {house_score}") --------- Testing
        # While loop for game over:
        GAME_OVER = False
        while not GAME_OVER:
            if len(player_hand) == 2 and PLAYER_SCORE == 21:
                print("Black Jack")
                print("You win.")
                GAME_OVER = True
            # Ask player if another card and issue if yes.
            else:
                new_card = input("\nWould you like another card: ").lower()
                if new_card == 'yes':
                    random_card, random_value = deal_card()
                    player_hand.append(random_card)
                    PLAYER_SCORE += random_value
                    player_hand, PLAYER_SCORE, PLAYER_ACE_REDUCTIONS = score_check(player_hand, PLAYER_SCORE,
                                                                                   PLAYER_ACE_REDUCTIONS)
                    print(f"\n{player} your hand is now {player_hand}")
                    print(f"Your hand score is {PLAYER_SCORE}")
                    print(f"\nThe house has {house_hand[0]}")
                    # print(f"The house hand score is {house_score}") --------- Testing
                    # If player score less than 22:
                    if PLAYER_SCORE < 22:
                        continue
                    # If player score 22 or over.
                    else:
                        print("\nSorry you are bust.")
                        GAME_OVER = True
                # If player does not want additional cards:
                elif new_card == "no":
                    print("\nYou are sticking.")
                    print(f"\n{player} your hand is now {player_hand}")
                    print(f"Your hand score is {PLAYER_SCORE}")
                    print(f"\nThe house has {house_hand}")
                    print(f"The house hand score is {HOUSE_SCORE}")
                    # If house score is less than 17:
                    if HOUSE_SCORE < 17:
                        # House issued extra card
                        random_card, random_value = deal_card()
                        house_hand.append(random_card)
                        HOUSE_SCORE += random_value
                        house_hand, HOUSE_SCORE, HOUSE_ACE_REDUCTIONS = score_check(house_hand, HOUSE_SCORE,
                                                                                    HOUSE_ACE_REDUCTIONS)
                        print("\nThe house has less than 17 another card will be issued.")
                        print(f"\nThe house has {house_hand}")
                        print(f"\nThe house hand score is {HOUSE_SCORE}")
                    # If house score 22 or over.
                    if HOUSE_SCORE > 21:
                        print("\nHouse is BUST. You Win.")
                        GAME_OVER = True
                    # Else if player and house tied.
                    elif HOUSE_SCORE == PLAYER_SCORE:
                        print("\nIt's a tie.")
                        GAME_OVER = True
                    elif 21 - PLAYER_SCORE < 21 - HOUSE_SCORE:
                        print("\nYou win.")
                        GAME_OVER = True
                    # Else house wins.
                    else:
                        print("\nHouse wins.")
                        GAME_OVER = True
                else:
                    print("You did not type 'Yes' or 'No'.")
                    continue
        print("\nWould you like to play again?")
        continue
    elif replay == "no":
        GAME_REPLAY = False
    else:
        print("Invalid input.")
print("\n" * 20)
print("\nGame Over")
