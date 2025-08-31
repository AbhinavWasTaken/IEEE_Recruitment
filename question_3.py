# Importing the required libraries
import numpy as np

# Generating and printing a random 5x5 array with entries being integers from 0-100
a = np.random.randint(101, size=(5,5))
print(a)
# Printing the mean, maximum and minimum value of all entries in the 5x5 matrix
print("The mean is: ", a.mean())
print("The maximum value in the array is: ", a.max())
print("The minimum value in the array is: ", a.min())

# Defining and printing a normalized matrix using a formula to normalize all elements of the 5x5 matrix to between values of 0 and 1
a_normalized = (a-a.min()) / (a.max()-a.min())
print("The normalized matrix of a is:\n", a_normalized)

# Flattening and sorting the original 5x5 matrix
a_flatten = a.flatten()
print("The 1D flattened and sorted array is:\n", np.sort(a_flatten))