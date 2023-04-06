# -----------------------------------------------------------
# Complete the function word (string) and returns a string that spells the word using the NATO phonetic alphabet.
# 
# There should be a space between each word in the returned string, and the first letter of each word should be capitalized.
# 
# For those of you that don't want your fingers to bleed, this kata already has a dictionary typed out for you.
# 
# Examples
# "hi"      -->  "Hotel India"
# "abc"     -->  "Alpha Bravo Charlie"
# "babble"  -->  "Bravo Alpha Bravo Bravo Lima Echo"
# "Banana"  -->  "Bravo Alpha November Alpha November Alpha"
# -----------------------------------------------------------

nato_alphabet = {
    "a": "Alpha", "b": "Bravo", "c": "Charlie",
    "d": "Delta", "e": "Echo", "f": "Foxtrot",
    "g": "Golf", "h": "Hotel", "i": "India",
    "j": "Juliett", "k": "Kilo", "l": "Lima",
    "m": "Mike", "n": "November", "o": "Oscar",
    "p": "Papa", "q": "Quebec", "r": "Romeo",
    "s": "Sierra", "t": "Tango", "u": "Uniform",
    "v": "Victor", "w": "Whiskey", "x": "X-ray",
    "y": "Yankee", "z": "Zulu"
    
}
  
def nato(word):
    return " ".join(nato_alphabet[i] for i in word.lower())

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