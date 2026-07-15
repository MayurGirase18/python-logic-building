"""
Python OOP Logic Building

Problem:
Inventory Value Calculator.
Create product objects and calculate the total inventory value.

Purpose:
Practice creating product objects and calculating the total inventory value
using Object-Oriented Programming.

"""


from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int


    def inventory_value(self):
        return self.price * self.quantity


    def display(self):
        print("Product name: ", self.name)
        print("Price: ", self.price)
        print("Quantity: ", self.quantity)
        print(f"Value: ₹{self.inventory_value():,}")



products = [
    Product("Laptop", 60000, 5),
    Product("Mobile", 15000, 10),
    Product("Headphone", 4000, 18),
    Product("Mini Speaker", 2000, 10)
]

total_inventory_value = 0

for product in products:
    value = product.inventory_value()
    total_inventory_value += value

    product.display()
    print("-" * 30)


print(f"Total Inventory Value: ₹{total_inventory_value:,}")