# -----------------------------------------------------------
# Given two strings comprised of + and -, return a new string which shows how the two strings interact in the following way:
# 
# When positives and positives interact, they remain positive.
# When negatives and negatives interact, they remain negative.
# But when negatives and positives interact, they become neutral, and are shown as the number 0.
# 
# Worked Example
# ("+-+", "+--") ➞ "+-0"
# # Compare the first characters of each string, then the next in turn.
# # "+" against a "+" returns another "+".
# # "-" against a "-" returns another "-".
# # "+" against a "-" returns "0".
# # Return the string of characters.
# 
# Examples
# ("--++--", "++--++") ➞ "000000"
# 
# ("-+-+-+", "-+-+-+") ➞ "-+-+-+"
# 
# ("-++-", "-+-+") ➞ "-+00"
# 
# Notes
# The two strings will be the same length.
# -----------------------------------------------------------

def neutralise(s1, s2):
    answer = ""
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            answer += s1[i]
        else:
            answer += "0"
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