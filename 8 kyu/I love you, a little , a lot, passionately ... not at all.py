# -----------------------------------------------------------
# Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the following phrases each 
# time a petal was torn:
# 
# I love you
# a little
# a lot
# passionately
# madly
# not at all
# 
# When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.
# 
# Your goal in this kata is to determine which phrase the girls would say for a flower of a given number of petals, where nb_petals > 0.
# -----------------------------------------------------------

def how_much_i_love_you(nb_petals):
    if (nb_petals == 1) or ((nb_petals % 6) == 1):
        return("I love you")
    if (nb_petals == 2) or ((nb_petals % 6) == 2):
        return("a little")
    if (nb_petals == 3) or ((nb_petals % 6) == 3):
        return("a lot")
    if (nb_petals == 4) or ((nb_petals % 6) == 4):
        return("passionately")
    if (nb_petals == 5) or ((nb_petals % 6) == 5):
        return("madly")
    if (nb_petals == 6) or ((nb_petals % 6) == 0):
        return("not at all")

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