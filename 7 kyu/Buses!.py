# -----------------------------------------------------------
# Description:
# 
# To get to the health camp, the organizers decided to order buses. It is known that some children kids and adults adults are going to go to the 
# camp. Each bus has a certain number of seats places. There must be at least two adults on each bus in which children will travel.
# 
# Determine whether it will be possible to send all children and adults to the camp, and if so, what is the minimum number of buses required to order 
# for this.
# 
# Input data:
# 
# arguments kids, adults, places each of them does not exceed 10,000.
# 
# Output data:
# 
# We need to return the number of buses that need to be ordered. If it is impossible to send everyone to the camp, return 0
# 
# buses(10, 4, 7) --> 2
# buses(10, 4, 5) --> 0
# 
# Happy coding :)
# -----------------------------------------------------------

import math

def buses(kids, adults, places):
    try:
        number_of_buses = math.ceil((kids + adults) / places)
        if number_of_buses > adults / 2:
            return 0
        return number_of_buses
    except ZeroDivisionError:
        return 0