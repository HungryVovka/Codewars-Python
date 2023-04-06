# -----------------------------------------------------------
# Imagine you are creating a game where the user has to guess the correct number. But there is a limit of how many guesses the user can do.
# 
# If the user tries to guess more than the limit, the function should throw an error.
# If the user guess is right it should return true.
# If the user guess is wrong it should return false and lose a life.
# 
# Can you finish the game so all the rules are met?
# -----------------------------------------------------------

class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
    
    def guess(self, n):
        if self.lives == 0:
            raise "No more lives, try again!"
        elif n == self.number:
            return True
        self.lives -= 1
        return False

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