# -----------------------------------------------------------
# This is a rather simple but interesting kata. Try to solve it using logic. The shortest solution can be fit into one line.
# 
# Task
# The point is that a natural number N (1 <= N <= 10^9) is given. You need to write a function which finds the number of natural numbers not 
# exceeding N and not divided by any of the numbers [2, 3, 5].
# 
# Example
# Let's take the number 5 as an example:
# 
# 1 - doesn't divide integer by 2, 3, and 5
# 2 - divides integer by 2
# 3 - divides integer by 3
# 4 - divides integer by 2
# 5 - divides integer by 5
# Answer: 1
# 
# because only one number doesn't divide integer by any of 2, 3, 5
# 
# Note
# Again, try to think of a formula that will shorten your solution and help you pass big tests.
# 
# Good luck :)
# -----------------------------------------------------------

def real_numbers(n):
    a = n // 2
    b = n // 3
    c = n // 5
    ab = n // 6
    ac = n // 10
    bc = n // 15
    abc = n // 30
    return n - (a + b + c) + (ab + ac + bc) - abc

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