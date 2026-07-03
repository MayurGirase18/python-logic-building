"""
Python Exception Handling Practice

Problem:
Read Numbers from a File and Ignore Invalid Entries

Purpose:
Practice reading files while safely handling invalid data.

"""


FILE_NAME = "numbers.txt"
numbers = []

with open(FILE_NAME, "w") as file:
    file.write("10\n")
    file.write("\n")
    file.write("18\n")
    file.write("Python\n")
    file.write("AI\n")
    file.write("45\n")
    file.write("Agent\n")
    file.write("4\n")

with open(FILE_NAME, "r") as file:
    for line in file:
        value = line.strip()

        if not value:
            continue

        try:
            number = float(value)
            print("Valid number: ", number)
            numbers.append(number)

        except ValueError:
            print("Ignored invalid entry: ", value)

print("Valid numbers: ", numbers)
