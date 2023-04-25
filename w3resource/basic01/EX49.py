# 49. Write a Python program to list all files in a directory in Python
import os
print(os.system("dir"))
print(os.system("ls -l"))

# review each solution and see if you can improve on it.

# Alternative Soln 1 

# from os import listdir
# from os.path import isfile, join
# files_list = [f for f in listdir('/home/students') if isfile(join('/home/students', f))]
# print(files_list)

# Alternative Soln 2
# import os
# print(os.listdir())

# Alternative Soln 3
# path = "D://Folder/Folder"

# def printFiles(directory):
# exist = os.path.exists(directory)
# if exist:
# file_list = []
# for i in os.listdir(directory):
# if os.path.isfile(i):
# file_list.append(i)
# for i in file_list:
# print(i)
# else:
# print("Directory does not exist")

# printFiles(path)