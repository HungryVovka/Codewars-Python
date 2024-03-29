# -----------------------------------------------------------
# In this kata you have to implement a base converter, which converts positive integers between arbitrary bases / alphabets. Here are some pre-
# defined alphabets:
# 
# bin      = '01'
# oct      = '01234567'
# dec      = '0123456789'
# hex      = '0123456789abcdef'
# allow    = 'abcdefghijklmnopqrstuvwxyz'
# allup    = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# alpha    = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# alphanum = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# 
# The function convert() should take an input (string), the source alphabet (string) and the target alphabet (string). You can assume that the input 
# value always consists of characters from the source alphabet. You don't need to validate it.
# 
# Examples
# convert("15", dec, bin)       ==>  "1111"
# convert("15", dec, oct)       ==>  "17"
# convert("1010", bin, dec)     ==>  "10"
# convert("1010", bin, hex)     ==>  "a"
# convert("0", dec, alpha)      ==>  "a"
# convert("27", dec, allow)     ==>  "bb"
# convert("hello", allow, hex)  ==>  "320048"
# 
# Additional Notes:
# 
# The maximum input value can always be encoded in a number without loss of precision in JavaScript. In Haskell, intermediate results will 
# probably be too large for Int.
# The function must work for any arbitrary alphabets, not only the pre-defined ones
# You don't have to consider negative numbers
# -----------------------------------------------------------

def convert(data, source, target):
    data = reversed(data)
    len_source, len_target  = len(source), len(target)
    basecon = sum([source.index(j) * len_source ** i for i, j in enumerate(data)])
    arr = []
    if basecon == 0:
        arr.append(target[0])
    else:
        while basecon:
            arr.append(target[basecon % len_target])
            basecon = basecon // len_target 
    return "".join(reversed(arr))

# or

def convert(input, source, target):
    con = ""
    basecon = 0
    for i in input:
        basecon = basecon * len(source) + source.index(i)
    if basecon == 0:
        return target[0]
    while basecon > 0:
        con += target[basecon % len(target)]
        basecon //= len(target)
    return con[::-1]

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