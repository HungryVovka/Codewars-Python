# -----------------------------------------------------------
# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you 
# must multiply the digits in num until you reach a single digit.
# 
# For example (Input --> Output):
# 
# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)
# -----------------------------------------------------------

def persistence(n):
    answer = 0
    while True:
        if n > 9:
            n = list(str(n))
            new_n = 1
            for i in n:
                new_n *= int(i)
                print (new_n)
            n = new_n
            answer += 1
        else:
            return answer

# or

def persistence(n):
    answer = 0
    while n > 9:
        new_n = 1
        for i in str(n):
            new_n *= int(i)
        n = new_n
        answer += 1
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