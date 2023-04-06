# -----------------------------------------------------------
# An AI has infected a text with a character!!
# 
# This text is now fully mutated to this character.
# 
# If the text or the character are empty, return an empty string.
# There will never be a case when both are empty as nothing is going on!!
# 
# Note: The character is a string of length 1 or an empty string.
# 
# Example
# text before = "abc"
# character   = "z"
# text after  = "zzz"
# -----------------------------------------------------------

def contamination(text, char):
    return text.replace(text, char * len(text))

# or

def contamination(text, char):
    return char * len(text)

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