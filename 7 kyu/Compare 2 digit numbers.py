# -----------------------------------------------------------
# You are given 2 two-digit numbers. You should check if they are similar by comparing their numbers, and return the result in %.
# 
# Example:
# 
# compare(13,14)=50%;
# compare(23,22)=50%;
# compare(15,51)=100%;
# compare(12,34)=0%.
# -----------------------------------------------------------

def compare(a, b):
    a = sorted(list(str(a)))
    b = sorted(list(str(b)))
    if a == b:
        return "100%"
    elif a[0] in b or a[1] in b:
        return "50%"
    else:
        return "0%"