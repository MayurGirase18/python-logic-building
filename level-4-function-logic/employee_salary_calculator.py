"""
Practice 2: Employee Salary Calculator

Functions:

calculate_bonus()
calculate_tax()
calculate_salary()

Input:

Employee Name
Base Salary

Output:

Bonus
Tax
Final Salary

Engineering Skill:
Breaking large logic into smaller functions.

"""


def calculate_bonus(base_salary):
    return base_salary * 0.1

def calculate_tax(base_salary):
    return base_salary * 0.05

def calculate_salary(base_salary):
    bonus = calculate_bonus(base_salary)
    tax = calculate_tax(base_salary)

    final_salary = base_salary + bonus - tax

    return bonus, tax, final_salary


name = input("Enter Employee name: ")
salary = float(input("Enter base salary: "))

bonus, tax, final_salary = calculate_salary(salary)

print("\n--- Employee Report ---")
print("Name: ", name)
print("Base salary: ", salary)
print("Bonus: ", bonus)
print("Tax: ", tax)
print("Final salary: ", final_salary)