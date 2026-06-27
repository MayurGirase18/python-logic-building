"""
Problem 8: Username Generator

Input:

first name
last name
birth year

Generate username automatically.

"""

firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
birthyear = int(input("Enter your Birth year: "))

username = firstname.lower() + "_" + lastname.lower() + "_" + str(birthyear)

print("Generated username: ", username)