# -----------------------------------------------------------
# An integer partition of n is a weakly decreasing list of positive integers which sum to n.
# 
# For example, there are 7 integer partitions of 5:
# 
# [5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1].
# Write a function which returns the number of integer partitions of n. The function should be able to find the number of integer partitions of n for 
# n at least as large as 100.
# -----------------------------------------------------------

def partitions(n):
    partit = [[1] * (n + 1)]
    for i in range(1, n + 1):
        partit.append([0])
        for j in range(1, i + 1):
            if j > i - j:
                k = partit[i - j][i - j]
            else:
                k = partit[i - j][j]
            partit[i].append(partit[i][j - 1] + k)
    return partit[n][n]

# or

def partitions(n):
    partit = [1] + [0] * n
    for a in range(1, n + 1):
        for b, c in enumerate(range(a, n + 1)):
            partit[c] += partit[b]
    return partit[n]

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