"""
Dictionary practice in Python:
1. Invert keys and values in a dictionary
2. Count character frequency in a word
3. Group names by first letter
4. Sum all values in a dictionary
"""

# Task 1: Invert keys and values in a dictionary
country_codes = {
    "India": "IN",
    "Germany": "DE",
    "France": "FR",
}

print("Task 1: Invert Dictionary\n")
print(f"Original dictionary: {country_codes}")

inverted_codes = {}
for key, value in country_codes.items():
    inverted_codes[value] = key

print(f"Inverted dictionary: {inverted_codes}")


# Task 2: Count character frequency in a word
word = "dictionary"
char_count = {}

print("\nTask 2: Character Frequency Count\n")
print(f"Word: {word}")

for char in word:
    if char not in char_count:
        char_count[char] = 1
    else:
        char_count[char] += 1

print(f"Character frequency: {char_count}")


# Task 3: Group names by first letter
names = ["Max", "Mia", "Alex", "Anna", "Ben", "Bella"]

print("\nTask 3: Group Names by First Letter\n")
print(f"Names list: {names}")

grouped_names = {}
for name in names:
    first_letter = name[0]
    if first_letter not in grouped_names:
        grouped_names[first_letter] = [name]
    else:
        grouped_names[first_letter].append(name)

print(f"Grouped names: {grouped_names}")


# Task 4: Sum all values in a dictionary
monthly_sales = {
    "week_1": 1200,
    "week_2": 1500,
    "week_3": 1100,
    "week_4": 1700,
}

print("\nTask 4: Sum Dictionary Values\n")
print(f"Monthly sales: {monthly_sales}")

total_sales = 0
for value in monthly_sales.values():
    total_sales += value

print(f"Total sales: {total_sales}")
