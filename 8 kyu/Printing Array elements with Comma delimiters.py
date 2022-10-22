# -----------------------------------------------------------
# Input: Array of elements
# 
# ["h","o","l","a"]
# 
# Output: String with comma delimited elements of the array in th same order.
# 
# "h,o,l,a"
# 
# Note: if this seems too simple for you try the next level
# -----------------------------------------------------------

def print_array(arr):
    answer = []
    for i in arr:
        answer.append(str(i))
    return ",".join(answer)

# or

def print_array(arr):
    return ",".join(str(i) for i in arr)

# or

def print_array(arr):
    return ",".join(map(str, arr))