# -----------------------------------------------------------
# You are given 4 spheres, one of them lies on 3 others; all the spheres are in contact:
# 
# All spheres have the same radius r
# 
# Task
# Your task is to write a function that accepts a radius r, and returns the distance between the bottom of the upper sphere and the plane on which 
# they are all located (vertical dashed line at the image below). The answer should be rounded to 4 decimal places. If the function recieves invalid float 
# for radius (r < 0), then it should return 0.0 as an answer.
# 
# Code limit
# The maximum code length: 58
# 
# Examples
# 10   -->  16.3299
# 9    -->  14.6969
# 1.224744871391589  -->  2.0
# -10  -->  0.0
# -----------------------------------------------------------

calculate_distance = lambda x:round(x*(8/3)**0.5,4)*(x>0)