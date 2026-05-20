"""
Problem 7: Email Validator (Basic)

Check:

contains "@"
contains "."
no spaces

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