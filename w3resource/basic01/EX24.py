# Write a Python program to test whether a passed letter is a vowel or not.

# algo
# input a letter
# have a list of vowels
# check if the letter is in the vowels list
# print out statement confirming truth or false

# inp = input("Please enter a letter : ")
# vowels = ['a','i','e','o','u']
# for i in vowels:
#     if inp == i:
#         print (f"{inp} is a Vowel")
#     else:
#         print (f"{inp} is a Consonant")

def is_vowel(char):
    all_vowels = "aeiou"
    return char in all_vowels
print(is_vowel('a'))
