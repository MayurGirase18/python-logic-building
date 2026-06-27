"""
Python File Handling Practice

Problem:
Store Marks of 5 Students and Calculate Average

Purpose:
Learn how to write data to a file, read it back, and perform basic calculations.

"""


print(f"{'\n    Student Marks Management    \n':=^100}")

with open("student_marks.txt", "w") as file:
    for i in range(1,6):
        mark = float(input(f"Enter marks of student {i}: "))
        file.write(f"Student {i} marks: {mark}\n")

print("Student marks added in file successfully.")


with open("student_marks.txt", "r") as file:
    data = file.read()

print("\nFile content: ")
print(data)


with open("student_marks.txt", "r") as file:
    marks = []

    for line in file:
        if line.strip():
            parts = line.split(":")

            number_string = parts[1].strip()
            marks.append(float(number_string))

if marks:
    average = sum(marks) / len(marks)
    print(f"Average marks: {average:.2f}")
else:
    print("No marks found in the file.")
