# -----------------------------------------------------------
# Write a function which removes from string all non-digit characters and parse the remaining to number. E.g: "hell5o wor6ld" -> 56
# 
# Function:
# 
# getNumberFromString(s)
# -----------------------------------------------------------

string_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def get_number_from_string(string):
    answer = ""
    string = list(string)
    for i in string:
        if i in string_numbers:
            answer += i
    return int(answer)

# or

def get_number_from_string(string):
    answer = [i for i in string if i.isdigit()]
    return int("".join(answer))