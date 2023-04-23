# www.w3resource.com/python-exercises/python-basic-exercises.php
#  Write a Python program to print out a set containing all the colors from color_list_1 
#  which are not present in color_list_2.
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}


# note a set can be assigned with set([listitems1,listitems2,listitems3]) or {listitems1,listitems2,listitems3}
# Algorithm
# sets are not iteriable but lists are, i could do the work in a list and save the result as a set
# for I in colorlist2 and for I in colorlist1 if 

color_list_1 = ["White", "Black", "Red"]
color_list_2 = ["Red", "Green"]

output=[]
for i in color_list_1:
    if i not in color_list_2:
	    output.append(i)
print(set(output))
# for ii in color_list_1:
#     print(ii)
#         # if i in color_list_1:

# what was the class solution?

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# print("Original set elements:")
# print(color_list_1)
# print(color_list_2)
# print("\nDifferenct of color_list_1 and color_list_2:")
# print(color_list_1.difference(color_list_2))
# print("\nDifferenct of color_list_2 and color_list_1:")
# print(color_list_2.difference(color_list_1))
# The difference() method returns a set that contains the difference between two sets.
# hahah that easy  .difference() wow

