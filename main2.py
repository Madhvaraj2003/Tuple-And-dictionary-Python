def prime_num (n):                                 # Created the function of Prime_num(n).
    for i in range(2,n):                           # Used for  to  find the number is prime or not.
        if n%i==0:
            return False
    return True
numbers = [10, 501, 22, 37, 100, 997, 87, 351]    # Created the list of numbers.
for number in numbers:                            # Used for loop to get the prime numbers.
    if prime_num(number):
        print("Prime numbers:", number)           # Used to display the prime numbers.