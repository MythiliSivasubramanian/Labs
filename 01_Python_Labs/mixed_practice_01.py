"""
Given a predefined List nums,
Create a new list that contains only even numbers, 
but each number should be multiplied by 10.

"""
print(
        f"\n\nTask 1 :"
        f"\nGiven a predefined List nums :\n"
        f"\t1. Create a new list that contains only even numbers,\n"
        f"\t2. And each number should be multiplied by 10."
    )

# Predefined List
nums = [3, 7, 2, 9, 4, 6, 1]
print(f"\nPredefined List nums : {nums}")

# List with even numbers only
new_list = [num * 10 for num in nums if num % 2 == 0]
print(f"\nList with only even numbers and those are multiplied by 10 : "
      f"\n{new_list}\n\n")


"""
Given a predefined list of fruits, Create a new list that contains:
    1. ONLY words with length greater than 5
    2. Convert them to UPPERCASE

"""

print(
        f"\n\nTask 2 :"
        f"\nGiven a predefined list of fruits, Create a new list that contains:\n"
        f"\t1. ONLY words with length greater than 5\n"
        f"\t2. Convert them to UPPERCASE"
    )
    
# Predefined list of fruits 
words = ["apple", "banana", "cherry", "kiwi", "grape"]
print(f"\nPredefined List of words : {words}")

final_words = [word.upper() for word in words if len(word) > 5]

print(f"\nList with words greater than 5 & in upper case : {final_words}\n\n")

"""
Given a predfined dictionary, create a new dictionary that contains:
    1. ONLY students with marks >= 50  
    2. Increase their marks by 5 but maximum mark is 100

"""

print(
         f"\n\nTask 3 :"
        f"\nGiven a predfined dictionary, create a new dict that contains:\n"
        f"\t1. ONLY students with marks >= 50\n"
        f"\t2. Increase their marks by 5 but maximum mark is 100"
)
# predefined Dictionary
students = { "Alice": 85, "Bob": 42, "Charlie": 73, "David": 30, "Eve": 100 }
print(f"\nPredefined students dictionary : {students}")


passed_students = {name : min(mark + 5, 100) for name,mark in  students.items() if mark >= 50}

print(f"\nStudents with marks >= 50 and such marks added by 5 marks but maximum mark is 100: {passed_students}\n\n")
