# -----------------------------------------------------------
# In the following 6 digit number:
# 
# 283910
# 
# 91 is the greatest sequence of 2 consecutive digits.
# 
# In the following 10 digit number:
# 
# 1234567890
# 
# 67890 is the greatest sequence of 5 consecutive digits.
# 
# Complete the solution so that it returns the greatest sequence of five consecutive digits found within the number given. The number will be passed 
# in as a string of only digits. It should return a five digit integer. The number passed may be as large as 1000 digits.
# 
# Adapted from ProjectEuler.net
# -----------------------------------------------------------

def solution(digits):
    arr = list(digits)
    largest = 0
    i = 0
    while i <= (len(arr) - 5):
        five_digits = int("".join(arr[i:i+5]))
        if five_digits > largest:
            largest = five_digits
        i += 1
    return largest

# or

def solution(digits):
    arr = list(digits)
    largest = 0
    for i in range(len(digits) - 4):
        five_digits = int("".join(arr[i:i+5]))
        if five_digits > largest:
            largest = five_digits
    return largest

# or

def solution(digits):
    return max(int(digits[i:i+5]) for i in range(len(digits) - 4))

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