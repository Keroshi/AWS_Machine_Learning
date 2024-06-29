import numpy as np

# Create an array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Select elements greater than 5
result = sum((array[array > 5])*5)

print("Original array:", array)
print("Elements greater than 5:", result)
