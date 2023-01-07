# -----------------------------------------------------------
# A rook is a piece used in the game of chess which is played on a board of square grids. A rook can only move vertically or horizontally from its current 
# position and two rooks attack each other if one is on the path of the other. In the following figure, the dark squares represent the reachable locations 
# for rook R1 from its current position. The figure also shows that the rook R1 and R2 are in attacking positions where R1 and R3 are not. R2 and R3 are 
# also in non-attacking positions.
# 
# Now, given two numbers n and k, your job is to determine the number of ways one can put k rooks on an nxn chessboard so that no two of them 
# are in attacking positions.
# 
# Range: (1 ≤ n ≤ 15) and (0 ≤ k ≤ n2)
# -----------------------------------------------------------

def rooks(n, k):
    x, y = 0, 1
    while x < k:
        y = y * n * n
        n = n - 1
        y = y / (x + 1)
        x += 1
    return y

# or

import math

def rooks(n, k):
    return math.comb(n, k) * math.comb(n, k) * math.factorial(k)