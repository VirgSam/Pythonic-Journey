# 38. Write a Python program to solve (x + y) * (x + y). 
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49

x, y = 4, 3
output = x**2 + 2*x*y + y**2
print(f"The Expected output is: ({x} + {y})^2 = {output} " ) # 
# print("Input text for conca" + str(output))<-- how to concatenate a str and an integer where output == integer
# Alternate soln
# x, y = 4, 3
# result = x * x + 2 * x * y + y * y
# print("({} + {}) ^ 2) = {}".format(x, y, result))

