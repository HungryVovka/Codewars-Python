# -----------------------------------------------------------
# Write a function that calculates the original product price, without VAT.
# 
# Example
# If a product price is 200.00 and VAT is 15%, then the final product price (with VAT) is: 200.00 + 15% = 230.00
# 
# Thus, if your function receives 230.00 as input, it should return 200.00
# 
# Notes:
# 
# VAT is always 15% for the purposes of this Kata.
# Round the result to 2 decimal places.
# If null value given then return -1
# -----------------------------------------------------------

def excluding_vat_price(price):
    if price == None:
        return -1
    else:
        return round(price / 115 * 100, 2)

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