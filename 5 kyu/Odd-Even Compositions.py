# -----------------------------------------------------------
# Introduction (skippable)
# Let's suppose you got a cake... : I eat it and the kata ends.
# 
# Consider it to weigh `3 hg`, with the smallest possible slice to weigh `1 hg`.
# In how many ways can you serve the whole cake?
# You can either avoid or use the knife:
# 3
# 2 + 1
# 1 + 2
# 1 + 1 + 1
# 
# It can be served in 4 different ways, assuming that order matters.
# 
# The number 3 has been expressed as the sum of natural numbers.
# This is called a composition : our cake has 4 compositions.
# 
# Notice that if order didn't matter it would be called a partition.
# Thus there would have been 3 partitions, being 2+1 and 1+2 considered the same.
# 
# Description
# Partitions sound like constrained Compositions.
# What if another aspect of Compositions, instead of order, gets restricted ?
# Let's call these odd-even compositions and call the number to decompose "N".
# N = 4
# To reach 4 we can...
# 
# Compositions		Odd-Even Compositions
# 4	4
# 3 + 1				3 + 1
# 2 + 2				2 + 2
# 2 + 1 + 1			2 + 1 + 1
# 1 + 3				1 + 3
# 1 + 2 + 1			1 + 2 + 1
# 1 + 1 + 2			1 + 1 + 2
# 1 + 1 + 1 + 1		1 + 1 + 1 + 1
# Total : 8			Total : 6
# 
# And back to the example of the cake (notice the similarity with the previous example): N = 3
# To reach 3 we can...
# 
# Compositions		Odd-Even Compositions
# 3					3
# 2 + 1				2 + 1
# 1 + 2				1 + 2
# 1 + 1 + 1			1 + 1 + 1
# Total : 4			Total : 3
# 
# Notice how numbers are highlighted:
# Gray numbers are always valid.
# i.e. 1 and the number itself (which is N).
# 
# Green numbers are valid because they share parity/disparity with N
# with N=4, 2 is valid because both are even.
# 
# Red numbers are not valid because they don't share parity/disparity with N
# back to the first example, 3 is not valid because it is odd, while 4 is even.
# 
# Thus about the first example (N=4):
# "3+1" is invalid :
# 3 is red because 3 is odd while 4 (N) is even.
# 
# "1+2+1" is invalid :
# 1 is gray and N becomes N=N-1 --> N=3
# 2 is red because 2 is even while 3 (N) is odd.
# 
# "1+3" is valid :
# 1 is gray and N becomes N=N-1 --> N=3
# 3 is gray because 3 is the number itself (N=3)
# 
# "2+2" is valid :
# 2 is green because 2 and 4(N) are even, so N=N-2 --> N=2
# 2 is gray because 2 is the number itself (N=2)
# 
# Task
# Return the number of odd-even compositions* by which the given number can be expressed.
# * didn't know how else to call them D: ... i've just "invented" the name
# 
# Warning
# The given numbers will range from 0 to 10^3 inclusive, then time-out may occur if your solution isn't fast enough.
# If input is 0 return 1.
# 
# Other Examples
# odd_even_compositions(0)   # returns 1
# 
# odd_even_compositions(7)   # returns 27
# 
# odd_even_compositions(28)  # returns 3188646
# 
# Hints
# If additions feel weird, try to express the concept using subtractions.
# I asked you to calculate odd-even compositions.
# What if i asked to calculate compositions?
# -----------------------------------------------------------

def odd_even_compositions(n):
    if n <= 1:
        return 1
    answer = 3**((n - 1) // 2)
    if n % 2 != 0:
        return answer
    return answer * 2

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