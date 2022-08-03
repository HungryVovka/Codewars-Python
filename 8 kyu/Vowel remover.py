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