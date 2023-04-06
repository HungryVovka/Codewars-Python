# -----------------------------------------------------------
# Haskell has some useful functions for dealing with lists:
# 
# $ ghci
# GHCi, version 7.6.3: http://www.haskell.org/ghc/  :? for help
# λ head [1,2,3,4,5]
# 1
# λ tail [1,2,3,4,5]
# [2,3,4,5]
# λ init [1,2,3,4,5]
# [1,2,3,4]
# λ last [1,2,3,4,5]
# 5
# 
# Your job is to implement these functions in your given language. Make sure it doesn't edit the array; that would cause problems! Here's a cheat 
# sheet:
# 
# | HEAD | <----------- TAIL ------------> |
# [  1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
# | <----------- INIT ------------> | LAST |
# 
# head [x] = x
# tail [x] = []
# init [x] = []
# last [x] = x
# 
# Here's how I expect the functions to be called in your language:
# 
# head([1,2,3,4,5]) => 1
# tail([1,2,3,4,5]) => [2,3,4,5]
# 
# Most tests consist of 100 randomly generated arrays, each with four tests, one for each operation. There are 400 tests overall. No empty arrays will 
# be given. Haskell has QuickCheck tests
# -----------------------------------------------------------

def head(arr):
    return arr[0]

def tail(arr):
    return arr[1:]

def init(arr):
    return arr[0: -1]

def last(arr):
    return arr[len(arr) - 1]

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