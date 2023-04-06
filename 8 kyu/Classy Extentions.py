# -----------------------------------------------------------
# Classy Extensions
# Classy Extensions, this kata is mainly aimed at the new JS ES6 Update introducing extends keyword. You will be preloaded with the Animal class, so 
# you should only edit the Cat class.
# 
# Task
# Your task is to complete the Cat class which Extends Animal and replace the speak method to return the cats name + meows. e.g. 
# 'Mr Whiskers meows.'
# 
# The name attribute is passed with this.name (JS), @name (Ruby) or self.name (Python).
# 
# Reference: JS, Ruby, Python.
# -----------------------------------------------------------

class Cat(Animal):
    def speak(self):
        return self.name + " meows."

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