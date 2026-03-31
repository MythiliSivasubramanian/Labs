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