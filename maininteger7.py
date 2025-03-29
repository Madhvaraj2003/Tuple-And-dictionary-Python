from collections import Counter                # Imported the counter function from library.
def first_non_repeating(numbers):              # Created a function called first non repeating().
    count = Counter(numbers)  # Used count variable for to store numbers.
    result = [num for num in numbers if count[num] == 1] # Iterates all the numbers to find the non-repeating integer.
    return result            # Calling the function.
numbers = (5, 7, 8, 9, 10, 10, 9, 3, 66, 23, 5, 7) # Declared numbers.
print("Non Repeating Elements: ", first_non_repeating(numbers))
# Used to print the Output.