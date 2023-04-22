#Write a Python program to count the number 4 in a given list.

#a for loop to enter intergers and save them in a list
#a function that takes the complied list and counts
# how to convert a string list into an int list.
values = input("Please input a list of numbers separated by a comma")
input_1 = values.split(",")  
integer_map = map (int, input_1)
integer_list = list(integer_map)

def count_four(integer_list):
    count = 0
    for i in integer_list:
        if i == 4:
            count = count + 1
    return count

count_four(integer_list)




# Use map() to convert a list of strings to ints
# string_list = ["1", "2", "3"]
# integer_map = map(int, string_list) Maps each string to an int.
# integer_list = list(integer_map) Converts mapped output to a list of ints.
# print(integer_list)