# -----------------------------------------------------------
# A Narcissistic Number is a number of length l in which the sum of its digits to the power of l is equal to the original number. If this seems 
# confusing, refer to the example below.
# 
# Ex: 153, where l = 3 ( the number of digits in 153 )
# 1^3 + 5^3 + 3^3 = 153
# 
# Write a function that, given n, returns whether or not n is a Narcissistic Number.
# -----------------------------------------------------------

def is_narcissistic(i):
    str_i = str(i)
    i_arrstr = list(str_i)
    number = 0
    for n in i_arrstr:
        n = int(n)
        number += n**len(i_arrstr)
    if i == number:
        return(True)
    else:
        return(False)
