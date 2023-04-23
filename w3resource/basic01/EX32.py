# www.w3resource.com/python-exercises/python-basic-exercises.php
# 32. Write a Python program to get the least common multiple (LCM) of two positive integers

try:
    input_1 = int(input("Please enter the first integer: "))
    input_2 = int(input("Please enter the second integer: "))
except ValueError:
    print("Invalid Entry: ")
if input_1 > input_2:
    dividend = input_1
    divisor = input_2
else:
    dividend = input_2
    divisor = input_1
quotient = dividend // divisor
modulo = dividend % divisor

while True:
    if modulo != 0:
        newDividend = divisor
        newDivisor = modulo
        modulo = newDividend % newDivisor
    
    else:
        lcm = (input_1*input_2)//newDivisor
        print(f"The Lowest Common Multiple between: {input_1} and {input_2} is {lcm}")
        break

# Alternative approach
# def lcm(x, y):
#   if x > y:
#       z = x
#   else:
#       z = y
#   while(True):
#       if((z % x == 0) and (z % y == 0)):
#           lcm = z
#           break
#       z += 1
#   return lcm
# print(lcm(4, 6))
# print(lcm(15, 17))
