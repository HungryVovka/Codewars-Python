# -----------------------------------------------------------
# Define a function that removes duplicates from an array of numbers and returns it as a result.
# 
# The order of the sequence has to stay the same.
# -----------------------------------------------------------

def distinct(seq):
    newseq = []
    for i in seq:
        if i not in newseq:
            newseq.append(i)
    return newseq

# or

def distinct(seq):
    return sorted(set(seq), key = seq.index)

# or

def distinct(seq):
    return list(dict.fromkeys(seq))

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