'''
Problem 3: ATM Withdrawal Simulator

User enters:

balance
withdrawal amount

Check:

sufficient balance
invalid withdrawal
negative values
Real Concepts
validation
transaction rules
edge cases

'''

balance = float(input("Enter your current bank balance: "))
withdrawal_amount = float(input("Enter the amount for Withdrawal: "))

if balance < 0:
    print("Invalid Balance!!")

else:
    if withdrawal_amount < 0 or withdrawal_amount > balance:
        print("Invalid Withdrawal!!")

    else:
        balance = balance - withdrawal_amount
        print(f"{withdrawal_amount} is withdrawal successfully.")
        print(f"Remaining Balance: {balance}")
