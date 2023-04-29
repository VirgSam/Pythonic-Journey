name = ""
while not name:
    print("Enter your name")
    name = input()
print("How many guests will you have?")
numOfGuests = int(input())
if numOfGuests:
    print(f"Be sure to have enough room for all {numOfGuests} of your guests")
