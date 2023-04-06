# -----------------------------------------------------------
# Create a method each_cons that accepts a list and a number n, and returns cascading subsets of the list of size n, like so:
# 
# each_cons([1,2,3,4], 2)
#   #=> [[1,2], [2,3], [3,4]]
# 
# each_cons([1,2,3,4], 3)
#   #=> [[1,2,3],[2,3,4]]
#   
# As you can see, the lists are cascading; ie, they overlap, but never out of order.
# -----------------------------------------------------------

def each_cons(lst, n):
    arr = []
    for i in range(len(lst) - n + 1):
        arr.append(lst[i: i + n])
    return arr

# or

each_cons = lambda lst, n: [lst[i : i + n] for i, j in enumerate(lst[n - 1:])]

# or

def each_cons(lst, n):
    return list(lst[i : i + n] for i, j in enumerate(lst[n - 1:]))

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