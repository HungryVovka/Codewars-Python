# -----------------------------------------------------------
# Define a function that removes duplicates from an array of numbers and returns it as a result.
# 
# The order of the sequence has to stay the same.
# -----------------------------------------------------------

def distinct(seq):
    newseq = []
    for i in seq:
        if i not in newseq:
            newseq.append(i)
    return newseq

# or

def distinct(seq):
    return sorted(set(seq), key = seq.index)

# or

def distinct(seq):
    return list(dict.fromkeys(seq))