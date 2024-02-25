def factorial(n):
    result = 1
    for i in range(1, n + 1):
        print(i)
        result *= i
        print(result)
    return result

# number = 6
# factorial_of_6 = factorial(number)
# print(f"The factorial of {number} is {factorial_of_6}")

w = factorial(5)/factorial(3)

x = 4*5*6

y = 1*2*3

z = 4*5

if w == x:
    print("x is factorial of 6 ")
else:
    print("x is not factorial of 6 ")
if w == y:
    print("y is factorial of 6 ")
else:
    print("y is not factorial of 6 ")
if w == z:
    print("z is factorial of 6 ")
else:
    print("z is not factorial of 6 ")