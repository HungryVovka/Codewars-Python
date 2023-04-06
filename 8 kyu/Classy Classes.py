# -----------------------------------------------------------
# Classy Classes
# Basic Classes, this kata is mainly aimed at the new JS ES6 Update introducing classes
# 
# Task
# Your task is to complete this Class, the Person class has been created. You must fill in the Constructor method to accept a name as string and an age 
# as number, complete the get Info property and getInfo method/Info getter which should return johns age is 34
# 
# Reference: https://docs.python.org/3/tutorial/classes.html
# -----------------------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = "%ss age is %d" % (name, age)

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