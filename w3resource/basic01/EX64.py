# 64. Write a Python program to get file creation and modification date/times.
# import os
# print(dir(os)) == shows what is hidden in os module
import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("test2.txt")))
print("Created: %s" % time.ctime(os.path.getctime("test2.txt")))

# what if it is in another folder, how would i access that file??

# Alternative soln
import os.path,time

file = open('test.txt','w')

print('modified time: ',time.ctime(os.path.getmtime("test.txt")))
print('created time: ',time.ctime(os.path.getctime("test.txt")))