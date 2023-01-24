# -----------------------------------------------------------
# You are going to place n balls. You need to place blue b balls with red r balls until you get n balls. Your task is return How many blue 
# balls in n balls that you arrange.
# 
# Example B is Blue and R is Red
# 
# count_ball(10,2,4) -> "BBRRRRBBRR" -> returns 4 blue balls
# 
# count_ball(12,2,1) -> "BBRBBRBBRBBR" -> returns 8 blue balls
# 
# Note: your code must be less or equal 55 characters.
# 
# constrains
# 
# 1≤N<pow(10,10000)
# 
# 1≤A≤10000
# 
# 1≤B<10000
# -----------------------------------------------------------

def count_ball(n,b,r): return min(b,n%(b+r))+n//(b+r)*b