# -----------------------------------------------------------
# Switch/Case - Bug Fixing #6
# 
# Oh no! Timmy's evalObject function doesn't work. He uses Switch/Cases to evaluate the given properties of an object, can you fix timmy's function?
# -----------------------------------------------------------

def eval_object(v):
    operation = {
        "+": v["a"] + v["b"],
        "-": v["a"] - v["b"],
        "/": v["a"] / v["b"],
        "*": v["a"] * v["b"],
        "%": v["a"] % v["b"],
        "**": v["a"] ** v["b"],
    }
    return operation.get(v["operation"])

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