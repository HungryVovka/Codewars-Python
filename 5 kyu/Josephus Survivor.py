# -----------------------------------------------------------
# In this kata you have to correctly return who is the "survivor", ie: the last element of a Josephus permutation.
# 
# Basically you have to assume that n people are put into a circle and that they are eliminated in steps of k elements, like this:
# 
# n=7, k=3 => means 7 people in a circle
# one every 3 is eliminated until one remains
# [1,2,3,4,5,6,7] - initial sequence
# [1,2,4,5,6,7] => 3 is counted out
# [1,2,4,5,7] => 6 is counted out
# [1,4,5,7] => 2 is counted out
# [1,4,5] => 7 is counted out
# [1,4] => 5 is counted out
# [4] => 1 counted out, 4 is the last element - the survivor!
# 
# The above link about the "base" kata description will give you a more thorough insight about the origin of this kind of permutation, but basically 
# that's all that there is to know to solve this kata.
# 
# Notes and tips: using the solution to the other kata to check your function may be helpful, but as much larger numbers will be used, using an 
# array/list to compute the number of the survivor may be too slow; you may assume that both n and k will always be >=1.
# -----------------------------------------------------------

def josephus_survivor(n, k):
    survivors = [i for i in range(1, n+1)]
    j = 0
    while len(survivors) > 1:
        j = (j + k - 1) % len(survivors)
        del survivors[j]
    return survivors[0]

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