"""
Problem 13: Menu Driven Calculator

Menu:

Add
Subtract
Multiply
Divide
Exit

"""


print("--- Simple Calculator ---")

while True:
    print("\n--- Menu ---")
    print("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit\n")
    choice = int(input("Select operation (1 to 5): "))

    if choice == 5:
        print("Exiting....")
        break

    if choice < 1 or choice > 5:
        print("Invalid choice")
        break

    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))

    if choice == 1:
        print("Addition: ", num1 + num2)

    elif choice == 2:
        print("Subtraction: ", max(num1, num2) - min(num1, num2))

    elif choice == 3:
        print("Multiplication: ", num1 * num2)

    elif choice == 4:
        if num2 == 0:
            print("Can't divide by zero")

        else:
            print("Division: ", num1 / num2)