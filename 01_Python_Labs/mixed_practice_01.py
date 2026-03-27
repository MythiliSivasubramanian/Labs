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
Task 4 :
List is mutable, changble in place. 
In below code, whenever the car name starts with T, then it is poped. 
pop shrinks the list during iteration
Hence will result in Index out of range error since some items starting with t is popped.
"""

print(
        f"\n\nTask 4 : \n"
        f"List is mutable, changable in place." 
        f"\nIn below code, whenever the car name starts with T, then it is poped." 
        f"\nso the length of the loop is reduced whenever the item is poped."
        f"\nHence will result in Index out of range error since some items starting with t is popped."
    )


cars = ["Audi", "Toyota", "Tesla", "BMW"]
print(f"\npredefined List cars {cars}")

try:
    for i in range(len(cars)):
        if cars[i].startswith("T"):
            cars.pop(i)
    print(cars)
except IndexError as e:
    print(f"Resulted in error : {e}")
    
    
    
"""
Alternative method for accomplishing Task 4 
    1. Using List comprehension
    2. Creating a copy of lists
"""

#     1. Using List comprehension

print(
        f"\nAlternative method for accomplishing Task 4 : \n"
        f"\t1. Using List comprehension\n"
    )

cars = [car for car in cars if not car.startswith("T")]

print(f"Lists without car names starting with 'T' : {cars}")

#  2. Creating a copy of lists
print(
        f"\nAlternative method for accomplishing Task 4 : \n"
        f"\t2. Creating a copy of lists\n"
    )


for car in cars[:]:  # copy
    if car.startswith("T"):
        cars.remove(car)
print(f"Lists without car names starting with 'T' : {cars}")

"""
Given an predefined list of numbers, create a set that contains:

    1.ONLY numbers greater than 3
    2.Each number should be squared

"""

# Predefined list of numbers
nums_1 = [1, 2, 2, 3, 4, 4, 5, 6, 6]

print(
        f"\n\nTask 4 : \n"
        f"Given an predefined list of numbers, create a set that contains :\n" 
        f"\t1.ONLY numbers greater than 3\n" 
        f"\t2.Each number should be squared \n"
        
    )
print(f"\npredefined List of numbers {nums_1}")

# Set comprehension using {}
my_set = {number ** 2 for number in nums_1 if number > 3}
print(f"\nSet of numbers greater than 3 and square of it is : {my_set}\n\n")
