# -----------------------------------------------------------
# Task
# You will be given a list of objects. Each object has type, material, and possibly secondMaterial. The existing materials are: paper, glass, 
# organic, and plastic.
# 
# Your job is to sort these objects across the 4 recycling bins according to their material (and secondMaterial if it's present), by listing the type's of 
# objects that should go into those bins.
# 
# Notes
# The bins should come in the same order as the materials listed above
# All bins should be listed in the output, even if some of them are empty
# If an object is made of two materials, its type should be listed in both of the respective bins
# The order of the type's in each bin should be the same as the order of their respective objects was in the input list
# Contrary to the example below, the output in Python should be a tuple of 4 lists instead of a 2-dimensional list
# 
# Example
# input = [
#   {"type": "rotten apples", "material": "organic"},
#   {"type": "out of date yogurt", "material": "organic", "secondMaterial": "plastic"},
#   {"type": "wine bottle", "material": "glass", "secondMaterial": "paper"},
#   {"type": "amazon box", "material": "paper"},
#   {"type": "beer bottle", "material": "glass", "secondMaterial": "paper"}
# ]
# 
# output = [
#   ["wine bottle", "amazon box", "beer bottle"],
#   ["wine bottle", "beer bottle"],
#   ["rotten apples", "out of date yogurt"],
#   ["out of date yogurt"]
# ]
# -----------------------------------------------------------

def recycle(a):
    materials = ["paper", "glass", "organic", "plastic"]
    answer = ([],[],[],[])
    for i in a:
        answer[materials.index(i["material"])].append(i["type"])
        if "secondMaterial" in i.keys():
            answer[materials.index(i["secondMaterial"])].append(i["type"])
    return answer

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