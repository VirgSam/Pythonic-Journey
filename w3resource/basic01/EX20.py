#Write a Python program 
# to get a string which is n (non-negative integer) copies of a given string.

# Input_1 = input("Please enter Word you would like copied :")
# Input_2 = int(input("Please enter number of copies you would like :"))
# output = Input_1 * abs(Input_2)
# print (output)


def larger_string(str, n):
    """ 
    Use the script block below, you recognise it from Gesa, 
    try creating functions directed solutions
    """

    result = ""
    for i in range(n):
        result = result + str
    return result

print(larger_string('abc', 2))
print(larger_string('.py', 3))
