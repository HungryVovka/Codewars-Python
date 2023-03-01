# -----------------------------------------------------------
# Jumps in a cycle [a1,...,an] can be written in a extended form with a jump rate equal to 1 as a1 -> a2 -> ... -> an -> a1 -> ... -> an...
# 
# Given a jump rate k and starting in the first element, you must find the number of jumps you have to take in order to reach the same element.
# 
# ASSUMPTION: The elements in the cycle are distinguishable.
# 
# Examples
# [1,5,7,8,9] and jump rate 1, then 1 -> 5 -> 7 -> 8 -> 9 -> 1. That is, 5 jumps.
# 
# [1,5,7,8,9] and jump rate 2, then 1 -> 7 -> 9 -> 5 -> 8 -> 1. That is, 5 jumps.
# 
# [1,5,1] and jump rate 2, then 1 -> 1 -> 5 -> 1. That is, 3 jumps.
# 
# Input
# cl: (list) the list with the cycle. 2 <= cl <= 2^30
# 
# k: (int) the jump rate. 1 <= k <= 2^40
# 
# Output
# (int) The number of jumps in order to reach the same first element in the cycle.
# -----------------------------------------------------------

import math

def get_jumps(cycle_list, k):
    return len(cycle_list) / math.gcd(len(cycle_list), k)