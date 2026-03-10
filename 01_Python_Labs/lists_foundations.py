"""
Lists Foundations :  without and predefined options
    1. Remove Duplicates 
    2. Find the second largest number 
    3. Find all even numbers in a list 
    4. Reverse a list 
    5. Find the Frequency of Each Element (using list, loops and not dict)
    6. Find the Largest Number in a List  
    7. Find the Smallest Number
    8. Rotate a List (Right Rotation)
    9. Flatten a Nested List

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

# 4. Reverse a list 
# Method 1 
# Using loop

# predfefined list
sample = [10, 0, 8, -20, 15]
print(f"Reverse the elements in the list : \nOriginal List : {sample}\n\n")
reversed_list = []

for num in sample:
    reversed_list.insert(0,num)
print(
        f"\tUsing Loops : \n"
        f"\tReversed List : {reversed_list}\n"
    )

# Method 2 
# Using Slicing and step value
print(
        f"\n\tUsing Slicing & Step value : \n"
        f"\tReversed List : {sample[::-1]}\n"
    )

# Method 3
# Using reversed() 
rev_list = list(reversed(sample))

print(
        f"\n\tUsing list(reversed(list)) : \n"
        f"\tReversed List : {rev_list}\n"
    )

# Method 4
# using list.reverse (Modifies the original list in place)

sample_copy = sample.copy()
sample_copy.reverse()
print(
        f"\n\tUsing list.reverse() : \n"
        f"\tModifies the original list in place\n"
        f"\tReversed List : {sample_copy}\n"
)



# 5. Find the Frequency of Each Element 
# Using list and loop logic and not dictionaries

# Predefined list
nums  = [1,2,2,3,3,3]

number = []
times = []

for n in nums:
    if n not in number:
        number.append(n)


for n in number:
    times.append(nums.count(n))
    
frequency = list(zip(number,times))
print(
        f"Frequency of each elements in list :\n"
        f"Original List : {nums}\n"
        f"\n\tUsing Loop and list :\n"
        f"\tElements and its frequency : {frequency}\n"
        )

# 6. Find the Largest Number in a List
# Method 1
# Using loop and comparision operator

#Predefined list
my_list = [10,4,8,20,3]
large_num = my_list[0]

for n in my_list[1:]:
    if n > large_num:
        large_num = n
        
print(
    
        f"\nFind the Largest Number in a List :\n"
        f"Original List : {my_list}\n"
        f"\n\tUsing Loop :\n"
        f"\tLargest number : {large_num}\n"
    )


# Method 2
# using max()

print(
        f"\n\tUsing max() :\n"
        f"\tLargest number : {max(my_list)}\n"
    )

# 7. Find the Smallest Number
# Method 1 
# using loops and comparison operator

#Predefined list
n = [10,4,8,20,3]
smallest = n[0]
for elements in n[1:]:
    if elements < smallest:
        smallest = elements
        
print(
        f"\nFind the smallest Number in a List :\n"
        f"Original List : {n}\n"
        f"\n\tUsing Loop :\n"
        f"\tSmallest number : {smallest}\n"
    )

# Method 2
# using min()
print(
        f"\n\tUsing min() :\n"
        f"\tSmallest number : {min(n)}\n"
    )
  
 # 8. Rotate a List (Right Rotation)
# Method 1
# Using slicing
 
numbers = [1,2,3,4,5]
list_length = len(numbers)
rotated = numbers[(list_length -1):] + numbers[:(list_length -1)]
print(
        f"\nRotate a List (Right Rotation) :\n"
        f"Original List : {numbers}\n"
        f"\n\tUsing slicing :\n"
        f"\tRotated List : {rotated}\n"
    )

# Method 2
# using Loop
rotate = []
length_list = len(numbers)
rotate.insert(0,numbers[length_list - 1])
rotate.extend(numbers)
rotate.pop()
print(
        f"\n\tUsing List Operations :\n"
        f"\tRotated List : {rotate}\n"
    )

# Method 3
# Using Loop

# Last element
last_element = numbers[-1]
rotated_list = [last_element]

for n in numbers[:-1]:
    rotated_list.append(n)
print(
        f"\n\tUsing Loop :\n"
        f"\tRotated List : {rotated_list}\n"
    )


# 9. Flatten a Nested List

# Predefined nested list
nested_list = [[1,2],[3,4],[5,6]]

# Method 1
# using nested loops
flat_list = []
for sublist in nested_list:
    for n in sublist:
        flat_list.append(n)
print(
        f"\nFlatten a Nested List :\n"
        f"Original Nested List : {nested_list}\n"
        f"\n\tUsing Loop :\n"
        f"\tFlat List : {flat_list}\n"
      )

# Method 2
# Using List comprehension
flatten_list = [num for sublist in nested_list for num in sublist]
print(
        f"\n\tUsing List Comprehension :\n"
        f"\tFlat List : {flatten_list}\n"
      )