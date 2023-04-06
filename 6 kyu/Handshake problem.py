# -----------------------------------------------------------
# Johnny is a farmer and he annually holds a beet farmers convention "Drop the beet".
# 
# Every year he takes photos of farmers handshaking. Johnny knows that no two farmers handshake more than once. He also knows that some of the 
# possible handshake combinations may not happen.
# 
# However, Johnny would like to know the minimal amount of people that participated this year just by counting all the handshakes.
# 
# Help Johnny by writing a function, that takes the amount of handshakes and returns the minimal amount of people needed to perform these 
# handshakes (a pair of farmers handshake only once).
# -----------------------------------------------------------

import math

def get_participants(handshakes):
    return 0 if handshakes == 0 else math.ceil((math.sqrt(1 + 8 * handshakes) - 1) / 2) + 1

# or

def get_participants(handshakes):
    i, j = 0, 0
    while i < handshakes:
        i = j * (j + 1) / 2
        j += 1
    return j

# or

def get_participants(handshakes):
    i, j = 0, 0
    while i < handshakes:
        i += j
        j += 1
    return j

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