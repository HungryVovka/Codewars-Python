# -----------------------------------------------------------
# You're on your way to the market when you hear beautiful music coming from a nearby street performer. The notes come together like you wouln't 
# believe as the musician puts together patterns of tunes. As you wonder what kind of algorithm you could use to shift octaves by 8 pitches or 
# something silly like that, it dawns on you that you have been watching the musician for some 10 odd minutes. You ask, "how much do people 
# normally tip for something like this?" The artist looks up. "It's always gonna be about tree fiddy."
# 
# It was then that you realize the musician was a 400 foot tall beast from the paleolithic era! The Loch Ness Monster almost tricked you!
# 
# There are only 2 guaranteed ways to tell if you are speaking to The Loch Ness Monster: A) it is a 400 foot tall beast from the paleolithic era; B) it will 
# ask you for tree fiddy.
# 
# Since Nessie is a master of disguise, the only way accurately tell is to look for the phrase "tree fiddy". Since you are tired of being grifted by this 
# monster, the time has come to code a solution for finding The Loch Ness Monster. Note that the phrase can also be written as "3.50" or 
# "three fifty".
# -----------------------------------------------------------

def is_lock_ness_monster(string):
    phrase = ["tree fiddy", "3.50", "three fifty"]
    for i in phrase:
        if i in string:
            return True
    return False

# or

import re

def is_lock_ness_monster(string):
    return bool(re.search(r"tree fiddy|3\.50|three fifty", string))

# or

def is_lock_ness_monster(string):
    phrase = ["tree fiddy", "3.50", "three fifty"]
    return any(i in string for i in phrase)

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