# -----------------------------------------------------------
# Give the summation of all even numbers in a Fibonacci sequence up to, but not including, the number passed to your function. Or, in other words, 
# sum all the even Fibonacci numbers that are lower than the given number n (n is not the nth element of Fibonacci sequence) without including n.
# 
# The Fibonacci sequence is a series of numbers where the next value is the addition of the previous two values. The series starts with 0 and 1:
# 
# 0 1 1 2 3 5 8 13 21...
# 
# For example:
# 
# eve_fib(0)==0
# eve_fib(33)==10
# eve_fib(25997544)==19544084
# -----------------------------------------------------------

def even_fib(n):
    a, b = 0, 1
    even_fib_sum = 0
    while b < n:
        if b % 2 == 0:
            even_fib_sum += b
        a, b = b, (a + b)
    return even_fib_sum

# or

def even_fib(n, a=0, b=1, even_fib_sum=0):
    if b >= n:
        return even_fib_sum
    if b % 2 == 0:
        even_fib_sum += b
    return even_fib(n, b, (a + b), even_fib_sum)

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