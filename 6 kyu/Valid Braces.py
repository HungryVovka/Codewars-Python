# -----------------------------------------------------------
# Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false 
# if it's invalid.
# 
# This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the 
# idea!
# 
# All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.
# 
# What is considered Valid?
# A string of braces is considered valid if all braces are matched with the correct brace.
# 
# Examples
# "(){}[]"   =>  True
# "([{}])"   =>  True
# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False
# -----------------------------------------------------------

def valid_braces(string):
    a = "[]"
    b = "()"
    c = "{}"
    while (string.find(a) != -1) or (string.find(b) != -1) or (string.find(c) != -1):
        if string.find(a) != -1:
            string = string.replace(a, "")
        if string.find(b) != -1:
            string = string.replace(b, "")
        if string.find(c) != -1:
            string = string.replace(c, "")
    return not len(string)

# or

def valid_braces(string):
    while "[]" in string or "()" in string or "{}" in string:
        string = string.replace("[]", "")
        string = string.replace("()", "")
        string = string.replace("{}", "")
    return string == ""

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