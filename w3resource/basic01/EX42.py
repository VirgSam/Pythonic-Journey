# 42. Write a Python program to determine if a Python shell 
# is executing in 32bit or 64bit mode on OS.

# import sys
# sys.version

# # Alternate approach 1

# import sys


# def determineIfPythonShellIsExecutingIn32Or64BitMode():
#     if sys.maxsize == 9223372036854775807:
#         print('Python shell is executing in 64 bit mode')
#     else:
#         print('Python shell is excuting in 32 bit mode')

# Alternate approach 2

# import platform, struct

# print(platform.architecture()[0])
# print(struct.calcsize("P") * 8)