# -----------------------------------------------------------
# A square of squares
# You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square 
# building blocks!
# 
# However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a 
# way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.
# 
# Task
# Given an integral number, determine if it's a square number:
# 
# In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer 
# with itself.
# 
# The tests will always use some integral number, so don't worry about that in dynamic typed languages.
# 
# Examples
# -1  =>  false
#  0  =>  true
#  3  =>  false
#  4  =>  true
# 25  =>  true
# 26  =>  false
# -----------------------------------------------------------

def is_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    n1, n2 = 1, n
    while n1 + 1 < n2:
        n3 = (n1 + n2) // 2
        if n3**2 < n:
            n1 = n3
        else:
            n2 = n3
    answer = (n == n1**2 or n == (n1 + 1)**2)
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