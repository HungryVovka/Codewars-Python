# -----------------------------------------------------------
# A prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
# 
# You will be given the lower and upper limits: the program will look for any prime number that exists between the lower limit to the upper limit 
# (included).
# 
# Your objective is to sum all the primes between the given limits.
# 
# If the limits are primes, then they are included
# 
# -100000 <= lower < upper <= 100000
# 
# If lower is greater than upper, it should return 0
# 
# Example
# You are given a lower limit of 4 and an upper limit of 20.
# 
# So the prime numbers from 4 to 20 will be: 5, 7, 11, 13, 17, 19
# 
# and if you add them up, the result will be 72.
# 
# sum_primes(4, 20) = 72  # 5 + 7 + 11 + 13 + 17 + 19 = 72
# 
# sum_primes(20, 4) = 0  # since lower is greater than upper
# 
# sum_primes(2, 7) = 17  # 2 + 3 + 5 + 7 = 17
# 
# sum_primes(11, 11) = 11  # it consists of one prime number
# 
# sum_primes(60, 60) = 0  # since 60 is not a prime number
# -----------------------------------------------------------

def prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def sum_primes(lower, upper):
    y = [x for x in range(lower, upper + 1) if prime(x)]
    return sum(y)

# or

import gmpy2

def sum_primes(lower, upper):
    x = gmpy2.next_prime(lower - 1)
    y = 0
    while x <= upper:
        y += x
        x = gmpy2.next_prime(x)
    return y