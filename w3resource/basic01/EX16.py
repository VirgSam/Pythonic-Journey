# Write a Python program to get the difference between a given number and 17, 
# if the number is greater than 17 return double the absolute difference.

# enter interger input of a number in var container x
# if x is =< 17, then 17 - x print output with statement x is less than 17
# else x is > 17, then x - 17 = output, print (abs(output**2))

x = int(input("Please input an interger for calculation: "))

if x <= 17:
    output = 17 - x
    print ("Initial entry was equal to or less than 17, Value of output is: ", abs(output))
else:
    output = x - 17
    print ("Initial entry was greater than 17, Value of output is: ", abs(output**2))