# import libraries
from numpy import NaN

# Display the calculator interface
print("""
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
""")

print("Welcome to the calculator program!")

# This function checks if the input is a valid number
def is_valid_number(num):
    """Check if the input is a valid number."""
    try:
        float(num)
        return True
    except ValueError:
        return False
# This function gets two numbers from the user
def get_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if not is_valid_number(num1) or not is_valid_number(num2):
        print("Invalid input! Please enter valid numbers.")
        return get_numbers()
    return float(num1), float(num2)

# This function gets the operator from the user
def get_operator():
    operator = input("Enter the operator (+, -, *, /): ")
    return operator


# this main loop runs the calculator program
while True:
    
    num1, num2 = get_numbers()
    operator = get_operator()

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero!")
            continue
        result = num1 / num2

    else:
        print("Invalid operator!")
        continue

    print(f"The result is: {result}")

    more_calculations = input("Do you want to perform another calculation? (yes/no): ").lower()
    if more_calculations != "yes":
        print("Thank you for using the calculator!")
        break