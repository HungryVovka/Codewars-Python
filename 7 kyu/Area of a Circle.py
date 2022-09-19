# -----------------------------------------------------------
# Complete the function circleArea so that it will return the area of a circle with the given radius. Round the returned number to two decimal 
# places (except for Haskell). If the radius is not positive or not a number, return false.
# 
# Example:
# 
# circleArea(-1485.86)     #returns False
# circleArea(0)            #returns False
# circleArea(43.2673)      #returns 5881.25
# circleArea(68)           #returns 14526.72
# circleArea("number")     #returns False
# -----------------------------------------------------------

import math

def circle_area(r):
    if not isinstance(r, int) or r <= 0:
        return False;
    return round(math.pi * r * r, 2)