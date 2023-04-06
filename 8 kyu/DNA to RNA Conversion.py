# -----------------------------------------------------------
# Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine 
# ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').
# 
# Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In 
# RNA Thymine is replaced by another nucleic acid Uracil ('U').
# 
# Create a function which translates a given DNA string into RNA.
# 
# For example:
# 
# "GCAT"  =>  "GCAU"
# The input string can be of arbitrary length - in particular, it may be empty. All input is guaranteed to be valid, i.e. each input string will only ever 
# consist of 'G', 'C', 'A' and/or 'T'.
# -----------------------------------------------------------

import string

def dna_to_rna(dna):
    rna = str.maketrans("T", "U")
    return dna.translate(rna)

# or

def dna_to_rna(dna):
    return dna.replace("T", "U")

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