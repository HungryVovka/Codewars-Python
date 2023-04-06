# -----------------------------------------------------------
# Make a program that filters a list of strings and returns a list with only your friends name in it.
# 
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
# 
# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
# 
# i.e.
# 
# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
# 
# Note: keep the original order of the names in the output.
# -----------------------------------------------------------

def friend(x):
    arr = []
    for name in x:
        if len(name) != 4:
            continue
        elif name.isdigit():
            continue
        else:
            arr.append(name)
    return arr

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