"""
Given a predefined List nums,
Create a new list that contains only even numbers, 
but each number should be multiplied by 10.

"""
# Predefined List
nums = [3, 7, 2, 9, 4, 6, 1]
print(f"\n\nPredefined List nums : {nums}\n")

# List with even numbers only
new_list = [num * 10 for num in nums if num % 2 == 0]
print(f"\nList with only even numbers and those are multiplied by 10 : "
      f"\n{new_list}\n\n")