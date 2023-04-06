# -----------------------------------------------------------
# Welcome.
# 
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# 
# If anything in the text isn't a letter, ignore it and don't return it.
# 
# "a" = 1, "b" = 2, etc.
# 
# Example
# alphabet_position("The sunset sets at twelve o' clock.")
#
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )
# -----------------------------------------------------------

def alphabet_position(text):
    text = text.lower()
    repl = ""
    for i in text:
        if i.isalpha():
            repl += str(ord(i) - 96) + " "
    return repl.rstrip()

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