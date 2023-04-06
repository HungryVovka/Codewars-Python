# -----------------------------------------------------------
# Hello Codewarriors,
# 
# In this exercise you will have to multiply 2 numpy matrices (2d numpy arrays) in the following way:
# 
# Take each element of the first matrix and multiply by the second matrix
# Place the resulting matrices in the same order as elements of the first matrix.
# 
# Important: use Numpy arrays as input and as output
# 
# If arrays with wrong shape (not 2d) or arrays with zero shape (shape=(0, 0)) are passed as an input, please return None
# 
# Examples:
# 
# I. A = [[2]]
# 
# B = [[1, 2], [3, 4]]
# 
# AB = [[2, 4], [6, 8]]
# 
# II. A = [[2, 3]]
# 
# B = [[40], [50]]
# 
# AB = [[80, 120], [100, 150]]
# 
# III. A = [[0, 1], [2, 3]]
# 
# B = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
# 
# AB = [[ 0, 0, 0, 1, 1, 1], [ 0, 0, 0, 1, 1, 1], [ 0, 0, 0, 1, 1, 1], [ 0, 0, 0, 1, 1, 1], [ 2, 2, 2, 3, 3, 3], [ 2, 2, 2, 3, 3, 3], [ 2, 2, 2, 3, 3, 3], [ 2, 2, 2, 3, 3, 3]]
# 
# IV. A = [[1, 2], [3, 4]]
# 
# B = [[10, 20, 30], [40, 50, 60]]
# 
# AB = [[ 10, 20, 30, 20, 40, 60], [ 40, 50, 60, 80, 100, 120], [ 30, 60, 90, 40, 80, 120], [120, 150, 180, 160, 200, 240]]
# -----------------------------------------------------------

import numpy as np

def np_append(A, B):
    return [np.append([], [j * k for k in i]) for i in A for j in B]

def weird_mul(A, B):
    if len(A.shape) == 2 == len(B.shape):
        answer = np.array(np_append(A, B))
        if answer != []:
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