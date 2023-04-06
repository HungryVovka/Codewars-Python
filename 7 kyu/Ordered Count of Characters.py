# -----------------------------------------------------------
# Count the number of occurrences of each character and return it as a list of tuples in order of appearance. For empty output return an empty list.
# 
# Example:
# 
# ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
# -----------------------------------------------------------

def ordered_count(inp):
    orderedcount = []
    for i in inp:
        if i not in orderedcount:
            orderedcount.append(i)
    return [(j, inp.count(j)) for j in orderedcount]

# or

from collections import Counter

def ordered_count(inp):
    return list(Counter(inp).items())

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