"""
Stings Foundations :

1. Find the 1st character that appears the most times in given Input.
2. Find the first Non-Repeating Character from the given Input
3. check if two strings are Anagram (Among the 2 strings, same characters and same frequency))


"""

# Get a common Input 
user_input = input("\n\nEnter the Input String : ")

# 1. Find the character that appears the most times in given Input.
print(
        f"\n\nTask 1 :\n"
        f"Find the character that appears the most times in given Input :\n"
     )

# Find the  greatest of value from a dictionary by finding the frequency of each Key
my_string = {}

for each_char in user_input:
    if each_char not in my_string:
        my_string[each_char] = 1
    else:
        my_string[each_char] += 1
    
# Find the 1st greatest value and its corresponding key
greatest_count = 0
max_char = ""

for k,v in my_string.items():
    if v > greatest_count:
        greatest_count = v
        max_char = k
        
        
print(
        f"\n\tThe 1st character that appears the most times in given Input is : "
        f"{max_char} which is {greatest_count} times\n"
    )


# 2. Find the first Non-Repeating Character from the given Input

print(
        f"\nTask 2 :\n"
        f"Find the first Non-Repeating Character from the given Input"
     )
found = False
for char in user_input:
    if my_string[char] == 1:
        found = True        
        print(
                f"\n\tThe first Non-Repeating Character from the given Input is : {char}\n"
             )
        break
if found == False:
    print("\nNo non repeating characters\n")
    
# 3. check if two strings are Anagram

# Predefined Strings s1 and s2
s1 = "listen"
s2 = "silent"
  
s1_dict = {}
s2_dict = {}
for char in s1:
    if char not in s1_dict:
        s1_dict[char] = 1
    else:
        s1_dict[char] += 1
        