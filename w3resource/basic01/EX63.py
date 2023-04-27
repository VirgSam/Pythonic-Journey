# 63. Write a Python program to get an absolute file path.
# look in  OS module
from os import path
path.abspath("my_path")

# Alternative soln
def absolute_file_path(path_fname):
    import os
    return os.path.abspath('path_fname')        

print("Absolute file path: ",absolute_file_path("test.txt"))

