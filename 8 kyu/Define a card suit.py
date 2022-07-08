# -----------------------------------------------------------
# You get any card as an argument. Your task is to return the suit of this card (in lowercase).
# 
# Our deck (is preloaded):
# 
# ('3♣') -> return 'clubs'
# ('3♦') -> return 'diamonds'
# ('3♥') -> return 'hearts'
# ('3♠') -> return 'spades'
# -----------------------------------------------------------

def define_suit(card):
    for c in card:
        if 'C' in c:
            return('clubs')
        if 'D' in c:
            return('diamonds')        
        if 'H' in c:
            return('hearts')
        if 'S' in c:
            return('spades')