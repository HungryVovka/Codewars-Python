# -----------------------------------------------------------
# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still 
# correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.
# 
# Your task is to write a function maskify, which changes all but the last four characters into '#'.
# 
# Examples
# "4556364607935616" --> "############5616"
#      "64607935616" -->      "#######5616"
#                "1" -->                "1"
#                 "" -->                 ""
# 
# // "What was the name of your first pet?"
# 
# "Skippy" --> "##ippy"
# 
# "Nananananananananananananananana Batman!"
# -->
# "####################################man!"
# -----------------------------------------------------------

def maskify(cc):
    return "#" * (len(cc) - 4) + cc[-4:]

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