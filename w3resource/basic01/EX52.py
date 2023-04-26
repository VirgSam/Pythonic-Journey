#  52. Write a Python program to print to stderr.
# notes: https://www.geeksforgeeks.org/how-to-print-to-stderr-and-stdout-in-python/
# what is the function of the python stderr?

import sys
# def print_to_stderr(*a):
# # Here a is the array holding the objects
# # passed as the argument of the function
#     print(*a, file=sys.stderr)
# print_to_stderr("Hello World")

# import sys
# print('Example 1')
# print('Example 2',file=sys.stderr)
# sys.stderr.write('Example 3')

# import logging
# logging.basicConfig(format='%(message)s') 
# log = logging.getLogger(__name__)
# log.warning('Error: Hello World')
# print('GeeksforGeeks')

# Alternative approach
# https://www.w3resource.com/python-exercises/python-basic-exercise-52.php
# from __future__ import print_function
# import sys

# def eprint(*args, **kwargs):
#     print(*args, file=sys.stderr, **kwargs)

# eprint("abc", "efg", "xyz", sep="--")

# Alternative approach 2
# import sys
# a = int(input("enter the number:"))
# b = int(input("enter the number:"))
# if a == b:
#     print(a,b,file=sys.stderr)
# else:
#     print("none_process")