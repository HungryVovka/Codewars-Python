# -----------------------------------------------------------
# Trolls are attacking your comment section!
# 
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# 
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# 
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# 
# Note: for this kata y isn't considered a vowel.
# -----------------------------------------------------------

def disemvowel(string_):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    newstring = ''
    
    for n in string_:
        if n in vowels:
            continue
        else:
            newstring += n
    return newstring

# or

def disemvowel(string_):
    for vovel in "aAeEiIoOuU":
        string_ = string_.replace(vovel, "")
    return string_

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