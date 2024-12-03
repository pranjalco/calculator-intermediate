# Importing art module so that we can print calculator logo
import art

"""
# Project 7: Calculator
### Description:
A functional calculator program that allows users to perform basic arithmetic operations 
(addition, subtraction, multiplication, division) interactively. The program supports reusability by allowing users 
to continue calculations with the previous result or start afresh. Features include an intuitive user interface for
input, dynamic operation handling using functions stored in a dictionary, and a visual logo integration from art.py.

### Features:
Dynamic calculation logic, supports multiple operations, option to continue with previous results, uses 
dictionaries for operation mapping, modular function-based design, external file integration for logo.

# Level: Intermediate
Author: Pranjal Sarnaik
Date: 2024-12-03
"""

# Defining required functions to do mathematical operations


def add(n1, n2):
    """This function takes two numbers and returns addition of two numbers"""
    return n1 + n2


def subtract(n1, n2):
    """This function takes two numbers and returns subtraction of two numbers"""
    return n1 - n2


def multiply(n1, n2):
    """This function takes two numbers and returns multiplication of two numbers"""
    return n1 * n2


def divide(n1, n2):
    """This function takes two numbers and returns division of two numbers"""
    if n2 == 0:
        # Here we are checking if second number is zero or not as division by zero is not possible.
        print("ZeroDivisionError: division by zero is not possible please enter positive number.")
        return None
    return n1 / n2


def get_number1():
    """This function takes number from user as input and returns that number as output"""
    while True:
        # Here we are checking and handling error when user enters something other than number using try except block
        try:
            return float(input("Please enter first number: "))
        except ValueError:
            print("could not convert string to float, please enter valid number.")


def get_number2():
    """This function takes number from user as input and returns that number as output"""
    while True:
        # Here we are checking and handling error when user enters something other than number using try except block
        try:
            return float(input("Please enter second number: "))
        except ValueError:
            print("could not convert string to float, please enter valid number.")


# This is dictionary from where based on user choice we are going to access mathematical functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

""" Here we made calculator_on True and as long as it is True the loop will continue to ask and 
perform calculation operations."""
# When user decides to quit calculator then this calculator_on becomes False and program stops.
calculator_on = True
while calculator_on:
    print(art.logo)

    try:
        # using get_number() we are asking user to enter number
        first_number = get_number1()
    except ValueError:
        print("could not convert string to float, please enter valid number")

    # Here if user wanted to perform operations based on the final result get then program will again start here.
    while True:
        # Here the first_number becomes the result which we get previously.

        operation_to_do = ""
        while operation_to_do not in operations:
            # Here when we will enter operation present in operations dictionary this loop will break.
            # If the user enters something that is not present in the operations dictionary, the program will continue
            # to ask for input until the user enters a valid operation from the dictionary.
            for symbol in operations:
                print(symbol)
            operation_to_do = input("Pick an operation: ")

            if operation_to_do not in operations:
                print("Error: Invalid input provided, please enter from (+, -, *, /)")

        # Asking user to enter second number using get_number() function
        second_number = get_number2()

        def calculations():
            """This function access the mathematical functions defined above based on user choice and return
            us the calculated result."""

            # We are checking if the selected operation is present in operations dictionary or not and if present then
            # doing the calculations by calling the functions.
            if operation_to_do in operations:
                return operations[operation_to_do](first_number, second_number)
            else:
                # If user enters invalid input then it will give error and exits the program.
                print("Error: Please enter valid input")
                exit()

        result = calculations()

        # If second number is zero in that case it can return result as None, So we're exiting the program here.
        if result is None:
            exit()

        # We are printing the result and the numbers.
        print(f"{first_number} {operation_to_do} {second_number} = {result}")
        """Here we are asking whether user want to continue operations using the result or want to 
        start using two new numbers."""
        # User also can quit the program by entering 'q'.
        continue_result = input(f"Enter 'y' to continue calculating with {result} or 'n' to start new calculation or 'q' to quit\n")

        # Here based on user choice we are going to do the operations.

        # If user enters "y" then using result as first number the operations will continue to run.
        if continue_result == "y":
            first_number = result
        # If user enters 'n' then it will start new by asking first number and second number.
        elif continue_result == "n":
            print("\n"*50)
            break
        # If user enters 'q' then it will stop the program.
        elif continue_result == "q":
            print("Calculator turned off")
            calculator_on = False
            break
        # If user enters something invalid then also it will stop the program.
        else:
            calculator_on = False
            print("Error: Please enter valid input, now turning off calculator.")
            break
