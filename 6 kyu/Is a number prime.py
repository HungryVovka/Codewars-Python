# -----------------------------------------------------------
# Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.
# 
# Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
# 
# Requirements
# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
# NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 ( or 
# , depending on language ). Looping all the way up to n, or n/2, will be too slow.
# 
# Example
# is_prime(1)  /* false */
# is_prime(2)  /* true  */
# is_prime(-1) /* false */
# -----------------------------------------------------------

def is_prime(num):
    if num == 2 or num == 3: 
        return True
    if num % 2 == 0 or num < 2: 
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# or

import math

def is_prime(num):
    if num < 2:
        return False
    numsq = math.sqrt(num)
    i = 2
    while i <= numsq:
        if num % i == 0:
            return False
        i += 1
    return True

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