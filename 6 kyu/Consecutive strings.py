# -----------------------------------------------------------
# You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings 
# taken in the array.
# 
# Examples:
# strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2
# 
# Concatenate the consecutive strings of strarr by 2, we get:
# 
# treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
# folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
# trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
# blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
# abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]
# 
# Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
# The first that came is "folingtrashy" so 
# longest_consec(strarr, 2) should return "folingtrashy".
# 
# In the same way:
# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
# 
# n being the length of the string array, if n = 0 or k > n or k <= 0 return "" (return Nothing in Elm, "nothing" in Erlang).
# 
# Note
# consecutive strings : follow one after another without an interruption
# -----------------------------------------------------------

def longest_consec(strarr, k):
    longest = ""
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ""
    for i in range(n - k + 1):
        check = "".join(strarr[i:i + k])
        if len(longest) < len(check):
            longest = check
    return longest

# or

def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ""
    options = ["".join(strarr[i:i + k]) for i in range(n - k + 1)]
    return max(options, key=len)

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