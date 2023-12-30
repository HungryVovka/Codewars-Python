# -----------------------------------------------------------
# Middle Earth is about to go to war. The forces of good will have many battles with the forces of evil. Different races will certainly be involved. Each 
# race has a certain worth when battling against others. On the side of good we have the following races, with their associated worth:
# 
# Hobbits: 1
# Men: 2
# Elves: 3
# Dwarves: 3
# Eagles: 4
# Wizards: 10
# 
# On the side of evil we have:
# 
# Orcs: 1
# Men: 2
# Wargs: 2
# Goblins: 2
# Uruk Hai: 3
# Trolls: 5
# Wizards: 10
# 
# Although weather, location, supplies and valor play a part in any battle, if you add up the worth of the side of good and compare it with the worth of 
# the side of evil, the side with the larger worth will tend to win.
# 
# Thus, given the count of each of the races on the side of good, followed by the count of each of the races on the side of evil, determine which side 
# wins.
# 
# Input:
# The function will be given two parameters. Each parameter will be a string of multiple integers separated by a single space. Each string will contain 
# the count of each race on the side of good and evil.
# 
# The first parameter will contain the count of each race on the side of good in the following order:
# 
# Hobbits, Men, Elves, Dwarves, Eagles, Wizards.
# The second parameter will contain the count of each race on the side of evil in the following order:
# 
# Orcs, Men, Wargs, Goblins, Uruk Hai, Trolls, Wizards.
# All values are non-negative integers. The resulting sum of the worth for each side will not exceed the limit of a 32-bit integer.
# 
# Output:
# Return "Battle Result: Good triumphs over Evil" if good wins, "Battle Result: Evil eradicates all trace of Good" if evil wins, or 
# "Battle Result: No victor on this battle field" if it ends in a tie.

def good_vs_evil(good, evil):
    good_worth = (1, 2, 3, 3, 4, 10)
    evil_worth = (1, 2, 2, 2, 3, 5, 10)
    good_power = [int(g) for g in good.split()] 
    evil_power = [int(e) for e in evil.split()]
    total = lambda power, worth: \
    sum([worth[i] * power[i] for i in range(len(power))])
    good_total = total(good_power, good_worth)
    evil_total = total(evil_power, evil_worth)
    outcome = {
        good_total > evil_total: 
        "Battle Result: Good triumphs over Evil",
        good_total < evil_total: 
        "Battle Result: Evil eradicates all trace of Good",
        good_total == evil_total: 
        "Battle Result: No victor on this battle field"
    }
    return outcome[True]

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