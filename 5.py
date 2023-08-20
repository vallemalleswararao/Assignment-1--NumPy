import numpy as np

# Create a 10x10 array with random values between 0 and 1
my_array = np.random.rand(10, 10)

# Find the minimum and maximum values in the array
min_value = my_array.min()
max_value = my_array.max()

print("Minimum value:", min_value)
print("Maximum value:", max_value)
