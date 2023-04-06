# -----------------------------------------------------------
# Given a sequence of items and a specific item in that sequence, return the item immediately following the item specified. If the item occurs more 
# than once in a sequence, return the item after the first occurence. This should work for a sequence of any type.
# 
# When the item isn't present or nothing follows it, the function should return nil in Clojure and Elixir, Nothing in Haskell, undefined in JavaScript, 
# None in Python.
# 
# next_item([1, 2, 3, 4, 5, 6, 7], 3) # => 4
# next_item(['Joe', 'Bob', 'Sally'], 'Bob') # => "Sally"
# -----------------------------------------------------------

def next_item(xs, item):
    nexti = iter(xs)
    for i in nexti:
        if i == item:
            break
    return next(nexti, None)

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