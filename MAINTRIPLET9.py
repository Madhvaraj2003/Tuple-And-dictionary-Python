# Created a list .
list = [10, 20, 30, 9]
res = 59
for i in range(len(list) - 2):      # Used To find the triplet of the 59.
     for j in range(i + 1, len(list) - 1):         # Used loop to find the triplet from the list.
        for k in range(j + 1, len(list)):
            if list[i] + list[j] + list[k] == res:
                print(f"The Triplet of 59 is, {list[i]}, {list[j]}, {list[k]}")  # Used to display the output.