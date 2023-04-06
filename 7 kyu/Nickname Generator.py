# -----------------------------------------------------------
# Nickname Generator
# 
# Write a function, nicknameGenerator that takes a string name as an argument and returns the first 3 or 4 letters as a nickname.
# 
# If the 3rd letter is a consonant, return the first 3 letters.
# 
# nickname("Robert") //=> "Rob"
# nickname("Kimberly") //=> "Kim"
# nickname("Samantha") //=> "Sam"
# 
# If the 3rd letter is a vowel, return the first 4 letters.
# 
# nickname("Jeannie") //=> "Jean"
# nickname("Douglas") //=> "Doug"
# nickname("Gregory") //=> "Greg"
# 
# If the string is less than 4 characters, return "Error: Name too short".
# 
# Notes:
# 
# Vowels are "aeiou", so discount the letter "y".
# Input will always be a string.
# Input will always have the first letter capitalised and the rest lowercase (e.g. Sam).
# The input can be modified
# -----------------------------------------------------------

def nickname_generator(name):
    if len(name) < 4:
        return "Error: Name too short"
    elif name[2] in 'aeiou':
        return name[:4]
    else:
        return name[:3]

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