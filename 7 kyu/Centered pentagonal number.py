# -----------------------------------------------------------
# Centered pentagonal number
# Complete the function that takes an integer and calculates how many dots exist in a pentagonal shape around the center dot on the Nth iteration.
# 
# In the image below you can see the first iteration is only a single dot. On the second, there are 6 dots. On the third, there are 16 dots, and on the 
# fourth there are 31 dots. The sequence is: 1, 6, 16, 31...
# 
# If the input is equal to or less than 0, return -1
# 
# Examples
# 1  -->    1
# 2  -->    6
# 8  -->  141
# 0  -->   -1
# 
# Note:
# Input can reach 10**20
# -----------------------------------------------------------

def pentagonal(n):
    return - 1 if n < 1 else 1 + ((n - 1) * 5 * n) // 2