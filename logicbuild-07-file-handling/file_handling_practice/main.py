"""
Python Practice
Topic: File Handling

Purpose:
Practice Python file operations through progressively difficult exercises.

"""


# Practice 1: Create and Write File
print(f"{'\n    Practice 1: Create and Write File   \n':=^150}")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
branch = input("Enter your branch: ")

with open("student_info.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Branch: {branch}\n")

print("Data written successfully.")



# Practice 2: Read File
print(f"{'\n    Practice 2: Read File   \n':=^100}")

with open("student_info.txt", "r") as file:
    data = file.read()

print("File content: ")
print(data)



# Practice 3: Append Data
print(f"{'\n    Practice 3: Append Data   \n':=^100}")

new_info = input("Enter new information for append: ")

with open("student_info.txt", "a") as file:
    file.write(f"New Data: {new_info}\n")

print("Data appended successfully.\n")



# Practice 4: Count Lines
print(f"{'\n    Practice 4: Count Lines   \n':=^100}")

with open("student_info.txt", "r") as file:
    line_count = 0

    for line in file:
        line_count +=1

print("Total lines: ", line_count)
