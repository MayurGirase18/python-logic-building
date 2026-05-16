"""
Take a number and print:

even/odd
positive/negative
divisible by 5 
divisible by 10

"""

num = int(input("Enter a number: "))

# even/odd
if num % 2 == 0:
    print(f"{num} is Even.")

else:
    print(f"{num} is Odd.")

# positive/negative
if num > 0:
    print(f"{num} is Positive.")

elif num < 0:
    print(f"{num} is Negative.")

else:
    print(f"{num} is Zero.")

# divisible by 5 or 10
if num % 5 == 0:
    print(f"{num} is divisible by 5.")

if num % 10 == 0:
    print(f"{num} is divisible by 10.")