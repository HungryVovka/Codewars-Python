# -----------------------------------------------------------
# The aim of the kata is to decompose n! (factorial n) into its prime factors.
# 
# Examples:
# 
# n = 12; decomp(12) -> "2^10 * 3^5 * 5^2 * 7 * 11"
# since 12! is divisible by 2 ten times, by 3 five times, by 5 two times and by 7 and 11 only once.
# 
# n = 22; decomp(22) -> "2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19"
# 
# n = 25; decomp(25) -> 2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23
# 
# Prime numbers should be in increasing order. When the exponent of a prime is 1 don't put the exponent.
# 
# Notes
# 
# the function is decomp(n) and should return the decomposition of n! into its prime factors in increasing order of the primes, as a string.
# factorial can be a very big number (4000! has 12674 digits, n can go from 300 to 4000).
# In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use 
# dynamically allocated character strings.
# -----------------------------------------------------------

class PrimeFactors:
    def __init__(self, n):
        self.n = n
        self.primes = self.count_prime_factors(n)
        
    def prime_factors(self, n):
        factors = []
        i = 2
        while i**2 <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors
    
    def count_prime_factors(self, n):
        primes = {}
        for i in range(2, n+1):
            factors = self.prime_factors(i)
            for factor in set(factors):
                count_f = factors.count(factor)
                if factor in primes:
                    primes[factor] += count_f
                else:
                    primes[factor] = count_f
        return primes
    
    def format_decomposition(self):
        decomposition = ""
        for prime, count_f in sorted(self.primes.items()):
            if count_f == 1:
                decomposition += "%d * " % (prime)
            else:
                decomposition += "%d^%d * " % (prime, count_f)
        return decomposition[:-3]
    
    def decompose(self):
        return self.format_decomposition()

def decomp(n):
    return PrimeFactors(n).decompose()

# -----------------------------------------------------------
# License
# Tasks are the property of Codewars (https://www.codewars.com/) 
# and users of this resource.
# 
# All solution code in this repository 
# is the personal property of Vladimir Rukavishnikov
# (vladimirrukavishnikovmail@gmail.com).
# 
# Copyright (C) 2022 Vladimir Rukavishnikov
# 
# This file is part of the HungryVovka/Codewars-Python
# (https://github.com/HungryVovka/Codewars-Python)
# 
# License is GNU General Public License v3.0
# (https://github.com/HungryVovka/Codewars-Python/blob/main/LICENSE.md)
# 
# You should have received a copy of the GNU General Public License v3.0
# along with this code. If not, see http://www.gnu.org/licenses/
# -----------------------------------------------------------