# -----------------------------------------------------------
# You're running an online business and a big part of your day is fulfilling orders. As your volume picks up that's been taking more of your time, and 
# unfortunately lately you've been running into situations where you take an order but can't fulfill it.
# 
# You've decided to write a function fillable() that takes three arguments: a dictionary stock representing all the merchandise you have in stock, 
# a string merch representing the thing your customer wants to buy, and an integer n representing the number of units of merch they would like to 
# buy. Your function should return True if you have the merchandise in stock to complete the sale, otherwise it should return False.
# 
# Valid data will always be passed in and n will always be >= 1.
# -----------------------------------------------------------

def fillable(stock, merch, n):
    return stock.get(merch, 0) >= n

# or

def fillable(stock, merch, n):
    return merch in stock and stock[merch] >= n

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