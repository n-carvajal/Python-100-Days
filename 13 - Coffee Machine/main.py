"""Coffee Machine Simulator"""

# Imports
from data import MENU, resources, coins


# Functions
def get_order():
    """
    Prompts user for an order or key command.
    Checks command is valid or input inside menu.
    Returns validated item.
    """
    valid_input = False
    while not valid_input:
        order = input("What would you like? ").lower()
        if order != "off" and order != "report" and order not in MENU:
            print("You did not enter an item from the menu.")
            continue
        return order


def order_check(order):
    """
    Check user order ingredients against resources.
    If resources insufficient stops order and lists items missing.
    If resources sufficient returns True.
    """
    insufficient_items = []
    for item in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][item] >= resources[item]:
            insufficient_items.append(item)
    if insufficient_items:
        print(f"Sorry I cannot complete your order. I do not have enough: {', '.join(insufficient_items)}.\n")
    else:
        return True


def cost_check(order):
    """
    Indexes MENU using order to get cost.
    Returns cost of user's order.
    """
    return MENU[order]["cost"]


def get_coins():
    """
    Ensures user input for coins is a digit. Otherwise, asks again.
    Returns quarters, dimes, nickels, cents
    """
    while True:
        input_quarters = input("\nEnter your quarters: ")
        if not input_quarters.isdigit():
            print("You did not enter a numerical value for quarters.")
            continue
        input_dimes = input("Enter your dimes: ")
        if not input_dimes.isdigit():
            print("You did not enter a numerical value for dimes.")
            continue
        input_nickels = input("Enter your nickels: ")
        if not input_nickels.isdigit():
            print("You did not enter a numerical value for nickels.")
            continue
        input_cents = input("Enter your cents: ")
        if not input_cents.isdigit():
            print("You did not enter a numerical value for cents.")
            continue
        return int(input_quarters), int(input_dimes), int(input_nickels), int(input_cents)


def coin_tally(entered_quarters, entered_dimes, entered_nickels, entered_cents):
    """
    Returns sum of inputted coins.
    """
    total_quarters = entered_quarters * coins["quarters"]
    total_dimes = entered_dimes * coins["dimes"]
    total_nickels = entered_nickels * coins["nickels"]
    total_cents = entered_cents * coins["cents"]
    return total_quarters + total_dimes + total_nickels + total_cents


def display_resources():
    """
    Displays formatted view of resources.
    """
    print("\nCurrently the machine has:\n")
    print(f"Water: {resources['water']}ml.")
    print(f"Milk: {resources['milk']}ml.")
    print(f"Coffee: {resources['coffee']}g.")
    print(f"Money: ${resources['money']}.\n")


# Set while loop for machine to constantly vend:
MACHINE_VENDING = True
while MACHINE_VENDING:
    # Get valid user order:
    user_order = get_order()
    # If user enters 'off' stop machine vending:
    if user_order == "off":
        MACHINE_VENDING = False
    # Else if user enters 'report' have machine print current resources:
    elif user_order == "report":
        display_resources()
    # Else if user enters an item in the menu check order against resources:
    else:
        # If enough resources to process order:
        if order_check(user_order):
            print("\nProceeding with order.")
            # Calculate cost of order:
            cost = cost_check(user_order)
            print(f"The cost of your order is: {cost:.2f}")
            # Ask user to input coins.
            quarters, dimes, nickels, cents = get_coins()
            # Tally up the coins entered.
            amount_paid = coin_tally(quarters, dimes, nickels, cents)
            # If amount_paid is less than the cost return message.
            if amount_paid < cost:
                print("\nSorry not enough money. Money refunded\n")
            # Else if amount paid is greater than the cost.
            elif amount_paid >= cost:
                # Figure out the change due and return with message.
                change = amount_paid - cost
                # If change is greater than 0:
                if change > 0:
                    print(f"\nYour change is {change:.2f}.")
                else:
                    pass
                # Add price of transaction to money
                resources["money"] += cost
                # Make order and update machine resources to reflect stock usage.
                print(f"\nEnjoy your {user_order} ☕ \n")
                resources["water"] -= MENU[user_order]["ingredients"]["water"]
                resources["milk"] -= MENU[user_order]["ingredients"]["milk"]
                resources["coffee"] -= MENU[user_order]["ingredients"]["coffee"]
print("\nMachine turning off.")
