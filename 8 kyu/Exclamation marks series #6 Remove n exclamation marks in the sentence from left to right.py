# -----------------------------------------------------------
# Description:
# Remove n exclamation marks in the sentence from left to right. n is positive integer.
# 
# Examples
# remove("Hi!",1) === "Hi"
# remove("Hi!",100) === "Hi"
# remove("Hi!!!",1) === "Hi!!"
# remove("Hi!!!",100) === "Hi"
# remove("!Hi",1) === "Hi"
# remove("!Hi!",1) === "Hi!"
# remove("!Hi!",100) === "Hi"
# remove("!!!Hi !!hi!!! !hi",1) === "!!Hi !!hi!!! !hi"
# remove("!!!Hi !!hi!!! !hi",3) === "Hi !!hi!!! !hi"
# remove("!!!Hi !!hi!!! !hi",5) === "Hi hi!!! !hi"
# remove("!!!Hi !!hi!!! !hi",100) === "Hi hi hi"
# -----------------------------------------------------------

def remove(s, n):
    arr = []
    i = 1
    for j in range(len(s)):
        if s[j] == "!" and i <= n:
            i += 1
        else:
            arr.append(s[j])
    return "".join(arr)

# or

def remove(s, n):
    return s.replace("!", "", n)