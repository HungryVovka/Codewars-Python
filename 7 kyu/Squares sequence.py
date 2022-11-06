# -----------------------------------------------------------
# Complete the function that returns an array of length n, starting with the given number x and the squares of the previous number. If n is negative 
# or zero, return an empty array/list.
# 
# Examples
# 2, 5  -->  [2, 4, 16, 256, 65536]
# 3, 3  -->  [3, 9, 81]
# -----------------------------------------------------------

def squares(x, n):
    i = 1
    arr = []
    while i <= n:
        arr.append(x)
        x = x**2
        i += 1
    return arr

# or

def squares(x, n):
    return list(x**(2**i) for i in range(n))

# or

squares = lambda x, y : [x**(2**y1) for y1 in range(y)]