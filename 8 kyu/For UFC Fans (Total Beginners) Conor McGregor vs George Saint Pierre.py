# -----------------------------------------------------------
# This is a beginner friendly kata especially for UFC/MMA fans.
# 
# It's a fight between the two legends: Conor McGregor vs George Saint Pierre in Madison Square Garden. Only one fighter will remain standing, and 
# after the fight in an interview with Joe Rogan the winner will make his legendary statement. It's your job to return the right statement depending on 
# the winner!
# 
# If the winner is George Saint Pierre he will obviously say:
# 
# "I am not impressed by your performance."
# 
# If the winner is Conor McGregor he will most undoubtedly say:
# 
# "I'd like to take this chance to apologize.. To absolutely NOBODY!"
# 
# Good Luck!
# 
# Note
# The given name may varies in casing, eg., it can be "George Saint Pierre" or "geOrGe saiNT pieRRE". Your solution should treat both as the same 
# thing (case-insensitive).
# -----------------------------------------------------------

def quote(fighter):
    conor = "conor mcgregor"
    return "I am not impressed by your performance." if fighter.lower() != conor \
        else "I'd like to take this chance to apologize.. To absolutely NOBODY!"

# or

quotes = {
    "george saint pierre" : "I am not impressed by your performance.",
    "conor mcgregor" : "I'd like to take this chance to apologize.. To absolutely NOBODY!",
}

def quote(fighter):
    return quotes[fighter.lower()]

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