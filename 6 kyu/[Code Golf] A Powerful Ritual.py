# -----------------------------------------------------------
# In https://www.codewars.com/kata/63d6dba199b0cc0ff46b5d8a, you were given an integer n >= 1 and asked to find the determinant of the n-
# by-n matrix m with elements m[i][j] = i * j, 1 <= i,j <= n.
# 
# This task is identical, but the matrix elements are given by m[i][j] = i ** j; that is, with power instead of multiplication. Also, the case n = 0 
# will be tested. Return your answer modulo 1 000 000 007.
# 
# Code Limit
# No more than 62 characters. Reference solution is 59 characters, so there should be some leeway.
# 
# Inputs
# A non-negative integer n <= 800. There will be a few fixed tests plus 400 random tests within this range.
# -----------------------------------------------------------

ritual=f=lambda n,x=1: 1 if n<1 else n**x*f(n-1,x+1)%(10**9+7)