"""
Strings Foundations
    1. Indexing 
        1.1. Print first character 
        1.2. Print last character

    2. Slicing
        2.1 Print first 3 characters 
        2.2 Print last 3 characters 
        
    3. Basic operations
        3.1 Convert string:
                To uppercase
                To lowercase
    
    4. Reverse the string
    
    5. Count the number of characters manually in : text = "python"
        (Without using Buildins)
        
    6. Count no of vowels are in text = "python"   (Without using Buildins)
    
"""

# Predefined String
text = "python"
print(
        f"\n\n\nString Foundations\n"
        f"\nPredefined String : {text}\n"
     )

# 1.1. Print first character (Indexing)
print(
        f"Print first character : {text[0]}\n"
     )

# 1.2. Print last character (Indexing)
print(
        f"Print last character : {text[-1]}\n"
     )

# 2.1 Print first 3 characters (Slicing)
print(
        f"Print first 3 characters : {text[:3]}\n"
     )

# 2.2 Print last 3 characters (Slicing)
print(
        f"Print last 3 characters : {text[-3:]}\n"
     )

# 3. Convert the String to Uppercase
print(
        f"Convert the String to Uppercase : {text.upper()}\n"
     )

# 3. Convert the String to lowercase
print(
        f"Convert the String to Lowercase : {text.lower()}\n"
     )

# 4. Reverse the string
print(
        f"Reverse the String : {text[::-1]}\n"
     )

# 5. Count no of characters in 'text'
characters_count = 0

for character in text:
    characters_count += 1

print(
        f"Count no of characters in variable 'text' : {characters_count}\n"
     )

# 6. Count no of vowels in 'text'
vowels = "AEIOUaeiou"
vowels_count = 0

for characters in text:
    if characters in vowels:
        vowels_count += 1

print(
        f"Count no of vowels in variable 'text' : {vowels_count}\n"
     )