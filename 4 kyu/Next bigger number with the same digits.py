# -----------------------------------------------------------
# Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:
# 
# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071
# 
# nextBigger(num: 12)   // returns 21
# nextBigger(num: 513)  // returns 531
# nextBigger(num: 2017) // returns 2071
# 
# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):
# 
# 9 ==> -1
# 111 ==> -1
# 531 ==> -1
# 
# nextBigger(num: 9)   // returns nil
# nextBigger(num: 111) // returns nil
# nextBigger(num: 531) // returns nil
# -----------------------------------------------------------

def next_bigger(n):
    if str(n) == "".join(sorted(str(n))[::-1]):
        return -1
    bigger = n
    while True:
        bigger += 1
        if sorted(str(bigger)) == sorted(str(n)):
            return bigger

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