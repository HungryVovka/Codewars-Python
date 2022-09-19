# -----------------------------------------------------------
# Count the number of occurrences of each character and return it as a list of tuples in order of appearance. For empty output return an empty list.
# 
# Example:
# 
# ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
# -----------------------------------------------------------

def ordered_count(inp):
    orderedcount = []
    for i in inp:
        if i not in orderedcount:
            orderedcount.append(i)
    return [(j, inp.count(j)) for j in orderedcount]

# or

from collections import Counter

def ordered_count(inp):
    return list(Counter(inp).items())