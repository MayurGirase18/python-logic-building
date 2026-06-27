# Practice 1: Student Names System

students = ["Mayur", "Ram", "Shiv", "Samarth"]
empty_list = []
single_element_list = [102]

print("First student: ", students[0])
print("Third student: ", students[2])
print("Last student: ", students[-1])
print("Total students: ", len(students))


# Practice 2: Shopping Cart System

cart = []
cart.append("Laptop")
cart.append("Mouse")
cart.append("Mobile")
cart.append("Headphone")

print("Cart: ", cart)

cart.remove("Mouse")
print("After remove, Cart: ", cart)

print("Total items: ", len(cart))


# Practice 3: Marks Analysis System

marks = [20, 86, 91, 50, 78, 12, 97, 85]
print("Highest marks: ", max(marks))
print("Lowest marks: ", min(marks))
print("Average marks: ", sum(marks)/len(marks))
print("Total marks: ", sum(marks))
print("Total Subjects: ", len(marks))