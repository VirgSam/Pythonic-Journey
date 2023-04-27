"""
69. Write a Python program to sort three integers without using conditional statements and loops.
"""
# input integers into a list
# int_one=int(input("Please enter first Integer: "))
# int_two=int(input("Please enter second Integer: "))
# int_three=int(input("Please enter third Integer: "))
# # use sort() on list
# sort_list=[]
# sort_list.append(int_one)
# sort_list.append(int_two)
# sort_list.append(int_three)
# sort_list.sort()
# # output list
# print(sort_list)

#Alternative soln: nice solution with the maths element.
x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)
