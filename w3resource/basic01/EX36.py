# https://www.w3resource.com/python-exercises/python-basic-exercises.php
# 36. Write a Python program to add two objects if both objects are an integer type.

def add_objects(x, y):
    if isinstance(x, int) and isinstance(y, int):
        sum = x + y
        return sum
    else:
        return "Inputs must be integers!"

print(add_objects(7, 2))
print(add_objects(7, 'a'))

# Alternative approach
# def add_numbers(a, b):
#    if not (isinstance(a, int) and isinstance(b, int)):
#        return "Inputs must be integers!"
#    return a + b
# print(add_numbers(10, 20))
# print(add_numbers(10, 20.23))
# print(add_numbers('5', 6))
# print(add_numbers('5', '6'))
