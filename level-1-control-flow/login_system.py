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

attempt = 3

while attempt > 0: 
    username = input("Enter the username: ")
    password = input("Enter your password: ")

    if username == stored_username and password == stored_password:
        print("Login Successfull.")
        break

    else:
        attempt-=1
        if username != stored_username and password == stored_password:
            print("Incorrect Username!!")
            print(f"Remaining Attempts: {attempt}")

        elif username == stored_username and password != stored_password:
            print("Incorrect Password!!")
            print(f"Remaining Attempts: {attempt}")

        else:
            print("Username & Password are wrong!!")
            print(f"Remaining Attempts: {attempt}")

if attempt == 0:
    print("Account blocked...")