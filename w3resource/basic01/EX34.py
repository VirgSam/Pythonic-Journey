# 34. Write a Python program to sum of two given integers. 
# However, if the sum is between 15 to 20 it will return 20.

try:
    input_1 = int(input("Please enter the first integer: "))
    input_2 = int(input("Please enter the second integer: "))
except ValueError:
    print("Invalid Entry: ")

totalSum = input_1 +input_2
if totalSum > 15 and totalSum > 20:
    print("The output is: 20")
else:
    print(f'The output is: {totalSum}')

# Alternative approach
# def sum(x, y):
#     sum = x + y
#     if sum in range(15, 20):
#         return 20
#     else:
#         return sum

# print(sum(10, 6))
# print(sum(10, 2))
# print(sum(10, 12))
