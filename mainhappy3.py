# used function to pass an argument N.
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen : # While loop to find the happy numbers.
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1
# created a Variable called numbers.
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
happy_count = 0      # Numbers Count will start from zero.
for num in numbers:  # For loop to find the happy number from above list.
    if is_happy(num):
        print(f"{num} is  a Happy Number")
        happy_count += 1    # counting The happy numbers.
print(f"Total Happy Numbers are {happy_count}")

