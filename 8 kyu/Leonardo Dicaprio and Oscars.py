# -----------------------------------------------------------
# You have to write a function that describe Leo:
# 
# def leo(oscar):
#   pass
# 
# if oscar was (integer) 88, you have to return "Leo finally won the oscar! Leo is happy".
# if oscar was 86, you have to return "Not even for Wolf of wallstreet?!"
# if it was not 88 or 86 (and below 88) you should return "When will you give Leo an Oscar?"
# if it was over 88 you should return "Leo got one already!"
# -----------------------------------------------------------

def leo(oscar):
    leonardo_dicaprio_an_oscars = {
        86 : "Not even for Wolf of wallstreet?!",
        87 : "When will you give Leo an Oscar?",
        88 : "Leo finally won the oscar! Leo is happy",
        89 : "Leo got one already!",
    }
    if oscar > 89: oscar = 89
    if oscar < 86: oscar = 87
    return leonardo_dicaprio_an_oscars.get(oscar)