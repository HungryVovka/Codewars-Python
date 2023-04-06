# -----------------------------------------------------------
# Convert a hash into an array. Nothing more, Nothing less.
# 
# {name: 'Jeremy', age: 24, role: 'Software Engineer'}
# 
# should be converted into
# 
# [["age", 24], ["name", "Jeremy"], ["role", "Software Engineer"]]
# 
# Note: The output array should be sorted alphabetically by key name.
# 
# Good Luck!
# -----------------------------------------------------------

def convert_hash_to_array(hash):
    return sorted(map(list, hash.items()))

# or

def convert_hash_to_array(hash):
    return sorted(list(h) for h in hash.items())

# or

def convert_hash_to_array(hash):
    return [[h, hash[h]] for h in sorted(hash)]

# or

def convert_hash_to_array(hash):
    return [[h, i] for h, i in sorted(hash.items())]

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