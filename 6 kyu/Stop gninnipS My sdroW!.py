# -----------------------------------------------------------
# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the 
# name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
# 
# Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( 
# "This is another test" )=> returns "This is rehtona test"
# -----------------------------------------------------------

def spin_words(sentence):
    reversed = []
    spl_str = sentence.split(" ")
    for i in spl_str:
        if len(i) > 4:
            reversed.append(i[::-1])
        else:
            reversed.append(i)
    return " ".join(reversed)

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