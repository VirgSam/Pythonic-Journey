#Write a Python program that accepts an 
# integer (n) and computes the value of n+nn+nnn.

# n = input("Please input an integer for computation: ")
# output = int(n) + int(n+n) + int(n+n+n)
# print (output)


# a = int(input("Input an integer : "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)


# using the Fstring
n = (input('Value of n : '))
print(f'Result : {int(n) + int(n+n) + int(n+n+n)}') #how do you concatenate within fstrings?