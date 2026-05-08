"""
Additional set practice in Python:
1. Find elements present in only one of two sets
2. Check whether one set is a subset of another
3. Remove duplicate characters from a string
4. Create a set of word lengths
"""

# Task 1: Find elements present in only one of two sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("Task 1: Symmetric Difference\n")
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

only_one_set = set_a ^ set_b
print(f"Elements present in only one set: {only_one_set}")


# Task 2: Check whether one set is a subset of another
main_set = {1, 2, 3, 4, 5, 6}
small_set = {2, 4, 6}

print("\nTask 2: Subset Check\n")
print(f"Main set: {main_set}")
print(f"Small set: {small_set}")

if small_set.issubset(main_set):
    print("Small set is a subset of main set")
else:
    print("Small set is not a subset of main set")


# Task 3: Remove duplicate characters from a string
text = "mississippi"

print("\nTask 3: Unique Characters in a String\n")
print(f"Original string: {text}")

unique_characters = set(text)
print(f"Unique characters: {unique_characters}")


# Task 4: Create a set of word lengths
words = ["apple", "banana", "kiwi", "grape", "banana"]

print("\nTask 4: Set of Word Lengths\n")
print(f"Words list: {words}")

word_lengths = {len(word) for word in words}
print(f"Unique word lengths: {word_lengths}")
