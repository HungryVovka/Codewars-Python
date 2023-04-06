# -----------------------------------------------------------
# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the 
# text that should be displayed next to such an item.
# 
# Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the 
# examples:
# 
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.
# -----------------------------------------------------------

def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return '%s likes this' % names[0]
    elif len(names) == 2:
        return '%s and %s like this' % (names[0], names[1])
    elif len(names) == 3:
        return '%s, %s and %s like this' % (names[0], names[1], names[2])
    else:
        return '%s, %s and %s others like this' % (names[0], names[1], str(len(names) - 2))

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