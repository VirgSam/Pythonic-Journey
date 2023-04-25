# 46. Write a python program to get the path and name of the file that is currently executing.
# notes: https://www.tutorialsteacher.com/python/os-module#:~:text=The%20OS%20module%20in%20Python,with%20the%20underlying%20operating%20system.

import os
print("Current File Name : ",os.path.realpath(__file__))


# Alternative Soln 1
# import os
# path = os.getcwd()
# print ("The name of the file is: ", os.path.basename(path))
# print ("And the path is: ", os.getcwd())
# Alternative Soln 2





