'''
Problem 2: Login System

Create:

stored username
stored password

Ask user to login.

Add:
incorrect username handling
incorrect password handling
successful login message
Advanced Version

Add:
3 login attempts
account locked message
'''

stored_username = "mayur18"
stored_password = "pass123"

username = input("Enter the username: ")
password = input("Enter your password: ")

if username == stored_username and password == stored_password:
    print("Login Successfull.")

elif username != stored_username and password == stored_password:
    print("Incorrect Username!!")

elif username == stored_username and password != stored_password:
    print("Incorrect Password!!")

else:
    print("Username & Password are wrong!!")