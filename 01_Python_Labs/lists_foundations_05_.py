"""
Lists foundations : additional topics

1. Left Rotate a List
2. Merge Two Sorted Lists
3. Find Duplicate Elements in a List
4. Combine Two Lists using zip()
5. Print List Items with Positions using enumerate()

"""

# 1. Left Rotate a List

# Predefined list
numbers = [1, 2, 3, 4, 5]

# Method 1
# Using slicing
left_rotated = numbers[1:] + numbers[:1]
print(
        f"\n\nLeft Rotate a List :\n"
        f"Original List : {numbers}\n"
        f"\n\tUsing Slicing :\n"
        f"\tLeft Rotated List : {left_rotated}\n"
    )

# Method 2
# Using loop and list operations
rotate_list = numbers.copy()
first_element = rotate_list.pop(0)
rotate_list.append(first_element)
print(
        f"\n\tUsing List Operations :\n"
        f"\tLeft Rotated List : {rotate_list}\n\n"
    )


# 2. Merge Two Sorted Lists

# Predefined lists
list_1 = [1, 3, 5, 7]
list_2 = [2, 4, 6, 8]

# Method 1
# Using + and sorted()
print(
        f"Merge Two Sorted Lists :\n"
        f"Original List_1 : {list_1}"
        f"\t\tOriginal List_2 : {list_2}\n"
        f"\n\tUsing + and sorted() :\n"
        f"\tMerged Sorted List : {sorted(list_1 + list_2)}\n"
    )

# Method 2
# Using loop
merged_sorted = []
for num in list_1:
    merged_sorted.append(num)

for num in list_2:
    merged_sorted.append(num)

merged_sorted.sort()
print(
        f"\n\tUsing Loop :\n"
        f"\tMerged Sorted List : {merged_sorted}\n\n"
    )


# 3. Find Duplicate Elements in a List

# Predefined list
items = [1, 2, 3, 2, 4, 5, 1, 6, 3]

# Method 1
# Using loop
seen = []
duplicates = []

for item in items:
    if item not in seen:
        seen.append(item)
    elif item not in duplicates:
        duplicates.append(item)

print(
        f"Find Duplicate Elements in a List :\n"
        f"Original List : {items}\n"
        f"\n\tUsing Loop :\n"
        f"\tDuplicate Elements : {duplicates}\n"
    )

# Method 2
# Using count()
duplicate_items = []
for item in items:
    if items.count(item) > 1 and item not in duplicate_items:
        duplicate_items.append(item)

print(
        f"\n\tUsing list.count() :\n"
        f"\tDuplicate Elements : {duplicate_items}\n\n"
    )


# 4. Combine Two Lists using zip()

# Predefined lists
students = ["Anu", "Bala", "Chitra"]
marks = [88, 91, 79]

combined_list = list(zip(students, marks))
print(
        f"Combine Two Lists using zip() :\n"
        f"Students List : {students}\n"
        f"Marks List : {marks}\n"
        f"\n\tUsing zip() :\n"
        f"\tCombined List : {combined_list}\n\n"
    )


# 5. Print List Items with Positions using enumerate()

# Predefined list
fruits = ["apple", "banana", "cherry", "mango"]

print(
        f"Print List Items with Positions using enumerate() :\n"
        f"Original List : {fruits}\n"
        f"\n\tUsing enumerate() :"
    )

for index, fruit in enumerate(fruits, start = 1):
    print(f"\t{index}. {fruit}")
