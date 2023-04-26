#58. Write a Python program to sum of the first n positive integers. 
# algo 
# function that asks user for integer input in a loop, include escape after nth time
# ignores all -ve numbers

# def addPositiveNum():
#     posNum = []
#     for i in range(10):
#         userInput = int(input('Please enter a positive or negative number you have 10 attempts: '))
#         if userInput > 0:
#            posNum.append(userInput)
#         else:
#             pass
#     print(sum(posNum))
# addPositiveNum()
# it works but need to figure out a way to resolve of -ve numbers without causing this to crash.

# Alternative soln
n = int(input("Input a number: "))
sum_num = (n * (n + 1)) / 2
print("Sum of the first", n ,"positive integers:", sum_num)
