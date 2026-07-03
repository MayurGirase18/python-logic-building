"""
Python Practice
Topic: Exception Handling

Purpose:
Practice Python exception handling using try, except, and finally.

"""


# Practice 1: Handle division by zero using try-except.
print(f"{' Practice 1: Handle division by zero using try-except ':-^64}")
try:
    num1 = 18
    num2 = 0

    result = num1/num2

    print("Result: ", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

print()



# Practice 2: Handle invalid integer input.
print(f"{' Practice 2: Handle invalid integer input ':-^50}")
try:
    number = int(input("Enter integer value: "))
    print("you entered value: ", number)

except ValueError:
    print("Error: Please enter a valid Integer value.")

print()



# Practice 3: Handle File Not Found Error
print(f"{' Practice 3: Handle File Not Found Error ':-^50}")
try:
    with open("demo.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("Error: File was not found.")

print()



# Practice 4: Use Finally Block to display a closing message.
print(f"{' Practice 4: Use Finally Block ':-^40}")
try:
    num1 = 18
    num2 = 0

    result = num1/num2

    print("Result: ", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

finally:
    print("Program execution completed successsfully.")
    print("Closing resources....")

print()