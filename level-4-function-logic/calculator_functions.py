"""
Practice 1: Calculator Functions

Create separate functions:

add()
subtract()
multiply()
divide()

User chooses operation.

"""


def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b == 0:
        return "Can't divide by zero"
    else:
        return a/b
    

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")

choice = int(input("Select operation (1-4): "))

if choice < 1 or choice > 4:
    print("Invalid choice!")

else:
    if choice == 1:
        print("Result: ", add(num1, num2))

    elif choice == 2:
        print("Result: ", subtract(num1, num2))

    elif choice == 3:
        print("Result: ", multiply(num1, num2))

    elif choice == 4:
        print("Result: ", round(divide(num1, num2), 2))

    else:
        print("Invalid choice selection!")