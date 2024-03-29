# -----------------------------------------------------------
# Tired of those repetitive javascript challenges? Here's a unique hackish one that should keep you busy for a while ;)
# 
# There's a mystery function which is already available for you to use. It's a simple function called mystery. It accepts a string as a parameter and 
# outputs a string. The exercise depends on guessing what this function actually does.
# 
# You can call the mystery function like this:
# 
# my_output = mystery("my_input")
# 
# Using your own test cases, try to call the mystery function with different input strings and try to analyze its output in order to guess what is does. 
# You are free to call the mystery function in your own test cases however you want.
# 
# When you think you've understood how my mystery function works, prove it by reimplementing its logic in a function that you should call 'solved(x)'. 
# To validate your code, your function 'solved' should return the same output as my function 'mystery' given the same inputs.
# 
# Beware! Passing your own test cases doesn't imply you'll pass mine.
# 
# Cheaters are welcome :)
# 
# Have fun!
# -----------------------------------------------------------

def solved(s):
    t = len(s)
    o = int((t - 1) / 2)
    if t % 2 != 0:
        s = s[:o] + s[o + 1:]
    return "".join(sorted(s))

# or

def solved(s):
    return "".join(sorted(s[:len(s)//2] + s[(len(s)//2)+1:] if  len(s) % 2 != 0 else s))

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