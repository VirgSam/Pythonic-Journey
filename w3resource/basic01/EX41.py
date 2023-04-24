# 41. Write a Python program to check whether a file exists.
#  https://www.w3resource.com/python-exercises/python-basic-exercises.php
# 41. Write a Python program to check whether a file exists.
# i would think it would use the osdir python module
# have a tester file to use to test if the file is in a dedicated folder
# C:\Users\chris\my_scripts\Training\Python Exercises\w3resource\Basic I
# Algo
# if os open() file.txt == true
# to do it, you can use the exists() function from the os.path module or 
# is_file() method from the Path class in the pathlib module.


import os.path

os.path.exists("file.txt")


# Alternative approach

import os.path
print(os.path.isfile('file.txt'))
print(os.path.isfile('file.py'))





