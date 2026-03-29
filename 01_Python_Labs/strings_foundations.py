"""
Basic string indexing and slicing
"""

s = "python programming"

print(f"First character: {s[0]}")
print(f"Last character: {s[-1]}")
print(f"Sliced word ('python'): {s[:6]}")



s = "  PyThOn Is AwEsOmE  "

# Step 1: Remove extra spaces
cleaned = s.strip()

# Step 2: Convert to lowercase
lowered = cleaned.lower()

# Step 3: Replace word
final = lowered.replace("awesome", "powerful")

print(f"\nOriginal string: {s}\n")
print(f"After strip: {cleaned}\n")
print(f"After lowercase: {lowered}\n")
print(f"After replace: {final}\n")