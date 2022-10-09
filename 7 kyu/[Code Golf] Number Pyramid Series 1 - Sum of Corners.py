# -----------------------------------------------------------
# Number Pyramid
# Image a number pyramid starts with 1, and the numbers increasing by 1.
# 
# For example, when the pyramid has 3 levels:
# 
#   1
#  2 3
# 4 5 6
# 
# And the sum of three corners are:
# 
# 1 + 4 + 6 = 11
# 
# Input:
# You will be given a number n, which means how many levels the pyramid has.
# 
# 0 <= n <= 5000
# 
# Output:
# You need to return the sum of three corners of the pyramid.
# 
# When there is no level, return 0 as there is no corner.
# 
# When there is only one level, return 1 as it is the only corner.
# 
# Examples:
# 
# sum_corners(0) --> 0
# sum_corners(1) --> 1
# sum_corners(2) --> 6
# sum_corners(3) --> 11
# 
# Golfing Message:
# The length of your code should be less or equal to 35.
# -----------------------------------------------------------

sum_corners = lambda x: (x>1)*2+x*x