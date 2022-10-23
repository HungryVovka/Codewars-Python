# -----------------------------------------------------------
# We define the function f1(n,k), as the least multiple of n that has all its digits less than k.
# 
# We define the function f2(n,k), as the least multiple of n that has all the digits that are less than k, and no others.
# 
# Each digit may occur more than once in both values of f1(n,k) and f2(n,k).
# 
# The possible values for n and k according to these ranges for both functions f1 and f2 in this kata:
# 
# 1 <= n <= 1.000.000.000.000
# 3 <= k <= 9
# 
# For example, let's see the value of both functions for n = 71 and k = 4:
# 
# f1(71,4) == 213 # all its digits less than 4
# f2(71,4) == 2130 # 0,1,2,3 all of them present 
# 
# The integer 76 is the first integer that has the same values of f1 and f2 for k = 4.
# 
# f1(76,4) = f2(76,4) = 10032
# 
# Let's call these kind of numbers, forgiving numbers. (Let's continue with the fashion of attributing personality traits to numbers and, of course, an 
# unknown one) So, 76 is the smallest forgiving number of order 4. In the same way, 485 is the smallest forgiving number of order 5.
# 
# Create a function that given an integer n and the order k, will output the higher and closest forgiving number to n of order k.
# 
# Let's see some examples:
# 
# find_f1_eq_f2(500,5) == 547
# find_f1_eq_f2(1600,6) == 1799
# find_f1_eq_f2(14900,7) == 14996
# 
# If the number n is a forgiving itself for a certain order k, the function will never output the same value, remember, closest and higher than n.
# 
# For example, 3456, is a forgiving one of order 4,
# 
# find_f1_eq_f2(3456,4) == 3462
# 
# Features of the tests:
# 
# n and k will be always valid and positive integers.
# 
# A total of 8 fixed tests.
# 
# A total of 150 random tests in the ranges for n and k given above.
# 
# I'll be waiting your awesome solution. :)
# -----------------------------------------------------------

def f1(n, k):
    m = n
    while any(list(int(i) >= k for i in str(m))):
        m += n
    return m

def forgiving(n, k):
    m = f1(n, k)
    return k == len(set(str(m)))

def find_f1_eq_f2(n,k):
    n += 1
    m = n
    while not forgiving(m, k):
        m += 1
    return m

# or

def find_f1_eq_f2(n, k):
    while True:
        n += 1
        m = n
        while True:
            fn = list(set(map(int, str(m))))
            if max(fn) < k:
                if len(fn) != k:
                    break
                else:
                    return n
            m += n