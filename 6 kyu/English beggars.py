# -----------------------------------------------------------
# Born a misinterpretation of this kata, your task here is pretty simple: given an array of values and an amount of beggars, you are supposed to return 
# an array with the sum of what each beggar brings home, assuming they all take regular turns, from the first to the last.
# 
# For example: [1,2,3,4,5] for 2 beggars will return a result of [9,6], as the first one takes [1,3,5], the second collects [2,4].
# 
# The same array with 3 beggars would have in turn have produced a better out come for the second beggar: [5,7,3], as they will respectively take 
# [1,4], [2,5] and [3].
# 
# Also note that not all beggars have to take the same amount of "offers", meaning that the length of the array is not necessarily a multiple of n; 
# length can be even shorter, in which case the last beggars will of course take nothing (0).
# 
# Note: in case you don't get why this kata is about English beggars, then you are not familiar on how religiously queues are taken in the kingdom ;)
# 
# Note 2: do not modify the input array.
# -----------------------------------------------------------

def beggars(values, n):
    sumbeg = {}
    for i in range(n):
        j = 0
        for k in values:
            if sumbeg.get(i):
                sumbeg[i] += sum(values[i + j:i + j+ 1])
            else:
                sumbeg[i] = sum(values[i + j:i + j + 1])
            j += n
    return list(sumbeg.values())

# or

def beggars(values, n):
    if n == 0:
        return []
    return [sum(values[x::n]) for x in range(n)]

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