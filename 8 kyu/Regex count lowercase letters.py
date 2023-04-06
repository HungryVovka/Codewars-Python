# -----------------------------------------------------------
# Your task is simply to count the total number of lowercase letters in a string.
# 
# Examples
# lowercaseCount("abc"); ===> 3
# 
# lowercaseCount("abcABC123"); ===> 3
# 
# lowercaseCount("abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~"); ===> 3
# 
# lowercaseCount(""); ===> 0;
# 
# lowercaseCount("ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~"); ===> 0
# 
# lowercaseCount("abcdefghijklmnopqrstuvwxyz"); ===> 26
# -----------------------------------------------------------

def lowercase_count(strng):
    low_count = 0
    for i in list(strng):
        if i.islower():
            low_count += 1
    return low_count

# or

def lowercase_count(strng):
    return sum(i.islower() for i in strng)

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