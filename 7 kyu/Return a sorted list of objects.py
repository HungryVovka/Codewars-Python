# -----------------------------------------------------------
# You'll be passed an array of objects (list) - you must sort them in descending order based on the value of the specified property (sortBy).
# 
# Example
# When sorted by "a", this:
# 
# [
#   {"a": 1, "b": 3},
#   {"a": 3, "b": 2},
#   {"a": 2, "b": 40},
#   {"a": 4, "b": 12}
# ]
# 
# should return:
# 
# [
#   {"a": 4, "b": 12},
#   {"a": 3, "b": 2},
#   {"a": 2, "b": 40},
#   {"a": 1, "b": 3}
# ]
# 
# The values will always be numbers, and the properties will always exist.
# -----------------------------------------------------------

def sort_list(sort_by, lst):
    k = lambda x: x[sort_by]
    return sorted(lst, key = k, reverse = True)

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