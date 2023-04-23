# Write a Python program to check whether a specified value is contained in a group of values.

# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

#algo
# use a function
# save test list within function
# try return statement

def checker(value):
    int(value)
    test_data = [1, 5, 8, 3]
    if value in test_data:
        return True
    else:
        return False
print('is the number 5 within the approved list? ',checker(5))
print('is the number 9 within the approved list? ',checker(9))
