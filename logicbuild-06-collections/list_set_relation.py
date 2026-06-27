"""
List and Set relation
Datatypes boxing and unboxing

Concepts Practiced
Duplicate removal, 
Data cleaning, 
Set intersection, 
Set difference

"""

# 1: Remove duplicate names from a list using a set.
raw_names_list = ["Mayur", "Ram", "Anand", "Samarth", "Ram", "Samarth", "Ram"]
print(f"Original list with duplicates: {raw_names_list}")

unique_names_set = set(raw_names_list)
print(f"Unique set without duplicates: {unique_names_set}")

names_list = list(unique_names_set)
print(f"Clean list without duplicates: {names_list}")


# 2. Find all unique marks from a list.
marks_list = [94, 95, 91, 94, 85, 95, 91, 86, 81, 85]
print(f"Original list of marks with duplicates: {marks_list}")

unique_marks = set(marks_list)
print(f"Unique set of marks without duplicates: {unique_marks}")


# 3. Find students present in both classes.
class_a = {"Mayur", "Ram", "Anand", "Shiv", "Samarth"}
print("Class A: ", class_a)

class_b = {"Ram", "Virat", "Shiv", "Sai", "Ganesh"}
print("Class B: ", class_b)

print("Students present in both classes: ", class_a.intersection(class_b))


# 4. Find students who belong only to Class A.
print("Students who belong only to Class A", class_a.difference(class_b))
print("Students who belong only to Class B", class_b - class_a)