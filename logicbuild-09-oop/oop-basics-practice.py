"""
Python Practice
Topic: Object-Oriented Programming (OOP) Basics

Purpose:
Practice creating classes, objects, constructors, and methods.


"""

from dataclasses import dataclass       # for method 2 only


# Practice 1: Student class

print(f"{'\n        Practice 1: Student class       \n':=^120}")

# method 1----
# class Student:
#     def __init__(self, name, age, branch):
#         self.name = name
#         self.age = age
#         self.branch = branch

    
#     def display(self):
#         print("Name: ", self.name)
#         print("Age: ", self.age)
#         print("Branch: ", self.branch)


# method 2-----
@dataclass
class Student:
    name: str
    age: int
    branch: str

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Branch: ", self.branch)


s1 = Student("mayur", 20, "cse")
s2 = Student("roy", 22, "ai")
s1.display()
s2.display()
