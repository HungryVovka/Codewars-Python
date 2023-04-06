# -----------------------------------------------------------
# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If 
# the word's length is even, return the middle 2 characters.
# 
# #Examples:
# 
# Kata.getMiddle("test") should return "es"
# 
# Kata.getMiddle("testing") should return "t"
# 
# Kata.getMiddle("middle") should return "dd"
# 
# Kata.getMiddle("A") should return "A"
# 
# #Input
# 
# A word (string) of length 0 < str < 1000 (In javascript you may get slightly more than 1000 in some test cases due to an error in the test cases). 
# You do not need to test for this. This is only here to tell you that you do not need to worry about your solution timing out.
# 
# #Output
# 
# The middle character(s) of the word represented as a string.
# -----------------------------------------------------------

def get_middle(s):
    first = (len(s) - 1) // 2
    second = (len(s) + 2) // 2
    return s[first:second]

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