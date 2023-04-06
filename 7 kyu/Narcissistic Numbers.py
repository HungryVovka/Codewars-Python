# -----------------------------------------------------------
# A Narcissistic Number is a number of length l in which the sum of its digits to the power of l is equal to the original number. If this seems 
# confusing, refer to the example below.
# 
# Ex: 153, where l = 3 ( the number of digits in 153 )
# 1^3 + 5^3 + 3^3 = 153
# 
# Write a function that, given n, returns whether or not n is a Narcissistic Number.
# -----------------------------------------------------------

def is_narcissistic(i):
    str_i = str(i)
    i_arrstr = list(str_i)
    number = 0
    for n in i_arrstr:
        n = int(n)
        number += n**len(i_arrstr)
    if i == number:
        return(True)
    else:
        return(False)

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