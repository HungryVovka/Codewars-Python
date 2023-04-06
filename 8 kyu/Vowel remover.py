# -----------------------------------------------------------
# Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.
# 
# Examples
# "hello"     -->  "hll"
# "codewars"  -->  "cdwrs"
# "goodbye"   -->  "gdby"
# "HELLO"     -->  "HELLO"
# 
# don't worry about uppercase vowels
# y is not considered a vowel for this kata
# -----------------------------------------------------------

def shortcut( s ):
    vowels = ('a', 'e', 'i', 'o', 'u')
    newst = s
    for i in s:
        if i in vowels:
            newst = newst.replace(i, '')
    return newst

# or

import re

def shortcut( s ):
    return re.sub('[aoeui]', '', s)

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