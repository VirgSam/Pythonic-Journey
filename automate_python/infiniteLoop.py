# while True:
#     print('Hello, world!')
# ctrl+c does work on the VSCode editor or terminal to terminate the infinite loop

# using the break and the continue statments,
# the continue statement causes the program execution to jump back to the start of the loop
# the break statement terminates execution out of the while loop

while True:
    print("Who are you?")
    name = input()
    if name != "Joe":
        continue
    print("Hello, Joe. What is the password? (is it a fish.)")
    password = input()
    if password == "swordfish":
        break
print("Access Granted")
