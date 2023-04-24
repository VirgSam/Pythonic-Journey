# https://www.w3resource.com/python-exercises/python-basic-exercises.php
# 40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
# 1. Get the coordinates of both points in space.
# 1. Subtract the x-coordinates of one point from the other, same for the y components.
# 1. Square both results separately.
# 1. Sum the values you got in the previous step.
# 1. Find the square root of the result above.

# (x1-x2)squared+(y1+y2)squared=distances squared
# same formula as finding the hypothenus of a triangle

def computeDistance(x,y,x1,y1):
    point1 = (x - x1)**2
    point2 = (y - y1)**2
    import math
    dist = math.sqrt(point1 + point2)
    print(dist)

computeDistance(3,7,0,5)