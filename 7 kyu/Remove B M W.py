# -----------------------------------------------------------
# It happened decades before Snapchat, years before Twitter and even before Facebook. 
# Targeted advertising was a bit of a challenge back then. One day, the marketing 
# professor at my university told us a story that I am yet to confirm using reliable 
# sources. Nevertheless, I retold the story to dozens of my students already, so, sorry 
# BMW if it is all a big lie.
# 
# Allegedly, BMW, in an attempt to target the educated, produced billboard posters 
# featuring the English alphabet with three letters missing: B, M and W. Needless 
# to say, many were confused, some to the extent of road accidents.
# 
# Your task is to write a function that takes one parameter str that MUST be a 
# string and removes all capital and small letters B, M and W.
# If data of the wrong data type was sent as a parameter the function must throw 
# an error with the following specific message:
# 
# TypeError("This program only works for text.")
# 
# For Python here's a good resource you might need for the exception type ;)
# -----------------------------------------------------------

import re   # sub

def remove_bmw(string: str) -> str:
    if not isinstance(string, str):
        raise TypeError("This program only works for text.")    
    return re.sub(r"[BMWbmw]", "", string)

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