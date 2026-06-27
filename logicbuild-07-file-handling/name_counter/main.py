"""
Python File Handling Practice

Problem:
Read a File Containing Names and Count Total Names

Features:
Store one name per line.
Ignore blank lines while counting.
Remove white spaces.

Purpose:
Practice reading text files and counting stored records.

"""


with open("names.txt", "w") as file:
    total_names = int(input("How many names do you want to store?: "))

    for i in range(1, total_names+1):
        name = input(f"Enter name {i}: ").strip()
        file.write(f"{name}\n")

print("Names added successfully.")


with open("names.txt", "r") as file:
    names = []
    
    for line in file:
        name = line.strip()

        if name:
            names.append(name)


print("Names stored: ", names)
print("Total names: ", len(names))
