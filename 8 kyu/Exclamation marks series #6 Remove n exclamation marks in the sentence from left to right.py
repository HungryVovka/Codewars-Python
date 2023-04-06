# -----------------------------------------------------------
# Description:
# Remove n exclamation marks in the sentence from left to right. n is positive integer.
# 
# Examples
# remove("Hi!",1) === "Hi"
# remove("Hi!",100) === "Hi"
# remove("Hi!!!",1) === "Hi!!"
# remove("Hi!!!",100) === "Hi"
# remove("!Hi",1) === "Hi"
# remove("!Hi!",1) === "Hi!"
# remove("!Hi!",100) === "Hi"
# remove("!!!Hi !!hi!!! !hi",1) === "!!Hi !!hi!!! !hi"
# remove("!!!Hi !!hi!!! !hi",3) === "Hi !!hi!!! !hi"
# remove("!!!Hi !!hi!!! !hi",5) === "Hi hi!!! !hi"
# remove("!!!Hi !!hi!!! !hi",100) === "Hi hi hi"
# -----------------------------------------------------------

def remove(s, n):
    arr = []
    i = 1
    for j in range(len(s)):
        if s[j] == "!" and i <= n:
            i += 1
        else:
            arr.append(s[j])
    return "".join(arr)

# or

def remove(s, n):
    return s.replace("!", "", n)

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