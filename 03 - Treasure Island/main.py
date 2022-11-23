"""Treasure Island Choice Game"""

# Intro
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a crossroads.")
print("Where do you want to go?")
crossroad = input("Type 'Left', 'Right', or 'Straight': ")
# If user takes a LEFT:
if crossroad.lower() == "left":
    print("After a long walk, you reach a stream.")
    print("It's a hot day and you are thirsty.")
    print("Do you drink from it?")
    drink = input("Type 'Yes' or 'No': ")
    # If user takes a DRINK:
    if drink.lower() == "yes":
        print("The water is filled with parasites.")
        print("They sap you of your strength and you require rescue.")
        print("Do you want to start a fire to signal you need help or head back where you came?")
        fire = input("Type 'Fire' or 'Return': ")
        # If user makes a FIRE:
        if fire.lower() == "fire":
            print("The fire alerts the local cannibals of your existence.")
            print("They quickly round you up and boil you in their pot for dinner.")
            print("You LOSE.")
        # else user NO FIRE:
        else:
            print("The parasites cause complete debilitation.")
            print("You faint on the way back and are soon vulture supper.")
            print("You LOSE.")
    # else user NO DRINK:
    else:
        print("You become delusional from thirst and start to hallucinate.")
        print("In your stupor you fail to see a giant crevice.")
        print("You swiftly fall in and starve over a period of days.")
        print("You LOSE.")
# Else if user takes a RIGHT:
elif crossroad.lower() == "right":
    print("After a long walk you reach an oasis where there is a cave.")
    print("Do you dare venture inside?")
    cave = input("Type 'Yes' or 'No'")
    # if user goes in CAVE:
    if cave.lower() == "yes":
        print("Once inside you see a massive haul of treasure.")
        print("You swiftly proceed to fill your boots and promptly return to base.")
        print("You WIN.")
    # else if user NO CAVE:
    else:
        print("Being in the open whilst in the wild is not a good idea.")
        print("A pack of Leopards chance upon you and proceed to rip the meat from your bones.")
        print("You LOSE.")
# Else user goes STRAIGHT:
else:
    print("Unbeknownst to you, there lies a tavern full of scoundrels up ahead.")
    print("It's closing time and everyone is looking for easy loot and a fight.")
    print("You are robbed of your possessions and in the ensuing struggle are mortally wounded.")
    print("You LOSE.")
