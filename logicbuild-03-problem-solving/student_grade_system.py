"""
Problem 12: Student Grade System

Input:

multiple subject marks

Output:

percentage
grade
fail/pass

Add:

top subject detection.

"""

math = int(input("Enter math marks: "))
python = int(input("Enter python marks: "))
java = int(input("Enter java marks: "))
js = int(input("Enter js marks: "))

total = math + python + java + js
print("Total obtained marks: ", total)

percentage = total/4
print(f"\nPercentage:  {percentage} %")

if percentage >= 90 and percentage <=100:
    print("Grade: A")

elif percentage >=80:
    print("Grade: B")

elif percentage >=70:
    print("Grade: C")

elif percentage >=60:
    print("Grade: D")

elif percentage >=40:
    print("Grade: Pass")

else:
    print("Grade: Fail")


highest = max(math, python, java, js)
print("Highest marks: ", highest)