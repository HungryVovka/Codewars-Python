# -----------------------------------------------------------
# Calculations with time units can be confusing, because we are used to calculating in the decimal system in every day use. An hour, however, consists 
# of sixty minutes, which in turn consist of sixty seconds each.
# 
# When dealing with multiple entries of measured time - for example, in a working time recording - it can get hard to correctly sum up the total. A 
# seemingly natural algorithm is to add up hours and minutes separately, then divmod the minutes with 60 to get additional complete hours and 
# remaining minutes.
# 
# In Germany, some companies use decimal time (in German: "Industriezeit") to keep track of working hours, which makes it a lot easier to calculate 
# multiple entries. One hour has 100 "industrial minutes" (or 10,000 seconds) in decimal time, yet its duration is the same as in normal time. Thus an 
# "Industrieminute" consists of 36 normal seconds, which is 1/100 of an hour.
# 
# Working time is usually rounded to Integer decimal minutes. Thus one normal minute equals 0.02 decimal hours, while two normal minutes equal 
# 0.03 decimal hours and so on.
# 
# Your task: write two functions, one that converts normal time to decimal time and one that converts decimal time to normal time.
# 
# to_industrial(time) should accept either the time in minutes as an Integer or a string of the format "h:mm" or "hhh:mm". Minutes will always 
# consist of two digits in the tests (e.g., "0:05"); hours can have more. Tests are simple in this regard: Expect rather small values (900 is the 
# maximum). Return a Float that represents decimal hours (e.g. 1.75 for 1h 45m). Round to a precision of two decimal digits - do not simply 
# truncate!
# 
# to_normal(time) should accept a Float representing decimal time in hours. Return a string that represents normal time in the format "h:mm".
# 
# There will be no seconds in the tests. We'll neglect them for the purpose of this kata.
# -----------------------------------------------------------

def to_industrial(time):
    if type(time) == str:
        hour, minute = time.split(":")
        return round(int(minute) / 60 + int(hour), 2)
    return round(time / 60, 2)

def to_normal(time):
    return "%d:%02d" % (int(time), round(time % 1 * 60))