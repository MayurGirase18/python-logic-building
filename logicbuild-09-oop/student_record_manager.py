"""
Python OOP Logic Building

Problem:
Student Record Manager.
Create multiple student objects and display all records.

Purpose:
Practice creating multiple objects, storing them in a collection,
and displaying object information using Object-Oriented Programming.

"""


from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    branch: str

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Branch: ", self.branch)
        print("-" * 30)


students = [
    Student("Mayur", 20, "AI"),
    Student("Ram", 22, "CS"),
    Student("Pravin", 17, "CSE"),
    Student("Mahendra", 19, "Software")
]

print("Students Record:\n")

for student in students:
    student.display()