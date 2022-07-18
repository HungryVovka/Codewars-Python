# -----------------------------------------------------------
# Lot of museum allow you to be a member, for a certain amount amount_by_year you can have unlimitted acces to the museum.
# 
# In this kata you should complete a function in order to know after how many visit it will be better to take an annual pass. The function take 2 
# arguments annual_price and individual_price.
# -----------------------------------------------------------

def how_many_times(annual_price, individual_price):
    n = 1
    first = annual_price
    second = individual_price
    while second < first:
        second += individual_price
        n += 1
    return(n)