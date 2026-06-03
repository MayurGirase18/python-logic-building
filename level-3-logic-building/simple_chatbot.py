"""
Problem 14: Simple Chatbot

Create responses like:

hello
bye
how are you

Add:
unknown input handling.

"""


print("Simple chatbot")

while True:
    message = input("You: ").lower()

    if message == "hello":
        print("Bot: Hi!")

    elif message == "how are you?":
        print("Bot: I am fine.")

    elif message == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: I can't understand")