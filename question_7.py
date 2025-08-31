# Defining two arbitrary lists
list1 = [3, 4, 5, 1, 4, 6, 1, 7, 7] 
list2 = [5, 8, 2, 9, 9, 4, 6, 3]

#Converting them into sets to remove repeating elements
set1 = set(list1)
set2 = set(list2)

#Creating an empty set to add the common elements into
intersection_set = set()

#Adding in common elements through a loop
for x in set1 & set2:
    intersection_set.add(x)

#Printing the final set
print("The intersection of list 1 and list 2 is:\n", intersection_set)