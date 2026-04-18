"""
Stings Foundations :

1. Find the character that appears the most times in given Input.

"""

# Get a common Input 
user_input = input("\n\nEnter a String : ")

# 1. Find the character that appears the most times in given Input.
print(
        f"\n\n1. Find the character that appears the most times in given Input :\n"
     )

# Find the greatest of value from a dictionary by finding the frequency of each Key
my_string = {}

for each_char in user_input:
    if each_char not in my_string:
        my_string[each_char] = 1
    else:
        my_string[each_char] += 1
    
# Find the greatest value and its corresponding key
greatest_count = 0
max_char = ""

for k,v in my_string.items():
    if v > greatest_count:
        greatest_count = v
        max_char = k
        
        
print(
        f"\nThe character that appears the most times in given Input is "
        f"{max_char} which is {greatest_count} times\n"
    )