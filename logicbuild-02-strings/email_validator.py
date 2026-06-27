"""
Problem 7: Email Validator (Basic)

Check:

contains "@"
contains "."
no spaces

"""

# Trick 1:
""" 
email = input("Enter an Email: ")

valid_AtTheRate = False
valid_dot = False
valid_notSpace = False

for char in email:
    if char == "@":
        valid_AtTheRate = True

    if char == ".":
        valid_dot = True

    if char == " ":
        valid_notSpace = False


if valid_AtTheRate and valid_dot and valid_notSpace:
    print("Your email is valid..")

else:
    print("Your email is not valid!!")

"""


# Trick 2:
email = input("Enter an email: ")

if "@" in email and "." in email and " " not in email:
    print("Your email is valid..")

else:
    print("Your email is not valid!!")