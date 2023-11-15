# -----------------------------------------------------------
# If　a = 1, b = 2, c = 3 ... z = 26
# 
# Then l + o + v + e = 54
# 
# and f + r + i + e + n + d + s + h + i + p = 108
# 
# So friendship is twice as strong as love :-)
# 
# Your task is to write a function which calculates the value of a word based off the sum of the alphabet positions of its characters.
# 
# The input will always be made of only lowercase letters and will never be empty.
# -----------------------------------------------------------

def words_to_marks(s):
    word_value = 0
    for i in s:
        word_value += ord(i) - 96
    return word_value

# or

def words_to_marks(s):
    return sum(ord(i) - 96 for i in s)

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