# -----------------------------------------------------------
# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
# -----------------------------------------------------------

def even_or_odd(number):
    if number % 2 == 0:
        return("Even")
    else:
        return("Odd")

# or

def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

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