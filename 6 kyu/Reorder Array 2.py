# -----------------------------------------------------------
# This kata focuses on the Numpy python package and you can read up on the Numpy array manipulation functions here: 
# https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.array-manipulation.html
# 
# You will get two integers N and M. You must return an array with two sub-arrays with numbers in ranges [0, N / 2) and [N / 2, N) 
# respectively, each of them being rotated M times.
# 
# reorder(10, 1)   =>  [[4, 0, 1, 2, 3], [9, 5, 6, 7, 8]]
# reorder(10, 3)   =>  [[2, 3, 4, 0, 1], [7, 8, 9, 5, 6]]
# reorder(10, 97)  =>  [[3, 4, 0, 1, 2], [8, 9, 5, 6, 7]]
# -----------------------------------------------------------

import numpy as np

def reorder(n, m):
    x1 = np.roll(np.array([i for i in range(0, int(n / 2))]), m)
    x2 = np.roll(np.array([i for i in range(int(n / 2), n)]), m)
    return [[i for i in x1], [i for i in x2]]

# or

def reorder(n, m):
    x1 = list(range(n // 2))
    x2 = list(range(n // 2, n))
    i = m % len(x1)
    while i > 0:
        x1 = [x1[-1]] + x1[:-1]
        x2 = [x2[-1]] + x2[:-1]
        i -= 1
    return [x1, x2]

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