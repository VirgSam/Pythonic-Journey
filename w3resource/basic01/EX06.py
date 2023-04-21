#Write a Python program which accepts a sequence of 
# comma-separated numbers from user and generate a list 
# and a tuple with those numbers


value = input("Input only numbers with a comma separating each")
myList = value.split(",")
mytuple = tuple(myList)
print ("List: ", myList)
print ("Tuple: ", mytuple)

print ("What number is located on list location space 2: ", myList[2])

print ("What number is located on tuple location space 9: ", mytuple[9])