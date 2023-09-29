# -----------------------------------------------------------
# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
# 
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# 
# For better understanding, please follow the numbers of the next array consecutively:
# 
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
# 
# NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.
# 
# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
# -----------------------------------------------------------

def snail(snail_map):
    answer = []
    while snail_map != []:
        answer.extend(snail_map.pop(0))
        for i in snail_map:
            answer.append(i.pop())
        if snail_map != []:
            answer.extend(snail_map.pop()[::-1])
        for j in range(len(snail_map) - 1, -1, -1):
            answer.append(snail_map[j].pop(0))
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