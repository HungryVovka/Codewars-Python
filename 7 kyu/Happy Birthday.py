# -----------------------------------------------------------
# It's your best friend's birthday! You already bought a box for the present. Now you want to pack the present in the box. You want to decorate the box 
# with a ribbon and a bow.
# 
# But how much cm of ribbon do you need?
# 
# Write the method wrap that calculates that!
# 
# A box has a height, a width and a length (in cm). The ribbon is crossed on the side with the largest area. Opposite this side (also the side with the 
# largest area) the loop is bound, calculate with 20 cm more tape.
# 
#   wrap(17,32,11) => 162
#   wrap(13,13,13) => 124
#   wrap(1,3,1) => 32
#  
# Notes:
# height, width and length will always be >0
# -----------------------------------------------------------

def wrap(height, width, length):
    p1 = height
    p2 = width
    p3 = length
    if p1 < p2 and p1 < p3:
        return(p1*4 + p2*2 + p3*2 + 20)
    if p2 < p1 and p2 < p3:
        return(p1*2 + p2*4 + p3*2 + 20)
    if p3 < p1 and p3 < p2:
        return(p1*2 + p2*2 + p3*4 + 20)
    if p1 == p2 and p1 < p3:
        return(p1*4 + p2*2 + p3*2 + 20)     
    if p1 == p3 and p1 < p2:
        return(p1*4 + p2*2 + p3*2 + 20) 
    if p2 == p3 and p2 < p1:
        return(p1*2 + p2*4 + p3*2 + 20)
    if p1 == p3 and p1 == p2:
        return(p1*4 + p2*2 + p3*2 + 20)