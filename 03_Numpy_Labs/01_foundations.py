"""
Numpy foundations:

Predefined list my_list = [1, 2, 3, 4, 5].

Task 1. Create a 1D NumPy array from predefined List
        Then:
            1. Multiply each element by 2.
            2. Subtract 1 from the result.
            
Task 2. Create a 2D array from the predefined List
        Method 1 : Safe (without changing actual list) using Row or column vector (5, 1) and (1, 5)
        Method 2 : Append actual list to match the len(list) = 2 * 3 or 3 * 2

"""

import numpy as np

# Predefined list
print(
        f"\n\nCreate a 1D NumPy array from a list: [1, 2, 3, 4, 5]. Then:\n"
        f"\t1. Multiply each element by 2.\n"
        f"\t2. Subtract 1 from the result.\n"
    )

my_list = [1, 2, 3, 4, 5]
print(
        f"\n\nPredefined List : {my_list}\n"
        f"\tType : {type(my_list)}\n"
    )

# Create a numpy array from a predefined List
one_d_array = np.array(my_list)
print(
        f"\nNumpy array is : {one_d_array}\n"
        f"\tType : {type(one_d_array)}\n"
        f"\tShape : {one_d_array.shape}\n"
        f"\tDimension : {one_d_array.ndim}\n"
    )   

# Multiply each element by 2 and Subtract 1 from the result.
result = one_d_array * 2 - 1
print(
        f"\nMultiply each element by 2 and Subtract 1 from the result :\n"
        f"\t Result is : {result}\n"
)

# Task 2 : Create a 2D array from the predefined list my_list  = [1, 2, 3, 4, 5]
"""
The length of the list is 5.

A 2D array requires rows and columns. Common reshape options such as
(2, 3) or (3, 2) needs 6 elements but len of list is 5.

Approaches:
1. Safe method with no change to the original list:
   reshape to (5, 1) as a column vector or (1, 5) as a row vector.
2. Append one element to the list and then reshape it to a 2D array.
"""
print(
        f"\n\nTask 2 :\n"
        f"Create a 2D array from the predefined list my_list  = [1, 2, 3, 4, 5]"
    )


# Method 1:
"""
Method 1: Safe approach with no change to the original list.

Reshape into:
- (5, 1) for a column vector or
- (1, 5) for a row vector
"""
two_d_array_1 = np.array(my_list).reshape(5,1)
print(
        f"\n\nMethod 1:\n"
        f"\tReshape into:   (5,1) : Column vector or (1,5) : Row vector :\n"
        f"2d Array is :\n{two_d_array_1}\n"
        f"Shape is : {two_d_array_1.shape}\n"
        f"Dim is : {two_d_array_1.ndim}\n"
        
    )

# Method 2
# Append an element to list to match len(list) = reshape(2 * 3) or .reshape(3 * 2) 
my_list.append(6)

two_d_array_2 = np.array(my_list).reshape(2,3)
print(
        f"\n\nMethod 2:\n"
        f"\tAppending an element to list and then reshape :\n"
        f"2d Array is :\n{two_d_array_2}\n"
        f"Shape is : {two_d_array_2.shape}\n"
        f"Dim is : {two_d_array_2.ndim}\n"
        
    )

