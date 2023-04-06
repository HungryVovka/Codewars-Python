# -----------------------------------------------------------
# You can print your name on a billboard ad. Find out how much it will cost you. Each letter has a default price of £30, but that can be different if you 
# are given 2 parameters instead of 1.
# 
# You can not use multiplier "*" operator.
# 
# If your name would be Jeong-Ho Aristotelis, ad would cost £600. 20 leters * 30 = 600 (Space counts as a letter).
# -----------------------------------------------------------

def billboard(name, price=30):
    i = 1
    pricelist = price
    while i < len(name):
        pricelist += price
        i += 1
    return(pricelist)

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