# -----------------------------------------------------------
# #Description
# 
# Everybody has probably heard of the animal heads and legs problem from the earlier years at school. It goes:
# 
# “A farm contains chickens and cows. There are x heads and y legs. How many chickens and cows are there?”
# 
# Where x <= 1000 and y <=1000
# 
# #Task
# 
# Assuming there are no other types of animals, work out how many of each animal are there.
# 
# Return a tuple in Python - (chickens, cows) and an array list - [chickens, cows]/{chickens, cows} in all other languages
# 
# If either the heads & legs is negative, the result of your calculation is negative or the calculation is a float return "No solutions" (no valid cases), or [-1, 
# -1] in COBOL.
# 
# In the form:
# 
# (Heads, Legs) = (72, 200)
# 
# VALID - (72, 200) =>             (44 , 28) 
#                              (Chickens, Cows)
# 
# INVALID - (72, 201) => "No solutions"
# 
# However, if 0 heads and 0 legs are given always return [0, 0] since zero heads must give zero animals.
# 
# There are many different ways to solve this, but they all give the same answer.
# 
# You will only be given integers types - however negative values (edge cases) will be given.
# 
# Happy coding!
# -----------------------------------------------------------

def animals(heads, legs):
    farm = (2*heads - legs/2, legs/2 - heads)
    if legs % 2 == 0 and farm[0] >= 0 and farm[1] >= 0:
        return farm
    else:
        return 'No solutions'

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