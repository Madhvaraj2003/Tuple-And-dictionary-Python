# Defined the numbers in a variable called Numbers.
Numbers = [4, 2, -3, 1, 6]
for i in range(len(Numbers)): # Using the for loop to find the length of the numbers.
    sum_sublist = 0           # The sublist stars from the zero.
    for j in range (i, len(Numbers)): #  Declared For loop to find the sublist.
            print(f" sub list exists {Numbers}, The Sub Lists are {Numbers[i:j+1]}")
            # To print the  sub list.
