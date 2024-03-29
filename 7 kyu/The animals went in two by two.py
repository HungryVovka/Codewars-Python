# -----------------------------------------------------------
# A great flood has hit the land, and just as in Biblical times we need to get the animals to the ark in pairs. We are only interested in getting one pair of 
# each animal, and not interested in any animals where there are less than 2....they need to mate to repopulate the planet after all!
# 
# You will be given a list of animals, which you need to check to see which animals there are at least two of, and then return a dictionary containing the 
# name of the animal along with the fact that there are 2 of them to bring onto the ark.
# 
# >>> two_by_two(['goat', 'goat', 'rabbit', 'rabbit', 'rabbit', 'duck', 'horse', 'horse', 'swan'])
# {'goat': 2, 'horse': 2, 'rabbit': 2}
# 
# # If the list of animals is empty, return False as there are no animals to bring onto the ark and we are all doomed!!!
# >>> two_by_two([])
# False
# 
# # If there are no pairs of animals, return an empty dictionary
# >>> two_by_two(['goat'])
# {}
# -----------------------------------------------------------

def two_by_two(animals):
    return False if not animals else {animal: 2 for animal in animals if animals.count(animal) > 1}

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