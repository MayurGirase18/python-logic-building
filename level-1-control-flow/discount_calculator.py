"""
Problem 5: Discount Calculator

Input:

product price
membership status

Rules:

members get extra discount
large orders get more discount

"""

price = float(input("Enter the product price: "))
is_member = input("Are you a Member? (yes/no) ")

discount = 0

if price > 5000:
    discount+=10

if is_member == "yes":
    discount+=5

final_price = price - (price*discount/100)

print(f"Actual price: {price}")
print(f"Discount: {discount}")
print(f"Final Price: {final_price}")