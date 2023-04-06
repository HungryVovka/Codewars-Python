# -----------------------------------------------------------
# We have implemented a function wrap(value) that takes a value of arbitrary type and wraps it in a new JavaScript Object or Python Dict setting the 
# 'value' key on the new Object or Dict to the passed-in value.
# 
# So, for example, if we execute the following code:
# 
# wrapper_obj = wrap("my_wrapped_string"); 
#  # wrapper_obj should be  {"value":"my_wrapped_string"}
# 
# We would then expect the following statement to be true:
# 
# wrapper_obj["value"] == "my_wrapped_string"
# 
# Unfortunately, the code is not working as designed. Please fix the code so that it behaves as specified.
# -----------------------------------------------------------

def wrap(value):
    return {"value": value}

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