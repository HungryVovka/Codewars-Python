# -----------------------------------------------------------
# A latin square is an n × n array filled with the integers 1 to n, each occurring once in each row and column.
# 
# Here are examples of latin squares of size 4 and 7:
# 
# [[1, 4, 3, 2],      [[2, 3, 1, 7, 4, 6, 5], 
#  [4, 3, 2, 1],       [7, 1, 6, 5, 2, 4, 3], 
#  [3, 2, 1, 4],       [6, 7, 5, 4, 1, 3, 2], 
#  [2, 1, 4, 3]]       [4, 5, 3, 2, 6, 1, 7], 
#                      [5, 6, 4, 3, 7, 2, 1], 
#                      [1, 2, 7, 6, 3, 5, 4], 
#                      [3, 4, 2, 1, 5, 7, 6]]
# 
# Latin squares have many practical uses, for example in error-correcting-codes and the design of agricultural experiments. See 
# https://en.wikipedia.org/wiki/Latin_square for more details. Sudoku is a special type of 9 x 9 latin square, with additional conditions.
# 
# Write a function that returns a latin square for any positive integer n.
# 
# If you are interested in verifying that any array is a latin square, see Latin Square Validator.
# -----------------------------------------------------------

def make_latin_square(n):
    ## Make all rows 1,2,...,n
    latin_square = [[(i + _) % n + 1 for i in range(n)] for _ in range(n)]
    return latin_square

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