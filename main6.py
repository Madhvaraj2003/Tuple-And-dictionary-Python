list1 = [1, 246, 3, 44, 5, 9]                           # Declared the three list.
list2 = [1, 424, 30, 44, 5, 62]
list3 = [12, 246, 3, 4, 56, 9]
set1 = set(list1)                                       # Here we are converting the list into set.
set2 = set(list2)
set3 = set(list3)
print("Duplicate elements")                             # printing the duplicate elements.
print(set1.intersection(set2),set1.intersection(set3))  # Performing the intersection operation to find the duplicate elements.
print(" After removing the duplicate elements")         # Printing the elements which are unique.
union = set1 | set2 | set3                              # Used to find unique elements in the set.
print(union)