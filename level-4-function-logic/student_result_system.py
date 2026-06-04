"""
Practice 3: Student Result System

Functions:

calculate_percentage()
calculate_grade()
display_report()

Output:

Percentage
Grade
Pass/Fail

"""

def calculate_percentage(marks):
    total = sum(marks)
    percentage = total/5
    return total, percentage

def calculate_grade(percentage):
    if percentage>=90 and percentage<100:
        grade = "A"

    elif percentage>=80:
        grade = "B"

    elif percentage>=70:
        grade = "C"

    elif percentage>=40:
        grade = "D"

    else:
        grade = "F"

    return grade

def display_report(name, total, percentage, grade):
    print("\n--- Student Report ---")
    print("Name: ", name)
    print("Total obtained marks: ", total)
    print("Percentage: ", percentage)
    print("Grade: ", grade)

    if percentage >= 40:
        print("Status: Pass")

    else:
        print("Status: Fail")



name = input("Enter your name: ")
marks = []

for i in range(5):
    mark = int(input(f"Enter subject {i+1} marks: "))
    marks.append(mark)

total, percentage = calculate_percentage(marks)
grade = calculate_grade(percentage)
display_report(name, total, percentage, grade)