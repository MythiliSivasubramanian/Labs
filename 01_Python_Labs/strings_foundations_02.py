"""
Manual Counting without using Built ins
s1 = "python is powerful and python is easy"
    1. Count how many times "python" appears
    2. Print the result
"""

print(
        f"Task 1: Manual Counting without using Built ins :\n"
        f"\t1. Count how many times 'python' appears?"
        f"\t2. Print the result\n"
    )

# Predefined String 
s1 = "python is powerful and python is easy"
print(
        f"Original String s1:\n"
        f"{s1}\n"
    )
# Count 'python' in s4 without using builtins (count)

search_word = "python"
# Initialize the search word_count as 0
count = 0

# convert the string into words [list] using .split()
for word in s1.split():
    if word == search_word:
        count += 1
    
print(
        f"Count of word'python' in s1 : {count}\n"
     )