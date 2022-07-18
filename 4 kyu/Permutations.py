# -----------------------------------------------------------
# In this kata you have to create all permutations of a non empty input string and remove duplicates, if present. This means, you have to shuffle all 
# letters from the input in all possible orders.
# 
# Examples:
# 
# * With input 'a'
# * Your function should return: ['a']
# * With input 'ab'
# * Your function should return ['ab', 'ba']
# * With input 'aabb'
# * Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
# The order of the permutations doesn't matter.
# 
# -----------------------------------------------------------

from itertools import permutations as perm

def permutations(string):
    prm = perm(string, len(string))
    return set(list(map(lambda x: "".join(x), prm)))