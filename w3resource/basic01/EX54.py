# 54. Write a Python program to get the current username.
# https://www.geeksforgeeks.org/how-to-get-the-current-username-in-python/

import os
username= os.getlogin()
print(username)

# alternative soln
# import getpass
# print(getpass.getuser())

# # alternative soln
# import os
# print(os.environ['USERNAME'])

# # alternative soln
# import os
# print(os.getenv('USERNAME') or os.getenv('USER') or os.getenv('LOGNAME'))