# -----------------------------------------------------------
# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
# 
# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# 
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!
# -----------------------------------------------------------

def create_phone_number(n):
    arr_n = [str(i) for i in n]
    str_n = "".join(arr_n)
    return f"({str_n[:3]}) {str_n[3:6]}-{str_n[6:]}"

# or

def create_phone_number(n):
    number = "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
    return number

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