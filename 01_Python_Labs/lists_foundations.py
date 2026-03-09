"""
Lists Foundations :
    1. Remove Duplicates (Logic Builder) without and predefined options
    2. Find the second largest number (without and predefined options)
    3. Find all even numbers in a list (without and predefined options)

"""

# Method 1
# 1. Remove Duplicates (Logic Builder)
"""
    Keep the original order
    Do NOT use set()
    Use a loop and logic
"""

# Predefined List
nums = [1, 2, 2, 3, 4, 4, 5, 1, 6]
print(
        f"\n\nRemove the duplicates in below list :\n"
        f"Original List : {nums}\n"
    )

unique_nums = []
for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)
print(f"\tUsing Loops :\n\tAfter removing Duplicates : {unique_nums}\n")
        
# Method 2
# Using Sets 
my_sets = set(nums)
print(f"\tUsing Sets: \n\tAfter removing Dupliucates : {list(my_sets)}\n\n")

# 2. Find the second largest number
# Method 1 
# Manual logic
"""
Do NOT use sorted()
Do NOT use max() twice
Use loop logic
"""
        
# Predefined List
sample_nums = [10, 5, 8, 20, 15]

first = second = float('-inf') # Safe for negative numbers aswell
for num in sample_nums:
    if num > first:
        second = first
        first = num
    elif num > second:
        second = num
print(
        f"Second largest from list : \n"
        f"Original List : {sample_nums}\n"
        f"\n\tUsing Loops : \n\tSecond largest number : {second}\n"
    )

# Method 2
# Using sorted()
sorted_list = sorted(sample_nums, reverse = True)
print(f"\tUsing sorted() :\n\tSecond largest number : {sorted_list[1]}\n")

# Method 3
# Using max() twice
first_largest = max(sample_nums)
second_largest = max(n for n in sample_nums if n != first_largest) 
print(f"\tUsing max() :\n\tSecond largest number : {second_largest}\n\n")



# 3. Find all even numbers in a list

# Predefined List
sample_list = [100, 20, 33, 432, 2, 445, 6, -56, 0, -77, 2, -31]

even_list = []
for num in sample_list:
    if num % 2 == 0:
        even_list.append(num)
        
print(
        f"Find all even numbers in the list :\n"
        f"Original list : {sample_list}\n"
        f"\n\tUsing loops :\n\tList with only even numbers : {even_list}\n"
    )

# Method 2 using list comprehension

even_list_1 = [num for num in sample_list if num % 2 == 0]
print(f"\n\tUsing List comprehension :\n\tList with only even numbers : {even_list_1}\n\n")


