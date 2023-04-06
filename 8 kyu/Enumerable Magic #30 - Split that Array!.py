# -----------------------------------------------------------
# Create a method partition that accepts a list and a method/block. It should return two arrays: the first, with all the elements for which the given 
# block returned true, and the second for the remaining elements.
# 
# Here's a simple Ruby example:
# 
# animals = ["cat", "dog", "duck", "cow", "donkey"]
# partition(animals){|animal| animal.size == 3}
#     #=> [["cat", "dog", "cow"], ["duck", "donkey"]]
# 
# The equivalent in Python would be:
# 
# animals = ['cat', 'dog', 'duck', 'cow', 'donkey']
# partition(animals, lambda x: len(x) == 3)
#     # (['cat', 'dog', 'cow'], ['duck', 'donkey'])
# 
# If you need help, here's a reference:
# 
# http://www.rubycuts.com/enum-partition
# -----------------------------------------------------------

def partition(arr, classifier_method):
    return ([i for i in arr if classifier_method(i)], \
           [j for j in arr if not classifier_method(j)])

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