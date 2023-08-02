# -----------------------------------------------------------
# Find the missing letter
# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
# 
# You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
# The array will always contain letters in only one case.
# 
# Example:
# 
# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'
# 
# (Use the English alphabet with 26 letters!)
# 
# Have fun coding it and please don't forget to vote and rank this kata! :-)
# 
# I have also created other katas. Take a look if you enjoyed this kata!
# -----------------------------------------------------------

def find_missing_letter(chars):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abc += abc.lower()
    ch = abc.index(chars[0])
    for i in range(len(chars)):
        if chars[i] != abc[ch + i]:
            return abc[ch + i]

# or

def find_missing_letter(chars):
    i = 0
    while i < (len(chars) - 1):
        if ord(chars[i]) - ord(chars[i + 1]) != -1:
            return chr(ord(chars[i]) + 1)
        else:
            i += 1

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