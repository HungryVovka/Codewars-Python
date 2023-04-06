# -----------------------------------------------------------
# There is a socket listening on port 1111 of local host.
# 
# The socket either belongs to a server that sends back anything you send to it, or to a server that reverses anything you send to it.
# 
# Create a function that does the following:
# 
# Connects to the socket on port 1111.
# Sends one packet to the server.
# Receives one packet from the server.
# Returns True if the server is the regular type (i.e., it sends back the same packet that was sent to it), or False if the server is the reversing type 
# (i.e., it reverses the packet that was sent to it).
# 
# Make sure to close the socket after you are done using it. If you time out while trying to connect, it is likely that you did not connect, send, receive, 
# and close the socket in the correct order.
# 
# Happy coding!
# -----------------------------------------------------------

import socket

def socket_client():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(("127.0.0.1", 1111))
    server.send(b"HungryVovka")
    response = server.recv(1024)
    server.close()
    return response == b"HungryVovka"

# or

import socket

def socket_client():
    packet = b"HungryVovka"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.connect(("127.0.0.1", 1111))
        server.send(packet)
        response = server.recv(1024)
        return response == packet

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