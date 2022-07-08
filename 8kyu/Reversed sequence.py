# -----------------------------------------------------------
# Build a function that returns an array of integers from n to 1 where n>0.
# 
# Example : n=5 --> [5,4,3,2,1]
# -----------------------------------------------------------

def reverse_seq(n):
    n_arr = []
    p = n
    while p > 0:
        n_arr.append(p)
        p -= 1
    return(n_arr)