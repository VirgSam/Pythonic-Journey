# 45. Write a Python program to call an external command.
# import os
# os.system("echo Hello World")

# https://www.delftstack.com/howto/python/call-external-programs-python/

# Alternative Soln 1
import os
print(os.system('ls -l'))

# Alternative soln 2
from subprocess import call
call(["ls", "-l"])