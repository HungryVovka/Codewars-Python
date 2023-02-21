# -----------------------------------------------------------
# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
# 
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
# -----------------------------------------------------------

def move_zeros(lst):
    no_zeroes, zeroes = [], []
    for i in lst:
        if i != 0:
            no_zeroes.append(i)
        else:
            zeroes.append(i)
    return no_zeroes + zeroes