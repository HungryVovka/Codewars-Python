# -----------------------------------------------------------
# You have a square shape of 4x4, you need to find out by what criterion there are cute and not cute patterns in these cases:
# 
# B W B W    B W W B    B W W W        B B W B    W B B W    B W W B
# W B W B    W B W W    W W B W        B B W B    B W W B    W B B W
# B W B W    W W B W    B W W W        W W B W    B W W B    W B B W
# W B W B    B W W B    W W B W        B B W B    W B B W    B W W B
# 
# 		Cute patterns						Not a cute pattern
# 
# According to the given arrangement of tiles, it is required to determine whether the executed pattern is cute. You need to write a function.
# 
# Input data:
# 
# A string value is entered into the function by type "BWBW\nBBWB\nWWBB\nBWWW".
# 
# B - black tile
# 
# W - white tile
# 
# \n - included just for line wrapping
# 
# Output data:
# 
# Return True if the pattern is cute and False otherwise.
# 
# Examples:
# 
# cute_pattern("BWBW\nBBWB\nWWBB\nBWWW") # should return True
# cute_pattern("BBWB\nBBWB\nWWBW\nBBWB") # should return False
# -----------------------------------------------------------

def cute_pattern(tiles):
    tiles = tiles.splitlines()
    for i in range(len(tiles) - 1):
        for j in range(len(tiles) - 1):
            a = tiles[i][j]
            b = tiles[i][j + 1]
            c = tiles[i + 1][j]
            d = tiles[i + 1][j + 1]
            if a == b == c == d:
                return False
    return True

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