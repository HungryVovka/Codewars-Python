# -----------------------------------------------------------
# How many ways can you make the sum of a number?
# From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)#
# 
# In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive 
# integers. Two sums that differ only in the order of their summands are considered the same partition. If order matters, the sum becomes a 
# composition. For example, 4 can be partitioned in five distinct ways:
# 
# 4
# 3 + 1
# 2 + 2
# 2 + 1 + 1
# 1 + 1 + 1 + 1
# 
# Examples
# 
# Basic
# exp_sum(1) # 1
# exp_sum(2) # 2  -> 1+1 , 2
# exp_sum(3) # 3 -> 1+1+1, 1+2, 3
# exp_sum(4) # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
# exp_sum(5) # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3
# 
# exp_sum(10) # 42
# 
# Explosive
# 
# exp_sum(50) # 204226
# exp_sum(80) # 15796476
# exp_sum(100) # 190569292
# 
# See here (http://www.numericana.com/data/partition.htm) for more examples.
# -----------------------------------------------------------

def exp_sum(n):
    if n < 0:
        return 0
    esum = [1] + [0]*n
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            esum[j] += esum[j - i]
    return esum[-1]

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