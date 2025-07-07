# -----------------------------------------------------------
# #Bubbleing around
# 
# Since everybody hates chaos and loves sorted lists we should implement some more sorting algorithms. Your task is to implement a Bubble sort 
# (for some help look at https://en.wikipedia.org/wiki/Bubble_sort) and return a list of snapshots after each change of the initial list.
# 
# e.g.
# 
# If the initial list would be l=[1,2,4,3] my algorithm rotates l[2] and l[3] and after that it adds [1,2,3,4] to the result, which is a list of snapshots.
# 
# [1,2,4,3] should return [ [1,2,3,4] ]
# [2,1,4,3] should return [ [1,2,4,3], [1,2,3,4] ]
# [1,2,3,4] should return []
# -----------------------------------------------------------

def bubble(lst):
    answer = [] 
    n = len(lst)
    i, k = 0, 0
    while i < (n - 1):
        j = 0
        while j < (n - 1 - i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                answer.insert(k, lst[:])
                k += 1
            j += 1
        i += 1
    return answer

# -----------------------------------------------------------
# License
# Tasks are the property of Codewars (https://www.codewars.com/) 
# and users of this resource.
# 
# All solution code in this repository 
# is the personal property of Vladimir Rukavishnikov
# (vladimirrukavishnikovmail@gmail.com).
# 
# Copyright (C) 2025 Vladimir Rukavishnikov
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