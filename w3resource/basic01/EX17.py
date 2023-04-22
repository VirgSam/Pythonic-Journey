#Write a Python program to test whether a number is within 100 of 1000 or 2000.

# def near_thousand(n):
#       return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
# print(near_thousand(1000))
# print(near_thousand(900))
# print(near_thousand(800))   
# print(near_thousand(2200))


# number = int(input('Please enter a number: '))
# if number in range(900,1100) or number in range(1900,2100):
#     print('The number is in range!')
# else:
#     print('The number is not in range.')

number = int(input("Please input a number: "))
if number in range(900,1101) or number in range(1900,2101):
    	print("The number is within range")
else:
	print("The number is out of range")