# -----------------------------------------------------------
# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living 
# organisms.
# 
# If you want to know more: http://en.wikipedia.org/wiki/DNA
# 
# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for 
# Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
# 
# More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)
# 
# Example: (input --> output)
# 
# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"
# -----------------------------------------------------------

def DNA_strand(dna):
    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    return ''.join([complement[i] for i in dna])

# or

import string

com = str.maketrans("CGAT", "GCTA")

def DNA_strand(dna):
    return dna.translate(com)

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