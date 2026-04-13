"""
Strings foundations : 

1. Reverse a string
2. Count vowels and consonants in a string
3. Remove all spaces from a string
4. Find the longest word in a sentence
5. Capitalize the first letter of each word
6. Count the number of words in a sentence
7. Check whether a string starts and ends with a given character

"""

# 1. Reverse a string

# Predefined string
s1 = "python"

# Method 1
# Using slicing
print(
        f"\n\nReverse a String :\n"
        f"Original String : '{s1}'\n"
        f"\n\tUsing Slicing :\n"
        f"\tReversed String : '{s1[::-1]}'\n"
    )

# Method 2
# Using loop
reversed_string = ""
for char in s1:
    reversed_string = char + reversed_string

print(
        f"\n\tUsing Loop :\n"
        f"\tReversed String : '{reversed_string}'\n\n"
    )


# 2. Count vowels and consonants in a string

# Predefined string
s2 = "Data Science"
vowels = 0
consonants = 0

for char in s2.lower():
    if char.isalpha():
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1

print(
        f"Count Vowels and Consonants in a String :\n"
        f"Original String : '{s2}'\n"
        f"\n\tVowels : {vowels}\n"
        f"\tConsonants : {consonants}\n\n"
    )


# 3. Remove all spaces from a string

# Predefined string
s3 = "python is easy to learn"

# Method 1
# Using replace()
print(
        f"Remove All Spaces from a String :\n"
        f"Original String : '{s3}'\n"
        f"\n\tUsing replace() :\n"
        f"\tWithout Spaces : '{s3.replace(' ', '')}'\n"
    )

# Method 2
# Using loop
no_space_string = ""
for char in s3:
    if char != " ":
        no_space_string += char

print(
        f"\n\tUsing Loop :\n"
        f"\tWithout Spaces : '{no_space_string}'\n\n"
    )


# 4. Find the longest word in a sentence

# Predefined string
s4 = "python programming builds problem solving skills"
words = s4.split()
longest_word = words[0]

for word in words[1:]:
    if len(word) > len(longest_word):
        longest_word = word

print(
        f"Find the Longest Word in a Sentence :\n"
        f"Original String : '{s4}'\n"
        f"\n\tLongest Word : '{longest_word}'\n"
        f"\tLength : {len(longest_word)}\n\n"
    )


# 5. Capitalize the first letter of each word

# Predefined string
s5 = "welcome to python practice"

# Method 1
# Using title()
print(
        f"Capitalize the First Letter of Each Word :\n"
        f"Original String : '{s5}'\n"
        f"\n\tUsing title() :\n"
        f"\tCapitalized String : '{s5.title()}'\n"
    )

# Method 2
# Using loop
capitalized_words = []
for word in s5.split():
    capitalized_words.append(word[0].upper() + word[1:])

final_string = " ".join(capitalized_words)
print(
        f"\n\tUsing Loop :\n"
        f"\tCapitalized String : '{final_string}'\n"
    )


# 6. Count the number of words in a sentence

# Predefined string
s6 = "python practice makes coding habits stronger"

# Method 1
# Using split() and len()
print(
        f"\nCount the Number of Words in a Sentence :\n"
        f"Original String : '{s6}'\n"
        f"\n\tUsing split() and len() :\n"
        f"\tWord Count : {len(s6.split())}\n"
    )

# Method 2
# Using loop
word_count = 0
for word in s6.split():
    word_count += 1

print(
        f"\n\tUsing Loop :\n"
        f"\tWord Count : {word_count}\n"
    )


# 7. Check whether a string starts and ends with a given character

# Predefined string
s7 = "python"
target_char = "p"
end_char = "n"

# Method 1
# Using indexing
print(
        f"\nCheck Whether a String Starts and Ends with Given Characters :\n"
        f"Original String : '{s7}'\n"
        f"Start Character : '{target_char}'\n"
        f"End Character : '{end_char}'\n"
        f"\n\tUsing Indexing :\n"
        f"\tStarts Correctly : {s7[0] == target_char}\n"
        f"\tEnds Correctly : {s7[-1] == end_char}\n"
    )

# Method 2
# Using startswith() and endswith()
print(
        f"\n\tUsing startswith() and endswith() :\n"
        f"\tStarts Correctly : {s7.startswith(target_char)}\n"
        f"\tEnds Correctly : {s7.endswith(end_char)}\n"
    )
