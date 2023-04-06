# -----------------------------------------------------------
# Please write a function that sums a list, but ignores any duplicate items in the list.
# 
# For instance, for the list [3, 4, 3, 6] , the function should return 10.
# -----------------------------------------------------------

def sum_no_duplicates(l):
    arr = []
    for i in l:
        if l.count(i) == 1:
            arr.append(i)
    return sum(arr)

# or

def sum_no_duplicates(l):
    return sum(i for i in l if l.count(i) == 1)

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