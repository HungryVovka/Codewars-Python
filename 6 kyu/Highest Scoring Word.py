# -----------------------------------------------------------
# Given a string of words, you need to find the highest scoring word.
# 
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# 
# For example, the score of abad is 8 (1 + 2 + 1 + 4).
# 
# You need to return the highest scoring word as a string.
# 
# If two words score the same, return the word that appears earliest in the original string.
# 
# All letters will be lowercase and all inputs will be valid.
# -----------------------------------------------------------

def high(x):
    words_and_scores = {}
    words = x.split()
    for word in words:
        score = sum((ord(i) - ord('a') + 1) for i in word)
        words_and_scores[word] = score
    return max(words_and_scores, key=words_and_scores.get)

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