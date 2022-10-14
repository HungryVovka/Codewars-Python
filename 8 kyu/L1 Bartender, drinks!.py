# -----------------------------------------------------------
# Complete the function that receives as input a string, and produces outputs according to the following table:
# 
# Input	Output
# "Jabroni"	"Patron Tequila"
# "School Counselor"	"Anything with Alcohol"
# "Programmer"	"Hipster Craft Beer"
# "Bike Gang Member"	"Moonshine"
# "Politician"	"Your tax dollars"
# "Rapper"	"Cristal"
# anything else	"Beer"
# 
# Note: anything else is the default case: if the input to the function is not any of the values in the table, then the return value should be "Beer".
# 
# Make sure you cover the cases where certain words do not show up with correct capitalization. For example, the input "pOLitiCIaN" should still 
# return "Your tax dollars".
# -----------------------------------------------------------

drinks = {
    "JABRONI": "Patron Tequila",
    "SCHOOL COUNSELOR": "Anything with Alcohol",
    "PROGRAMMER": "Hipster Craft Beer",
    "BIKE GANG MEMBER": "Moonshine",
    "POLITICIAN": "Your tax dollars",
    "RAPPER": "Cristal",
}

def get_drink_by_profession(param):
    return drinks.get(param.upper(), "Beer") 