# -----------------------------------------------------------
# #~For Kids Challenges~#
# Your task is easy, write a function that takes an date in format d/m/Y(String) and return what day of the week it was(String).
# Example: "21/01/2017" -> "Saturday", "31/03/2017" -> "Friday"
# Have fun!
# -----------------------------------------------------------

import datetime

def day_of_week(date):
    day, month, year = (int(x) for x in date.split('/'))
    answer = datetime.date(year, month, day)
    return answer.strftime("%A")