"""
string_practice.py
Basic string operations in Python:
1. Indexing and slicing
2. String cleaning and transformation

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

# Step 1: Remove extra spaces
cleaned = s2.strip()

# Step 2: Convert to lowercase
lowered = cleaned.lower()

# Step 3: Replace 'awesome' with 'powerful'
final = lowered.replace("awesome", "powerful")

print(f"Original string: '{s2}'")
print(f"After strip: '{cleaned}'")
print(f"After lowercase: '{lowered}'")
print(f"Final output: '{final}'")


s3 = "python is easy and python is powerful"
"""
- Count how many times "python" appears
- Find the first occurrence index of "python"
- Replace only the first occurrence of "python" with "Java"
- Convert the whole string into a list of words
"""
print(f"\nThe original String : {s3}\n")
print(f"\nCount how many times 'python' appears : {s3.count("python")}\n")
print(f"Find the first occurrence index of 'python' : {s3.find('python')}\n")
print(f"Replace only the first occurrence of 'python' with 'Java' : {s3.replace("python","Java", 1)}\n")
print(f"Convert the whole string into a list of words : {s3.split()}\n")
