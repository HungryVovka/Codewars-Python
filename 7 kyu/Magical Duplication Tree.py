# -----------------------------------------------------------
# Story (skippable):
# Once upon a time, a farmer came across a magic seed shop. Once inside, the salesman sold him a pack of magical trees. Before leaving, the salesman 
# gave him a warning:
# 
# "These are no ordinary trees, farmer. These trees split up into smaller, further dividing duplicate trees with each passing day," The salesperson said.
# 
# The farmer returned home with his purchase and decided to clear a patch of land for the new crop. He planted one down in the middle of his field. 
# Upon returning the next day, the farmer was greeted by two slightly smaller trees in place of the original tree, as promised.
# 
# The farmer got both very excited and very nervous. He realized he had an easy way to turn a profit. That was great news for him! But he also figured 
# he had no idea of how to predict and report what his profits would be.
# 
# The farmer needs your help coding a function that can return what the field will look like after a certain number of days.
# 
# Task:
# You are given a multi-line string p_field containing a single magic tree that recursively divides itself into a split number of shorter copies every 
# day. Return the p_field after n days. The tree's splitting decreases its height by one | each generation.
# 
# Only valid tree's will be asked for, there will be no asking for splitting for more days than possible.
# 
# WARNING: These fields can get BIG!!! Make sure your code runs efficiently.
# 
# Example:
# The following is the start of a p_field with a split value of 2:
# 
# o
# |
# |
# |
# 
# On day 1, the field will look like this:
# 
# oo  
# ||
# ||
# 
# The next day, the field would grow to this:
# 
# oooo
# ||||
# 
# In 3 days, which is the maximum possible n value for this example, the field will look like this:
# 
# oooooooo 
# 
# If n is 2, your function needs to return the third p_field displayed and return the fourth example if n was 3.
# 
# If split is 3, the function instead returns ooooooooooooooooooooooooooo on the third day. (1 => 3 => 9 => 27)
# -----------------------------------------------------------

def magic_plant(p_field, split, n):
    tree = p_field.split("\n")
    tree = tree[:len(tree) - n]
    return "\n".join(i * (split**n) for i in tree)

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