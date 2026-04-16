"""
Basic dictionary operations in Python:
1. Create, access, update, and add dictionary values
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
