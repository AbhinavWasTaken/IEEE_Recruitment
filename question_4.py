# Importing the required libraries
import numpy as np

# Generating and printing random 5x5 array with entries being integers from 0-100
a = np.random.randint(101, size=(5,5))
print(a)

# Defining and printing a 3x3 matrix within 5x5 matrix whos rows/columns are bounded between the 2nd and 4th rows/columns respectively
b = a[1:4,1:4]
print("extracted 3x3 matrix is:\n", b)

# Calculating and printing the dot product of the first row/last column of 3x3 matrix
print("The dot product required is: ", np.dot(b[0,:], b[:,2]))