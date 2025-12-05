# -----------------------------------------------------------
# There are just some things you can't do on television. In this case, you've just 
# come back from having a "delicious" Barth burger and you're set to give an 
# interview. The Barth burger has made you queezy, and you've forgotten some of 
# the import rules of the "You Can't Do That on Television" set.
# 
# If you say any of the following words a large bucket of "water" will be dumped on 
# you: "water", "wet", "wash" This is true for any form of those words, like 
# "washing", "watered", etc.
# 
# If you say any of the following phrases you will be doused in "slime": 
# "I don't know", "slime"
# 
# If you say both in one sentence, a combination of water and slime, "sludge", will 
# be dumped on you.
# 
# Write a function, bucketOf(str), that takes a string and determines what will be 
# dumped on your head. If you haven't said anything you shouldn't have, the 
# bucket should be filled with "air". The words should be tested regardless of case.
# 
# Examples:
# 
# bucketOf("What is that, WATER?!?") -> "water"
# bucketOf("I don't know if I'm doing this right.") -> "slime"
# bucketOf("You won't get me!") -> "air"
# -----------------------------------------------------------

import re   # sub

def bucket_of(said: str) -> str:
    lower = said.lower()
    cleaned = re.sub(r"\bwas\b|\bwat\b", "", lower)
    water_hit = ("wa" in cleaned) or ("wet" in cleaned)
    slime_hit = ("i don't know" in cleaned) or ("slime" in cleaned)
    match (water_hit, slime_hit):
        case (True, True):
            return "sludge"
        case (True, False):
            return "water"
        case (False, True):
            return "slime"
        case _:
            return "air"

# -----------------------------------------------------------
# License
# Tasks are the property of Codewars (https://www.codewars.com/) 
# and users of this resource.
# 
# All solution code in this repository 
# is the personal property of Vladimir Rukavishnikov
# (vladimirrukavishnikovmail@gmail.com).
# 
# Copyright (C) 2025 Vladimir Rukavishnikov
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