# -----------------------------------------------------------
# We need a simple function that determines if a plural is needed or not. It should take a number, and return true if a plural should be used with that 
# number or false if not. This would be useful when printing out a string such as 5 minutes, 14 apples, or 1 sun.
# 
# You only need to worry about english grammar rules for this kata, where anything that isn't singular (one of something), it is plural (not one of 
# something).
# 
# All values will be positive integers or floats, or zero.
# -----------------------------------------------------------

def plural(n):
    return n != 1

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