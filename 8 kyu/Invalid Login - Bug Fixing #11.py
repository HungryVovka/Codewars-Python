# -----------------------------------------------------------
# Invalid Login - Bug Fixing #11
# Oh NO! Timmy has moved divisions... but now he's in the field of security. Timmy, being the top coder he is, has allowed some bad code through. You 
# must help Timmy and filter out any injected code!
# 
# Task
# Your task is simple, search the password string for any injected code (Injected code is any thing that would be used to exploit flaws in the current 
# code, so basically anything that contains || or //) if you find any you must return "Wrong username or password!" because no one likes someone 
# trying to cheat their way in!
# 
# Preloaded
# You will be given a preloaded class called Database with a method login this takes two parameters username and password. This is a generic 
# login function which will check the database for the user it will return either 'Successfully Logged in!' if it passes the test or 
# 'Wrong username or password!' if either the password is wrong or username does not exist.
# 
# Usage
# database = Database()
# database.login('Timmy', 'password')
# -----------------------------------------------------------

def validate(username, password):
    wrong = ["||", "//"]
    for i in wrong:
        if i in password:
            return "Wrong username or password!"
    database = Database()
    return database.login(username, password)

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