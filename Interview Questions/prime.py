"""
This code defines a function `is_prime` that checks if a given number is prime. A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers. The function first checks if the number is less than or equal to 1, in which case it returns False. Then, it iterates from 2 to the square root of the number (inclusive) and checks if the number is divisible by any of those integers. If it finds any divisor, it returns False, indicating that the number is not prime. If no divisors are found, it returns True, indicating that the number is prime.
"""

# The efficient code
def is_prime(num):
    if num <= 1:
        return False
        
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# The near efficient way without checking up to the square root

def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False
 
    # Loop through all the numbers between 2 and the number
    for i in range(2, num):
        # Check if the number (num) can be divided by the potential prime number
        if num % i == 0:
            return False
 
    # this return is outside the for loop which will only run once the loop finishes and none of the numbers are divisible. Therefore it is prime.
    return True
    