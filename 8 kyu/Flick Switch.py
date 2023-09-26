# -----------------------------------------------------------
# Task
# Create a function that always returns True for every item in a given list. However, if an element is the word "flick", switch to always returning the 
# opposite boolean value.
# 
# Examples
# ["codewars", "flick", "code", "wars"] ➞ [True, False, False, False]
# 
# ['flick', 'chocolate', 'adventure', 'sunshine'] ➞[False, False, False, False]
# 
# ['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]
# 
# Notes
# "flick" will always be given in lowercase.
# A list may contain multiple flicks.
# Switch the boolean value on the same element as the flick itself.
# -----------------------------------------------------------

def flick_switch(lst):
    i = True
    answer = []
    for j in lst:
        if j != "flick":
            answer.append(i)
        else:
            i = not i
            answer.append(i)
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