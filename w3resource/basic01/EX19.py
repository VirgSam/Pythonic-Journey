# Write a Python program to get a new string from a given string where
#  "Is" has been added to the front. 
# If the given string already begins with "Is" then return the string unchanged.

strInput = input("Please enter a couple of words: ")
strInput_l = strInput.split(" ")
if strInput_l[0:2] == "is" or strInput[0:2] == "Is":
   print("Your words have an added -IS- at the beginning :", strInput)
else:
    print("You entered a word without an -IS- at the beginning, this has been amended :","Is" , strInput)