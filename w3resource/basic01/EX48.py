# 48. Write a Python program to parse a string to Float or Integer.

# Data parsing is a process in which a string of data is converted 
# from one format to another. If you are reading data in raw HTML, 
# a data parser will help you convert it into a more readable format 
# such as plain text.

# Algo
# input container accepts a string
# if string contains a decimal point and assign to a float variable container
# if string contains no decimal point, then assign to integer variable container
# if the string has non-numeric characters output error statement
# print out 


def parserChecker():
    stringInput = input("Please enter an integer or float: ")
    if int(stringInput) == True:
        print(f"{stringInput} is an interger")
    elif float(stringInput) == True:
        print(f"{stringInput} is an float")
    else:
        print(f"{stringInput} is neither an integer nor float")

parserChecker()
# my solution was shitty, but good going below.

# Alternative soln
# def test(s):
#    try:
#        return int(s)
#    except ValueError:
#        return float(s)
# print(test('12'))
# print(test('233.12'))


# Alternative soln 2
# string = "246.2458"

# def whatType(str):
# try:
# int(str)
# return "String is an int: " + repr(str)
# except:
# try:
# float(str)
# return "String is a float: " + repr(str)
# except:
# return "String is neither an int or float"

# print(whatType(string))
