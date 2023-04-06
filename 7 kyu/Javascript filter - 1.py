# -----------------------------------------------------------
# While developing a website, you detect that some of the members have troubles logging in. Searching through the code you find that all logins 
# ending with a "_" make problems. So you want to write a function that takes an array of pairs of login-names and e-mails, and outputs an array of all 
# login-name, e-mails-pairs from the login-names that end with "_".
# 
# If you have the input-array:
# 
# [ [ "foo", "foo@foo.com" ], [ "bar_", "bar@bar.com" ] ]
# 
# it should output
# 
# [ [ "bar_", "bar@bar.com" ] ]
# 
# You have to use the filter-method which returns each element of the array for which the filter-method returns true.
# 
# https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter
# -----------------------------------------------------------

def search_names(logins):
    problems = lambda x: x[0].endswith("_")
    return list(filter(problems, logins))

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