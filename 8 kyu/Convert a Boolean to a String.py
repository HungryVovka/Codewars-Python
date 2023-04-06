# -----------------------------------------------------------
# Implement a function which convert the given boolean value into its string representation.
# 
# Note: Only valid inputs will be given.
# -----------------------------------------------------------

def boolean_to_string(b):
    if b == True:
        return("True")
    if b == False:
        return("False")

# or

def boolean_to_string(b):
    return "True" if b == True else "False"

# or

def boolean_to_string(b):
    return str(b)

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