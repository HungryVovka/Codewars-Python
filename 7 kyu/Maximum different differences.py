# -----------------------------------------------------------
# Maximum different differences
# 
# Assume A is a strictly increasing array of positive integers with n elements:
# 
# A = [a1, a2, ..., an] such that a1 < a2 < a3 < ... < an
# 
# The difference array of A is [a2 - a1, a3 - a2, ..., an - an-1] That, is
# D = [d1, d2, ..., dn-1] suck that di = ai+1 - ai.
# 
# For example,
# 
# 1. A = [1, 2, 3, 4] => D = [1, 1, 1]
# 2. A = [1, 3, 4, 10] => D = [2, 1, 6]
# 
# Denote the characteristic as the number of different elements in the array D.
# 
# Following above examples, the characteristic of the first example is 1, since the array only contains the element {1}. In the second example, 
# the characteristic is 3 : {1,2,6}.
# 
# Given the last element of a strictly increasing array A, i.e. an, find the maximum possible characteristic. Note the size of A is less or equal than an.
# 
# For example, if an = 7, some examples that you could think of are:
# 
# 1. A = [1, 2, 3, 4, 5, 6, 7] => D = [1, 1, 1, 1, 1, 1]
# 2. A = [1, 2, 7] => D = [1, 5]
# 3. A = [2, 3, 5, 7] => D = [1, 2, 2]
# 4. A = [1, 4, 5, 7] => D = [3, 1, 2]
# 
# The characteristic of the first example is 1 (it only has one different element: {1} in D), in the second and third one the characteristic is 2 and in 
# the last one, the characteristic is 3. If you try any other possible A, you won't find a characteristic greater than 3. Thus, the answer is 3.
# 
# Input
# a n : (int) The maximum/last element of A. 2 <= an <= 2^200
# 
# Output
# (int) The maximum possible characteristic based on an
#  
# Note: Be aware of the size of an and the precision when working with big numbers. Find an optimal solution
# -----------------------------------------------------------

import math

def max_df(an):
    return (math.isqrt(an * 8) - 1) // 2
