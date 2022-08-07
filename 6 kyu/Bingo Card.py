# -----------------------------------------------------------
# After yet another dispute on their game the Bingo Association decides to change course and automate the game.
# 
# Can you help the association by writing a method to create a random Bingo card?
# 
# Bingo Cards
# A Bingo card contains 24 unique and random numbers according to this scheme:
# 
# 5 numbers from the B column in the range 1 to 15
# 5 numbers from the I column in the range 16 to 30
# 4 numbers from the N column in the range 31 to 45
# 5 numbers from the G column in the range 46 to 60
# 5 numbers from the O column in the range 61 to 75
# 
# Task
# Write the function get_card()/getCard(). The card must be returned as an array of Bingo style numbers:
# 
# [ 'B14', 'B12', 'B5', 'B6', 'B3', 'I28', 'I27', ... ]
# 
# The numbers must be in the order of their column: B, I, N, G, O. Within the columns the order of the numbers is random.
# -----------------------------------------------------------

import functools
import random

bingo = [["B", [1, 15], 5],
         ["I", [16, 30], 5],
         ["N", [31, 45], 4],
         ["G", [46, 60], 5],
         ["O", [61, 75], 5]]


def get_bingo_card():
    return list(
        functools.reduce(
        lambda a, b: a + b, 
            [[j + i for i in card(k, l)] 
                    for j, k, l in bingo]))       
                
    
def card(k, l):
    arr = []
    s = set()
    while len(arr) != l:
        m = random.randint(k[0], k[1])
        if m not in s:
            arr.append(str(m))
            s.add(m)
    return arr

# or

from random import sample

def get_bingo_card():
    b = ["B" + str(B) for B in sample(range(1, 16), 5)]
    i = ["I" + str(I) for I in sample(range(16, 31), 5)]
    n = ["N" + str(N) for N in sample(range(31, 46), 4)]
    g = ["G" + str(G) for G in sample(range(46, 61), 5)]
    o = ["O" + str(O) for O in sample(range(61, 76), 5)]
    return b + i + n + g + o