# -----------------------------------------------------------
# Create a function that takes in the sum and age difference of two people, calculates their individual ages, and returns a pair of values (oldest age 
# first) if those exist or null/None if:
# 
# sum < 0
# difference < 0
# 
# Either of the calculated ages come out to be negative
# -----------------------------------------------------------

def get_ages(sum_, difference):
    if sum_ < 0 or difference < 0:
        return(None)
    if sum_ >= 0 and difference >= 0:
        second = (sum_ - difference) / 2
        first = second + difference
        if first >= 0 and second >= 0:
            return(first, second)
        else:
            return(None)