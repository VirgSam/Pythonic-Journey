# name = 'Zophie the cat'
# name[7] = 'the' strings are immutable

name = "Zophie a cat"
newName = name[0:7] + " the " + name[8:12]
print(name)
print(newName)

eggs = [1, 2, 3]
print(eggs)
eggs = [4, 5, 6]
print(eggs)
eggs = [1, 2, 3]
print(eggs)
del eggs[2]
print(eggs)
del eggs[1]
print(eggs)
del eggs[0]
print(eggs)
eggs.append(4)
print(eggs)
eggs.append(5)
print(eggs)
eggs.append(6)
print(eggs)
