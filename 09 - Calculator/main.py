"""Simple Calculator Simulator"""


# Function Definitions:
def addition(n_1, n_2):
    """Takes two numbers and returns their addition."""
    return n_1 + n_2


def subtraction(n_1, n_2):
    """Takes two numbers and returns their subtraction."""
    return n_1 - n_2


def multiplication(n_1, n_2):
    """Takes two numbers and returns their multiplication."""
    return n_1 * n_2


def division(n_1, n_2):
    """Takes two numbers and returns their division."""
    return n_1 / n_2


def use_calc():
    """Asks to start calculator and validates response."""
    print("Would you like to use the calculator to perform operations?")
    valid_input = False
    while not valid_input:
        use_app = input("Type 'Yes' or 'No': ").lower()
        if use_app == "yes":
            return True
        elif use_app == "no":
            print("Calculator closing.")
            return False
        else:
            print("You did not type 'Yes' or 'No'.")


def number_validation():
    """Ensures value entered for operations is numerical."""
    valid_input = False
    while not valid_input:
        number = input("Enter a number to use in your calculation: ")
        if number.isdigit():
            return int(number)
        else:
            print("You did not enter a numerical value.")


def operation_validation():
    """Ensures the operations instructed is valid."""
    valid_operation = False
    while not valid_operation:
        operation = input("Type the sign of the operation you wish to perform: ")
        if operation in operations:
            return operation
        else:
            print("You did not enter an operation symbol from the list above.")


def restart_validation():
    """Asks if the user wants to perform new calculation and validates response."""
    valid_restart = False
    while not valid_restart:
        start_again = input("Type 'continue', 'restart', or 'quit': ").lower()
        if start_again == "continue" or start_again == "restart" or start_again == "quit":
            return start_again
        else:
            print("You did not type 'Continue', 'Restart', or 'Quit'.")


def display_symbols(operators):
    """Displays the symbols of the operations available."""
    for symbol in operators:
        print(symbol)


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}

print("Welcome to my calculator app.")
CALCULATING = True
CALCULATIONS = 1
if use_calc():
    while CALCULATING:
        if CALCULATIONS < 2:
            num1 = number_validation()
            display_symbols(operations)
            operator = operation_validation()
            num2 = number_validation()
            result = operations[operator](num1, num2)
            print(f"{num1} {operator} {num2} = {result}")
            print("Do you want to continue, stat again, or quit?")
            again = restart_validation()
            if again == 'continue':
                CALCULATIONS += 1
                print(f"Your current total is: {result}")
                display_symbols(operations)
                continue
            elif again == "quit":
                break
            else:
                CALCULATIONS = 0
                continue
        else:
            num3 = result
            operator = operation_validation()
            num4 = number_validation()
            result = operations[operator](num3, num4)
            print(f"{num3} {operator} {num4} = {result}")
            print("Do you want to continue or stat again?")
            again = restart_validation()
            if again == 'continue':
                CALCULATIONS += 1
                print(f"Your current total is: {result}")
                display_symbols(operations)
                continue
            elif again == "quit":
                break
            else:
                CALCULATIONS = 0
                continue
    print("Calculator closing.")
