"""
Problem 9: Word Counter

Input sentence:
Print:

total characters
total words
uppercase count
lowercase count

"""

sentence = input("Write a Sentence: ")

total_ch = len(sentence)
words = sentence.split()
total_words = len(words)

upeercase_word = 0
lowercase_word = 0

for char in sentence:
    if char.isupper():
        upeercase_word+=1

    if char.islower():
        lowercase_word+=1


print("Sentence: ", sentence)
print("Total Characters: ", total_ch)
print("Total words: ", total_words)
print("Total uppercase count: ", upeercase_word)
print("Total lowercase words: ", lowercase_word)