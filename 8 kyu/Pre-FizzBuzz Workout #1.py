# -----------------------------------------------------------
# This is the first step to understanding FizzBuzz.
# 
# Your inputs: a positive integer, n, greater than or equal to one. n is provided, you have NO CONTROL over its value.
# 
# Your expected output is an array of positive integers from 1 to n (inclusive).
# 
# Your job is to write an algorithm that gets you from the input to the output.
# -----------------------------------------------------------

def pre_fizz(n):
    return [1 + x for x in range(n)]

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