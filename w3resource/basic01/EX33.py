# www.w3resource.com/python-exercises/python-basic-exercises.php
# 33. Write a Python program to sum of three given integers.
#  However, if two values are equal sum will be zero

# input allowance for 3 intergers
# if input_1 == input_2 or input_1 == input_3, then print output is 'Zero'
# else  print output input_1 + input_2 + input_3

try:
    input_1 = int(input("Please enter the first integer: "))
    input_2 = int(input("Please enter the second integer: "))
    input_3 = int(input("Please enter the second integer: "))
except ValueError:
    print("Invalid Entry: ")

if input_1 == input_2 or input_1 == input_3:
    print('Sum is equals to Zero')
else:
    sumValue = input_1 + input_2 + input_3
    print(f'Sum is equals to {sumValue}')

# Alternative approach
# def sum_three(x, y, z):
#     if x == y or y == z or x==z:
#         sum = 0
#     else:
#         sum = x + y + z
#     return sum
# print(sum_three(2, 1, 2))
# print(sum_three(3, 2, 2))
# print(sum_three(2, 2, 2))
# print(sum_three(1, 2, 3))
