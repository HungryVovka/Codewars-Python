# -----------------------------------------------------------
# You need to write a function that reverses the words in a given string. A word can also fit an empty string. If this is not clear enough, here are some 
# examples:
# 
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
# 
# Example (Input --> Output)
# 
# "Hello World" --> "World Hello"
# "Hi There." --> "There. Hi"
# 
# Happy coding!
# -----------------------------------------------------------

def reverse(st):
    st = st.split()
    return " ".join(st[::-1])

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