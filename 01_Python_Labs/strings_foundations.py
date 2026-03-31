"""
Basic string operations in Python:
1. Indexing and slicing
2. String cleaning and transformation
3. String search, replace, and split
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
