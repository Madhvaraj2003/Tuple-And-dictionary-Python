# Created a array list.
Array = [1, 2, 3, 4, 5]                #
n = 2      # Declared a variable to rotate a list.
rotated_list = Array[n:] + Array[:-n]  # making the array list to rotate.
print("Rotated List Is: ", rotated_list)  # printing the array list.
print("Minimum Value in Rotated List Is", min(rotated_list)) # Finding the minimum element in the rotated array list.
