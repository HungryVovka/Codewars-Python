# -----------------------------------------------------------
# A spoonerism is a spoken phrase in which the first letters of two of the words are swapped around, often with amusing results.
# 
# In its most basic form a spoonerism is a two word phrase in which only the first letters of each word are swapped:
# 
# "not picking" --> "pot nicking"
# 
# Your task is to create a function that takes a string of two words, separated by a space: words and returns a spoonerism of those words in a string, 
# as in the above example. A "word" in the context of this kata can contain any of the letters A through Z in upper or lower case, and the numbers 0 
# to 9. Though spoonerisms are about letters in words in the domain of written and spoken language, numbers are included in the inputs for the 
# random test cases and they require no special treatment.
# 
# NOTE: All input strings will contain only two words. Spoonerisms can be more complex. For example, three-word phrases in which the first letters of 
# the first and last words are swapped: "pack of lies" --> "lack of pies" or more than one letter from a word is swapped: 
# "flat battery --> "bat flattery" You are NOT expected to account for these, or any other nuances involved in spoonerisms.
# 
# Once you have completed this kata, a slightly more challenging take on the idea can be found here: 
# http://www.codewars.com/kata/56dbed3a13c2f61ae3000bcd
# -----------------------------------------------------------


def spoonerize(words):
    arr = words.split(" ")
    i, j = list(arr[0]), list(arr[1])
    i[0], j[0] = j[0], i[0]
    return "".join(i) + " " + "".join(j)

# or

def spoonerize(words):
    i, j = words.split()
    return "{}{} {}{}".format(j[0], i[1:], i[0], j[1:])

# or

def spoonerize(words):
    i, j = words.split()
    return f"{j[0]}{i[1:]} {i[0]}{j[1:]}"

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