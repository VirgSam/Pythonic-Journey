#www.w3resource.com/python-exercises/python-basic-exercises.php
#27. Write a Python program to concatenate all elements in a list into a string and return it. Go to the editor
#Click me to see the sample solution

# create a list and populate it with individual items
# use the .join() func and see what comes out

def joinerExercise():
    basicList = ['We','didnt','start','the','fire','but','the','house','was','burning.']
    join_elements = ' '.join(basicList)
    print(join_elements)

joinerExercise()


""" 

Think about the options below they could be of use to you.
def concatenate(list):
string = ""
for i in list:
string += str(i)
return string
print(concatenate([1, 5, 12, 2]))
print(concatenate(["a", 5, 5.5, "a"]))

def concatenate_string(list):
for i in list:
r = str(i)
print(r, end='')

concatenate_string([1, 2, 4, 5])

list1 = ['1', '2', '3', 4, 5]
str1 = ''.join(str(e) for e in list1)

print(str1)


"""