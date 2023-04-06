# -----------------------------------------------------------
# Consider the following array:
# 
# [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789, 12345678910, 1234567891011...]
# 
# If we join these blocks of numbers, we come up with an infinite sequence which starts with 112123123412345123456.... The list is infinite.
# 
# You will be given an number (n) and your task will be to return the element at that index in the sequence, where 1 ≤ n ≤ 10^18. Assume the 
# indexes start with 1, not 0. For example:
# 
# solve(1) = 1, because the first character in the sequence is 1. There is no index 0. 
# solve(2) = 1, because the second character is also 1.
# solve(3) = 2, because the third character is 2.
# 
# More examples in the test cases. Good luck!
# -----------------------------------------------------------

import math

class Solve:
    def __init__(self):
        self.n = 0
    
    def first_half(self, n):
        len_n = len(str(n))
        return len_n * (n + 1) - math.floor((10**len_n - 1) / 9)
    
    def second_half(self, n):
        len_n = len(str(n))
        x1 = 100**(len_n - 1)
        x2 = 10**(len_n - 1)
        return ((x1 + x2) * (len_n - 1) -\
                math.floor((x1 - 1) * 7 / 33) + \
                math.floor((x2 - 1) / 9)) // 2 + \
        (n + x2 + 2) * (n - x2 + 1) * len_n // 2 - \
        (n - x2 + 1) * math.floor((x2 * 10 - 1) / 9)
        
    def appart(self, part, n):
        a = -1
        b = n
        while b - a != 1:
            c = math.floor((a + b) / 2)
            if part(c) >= n:
                b = c
            else:
                a = c
        return b
    
    def answer(self):
        res = self.appart(self.second_half, self.n)
        self.n -= self.second_half(res - 1)
        res = self.appart(self.first_half, self.n)
        self.n -= self.first_half(res -  1)
        return int(str(res)[self.n - 1])

def solve(n):
    s = Solve()
    s.n = n
    return s.answer()

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