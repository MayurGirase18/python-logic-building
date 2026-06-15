"""
Python Set Practice Exercises
------------------------------
This file contains solutions for three basic Python tuple practice exercises:
1. Create a set of fruits and display all fruits.
2. Add new fruits to an existing set.
3. Remove fruits from a set.
4. Check whether a fruit exists in a set.
5. Find the total number of unique items.

Concepts Practiced
Set creation, insertion, deletion, Membership testing, Uniqueness property of sets.

"""

# Practice-1: Set Creation
fruits = {"Apple", "Banana", "Cherry", "Orange", "Apple", "Cherry"}
single_set = {1}
empty_set = set()

print("Initial Fruit Set: ", fruits)


# Practice-2: Add Elements
fruits.add("Coconut")
fruits.add("Grapes")

print("\nSet After add new fruits: ", fruits)


# Practice-3: Remove fruits
fruits.remove("Grapes")
print("\nSet after remove fruit: ", fruits)


# Practice-4: Membership Check
search_fruit = input("\nEnter a fruit name to check its existence: ").capitalize()

if search_fruit in fruits:
    print(f"Yes, '{search_fruit}' is present in the set.")
else:
    print(f"No, '{search_fruit}' is NOT present in the set.")


# Practice-5: Count Unique Items
print("\nFinal Fruits set: ", fruits)
print("Total Unique fruits: ", len(fruits))