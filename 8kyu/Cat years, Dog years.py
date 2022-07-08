# -----------------------------------------------------------
# Kata Task
# I have a cat and a dog.
# 
# I got them at the same time as kitten/puppy. That was humanYears years ago.
# 
# Return their respective ages now as [humanYears,catYears,dogYears]
# 
# NOTES:
# 
# humanYears >= 1
# humanYears are whole numbers only
# 
# Cat Years
# 15 cat years for first year
# +9 cat years for second year
# +4 cat years for each year after that
# 
# Dog Years
# 15 dog years for first year
# +9 dog years for second year
# +5 dog years for each year after that
# 
# References
# 
# http://www.catster.com/cats-101/calculate-cat-age-in-cat-years
# http://www.slate.com/articles/news_and_politics/explainer/2009/05/a_dogs_life.html
# 
# If you liked this Kata there is another related one here (https://www.codewars.com/kata/cat-years-dog-years-2)
# -----------------------------------------------------------

def human_years_cat_years_dog_years(human_years):
    cat_years1 = 15
    cat_years2 = cat_years1 + 9
    cat_years3 = cat_years2 + (human_years - 2) * 4
    dog_years1 = 15
    dog_years2 = dog_years1 + 9
    dog_years3 = dog_years2 + (human_years - 2) * 5
    if human_years == 0:
        return [0, 0, 0]
    if human_years == 1:
        return [human_years, cat_years1, dog_years1]
    if human_years == 2:
        return [human_years, cat_years2, dog_years2]   
    if human_years > 2:
        return [human_years, cat_years3, dog_years3]