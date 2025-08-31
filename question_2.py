# Taking a paragraph of words as input and splitting it into a list of each word in the paragraph
a = input("Please enter a string of text: ").split()
# Defining a variable as a counter for number of palindromes
palindrome = 0

# Iteratively checking if each word in the list is a palindrome or not
for x in a:
    # Breaking each word into a list of its letters
    b = list(x)
    # Number of letters in each word to have separate cases for words with even/odd number of letters
    n = len(b)
    
    # For Even
    if n % 2 == 0:
        n = n/2
        
        # Loop within a loop to individually check if a letter and its complement match (condition for a word being palindromic)
        while n >= 1:
            if b[int(n-1)] != b[int(-n)]:
                break
            else:
                n = n-1
        # Increasing the counter if the word was a palindrome
        if n == 0:
            palindrome = palindrome + 1
            print(x, " ", "is a palindrome!")

    # For Odd       
    elif n % 2 == 1:
        n = (n-1)/2

        # Loop within a loop to individually check if a letter and its complement match (condition for a word being palindromic)
        while n >= 1:
            if b[int(n-1)] != b[int(-n)]:
                break
            else:
                n = n-1
        # Increasing the counter if the word was a palindrome
        if n == 0: 
            palindrome = palindrome + 1
            print(x, "is a palindrome!")

# Printing the final value of the palindrome counter
print("The total number of palindromes in the text is: ", palindrome)
