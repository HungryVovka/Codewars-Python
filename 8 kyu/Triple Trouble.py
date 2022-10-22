# -----------------------------------------------------------
# Triple Trouble
# Create a function that will return a string that combines all of the letters of the three inputed strings in groups. Taking the first letter of all of the 
# inputs and grouping them next to each other. Do this for every letter, see example below!
# 
# E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"
# 
# Note: You can expect all of the inputs to be the same length.
# -----------------------------------------------------------

def triple_trouble(one, two, three):
    one = list(one)
    two = list(two)
    three = list(three)
    arr = []
    i = 0
    while i < len(one):
        arr.append(one[i])
        arr.append(two[i])
        arr.append(three[i])
        i += 1
    return "".join(arr)

# or

def triple_trouble(one, two, three):
    return "".join(i1 + i2 + i3 for i1, i2, i3 in zip(one, two, three))

# or

def triple_trouble(one, two, three):
    return "".join("".join(i) for i in zip(one, two, three))