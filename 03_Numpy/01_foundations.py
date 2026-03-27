"""
Create a NumPy array from: [1, 2, 3, 4, 5]
Then:
    1. Multiply each element by 2
    2. Subtract 1 from the result
"""

import numpy as np

# Predefined list
print(
        f"\n\nCreate a NumPy array from a list: [1, 2, 3, 4, 5]. Then:\n"
        f"\t1. Multiply each element by 2.\n"
        f"\t2. Subtract 1 from the result.\n"
    )

my_list = [1, 2, 3, 4, 5]
print(
        f"\n\nPredefined List : {my_list}\n"
        f"\tType : {type(my_list)}\n"
    )

# Create a numpy array from a predefined List
my_array = np.array(my_list)
print(
        f"\nNumpy array is : {my_array}\n"
        f"\tType : {type(my_array)}\n"
        f"\tShape : {my_array.shape}\n"
        f"\tDimension : {my_array.ndim}\n"
    )   

# Multiply each element by 2 and Subtract 1 from the result.
result = my_array * 2 - 1
print(
        f"\nMultiply each element by 2 and Subtract 1 from the result :\n"
        f"\t Result is : {result}\n"
)