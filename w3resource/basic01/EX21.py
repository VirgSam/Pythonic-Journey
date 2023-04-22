# Write a Python program to find whether a given number 
# (accept from the user) is even or odd, 
# print out an appropriate message to the user.

user_input = int(input("Please Insert an Integer for calculation :"))
if user_input % 2 == 0:
    print(user_input," is even numbered")
elif user_input % 2 != 0:
    print(user_input," is odd numbered")
else:
    print ("Entry error") # Have to figure out how to catch the exception of the user enters words