"""
Problem 10: String Compression

Input:

aaabbcccc

Output:

a3b2c4

"""


text = input("Enter a text: ")

compressed = ""     # string that used to store the result
count = 1       # count starts from 1 due to first character already exist

for i in range(len(text) - 1):
    if text[i] == text[i+1]:
        count+=1
    
    else:
        compressed += text[i] + str(count)
        count = 1


compressed += text[-1] + str(count)

print("Compressed String: ", compressed)