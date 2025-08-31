# Taking an input for the maximum number of stars in a row
n = int(input("Please enter what you want n to be: "))
# Defining a complement variable to represent the number of stars in a row
a = 1

# Iteratively reducing the whitespaces and increasing stars in each row to print the required pattern
while n >= 1:
    print(" " * (n-1),"*" * a)
    n = n-1
    a = a+1