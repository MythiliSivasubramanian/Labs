"""
Basic string operations in Python:
1. Indexing and slicing
2. String cleaning and transformation
3. String search, replace, and split
4. String analysis and formatting
5. Count character types in a string
6. Check if a string is a palindrome
"""

# Task 1: Indexing and Slicing
s1 = "python programming"

print("Task 1: Indexing & Slicing\n")
print(f"First character: {s1[0]}")
print(f"Last character: {s1[-1]}")
print(f"Sliced word ('python'): {s1[:6]}\n")

# Task 2: String Manipulation
s2 = "  PyThOn Is AwEsOmE  "

print("Task 2: String Manipulation\n")

cleaned = s2.strip()
lowered = cleaned.lower()
final = lowered.replace("awesome", "powerful")

print(f"Original string: '{s2}'")
print(f"After strip: '{cleaned}'")
print(f"After lowercase: '{lowered}'")
print(f"Final output: '{final}'\n")

# Task 3: Search, Replace, and Split
s3 = "python is easy and python is powerful"

print("Task 3: Search, Replace & Split\n")
print(f"Original string: '{s3}'")
print(f"Count of 'python': {s3.count('python')}")
print(f"First occurrence index of 'python': {s3.find('python')}")
print(
    f"Replace first occurrence of 'python' with 'Java': "
    f"'{s3.replace('python', 'Java', 1)}'"
)
print(f"List of words: {s3.split()}")

# Task 4: String Analysis and Formatting
s4 = "data science with python"

print("\nTask 4: String Analysis & Formatting\n")

words = s4.split()
vowel_count = 0

for char in s4.lower():
    if char in "aeiou":
        vowel_count += 1

print(f"Original string: '{s4}'")
print(f"Title case: '{s4.title()}'")
print(f"Word count: {len(words)}")
print(f"Vowel count: {vowel_count}")

# Task 5: Count Character Types
s5 = "Python 3.11 is fun!"

print("\nTask 5: Count Character Types\n")

letters = 0
digits = 0
spaces = 0
special_chars = 0

for char in s5:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        special_chars += 1

print(f"Original string: '{s5}'")
print(f"Letters: {letters}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print(f"Special characters: {special_chars}")

# Task 6: Check if a String Is a Palindrome
s6 = "madam"

print("\nTask 6: Palindrome Check\n")

cleaned_s6 = s6.replace(" ", "").lower()
is_palindrome = cleaned_s6 == cleaned_s6[::-1]

print(f"Original string: '{s6}'")
print(f"Cleaned string: '{cleaned_s6}'")
print(f"Is palindrome: {is_palindrome}")
