# 55. Write a Python program to find local IP addresses using Python's stdlib.

import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is:" +hostname)
print("Your Computer Address is:" +IPAddr)

# Alternative approach
import socket
print(socket.gethostbyname(socket.gethostname()))