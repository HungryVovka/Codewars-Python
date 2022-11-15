# -----------------------------------------------------------
# In this kata, you are given a string.
# 
# The goal is to find the sum of all the letters in the string, where a = 1, b = 2...z = 26.
# 
# All other characters count for 0, and capitals are counted twice.
# 
# Example
# string_sum("abCd")
# 
# Should return 13, because a = 1, b = 2, c = 3 * 2, d = 4.
# 
# The sum is 1 + 2 + 6 + 4 = 13
# -----------------------------------------------------------

def string_sum(string):
    answer = 0
    for i in repr(string):
        if i.isalpha():
            letter = ord(i.lower()) - 96
            if i == i.lower():
                answer += letter
            else:
                answer += letter * 2
    return answer