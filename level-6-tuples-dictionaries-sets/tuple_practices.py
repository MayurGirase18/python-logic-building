"""
Python Tuple Practice Exercises
------------------------------
This file contains solutions for three basic Python tuple practice exercises:
1. Student Information (Tuple creation and indexing)
2. Product Details (Tuple storage and arithmetic operations)
3. Employee Record (Tuple data representation and formatted output)

"""


# Practice-1: Student Information
print("---- Student Information ----")
student_info = ("Girase Mayur", 20, "Computer science", "Surat")
print("Full Student Information: ", student_info)
print("First element (Name): ", student_info[0])
print("Last element (City): ", student_info[-1])


# Practice-2: Products details
print("\n---- Products Details ----")
product_info = ("Laptop", 59999.999, 2)

product_name, price, quantity = product_info
total = price * quantity

print("Product name: ", product_name)
print(f"{product_name} price per unit: {price}")
print("Quantity: ", quantity)
print(f"Total Value: {total:.2f}")


# Practice-3: Employee Record
employee_record = ("EP1018", "Girase Mayur", 40500)
employee_id, employee_name, salary = employee_record

print("\n", "-"*5, " Employee Record ", "-"*5)
print(f"Employee ID      : {employee_id}")
print(f"Employee Name    : {employee_name}")
print(f"Salary           : ${salary:,}")