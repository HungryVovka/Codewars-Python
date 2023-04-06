# -----------------------------------------------------------
# There is a string of 32 alphanumeric characters hidden inside a dynamically generated function, which will then be passed into your function.
# 
# Your task is to recover this string and return it.
# -----------------------------------------------------------

def find_the_secret(f):
    a, b = f.__code__.co_consts
    return b

# or

def find_the_secret(f):
    return f.__code__.co_consts[1]

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