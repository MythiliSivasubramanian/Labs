"""
Lists foundations : missing topics part 2

1. Find the First and Last Element in a List
2. Swap the First and Last Element
3. Find Elements Greater Than the Average
4. Create a List of Squares
5. Create a List of Common Elements Without Duplicates

"""

# 1. Find the First and Last Element in a List

# Predefined list
numbers = [12, 25, 37, 48, 59]

print(
        f"\n\nFind the First and Last Element in a List :\n"
        f"Original List : {numbers}\n"
        f"\n\tUsing Indexing :\n"
        f"\tFirst Element : {numbers[0]}\n"
        f"\tLast Element : {numbers[-1]}\n\n"
    )


# 2. Swap the First and Last Element

# Predefined list
sample = [10, 20, 30, 40, 50]

# Method 1
# Using direct swapping
sample_copy = sample.copy()
sample_copy[0], sample_copy[-1] = sample_copy[-1], sample_copy[0]
print(
        f"Swap the First and Last Element :\n"
        f"Original List : {sample}\n"
        f"\n\tUsing Swapping :\n"
        f"\tUpdated List : {sample_copy}\n"
    )

# Method 2
# Using temp variable
swap_list = sample.copy()
temp = swap_list[0]
swap_list[0] = swap_list[-1]
swap_list[-1] = temp
print(
        f"\n\tUsing Temp Variable :\n"
        f"\tUpdated List : {swap_list}\n\n"
    )


# 3. Find Elements Greater Than the Average

# Predefined list
marks = [60, 75, 90, 45, 88, 72]
average = sum(marks) / len(marks)

# Method 1
# Using loop
greater_than_average = []
for mark in marks:
    if mark > average:
        greater_than_average.append(mark)

print(
        f"Find Elements Greater Than the Average :\n"
        f"Original List : {marks}\n"
        f"Average : {average}\n"
        f"\n\tUsing Loop :\n"
        f"\tElements greater than average : {greater_than_average}\n"
    )

# Method 2
# Using list comprehension
greater_marks = [mark for mark in marks if mark > average]
print(
        f"\n\tUsing List comprehension :\n"
        f"\tElements greater than average : {greater_marks}\n\n"
    )


# 4. Create a List of Squares

# Predefined list
values = [1, 2, 3, 4, 5, 6]

# Method 1
# Using loop
squares = []
for value in values:
    squares.append(value ** 2)

print(
        f"Create a List of Squares :\n"
        f"Original List : {values}\n"
        f"\n\tUsing Loop :\n"
        f"\tSquares List : {squares}\n"
    )

# Method 2
# Using list comprehension
squares_list = [value ** 2 for value in values]
print(
        f"\n\tUsing List comprehension :\n"
        f"\tSquares List : {squares_list}\n\n"
    )


# 5. Create a List of Common Elements Without Duplicates

# Predefined lists
list_1 = [1, 2, 2, 3, 4, 5]
list_2 = [2, 2, 4, 6, 5, 5]

# Method 1
# Using loop
common_unique = []
for num in list_1:
    if num in list_2 and num not in common_unique:
        common_unique.append(num)

print(
        f"Create a List of Common Elements Without Duplicates :\n"
        f"Original List_1 : {list_1}"
        f"\t\tOriginal List_2 : {list_2}\n"
        f"\n\tUsing Loop :\n"
        f"\tCommon unique elements : {common_unique}\n"
    )

# Method 2
# Using set
print(
        f"\n\tUsing set() :\n"
        f"\tCommon unique elements : {list(set(list_1) & set(list_2))}\n"
    )
