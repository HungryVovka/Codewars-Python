# -----------------------------------------------------------
# A stream of data is received and needs to be reversed.
# 
# Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:
# 
# 11111111  00000000  00001111  10101010
#  (byte1)   (byte2)   (byte3)   (byte4)
# should become:
# 
# 10101010  00001111  00000000  11111111
#  (byte4)   (byte3)   (byte2)   (byte1)
# The total number of bits will always be a multiple of 8.
# 
# The data is given in an array as such:
# 
# [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
# Note: In the C and NASM languages you are given the third parameter which is the number of segment blocks.
# -----------------------------------------------------------

def data_reverse(data):
    reverseit = []
    answer = []
    for i in range(0, len(data), 8):
        reverseit.append(data[i: i + 8])
    for j in reversed(reverseit):
        answer.extend(j)
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