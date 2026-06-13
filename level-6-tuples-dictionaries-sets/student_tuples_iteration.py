"""
Student Tuples
-------------------------
Concepts Practiced: Multiple tuples, Collections, Iteration

This script creates multiple student records as tuples, stores them 
in a list collection, and iterates through them to display the data.

"""


student_info = [
    (118, "Girase Mayur", "O"),
    (119, "Singh Anand", "A+"),
    (120, "Rajput Samarth", "O"),
    (121, "Virat Kohli", "A"),
    (122, "Roy Shiv", "B")
]

print(f"{'Student Record':-^40}\n")
print(f"{'Rollno':<10} | {'Name':<20} | {'Grade':<8}")

for student in student_info:
    roll_no, name, grade = student

    print(f"{roll_no:<10} | {name:<20} | {grade:<8}")