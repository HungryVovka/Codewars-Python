# -----------------------------------------------------------
# Combine strings function
# Create a function named (combine_names) that accepts two parameters (first and last name). The function should return the full name.
# 
# Example:
# 
# combine_names('James', 'Stevens')
# 
# returns:
# 
# 'James Stevens'
# -----------------------------------------------------------

def combine_names(first, second):
    return first + " " + second

# or

def combine_names(*args):
    return " ".join(args)

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