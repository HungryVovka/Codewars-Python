# -----------------------------------------------------------
# Task
# Given an array/list [] of n integers , find maximum triplet sum in the array Without duplications .
# 
# Notes :
# Array/list size is at least 3 .
# 
# Array/list numbers could be a mixture of positives , negatives and zeros .
# 
# Repetition of numbers in the array/list could occur , So (duplications are not included when summing).
# 
# Input >> Output Examples
# 1- maxTriSum ({3,2,6,8,2,3}) ==> return (17)
# 
# Explanation:
# As the triplet that maximize the sum {6,8,3} in order , their sum is (17)
# 
# Note : duplications are not included when summing , (i.e) the numbers added only once .
# 
# 2- maxTriSum ({2,1,8,0,6,4,8,6,2,4}) ==> return (18)
# 
# Explanation:
# As the triplet that maximize the sum {8, 6, 4} in order , their sum is (18) ,
# 
# Note : duplications are not included when summing , (i.e) the numbers added only once .
# 
# 3- maxTriSum ({-7,12,-7,29,-5,0,-7,0,0,29}) ==> return (41)
# 
# Explanation:
# As the triplet that maximize the sum {12 , 29 , 0} in order , their sum is (41) ,
# 
# Note : duplications are not included when summing , (i.e) the numbers added only once .
# 
# Playing with Numbers Series
# Playing With Lists/Arrays Series
# For More Enjoyable Katas
# ALL translations are welcomed
# Enjoy Learning !!
# Zizou
# -----------------------------------------------------------

def max_tri_sum(numbers):
    triplet = sorted(list(set(numbers)))
    return triplet[-1] + triplet[-2] + triplet[-3]

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