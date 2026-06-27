"""
Problem 6: Password Strength Checker

Check:

minimum length
uppercase exists
lowercase exists
digit exists

"""


password = input("Enter a password: ")

has_upper = False
has_lower = False
has_digit = False

for char in password:
    if char.isupper():
        has_upper = True

    if char.islower():
        has_lower = True

    if char.isdigit():
        has_digit = True

if len(password) >= 8 and has_upper == True and has_lower == True and has_digit == True:
    print("Your password is Strong..")

else:
    print("Your password is weak!!")