numbers = int(input("Enter numbers: ")) # Accepting number from the user.
firstdigit = numbers                    # Created a variable to store  the first digit.
lastdigit = numbers % 10                # Created variable to store the last digit and to find the last digit.
while firstdigit > 9 :                  # while loop to find the first digit.
    firstdigit = firstdigit // 10
Sum = firstdigit + lastdigit            # Created a new variable and finding the sum of the first and last digit.
print(Sum)                              # Used to print the sum