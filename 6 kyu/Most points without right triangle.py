# -----------------------------------------------------------
# Overview
# Given a 2-dimensional m * n rectangular grid with non-negative integer coordinates, can you develop an algorithm that will place the largest 
# possible number, P, of points on the grid without forming ANY right triangles in the resulting configuration of points ?
# 
# Language clarification: depending on your country, a "right triangle" can be also called "rectangle triangle", "orthogonal triangle", "right-angle 
# triangle" etc. It is a triangle which contains one angle that equals 90 degrees.
# 
# Inputs
# You will be given two positive integers, m >= 1 and n >= 1, representing the dimensions of an m * n rectangular grid with integer coordinates.
# 
# Values of m and n will be tested up to 50.
# 
# Outputs
# You must return a list (Python) of 2-element tuples, where each tuple represents the location of a point that you want to place in the 
# rectangular grid.
# 
# Each tuple must be of the form (x,y) where x and y must both be integers.
# 
# The order of the returned list does not matter, so no need to sort it etc.
# 
# We will count the integer coordinates from x = 0 and y = 0, so that the 4 corner points of the given grid will always be (0,0), (0,n-1), 
# (m-1,0), (m-1,n-1)
# 
# Troubleshooting and Test Explanation
# From your returned solution list, the tests will first check that your solution is valid i.e. that it contains integer 2-ples whose coordinates are not 
# outside the allowed range of 0 <= x <= m-1 and 0 <= y <= n-1.
# 
# Then the tests will check that there are no right triangles formed by any 3 of the points that you have placed.
# 
# Please pay attention to the possibility of forming right triangles whose right-angle is not "aligned" by the x- and y-axes.
# 
# For example, the triangle given by the 3 points {(1, 1), (2, 2), (1, 3)} is in fact a right triangle, even though you might not notice it in your grid.
# 
# Finally, if your solution list doesn't contain any right triangles, it will then be tested for optimality i.e. that you have managed to fit as many points as 
# possible into the grid.
# 
# If you fail at this last part of the tests, it is because there is a way to place even more points in the given grid than what you have found using your 
# current algorithm.
# 
# Example With NON-OPTIMAL Solution
# 
# Here we are dealing with an m=7 and n=5 grid; the 4 black points should clarify that the coordinates therefore start with x=0, y=0.
# 
# In this example, the user has succesfully placed a total of P = 6 points represented in red, so his solution would be returned as the list (order is not 
# important):
# 
# [(0,1), (1,3), (2,2), (4,2), (5,3), (6,1)]
# 
# You can confirm for yourself manually, or by using the solution-checker that is loaded in the test cases, that so far these P = 6 points do not form 
# any right triangles.
# 
# You can also experiment with the solution-checker and try adding any point with x-coordinate x = 3 to the above list; you will find that adding any 
# such point will create a right triangle somewhere.
# 
# Finally, this example with P = 6 points is not optimal for the given values of m and n: there are ways of placing P = 10 total points in this grid.
# -----------------------------------------------------------

# return a list of 2-ples of integers (x,y)
# e.g. [(12,4), (2,5), (7,0) ...]
# order of the returned list does not matter
def most_points(m,n):
    a = [(x, 0) for x in range(m)]
    b = [(0, y) for y in range(n)]
    if n == 1:
        return a
    if m == 1:
        return b
    return [(0, y) for y in range(1, n)] + [(x, 0) for x in range(1, m)]

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