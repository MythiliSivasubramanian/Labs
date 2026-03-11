"""
Lists foundations

1. Move All Zeros to the End
2. Check if List is a Palindrome
3. Find Common Elements Between Two Lists
4. Find Pairs With Target Sum
5. Merge Two Lists

"""


# 1. Move All Zeros to the End

# Predefined list
list_1 = [0,1,0,3,12]

# Method 1 
# Using 
count_zeros = list_1.count(0)
without_zeros = [num for num in list_1 if num != 0 ]
result_list = without_zeros + [0] * count_zeros
print(
        f"\n\nMove All Zeros to the End of the list : \n"
        f"Original List : {list_1 }\n"
        f"\n\tUsing List comprehension :\n"
        f"\tFinal List : {result_list}\n\n"
)

# 2. Check if List is a Palindrome
list_2 = [1,2,3,2,1]

# Method 1 
# Using slicing
print(
                f"Check if List is a Palindrome : \n"
                f"Original List_1 : {list_1 }"
                f"\t\tOriginal List_2 : {list_2}\n"
                f"\n\tUsing Slicing :\n"
                f"\tIs List_1 Palindrome : {list_1[:] == list_1[::-1]}\n"
                f"\tIs List_2 Palindrome : {list_2[:] == list_2[::-1]}\n\n"
        )

# Method 2
# Using loops
list_1_reverse = []
list_2_reverse = []

for n in list_1:
        list_1_reverse.insert(0,n)
        
for n in list_2:
        list_2_reverse.insert(0,n)
        
print(
                f"\n\tUsing Loops :\n"
                f"\tIs List_1 Palindrome : {list_1 == list_1_reverse}\n"
                f"\tIs List_2 Palindrome : {list_2 == list_2_reverse}\n\n"
        )

# 3. Find Common Elements Between Two Lists

list_3 = [1,2,3,4]
list_4 = [3,4,5,6]

# Method 1
# using memebership operator 'in'
common_elements = []
for n in list_3:
        if n in list_4:
                common_elements.append(n)
                
        
print(
                f"Find Common Elements Between Two Lists : \n"
                f"Original List_3 : {list_3}"
                f"\t\tOriginal List_4 : {list_4}\n"
                f"\n\tUsing Loops and memebership operator :\n"
                f"\tCommon elements List_3 & List_4 : {common_elements} \n\n"
        )

# Method 2
# Using list comprehension

common_ele = [n for n in list_3 if n in list_4 ]
print(
                f"\n\tUsing List comprehension and memebership :\n"
                f"\tCommon elements List_3 & List_4 : {common_ele} \n\n"
        )

"""
# 4. Find Pairs With Target Sum

nums = [2,7,11,15]
target = 9
Expected output: [(2,7)]

Another example:
nums = [1,3,2,2,4]
target = 4
Expected output: [(1,3),(2,2)]

"""

print("\n\nFind Pairs With Target Sum :")
input_parts = input("Enter the List 1 : ").split(",")
user_input = list(map(int,input_parts))
target = int(input("Enter the sum target number : "))

sum_pairs = []

for i in range(len(user_input)):
       for j in range(i + 1, len(user_input)):
               if user_input[i] + user_input[j] == target:
                       sum_pairs.append((user_input[i],user_input[j]))
print( 
               
                
                f"\n\tUsing nested Loops :\n"
                f"\tPossible combinations : {sum_pairs} \n\n")
        

# 5. Merge two lists
list_5 = [1,3,5]
list_6 = [2,4,6]

# Method 1
# Using +
print(
                f"Merge two lists : \n"
                f"Original List_5 : {list_5}"
                f"\t\tOriginal List_6 : {list_6}\n"
                f"\n\tUsing + :\n"
                f"\tMerged List : {list_5 + list_6} \n\n"
        )

# Method 2
# Using list.extend() 
#list_5.extend(list_6) adds list_6 to list_5 in place. Hence creating a copy

list_5_copy = list_5.copy()
list_5_copy.extend(list_6) # Ammends in place of list_5
print(
                
                f"\n\tUsing list.extend() :\n"
                f"\tMerged List : {list_5_copy} \n\n"
        )

# Method 3
# using loops
merged_list = list_5.copy()
for i in list_6:
      merged_list.append(i)
       
print(
                
                f"\n\tUsing Loop :\n"
                f"\tMerged List : {merged_list} \n\n"
        )
