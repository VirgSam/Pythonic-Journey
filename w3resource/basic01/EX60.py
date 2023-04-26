# 60. Write a Python program to calculate the hypotenuse of a right angled triangle.
# formular is c = sqrt(a**2 + b**2)

import math
a = int(input("Please enter the height of the right angle triangle: "))
b = int(input("Please enter the base of the right angle triangle: "))
c = math.sqrt(a**2 + b**2)
print(f" The Hypotenus of right angled triangle with a Height of {a} and a Base {b} is equal to {c} ")

# Alternative soln
from math import sqrt
print("Input lenghts of the shorter triangle sides: ")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 +b**2)
print ("The Length of the hypotenus is: ", c)