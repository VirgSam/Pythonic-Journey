# The in and not in Operators
"howdy" in ["hello", "hi", "howdy", "heyas"]
spam = ["hello", "hi", "howdy", "heyas"]
"cat" in spam
"howdy" not in spam
"cat" not in spam

mypets = ["Zoe", "Pooka", "fat-tail"]
print("Enter a pet name: ")
name = input()
if name not in mypets:
    print("I do not have a pet named " + name)
else:
    print(name + " is my pet.")
