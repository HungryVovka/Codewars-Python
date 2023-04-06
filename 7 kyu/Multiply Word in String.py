# -----------------------------------------------------------
# You are to write a function that takes a string as its first parameter. This string will be a string of words.
# 
# You are expected to then use the second parameter, which will be an integer, to find the corresponding word in the given string. The first word 
# would be represented by 0.
# 
# Once you have the located string you are finally going to multiply by it the third provided parameter, which will also be an integer. You are 
# additionally required to add a hyphen in between each word.
# 
# Example
# 
# modify_multiply ("This is a string",3,5) 
# 
# Should return
# 
# "string-string-string-string-string"
# 
# Since the 3rd word is 'string'(starting from 0 remember) and the third paramater indicates that it should be repeated 5 times.
# 
# Simple. Good luck.
# -----------------------------------------------------------

def modify_multiply(st, loc, num):
    st = st.split(" ")
    return "".join((st[loc] + "-") * num)[:-1]

# or

def modify_multiply(st, loc, num):
    return "-".join([st.split()[loc]] * num)

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