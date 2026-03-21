"""
Lists foundations : missing topics part 1

1. Find the Sum of all Elements in a List
2. Find the Average of Elements in a List
3. Count the Occurrences of a Given Element
4. Find the Index Positions of an Element
5. Split a List into Even and Odd Numbers

"""

# 1. Find the Sum of all Elements in a List

# Predefined list
numbers = [10, 20, 30, 40, 50]

# Method 1
# Using loop
total = 0
for num in numbers:
    total += num

print(
        f"\n\nFind the Sum of all Elements in a List :\n"
        f"Original List : {numbers}\n"
        f"\n\tUsing Loop :\n"
        f"\tSum of elements : {total}\n"
    )

# Method 2
# Using sum()
print(
        f"\n\tUsing sum() :\n"
        f"\tSum of elements : {sum(numbers)}\n\n"
    )


# 2. Find the Average of Elements in a List

# Predefined list
marks = [85, 90, 78, 92, 88]

# Method 1
# Using loop
marks_total = 0
for mark in marks:
    marks_total += mark

average_marks = marks_total / len(marks)
print(
        f"Find the Average of Elements in a List :\n"
        f"Original List : {marks}\n"
        f"\n\tUsing Loop :\n"
        f"\tAverage of elements : {average_marks}\n"
    )

# Method 2
# Using sum() and len()
print(
        f"\n\tUsing sum() and len() :\n"
        f"\tAverage of elements : {sum(marks) / len(marks)}\n\n"
    )


# 3. Count the Occurrences of a Given Element

# Predefined list
items = [2, 4, 2, 6, 2, 8, 4, 2]
target = 2

# Method 1
# Using loop
count = 0
for item in items:
    if item == target:
        count += 1

print(
        f"Count the Occurrences of a Given Element :\n"
        f"Original List : {items}\n"
        f"Target Element : {target}\n"
        f"\n\tUsing Loop :\n"
        f"\tOccurrence count : {count}\n"
    )

# Method 2
# Using count()
print(
        f"\n\tUsing list.count() :\n"
        f"\tOccurrence count : {items.count(target)}\n\n"
    )


# 4. Find the Index Positions of an Element

# Predefined list
values = [5, 1, 5, 7, 5, 9, 2]
search_element = 5

# Method 1
# Using loop
index_positions = []
for index in range(len(values)):
    if values[index] == search_element:
        index_positions.append(index)

print(
        f"Find the Index Positions of an Element :\n"
        f"Original List : {values}\n"
        f"Search Element : {search_element}\n"
        f"\n\tUsing Loop :\n"
        f"\tIndex positions : {index_positions}\n"
    )

# Method 2
# Using list comprehension
index_list = [index for index in range(len(values)) if values[index] == search_element]
print(
        f"\n\tUsing List comprehension :\n"
        f"\tIndex positions : {index_list}\n\n"
    )


# 5. Split a List into Even and Odd Numbers

# Predefined list
sample_list = [11, 24, 35, 46, 57, 68, 79, 80]

# Method 1
# Using loop
even_numbers = []
odd_numbers = []

for num in sample_list:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print(
        f"Split a List into Even and Odd Numbers :\n"
        f"Original List : {sample_list}\n"
        f"\n\tUsing Loop :\n"
        f"\tEven Numbers : {even_numbers}\n"
        f"\tOdd Numbers : {odd_numbers}\n"
    )

# Method 2
# Using list comprehension
even_list = [num for num in sample_list if num % 2 == 0]
odd_list = [num for num in sample_list if num % 2 != 0]
print(
        f"\n\tUsing List comprehension :\n"
        f"\tEven Numbers : {even_list}\n"
        f"\tOdd Numbers : {odd_list}\n"
    )
