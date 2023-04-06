# -----------------------------------------------------------
# Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed as an empty String).
# 
# Assuming that name is a String and it checks for user typos to return a name with a first capital letter (Xxxx).
# 
# Examples:
# 
# * With `name` = "john"  => return "Hello, John!"
# * With `name` = "aliCE" => return "Hello, Alice!"
# * With `name` not given 
#   or `name` = ""        => return "Hello, World!"
# -----------------------------------------------------------

def hello(name=""):
    if name != "":
        name = str.capitalize(str.lower(name))
        return "Hello, %s!" % (name)
    else:
        return "Hello, World!"

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