# -----------------------------------------------------------
# Create a function that accepts two parameters. The first will be a list of ages. The second parameter will be a string that can be one of the following 
# values: asc, desc, and none.
# 
# If the second parameter is “asc,” then the function should return a list with the numbers in ascending order. If it’s “desc,” then the list should be in 
# descending order, and if it’s “none,” it should return the original list unaltered.
# -----------------------------------------------------------

# Can you figure out who would be the youngest 
# or the oldest friend in your frind group?
# good luck
def sorted_out(ages, sorting_order):
    if sorting_order == "asc":
        return sorted(ages)
    elif sorting_order == "desc":
        return sorted(ages)[::-1]
    else:
        return ages

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