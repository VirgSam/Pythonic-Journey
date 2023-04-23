#  Write a Python program to create a histogram from a given list of integers

import matplotlib.pyplot as plt

#soln 1
# def histogram(items):
#     for n in items:
#         output = ''
#         times = n
#         while (times > 0):
#             output += '*'
#             times -= 1
#         # print(output)
# histogram([5,4,7,9,10])


#Soln 2
nums_data = input('Enter list of numbers separated by a comma: ')
nums_data = list(nums_data)
nums_data = [i for i in nums_data if i != ',']

plt.hist(nums_data, density=True, bins=50)
plt.show()