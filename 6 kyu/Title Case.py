# -----------------------------------------------------------
# A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the first letter of the word is in upper case) or 
# (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.
# 
# Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The list of minor words will be given as a 
# string with each word separated by a space. Your function should ignore the case of the minor words string -- it should behave in the same way even 
# if the case of the minor word string is changed.
# 
# Arguments (Haskell)
# First argument: space-delimited list of minor words that must always be lowercase except for the first word in the string.
# Second argument: the original string to be converted.
# 
# Arguments (Other languages)
# First argument (required): the original string to be converted.
# Second argument (optional): space-delimited list of minor words that must always be lowercase except for the first word in the string. The 
# JavaScript/CoffeeScript tests will pass undefined when this argument is unused.
# 
# Example
# title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
# title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
# title_case('the quick brown fox') # should return: 'The Quick Brown Fox'
# -----------------------------------------------------------

def title_case(title, minor_words=''):
    title = [i.capitalize() for i in title.split()]
    minor_words = minor_words.upper().split()
    for j in range(1, len(title)):
        if title[j].upper() in minor_words:
            title[j] = title[j].lower()
    return " ".join(title)

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