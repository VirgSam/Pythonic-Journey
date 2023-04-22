#Write a Python program to accept a filename from the user and print the extension of that
fileName = str(input("Input file name: "))
output = fileName.split(".")
# print(output[0]) 
# print(output[1])
# print(output[-1])
print(repr(output[-1]))# Figure out how the repr works, why the -1?