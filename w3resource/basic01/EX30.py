# www.w3resource.com/python-exercises/python-basic-exercises.php
# 30. Write a Python program that will accept the base and height of a triangle and compute the area.

# user inputs numerical string for base and height
# string is converted to a integer
# integer saved in variable containers for base and height
try:
    base = int(input("Please enter the Base: "))
    height = int(input("Please enter the height: "))
except ValueError:
    print("Invalid Entry: ")
    
# multiply (bxh) divide result by 2
result = base * height/2
# print out output message
print(f" The Area for the triangle with a base of: {base} and a height of: {height} is {result}")
 