#Write a Python program to calculate the sum of three given numbers, 
# if the values are #equal then return three times of their sum.

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
num3 = int(input("Please enter the third number: "))

def calc_sum(num1,num2,num3):
    if num1==num2==num3:
        print("The numbers were identical, the numbers were summed up and multiplied by 3: ", (num1+num1+num1) * 3)
    else:
        print ("The numbers where different the sum of the numbers is: ", num1+num2+num3)

# def calc_sum(num1,num2,num3):
# 	if num1==num2 and num2==num3 and num1==num3:
# 		return num1 * 3
# 	else:
# 		return num1+num2+num3

calc_sum(num1,num2,num3)