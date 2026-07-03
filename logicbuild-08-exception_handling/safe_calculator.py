"""
Python Exception Handling Practice

Problem:
Safe Calculator
Create a calculator that never crashes because of invalid input.

Purpose:
Practice handling invalid user input and runtime errors so the program never crashes.

"""


print(f"{' Calculator ':-^20}")

try:
    num1 = float(input("Enter the number 1: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter the number 2: "))

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        result = num1 / num2

    else:
        raise ValueError("Invalid operator.")
    
    print("\nResult: ", result)

except ValueError as error:
    print("Input Error: ", error)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except Exception as error:
    print("Unexpected Error: ", error)

finally:
    print("Calculator closed successfully.")
