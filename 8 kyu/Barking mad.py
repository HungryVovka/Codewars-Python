# -----------------------------------------------------------
# Teach snoopy and scooby doo how to bark using object methods. Currently only snoopy can bark and not scooby doo.
# 
# snoopy.bark() #return "Woof"
# scoobydoo.bark() #undefined
# 
# Use method prototypes to enable all Dogs to bark.
# -----------------------------------------------------------

class Dog():
    def __init__(self, breed):
        self.breed = breed
        self.bark = lambda: "Woof"
    
snoopy, scoobydoo = Dog("Beagle"), Dog("Great Dane")

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