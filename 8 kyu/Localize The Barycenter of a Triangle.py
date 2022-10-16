# -----------------------------------------------------------
# The medians of a triangle are the segments that unit the vertices with the midpoint of their opposite sides. The three medians of a triangle intersect 
# at the same point, called the barycenter or the centroid. Given a triangle, defined by the cartesian coordinates of its vertices we need to localize its 
# barycenter or centroid.
# 
# The function bar_triang() or barTriang or bar-triang, receives the coordinates of the three vertices A, B and C  as three different arguments 
# and outputs the coordinates of the barycenter O in an array [xO, yO]
# 
# This is how our asked function should work: the result of the coordinates should be expressed up to four decimals, (rounded result).
# 
# You know that the coordinates of the barycenter are given by the following formulas.
# 
# xO = (xA + xB + xC) / 3
# yO = (yA + yB + yC) / 3
# 
# For additional information about this important point of a triangle see at: (https://en.wikipedia.org/wiki/Centroid)
# 
# Let's see some cases:
# 
# bar_triang([4, 6], [12, 4], [10, 10]) ------> [8.6667, 6.6667]
# 
# bar_triang([4, 2], [12, 2], [6, 10] ------> [7.3333, 4.6667]
# 
# The given points form a real or a degenerate triangle but in each case the above formulas can be used.
# 
# Enjoy it and happy coding!!
# -----------------------------------------------------------

def bar_triang(point_a, point_b, point_c): 
    xo = (point_a[0] + point_b[0] + point_c[0]) / 3
    yo = (point_a[1] + point_b[1] + point_c[1]) / 3
    xo = round(xo, 4)
    yo = round(yo, 4)
    return [xo, yo]

# or

import numpy as np

def bar_triang(*args):
    return [round(np.mean(coordinates), 4) for coordinates in zip(*args)]

# or

bar_triang = lambda *args: [round(sum(coordinates) / 3, 4) for coordinates in zip(*args)]