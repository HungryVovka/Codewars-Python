# -----------------------------------------------------------
# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
# 
# Write a function which takes a list of strings and returns each line prepended by the correct number.
# 
# The numbering starts at 1. The format is n: string. Notice the colon and space in between.
# 
# Examples: (Input --> Output)
# 
# [] --> []
# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]
# -----------------------------------------------------------

def number(lines):
    try:
        answer = []
        i = 1
        for l in lines:
            answer.append(f"{i}: {l}")
            i += 1
        return answer
    except:
        return []

# or

def number(lines):
    return ["%s: %s" % l for l in enumerate(lines, 1)]

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