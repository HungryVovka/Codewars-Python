# -----------------------------------------------------------
# Imagine that you are given two sticks. You want to end up with three sticks of equal length. You are allowed to cut either or both of the sticks to 
# accomplish this, and can throw away leftover pieces.
# 
# Write a function, maxlen, that takes the lengths of the two sticks (L1 and L2, both positive values), that will return the maximum length you can make 
# the three sticks.
# -----------------------------------------------------------

def maxlen(L1,L2):
    return L1 / 3 if L1 / 3 > L2 and L1 > L2 else \
        L2 / 3 if L2 / 3 > L1 and L1 < L2 else \
        L1 if L2 / 2 > L1 and L1 < L2 else \
        L2 if L1 / 2 > L2 and L1 > L2 else \
        L1 / 2 if L1 / 2 < L2 and L1 > L2 else \
        L2 / 2 if L2 / 2 < L1 and L1 < L2 else 0

# or

def maxlen(L1, L2):
    x1, x2 = sorted((L1, L2))
    return min(x2 / 2, max(x2 / 3, x1))