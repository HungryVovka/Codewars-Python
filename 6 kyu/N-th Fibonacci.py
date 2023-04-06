# -----------------------------------------------------------
# I love Fibonacci numbers in general, but I must admit I love some more than others.
# 
# I would like for you to write me a function that when given a number (n) returns the n-th number in the Fibonacci Sequence.
# 
# For example:
# 
#    nth_fib(4) == 2
# Because 2 is the 4th number in the Fibonacci Sequence.
# 
# For reference, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two.
# -----------------------------------------------------------

def nth_fib(n):
    fibon = [0, 1]
    i = 0
    while i < n:
        fibon.append(fibon[i] + fibon[i + 1])
        i += 1
    return fibon[n - 1]

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