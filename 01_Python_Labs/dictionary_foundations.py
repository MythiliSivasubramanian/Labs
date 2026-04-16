"""
Basic dictionary operations in Python:
1. Create, access, update, and add dictionary values
2. Loop through dictionary keys and values
3. Check if a key exists in a dictionary
"""

# Task 1: Create, Access, Update, and Add Values
student = {
    "name": "Max",
    "age": 24,
    "course": "Python",
}

print("Task 1: Dictionary Basics\n")
print(f"Original dictionary: {student}")
print(f"Student name: {student['name']}")
print(f"Student course: {student['course']}")

student["age"] = 25
student["city"] = "Berlin"

print(f"Updated age: {student['age']}")
print(f"Dictionary after adding city: {student}")

# Task 2: Loop Through Dictionary Keys and Values
product = {
    "id": 101,
    "name": "Laptop",
    "price": 75000,
    "stock": 12,
}

print("\nTask 2: Loop Through Dictionary\n")
print(f"Original dictionary: {product}\n")

print("Keys:")
for key in product:
    print(key)

print("\nValues:")
for value in product.values():
    print(value)

print("\nKey-Value pairs:")
for key, value in product.items():
    print(f"{key}: {value}")

# Task 3: Check if a Key Exists in a Dictionary
employee = {
    "id": 501,
    "name": "Alex",
    "department": "Data",
    "salary": 55000,
}

search_key = "department"
missing_key = "email"

print("\nTask 3: Check Key Existence\n")
print(f"Dictionary: {employee}")

if search_key in employee:
    print(f"'{search_key}' exists with value: {employee[search_key]}")
else:
    print(f"'{search_key}' does not exist in the dictionary")

if missing_key in employee:
    print(f"'{missing_key}' exists with value: {employee[missing_key]}")
else:
    print(f"'{missing_key}' does not exist in the dictionary")
