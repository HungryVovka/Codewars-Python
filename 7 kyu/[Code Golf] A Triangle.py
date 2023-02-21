# -----------------------------------------------------------
# Task
# Given three sides a, b and c, determine if a triangle can be built out of them.
# 
# Code limit
# Your code can be up to 40 characters long.
# 
# Note
# Degenerate triangles are not valid in this kata.
# -----------------------------------------------------------

triangle=lambda a,b,c:a+b>c>abs(b-a)

# or

triangle=lambda *x:sum(x)>2*max(x)