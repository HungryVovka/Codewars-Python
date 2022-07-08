# -----------------------------------------------------------
# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
# 
# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the 
# fourth quarter.
# -----------------------------------------------------------

def quarter_of(month):
    q = [1, 2, 3, 4]
    if month in range(1, 4):
        return q[0]
    if month in range(4, 7):
        return q[1]
    if month in range(7, 10):
        return q[2]
    if month in range(10, 13):
        return q[3]