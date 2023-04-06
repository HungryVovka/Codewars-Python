# -----------------------------------------------------------
# This Kata is intended as a small challenge for my students
# 
# All Star Code Challenge #18
# 
# Create a function that accepts 2 string arguments and returns an integer of the count of occurrences the 2nd argument is found in the first one.
# 
# If no occurrences can be found, a count of 0 should be returned.
# 
# ("Hello", "o")  ==>  1
# ("Hello", "l")  ==>  2
# ("", "z")       ==>  0
# 
# Notes:
# 
# The first argument can be an empty string
# The second string argument will always be of length 1
# -----------------------------------------------------------

def str_count(strng, letter):
    return len(strng.split(letter)) - 1

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