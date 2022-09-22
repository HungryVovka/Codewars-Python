# -----------------------------------------------------------
# You just got done with your set at the gym, and you are wondering how much weight you could lift if you did a single repetition. Thankfully, a few 
# scholars have devised formulas for this purpose (from Wikipedia(https://en.wikipedia.org/wiki/One-repetition_maximum)):
# 
# Epley
# 1RM = w * (1 + r / 30)
# 
# McGlothin
# 1RM = (100 * w) / (101.3 - 2.67123 * r)
# 
# Lombardi 
# 1RM = w * r**0.1
# 
# Your function will receive a weight w and a number of repetitions r and must return your projected one repetition maximum. Since you are not 
# sure which formula to use and you are feeling confident, your function will return the largest value from the three formulas shown above, rounded 
# to the nearest integer. However, if the number of repetitions passed in is 1 (i.e., it is already a one rep max), your function must return w. Also, if the 
# number of repetitions passed in is 0 (i.e., no repetitions were completed), your function must return 0.
# -----------------------------------------------------------

def calculate_1RM(w, r):
    if w == 0 or r == 0:
        return 0
    if r == 1:
        return w
    epley = w * (1 + r / 30)
    mc_glothin = (100 * w) / (101.3 - 2.67123 * r)
    lombardi = w * r**0.1
    return round(max(epley, mc_glothin, lombardi))