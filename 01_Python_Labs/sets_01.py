"""
Basic set operations in Python:
1. Create a set and remove duplicate values
2. Add and remove items from a set
3. Find union, intersection, and difference
4. Use set comprehension
"""

# Task 1: Create a set and remove duplicate values
numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]

print("Task 1: Remove Duplicates Using Set\n")
print(f"Original list: {numbers}")

unique_numbers = set(numbers)
print(f"Unique values as set: {unique_numbers}")


# Task 2: Add and remove items from a set
fruits = {"apple", "banana", "cherry"}

print("\nTask 2: Add and Remove Set Items\n")
print(f"Original set: {fruits}")

fruits.add("orange")
print(f"After adding orange: {fruits}")

fruits.remove("banana")
print(f"After removing banana: {fruits}")


# Task 3: Union, intersection, and difference
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("\nTask 3: Set Operations\n")
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union: {set_a | set_b}")
print(f"Intersection: {set_a & set_b}")
print(f"Difference (A - B): {set_a - set_b}")


# Task 4: Set comprehension
nums = [1, 2, 2, 3, 4, 5, 5, 6]

print("\nTask 4: Set Comprehension\n")
print(f"Original list: {nums}")

squared_even_numbers = {num ** 2 for num in nums if num % 2 == 0}
print(f"Squared even numbers as set: {squared_even_numbers}")
