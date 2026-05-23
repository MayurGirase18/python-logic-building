"""
Problem 11: Simple Billing System

Take:

product name
quantity
price

Generate:

subtotal
tax
total bill

Add:

formatted receipt output.

"""


product_name = input("Enter Product name: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Product Price: "))

subtotal = quantity * price
tax = subtotal * 0.20
total = subtotal + tax

print("\n--- Bill ---")
print("\nProduct name: ", product_name)
print("Quantity: ", quantity)
print("Price: ", price)

print("\nsubtotal: ", subtotal)
print("Tax: ", tax)
print("Total Amount: ", total)