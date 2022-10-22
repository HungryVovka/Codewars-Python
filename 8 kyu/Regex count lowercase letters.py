# -----------------------------------------------------------
# Your task is simply to count the total number of lowercase letters in a string.
# 
# Examples
# lowercaseCount("abc"); ===> 3
# 
# lowercaseCount("abcABC123"); ===> 3
# 
# lowercaseCount("abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~"); ===> 3
# 
# lowercaseCount(""); ===> 0;
# 
# lowercaseCount("ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~"); ===> 0
# 
# lowercaseCount("abcdefghijklmnopqrstuvwxyz"); ===> 26
# -----------------------------------------------------------

def lowercase_count(strng):
    low_count = 0
    for i in list(strng):
        if i.islower():
            low_count += 1
    return low_count

# or

def lowercase_count(strng):
    return sum(i.islower() for i in strng)