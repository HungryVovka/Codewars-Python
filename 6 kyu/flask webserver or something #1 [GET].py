# -----------------------------------------------------------
# flask webserver or something
# 
# task
# Make a flask server with localhost as the host and 4000 as the port.
# Make two routes, one for / the home route and the second /reset for the test cases.
# Make them return a dict with key value pair as toreturn and whatitreturned respectively.
# 
# Also make a runner() method where the flask server will be hosted i.e. where the run() method will be for the webserver
# 
# NOTE
# 1. Sometimes the requests library wont connect because of certain unknown reason, in those cases just reattempt in 2-3 seconds.
# Declare the webserver outside of runner method if you face the error frequently.
# -----------------------------------------------------------

from flask import Flask

app = Flask("Flask webserver")
respectively_dict = {"toreturn": "whatitreturned"}

@app.route("/")
def index():
    return respectively_dict

@app.route("/reset")
def reset():
    return respectively_dict

def runner():
    # make it so that the webserver runs when this method is called
    app.run(port = 4000)
    pass

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