# Importing the relevant libraries
import matplotlib.pyplot as plt
import numpy as np

# Generating a 1000 normal distribution values to be plotted on the X-axis
x = np.random.normal(size = 1000)
# Generating values from 0-999 to correspond to each value of X
y = np.arange(1000)

# Plotting a scatter plot with appropriate title
plt.scatter(x, y)
plt.title("Scatter plot of normal distribution values")
# Labelling the axes with appropriate names
plt.xlabel("Normal Value")
plt.ylabel("Y Axis")

plt.show()