eggs = ("hello", 42, 0.5)
eggs[0]
eggs[1:3]
len(eggs)
# eggs[1]= 99 #TypeError: 'tuple' object does not support item assignment, tuples are immutable also sets
type(("hello"))
type(("hello",))

# Converting Types with the list() and tuple() Functions
tuple(["cat", "dog", 5])
list(("cat", "dog", 5))
list("hello")  # turned the individual letters into items on a list

# referencing
spam = [0, 1, 2, 3, 4, 5]
cheese = spam  # The reference is being copied , not the list.
cheese[
    1
] = "Hello!"  # this changes the list value. shit editting cheese affects spam use copy.copy()
print(spam)
print(cheese)

# Identity and the id() Function
id("Howdy")  # the number returned will be different on your machine
bacon = "Hello"
id(bacon)

# mutability of list and how it affects the python reference id of the list
eggs = ["cat", "dog"]  # this creates a new list
print(id(eggs))
eggs.append("moose")  # append() modifies the list "in place".
print(id(eggs))  # eggs still refers to the same list as before.
print(eggs)
eggs = ["bat", "rat", "cow"]  # this creates a new list
print(id(eggs))  # eggs now refers to a completely different list.
print(eggs)
