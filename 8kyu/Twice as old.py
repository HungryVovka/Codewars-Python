# -----------------------------------------------------------
# Your function takes two arguments:
# 
# current father's age (years)
# current age of his son (years)
# 
# Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).
# -----------------------------------------------------------

def twice_as_old(dad_years_old, son_years_old):
    if (dad_years_old - (son_years_old * 2)) >= 0:
        return dad_years_old - (son_years_old * 2)
    else:
        return 0 - (dad_years_old - (son_years_old * 2))

# or

def twice_as_old(dad_years_old, son_years_old):
    age = dad_years_old - son_years_old * 2
    if age >= 0:
        return age
    else:
        return 0 - age

# or

def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - (son_years_old * 2))