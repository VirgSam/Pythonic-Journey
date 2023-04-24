# https://www.w3resource.com/python-exercises/python-basic-exercises.php
# 35. Write a Python program that will return true 
# if the two given integer values are equal or their sum or difference is 5.

try:
    input_1 = int(input("Please enter the first integer: "))
    input_2 = int(input("Please enter the second integer: "))
except ValueError:
    print("Invalid Entry: ")

if input_1 == input_2 or input_1 + input_2 == 5 or input_1 - input_2 == 5 or input_2 - input_1 == 5:
    print("True")
else:
    print("False")

# Alternative approach
# def test_number5(x, y):
#    if x == y or abs(x-y) == 5 or (x+y) == 5: # interesting use of abs()
#        return True                           # the return syntax works well within a defined function
#    else:
#        return False
# print(test_number5(7, 2))
# print(test_number5(3, 2))
# print(test_number5(2, 2))
# print(test_number5(7, 3))
# print(test_number5(27, 53))