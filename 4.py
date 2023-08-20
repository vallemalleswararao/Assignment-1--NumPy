import numpy as np

# Create the array
my_array = np.array([1, 2, 0, 0, 4, 0])

# Find the indices of non-zero elements
non_zero_indices = np.nonzero(my_array)

print(non_zero_indices)
