# -----------------------------------------------------------
# Task
# Let
# 
# gcd(a,b)=x
# lcm(a,b)=y
# a,b∈N
# 
# where gcd represents the greatest common divisor of two integers and lcm represents the least common multiple of two integers.
# 
# Given x and y, find any possible pair (a,b) that satisfies the condition above with aaa and bbb being positive integers. If there are multiple solutions, 
# return any. If there are no solutions, return None. Return your answer as a tuple of (a,b)
# 
# Constraints
# 1 ≤ x,y ≤ 10^9
#  
# 
# Examples (More in Example Tests)
# ---------------------------------
# |   x   |   y   |   a   |   b   |
# |   6   |   36  |   12  |   18  |
# |   7   |   8   |     None      |    
# |   8   |   48  |   24  |   16  |
# ---------------------------------
# 
# Note that there are multiple solutions for the 1st and 3rd examples.
# 
# If you are having issues about the time limit, please try to first make an observation instead of straight up brute force. View solutions if necessary 
# (they may surprise you!)
# -----------------------------------------------------------

def gcd_lcm(x, y):
    if y % x == 0:
        return x, y

# or

def gcd_lcm(x, y):
    return (x, y) if y % x == 0 else None