# -----------------------------------------------------------
# Let's build a matchmaking system that helps discover jobs for developers based on a number of factors.
# 
# One of the simplest, yet most important factors is compensation. As developers we know how much money we need to support our lifestyle, so we 
# generally have a rough idea of the minimum salary we would be satisfied with.
# 
# Let's give this a try. We'll create a function match which takes a candidate and a job, which will return a boolean indicating whether the job is a 
# valid match for the candidate.
# 
# A candidate will have a minimum salary, so it will look like this:
# 
# candidate = {
#   'min_salary': 120000
# }
# 
# A job will have a maximum salary, so it will look like this:
# 
# job = {
#   'max_salary': 140000
# }
# 
# If either the candidate's minimum salary or the job's maximum salary is not present, throw an error.
# 
# For a valid match, the candidate's minimum salary must be less than or equal to the job's maximum salary. However, let's also include 10% wiggle 
# room (deducted from the candidate's minimum salary) in case the candidate is a rockstar who enjoys programming on Codewars in their spare time. 
# The company offering the job may be able to work something out.
# -----------------------------------------------------------

def match(candidate, job):
    return job["max_salary"] >= candidate["min_salary"] * 0.9

# -----------------------------------------------------------
# License
# Tasks are the property of Codewars (https://www.codewars.com/) 
# and users of this resource.
# 
# All solution code in this repository 
# is the personal property of Vladimir Rukavishnikov
# (vladimirrukavishnikovmail@gmail.com).
# 
# Copyright (C) 2022 Vladimir Rukavishnikov
# 
# This file is part of the HungryVovka/Codewars-Python
# (https://github.com/HungryVovka/Codewars-Python)
# 
# License is GNU General Public License v3.0
# (https://github.com/HungryVovka/Codewars-Python/blob/main/LICENSE.md)
# 
# You should have received a copy of the GNU General Public License v3.0
# along with this code. If not, see http://www.gnu.org/licenses/
# -----------------------------------------------------------