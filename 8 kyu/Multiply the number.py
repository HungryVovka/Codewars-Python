# -----------------------------------------------------------
# Jack really likes his number five: the trick here is that you have to multiply each number by 5 raised to the number of digits of each numbers, so, for
# example:
#
# multiply(3)==15 # 3 * 5¹
# multiply(10)==250 # 10 * 5²
# multiply(200)==25000 # 200 * 5³
# multiply(0)==0 # 0 * 5¹
# multiply(-3)==-15 # -3 * 5¹
# -----------------------------------------------------------

def multiply(n):
    n_length = abs(n)
    new_n = n * (5 ** (len(str(n_length))))
    return(new_n)

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