import random

pets = ["Dog", "Cat", "Moose"]
print(random.choice(pets))

print(pets[random.randint(0, len(pets) - 1)])

# random.choice(pets) == pets[random.randint(0,len(pets) -1)]

people = ["alice", "bob", "carol", "david"]
print("Before Shuffle :")
people
random.shuffle(people)
print("After Shuffle :")
people
