# 53. Write a python program to access environment variables.
# https://www.geeksforgeeks.org/python-os-environ-object/

# import os
# import pprint

# # get the list of user's
# # enviromnet
# envVar = os.environ

# #print the list of users
# # environment variables
# print('Users Environment Variable: ')
# pprint.pprint(dict(envVar), width=1) 

# Alternative soln
# Note: there was more output data using this technique than the above.
# import os
# for data in os.environ:
#    print(data)
#    print('-'*15)
#    print(os.environ[data])
#    print('='*30)
# 