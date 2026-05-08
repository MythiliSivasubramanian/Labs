"""
More set practice in Python:
1. Check membership in a set
2. Remove duplicates from two lists and combine them
3. Find common words between two sentences
4. Find unique vowels in a word
"""

# Task 1: Check membership in a set
colors = {"red", "blue", "green", "yellow"}
check_color = "blue"
missing_color = "black"

print("Task 1: Check Membership in Set\n")
print(f"Available colors: {colors}")

if check_color in colors:
    print(f"{check_color} is present in the set")
else:
    print(f"{check_color} is not present in the set")

if missing_color in colors:
    print(f"{missing_color} is present in the set")
else:
    print(f"{missing_color} is not present in the set")


# Task 2: Remove duplicates from two lists and combine them
list_a = [1, 2, 2, 3, 4, 4]
list_b = [3, 4, 4, 5, 6, 6]

print("\nTask 2: Combine Unique Values\n")
print(f"List A: {list_a}")
print(f"List B: {list_b}")

combined_unique = set(list_a) | set(list_b)
print(f"Combined unique values: {combined_unique}")


# Task 3: Find common words between two sentences
sentence_1 = "python is easy and powerful"
sentence_2 = "python is powerful and popular"

print("\nTask 3: Common Words in Sentences\n")
print(f"Sentence 1: {sentence_1}")
print(f"Sentence 2: {sentence_2}")

words_1 = set(sentence_1.split())
words_2 = set(sentence_2.split())
common_words = words_1 & words_2
print(f"Common words: {common_words}")


# Task 4: Find unique vowels in a word
word = "programming"
vowels = {"a", "e", "i", "o", "u"}

print("\nTask 4: Unique Vowels in a Word\n")
print(f"Word: {word}")

found_vowels = {char for char in word if char in vowels}
print(f"Unique vowels: {found_vowels}")
