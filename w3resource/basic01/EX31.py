# # www.w3resource.com/python-exercises/python-basic-exercises.php
# 31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
# use Euclid's Algorithm to do the calculation.
# Dividend - The number being divided
# Divisor - The number performing the division
# Quotient - The result of the division
# Remainder - The number left over after division
# Dividend = Divisor * Quotient + Reminder (modulus)
# GCD(32,5)
# Drop any negative signs
# 32 = 5 x 6 + 2
# 32 / 5 = 6 r. 2
# 32 > 5 -- 32 -dividend and 5 -divisor
# identify the larger of the 2 numbers, this will be the dividend and the smaller divisor
# Write out this algorithm: (dividend) = (divisor) * (quotient) + (remainder)
# insert 

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
        print(f"The Greatest Common Divisor between: {input_1} and {input_2} is {newDivisor}")
        break


