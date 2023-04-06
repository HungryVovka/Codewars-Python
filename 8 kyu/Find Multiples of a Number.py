# -----------------------------------------------------------
# In this simple exercise, you will build a program that takes a value, integer , and returns a list of its multiples up to another value, limit . If limit 
# is a multiple of integer, it should be included as well. There will only ever be positive integers passed into the function, not consisting of 0. The limit 
# will always be higher than the base.
# 
# For example, if the parameters passed are (2, 6), the function should return [2, 4, 6] as 2, 4, and 6 are the multiples of 2 up to 6.
# 
# If you can, try writing it in only one line of code.
# -----------------------------------------------------------

def find_multiples(integer, limit):
    answer = []
    count = int(limit / integer)
    while count != 0:
        answer.insert(0, integer * count)
        count -= 1
    return(answer)

# or

def find_multiples(integer, limit):
    return list(range(integer, limit + 1, integer))

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