# -----------------------------------------------------------
# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
# 
# Example(Input => Output):
# 348597 => [7,9,5,8,4,3]
# 0 => [0]
# -----------------------------------------------------------

def digitize(n):
    arr = [int(i) for i in str(n)]
    return arr[::-1]