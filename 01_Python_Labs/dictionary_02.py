"""

1. Count frequency of each word in a sentence
2. Merge two dictionaries
3. Find the key with the highest value
4. Build a dictionary from two lists
"""

# Task 1: Count frequency of each word in a sentence
sentence = "python is easy and python is powerful"
words = sentence.split()
word_count = {}

for word in words:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1

print("Task 1: Word Frequency Count\n")
print(f"Sentence: {sentence}")
print(f"Word frequency: {word_count}")


# Task 2: Merge two dictionaries
student_marks_1 = {
    "math": 85,
    "science": 90,
}

student_marks_2 = {
    "english": 88,
    "science": 95,
}

print("\nTask 2: Merge Two Dictionaries\n")
print(f"Dictionary 1: {student_marks_1}")
print(f"Dictionary 2: {student_marks_2}")

merged_marks = student_marks_1.copy()
merged_marks.update(student_marks_2)

print(f"Merged dictionary: {merged_marks}")


# Task 3: Find the key with the highest value
expenses = {
    "rent": 1200,
    "food": 450,
    "travel": 300,
    "utilities": 250,
}

print("\nTask 3: Find Highest Value in Dictionary\n")
print(f"Expenses: {expenses}")

highest_key = ""
highest_value = 0

for key, value in expenses.items():
    if value > highest_value:
        highest_value = value
        highest_key = key

print(f"Highest expense category: {highest_key}")
print(f"Highest expense amount: {highest_value}")


# Task 4: Build a dictionary from two lists
keys = ["id", "name", "course"]
values = [101, "Max", "Python"]

print("\nTask 4: Create Dictionary from Two Lists\n")
print(f"Keys list: {keys}")
print(f"Values list: {values}")

student_record = {}
for index in range(len(keys)):
    student_record[keys[index]] = values[index]

print(f"Created dictionary: {student_record}")
