# -----------------------------------------------------------
# Complete the function/method so that it returns the url with anything after the anchor (#) removed.
# 
# Examples
# "www.codewars.com#about" --> "www.codewars.com"
# "www.codewars.com?page=1" -->"www.codewars.com?page=1"
# -----------------------------------------------------------

def remove_url_anchor(url):
    new_url = ""
    for i in url:
        if i == "#":
            break
        new_url += i
    return new_url

# or

def remove_url_anchor(url):
    return url.partition("#")[0]

# or

def remove_url_anchor(url):
    return url.split("#")[0]

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