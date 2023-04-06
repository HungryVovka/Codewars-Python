# -----------------------------------------------------------
# Terminal Game - Create Hero Prototype
# In this first kata in the series, you need to define a Hero prototype to be used in a terminal game. The hero should have the following attributes:
# 
# attribute			value
# name				user argument or 'Hero'
# position			'00'
# health			100
# damage			5
# experience		0
# -----------------------------------------------------------

class Hero(object):
    def __init__(self, name = "Hero", health = 100, damage = 5, \
                 experience = 0, position = "00"):
        self.name = name
        self.health = health
        self.damage = damage
        self.experience = experience
        self.position = position

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