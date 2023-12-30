# -----------------------------------------------------------
# Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make 
# this happen, he needs your help.
# 
# Task
# You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be 
# removed, and every line must be terminated with a newline character (\n).
# 
# Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.
# 
# Examples
# A size 3 diamond:
# 
#  *
# ***
#  *
# 
# ...which would appear as a string of " *\n***\n *\n"
# 
# A size 5 diamond:
# 
#   *
#  ***
# *****
#  ***
#   *
# 
# ...that is:
# 
# "  *\n ***\n*****\n ***\n  *\n"
# -----------------------------------------------------------

def diamond(n):
    if n < 1 or n % 2 == 0:
        return None
    diamond = ""
    i = 0
    while i < n:
        spaces_num = abs((n - 1) // 2 - i)
        spaces = " " * spaces_num
        stars = "*" * (n - 2 * spaces_num)
        diamond += f"{spaces}{stars}\n"
        i += 1
    return diamond

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