import numpy as np

arr = np.array([1, 3, 2, 7, 5])  # Create a NumPy array
n = 2  # Specify the number of maximum values to find

# Get indices of n maximum values
indices = np.argsort(arr)[-n:]  # Sort the array, get the last n elements (largest values)

print(indices)  # Output the indices of the two largest values


######################################################