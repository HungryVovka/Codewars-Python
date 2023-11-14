# -----------------------------------------------------------
# Instructions
# Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in 
# the string.
# 
# Example (Input --> Output)
# "CodEWaRs" --> [0,3,4,6]
# -----------------------------------------------------------

def capitals(word):
    answer = []
    i = 0
    for char in word:
        if ord(char) >= 65 and ord(char) <= 90:
            answer.append(i)
        i += 1
    return answer

# or

def capitals(word):
    answer = []
    for i in range(len(word)):
        if ord(word[i]) >= 65 and ord(word[i]) <= 90:
            answer.append(i)
        i += 1
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