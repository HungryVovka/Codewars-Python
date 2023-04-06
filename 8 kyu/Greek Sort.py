# -----------------------------------------------------------
# Write a comparator for a list of phonetic words for the letters of the greek alphabet.
# 
# A comparator is:
# 
# a custom comparison function of two arguments (iterable elements) which should return a negative, zero or positive number depending on 
# whether the first argument is considered smaller than, equal to, or larger than the second argument
# 
# (source: https://docs.python.org/2/library/functions.html#sorted)
# 
# The greek alphabet is preloded for you as greek_alphabet:
# 
# greek_alphabet = (
#     'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 
#     'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 
#     'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
#     'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')
# 
# Examples
# greek_comparator('alpha', 'beta')   <  0
# greek_comparator('psi', 'psi')      == 0
# greek_comparator('upsilon', 'rho')  >  0
# -----------------------------------------------------------

greek_comparator = lambda x, y, f = greek_alphabet.index: f(x) - f(y)

# or

def greek_comparator(lhs, rhs):
    return greek_alphabet.index(lhs) - greek_alphabet.index(rhs)

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