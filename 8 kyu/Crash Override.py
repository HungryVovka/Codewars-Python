# -----------------------------------------------------------
# Every budding hacker needs an alias! The Phantom Phreak, Acid Burn, Zero Cool and Crash Override are some notable examples from the film 
# Hackers.
# 
# Your task is to create a function that, given a proper first and last name, will return the correct alias.
# 
# Notes:
# Two objects that return a one word name in response to the first letter of the first name and one for the first letter of the surname are already 
# given.
# 
# If the first character of either of the names given to the function is not a letter from A - Z, you should return 
# "Your name must start with a letter from A - Z."
# 
# Sometimes people might forget to capitalize the first letter of their name so your function should accommodate for these grammatical errors.
# 
# Examples
# FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', ...}
# SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst' ...}
# 
# alias_gen('Larry', 'Brentwood') == 'Logic Bomb'
# alias_gen('123abc', 'Petrovic') == 'Your name must start with a letter from A - Z.'
# 
# Happy hacking!
# -----------------------------------------------------------

def alias_gen(f_name, l_name):
    f = FIRST_NAME.get(f_name[0].upper())
    l = SURNAME.get(l_name[0].upper())
    return "{} {}".format(f, l) if f and l else "Your name must start with a letter from A - Z."

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