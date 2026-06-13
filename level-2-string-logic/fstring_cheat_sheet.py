# Python f-String Usage Guide & Cheat Sheet

# 1. Basic Substitution
name = "Mayur"
age = 20
print(f"Name: {name}\nAge: {age}")      # output: 
                                        # Name: Mayur
                                        # Age: 20

# 2. Calling Methods and Function
title = "my name is mayur!"
print(f"Uppercase: {title.upper()}")        # Uppercase: MY NAME IS MAYUR!
print(f"Is it lower?: {title.islower()}")   # Is it lower?: True


# 3. Numbers and Currency Formatting
pi = 3.14159265
large_number = 1000000000
percentage = 0.756

print(f"PI: {pi:.2f}")      # PI: 3.14
print(f"Population: {large_number:,}")      # Population: 1,000,000,000
print(f"Accuracy: {percentage:.1%}")        # Accuracy: 75.6%


# 4. Padding and Alignment
text = "test"
print(f"{text:<10} is")     # test       is
print(f"is {text:>10}")     # is       test
print(f"{text:-^10}")       # ---test---


# 5. Inline Debugging
x = 10
y = 15

# Return both the variable name and its value
print(f"{x=}")      # x=10

# It also works with expressions
print(f"{x + y = }")    # x + y = 25