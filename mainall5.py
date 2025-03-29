target = 10          # Declared a variable with value 10.
for ten in range(2): # For loop iterate through all the numbers.
    for five in  range((target - ten * 10 // 2) // 5 + 1):  # Finding the combination of five.
        for two in range((target - ten * 10 // 2 - five * 5) // 2 + 1): # Finding the combination of two.
            one = target - ten * 10 + five * 5 + two * 2
            print(f" 10x THE COMBINATION IS  {ten}, 5x {five}, 2x {two}, 1x {one}")
            # To display the combination using print.