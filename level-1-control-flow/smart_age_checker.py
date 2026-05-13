''' PROBLEM 1 — Smart Age Checker
Problem

Take age input and print:

child
teenager
adult
senior citizen

Also validate:

negative age
age > 120 '''



age = int(input("Enter your age: "))
print("Your age: ", age)

if age<0 or age>120:
    print("Invalid age!!")

elif age<=12:
    print("Child")

elif age<=19:
    print("Teenager")

elif age<=59:
    print("adult")

else:
    print("Senior Citizen")